import requests
from model.player import Player

STREAMELEMENTS_CHANNEL_URL = "https://api.streamelements.com/kappa/v2/channels/"
STREAMELEMENTS_COMMANDS_URL = "https://api.streamelements.com/kappa/v2/bot/commands/%s/public"


def query_streamelements(player: Player) -> dict:
    commands = {}
    url = STREAMELEMENTS_CHANNEL_URL + player.username
    response = requests.get(url)

    if response.status_code == 200:
        user_id = response.json().get("_id")

        for cmd in _query_commands(user_id):
            commands[f"!{cmd['command']}"] = cmd["reply"]

    return commands


def _query_commands(user_id: str) -> list:
    commands_url = STREAMELEMENTS_COMMANDS_URL % user_id
    response = requests.get(commands_url)

    if response.status_code == 200:
        return response.json()

    return []
