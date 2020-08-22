import json
from db.database_engine import DatabaseEngine
from model.player import Player
from typing import Optional, ValuesView

JSON_FILE = "db/database.json"
TEST_JSON_FILE = "db/test/test_database.json"


class JSONDatabaseEngine(DatabaseEngine):

    def __init__(self, test_mode=False):
        self._database = {}
        self._file = TEST_JSON_FILE if test_mode else JSON_FILE
        self._test_mode = test_mode

        with open(self._file, "r+") as f:
            self._database = json.load(f)

        # Create static materialised view
        self._player_view = {name: _deserialise_player(data) for name, data in self._database.items()}

    def select_player(self, username: str) -> Optional[Player]:
        return self._player_view.get(username)

    def select_players(self) -> ValuesView[Player]:
        return self._player_view.values()

    def add_player(self, player: Player):
        self._database[player.username.lower()] = player.serialise()
        self._commit()

    def _commit(self):
        if self._test_mode:
            return

        with open(self._file, "r+") as file:
            file.seek(0)
            json.dump(self._database, file, indent=2, sort_keys=True)
            file.truncate()


def _deserialise_player(data: dict) -> Player:
    return Player(
        data.get("username", "N/A"),
        data.get("avatar", ""),
        data.get("last_updated", ""),
        data.get(
            "loadouts", {"N/A": {
                "source": "",
                "attachments": ["N/A", "N/A", "N/A", "N/A", "N/A"]
            }}
        ),
        data.get("commands", {}),
        data.get("spreadsheet", {})
    )
