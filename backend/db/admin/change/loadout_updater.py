import logging
from typing import Optional, Tuple
from fuzzywuzzy import fuzz
from db.admin.change.command_source import CommandSource
from db.admin.change.detect_changes import SOURCE_KEY, ALL_COMMANDS
from db.json_database_engine import JSONDatabaseEngine
from model.weapon.new_attachment import *
from model.weapon.weapon import Weapon, AssaultRifle, LightMachineGun, MarksmanRifle, Pistol, Shotgun, SniperRifle, \
    SubmachineGun, TacticalRifle

DELIMITERS = [",", "-", "|"]
MIN_ATTACHMENTS = 4
MAX_ATTACHMENTS = 5
RATIO_THRESHOLD = 50

ALL_WEAPONS = list(AssaultRifle) + list(LightMachineGun) + list(MarksmanRifle) + list(Pistol) + list(Shotgun) + \
              list(SniperRifle) + list(SubmachineGun) + list(TacticalRifle)

WEAPON_COMMANDS = set(ALL_COMMANDS)  # TODO: use weapon aliases
[WEAPON_COMMANDS.remove(c) for c in {"class", "guns", "loadout", "loadout2", "loadouts"}]


def update_loadouts():
    db = JSONDatabaseEngine()
    players = db.select_players()

    success_count, failure_count = 0, 0

    for player in players:
        previous_commands = player.commands
        source_name = previous_commands.pop(SOURCE_KEY, None)

        if not source_name:
            continue

        print(player.username)
        source = CommandSource(source_name)
        current_commands = source.query(player)

        for command in WEAPON_COMMANDS:

            response = current_commands[command] if command in current_commands else current_commands.get("!" + command)

            if response is None:
                continue

            updated = update_command(command, response)

            if updated:
                success_count += 1
            else:
                failure_count += 1

    logging.info(f"Loadouts updated: {success_count} ✔ {failure_count} ❌")


def update_command(command: str, response: str) -> bool:
    weapon = find_weapon(command)  # TODO: retry if cold war counterpart

    if weapon is None:
        print(f"\tWeapon not found: {command}")
        return False

    if len(weapon.attachments) == 0:
        print(f"\t{weapon} data missing")
        return False

    attachments = _find_attachments(weapon.attachments, response)

    if len(attachments) < MIN_ATTACHMENTS:
        return False

    # print(f"\t{command}: {response}")
    # print(f"\t\t-> {[f'{str(a)} {r}%' for a, r in attachments.items()]}")
    return True


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

    for part in parts:

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

    if max_ratio < 100:
        print("\t" + part, "->", str(matched_attachment), max_ratio)  # TODO: fix these

    return matched_attachment, max_ratio


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    update_loadouts()
