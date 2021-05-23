import atexit
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from db.loadout_updater import LoadoutUpdater
from db.json_database_engine import db
from flask import Flask, Blueprint, abort, jsonify
from flask_cors import CORS
from markupsafe import escape

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
app = Flask(__name__)
CORS(app)
api = Blueprint("api", __name__)
scheduler = BackgroundScheduler(daemon=True)
loadout_updater = LoadoutUpdater()


@api.route("/players")
def get_players():
    players = [
        dict(
            username=player.username,
            avatar=player.avatar,
            views=player.views,
            lastUpdated=player.last_updated,
            loadoutKeys=list(player.loadouts.keys()),
        )
        for player in db.select_players()
    ]
    return jsonify(players)


@api.route("/loadouts/<username>")
def get_player_loadouts(username: str):
    sanitised_username = escape(username.lower())
    player = db.select_player(sanitised_username)
    return player.loadouts if player else abort(404)


@api.route("/view/<username>", methods=['POST'])
def view_player(username: str):
    sanitised_username = escape(username.lower())
    player = db.select_player(sanitised_username)
    player.views += 1
    return jsonify(success=True)


@api.route("/recentUpdates")
def get_recent_updates():
    return jsonify(list(reversed(loadout_updater.recent_updates)))


scheduler.remove_all_jobs()
scheduler.add_job(func=loadout_updater.run, trigger="interval", hours=1)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

app.register_blueprint(api, url_prefix="/api")
