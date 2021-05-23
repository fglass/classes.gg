import unittest
from db.json_database_engine import JSONDatabaseEngine
from model.player import Player
from model.weapon.weapon import AssaultRifle


class TestJSONDatabaseEngine(unittest.TestCase):

    def test_select_player(self):
        db = JSONDatabaseEngine(test_mode=True)
        player = db.select_player("scump")
        self.assertIn(str(AssaultRifle.AK_47), player.loadouts)

    def test_select_players(self):
        db = JSONDatabaseEngine(test_mode=True)
        players = list(db.select_players())
        self.assertEqual(1, len(players))
        self.assertIn("Scump", players[0].username)

    def test_add_player(self):
        db = JSONDatabaseEngine(test_mode=True)
        username = "test_player"
        player = Player(
            username,
            avatar="",
            command_source="",
            last_updated="",
            loadouts={},
            spreadsheet={},
            views=0
        )
        db.add_player(player)
        self.assertIn(username, db._database)
