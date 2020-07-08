from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import *
from model.weapon import Weapon

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    player = db.select_player("huskerrs")

    loadout = Weapon.AK_47.value
    source = "https://tinyurl.com/huskloadout"
    last_updated = datetime.now().isoformat()
    attachments = [
        Muzzle.MONOLITHIC_SUPPRESSOR,
        Barrel.RPK_BARREL,
        Laser.TAC_LASER,
        Underbarrel.COMMANDO_FOREGRIP,
        Ammunition.NATO_ROUND_MAGS
    ]

    player.commands["!m4"] = "Nade's M4 Class -> Monolithic Suppressor, Commando Foregrip, Stock M16 Grenadier Barrel, 60 Round Mag, Tac Laser"

    # Post-process
    attachments.sort(key=lambda attachment: attachment.value)
    attachments = {attachment.get_type(): attachment.value for attachment in attachments}

    player.loadouts[source] = {
        "source": source,
        "lastUpdated": last_updated,
        "attachments": attachments
    }

    db.add_player(player)
    print(f"Added {player.username}'s {source}")

