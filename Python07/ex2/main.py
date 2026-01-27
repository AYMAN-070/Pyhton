# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    main.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/24 22:20:17 by ayman             #+#    #+#             #
#    Updated: 2026/01/24 22:20:18 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex2.EliteCard import Elitecard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


def get_methods(cls):
    return [method for method in dir(cls) if not method.startswith('_')]


if __name__ == "__main__":
    print("=== DataDeck Ability System ===")
    print()
    print("EliteCard capabilities:")
    print(f"Card: {get_methods(Card)}")
    print(f"Combatable: {get_methods(Combatable)}")
    print(f"Magical: {get_methods(Magical)}")
    print()
    test = Elitecard("Arcane warrior", 7, "Legendary", 5, 10)
    print(f"Playing {test.name} (Elite Card):")
    print()
    print("Combat phase: ")
    print("Attack result:", test.attack("Enemy"))
    print("Defense result:", test.defend(5))
    print()
    print("Magic phase:")
    print("Spell cast:", test.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print("Mana channel:", test.channel_mana(3))
    print()
    print("Multiple interface implementation successful!")
