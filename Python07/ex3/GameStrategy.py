# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    GameStrategy.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/25 22:48:04 by ayman             #+#    #+#             #
#    Updated: 2026/01/25 22:48:05 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod
from ex0.Card import Card


class GameStrategy(ABC):
    """Abstract interface defining how a Gamestrategy should execute a turn"""

    @abstractmethod
    def execute_turn(self, hand: list[Card], battlefield: list[Card]) -> dict:
        """Analyzes the hand and battlefield to perform actions"""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Returns the identifier name of the strategy"""
        return "AgressiveStrategy"

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Determines which targets to attack first"""
        pass
