from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, 10)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 5, 4, 8)
    knight = TournamentCard("Iron Knight", 3, "Common", 4, 6, 9)

    platform = TournamentPlatform()

    print("Registering Tournament Cards...")
    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)
    knight_id = platform.register_card(knight)

    for card_id, card in [
        (dragon_id, dragon),
        (wizard_id, wizard),
        (knight_id, knight)
    ]:
        info = card.get_rank_info()
        print(f"\n{card.name} (ID: {card_id}):")
        print("  - Interfaces: [Card, Combatable, Rankable]")
        print(f"  - Rating: {info['rating']}")
        print(f"  - Record: {info['record']}")

    print("\nCreating tournament matches...")
    match1 = platform.create_match(dragon_id, wizard_id)
    print(f"Match 1 result: {match1}")

    match2 = platform.create_match(wizard_id, knight_id)
    print(f"Match 2 result: {match2}")

    match3 = platform.create_match(dragon_id, knight_id)
    print(f"Match 3 result: {match3}")

    print("\nTournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(
            f"  {entry['rank']}. {entry['name']} "
            f"- Rating: {entry['rating']} "
            f"({entry['record']})"
        )

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    for key, val in report.items():
        print(f"  {key}: {val}")

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
