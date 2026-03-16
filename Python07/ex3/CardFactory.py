# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    CardFactory.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/25 22:49:46 by ayman             #+#    #+#             #
#    Updated: 2026/01/25 22:49:47 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract Factory interface for creating themed game cards"""

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Creates a creature card"""
        pass  # type: ignore

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Creates a spell card"""
        pass  # type: ignore

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Creates an artifact card"""
        pass  # type: ignore

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Generates a summary of a themed deck"""
        return {"theme": "Fantasy", "size": size}

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass  # type: ignore
