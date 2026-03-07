import random
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


CREATURES = {
    'malenia':  ('Malenia Blade of Miquella', 9,
                 'Legendary', 10, 8),
    'radahn': ('Starscourge Radahn', 8, 'Legendary', 9, 10),
    'morgott': ('Morgott the Omen King', 7, 'Legendary', 7, 9),
    'godrick': ('Godrick the Grafted', 6, 'Legendary', 7, 7),
    'rykard': ('Rykard Lord of Blasphemy', 7, 'Legendary', 8, 6),
    'maliketh': ('Maliketh the Black Blade', 8, 'Legendary', 9, 7),
    'crucible_knight': ('Crucible Knight', 4, 'Rare', 5, 6),
    'tree_sentinel': ('Tree Sentinel', 3, 'Rare', 4, 6),
    'night_cavalry': ('Night Cavalry', 3, 'Rare', 5, 4),
    'erdtree_avatar': ('Erdtree Avatar', 4, 'Rare', 4, 7),
    'Fire_giant': ('Fire Giant', 2, 'Common', 2, 4)
}

SPELLS = {
    'stars_of_ruin': ('Stars of Ruin', 6, 'Legendary', 'damage'),
    'ranni_dark_moon': ("Ranni's Dark Moon", 7, 'Legendary', 'debuff'),
    'elden_stars': ('Elden Stars', 8, 'Legendary', 'damage'),
    'rot_breath': ('Dragonmaw Rot Breath', 5, 'Rare', 'debuff'),
    'gravitas': ('Gravitas', 3, 'Rare', 'debuff'),
    'rock_sling': ('Rock Sling', 3, 'Rare', 'damage'),
    'glintstone_pebble': ('Glintstone Pebble', 1, 'Common', 'damage'),
    'heal': ('Erdtree Heal', 4, 'Common', 'heal'),
    'flame_sling': ('Flame Sling', 2, 'Common', 'damage'),
    'carian_slicer': ('Carian Slicer', 2, 'Common', 'damage')
}

ARTIFACTS = {
    'erdtree_favor': ('Talisman of the Erdtree\'s Favor', 4,
                      'Legendary', 8,
                      '+5 HP, +3 stamina, +1 equip load per turn'),
    'marika_soreseal': ('Radagon\'s Soreseal', 4, 'Legendary', 7,
                        '+5 to all attributes, '
                        '-15% damage negation'),
    'two_fingers_heirloom': ('Two Fingers Heirloom', 3,
                             'Legendary', 6,
                             '+5 Faith, boost all incantations'),
    'stargazer_heirloom': ('Stargazer Heirloom', 3, 'Rare', 5,
                           '+5 Intelligence, boost all sorceries'),
    'arrow_sting': ('Arrow\'s Sting Talisman', 2, 'Rare', 5,
                    '+10% ranged damage'),
    'carian_filigreed': ('Carian Filigreed Crest', 2, 'Rare', 4,
                         'Reduce skill FP cost by 25%'),
    'starlight_shards': ('Starlight Shards', 1, 'Common', 3,
                         '+1 mana per turn'),
    'talisman_of_refuge': ('Talisman of Refuge', 1, 'Common', 3,
                           'Reduce incoming damage by 1')
}


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        key = name_or_power if name_or_power in CREATURES else (
            random.choice(list(CREATURES.keys()))
        )
        name, cost, rarity, attack, health = CREATURES[key]
        return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        key = name_or_power if name_or_power in SPELLS else (
            random.choice(list(SPELLS.keys()))
        )
        name, cost, rarity, effect = SPELLS[key]
        return SpellCard(name, cost, rarity, effect)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        key = name_or_power if name_or_power in ARTIFACTS else (
            random.choice(list(ARTIFACTS.keys()))
        )
        name, cost, rarity, durability, effect = ARTIFACTS[key]
        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> dict:
        deck = Deck()
        for i in range(size):
            roll = i % 3
            if roll == 0:
                deck.add_card(self.create_creature())
            elif roll == 1:
                deck.add_card(self.create_spell())
            else:
                deck.add_card(self.create_artifact())
        return {
            'theme': 'Elden Ring',
            'size': size,
            'cards': deck,
        }

    def get_supported_types(self) -> dict:
        return {
            'creatures': list(CREATURES.keys()),
            'spells': list(SPELLS.keys()),
            'artifacts': list(ARTIFACTS.keys()),
        }
