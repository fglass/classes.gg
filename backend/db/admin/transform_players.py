from db.json_database_engine import JSONDatabaseEngine

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    players = db.select_players()

    for player in players:
        dts = []
        loadouts = player.loadouts.items()

        for weapon, loadout in loadouts:
            loadout["game"] = loadout.pop("origin", "MW")

        db.add_player(player)
