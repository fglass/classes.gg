from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import *
from model.weapon import Weapon

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    player = db.select_player("sweetsurrenderd")

    loadout = Weapon.MP5.value
    source = "https://www.reddit.com/r/MWLoadouts/comments/ho6wrp/warzone_loadout_1_of_the_updated_as_of_123_patch/"
    last_updated = datetime.now().isoformat()
    attachments = [
        # Muzzle.MONOLITHIC_SUPPRESSOR,
        Barrel.MONOLITHIC_INTEGRAL_SUPPRESSOR,
        # Laser.TAC_LASER,
        # Optic.SNIPER_SCOPE,
        Stock.FTAC_COLLAPSIBLE,
        Underbarrel.MERC_FOREGRIP,
        Ammunition.ROUND_MAGS_45,
        RearGrip.STIPPLED_GRIP_TAPE,
        # Perk.AKIMBO,
        # TriggerAction.LIGHTWEIGHT_TRIGGER
    ]

    # player.commands["!loadouts"] = "FIND ALL OF CLOAKZY'S LOADOUTS HERE --> https://docs.google.com/spreadsheets/d/1FYQxMLATGyzFPKppIva3_eEG0J1ulwNMcUoBKtUtWEw/edit?usp=sharing (UPDATED 7/10 W/ BRUEN)"

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
