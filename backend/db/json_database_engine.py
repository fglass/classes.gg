import json
import os
from db.database_engine import DatabaseEngine
from model.player import Player
from typing import Optional, ValuesView

ENVIRONMENT = os.environ.get("ENVIRONMENT", "DEV")
IS_PROD = ENVIRONMENT == "PROD"
DATABASE_FILE = "/database/database.json" if IS_PROD else "db/database.json"
TEST_DATABASE_FILE = "db/test/test-database.json"


class JSONDatabaseEngine(DatabaseEngine):

    def __init__(self, test_mode=False):
        self._database = {}
        self._file = TEST_DATABASE_FILE if test_mode else DATABASE_FILE
        self._test_mode = test_mode

        with open(self._file, "r+") as file:
            self._database = json.load(file)

        self._player_view = self._create_materialised_view()

    def _create_materialised_view(self) -> dict:
        return {name: _deserialise_player(data) for name, data in self._database.items()}

    def select_player(self, username: str) -> Optional[Player]:
        return self._player_view.get(username)

    def select_players(self) -> ValuesView[Player]:
        return self._player_view.values()

    def add_player(self, player: Player, save: bool = True):
        username = player.username.lower()
        self._database[username] = player.serialise()
        self._player_view[username] = player
        if save:
            self.save()

    def save(self):
        if self._test_mode:
            return

        with open(DATABASE_FILE, "r+") as file:
            file.seek(0)
            json.dump(self._database, file, indent=2, sort_keys=True)
            file.truncate()


def _deserialise_player(data: dict) -> Player:
    return Player(
        data.get("username", "N/A"),
        data.get("avatar", ""),
        data.get("command_source", ""),
        data.get("last_updated", ""),
        data.get("loadouts", {}),
        data.get("spreadsheet", {}),
        data.get("views", 0)
    )


db = JSONDatabaseEngine()
