import logging
from typing import Optional
from fuzzywuzzy import fuzz

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import Muzzle, Barrel, Optic, Underbarrel, Ammunition, RearGrip, Stock, Perk, Laser
from model.weapon.impl.assault_rifle import AssaultRifle
from model.weapon.impl.light_machine_gun import LightMachineGun
from model.weapon.impl.marksman_rifle import MarksmanRifle
from model.weapon.impl.pistol import Pistol
from model.weapon.impl.shotgun import Shotgun
from model.weapon.impl.sniper_rifle import SniperRifle
from model.weapon.impl.submachine_gun import SubmachineGun
from model.weapon.impl.tactical_rifle import TacticalRifle
from model.weapon.weapon import Weapon

TEST_COMMAND = "!kilo"
TEST_RESPONSE = "@[user] Kilo: Monolithic Suppressor, Singuard 19.8, VLK/Holo (blue dot), Commando Foregrip, 60 Round Mags"

DELIMITERS = [",", "-", "|"]
MIN_ATTACHMENTS = 4
MAX_ATTACHMENTS = 5

ALL_WEAPONS = list(AssaultRifle) + list(LightMachineGun) + list(MarksmanRifle) + list(Pistol) + list(Shotgun) + \
              list(SniperRifle) + list(SubmachineGun) + list(TacticalRifle)

ALL_ATTACHMENTS = list(Muzzle) + list(Barrel) + list(Underbarrel) + list(Optic) + list(Ammunition) + \
                  list(RearGrip) + list(Stock) + list(Perk) + list(Laser)


def main():
    db = JSONDatabaseEngine()
    players = db.select_players()

    for player in players:
        print(player.username + "-" * 20)
        for command, response in player.commands.items():
            update_command(command, response)


def update_command(command: str, response: str) -> bool:
    weapon = _find_weapon(command)

    if weapon is None:
        return False

    # TODO: check if current source changed

    attachments = _find_attachments(weapon, response)

    if len(attachments) < MIN_ATTACHMENTS:
        return False

    print(f"{command}: {response}")
    print(f"\t-> {[str(a) for a in attachments]}")

    return True


def _find_weapon(command: str) -> Optional[Weapon]:
    for weapon in ALL_WEAPONS:
        if any([alias in command for alias in weapon.aliases]):
            return weapon


def _find_attachments(weapon: Weapon, response: str) -> list:
    delimiter = _find_delimiter(response)
    parts = response.split(delimiter)

    if len(parts) < MIN_ATTACHMENTS:
        return []

    attachments = []

    for part in parts:

        if part == "":
            continue

        part = part.strip().lower()
        matched = (None, None)

        for attachment in ALL_ATTACHMENTS:

            if attachment.game != weapon.game:
                continue

            for alias in attachment.aliases:
                ratio = fuzz.partial_ratio(part, alias)

                current_ratio = matched[1] if matched[1] is not None else 0
                if ratio > current_ratio:
                    matched = attachment, ratio

                # TODO: break outer if 100

        attachments.append(matched[0])

    return attachments


def _find_delimiter(response: str) -> str:
    return max(DELIMITERS, key=lambda delimiter: response.count(delimiter))


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    # update_command(TEST_COMMAND, TEST_RESPONSE)
    main()
