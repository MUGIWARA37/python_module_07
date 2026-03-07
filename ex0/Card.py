from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = Rarity(rarity)

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def is_playable(self, available_mana: int) -> bool:
        return self.cost <= available_mana

    def get_card_info(self) -> dict:
        return {
            "Card Name": self.name,
            "Card Mana": self.cost,
            "Card Rarity": self.rarity.value,
        }
