import json
from typing import Type
from model.weapon.attachment import Attachment, Muzzle, Barrel, Underbarrel, Optic, Ammunition, RearGrip, \
     Stock, Perk, Laser, Arms, Bolt, Cable, BoltAssembly

WEAPON_DATA_FILE = "model/weapon/weapon-data.json"
CATEGORIES = {category.__name__: category for category in {
    Muzzle, Barrel, Underbarrel, Optic, Ammunition, RearGrip, Stock, Perk, Laser, Arms, Bolt, Cable, BoltAssembly
}}


def _load_weapon_data():
    weapon_data = {}

    with open(WEAPON_DATA_FILE, "r+") as f:
        dump = json.load(f)

        for weapon, groups in dump.items():
            weapon_data[weapon] = []

            for attachment_group, attachments in groups.items():
                category = get_attachment_category(attachment_group)

                for attachment_name in attachments:
                    attachment = category[attachment_name]
                    weapon_data[weapon].append(attachment)

    return weapon_data


def get_attachment_category(slot: str) -> Type[Attachment]:
    slot = slot.replace(" ", "")
    return CATEGORIES[slot]


WEAPON_DATA = _load_weapon_data()
