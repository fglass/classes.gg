from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import *
from model.weapon import Weapon

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    player = db.select_player("mutex")

    loadout = Weapon.KAR98K.value
    source = "https://www.twitch.tv/mutex"
    last_updated = datetime.now().isoformat()
    attachments = [
        Muzzle.MONOLITHIC_SUPPRESSOR,
        Barrel.SINGUARD_CUSTOM_276,
        Laser.TAC_LASER,
        Optic.VARIABLE_ZOOM_SCOPE,
        Stock.STVOL_PRECISION_COMB,
        # Underbarrel.MERC_FOREGRIP,
        # Ammunition.ROUND_MAGS_45,
        # RearGrip.STIPPLED_GRIP_TAPE,
        # Perk.SLEIGHT_OF_HAND,
        # TriggerAction.LIGHTWEIGHT_TRIGGER
    ]

    player.commands["!sniper"] = "[user] Kar98 - Muzzle - Monolithic Suppressor , Barrel - Siinguard Custom 27.6\" , Laser- Tac Laser , Optic - Variable Zoom Scope , Stock - STVOL Precision Comb"

    attachments = {attachment.get_type(): attachment.value for attachment in attachments}

    print(f"{loadout}:")
    if loadout in player.loadouts:
        previous_attachments = list(player.loadouts[loadout]["attachments"].values())
        sorted_keys = sorted(attachments)
        [print(f"\t{previous_attachments[i]} -> {attachments[sorted_keys[i]]}") for i in range(5)]
    else:
        [print(f"\t{attachment}") for attachment in attachments.values()]

    confirmation = input("Confirm? ")

    if confirmation == "y":
        player.loadouts[loadout] = {
            "source": source,
            "lastUpdated": last_updated,
            "attachments": attachments
        }
        db.add_player(player)
        print(f"Added {player.username}'s {loadout}")
