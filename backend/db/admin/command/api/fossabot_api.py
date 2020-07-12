import requests
from model.player import Player

FOSSABOT_COMMANDS_URL = "https://api-v1.fossabot.com/api/v1/%s/public-commands"


def query_fossabot(player: Player) -> dict:
    commands = {}
    url = FOSSABOT_COMMANDS_URL % player.username
    response = requests.get(url)

    if response.status_code == 200:
        for cmd in response.json().get("commands", []):
            commands[cmd["name"]] = cmd["response"]

    return commands
