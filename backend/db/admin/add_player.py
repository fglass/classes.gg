from db.admin.command.command_source import CommandSource
from db.json_database_engine import JSONDatabaseEngine
from model.attachment import Attachment
from model.player import Player
from model.weapon import Weapon
from datetime import datetime


NEW_PLAYER = Player(
    username="HusKerrs",
    avatar="https://static-cdn.jtvnw.net/jtv_user_pictures/huskerrs-profile_image-da754786ed2851c1-300x300.jpeg",
    loadouts={
        Weapon.M4A1.value: {
            "source": "https://www.twitch.tv/huskerrs",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.STOCK_M16_GRENADIER.value,
                Attachment.TAC_LASER.value,
                Attachment.ROUND_MAGS_60.value,
                Attachment.COMMANDO_FOREGRIP.value
            ]
        },
    },
    commands={
        "!loadout": "See !M4 !MP7 !MP5 !GRAU !HDR !M13 !KAR !FENNEC for attachments :)",
        "source": CommandSource.STREAMELEMENTS.value
    }
)

if __name__ == '__main__':
    [v["attachments"].sort() for k, v in NEW_PLAYER.loadouts.items()]
    JSONDatabaseEngine().add_player(NEW_PLAYER)
    print(f"Added {NEW_PLAYER.username}")
