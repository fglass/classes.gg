import json
from enum import Enum
from typing import Type

from model.game import Game
from model.weapon.new_attachment import *

WEAPON_DATA = {}


class Weapon(Enum):

    def __init__(self, name: str, game: Game, aliases: list = None):
        self._name = name
        self._game = game
        self._aliases = aliases if aliases else []

    def __str__(self):
        return self._name

    @property
    def aliases(self) -> list:
        return [self._name.lower()] + self._aliases

    @property
    def attachments(self) -> list:
        if len(WEAPON_DATA) == 0:
            _load_weapon_data()
        return WEAPON_DATA[self.name] if self.name in WEAPON_DATA else []


def _load_weapon_data():
    global WEAPON_DATA  # TODO: refactor into separate file

    with open("model/weapon/weapon-data.json", "r+") as f:
        dump = json.load(f)

        for weapon, groups in dump.items():
            WEAPON_DATA[weapon] = []

            for attachment_group, attachments in groups.items():
                category = get_attachment_category(attachment_group)

                for attachment_name in attachments:
                    attachment = category[attachment_name]
                    WEAPON_DATA[weapon].append(attachment)


def get_attachment_category(slot: str) -> Type[NewAttachment]:
    if slot == "Muzzle":
        return Muzzle
    if slot == "Barrel":
        return Barrel
    if slot == "Underbarrel":
        return Underbarrel
    if slot == "Optic":
        return Optic
    if slot == "Ammunition":
        return Ammunition
    if slot == "Rear Grip" or slot == "RearGrip":
        return RearGrip
    if slot == "Stock":
        return Stock
    if slot == "Perk":
        return Perk
    if slot == "Laser":
        return Laser
    if slot == "Arms":
        return Arms
    if slot == "Bolt":
        return Bolt
    if slot == "Cable":
        return Cable
    if slot == "Bolt Assembly" or slot == "BoltAssembly":
        return BoltAssembly
