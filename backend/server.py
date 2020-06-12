from backend.db.json_database_engine import JSONDatabaseEngine
from flask import Flask
from markupsafe import escape

app = Flask(__name__)
db = JSONDatabaseEngine()


@app.route('/player/<username>')
def get_player(username):
    player = db.select_player(username=escape(username))
    return {
        "username": player.username,
        "weapons": player.weapons,
        "commands": player.commands
    }
