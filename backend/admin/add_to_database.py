from backend.db.json_database_engine import JSONDatabaseEngine
from backend.player import Player

NEW_PLAYER = Player(
    username="spratt",
    avatar="https://static-cdn.jtvnw.net/jtv_user_pictures/68e25fb7-62f1-4192-b637-72ead12d140a-profile_image-300x300.png",
    weapons={},
    commands={}
)

if __name__ == '__main__':
    JSONDatabaseEngine().add_player(NEW_PLAYER)
