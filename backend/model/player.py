class Player:
    def __init__(self, username: str, avatar: str, loadouts: dict, commands: dict, spreadsheet: dict):
        self.username = username
        self.avatar = avatar
        self.loadouts = loadouts
        self.commands = commands
        self.spreadsheet = spreadsheet

    def serialise(self) -> dict:
        return {
            "username": self.username,
            "avatar": self.avatar,
            "loadouts": self.loadouts,
            "commands": self.commands,
            "spreadsheet": self.spreadsheet
        }
