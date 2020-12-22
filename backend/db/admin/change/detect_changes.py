import difflib
import hashlib
import logging
import requests
from db.admin.change.command_source import CommandSource
from db.json_database_engine import JSONDatabaseEngine

SOURCE_KEY = "source"
SHEETS_KEY = "sheets"
GOOGLE_SHEET_KEY = "google"
DIFF_CONTROL_PREFIXES = {"---", "+++", "@@"}
DATA_PATH = "db/admin/change/data"


def main():
    db = JSONDatabaseEngine()
    players = db.select_players()

    for player in players:

        username = player.username.lower()
        previous_commands = player.commands
        source_name = previous_commands.pop(SOURCE_KEY, None)

        if source_name:
            source = CommandSource(source_name)
            current_commands = source.query(player)
            _compare_commands(username, previous=previous_commands, current=current_commands)

        if player.spreadsheet:
            _compare_spreadsheet(username, player.spreadsheet)

    logging.info(f"{len(players)} players checked")


def _compare_commands(username: str, previous: dict, current: dict):
    for cmd, msg in previous.items():
        new_msg = current.get(cmd)
        if msg != new_msg:
            logging.info(f"[{username}] [{cmd}]: {new_msg}")


def _compare_spreadsheet(username: str, spreadsheet_meta: dict):
    if spreadsheet_meta[SOURCE_KEY] != GOOGLE_SHEET_KEY:
        return

    for sheet in spreadsheet_meta[SHEETS_KEY]:
        _compare_sheet_hash(username, spreadsheet_meta, sheet)


def _compare_sheet_hash(username: str, spreadsheet_meta: dict, sheet: str):
    filename = f"{DATA_PATH}/{username}-{sheet}.csv"
    file_data = _try_get_file_data(filename)
    previous_hash = hashlib.md5(file_data).hexdigest()

    key = spreadsheet_meta["id"]
    export_url = f"https://docs.google.com/spreadsheets/d/{key}/export?format=csv&gid={sheet}"
    response = requests.get(export_url)
    current_hash = hashlib.md5(response.content).hexdigest()

    if previous_hash != current_hash:
        logging.info(f"[{username}]: {export_url}")
        _display_spreadsheet_diff(previous=file_data, current=response.content)
        _save_new_data(filename, response.content)


def _try_get_file_data(filename: str) -> bytes:
    try:
        with open(filename, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        data = bytes()

    return data


def _display_spreadsheet_diff(previous: bytes, current: bytes):
    a = previous.decode("utf-8").splitlines()
    b = current.decode("utf-8").splitlines()
    diff = difflib.unified_diff(a, b, fromfile="Previous", tofile="Current", lineterm="", n=0)
    delta = filter(lambda line: not any(line.startswith(prefix) for prefix in DIFF_CONTROL_PREFIXES), diff)
    [logging.info(f"\t\t{line}") for line in delta]


def _save_new_data(filename: str, new_data: bytes):
    with open(filename + ".new", "wb") as f:
        f.write(new_data)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    main()
