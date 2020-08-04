from db.admin.change.command_source import CommandSource
from db.json_database_engine import JSONDatabaseEngine
from model.player import Player


NEW_PLAYER = Player(
    username="IceManIsaac",
    avatar="https://static-cdn.jtvnw.net/jtv_user_pictures/28de8cd2-e1cd-4c7d-9ad5-31c9e5788a02-profile_image-300x300.png",
    loadouts={},
    commands={"source": CommandSource.NIGHTBOT.value},
    gsheet = {},
)

if __name__ == '__main__':
    JSONDatabaseEngine().add_player(NEW_PLAYER)
    print(f"Added {NEW_PLAYER.username}")
