from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import Attachment
from model.weapon import Weapon

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    player = db.select_player("huskerrs")

    loadout = Weapon.AK_47.value

    player.loadouts[loadout] = {
        "source": "https://tinyurl.com/huskloadout",
        "lastUpdated": datetime.now().isoformat(),
        "attachments": [
            Attachment.MONOLITHIC_SUPPRESSOR.value,
            Attachment.RPK_BARREL.value,
            Attachment.TAC_LASER.value,
            Attachment.COMMANDO_FOREGRIP.value,
            Attachment.NATO_ROUND_MAGS.value
        ]
    }

    player.commands["!m4"] = "Nade's M4 Class -> Monolithic Suppressor, Commando Foregrip, Stock M16 Grenadier Barrel, 60 Round Mag, Tac Laser"

    [v["attachments"].sort() for k, v in player.loadouts.items()]

    db.add_player(player)
    print(f"Added {player.username}'s {loadout}")
