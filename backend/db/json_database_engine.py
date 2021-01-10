import json
from db.database_engine import DatabaseEngine
from model.player import Player
from typing import Optional, ValuesView

DATABASE_FILE = "db/database.json"
TEST_DATABASE_FILE = "db/test/test_database.json"
VIEW_COUNTS_FILE = "db/view_counts.json"


class JSONDatabaseEngine(DatabaseEngine):

    def __init__(self, test_mode=False):
        self._database = {}
        self._file = TEST_DATABASE_FILE if test_mode else DATABASE_FILE
        self._test_mode = test_mode

        with open(self._file, "r+") as f:
            self._database = json.load(f)

        self._player_view = self._create_materialised_view()
        self._load_view_counts()

    def _create_materialised_view(self) -> dict:
        return {name: _deserialise_player(data) for name, data in self._database.items()}

    def _load_view_counts(self):
        with open(VIEW_COUNTS_FILE, "r+") as f:
            view_counts = json.load(f)
            for name, player in self._player_view.items():
                player.views = view_counts.get(name, 0)

    def select_player(self, username: str) -> Optional[Player]:
        return self._player_view.get(username)

    def select_players(self) -> ValuesView[Player]:
        return self._player_view.values()

    def add_player(self, player: Player):
        username = player.username.lower()
        self._database[username] = player.serialise()
        self._player_view[username] = player
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
