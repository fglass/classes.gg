import json

from backend.db.database_engine import DatabaseEngine
from backend.player import Player

DEFINITIONS_FILE = "backend/db/database.json"


class JSONDatabaseEngine(DatabaseEngine):

    def __init__(self):
        self._database = {}
        with open(DEFINITIONS_FILE, 'r+') as file:
            self._database = json.load(file)

    def add_player(self, player: Player):
        self._database[player.username] = player.serialise()
        self._commit()

    def _commit(self):
        with open(DEFINITIONS_FILE, 'r+') as file:
            file.seek(0)
            json.dump(self._database, file, indent=2)
            file.truncate()

    def select_player(self, username) -> Player:
        data = self._database.get(username, {})
        return Player(username, data.get("weapons", {}), data.get("commands", {}))

    def select_players(self) -> list:
        return [
            Player(username, data.get("weapons", {}), data.get("commands", {}))
            for username, data in self._database.items()
        ]
