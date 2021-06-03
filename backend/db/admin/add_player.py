from datetime import datetime

from model.command.command_source import CommandSource
from db.json_database_engine import JSONDatabaseEngine
from model.player import Player


NEW_PLAYER = Player(
    username="ScummN",
    avatar="https://static-cdn.jtvnw.net/jtv_user_pictures/a1ab18a3-c807-4ad8-bdee-87d8b9a7be49-profile_image-300x300.png",
    command_source=CommandSource.NIGHTBOT.value,
    last_updated=datetime.now().isoformat(),
    loadouts={},
    spreadsheet={
        "id": "18KTt5UtHhY5nWqZt7GEMcUPM4UJjkoRqgamnbFAuFaM",
        "sheets": ["0"],
    },
    views=0,
)

if __name__ == '__main__':
    JSONDatabaseEngine().add_player(NEW_PLAYER)
    print(f"Added {NEW_PLAYER.username}")
