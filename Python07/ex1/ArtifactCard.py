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
    """Represents permanent game modifiers that stay on the battlefield."""
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability < 0:
            raise ValueError("Durability must be positive")
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict):
        """Implements the play method for artifacts."""
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': self.effect}

    def activate_ability(self) -> dict:
        """Activates the artifact's specific ability"""
        return {'activation': self.effect, 'durability': self.durability}
