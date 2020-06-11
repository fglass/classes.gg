import json
import requests

DEFINITIONS_FILE = "../src/database.json"


def main():
    with open(DEFINITIONS_FILE, 'r+') as file:
        database = json.load(file)
        for entry in database.items():
            query_nightbot(entry)


def query_nightbot(entry):
    key, value = entry
    url = f"https://api.nightbot.tv/1/channels/t/{key}"
    print(f"Requesting {url}")
    response = requests.get(url).json()

    if response.get('status') == 200:
        user_id = response.get('channel', {}).get('_id')
        commands = query_commands(user_id)

        new_commands = {}
        for cmd in commands:
            new_commands[cmd['name']] = cmd['message']

        compare_commands(old=value.get("commands"), new=new_commands)


def query_commands(user_id):
    url = "https://api.nightbot.tv/1/commands"
    headers = {"nightbot-channel": user_id}
    response = requests.get(url, headers=headers).json()

    if response.get('status') == 200:
        return response.get("commands", {})

    return {}


def compare_commands(old, new):
    for entry in old:
        cmd = entry["command"]
        msg = entry["message"]
        print(f"Command {cmd}")
        print(f"Old: {msg}")
        print(f"New: {new.get(cmd)}")
        print(f"Change: {msg != new.get(cmd)}")
        print("-" * 10)


if __name__ == '__main__':
    main()
