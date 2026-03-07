from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    BASE_RATING = 1000

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, defense: int, health: int) -> None:
        Card.__init__(self, name, cost, rarity)
        self.attack_power = attack
        self.defense = defense
        self.health = health
        self._wins = 0
        self._losses = 0
        self._rating = self.BASE_RATING + (attack * 10) + (health * 5)

    def play(self, game_state: dict) -> dict:

        try:
            mana = game_state["player_mana"]
        except KeyError:
            raise ValueError("game_state must contain 'player_mana'")
        if not super().is_playable(mana):
            return {"Playable": False}
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Tournament card deployed',
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['type'] = 'Tournament'
        info['attack_power'] = self.attack_power
        info['defense'] = self.defense
        info['health'] = self.health
        return info

    def attack(self, target) -> dict:

        target_name = target if isinstance(target, str) else target.name
        if not isinstance(target, str):
            target.health = max(0, target.health - self.attack_power)
            if target.health == 0:
                print(f"{target_name.upper()} IS NO MORE !!")
        return {
            'attacker': self.name,
            'target': target_name,
            'damage': self.attack_power,
            'combat_type': 'tournament',
        }

    def defend(self, incoming_damage: int) -> dict:

        blocked = min(self.defense, incoming_damage)
        overflow = incoming_damage - blocked
        self.defense = max(0, self.defense - incoming_damage)
        if self.defense == 0:
            print(f"{self.name.upper()} IS VULNERABLE !!")
        self.health = max(0, self.health - overflow)
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': blocked,
            'still_alive': self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack_power': self.attack_power,
            'defense': self.defense,
            'health': self.health,
            'is_vulnerable': self.defense == 0,
            'still_alive': self.health > 0,
        }

    def calculate_rating(self) -> int:

        self._rating = (
            self.BASE_RATING
            + (self.attack_power * 10)
            + (self.health * 5)
            + (self._wins * 16)
            - (self._losses * 16)
        )
        return self._rating

    def update_wins(self, wins: int) -> None:
        self._wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self._losses += losses
        self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {
            'name': self.name,
            'rating': self.calculate_rating(),
            'wins': self._wins,
            'losses': self._losses,
            'record': f"{self._wins}-{self._losses}",
        }

    def get_tournament_stats(self) -> dict:
        stats = {}
        for key, val in self.get_card_info().items():
            stats[key] = val
        for key, val in self.get_rank_info().items():
            stats[key] = val
        for key, val in self.get_combat_stats().items():
            stats[key] = val
        return stats
