class Player:
    def __init__(
        self,
        username: str,
        avatar: str,
        command_source: str,
        last_updated: str,
        loadouts: dict,
        spreadsheet: dict,
        views: int
    ):
        self.username = username
        self.avatar = avatar
        self.command_source = command_source
        self.last_updated = last_updated
        self.loadouts = loadouts
        self.spreadsheet = spreadsheet
        self.views = views

    def serialise(self) -> dict:
        return {
            "username": self.username,
            "avatar": self.avatar,
            "command_source": self.command_source,
            "last_updated": self.last_updated,
            "loadouts": self.loadouts,
            "spreadsheet": self.spreadsheet,
            "views": self.views
        }
