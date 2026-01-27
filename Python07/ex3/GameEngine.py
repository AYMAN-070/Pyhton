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


class GameEngine:

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        pass

    def simulate_turn(self) -> dict:
        pass

    def get_engine_status(self) -> dict:
        pass
