from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import *
from model.player import Player
from model.weapon import Weapon


USERNAME = "cloakzy"
LOADOUT = "MAC-10"
ORIGIN = "CW"
SOURCE = "https://bit.ly/31oYMFu"
COMMAND, MESSAGE = (None, "")
ATTACHMENTS = [
    # Muzzle.INFANTRY_COMPENSATOR_CW,
    Barrel.EXTENDED_BARREL_CW,
    # Laser.MW_LASER_5,
    Optic.MILLSTOP_REFLEX_CW,
    Stock.WIRE_STOCK,
    # Underbarrel.FIELD_AGENT_CW,
    Ammunition.STANAG_CW,
    RearGrip.SASR_JUNGLE,
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
        player.last_updated = datetime.now().isoformat()
        player.loadouts[LOADOUT] = {
            "origin": ORIGIN,
            "source": SOURCE,
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
