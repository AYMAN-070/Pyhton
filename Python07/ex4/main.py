# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    main.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/26 22:37:34 by ayman             #+#    #+#             #
#    Updated: 2026/01/26 22:37:35 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard

if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===")
    print()
    platform = TournamentPlatform()
    print("Registering Tournament Cards...")
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5,
                            "dragon_001", 1200)
    wizard = TournamentCard("Ice Wizard", 4, "Epic", 5, 4, "wizard_001", 1150)
    platform.register_card(dragon)
    print(f"{dragon.name} (ID: {dragon.card_id}):")
    print("- Interfaces: ['Card', 'Combatable', 'Rankable']")
    print(f"- Rating: {dragon.calculate_rating()}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")
    print()
    platform.register_card(wizard)
    print(f"{wizard.name} (ID: {wizard.card_id}):")
    print("- Interfaces: ['Card', 'Combatable', 'Rankable']")
    print(f"- Rating: {wizard.calculate_rating()}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")
    print()
    print("Creating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}")
    print()
    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, card in enumerate(leaderboard, 1):
        print(f"{i}. {card.name} - Rating: {card.calculate_rating()} "
              "({card.wins}-{card.losses})")
    print()
    print("Platform Report:")
    print(platform.generate_tournament_report())
    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
