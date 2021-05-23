from datetime import datetime

from model.command.command_source import CommandSource
from db.json_database_engine import JSONDatabaseEngine
from model.player import Player


NEW_PLAYER = Player(
    username="Crowder",
    avatar="https://static-cdn.jtvnw.net/jtv_user_pictures/6d8a01d4-323c-42b7-95fe-8df59cd94c0c-profile_image-300x300.png",
    views=0,
    last_updated=datetime.now().isoformat(),
    loadouts={},
    commands={"source": CommandSource.NIGHTBOT.value},
    spreadsheet={
        "source": "google",
        "id": "1S8YyLcm0qJGwrtIxb3_9RkzIo_Icf_ld979ucdKllwc",
        "sheets": ["0"],
    },
)

if __name__ == '__main__':
    JSONDatabaseEngine().add_player(NEW_PLAYER)
    print(f"Added {NEW_PLAYER.username}")
