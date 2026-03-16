# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    SpellCard.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/16 14:31:10 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/16 14:31:11 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex0.Card import Card
from typing import Dict, Any, List


class SpellCard(Card):
    """Represents instant magical effects that are consumed upon use."""
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        if not effect_type or not isinstance(effect_type, str):
            raise ValueError("Effect type must be none empty")
        self.effect_type = effect_type

    def play(self, game_state: dict) -> Dict[str, Any]:
        """Casts the spell, consuming mana and triggering its effect."""
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': self.effect_type}

    def resolve_effect(self, target: List) -> Dict[str, Any]:
        """Processes the instant magical effect on the specified targets."""
        return {}
