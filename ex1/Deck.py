from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards_deck = []

    def add_card(self, card: Card) -> None:
        self.cards_deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        try:
            self.cards_deck.remove(card_name)
        except ValueError:
            raise ValueError(f"{card_name} not in your deck !!")

    def shuffle(self) -> None:
        n = len(self.cards_deck)
        if n <= 1:
            return
        import random
        if n == 2:
            self.cards_deck[0], self.cards_deck[1] = (self.cards_deck[1],
                                                      self.cards_deck[0])
            return

        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.cards_deck[i], self.cards_deck[j] = (self.cards_deck[j],
                                                      self.cards_deck[i])

        print("Your deck is shuffled")

    def draw_card(self) -> Card:
        try:
            card = self.cards_deck[0]
            self.cards_deck.pop(0)
            return card
        except Exception:
            raise ValueError("Your deck is empty!!")

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards_deck)
        creaters = 0
        spells = 0
        artifacts = 0
        avg_cost = 0

        for card in self.cards_deck:
            if card.__class__.__name__ == "CreatureCard":
                creaters += 1
            elif card.__class__.__name__ == "SpellCard":
                spells += 1
            elif card.__class__.__name__ == "ArtifactCard":
                artifacts += 1
            avg_cost += card.cost
        avg_cost = round(avg_cost / total_cards, 2)

        return {
            'total_cards': total_cards,
            'creatures': creaters,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': avg_cost,
        }
