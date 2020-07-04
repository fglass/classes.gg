from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import Attachment
from model.weapon import Weapon

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    player = db.select_player("huskerrs")

    player.loadouts[Weapon.UZI.value] = {
        "source": "https://www.twitch.tv/huskerrs",
        "lastUpdated": datetime.now().isoformat(),
        "attachments": [
            Attachment.MONOLITHIC_SUPPRESSOR.value,
            Attachment.FSS_CARBINE_PRO.value,
            Attachment.TAC_LASER.value,
            Attachment.COMMANDO_FOREGRIP.value,
            Attachment.AE_ROUND_MAGS_32.value
        ]
    }

    player.commands["!uzi"] = "Monolithic Suppressor, FSS Carbine Pro, Tac Laser, Commando Foregrip, .41 AE 32-Round Mags"

    db.add_player(player)
    print(f"Edited {player.username}")
