# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    Card.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/14 15:59:26 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/14 15:59:27 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod


class Card(ABC):
    """
    Abstract Base Class representing the universal blueprint for all cards"""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Abstract method to define the card's effect when played."""
        pass

    def get_card_info(self) -> dict:
        """Returns a dictionary containing the card's basic information."""
        return {"name": self.name, "cost": self.cost, "rarity": self.rarity}

    def is_playable(self, available_mana: int) -> bool:
        """Checks if the card can be played based on the available mana."""
        if available_mana >= self.cost:
            return True
        else:
            return False
