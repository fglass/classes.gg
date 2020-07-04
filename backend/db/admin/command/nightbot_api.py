import requests
from model.player import Player

NIGHTBOT_CHANNEL_URL = "https://api.nightbot.tv/1/channels/t/"
NIGHTBOT_COMMANDS_URL = "https://api.nightbot.tv/1/commands"


def query_nightbot(player: Player) -> dict:
    commands = {}
    url = NIGHTBOT_CHANNEL_URL + player.username
    response = requests.get(url).json()

    if response.get("status") == 200:
        user_id = response.get("channel", {}).get("_id")

        for cmd in _query_commands(user_id):
            commands[cmd["name"]] = cmd["message"]

    return commands


def _query_commands(user_id: str):
    headers = {"nightbot-channel": user_id}
    response = requests.get(NIGHTBOT_COMMANDS_URL, headers=headers).json()

    if response.get("status") == 200:
        return response.get("commands", [])

    return []
