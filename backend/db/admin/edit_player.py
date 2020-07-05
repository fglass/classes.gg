from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import Attachment
from model.weapon import Weapon

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    player = db.select_player("symfuhny")

    player.loadouts[Weapon.MP5.value] = {
        "source": "https://clips.twitch.tv/CourteousBlueStinkbugMcaT",
        "lastUpdated": datetime.now().isoformat(),
        "attachments": [
            Attachment.MONOLITHIC_SUPPRESSOR.value,
            Attachment.ROUND_MAGS_45.value,
            Attachment.MERC_FOREGRIP.value,
            Attachment.FTAC_COLLAPSIBLE.value,
            Attachment.SLEIGHT_OF_HAND.value
        ]
    }

    player.commands["!mp5"] = "@{touser.name} https://clips.twitch.tv/CourteousBlueStinkbugMcaT"

    db.add_player(player)
    print(f"Edited {player.username}")
