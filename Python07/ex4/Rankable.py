# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#     Rankable.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/27 13:35:09 by ayman             #+#    #+#             #
#    Updated: 2026/01/27 13:35:10 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod


class Rankable(ABC):
    """Abstract interface for entities that can be ranked within a tournament
    system"""
    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculates and returns the current rating score"""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Updates the win count and adjusts the rating accordingly"""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Updates the loss count and adjusts the rating accordingly"""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Returns a summary of ranking statistics"""
        pass
