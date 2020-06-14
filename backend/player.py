class Player:
    def __init__(self, username: str, avatar: str, weapons: dict, commands: dict):
        self.username = username
        self.avatar = avatar
        self.weapons = weapons
        self.commands = commands

    def serialise(self) -> dict:
        return {
            "username": self.username,
            "avatar": self.avatar,
            "weapons": self.weapons,
            "commands": self.commands
        }
