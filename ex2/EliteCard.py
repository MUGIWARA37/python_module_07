from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 defense: int, health: int, mana_pool: int):
        Card.__init__(self, name, cost, rarity)
        self.attack_power = attack
        self.defense = defense
        self.health = health
        self.mana_pool = mana_pool
        self._total_mana = mana_pool

    def attack(self, target: CreatureCard) -> dict:
        target.health = max(0, target.health - self.attack_power)
        if target.health == 0:
            print(f"{target.name.upper()} IS NO MORE !!")
        return {'attacker': self.name, 'target': target.name,
                'damage': self.attack_power, 'combat_type': 'melee'}

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

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = len(targets) if targets else 1
        self._total_mana = max(0, self._total_mana - mana_cost)
        target_names = [
            t if isinstance(t, str) else t.name for t in targets
        ]
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': target_names,
            'mana_used': mana_cost,
        }

    def channel_mana(self, amount: int) -> dict:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._total_mana += amount
        return {
            'channeled': amount,
            'total_mana': self._total_mana,
        }

    def get_magic_stats(self) -> dict:
        return {
            'mana_pool': self.mana_pool,
            'current_mana': self._total_mana,
        }

    def play(self, game_state: dict) -> dict:
        try:
            mana = game_state["player_mana"]
        except Exception:
            raise ValueError("Please Check the Game_status dict"
                             "provided invalide")
        if not super().is_playable(mana):
            return {"Playable": False}
