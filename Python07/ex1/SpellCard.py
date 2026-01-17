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


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        return {}

    def resolve_effect(self, target: list) -> dict:
        return{}

