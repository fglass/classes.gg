from backend.db.json_database_engine import JSONDatabaseEngine
from backend.model.attachment import Attachment
from backend.model.player import Player
from backend.model.weapon import Weapon
from datetime import datetime


NEW_PLAYER = Player(
    username="TeePee",
    avatar="https://static-cdn.jtvnw.net/jtv_user_pictures/baa7d2f5-3639-4296-ae30-f872c7e75d5b-profile_image-300x300.png",
    loadouts={
        Weapon.M4A1.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.RUBBERIZED_GRIP_TAPE.value,
                Attachment.ROUND_MAGS_60.value,
                Attachment.STOCK_M16_GRENADIER.value
            ]
        },
        Weapon.GRAU.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.TEMPUS_ARCHANGEL.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.TAC_LASER.value,
                Attachment.ROUND_MAGS_60.value
            ]
        },
        "Grau 5.56 V2": {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.TEMPUS_ARCHANGEL.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.VLK_3X_OPTIC.value,
                Attachment.ROUND_MAGS_60.value
            ]
        },
        Weapon.MP5.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_INTEGRAL_SUPPRESSOR.value,
                Attachment.TAC_LASER.value,
                Attachment.MERC_FOREGRIP.value,
                Attachment.SLEIGHT_OF_HAND.value,
                Attachment.ROUND_MAGS_45.value
            ]
        },
        Weapon.MP7.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_INTEGRAL_SUPPRESSOR.value,
                Attachment.FSS_RECON.value,
                Attachment.TAC_LASER.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.ROUND_MAGS_60.value
            ]
        },
        Weapon.FENNEC.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.ZLR_DEADFALl.value,
                Attachment.MERC_FOREGRIP.value,
                Attachment.ROUND_DRUM_MAGS_40.value,
                Attachment.SLEIGHT_OF_HAND.value,
                Attachment.TAC_LASER.value
            ]
        },
        Weapon.HDR.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.HDR_PRO.value,
                Attachment.TAC_LASER.value,
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.VARIABLE_ZOOM_SCOPE.value,
                Attachment.FTAC_STALKER_SCOUT.value
            ]
        },
        Weapon.AX_50.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.FACTORY_BARREL_32.value,
                Attachment.TAC_LASER.value,
                Attachment.STIPPLED_GRIP_TAPE.value,
                Attachment.SINGUARD_ARMS_EVADER.value
            ]
        },
        Weapon.M13.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.TEMPUS_MARKSMAN.value,
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.TAC_LASER.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.ROUND_MAGS_60.value
            ]
        },
        Weapon.AK_47.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.RPK_BARREL.value,
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.TAC_LASER.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.ROUND_MAGS_40.value
            ]
        },
        Weapon.PP19_BIZON.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.STEEL.value,
                Attachment.MONOLITHIC_INTEGRAL_SUPPRESSOR.value,
                Attachment.TAC_LASER.value,
                Attachment.NO_STOCK.value,
                Attachment.STIPPLED_GRIP_TAPE.value
            ]
        },
        Weapon.CR_56_AMAX.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.XRK_ZODIAC_S440.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.TAC_LASER.value,
                Attachment.ROUND_MAGS_45.value,
                Attachment.NO_STOCK.value
            ]
        },
        Weapon.FR.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.FR_SNIPER.value,
                Attachment.TAC_LASER.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.ROUND_MAGS_50.value
            ]
        },
        Weapon.HOLGER.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.RUBBERIZED_GRIP_TAPE.value,
                Attachment.TAC_LASER.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.NO_STOCK.value
            ]
        },
        Weapon.KILO_141.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.SINGUARD_ARMS_PROWLER.value,
                Attachment.VLK_3X_OPTIC.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.ROUND_MAGS_60.value
            ]
        },
        Weapon.ODEN.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.ODEN_FACTORY_810.value,
                Attachment.COLLOSUS_SUPPRESSOR.value,
                Attachment.TAC_LASER.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.SLEIGHT_OF_HAND.value
            ]
        },
        Weapon.P90.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.FORGE_TAC_RETRIBUTION.value,
                Attachment.TAC_LASER.value,
                Attachment.STIPPLED_GRIP_TAPE_U.value,
                Attachment.SLEIGHT_OF_HAND.value
            ]
        },
        Weapon.PKM.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.EXTENDED_BARREL.value,
                Attachment.TAC_LASER.value,
                Attachment.NO_STOCK.value,
                Attachment.SNATCH_GRIP.value
            ]
        },
        Weapon.RAM_7.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.ROUND_MAGS_50.value,
                Attachment.TAC_LASER.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.XRK_RANGER.value
            ]
        },
        Weapon.UZI.value: {
            "source": "https://tinyurl.com/teepeeattachments",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.FACTORY_CARBINE.value,
                Attachment.TAC_LASER.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.ROUND_MAGS_50.value
            ]
        },
    },
    commands={
        "!guns": "All of Teep's WZ classes are now in ONE place: https://tinyurl.com/teepeeattachments"
    }
)

if __name__ == '__main__':
    [v["attachments"].sort() for k, v in NEW_PLAYER.loadouts.items()]
    JSONDatabaseEngine().add_player(NEW_PLAYER)
    print(f"Added {NEW_PLAYER.username}")
