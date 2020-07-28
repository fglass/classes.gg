from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import *
from model.player import Player
from model.weapon import Weapon


USERNAME = "maven"
LOADOUT = Weapon.MP5.value
SOURCE = "https://docs.google.com/spreadsheets/d/11m240tfs_BI-bXVitV9iAVy4KzNWOT4NLObBu1jr0wE/edit?usp=sharing"
COMMAND, MESSAGE = (None, "")
ATTACHMENTS = [
    # Muzzle.MONOLITHIC_SUPPRESSOR,
    Barrel.MONOLITHIC_INTEGRAL_SUPPRESSOR,
    Laser.MW_LASER_5,
    # Optic.VLK_3X_OPTIC,
    Stock.FTAC_COLLAPSIBLE,
    Underbarrel.MERC_FOREGRIP,
    Ammunition.ROUND_MAGS_45,
    # RearGrip.RUBBERIZED_GRIP_TAPE,
    # Perk.SLEIGHT_OF_HAND,
    # TriggerAction.LIGHTWEIGHT_TRIGGER
]


def _add_loadout():
    db = JSONDatabaseEngine()
    player = db.select_player(USERNAME)
    attachments = {attachment.get_type(): attachment.value for attachment in ATTACHMENTS}

    _print_validation(player, attachments)
    confirmation = input("Confirm? ")

    if confirmation == "y":
        player.loadouts[LOADOUT] = {
            "source": SOURCE,
            "lastUpdated": datetime.now().isoformat(),
            "attachments": attachments
        }

        if COMMAND:
            player.commands[COMMAND] = MESSAGE

        db.add_player(player)
        print(f"Added {player.username}'s {LOADOUT}")


def _print_validation(player: Player, attachments: dict):
    print(f"{player.username}'s {LOADOUT}:")

    if LOADOUT in player.loadouts:
        previous_attachments = list(player.loadouts[LOADOUT]["attachments"].values())
        sorted_keys = sorted(attachments)
        [print(f"\t{previous_attachments[i]} -> {attachments[sorted_keys[i]]}") for i in range(5)]
    else:
        [print(f"\t{attachment}") for attachment in attachments.values()]

    print(f"{COMMAND}: {MESSAGE}")
    print("-" * 15)


if __name__ == '__main__':
    _add_loadout()
