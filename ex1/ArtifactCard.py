from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.type = "Artifact"
        self.effect = effect

    def activate_ability(self) -> dict:
        info = super().get_card_info()
        info['effect'] = self.effect
        return info

    def play(self, game_state: dict) -> dict:
        try:
            mana = game_state["player_mana"]
        except Exception:
            raise ValueError("Please Check the Game_status dict"
                             "provided is invalide")
        if not super().is_playable(mana):
            return {'Playable': False}
        return {'Playable': True, 'Play result': self.activate_ability()}
