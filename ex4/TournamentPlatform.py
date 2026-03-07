import random
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self) -> None:
        self._cards: dict = {}
        self._matches: list = []

    def register_card(self, card: TournamentCard) -> str:

        card_id = (f"{card.name.lower().replace(' ', '_')}"
                   f"_{len(self._cards):03}")
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:

        if card1_id not in self._cards:
            raise ValueError(f"{card1_id} is not registered")
        if card2_id not in self._cards:
            raise ValueError(f"{card2_id} is not registered")

        card1 = self._cards[card1_id]
        card2 = self._cards[card2_id]

        score1 = card1.attack_power + card1.health + random.randint(0, 5)
        score2 = card2.attack_power + card2.health + random.randint(0, 5)

        if score1 >= score2:
            winner, loser = card1_id, card2_id
        else:
            winner, loser = card2_id, card1_id

        self._cards[winner].update_wins(1)
        self._cards[loser].update_losses(1)

        result = {
            'winner': winner,
            'loser': loser,
            'winner_rating': self._cards[winner].calculate_rating(),
            'loser_rating': self._cards[loser].calculate_rating(),
        }
        self._matches.append(result)
        return result

    def get_leaderboard(self) -> list:

        ranked = sorted(
            self._cards.items(),
            key=lambda item: item[1].calculate_rating(),
            reverse=True,
        )
        leaderboard = []
        for rank, (card_id, card) in enumerate(ranked, start=1):
            info = card.get_rank_info()
            leaderboard.append({
                'rank': rank,
                'id': card_id,
                'name': info['name'],
                'rating': info['rating'],
                'record': info['record']
            })
        return leaderboard

    def generate_tournament_report(self) -> dict:

        ratings = [c.calculate_rating() for c in self._cards.values()]
        avg_rating = round(sum(ratings) / len(ratings), 0) if ratings else 0
        return {
            'total_cards': len(self._cards),
            'matches_played': len(self._matches),
            'avg_rating': int(avg_rating),
            'platform_status': 'active',
        }
