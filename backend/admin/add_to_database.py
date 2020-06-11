import json

DEFINITIONS_FILE = "../database.json"

NEW_USER = (
    "scump", {
        "commands": [
            {"command": "!grau", "message": "Monolithic Supressor, Tempus 26.4, Commando Foregrip, 60 Round, XRK Void II"},
            {"command": "!wzm4", "message": "stock m16, ranger foregrip, 60 round mag, mono supressor, stippled griptape"},
            {"command": "!mp5", "message": "MP5 Underbarrel: Operator Foregrip Ammunition: 10mm Auto 30-round Rear Grip: Stippled grip Perk: Sleight of Hand Stock: FTAC collapsible"}
        ],
        "guns": {
            "Grau": ["Monolithic Supressor", "Tempus 26.4", "Commando Foregrip", "60 Round", "XRK Void II"],
            "M4": ["stock m16", "ranger foregrip", "60 round mag", "mono supressor", "stippled griptape"],
            "MP5": ["Operator Foregrip", "10mm Auto 30-round", "Stippled grip", "Sleight of Hand", "FTAC collapsible"]
        }
    }
)


def main():
    with open(DEFINITIONS_FILE, 'r+') as file:
        database = json.load(file)
        add_user(database)
        save(file, database)


def add_user(database):
    key, value = NEW_USER
    database[key] = value


def save(file, database):
    file.seek(0)
    json.dump(database, file, indent=2)
    file.truncate()


if __name__ == '__main__':
    main()
