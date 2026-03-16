# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    Magical.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/24 14:54:47 by ayman             #+#    #+#             #
#    Updated: 2026/01/24 14:54:48 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod


class Magical(ABC):
    """Abstract interface for cards with magical capabilities."""
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Casts a specific spell on targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Increases available mana for the card."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Returns current magical statistics."""
        pass
