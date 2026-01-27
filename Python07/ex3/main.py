# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    main.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/25 23:05:38 by ayman             #+#    #+#             #
#    Updated: 2026/01/27 14:15:59 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def get_methods(cls):
    return [method for method in dir(cls) if not method.startswith('_')]


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===")
    print()
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    print("Factory: ", factory.__class__.__name__)
    print("Strategy: ", strategy.__class__.__name__)
    print("Available types: ", )
    print("Available types: ", factory.get_supported_types())
    print()
    print("Simulating aggressive turn...")
    hand = [factory.create_creature("dragon"),
            factory.create_creature("goblin"),
            factory.create_spell("lightning")]
    dispaly = [f"{card.name} ({card.cost})" for card in hand]
    print("Hand: ", dispaly)
    print()
    print("Turn execution:")
    print("Strategy: ", strategy.get_strategy_name())
    result = strategy.execute_turn(hand, [])
    print("Actions: ", result)
    print("Game Report:")
    report = {'turn_simulated': 1, 'strategy_used':
              strategy.get_strategy_name(),
              'total_damage': result['damage'],
              'cards_created': len(hand)}
    print(report)
    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
