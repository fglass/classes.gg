from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import *
from model.player import Player
from model.weapon import Weapon


USERNAME = "teepee"
LOADOUT = "MAC-10 Fast"  # str(Weapon.MAC_10)
GAME = Game.COLD_WAR
SOURCE = "https://tinyurl.com/teepeeattachments"
COMMAND, MESSAGE = (None, "")
ATTACHMENTS = [
    Muzzle.AGENCY_SUPPRESSOR,
    Barrel.TASK_FORCE_59,
    # Laser.TIGER_TEAM_SPOTLIGHT,
    # Optic.HAWKSMOOR,
    # Stock.RAIDER_STOCK,
    Underbarrel.PATROL_FOREGIP,
    Ammunition.SALVO_53,
    RearGrip.SASR_JUNGLE,
    # Perk.SLEIGHT_OF_HAND,
    # TriggerAction.LIGHTWEIGHT_TRIGGER
]


def _add_loadout():
    db = JSONDatabaseEngine()
    player = db.select_player(USERNAME)
    attachments = {attachment.get_type(): str(attachment) for attachment in ATTACHMENTS}

    _print_validation(player, attachments)
    confirmation = input("Confirm? ")

    if confirmation == "y":
        player.last_updated = datetime.now().isoformat()
        player.loadouts[LOADOUT] = {
            "game": GAME.value,
            "source": SOURCE,
            "attachments": attachments
        }

        if COMMAND:
            player.commands[COMMAND] = MESSAGE

        db.add_player(player)
        print(f"Added {player.username}'s {GAME.value} {LOADOUT}")


def _print_validation(player: Player, attachments: dict):
    print(f"{player.username}'s {GAME.value} {LOADOUT}:")

    if LOADOUT in player.loadouts:
        previous_attachments = list(player.loadouts[LOADOUT]["attachments"].values())
        sorted_keys = sorted(attachments)
        [print(f"\t{previous_attachments[i]} -> {attachments[sorted_keys[i]]}") for i in range(5)]
    else:
        [print(f"\t{attachment}") for attachment in attachments.values()]

    if COMMAND:
        print(f"{COMMAND}: {MESSAGE}")

    print("-" * 15)


if __name__ == '__main__':
    _add_loadout()
