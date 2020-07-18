from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import *
from model.weapon import Weapon

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    player = db.select_player("cloakzy")

    loadout = Weapon.FAL.value
    source = "https://clips.twitch.tv/BovineAffluentReubenKappaClaus"
    last_updated = datetime.now().isoformat()
    attachments = [
        Muzzle.MONOLITHIC_SUPPRESSOR,
        Barrel.XRK_ZODIAC_S440,
        # Laser.TAC_LASER,
        Optic.CORP_COMBAT_HOLO_SIGHT,
        # Stock.FTAC_STALKER_SCOUT,
        Underbarrel.COMMANDO_FOREGRIP,
        Ammunition.ROUND_MAGS_45,
        # RearGrip.STIPPLED_GRIP_TAPE,
        # Perk.SLEIGHT_OF_HAND,
        # TriggerAction.LIGHTWEIGHT_TRIGGER
    ]

    player.commands["!loadouts"] = "FIND ALL OF CLOAKZY'S LOADOUTS HERE --> https://docs.google.com/spreadsheets/d/1FYQxMLATGyzFPKppIva3_eEG0J1ulwNMcUoBKtUtWEw/edit?usp=sharing (UPDATED 7/17 W/ BRUEN & FAL)"

    attachments = {attachment.get_type(): attachment.value for attachment in attachments}

    print(f"{loadout}:")
    if loadout in player.loadouts:
        previous_attachments = list(player.loadouts[loadout]["attachments"].values())
        sorted_keys = sorted(attachments)
        [print(f"\t{previous_attachments[i]} -> {attachments[sorted_keys[i]]}") for i in range(5)]
    else:
        [print(f"\t{attachment}") for attachment in attachments.values()]

    confirmation = input("Confirm? ")

    if confirmation == "y":
        player.loadouts[loadout] = {
            "source": source,
            "lastUpdated": last_updated,
            "attachments": attachments
        }
        db.add_player(player)
        print(f"Added {player.username}'s {loadout}")
