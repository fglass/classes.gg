from db.admin.command.command_source import CommandSource
from db.json_database_engine import JSONDatabaseEngine
from model.player import Player


NEW_PLAYER = Player(
    username="Swagg",
    avatar="https://static-cdn.jtvnw.net/jtv_user_pictures/swagg-profile_image-a0898c1b75f6094d-300x300.png",
    loadouts={},
    commands={"source": CommandSource.NIGHTBOT.value}
)

if __name__ == '__main__':
    JSONDatabaseEngine().add_player(NEW_PLAYER)
    print(f"Added {NEW_PLAYER.username}")
