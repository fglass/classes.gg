from enum import Enum
from model.game import Game


class Weapon(Enum):

    def __init__(self, name: str, game: Game, aliases: list = None, attachments: list = None):
        self._name = name
        self._game = game
        self._aliases = aliases if aliases else []
        self._attachments = attachments if attachments else []

    def __str__(self):
        return self._name

    @property
    def attachments(self) -> list:
        return self._attachments

    @property
    def aliases(self) -> list:
        return [self._name.lower()] + self._aliases