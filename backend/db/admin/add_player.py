from datetime import datetime

from model.command.command_source import CommandSource
from db.json_database_engine import JSONDatabaseEngine
from model.player import Player


NEW_PLAYER = Player(
    username="fifakillvizualz",
    avatar="https://static-cdn.jtvnw.net/jtv_user_pictures/8b3404ed950b4fda-profile_image-300x300.jpeg",
    command_source=CommandSource.NIGHTBOT.value,
    last_updated=datetime.now().isoformat(),
    loadouts={},
    spreadsheet={
        # "id": "1SWU-40CNrKL1thqffc-877rr-BV5TXQfjyPVL3CzJ1I",
        # "sheets": ["0"],
    },
    views=0,
)

if __name__ == '__main__':
    JSONDatabaseEngine().add_player(NEW_PLAYER)
    print(f"Added {NEW_PLAYER.username}")
