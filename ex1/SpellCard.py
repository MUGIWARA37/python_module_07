from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


def positive_random() -> int:
    import random
    return random.randint(0, 100)


def generate_effect_msg(effect_type: str, effect_num: int) -> str:
    if effect_type == 'damage':
        return f"Dealing {effect_num} damage to all targets!"
    elif effect_type == 'heal':
        return f"Healing all targets by +{effect_num}!"
    elif effect_type == 'buff':
        return f"Buffing all targets' attack by {effect_num}!"
    elif effect_type == 'debuff':
        return f"Debuffing all targets' attack by {effect_num}!"
    return "Unknown effect!"


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.use_time = 1
        self.type = "Spell"
        if effect_type not in ('damage', 'heal', 'buff', 'debuff'):
            raise ValueError(
                "Spell Lost in the Void!! (incorrect effect_type)"
            )

        self.effect_type = effect_type
        self.effect_num = positive_random()
        self.effect_msg = generate_effect_msg(self.effect_type,
                                              self.effect_num)

    def resolve_effect(self, targets: list[CreatureCard]) -> dict:
        creature_status = {}

        if self.effect_type == 'damage':
            for target in targets:
                target.health = max(0, target.health - self.effect_num)
            creature_status[target.name] = f"{self.effect_msg} for"
            f"{target.name}"

        elif self.effect_type == 'heal':
            for target in targets:
                target.health += self.effect_num
            creature_status[target.name] = f"{self.effect_msg} for"
            f"{target.name}"

        elif self.effect_type == 'buff':
            for target in targets:
                target.attack += self.effect_num
            creature_status[target.name] = f"{self.effect_msg} for"
            f"{target.name}"

        elif self.effect_type == 'debuff':
            for target in targets:
                target.attack = max(1, target.attack - self.effect_num)
            creature_status[target.name] = f"{self.effect_msg} for"
            f"{target.name}"

        return creature_status

    def play(self, game_state: dict) -> dict:
        try:
            mana = game_state['player_mana']
        except Exception:
            raise ValueError("Invalid game_state dict")

        if not super().is_playable(mana) or self.use_time <= 0:
            return {'Playable': False}

        status = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect_msg
        }

        return {
            'Playable': True,
            'Play result': status
        }
