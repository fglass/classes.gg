import logging
import requests
from backend.db.json_database_engine import JSONDatabaseEngine
from backend.player import Player

NIGHTBOT_CHANNEL_URL = "https://api.nightbot.tv/1/channels/t/"
NIGHTBOT_COMMANDS_URL = "https://api.nightbot.tv/1/commands"


def main():
    db = JSONDatabaseEngine()
    players = db.select_players()
    [query_nightbot(player) for player in players]
    logging.info(f"{len(players)} players checked")


def query_nightbot(player: Player):
    url = NIGHTBOT_CHANNEL_URL + player.username
    response = requests.get(url).json()

    if response.get("status") == 200:
        user_id = response.get("channel", {}).get("_id")
        commands = {}

        for cmd in query_commands(user_id):
            commands[cmd["name"]] = cmd["message"]

        compare_commands(player.username, previous=player.commands, current=commands)


def query_commands(user_id: str):
    headers = {"nightbot-channel": user_id}
    response = requests.get(NIGHTBOT_COMMANDS_URL, headers=headers).json()

    if response.get("status") == 200:
        return response.get("commands", [])

    return []


def compare_commands(username: str, previous: dict, current: dict):
    for cmd, msg in previous.items():
        new_msg = current.get(cmd)
        if msg != new_msg:
            logging.info(f"[{username}] [{cmd}]: {new_msg}")


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    main()
