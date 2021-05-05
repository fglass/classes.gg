import unittest
from db.json_database_engine import JSONDatabaseEngine
from model.player import Player
from model.weapon.weapon import Weapon


class TestJSONDatabaseEngine(unittest.TestCase):

    def test_select_player(self):
        db = JSONDatabaseEngine(test_mode=True)
        player = db.select_player("Scump")
        self.assertIn(Weapon.GRAU.value, player.loadouts)
        self.assertIn("!grau", player.commands)

    def test_select_players(self):
        db = JSONDatabaseEngine(test_mode=True)
        players = list(db.select_players())
        self.assertEqual(1, len(players))
        self.assertIn("Scump", players[0].username)

    def test_add_player(self):
        db = JSONDatabaseEngine(test_mode=True)
        username = "test_player"
        player = Player(username, avatar="", last_updated="", loadouts={}, commands={}, spreadsheet={})
        db.add_player(player)
        self.assertIn(username, db._database)
