from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import *
from model.weapon import Weapon

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    player = db.select_player("tfue")

    loadout = Weapon.BRUEN.value
    source = "https://clips.twitch.tv/StylishMagnificentShingleAMPTropPunch"
    last_updated = datetime.now().isoformat()
    attachments = [
        Muzzle.MONOLITHIC_SUPPRESSOR,
        Barrel.XRK_SUMMIT,
        # Laser.MW_LASER_5,
        Optic.VLK_3X_OPTIC,
        # Stock.FTAC_COLLAPSIBLE,
        Underbarrel.COMMANDO_FOREGRIP,
        Ammunition.ROUND_MAGS_60,
        # RearGrip.STIPPLED_GRIP_TAPE,
        # Perk.AKIMBO,
        # TriggerAction.LIGHTWEIGHT_TRIGGER
    ]

    player.commands["!bruen"] = "https://clips.twitch.tv/StylishMagnificentShingleAMPTropPunch?tt_medium=twtr"

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
