from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    warrior = EliteCard("Arcane Warrior", 6, "Legendary", 5, 5, 20, 10)

    goblin = CreatureCard("Goblin Warrior", 2, "Common", 3, 4)

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print(f"\nPlaying {warrior.name} (Elite Card):")
    game_state = {"player_mana": 8}
    print(f"Play result: {warrior.play(game_state)}")

    print("\nCombat phase:")
    attack_result = warrior.attack(goblin)
    print(f"Attack result: {attack_result}")

    defense_result = warrior.defend(3)
    print(f"Defense result: {defense_result}")

    print(f"Combat stats: {warrior.get_combat_stats()}")

    print("\nMagic phase:")
    spell_result = warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_result}")

    channel_result = warrior.channel_mana(3)
    print(f"Mana channel: {channel_result}")

    print(f"Magic stats: {warrior.get_magic_stats()}")

    print("\nTesting insufficient mana:")
    poor_state = {"player_mana": 2}
    print(f"Play result: {warrior.play(poor_state).get('Playable')}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
