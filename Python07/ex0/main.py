# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    main.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/14 16:00:17 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/14 16:00:18 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()
    print("CreatureCard Info:")
    creature_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    card_info = creature_card.get_card_info()
    print(card_info)
    print()
    available_mana = 6
    print(f"Playing Fire Dragon with {available_mana} mana available:")
    print("Playable:", creature_card.is_playable(6))
    print("Play result: ", creature_card.play({}))
    print()
    print("Fire Dragon attacks Goblin Warrior:")
    print("Attack result:", creature_card.attack_target("Goblin Warrior"))
    print()
    print("Testing insufficient mana (3 available):")
    print("Playable: ", creature_card.is_playable(3))
    print()
    print("Abstract pattern successfully demonstrated!")
