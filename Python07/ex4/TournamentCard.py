# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#     TournamentCard.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/27 13:35:58 by ayman             #+#    #+#             #
#    Updated: 2026/01/27 13:35:59 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """A comprehensive card implementation that combines basic card
    attributes"""
    def __init__(self, name, cost, rarity, attack_value, health, card_id,
                 initial_rating=1000) -> None:
        super().__init__(name, cost, rarity)

        self.attack_value = attack_value
        self.health = health

        self.card_id = card_id
        self.rating = initial_rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        """Implements the mandatory play behavior"""
        return {"action": "play", "card": self.name}

    def attack(self, target) -> dict:
        """Executes a combat attack"""
        return {"attacker": self.name, "damage": self.attack_value}

    def defend(self, incoming_damage: int) -> dict:
        """Processes incoming damage during a match"""
        self.health -= incoming_damage
        return {"defender": self.name, "health_left": self.health}

    def get_combat_stats(self) -> dict:
        """Returns current attack and health stats"""
        return {"attack": self.attack_value, "health": self.health}

    def calculate_rating(self) -> int:
        """Calculates the current ranking score"""
        return self.rating

    def update_wins(self, count: int) -> None:
        """Updates the win record and increases the rating"""
        self.wins += count
        self.rating += (16 * count)

    def update_losses(self, count: int) -> None:
        """Updates the loss record and decreases the rating"""
        self.losses += count
        self.rating -= (16 * count)

    def get_rank_info(self) -> dict:
        return {
            "id": self.card_id,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> dict:
        """Returns a summary of the card's ranking status"""
        return self.get_rank_info()
