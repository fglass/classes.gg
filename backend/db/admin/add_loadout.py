from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import *
from model.weapon import Weapon

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    player = db.select_player("teepee")

    loadout = Weapon.PP19_BIZON.value
    source = "https://tinyurl.com/teepeeattachments"
    last_updated = datetime.now().isoformat()
    attachments = [
        Muzzle.MONOLITHIC_SUPPRESSOR,
        Barrel.STEEL,
        Laser.TAC_LASER,
        # Underbarrel.COMMANDO_FOREGRIP,
        Stock.NO_STOCK,
        # Ammunition.ROUND_MAGS_60
        RearGrip.STIPPLED_GRIP_TAPE
    ]

    player.commands["!m4"] = "Nade's M4 Class -> Monolithic Suppressor, Commando Foregrip, Stock M16 Grenadier Barrel, 60 Round Mag, Tac Laser"

    # Post-process
    attachments.sort(key=lambda attachment: attachment.value)  # TODO: needed now?
    attachments = {attachment.get_type(): attachment.value for attachment in attachments}

    player.loadouts[loadout] = {
        "source": source,
        "lastUpdated": last_updated,
        "attachments": attachments
    }

    db.add_player(player)
    print(f"Added {player.username}'s {loadout}")

