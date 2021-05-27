import atexit
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
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


@api.route("/nextUpdate")
def get_seconds_until_next_update():
    job = scheduler.get_jobs()[0]
    next_update = job.next_run_time.replace(tzinfo=None)
    time_remaining = next_update - datetime.now()
    return jsonify(time_remaining.total_seconds())


@api.route("/recentUpdates")
def get_recent_updates():
    return jsonify(list(reversed(loadout_updater.recent_updates)))


@api.route("/view/<username>", methods=['POST'])
def view_player(username: str):
    sanitised_username = escape(username.lower())
    player = db.select_player(sanitised_username)
    player.views += 1
    return jsonify(success=True)


scheduler.remove_all_jobs()
scheduler.add_job(func=loadout_updater.run, trigger="interval", hours=1)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

app.register_blueprint(api, url_prefix="/api")
