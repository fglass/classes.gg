import difflib
import hashlib
import logging
import requests
from db.admin.change.command_source import CommandSource
from db.json_database_engine import JSONDatabaseEngine

SOURCE_KEY = "source"
GOOGLE_SHEET_KEY = "google"
DIFF_CONTROL_PREFIXES = {"---", "+++", "@@"}


def main():
    db = JSONDatabaseEngine()
    players = db.select_players()

    for player in players:

        previous_commands = player.commands
        source_name = previous_commands.pop(SOURCE_KEY, None)

        if source_name:
            source = CommandSource(source_name)
            current_commands = source.query(player)
            _compare_commands(player.username, previous=previous_commands, current=current_commands)

        if player.spreadsheet:
            _compare_spreadsheet_hash(player.username, player.spreadsheet)

    logging.info(f"{len(players)} players checked")


def _compare_commands(username: str, previous: dict, current: dict):
    for cmd, msg in previous.items():
        new_msg = current.get(cmd)
        if msg != new_msg:
            logging.info(f"[{username}] [{cmd}]: {new_msg}")


def _compare_spreadsheet_hash(username: str, spreadsheet: dict):
    if spreadsheet[SOURCE_KEY] != GOOGLE_SHEET_KEY:
        return

    file = spreadsheet["file"]
    filename = f"db/admin/change/data/{file}"
    with open(filename, "rb") as f:
        content = f.read()
        current_hash = hashlib.md5(content).hexdigest()

    if not current_hash:
        return

    url = spreadsheet["url"]
    export_url = f"{url}/export?format=csv"
    response = requests.get(export_url)
    new_hash = hashlib.md5(response.content).hexdigest()

    if current_hash != new_hash:
        logging.info(f"[{username}]: {url}")
        _display_spreadsheet_diff(current=content, new=response.content)


def _display_spreadsheet_diff(current: bytes, new: bytes):
    a = current.decode("utf-8").splitlines()
    b = new.decode("utf-8").splitlines()
    diff = difflib.unified_diff(a, b, fromfile="Current", tofile="New", lineterm="", n=0)
    delta = filter(lambda line: not any(line.startswith(prefix) for prefix in DIFF_CONTROL_PREFIXES), diff)
    [logging.info(f"\t\t{line}") for line in delta]


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    main()
