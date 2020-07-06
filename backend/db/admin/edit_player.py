from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import Attachment
from model.weapon import Weapon

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    player = db.select_player("sorangkun")

    player.loadouts[Weapon.M13.value] = {
        "source": "https://www.reddit.com/r/MWLoadouts/comments/fwhb5z/ultimate_m13_guide_for_warzone/",
        "lastUpdated": datetime.now().isoformat(),
        "attachments": [
            Attachment.MONOLITHIC_SUPPRESSOR.value,
            Attachment.TEMPUS_MARKSMAN.value,
            Attachment.TAC_LASER.value,
            Attachment.ROUND_MAGS_50.value,
        ]
    }

    # player.commands["!mp5"] = "@{touser.name} https://clips.twitch.tv/CourteousBlueStinkbugMcaT"

    db.add_player(player)
    print(f"Edited {player.username}")
