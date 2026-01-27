# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    TournamentPlatform.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/27 13:37:25 by ayman             #+#    #+#             #
#    Updated: 2026/01/27 13:37:26 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return f"Card {card.name} registered successfully."

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        fighter1 = self.cards.get(card1_id)
        fighter2 = self.cards.get(card2_id)

        if not fighter1 or not fighter2:
            return {"error": "One or both cards not found"}

        self.matches_played += 1

        if fighter1.attack_value > fighter2.attack_value:
            winner = fighter1
            loser = fighter2
        else:
            winner = fighter2
            loser = fighter1

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        all_cards = list(self.cards.values())

        sorted_cards = sorted(all_cards, key=lambda x: x.rating, reverse=True)

        return sorted_cards

    def generate_tournament_report(self) -> dict:
        ratings = [c.rating for c in self.cards.values()]
        avg_rating = sum(ratings) / len(ratings) if ratings else 0

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": int(avg_rating),
            "platform_status": "active"
        }
