from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===\n")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    print("Configuring Elden Ring Card Game...")
    engine.configure_engine(factory, strategy)
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    supported = factory.get_supported_types()
    print("\nAvailable types:")
    print(f"  Creatures: {supported['creatures']}\n")
    print(f"  Spells: {supported['spells']}\n")
    print(f"  Artifacts: {supported['artifacts']}\n")

    print("\nSimulating aggressive turn...")
    turn = engine.simulate_turn()

    print("\nOpening Hand:")
    for card in turn['hand']:
        print(f"  - {card}")

    print("\nTurn execution:")
    for key, val in turn['turn_execution'].items():
        print(f"  {key}: {val}")

    print("\nGame Report:")
    report = engine.get_engine_status()
    for key, val in report.items():
        print(f"  {key}: {val}")

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
