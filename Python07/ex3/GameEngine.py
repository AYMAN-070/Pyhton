# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    GameEngine.py                                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/25 22:52:44 by ayman             #+#    #+#             #
#    Updated: 2026/01/25 22:52:45 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Optional


class GameEngine:
    """Orchestrates game interactions by combining a card factory and a
    strategy"""

    def __init__(self) -> None:
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Connects a factory and a strategy to the engine"""
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        """Executes a turn simulation based on current settings"""
        return {}

    def get_engine_status(self) -> dict:
        """Returns the configuration status of the engine"""
        return {"status": "initialized"}
