from .CreatureCard import CreatureCard


if __name__ == "__main__":
    try:
        player1 = {"name": "Reda", "player_mana": 100}
        player2 = {"name": "Yassin", "player_mana": 3}
        print("\n=== DataDeck Card Foundation ===")

        dragon = CreatureCard("Fire Dragon", 5, "Legendary", 5, 5)
        goblin = CreatureCard("Goblin Warrior", 2, "Epic", 4, 6)

        print("CreatureCard Info:")
        print(dragon.get_card_info(), end="\n\n")

        next_play = dragon.play(player1)
        print(f"Playing {dragon.name} with {player1['player_mana']} available")
        print(f"From the lande across the fog i calle you my {dragon.name}"
              " turn my enemies to ashes !!")
        print(f"Playable: {next_play['Playable']}")
        print(f"Play result: {next_play['Play result']}")

        print(f"\n{dragon.name} attacks {goblin.name}:")
        print(f"Attack result: {dragon.attack_target(goblin)}")

        try:
            next_play = dragon.play(player2)
            print(f"\nPlaying {dragon.name} with "
                  f"{player2['player_mana']} available")

            print(f"Playable: {next_play['Playable']}")
            print(f"Play result: {next_play['Play result']}")
        except Exception:
            pass
        print("\nAbstract pattern successfully demonstrated!")
    except Exception as e:
        print(e)
