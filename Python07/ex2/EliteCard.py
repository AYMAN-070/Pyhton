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
    """powerful card type combining physical combat and magical prowess"""
    def __init__(self, name, cost, rarity, attack_value, health) -> None:
        super().__init__(name, cost, rarity)
        self.attack_value = attack_value
        self.health = health
        self.mana = 4

    def play(self, game_state: dict) -> dict:
        """Implements the play method for elite cards."""
        return {"card_played": self.name, "type": "Elite Hybrid",
                "effect": "Uses multiple interfaces"}

    def attack(self, target) -> dict:
        """Executes a melee attack."""
        return {"attacker": self.name, "target": target,
                "damage": self.attack_value, "combat_type": "melee"}

    def defend(self, incoming_damage: int) -> dict:
        """Calculates defense and remaining health."""
        self.health -= incoming_damage
        return {"defender": self.name, "damage_taken": incoming_damage,
                "still_alive": self.health > 0}

    def get_combat_stats(self) -> dict:
        """Returns combat-related stats."""
        return {"attack": self.attack_value, "health": self.health}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Casts a spell using the elite card's mana."""
        return {"caster": self.name, "spell": spell_name,
                "targets": targets, "mana_used": self.mana}

    def channel_mana(self, amount: int) -> dict:
        """Channels extra mana into the card's pool."""
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> dict:
        """Returns magic-related stats."""
        return {"mana": self.mana}
