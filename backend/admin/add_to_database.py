from backend.db.json_database_engine import JSONDatabaseEngine
from backend.player import Player

NEW_PLAYER = Player(
    username="JukeyzL",
    avatar="https://static-cdn.jtvnw.net/jtv_user_pictures/9a0369b8-d6e3-4ce3-a3fe-cbbf35cfb068-profile_image-300x300.png",
    weapons={},
    commands={}
)

if __name__ == '__main__':
    JSONDatabaseEngine().add_player(NEW_PLAYER)
