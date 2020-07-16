from abc import ABC, abstractmethod
from model.player import Player
from typing import Optional, ValuesView


class DatabaseEngine(ABC):

    @abstractmethod
    def select_player(self, username: str) -> Optional[Player]:
        pass

    @abstractmethod
    def select_players(self) -> ValuesView[Player]:
        pass

    @abstractmethod
    def add_player(self, player: Player):
        pass
