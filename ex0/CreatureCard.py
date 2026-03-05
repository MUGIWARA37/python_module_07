from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.type = "Creature"
        if self.attack < 0:
            self.attack = 0
            print("attack power can't be NEGATIVE !! setting the default "
                  f"value {self.attack}\n")
        self.health = health
        if self.health < 1:
            self.health = 1
            print("Health can't be LESS THEN 1 !!setting the default "
                  f"value {self.health}\n")

    def play(self, game_state: dict) -> dict:
        try:
            mana = game_state["player_mana"]
        except Exception:
            raise ValueError("Please Check the Game_status dict"
                             "provided invalide")
        if not super().is_playable(mana):
            return {"Playable": False}
        return {
                "Playable": True,
                "Play result": {
                    "card_played": self.name,
                    "mana_used": self.cost,
                    "effect": f"{self.name} summoned to battlefield"
                }
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["Card tpye"] = "Creature"
        info["Card attack Power"] = self.attack
        info["Card health"] = self.health
        return info

    def attack_target(self, target: "CreatureCard") -> None:
        death_seant = False
        if target.health <= self.attack:
            print(f"{target.name} IS NO MORE !!")
            target.health = 0
            death_seant = True
        else:
            target.health -= self.attack
            print(
                f"Hard Strike from {self.name}: "
                f"-{self.attack} HP to {target.name}"
            )
        return {'attacker': self.name, 'target': target.name,
                'damage dealt': self.attack, 'combat_resolved': death_seant}
