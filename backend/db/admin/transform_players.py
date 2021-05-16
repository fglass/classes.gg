from db.json_database_engine import JSONDatabaseEngine

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    players = db.select_players()

    for player in players:
        # player.views = 0
        # db.add_player(player)
        player.loadouts = {}
        db.add_player(player, commit=False)

    db.commit()
