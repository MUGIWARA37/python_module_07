from .SpellCard import SpellCard, CreatureCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck

if __name__ == "__main__":
    try:
        print("\n=== DataDeck Deck Builder ===\n")

        player1 = {"name": "Reda", "player_mana": 100}
        deck = Deck()

        # Spells
        deck.add_card(SpellCard('Ice Shard', 2, 'Rare', 'damage'))
        deck.add_card(SpellCard('Healing Light', 4, 'Epic', 'heal'))
        deck.add_card(SpellCard('Wind Gust', 1, 'Common', 'debuff'))
        deck.add_card(SpellCard('Lightning Bolt', 3, 'Legendary', 'damage'))
        deck.add_card(SpellCard('Earthquake', 5, 'Epic', 'damage'))

        # Artifacts
        deck.add_card(ArtifactCard('Dragon Scale Shield', 5, 'Legendary', 8,
                                   '+20% defense for dragon creatures'))
        deck.add_card(ArtifactCard('Mana Crystal', 3, 'Rare', 2,
                                   '+5 mana per turn'))
        deck.add_card(ArtifactCard('Shadow Amulet', 2, 'Epic', 1,
                                   'Increase stealth of all creatures'))
        deck.add_card(ArtifactCard('Phoenix Feather', 4, 'Rare', 3,
                                   'Revive 1 creature'))

        # Creatures
        deck.add_card(CreatureCard('Water Serpent', 3, 'Rare', 6, 8))
        deck.add_card(CreatureCard('Earth Golem', 6, 'Epic', 15, 25))
        deck.add_card(CreatureCard('Thunder Phoenix', 4, 'Legendary', 12, 18))
        deck.add_card(CreatureCard('Goblin Scout', 1, 'Common', 2, 3))
        deck.add_card(CreatureCard('Forest Elf', 2, 'Rare', 3, 4))
        deck.add_card(CreatureCard('Necromancer', 5, 'Epic', 8, 12))
        deck.add_card(CreatureCard('Fire Dragon', 5, 'Legendary', 10, 20))
        deck.add_card(CreatureCard('Ice Golem', 4, 'Rare', 7, 10))

        # Targets for spell effects
        targets = [
            CreatureCard("Fire Dragon", 5, "Legendary", 5, 5),
            CreatureCard("Goblin Warrior", 5, "Epic", 5, 5),
            CreatureCard("Desert Eagle", 5, "Common", 5, 2)
        ]

        print("Building deck with different card typespass")
        print(f"Deck stats: {deck.get_deck_stats()}\n")

        deck.shuffle()
        for card in deck.cards_deck:
            print(f"Drew: {card.name} ({card.type})")
            play_result = card.play(player1)
            print(f"Play result: {play_result.get('Play result')}\n")
            if isinstance(card, SpellCard):
                card.resolve_effect(targets)

        print("Polymorphism in action: Same interface, "
              "different card behaviors!")

    except Exception as e:
        print(f"Error: {e}")
