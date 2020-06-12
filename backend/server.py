from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/player/<username>')
def get_player(username):
    return {
        "username": escape(username),
        "guns": ["Grau", "M4", "MP5"]
    }
