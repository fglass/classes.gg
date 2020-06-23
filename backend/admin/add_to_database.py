from backend.db.json_database_engine import JSONDatabaseEngine
from backend.model.player import Player
from datetime import datetime

NEW_PLAYER = Player(
    username="JukeyzL",
    avatar="https://static-cdn.jtvnw.net/jtv_user_pictures/9a0369b8-d6e3-4ce3-a3fe-cbbf35cfb068-profile_image-300x300.png",
    loadouts={
        "test_weapon": {
            "source": "",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": []
        }
    },
    commands={}
)

if __name__ == '__main__':
    JSONDatabaseEngine().add_player(NEW_PLAYER)  # TODO: add weapon and attachment enums
