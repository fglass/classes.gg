class Player:
    def __init__(self, username: str, weapons: dict, commands: dict):
        self.username = username
        self.weapons = weapons
        self.commands = commands

    def serialise(self) -> dict:
        return {
            "weapons": self.weapons,
            "commands": self.commands
        }
