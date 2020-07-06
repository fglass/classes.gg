from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import Attachment
from model.weapon import Weapon

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    player = db.select_player("sweetsurrenderd")

    player.loadouts[Weapon.FENNEC.value] = {
        "source": "https://www.reddit.com/r/MWLoadouts/comments/hdb5hq/warzone_loadout_16_of_the_series_all_about_war/",
        "lastUpdated": datetime.now().isoformat(),
        "attachments": [
            Attachment.ZLR_DEADFALl.value,
            Attachment.NO_STOCK.value,
            Attachment.MERC_FOREGRIP.value,
            Attachment.ROUND_DRUM_MAGS_40.value,
            Attachment.STIPPLED_GRIP_TAPE.value
        ]
    }

    # player.commands["!mp5"] = "@{touser.name} https://clips.twitch.tv/CourteousBlueStinkbugMcaT"

    db.add_player(player)
    print(f"Edited {player.username}")
