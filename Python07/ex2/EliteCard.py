# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    EliteCard.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/24 14:55:28 by ayman             #+#    #+#             #
#    Updated: 2026/01/24 14:55:29 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class Elitecard(Card, Combatable, Magical):

    def __init__(self, name, cost, rarity, attack_value, health):
        super().__init__(name, cost, rarity)
        self.attack_value = attack_value
        self.health = health
        self.mana = 4

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name, "type": "Elite Hybrid",
                "effect": "Uses multiple interfaces"}

    def attack(self, target) -> dict:
        return {"attacker": self.mana, "target": target,
                "damage": self.attack_value, "combat_type": "melee"}

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        return {"defender": self.name, "damage_taken": incoming_damage,
                "still_alive": self.health > 0}

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_value, "health": self.health}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {"caster": self.name, "spell": spell_name,
                "targets": targets, "mana_used": self.mana}

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> dict:
        return {"mana": self.mana}
