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
    @abstractmethod
    def attack(self, target) -> dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
