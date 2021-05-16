import logging
from datetime import datetime
from typing import Optional, Tuple, Dict, List
from fuzzywuzzy import fuzz
from db.admin.change.command_source import CommandSource
from db.admin.change.detect_changes import SOURCE_KEY, ALL_COMMANDS
from db.json_database_engine import JSONDatabaseEngine
from model.player import Player
from model.weapon.new_attachment import *
from model.weapon.weapon import Weapon, AssaultRifle, LightMachineGun, MarksmanRifle, Pistol, Shotgun, SniperRifle, \
    SubmachineGun, TacticalRifle

DELIMITERS = [",", "-", "|"]
MIN_ATTACHMENTS = 4
MAX_ATTACHMENTS = 5
RATIO_THRESHOLD = 60

ALL_WEAPONS = list(AssaultRifle) + list(LightMachineGun) + list(MarksmanRifle) + list(Pistol) + list(Shotgun) + \
              list(SniperRifle) + list(SubmachineGun) + list(TacticalRifle)

WEAPON_COMMANDS = set(ALL_COMMANDS)  # TODO: use weapon aliases instead
[WEAPON_COMMANDS.remove(c) for c in {"class", "guns", "loadout", "loadout2", "loadouts"}]

DUAL_GAME_WEAPONS: Dict[Weapon, Weapon] = {
    AssaultRifle.AK_47: AssaultRifle.AK_47_CW,
    AssaultRifle.AK_47_CW: AssaultRifle.AK_47,
    SubmachineGun.MP5: SubmachineGun.MP5_CW,
    SubmachineGun.MP5_CW: SubmachineGun.MP5,
    SubmachineGun.AUG: TacticalRifle.AUG_CW,
    TacticalRifle.AUG_CW: SubmachineGun.AUG,
    AssaultRifle.M4A1: AssaultRifle.XM4,
    AssaultRifle.XM4: AssaultRifle.M4A1
}


def update_loadouts():
    db = JSONDatabaseEngine()
    players = db.select_players()
    success_count, failure_count = 0, 0

    for player in players:
        s, f = _update_player(player)
        success_count += s
        failure_count += f
        db.add_player(player, commit=False)

    db.commit()
    logging.info(f"Loadouts updated: {success_count} ✔ {failure_count} ❌")


def _update_player(player: Player):
    success_count, failure_count = 0, 0
    previous_commands = player.commands
    source_name = previous_commands.pop(SOURCE_KEY, None)

    if not source_name:
        return success_count, failure_count

    print(player.username)
    source = CommandSource(source_name)
    current_commands = source.query(player)

    for command in WEAPON_COMMANDS:

        response = current_commands[command] if command in current_commands else current_commands.get("!" + command)

        if response is None:
            continue

        updated = _update_command(player, command, response)

        if updated:
            success_count += 1
        else:
            failure_count += 1

    return success_count, failure_count


def _update_command(player: Player, command: str, response: str) -> bool:
    loadout = _find_loadout(command, response)

    if loadout is None:
        return False

    now = datetime.now().isoformat()
    weapon, attachments = loadout

    player.last_updated = now
    player.loadouts[str(weapon)] = {
        "attachments": {a.__class__.__name__: str(a) for a in attachments.keys()},
        "game": weapon.game.value,
        "lastUpdated": now,
        "source": response,
        "sourceUrl": f"https://www.twitch.tv/{player.username.lower()}",
    }

    print(f"\t{command}: {response}")
    print(f"\t\t-> {str(weapon)} ({weapon.game.value}): {[f'{str(a)} {r}%' for a, r in attachments.items()]}")
    return True


def _find_loadout(command: str, response: str) -> Optional[Tuple[Weapon, dict]]:
    weapon = find_weapon(command)

    if weapon is None:
        print(f"\tWeapon not found: {command}")
        return

    if len(weapon.attachments) == 0:
        print(f"\t{weapon} data missing")

    attachments = _find_attachments(weapon.attachments, response)

    if weapon in DUAL_GAME_WEAPONS:
        weapon, attachments = _compare_weapon_counterpart(weapon, attachments, response)

    if len(attachments) < MIN_ATTACHMENTS:
        return

    return weapon, attachments


def find_weapon(command: str) -> Optional[Weapon]:
    for weapon in ALL_WEAPONS:
        if any([alias in command for alias in weapon.aliases]):
            return weapon


def _find_attachments(valid_attachments: list, response: str) -> dict:
    attachments = {}
    delimiter = _find_delimiter(response)
    parts = response.split(delimiter)

    if len(parts) < MIN_ATTACHMENTS:
        return attachments

    for part in reversed(parts):  # TODO: check part isn't weapon

        attachment, ratio = _find_attachment(part, valid_attachments)

        if attachment is not None:
            attachments[attachment] = ratio

        if len(attachments) == MAX_ATTACHMENTS:
            break

    return attachments


def _find_delimiter(response: str) -> str:
    return max(DELIMITERS, key=lambda delimiter: response.count(delimiter))


def _find_attachment(part: str, valid_attachments: list) -> Tuple[Optional[NewAttachment], int]:
    if part == "":
        return None, 0

    part = part.strip().lower()
    matched_attachment = None
    max_ratio = 0

    for attachment in valid_attachments:

        if part == str(attachment).lower():
            return attachment, 100

        for alias in attachment.aliases:
            ratio = fuzz.partial_ratio(part, alias)

            if ratio >= max_ratio:
                matched_attachment = attachment
                max_ratio = ratio

    if max_ratio < RATIO_THRESHOLD:
        return None, 0

    return matched_attachment, max_ratio


def _compare_weapon_counterpart(weapon: Weapon, attachments: dict, response: str):
    weapon_counterpart = DUAL_GAME_WEAPONS[weapon]
    other_attachments = _find_attachments(weapon_counterpart.attachments, response)

    if len(other_attachments) >= len(attachments):
        first_total = sum(attachments.values())
        second_total = sum(other_attachments.values())

        if second_total > first_total:
            return weapon_counterpart, other_attachments

    return weapon, attachments


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    update_loadouts()
