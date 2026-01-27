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

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")
    creature_card = CreatureCard("Fire_dragon", 5, "Legendary", 7, 5)
    artifact = ArtifactCard("Mana Crystal", 4, "Rare", 3,
                            "Prmanent: +1 mana per turn")
    spell = SpellCard("Lightning Bolt", 3, "Legendaray",
                      "Deal 3 damage to target")
    deck = Deck()
    deck.add_card(creature_card)
    deck.add_card(spell)
    deck.add_card(artifact)
    print(deck.get_deck_stats())
    print()
    print("Drawing and playing cards:")
    print()
    deck.shuffle()
    for x in range(3):
        card_type = ""
        card = deck.draw_card()
        if isinstance(card, CreatureCard):
            card_type = "Creature"
        if isinstance(card, SpellCard):
            card_type = "Spell"
        if isinstance(card, ArtifactCard):
            card_type = "Artifact"
        print(f"Drew: {card.name} ({card_type})")
        print(card.play({}))
        print()
    print("Polymorphism in action: Same interface, different card behaviors!")
