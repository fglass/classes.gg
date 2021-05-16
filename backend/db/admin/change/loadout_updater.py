import logging
import requests
from datetime import datetime
from typing import Optional, Tuple, Dict
from fuzzywuzzy import fuzz
from db.admin.change.command_source import CommandSource
from db.admin.change.detect_changes import SOURCE_KEY, ALL_COMMANDS, SHEETS_KEY
from db.json_database_engine import JSONDatabaseEngine
from model.player import Player
from model.weapon.new_attachment import *
from model.weapon.weapon import Weapon, AssaultRifle, LightMachineGun, MarksmanRifle, Pistol, Shotgun, SniperRifle, \
    SubmachineGun, TacticalRifle

DELIMITERS = [",", "-", "|"]
MIN_ATTACHMENTS = 4
MAX_ATTACHMENTS = 5
RATIO_THRESHOLD = 60

ALL_WEAPONS = list(AssaultRifle) + list(LightMachineGun) + list(MarksmanRifle) + list(Pistol) + list(Shotgun) + \
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

    def run(self):
        self._success_count, self._failure_count = 0, 0
        db = JSONDatabaseEngine()

        for player in db.select_players():
            self._update_player(player)
            db.add_player(player, commit=False)

        db.commit()
        logging.info(f"Loadouts updated: {self._success_count} ✔ {self._failure_count} ❌")

    def _update_player(self, player: Player):  # TODO: check previous
        print(player.username)

        if player.spreadsheet:
            self._update_spreadsheet(player)

        source_name = player.commands.get(SOURCE_KEY)

        if source_name:
            self._update_commands(player, source_name)

    def _update_spreadsheet(self, player: Player):
        for entries in _parse_spreadsheets(player.spreadsheet):
            for entry in entries:
                self._update_loadout(player, command=entry, response=entry, source_url="TODO")  # TODO: source url

    def _update_commands(self, player: Player, source_name: str):
        source = CommandSource(source_name)
        source_url = f"https://www.twitch.tv/{player.username.lower()}"

        current_commands = source.query(player)

        for command in WEAPON_COMMANDS:

            response = current_commands[command] if command in current_commands else current_commands.get("!" + command)

            if response is not None:
                self._update_loadout(player, command, response, source_url)

    def _update_loadout(self, player: Player, command: str, response: str, source_url: str):
        loadout = _find_loadout(command, response)

        if loadout is None:
            self._failure_count += 1
            return

        now = datetime.now().isoformat()
        weapon, attachments = loadout

        player.last_updated = now
        player.loadouts[str(weapon)] = {
            "attachments": {a.__class__.__name__: str(a) for a in attachments.keys()},
            "game": weapon.game.value,
            "lastUpdated": now,
            "source": response,
            "sourceUrl": source_url,
        }

        print(f"\t{command}: {response}")
        print(f"\t\t-> {str(weapon)} ({weapon.game.value}): {[f'{str(a)} {r}%' for a, r in attachments.items()]}")
        self._success_count += 1


def _parse_spreadsheets(spreadsheet_meta: dict) -> list:
    for sheet in spreadsheet_meta[SHEETS_KEY]:
        key = spreadsheet_meta["id"]
        export_url = f"https://docs.google.com/spreadsheets/d/{key}/export?format=csv&gid={sheet}"
        response = requests.get(export_url)
        lines = response.content.decode("utf-8").splitlines()
        yield lines


def _find_loadout(command: str, response: str) -> Optional[Tuple[Weapon, dict]]:
    weapon = find_weapon(command.lower())

    if weapon is None:
        print(f"\tWeapon not found: {command}")
        return

    if len(weapon.attachments) == 0:
        print(f"\t{weapon} data missing")

    attachments = _find_attachments(weapon.attachments, response)

    if weapon in DUAL_GAME_WEAPONS:
        weapon, attachments = _compare_weapon_counterpart(weapon, attachments, response)

    if len(attachments) < MIN_ATTACHMENTS:
        return

    return weapon, attachments


def find_weapon(command: str) -> Optional[Weapon]:
    for weapon in ALL_WEAPONS:
        if any([alias in command for alias in weapon.aliases]):
            return weapon


def _find_attachments(valid_attachments: list, response: str) -> dict:
    attachments = {}
    delimiter = _find_delimiter(response)
    parts = response.split(delimiter)

    if len(parts) < MIN_ATTACHMENTS:
        return attachments

    for part in reversed(parts):  # TODO: check part isn't weapon

        attachment, ratio = _find_attachment(part, valid_attachments)

        if attachment is not None:
            attachments[attachment] = ratio

        if len(attachments) == MAX_ATTACHMENTS:
            break

    return attachments


def _find_delimiter(response: str) -> str:
    return max(DELIMITERS, key=lambda delimiter: response.count(delimiter))


def _find_attachment(part: str, valid_attachments: list) -> Tuple[Optional[NewAttachment], int]:
    if part == "":
        return None, 0

    part = part.strip().lower()
    matched_attachment = None
    max_ratio = 0

    for attachment in valid_attachments:

        if part == str(attachment).lower():
            return attachment, 100

        for alias in attachment.aliases:
            ratio = fuzz.partial_ratio(part, alias)

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


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    LoadoutUpdater().run()
