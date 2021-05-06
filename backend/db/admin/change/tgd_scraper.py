import requests


WEAPON_TYPES = ["AR", "LMG", "SMG", "MR", "SR"]
WEAPONS_URL = "https://www.truegamedata.com/SQL_calls/grab_guns.php"
ATTACHMENTS_URL = "https://www.truegamedata.com/SQL_calls/grab_attachment_names.php"


def scrape():
    for weapon_type in WEAPON_TYPES:
        weapon_payload = {"selectedGunType": f'["{weapon_type}", "wz"]'}
        response = requests.post(WEAPONS_URL, data=weapon_payload)

        for weapon in response.json():
            weapon = weapon[0]
            payload = {"selectedGun": f'["{weapon}", "wz"]'}
            response = requests.post(ATTACHMENTS_URL, data=payload)
            print(f"{weapon}: {response.json()}")


if __name__ == "__main__":
    scrape()
