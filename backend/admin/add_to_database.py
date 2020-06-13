from backend.db.json_database_engine import JSONDatabaseEngine
from backend.player import Player

NEW_PLAYER = Player(
    username="georgina",
    weapons={
        "Grau": ["Monolithic Supressor", "Tempus 26.4", "Commando Foregrip", "60 Round", "XRK Void II"],
        "M4": ["stock m16", "ranger foregrip", "60 round mag", "mono supressor", "stippled griptape"],
        "MP5": ["Operator Foregrip", "10mm Auto 30-round", "Stippled grip", "Sleight of Hand", "FTAC collapsible"]
    },
    commands={
        "!grau": "Monolithic Supressor, Tempus 26.4, Commando Foregrip, 60 Round, XRK Void II",
        "!wzm4": "stock m16, ranger foregrip, 60 round mag, mono supressor, stippled griptape",
        "!mp5": "MP5 Underbarrel: Operator Foregrip Ammunition: 10mm Auto 30-round Rear Grip: Stippled grip Perk: Sleight of Hand Stock: FTAC collapsible"
    }
)

if __name__ == '__main__':
    JSONDatabaseEngine().add_player(NEW_PLAYER)
