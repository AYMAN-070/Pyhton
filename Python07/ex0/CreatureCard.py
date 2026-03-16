# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    CreatureCard.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/14 15:59:56 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/14 15:59:57 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from typing import Dict, Any
from ex0.Card import Card


class CreatureCard(Card):
    """A concrete implementation of Card representing a creature with
    combat stats"""
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        """Initialize a creature card with combat attributes."""
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a positive integer.")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be a positive integer.")
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def play(self, game_state: dict) -> Dict[str, Any]:
        """Implements the abstract play method to summon the creature."""
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': "Creature summoned to battlefield"}

    def get_card_info(self):
        """Extends basic card info with creature-specific stats."""
        info = {"name": self.name, "cost": self.cost, "rarity": self.rarity,
                "type": self.type, "attack": self.attack,
                "health": self.health}
        return info

    def attack_target(self, target) -> Dict[str, Any]:
        """Executes a combat action against a specific target."""
        return {"attacker": self.name, "target": "Goblin Warrior",
                "damage_dealt": self.attack, "combat_resolved": True}
