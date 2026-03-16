# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    Combatable.py                                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/24 14:54:24 by ayman             #+#    #+#             #
#    Updated: 2026/01/24 14:54:23 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod


class Combatable(ABC):
    """Abstract interface for cards with combat capabilities."""
    @abstractmethod
    def attack(self, target) -> dict:
        """Executes an attack on a target."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Processes incoming damage."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Returns current combat statistics."""
        pass
