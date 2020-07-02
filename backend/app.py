from db.json_database_engine import JSONDatabaseEngine
from flask import Flask, Blueprint, abort, jsonify
from markupsafe import escape

app = Flask(__name__)
api = Blueprint('api', __name__)
db = JSONDatabaseEngine()


@api.route('/player/<username>')
def get_player(username: str):
    player = db.select_player(username=escape(username.lower()))
    if not player:
        abort(404)
    return jsonify(player.serialise())


@api.route('/players')
def get_players():
    players = [player.serialise() for player in db.select_players()]
    return jsonify(players)


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


app.register_blueprint(api, url_prefix='/api')

