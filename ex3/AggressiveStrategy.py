from .GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard


def sort_by_cost(hand: list) -> list:

    remaining = hand[:]
    sorted_hand = []
    while remaining:
        cheapest = remaining[0]
        for card in remaining:
            if card.cost < cheapest.cost:
                cheapest = card
        sorted_hand.append(cheapest)
        remaining.remove(cheapest)
    return sorted_hand


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        players = [t for t in available_targets if t == "Enemy Player"]
        creatures = [t for t in available_targets if t != "Enemy Player"]
        return players + creatures

    def execute_turn(self, hand: list, battlefield: list) -> dict:

        hand = sort_by_cost(hand)
        mana_available = sum(c.cost for c in hand)
        mana_used = 0
        cards_played = []
        damage = 0
        game_state = {"player_mana": mana_available}

        for card in hand:
            if mana_used + card.cost > mana_available:
                break
            result = card.play(game_state)
            if not result.get("Playable"):
                continue
            cards_played.append(card.name)
            mana_used += card.cost
            if isinstance(card, CreatureCard):
                damage += card.attack

        targets = self.prioritize_targets(["Enemy Player"] + battlefield)

        return {
            'strategy': self.get_strategy_name(),
            'cards_played': cards_played,
            'mana_used': mana_used,
            'mana_remaining': mana_available - mana_used,
            'targets_attacked': targets[:1],
            'damage_dealt': damage
        }
