from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex1.Deck import Deck


class GameEngine:

    def __init__(self) -> None:
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._deck: Deck = Deck()
        self._hand: list = []
        self._battlefield: list = []
        self._turns_simulated: int = 0
        self._total_damage: int = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self._factory = factory
        self._strategy = strategy

        supported = factory.get_supported_types()
        creatures = supported.get('creatures', [])
        spells = supported.get('spells', [])
        artifacts = supported.get('artifacts', [])

        self._deck = Deck()
        self._deck.add_card(factory.create_creature(
            creatures[0] if creatures else None)
        )
        self._deck.add_card(factory.create_creature(
            creatures[1] if len(creatures) > 1 else None)
        )
        self._deck.add_card(factory.create_spell(
            spells[0] if spells else None)
        )
        self._deck.add_card(factory.create_artifact(
            artifacts[0] if artifacts else None)
        )

        self._deck.shuffle()

        self._hand = []
        for _ in range(len(self._deck.cards_deck)):
            self._hand.append(self._deck.draw_card())

    def simulate_turn(self) -> dict:
        if not self._factory or not self._strategy:
            raise RuntimeError(
                "Engine not configured. Call configure_engine first."
            )
        hand_summary = [f"{c.name} ({c.cost})" for c in self._hand]
        result = self._strategy.execute_turn(self._hand, self._battlefield)
        self._turns_simulated += 1
        self._total_damage += result.get('damage_dealt', 0)
        return {
            'hand': hand_summary,
            'turn_execution': result,
        }

    def get_engine_status(self) -> dict:

        return {
            'turns_simulated': self._turns_simulated,
            'strategy_used': (
                self._strategy.get_strategy_name()
                if self._strategy else None
            ),
            'total_damage': self._total_damage,
            'cards_created': len(self._hand),
            'deck_stats': self._deck.get_deck_stats(),
        }
