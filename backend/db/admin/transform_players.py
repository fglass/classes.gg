from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    players = db.select_players()

    for player in players:
        dts = []
        loadouts = player.loadouts.items()

        for weapon, loadout in loadouts:
            last_updated = datetime.strptime(loadout["lastUpdated"], "%Y-%m-%dT%H:%M:%S.%f")
            dts.append(last_updated)
            loadout.pop("lastUpdated")

        now = datetime.now()
        latest = max(dt for dt in dts if dt < now)
        player.last_updated = latest.isoformat()
        db.add_player(player)
