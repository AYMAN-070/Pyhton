# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#     FantasyCardFactory.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/25 23:06:59 by ayman             #+#    #+#             #
#    Updated: 2026/01/25 23:07:00 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Returns the list of fantasy cards this factory can produce["""
    def get_supported_types(self) -> dict:
        return {"creatures": ["dragon", "goblin"],
                "spells": ["fireball"],
                "artifacts": ["mana_ring"]}

    def create_creature(self, name_or_power=None) -> Card:
        """Creates a fantasy creature based on the provided name"""
        if name_or_power == "dragon":
            return CreatureCard("Fire Dragon", 5, "Epic", 7, 5)
        elif name_or_power == "goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 3, 2)
        return None  # type: ignore

    def create_spell(self, name_or_power=None) -> SpellCard:
        """Creates a fantasy spell"""
        if name_or_power == "lightning":
            return SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage")
        elif name_or_power == "fireball":
            return SpellCard("Fireball", 4, "Rare", "Deal 5 damage AOE")
        return None  # type: ignore

    def create_artifact(self, name_or_power=None) -> ArtifactCard:
        """Creates a fantasy artifact"""
        if name_or_power == "mana_ring":
            return ArtifactCard("Mana Ring", 2, "Rare", 5, "+1 Mana")
        return None  # type: ignore

    def create_themed_deck(self, size: int):
        """Generates a summary of a themed deck creation"""
        pass
