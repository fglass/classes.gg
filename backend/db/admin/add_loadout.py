from datetime import datetime

from db.json_database_engine import JSONDatabaseEngine
from model.attachment import *
from model.weapon import Weapon

if __name__ == '__main__':
    db = JSONDatabaseEngine()
    player = db.select_player("icemanisaac")

    loadout = Weapon.FENNEC.value
    source = "https://www.twitch.tv/icemanisaac"
    last_updated = datetime.now().isoformat()
    attachments = [
        Muzzle.ZLR_SABRE,
        # Barrel.HDR_PRO,
        # Laser.TAC_LASER,
        # Optic.VLK_3X_OPTIC,
        # Stock.FTAC_STALKER_SCOUT,
        Underbarrel.MERC_FOREGRIP,
        Ammunition.ROUND_DRUM_MAGS_40,
        RearGrip.STIPPLED_GRIP_TAPE,
        Perk.SLEIGHT_OF_HAND,
        # TriggerAction.LIGHTWEIGHT_TRIGGER
    ]

    player.commands["!bruen"] = "Isaac hasn't made his own build for this gun yet! The guns he does have a build for are the: Ram-7, Grau, Galil, MP7, MP5, Vector and the HDR!"
    player.commands["!fennec"] = "ZLR Sabre Barrel, Merc Foregrip, 40 Round Drum Mags, Stippled Grip Tape and Sleight of Hand (this is temporary until he unlocks all attachments for the Vector)"

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
