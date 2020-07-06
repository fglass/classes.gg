from db.admin.command.command_source import CommandSource
from db.json_database_engine import JSONDatabaseEngine
from model.player import Player


NEW_PLAYER = Player(
    username="SweetSurrenderD",
    avatar="https://imgur.com/zc1fAZ4.png",
    loadouts={},
    commands={"source": CommandSource.NIGHTBOT.value}
)

if __name__ == '__main__':
    JSONDatabaseEngine().add_player(NEW_PLAYER)
    print(f"Added {NEW_PLAYER.username}")
