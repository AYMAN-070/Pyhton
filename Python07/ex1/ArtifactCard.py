# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ArtifactCard.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/16 14:31:34 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/16 14:31:35 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict):
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': self.effect}

    def activate_ability(self) -> dict:
        return {'activation': self.effect, 'durability': self.durability}
