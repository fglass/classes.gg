import unittest
from backend.db.json_database_engine import JSONDatabaseEngine
from backend.player import Player


class TestJSONDatabaseEngine(unittest.TestCase):

    def test_select_player(self):
        db = JSONDatabaseEngine(test_mode=True)
        player = db.select_player("Scump")
        self.assertIn("Grau", player.loadouts)
        self.assertIn("!grau", player.commands)

    def test_select_players(self):
        db = JSONDatabaseEngine(test_mode=True)
        players = db.select_players()
        self.assertEqual(1, len(players))
        self.assertIn("Scump", players[0].username)

    def test_add_player(self):
        db = JSONDatabaseEngine(test_mode=True)
        username = "test_player"
        player = Player(username, avatar="", loadouts={}, commands={})
        db.add_player(player)
        self.assertIn(username, db._database)
