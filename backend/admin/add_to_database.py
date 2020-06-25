from backend.db.json_database_engine import JSONDatabaseEngine
from backend.model.attachment import Attachment
from backend.model.player import Player
from backend.model.weapon import Weapon
from datetime import datetime


NEW_PLAYER = Player(
    username="NICKMERCS",
    avatar="https://static-cdn.jtvnw.net/jtv_user_pictures/ff13760d-d795-49d9-8f3f-f05035930c81-profile_image-300x300.png",
    loadouts={
        Weapon.M4A1.value: {
            "source": "https://www.youtube.com/watch?v=FrsiqOFIhl8",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.RANGER_FOREGRIP.value,
                Attachment.STIPPLED_GRIP_TAPE.value,
                Attachment.ROUND_MAGS_60.value,
                Attachment.STOCK_M16_GRENADIER.value
            ]
        },
        Weapon.GRAU.value: {
            "source": "https://www.youtube.com/watch?v=16s4rytUqDM",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.TEMPUS_ARCHANGEL.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.CRONEN_SNIPER_ELITE.value,
                Attachment.ROUND_MAGS_60.value
            ]
        },
        Weapon.MP5.value: {
            "source": "https://www.youtube.com/watch?v=Is1CWVUX5T8",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_INTEGRAL_SUPPRESSOR.value,
                Attachment.FTAC_COLLAPSIBLE.value,
                Attachment.MERC_FOREGRIP.value,
                Attachment.SLEIGHT_OF_HAND.value,
                Attachment.ROUND_MAGS_45.value
            ]
        },
    },
    commands={}
)

if __name__ == '__main__':
    JSONDatabaseEngine().add_player(NEW_PLAYER)
    print(f"Added {NEW_PLAYER.username}")
