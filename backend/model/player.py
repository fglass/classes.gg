class Player:
    def __init__(self, username: str, avatar: str, loadouts: dict, commands: dict):
        self.username = username
        self.avatar = avatar
        self.loadouts = loadouts
        self.commands = commands

    def get_command_source(self) -> str:
        return self.commands.get("source")

    def serialise(self) -> dict:
        return {
            "username": self.username,
            "avatar": self.avatar,
            "loadouts": self.loadouts,
            "commands": self.commands
        }
