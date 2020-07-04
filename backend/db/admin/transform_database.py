from db.admin.command.command_source import CommandSource
from db.json_database_engine import JSONDatabaseEngine

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    players = db.select_players()

    for player in players:
        player.commands["source"] = CommandSource.NIGHTBOT.value
        db.add_player(player)
