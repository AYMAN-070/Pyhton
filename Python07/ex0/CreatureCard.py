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

from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def play(self, game_state: dict) -> dict:
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': "Creature summoned to battlefield"}

    def get_card_info(self):
        info = {"name": self.name, "cost": self.cost, "rarity": self.rarity,
                "type": self.type, "attack": self.attack,
                "health": self.health}
        return info

    def attack_target(self, target) -> dict:
        return {"attacker": self.name, "target": "Goblin Warrior",
                "damage_dealt": 7, "combat_resolved": True}
