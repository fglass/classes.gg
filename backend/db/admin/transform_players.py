from db.json_database_engine import JSONDatabaseEngine

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    players = db.select_players()

    for player in players:
        player.command_source = db._database[player.username.lower()].get("commands", {}).get("source")
        player.spreadsheet.pop("source", None)
        db.add_player(player, save=False)

    db.save()
