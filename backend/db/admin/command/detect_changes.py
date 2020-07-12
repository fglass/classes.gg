import logging

from db.admin.command.api.fossabot_api import query_fossabot
from db.admin.command.api.nightbot_api import query_nightbot
from db.admin.command.api.streamelements_api import query_streamelements
from db.admin.command.api.streamlabs_api import query_streamlabs
from db.admin.command.command_source import CommandSource
from db.json_database_engine import JSONDatabaseEngine


def main():
    db = JSONDatabaseEngine()
    players = db.select_players()

    for player in players:

        current_commands = []
        source = player.get_command_source()

        if source == CommandSource.FOSSABOT.value:
            current_commands = query_fossabot(player)
        elif source == CommandSource.NIGHTBOT.value:
            current_commands = query_nightbot(player)
        elif source == CommandSource.STREAMELEMENTS.value:
            current_commands = query_streamelements(player)
        elif source == CommandSource.STREAMLABS.value:
            current_commands = query_streamlabs(player)

        _compare_commands(player.username, previous=player.commands, current=current_commands)

    logging.info(f"{len(players)} players checked")


def _compare_commands(username: str, previous: dict, current: dict):
    for cmd, msg in previous.items():
        new_msg = current.get(cmd)
        if msg != new_msg and cmd != "source":
            logging.info(f"[{username}] [{cmd}]: {new_msg}")


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    main()
