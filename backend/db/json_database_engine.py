import json

from backend.db.database_engine import DatabaseEngine
from backend.player import Player

JSON_FILE = "backend/db/database.json"
TEST_JSON_FILE = "backend/db/test/test_database.json"


class JSONDatabaseEngine(DatabaseEngine):

    def __init__(self, test_mode=False):
        self._database = {}
        self._file = TEST_JSON_FILE if test_mode else JSON_FILE
        self._test_mode = test_mode

        with open(self._file, "r+") as f:
            self._database = json.load(f)

    def select_player(self, username: str) -> Player:
        data = self._database.get(username, {})
        return _deserialise_player(data)

    def select_players(self) -> list:
        return [_deserialise_player(data) for _, data in self._database.items()]

    def add_player(self, player: Player):
        self._database[player.username] = player.serialise()
        self._commit()

    def _commit(self):
        if self._test_mode:
            return

        with open(self._file, "r+") as file:
            file.seek(0)
            json.dump(self._database, file, indent=2)
            file.truncate()


def _deserialise_player(data: dict) -> Player:
    return Player(
        data.get("username", "Unknown"),
        data.get("avatar", ""),
        data.get("weapons", {"?": ["#1", "#2", "#3", "#4", "#5"]}),
        data.get("commands", {})
    )
