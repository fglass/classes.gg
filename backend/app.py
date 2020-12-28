from db.json_database_engine import JSONDatabaseEngine
from flask import Flask, Blueprint, abort, jsonify
from flask_cors import CORS
from markupsafe import escape

app = Flask(__name__)
CORS(app)
api = Blueprint("api", __name__)
db = JSONDatabaseEngine()


@api.route("/players")
def get_players():
    players = [
        dict(
            username=player.username,
            avatar=player.avatar,
            lastUpdated=player.last_updated,
            nLoadouts=len(player.loadouts)
        )
        for player in db.select_players()
    ]
    return jsonify(players)


@api.route("/loadouts/<username>")
def get_player(username: str):
    sanitised_username = escape(username.lower())
    player = db.select_player(sanitised_username)
    return player.loadouts if player else abort(404)


app.register_blueprint(api, url_prefix="/api")
