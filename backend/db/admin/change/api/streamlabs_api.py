import requests
from model.player import Player

STREAMLABS_CHANNEL_URL = "https://streamlabs.com/api/v6/user/"
STREAMLABS_COMMANDS_URL = "https://streamlabs.com/api/v6/%s/cloudbot/commands"


def query_streamlabs(player: Player) -> dict:
    commands = {}
    url = STREAMLABS_CHANNEL_URL + player.username
    response = requests.get(url)

    if response.status_code == 200:
        token = response.json().get("token")

        for cmd in _query_commands(token):
            commands[cmd["command"]] = cmd.get("response")

    return commands


def _query_commands(token: str) -> list:
    commands_url = STREAMLABS_COMMANDS_URL % token
    response = requests.get(commands_url)

    if response.status_code == 200:
        return response.json()

    return []
