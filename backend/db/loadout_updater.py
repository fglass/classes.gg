import collections
import logging
import requests
import time
from datetime import datetime
from typing import Optional, Tuple, Dict
from fuzzywuzzy import fuzz
from model.command.command_source import CommandSource
from db.admin.change.detect_changes import SHEETS_KEY
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
        self.recent_updates = collections.deque(maxlen=100)

    def run(self):
        start_s = time.time()

        players = db.select_players()
        previous_loadouts = {player.username: player.loadouts.copy() for player in players}

        [self._update_player(player) for player in players]
        update_count = self._save_changes(previous_loadouts)

        elapsed_s = time.time() - start_s
        logging.info(f"{update_count} loadouts updated in {elapsed_s:.2f}s")

    def _update_player(self, player: Player):
        logging.debug(player.username)

        if player.command_source:
            self._update_commands(player)

        if player.spreadsheet:
            self._update_spreadsheet(player)

    def _save_changes(self, previous_loadouts: dict) -> int:
        update_count = 0

        for player in db.select_players():
            for weapon, loadout in player.loadouts.items():

                previous_loadout = previous_loadouts[player.username].get(weapon, {})
                is_updated = loadout["source"] != previous_loadout.get("source")

                if is_updated:
                    self.recent_updates.append(_to_update_view_model(player, weapon, loadout))
                    player.last_updated = loadout["lastUpdated"]
                    update_count += 1

            db.add_player(player, save=False)

        db.save()
        return update_count

    def _update_commands(self, player: Player):
        source = CommandSource(player.command_source)
        source_url = f"https://www.twitch.tv/{player.username.lower()}"

        current_commands = source.query(player)

        for weapon in ALL_WEAPONS:
            for command in weapon.aliases:

                response = current_commands[command] if command in current_commands else current_commands.get("!" + command)

                if response is not None:
                    self._update_loadout(player, command, response, source_url)

    def _update_spreadsheet(self, player: Player):
        for rows, source_url in _parse_spreadsheets(player.spreadsheet):
            for row in reversed(rows):
                self._update_loadout(player, command=row, response=row, source_url=source_url)

    def _update_loadout(self, player: Player, command: str, response: str, source_url: str):
        loadout = _find_loadout(command, response)

        if loadout is None:
            return

        weapon, attachments = loadout
        now = datetime.utcnow().isoformat()

        player.loadouts[str(weapon)] = {
            "attachments": {a.get_class_name(): str(a) for a in attachments.keys()},
            "game": weapon.game.value,
            "lastUpdated": now,
            "source": response,
            "sourceUrl": source_url,
        }

        logging.debug(f"\t{command}: {response}")
        logging.debug(f"\t\t-> {str(weapon)} ({weapon.game.value}): {[f'{str(a)} {r}%' for a, r in attachments.items()]}")


def _parse_spreadsheets(spreadsheet_meta: dict) -> tuple:
    for sheet in spreadsheet_meta[SHEETS_KEY]:
        key = spreadsheet_meta["id"]
        export_url = f"https://docs.google.com/spreadsheets/d/{key}/export?format=csv&gid={sheet}"
        response = requests.get(export_url)
        content = response.content.decode("utf-8")
        yield content.splitlines(), export_url.replace("/export", "")


def _find_loadout(command: str, response: str) -> Optional[Tuple[Weapon, dict]]:
    weapon = find_weapon(command.lower())

    if weapon is None:
        logging.debug(f"\tWeapon not found: {command}")
        return

    if len(weapon.attachments) == 0:
        logging.debug(f"\t{weapon} data missing")

    attachments = _find_attachments(weapon, response)

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


def _find_attachments(weapon: Weapon, response: str) -> dict:  # TODO: one per attachment category?
    attachments = {}

    response = _slice_response_if_dual_game(weapon, response)
    sequences = _split_by_delimiter(response)
    sequences = _split_on_token(sequences, " and ")
    sequences = _split_on_token(sequences, " & ")

    if len(sequences) > MAX_SEQUENCES or len(sequences) < MIN_ATTACHMENTS:
        return attachments

    for sequence in reversed(sequences):

        attachment, ratio = _find_attachment(sequence, weapon.attachments)

        if attachment is not None:
            attachments[attachment] = ratio

        if len(attachments) == MAX_ATTACHMENTS:
            break

    return attachments


def _slice_response_if_dual_game(weapon: Weapon, response: str) -> str:
    if weapon in DUAL_GAME_WEAPONS and "MW" in response and "CW" in response:
        index = max(response.index("MW"), response.index("CW"))
        response = response[:index]
    return response


def _split_by_delimiter(response: str) -> list:
    delimiter = _find_delimiter(response)
    return response.split(delimiter)


def _find_delimiter(response: str) -> str:
    return max(DELIMITERS, key=lambda delimiter: response.count(delimiter))


def _split_on_token(sequences: list, token: str) -> list:
    new_sequences = []

    for sequence in sequences:
        parts = sequence.split(token)
        new_sequences.extend(parts)

    return new_sequences


def _find_attachment(sequence: str, valid_attachments: list) -> Tuple[Optional[Attachment], int]:
    if sequence == "":
        return None, 0

    sequence = sequence.strip().lower()
    matched_attachment = None
    max_ratio = 0

    for attachment in valid_attachments:
        for alias in attachment.aliases:

            if alias == sequence:  # Exact match
                return attachment, 100

            ratio = fuzz.partial_ratio(sequence, alias)

            if ratio >= max_ratio:

                is_same_ratio = ratio == max_ratio
                has_shorter_name = len(str(attachment)) < len(str(matched_attachment or ""))

                if is_same_ratio and has_shorter_name:
                    continue

                matched_attachment = attachment
                max_ratio = ratio

    if max_ratio < RATIO_THRESHOLD:
        return None, 0

    return matched_attachment, max_ratio


def _compare_weapon_counterpart(weapon: Weapon, attachments: dict, response: str):
    weapon_counterpart = DUAL_GAME_WEAPONS[weapon]
    other_attachments = _find_attachments(weapon_counterpart, response)

    if len(other_attachments) >= len(attachments):
        first_total = sum(attachments.values())
        second_total = sum(other_attachments.values())

        if second_total > first_total:
            return weapon_counterpart, other_attachments

    return weapon, attachments


def _to_update_view_model(player: Player, weapon: str, loadout: dict) -> dict:
    return {
        "attachments": loadout["attachments"],
        "game": loadout["game"],
        "lastUpdated": loadout["lastUpdated"],
        "source": loadout["source"],
        "sourceUrl": loadout["sourceUrl"],
        "username": player.username,
        "weapon": weapon
    }


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    LoadoutUpdater().run()
