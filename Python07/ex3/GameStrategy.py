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


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        return "AgressiveStrategy"

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        pass
