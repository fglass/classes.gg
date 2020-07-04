import logging

from db.admin.command.command_source import CommandSource
from db.admin.command.nightbot_api import query_nightbot
from db.admin.command.streamlabs_api import query_streamlabs
from db.json_database_engine import JSONDatabaseEngine


def main():
    db = JSONDatabaseEngine()
    players = db.select_players()

    for player in players:
        source = player.get_command_source()
        if source == CommandSource.NIGHTBOT.value:
            _compare_commands(player.username, previous=player.commands, current=query_nightbot(player))
        elif source == CommandSource.STREAMLABS.value:
            _compare_commands(player.username, previous=player.commands, current=query_streamlabs(player))
        # TODO: add stream elements API

    logging.info(f"{len(players)} players checked")


def _compare_commands(username: str, previous: dict, current: dict):
    for cmd, msg in previous.items():
        new_msg = current.get(cmd)
        if cmd != "source" and msg != new_msg:
            logging.info(f"[{username}] [{cmd}]: {new_msg}")


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    main()
