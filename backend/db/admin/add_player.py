from db.admin.command.command_source import CommandSource
from db.json_database_engine import JSONDatabaseEngine
from model.player import Player


NEW_PLAYER = Player(
    username="Tfue",
    avatar="https://static-cdn.jtvnw.net/jtv_user_pictures/82b63a01-628f-4c81-9b05-dd3a5011fdda-profile_image-300x300.png",
    loadouts={},
    commands={"source": CommandSource.FOSSABOT.value}
)

if __name__ == '__main__':
    JSONDatabaseEngine().add_player(NEW_PLAYER)
    print(f"Added {NEW_PLAYER.username}")
