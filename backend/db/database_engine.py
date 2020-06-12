from abc import ABC, abstractmethod
from backend.player import Player


class DatabaseEngine(ABC):

    @abstractmethod
    def add_player(self, player: Player):
        pass

    @abstractmethod
    def select_player(self, username: str) -> Player:
        pass

    @abstractmethod
    def select_players(self) -> list:
        pass

