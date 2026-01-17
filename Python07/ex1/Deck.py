# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    Deck.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/16 14:31:53 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/16 14:31:54 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck:

    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        return True

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if len(self.cards) == 0:
            return None
        card_return = self.cards[0]
        del self.cards[0]
        return card_return

    def get_deck_stats(self) -> dict:
        creatures_count = 0
        sorts_count = 0
        artefacts_count = 0
        total_cost = 0
        for x in self.cards:
            total_cost += x.cost
            if isinstance(x, CreatureCard):
                creatures_count += 1
            if isinstance(x, SpellCard):
                sorts_count += 1
            if isinstance(x, ArtifactCard):
                artefacts_count += 1
        if len(self.cards) > 0:
            average = total_cost / len(self.cards)
        return {'total_cards': len(self.cards), 'creatures': creatures_count,
                'spells': sorts_count, 'artifacts': artefacts_count,
                'average': average}
