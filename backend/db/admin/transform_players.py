from db.json_database_engine import JSONDatabaseEngine

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    players = db.select_players()

    for player in players:
        [v["attachments"].sort() for k, v in player.loadouts.items()]
        db.add_player(player)
