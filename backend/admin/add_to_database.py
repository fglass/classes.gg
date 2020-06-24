from backend.db.json_database_engine import JSONDatabaseEngine
from backend.model.attachment import Attachment
from backend.model.player import Player
from backend.model.weapon import Weapon
from datetime import datetime


NEW_PLAYER = Player(
    username="jukeyzl",
    avatar="https://static-cdn.jtvnw.net/jtv_user_pictures/9a0369b8-d6e3-4ce3-a3fe-cbbf35cfb068-profile_image-300x300.png",
    loadouts={
        Weapon.GRAU.value: {
            "source": "https://www.twitch.tv/jukeyzl",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.ROUND_MAGS_50.value,
                Attachment.TAC_LASER.value,
                Attachment.TEMPUS_ARCHANGEL.value,
                Attachment.MONOLITHIC_SUPPRESSOR.value
            ]
        },
        Weapon.MP5.value: {
            "source": "https://www.twitch.tv/jukeyzl",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.MERC_FOREGRIP.value,
                Attachment.ROUND_MAGS_45.value,
                Attachment.SLEIGHT_OF_HAND.value,
                Attachment.FTAC_COLLAPSIBLE.value
            ]
        },
        Weapon.M4A1.value: {
            "source": "https://www.twitch.tv/jukeyzl",
            "lastUpdated": datetime.now().isoformat(),
            "attachments": [
                Attachment.MONOLITHIC_SUPPRESSOR.value,
                Attachment.NO_STOCK.value,
                Attachment.COMMANDO_FOREGRIP.value,
                Attachment.ROUND_MAGS_60.value,
                Attachment.STOCK_M16_GRENADIER.value
            ]
        },
    },
    commands={
        "!class": "🔫 Grau: Commando Foregrip • 50 Round Mags • Tac Laser • Tempus 26.4\" Archangel • Monolithic Supressor 🔫 MP5: Mono suppressor, Merc Foregrip, 45 rounds, Sleight of hand, ftac collapsible stock 🍆 PERKS: Double time overkill amped, switching to ghost on a second loadout and picking up his overkill class guns.",
        "!loadout": "🔫 Grau: Commando Foregrip • 50 Round Mags • Tac Laser • Tempus 26.4\" Archangel • Monolithic Supressor 🔫 MP5: Mono suppressor, Merc Foregrip, 45 rounds, Sleight of hand, ftac collapsible stock 🍆 PERKS: Double time overkill amped, switching to ghost on a second loadout and picking up his overkill class guns.",
        "!loadout2": "🔫 M4: Monolithic Supp, No Stock, Commando Grip, 60 Rounds, M16 Grenadier 🔫 MP5: Mono suppressor, Merc Foregrip, 45 rounds, Sleight of hand, ftac collapsible stock 🍆 PERKS: Double time overkill amped, switching to ghost on a second loadout and picking up his overkill class guns."
    }
)

if __name__ == '__main__':
    JSONDatabaseEngine().add_player(NEW_PLAYER)
