from backend.db.json_database_engine import JSONDatabaseEngine
from flask import Flask, jsonify
from markupsafe import escape

app = Flask(__name__)
db = JSONDatabaseEngine()


@app.route('/player/<username>')
def get_player(username):
    player = db.select_player(username=escape(username))
    return jsonify(player.serialise())


@app.route('/players')
def get_players():
    players = [player.serialise() for player in db.select_players()]
    return jsonify(players)


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response
