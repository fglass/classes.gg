import logging
from typing import Optional, Tuple
from fuzzywuzzy import fuzz

from db.admin.change.command_source import CommandSource
from db.admin.change.detect_changes import SOURCE_KEY, ALL_COMMANDS
from db.json_database_engine import JSONDatabaseEngine
from model.weapon.impl.assault_rifle import AssaultRifle
from model.weapon.impl.light_machine_gun import LightMachineGun
from model.weapon.impl.marksman_rifle import MarksmanRifle
from model.weapon.impl.pistol import Pistol
from model.weapon.impl.shotgun import Shotgun
from model.weapon.impl.sniper_rifle import SniperRifle
from model.weapon.impl.submachine_gun import SubmachineGun
from model.weapon.impl.tactical_rifle import TacticalRifle
from model.weapon.new_attachment import *
from model.weapon.weapon import Weapon

TEST_COMMAND = "!kilo"
TEST_RESPONSE = "@[user] Kilo: Monolithic Suppressor, Singuard 19.8, VLK/Holo (blue dot), Commando Foregrip, 60 Round Mags"

DELIMITERS = [",", "-", "|"]
MIN_ATTACHMENTS = 4
MAX_ATTACHMENTS = 5

ALL_WEAPONS = list(AssaultRifle) + list(LightMachineGun) + list(MarksmanRifle) + list(Pistol) + list(Shotgun) + \
              list(SniperRifle) + list(SubmachineGun) + list(TacticalRifle)


def update():
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

        for command in ALL_COMMANDS:

            response = current_commands.get(command)

            if response is None:
                response = current_commands.get("!" + command)

            if response is None:
                continue

            updated = update_command(command, response)

            if updated:
                success_count += 1
            else:
                failure_count += 1

    print(f"Loadouts updated: {success_count} success, {failure_count} failure")


def update_command(command: str, response: str) -> bool:  # TODO: retry if cold war counterpart
    weapon = find_weapon(command)

    if weapon is None:
        return False

    if len(weapon.attachments) == 0:
        print(f"\t{weapon} data missing")
        return False

    attachments = _find_attachments(weapon.attachments, response)

    if len(attachments) < MIN_ATTACHMENTS:
        return False

    print(f"\t{command}: {response}")
    print(f"\t\t-> {[f'{str(a)} {r}%' for a, r in attachments.items()]}")
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

            if ratio > max_ratio:
                matched_attachment = attachment
                max_ratio = ratio

    return matched_attachment, max_ratio


def _find_delimiter(response: str) -> str:
    return max(DELIMITERS, key=lambda delimiter: response.count(delimiter))


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    # update_command(TEST_COMMAND, TEST_RESPONSE)
    update()
