import json
import re
import requests
from db.admin.change.loadout_updater import find_weapon
from model.weapon.weapon_data_loader import get_attachment_category

WEAPON_TYPES = ["AR", "LMG", "SMG", "MR", "SR"]
WEAPONS_URL = "https://www.truegamedata.com/SQL_calls/grab_guns.php"
ATTACHMENTS_URL = "https://www.truegamedata.com/SQL_calls/grab_attachment_names.php"
TGD_DUMP_FILE = "tgd-dump.json"
WEAPON_DATA_FILE = "../../../model/weapon/weapon-data.json"


def dump_tgd():
    weapon_data = {}

    for weapon_type in WEAPON_TYPES:
        weapon_payload = {"selectedGunType": f'["{weapon_type}", "wz"]'}
        response = requests.post(WEAPONS_URL, data=weapon_payload)

        for weapon in response.json():
            weapon = weapon[0]
            weapon_data[weapon] = {}
            print(f"Processing {weapon}")

            payload = {"selectedGun": f'["{weapon}", "wz"]'}
            response = requests.post(ATTACHMENTS_URL, data=payload)
            attachments = response.json()

            for attachment_info in attachments:
                attachment = attachment_info["attachment"]
                slot = attachment_info["slot"]

                if slot not in weapon_data[weapon]:
                    weapon_data[weapon][slot] = []

                weapon_data[weapon][slot].append(attachment)

    with open(TGD_DUMP_FILE, "w") as f:
        json.dump(weapon_data, f, indent=4, sort_keys=True)


def dump_to_enum_classes():
    with open(TGD_DUMP_FILE, "r+") as f:
        tgd_dump = json.load(f)

    categories = {}

    for weapon, data in tgd_dump.items():
        for category, attachments in data.items():

            if category not in categories:
                categories[category] = set()

            for attachment in attachments:
                categories[category].add(attachment)

    for category, attachments in categories.items():
        print(f"\nclass {category}(NewAttachment):")
        formatted_attachments = []
        for attachment in attachments:
            formatted = attachment.upper().replace(" ", "_").replace("-", "_").replace(".", "")

            if formatted[0].isdigit():
                split = formatted.split("_")
                start = split.pop(0)
                split.append(start)
                formatted = "_".join(split)

            formatted_attachments.append((formatted, attachment))

        for (formatted, attachment) in sorted(formatted_attachments, key=lambda a: a[0]):
            print(f"\t{formatted} = \"{attachment}\"")


def dump_to_weapon_data():
    with open(TGD_DUMP_FILE, "r+") as f:
        tgd_dump = json.load(f)

    weapon_data = {}
    error_count = 0

    for weapon_name, data in tgd_dump.items():

        weapon = find_weapon(weapon_name.lower())
        weapon = weapon.name if weapon is not None else weapon_name.upper()

        if weapon in weapon_data:
            weapon = weapon_name.upper()

        weapon_data[weapon] = {}

        for category_name, attachments in data.items():
            category = get_attachment_category(category_name)

            for attachment in attachments:
                formatted_attachment = re.sub(r"\(.*\)", "", attachment).strip()
                try:
                    typed_attachment = category(formatted_attachment).name

                    if category.__name__ not in weapon_data[weapon]:
                        weapon_data[weapon][category.__name__] = []

                    weapon_data[weapon][category.__name__].append(typed_attachment)
                except ValueError:
                    print(f"ERROR: [{weapon}] {formatted_attachment}")
                    error_count += 1

    with open(WEAPON_DATA_FILE, "w") as f:
        json.dump(weapon_data, f, indent=4, sort_keys=True)

    print(f"Dumped {WEAPON_DATA_FILE} with {error_count} errors")


if __name__ == "__main__":
    dump_tgd()
    # dump_to_enum_classes()
    # dump_to_weapon_data()
