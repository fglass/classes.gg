from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import *
from model.weapon import Weapon

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    player = db.select_player("vikkstar123")

    loadout = Weapon.BRUEN.value
    source = "https://www.youtube.com/watch?v=yvM_EWcIv5A"
    last_updated = datetime.now().isoformat()
    attachments = [
        Muzzle.MONOLITHIC_SUPPRESSOR,
        Barrel.XRK_SUMMIT,
        Laser.TAC_LASER,
        Optic.VLK_3X_OPTIC,
        # Underbarrel.MERC_FOREGRIP,
        # Stock.FTAC_COLLAPSIBLE,
        Ammunition.ROUND_MAGS_60,
        # RearGrip.STIPPLED_GRIP_TAPE,
        # Perk.SLEIGHT_OF_HAND,
    ]

    # player.commands["!mp5"] = "@{touser.name} https://clips.twitch.tv/AwkwardVainBottleDxAbomb"

    player.loadouts[loadout] = {
        "source": source,
        "lastUpdated": last_updated,
        "attachments": {attachment.get_type(): attachment.value for attachment in attachments}
    }

    db.add_player(player)
    print(f"Added {player.username}'s {loadout}")

