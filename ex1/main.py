from .SpellCard import SpellCard, CreatureCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck


def spells_caller(spell: SpellCard, player: dict) -> None:
    print(f"Drew: {spell.name} (Spell)")
    if spell.play(player).get('Playable'):
        print(f"Play result: {spell.resolve_effect(targets)}")
        spell.use_time = 0
    else:
        print("Not enaught mana to use the spell!")


def artifact_caller(artifact: ArtifactCard) -> None:
    print(f"\nDrew: {artifact.name} (Artifact)")
    if artifact.durability <= 0:
        print(f"{artifact.name} lost it's power you can't use it any more !!")
    elif artifact.play(player1).get('Playable'):
        print(f"Play result: {artifact.activate_ability()}")
        artifact.durability -= 1
    else:
        print("Not enaught Mana ")


def creature_summoning(creature: CreatureCard, player: dict) -> None:
    print(f"\nDrew: {creature.name} (Creature)")
    if creature.health <= 0:
        print(f"{creature.name} is Dead !!")
    elif creature.play(player).get('Playable'):
        print(f"Play result: {creature.play(player).get('Play result')}")


if __name__ == "__main__":
    try:
        print("\n=== DataDeck Deck Builder ===\n")

        player1 = {"name": "Reda", "player_mana": 100}
        deck = Deck()
        deck.add_card(SpellCard('Lightning Bolt', 3, 'Legendary', 'damage'))
        deck.add_card(ArtifactCard('Fire Scorpian Charme', 2, 'Commone', 10,
                      '+10% to Fire Damage'))
        deck.add_card(CreatureCard('Fire Dragon', 5, 'Legendary', 10, 20))

        targets = [
            CreatureCard("Fire Dragon", 5, "Legendary", 5, 5),
            CreatureCard("Goblin Warrior", 5, "Epic", 5, 5),
            CreatureCard("Desert Eagle", 5, "Commone", 5, 2)
        ]

        print("\nDrawing and playing cards:\n")
        spells_caller(deck.draw_card, player1)

        artifact_caller(deck.draw_card)

        creature_summoning(deck.draw_card, player1)

        print("\nPolymorphism in action: Same interface, different"
              " card behaviors!")
    except Exception as e:
        print(f"Error: {e}")
