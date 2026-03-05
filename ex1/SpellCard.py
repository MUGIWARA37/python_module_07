from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.use_time = 1
        if effect_type not in ('damage', 'heal', 'buff', 'debuff'):
            raise ValueError("Spell Lost in the Void!!(inccorect effect_type)"
                             "use the one of the next typs "
                             "(damage, heal, buff, debuff)")
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        try:
            mana = game_state["player_mana"]
        except Exception:
            raise ValueError("Please Check the Game_status dict"
                             "provided invalide")
        if not (super().is_playable(mana) or
                self.use_time <= 0):
            return {'Playable': False}
        return {'Playable': True}

    def resolve_effect(self, targets: list[CreatureCard]) -> dict:
        def positive_random(a: int, b: int) -> int:
            lower = max(1, min(a, b))
            upper = max(a, b)
            return lower + (id(object()) % (upper - lower + 1))

        effect_num = positive_random(self.cost, sum(t.cost for t in targets))

        if self.effect_type == 'damage':
            effect_msg = f"Dealing {effect_num} damage to all targets!"
            for target in targets:
                if max(0, target.health - effect_num) == 0:
                    target.health = 0
                    print(f"{target.name.upper()} IS NO MORE !!")

        elif self.effect_type == 'heal':
            effect_msg = f"Healing all targets by +{effect_num}!"
            for target in targets:
                target.health += effect_num

        elif self.effect_type == 'buff':
            effect_msg = f"Buffing all targets' attack by {effect_num}!"
            for target in targets:
                target.attack += effect_num

        elif self.effect_type == 'debuff':
            effect_msg = f"Debuffing all targets' attack by {effect_num}!"
            for target in targets:
                target.attack = max(1, target.attack - effect_num)

        else:
            effect_msg = "Unknown effect!"

        print(effect_msg)

        status = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': effect_msg
        }
        return status
