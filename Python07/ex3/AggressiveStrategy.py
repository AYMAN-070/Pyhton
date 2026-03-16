# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    AggressiveStrategy.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/25 22:54:45 by ayman             #+#    #+#             #
#    Updated: 2026/01/25 22:54:46 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex3.GameEngine import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


class AggressiveStrategy(GameStrategy):
    """A strategy that prioritizes low-cost cards and maximum damage output"""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Plays as many cards as possible starting from the lowest cost"""
        mana = 5
        cards_played = []
        damage = 0
        mana_used = 0
        sorted_hand = sorted(hand, key=lambda card: card.cost)
        for card in sorted_hand:
            if card.cost <= (mana - mana_used):
                cards_played.append(card.name)
                mana_used += card.cost
                if isinstance(card, CreatureCard):
                    damage += card.attack
                elif isinstance(card, SpellCard):
                    damage += 5
        return {"cards_played": cards_played, "mana_used": mana_used,
                "target_attacked": self.prioritize_targets([]),
                "damage": damage}

    def get_strategy_name(self) -> str:
        return "AgressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """Always targets the enemy player directly for maximum aggression"""
        return ["Enemy Player"]
