import collections
import logging
import requests
import time
from datetime import datetime
from typing import Optional, Tuple, Dict
from fuzzywuzzy import fuzz
from model.command.command_source import CommandSource
from db.admin.change.detect_changes import ALL_COMMANDS, SHEETS_KEY
from db.json_database_engine import db
from model.player import Player
from model.weapon.attachment import *
from model.weapon.weapon import Weapon, AssaultRifle, LightMachineGun, MarksmanRifle, Handgun, Shotgun, SniperRifle, \
    SubmachineGun, TacticalRifle

DELIMITERS = [",", "-", "|"]
COMMAND_TRIM_THRESHOLD = 20
MAX_SEQUENCES = 20
MIN_ATTACHMENTS = 4
MAX_ATTACHMENTS = 5
RATIO_THRESHOLD = 60

ALL_WEAPONS = list(AssaultRifle) + list(LightMachineGun) + list(MarksmanRifle) + list(Handgun) + list(Shotgun) + \
              list(SniperRifle) + list(SubmachineGun) + list(TacticalRifle)

WEAPON_COMMANDS = set(ALL_COMMANDS)  # TODO: use weapon aliases instead
[WEAPON_COMMANDS.remove(c) for c in {"class", "guns", "loadout", "loadout2", "loadouts"}]

DUAL_GAME_WEAPONS: Dict[Weapon, Weapon] = {
    AssaultRifle.AK_47: AssaultRifle.AK_47_CW,
    AssaultRifle.AK_47_CW: AssaultRifle.AK_47,
    SubmachineGun.MP5: SubmachineGun.MP5_CW,
    SubmachineGun.MP5_CW: SubmachineGun.MP5,
    SubmachineGun.AUG: TacticalRifle.AUG_CW,
    TacticalRifle.AUG_CW: SubmachineGun.AUG,
    AssaultRifle.M4A1: AssaultRifle.XM4,
    AssaultRifle.XM4: AssaultRifle.M4A1
}


class LoadoutUpdater:

    def __init__(self):
        self._success_count = 0
        self._failure_count = 0
        self.recent_updates = collections.deque(maxlen=100)

    def run(self):
        self._success_count, self._failure_count = 0, 0
        start = time.time()

        for player in db.select_players():
            self._update_player(player)
            db.add_player(player, commit=False)

        db.commit()
        elapsed = time.time() - start
        logging.info(f"{self._success_count} loadouts updated in {elapsed:.2f}s ({self._failure_count} ignored)")

    def _update_player(self, player: Player):
        logging.debug(player.username)

        if player.command_source:
            self._update_commands(player)

        if player.spreadsheet:
            self._update_spreadsheet(player)

    def _update_commands(self, player: Player):
        source = CommandSource(player.command_source)
        source_url = f"https://www.twitch.tv/{player.username.lower()}"

        current_commands = source.query(player)

        for command in WEAPON_COMMANDS:

            response = current_commands[command] if command in current_commands else current_commands.get("!" + command)

            if response is not None:
                self._update_loadout(player, command, response, source_url)

    def _update_spreadsheet(self, player: Player):
        for rows, source_url in _parse_spreadsheets(player.spreadsheet):
            for row in rows:
                self._update_loadout(player, command=row, response=row, source_url=source_url)  # TODO: split command

    def _update_loadout(self, player: Player, command: str, response: str, source_url: str):
        loadout = _find_loadout(player, command, response)

        if loadout is None:
            self._failure_count += 1
            return

        now = datetime.utcnow().isoformat()
        weapon, attachments = loadout

        player.last_updated = now
        player.loadouts[str(weapon)] = {
            "attachments": {a.get_class_name(): str(a) for a in attachments.keys()},
            "game": weapon.game.value,
            "lastUpdated": now,
            "source": response,
            "sourceUrl": source_url,
        }

        logging.debug(f"\t{command}: {response}")
        logging.debug(f"\t\t-> {str(weapon)} ({weapon.game.value}): {[f'{str(a)} {r}%' for a, r in attachments.items()]}")

        self._success_count += 1
        self.recent_updates.append(
            _to_recent_update_view_model(now, player, command, response, source_url, weapon, attachments)
        )


def _parse_spreadsheets(spreadsheet_meta: dict) -> tuple:
    for sheet in spreadsheet_meta[SHEETS_KEY]:
        key = spreadsheet_meta["id"]
        export_url = f"https://docs.google.com/spreadsheets/d/{key}/export?format=csv&gid={sheet}"
        response = requests.get(export_url)
        content = response.content.decode("utf-8")
        yield content.splitlines(), export_url.replace("/export", "")


def _find_loadout(player: Player, command: str, response: str) -> Optional[Tuple[Weapon, dict]]:
    weapon = find_weapon(command.lower())

    if weapon is None:
        logging.debug(f"\tWeapon not found: {command}")
        return

    if len(weapon.attachments) == 0:
        logging.debug(f"\t{weapon} data missing")

    existing_loadout = player.loadouts.get(str(weapon), {})
    if existing_loadout.get("source") == response:
        return  # TODO: not failure

    attachments = _find_attachments(weapon.attachments, response)

    if weapon in DUAL_GAME_WEAPONS:
        weapon, attachments = _compare_weapon_counterpart(weapon, attachments, response)

    if len(attachments) < MIN_ATTACHMENTS:
        return

    return weapon, attachments


def find_weapon(command: str) -> Optional[Weapon]:
    if len(command) > COMMAND_TRIM_THRESHOLD:
        command = command[:COMMAND_TRIM_THRESHOLD]

    for weapon in ALL_WEAPONS:
        if any([alias in command for alias in weapon.aliases]):
            return weapon


def _find_attachments(valid_attachments: list, response: str) -> dict:  # TODO: one per attachment category
    attachments = {}
    delimiter = _find_delimiter(response)
    sequences = response.split(delimiter)

    if len(sequences) > MAX_SEQUENCES or len(sequences) < MIN_ATTACHMENTS:
        return attachments

    for sequence in reversed(sequences):  # TODO: check part isn't weapon

        attachment, ratio = _find_attachment(sequence, valid_attachments)

        if attachment is not None:
            attachments[attachment] = ratio

        if len(attachments) == MAX_ATTACHMENTS:
            break

    return attachments


def _find_delimiter(response: str) -> str:
    return max(DELIMITERS, key=lambda delimiter: response.count(delimiter))


def _find_attachment(sequence: str, valid_attachments: list) -> Tuple[Optional[Attachment], int]:
    if sequence == "":
        return None, 0

    sequence = sequence.strip().lower()
    matched_attachment = None
    max_ratio = 0

    for attachment in valid_attachments:

        if sequence == str(attachment).lower():
            return attachment, 100

        for alias in attachment.aliases:
            ratio = fuzz.partial_ratio(sequence, alias)

            if ratio >= max_ratio:
                matched_attachment = attachment
                max_ratio = ratio

    if max_ratio < RATIO_THRESHOLD:
        return None, 0

    return matched_attachment, max_ratio


def _compare_weapon_counterpart(weapon: Weapon, attachments: dict, response: str):
    weapon_counterpart = DUAL_GAME_WEAPONS[weapon]
    other_attachments = _find_attachments(weapon_counterpart.attachments, response)

    if len(other_attachments) >= len(attachments):
        first_total = sum(attachments.values())
        second_total = sum(other_attachments.values())

        if second_total > first_total:
            return weapon_counterpart, other_attachments

    return weapon, attachments


def _to_recent_update_view_model(
    timestamp: str,
    player: Player,
    command: str,
    response: str,
    source_url: str,
    weapon: Weapon,
    attachments: dict
) -> dict:
    return {
        "attachments": [f"{a.name} {r}%" for a, r in attachments.items()],
        "command": command if command != response else None,
        "response": response,
        "timestamp": timestamp,
        "source": source_url,
        "username": player.username,
        "weapon": weapon.name
    }


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    LoadoutUpdater().run()
