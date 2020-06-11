import json
import logging
import requests

DEFINITIONS_FILE = "../database.json"
NIGHTBOT_CHANNEL_URL = "https://api.nightbot.tv/1/channels/t/"
NIGHTBOT_COMMANDS_URL = "https://api.nightbot.tv/1/commands"


def main():
    with open(DEFINITIONS_FILE, "r+") as file:
        database = json.load(file)
        [query_nightbot(entry) for entry in database.items()]
        logging.info(f"{len(database)} users checked")


def query_nightbot(entry):
    username, data = entry
    url = NIGHTBOT_CHANNEL_URL + username
    response = requests.get(url).json()

    if response.get("status") == 200:
        user_id = response.get("channel", {}).get("_id")
        commands = {}

        for cmd in query_commands(user_id):
            commands[cmd["name"]] = cmd["message"]

        compare_commands(username, previous=data.get("commands", []), current=commands)


def query_commands(user_id):
    headers = {"nightbot-channel": user_id}
    response = requests.get(NIGHTBOT_COMMANDS_URL, headers=headers).json()

    if response.get("status") == 200:
        return response.get("commands", [])

    return []


def compare_commands(username, previous, current):
    for entry in previous:
        cmd = entry["command"]
        msg = entry["message"]
        new_msg = current.get(cmd)

        if msg != new_msg:
            logging.info(f"[{username}] [{cmd}]: {new_msg}")


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    main()
