# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    main.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/16 14:32:28 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/16 14:32:29 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #
from ex0 import CreatureCard
from ex1 import SpellCard
from ex1 import ArtifactCard
from ex1 import Deck

if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")
    creature_card = CreatureCard("Fire_dragon", 5, "Legendary", 7, 5)
    artifact = ArtifactCard("Mana Crystal", 2, "Legendary", 7,
                            "Prmanent: +1 mana per turn")
    spell = SpellCard("LIghtning Bolt", 3, "Legendaray",
                      "Deal 3 damage to target")
    deck = Deck
    deck.add_card(creature_card)
    deck.add_card(spell)
    deck.add_card(artifact)
