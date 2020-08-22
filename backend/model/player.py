class Player:
    def __init__(self, username: str, avatar: str, last_updated: str, loadouts: dict, commands: dict, spreadsheet: dict):
        self.username = username
        self.avatar = avatar
        self.last_updated = last_updated
        self.loadouts = loadouts
        self.commands = commands
        self.spreadsheet = spreadsheet

    def serialise(self) -> dict:
        return {
            "username": self.username,
            "avatar": self.avatar,
            "last_updated": self.last_updated,
            "loadouts": self.loadouts,
            "commands": self.commands,
            "spreadsheet": self.spreadsheet
        }
