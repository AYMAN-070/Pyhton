# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_achievement_tracker.py                          :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/29 13:14:45 by ayman             #+#    #+#             #
#    Updated: 2026/01/06 15:39:11 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def track_achievements() -> None:
    """
    Tracks and analyzes player achievements using set operations.

    Demonstrates:
    - Union: All possible achievements
    - Intersection: Achievements shared by everyone
    - Difference: Unique or rare achievements per player
    """
    alice_achievements = {"first_kill", "level_10", "treasure_hunter",
                          "speed_demon"}
    bob_achievements = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie_achievements = {"level_10", "treasure_hunter", "boss_slayer",
                            "speed_demon", "perfectionist"}

    print("=== Achievement Tracker System ===")
    print()
    print("Player alice achievements: ", alice_achievements)
    print("Player bob achievements: ", bob_achievements)
    print("Player charlie achievements: ", charlie_achievements)
    print()

    print("=== Achievement Analytics ===")
    all_unique_achievements = set.union(alice_achievements, bob_achievements,
                                        charlie_achievements)
    print("All unique achievements: ", all_unique_achievements)
    print("Total unique achievements: ", len(all_unique_achievements))
    print()

    common_achievements = set.intersection(alice_achievements,
                                           bob_achievements,
                                           charlie_achievements)
    print("Common to all players: ", common_achievements)
    alice_rare = (alice_achievements -
                  (bob_achievements.union(charlie_achievements)))
    bob_rare = (bob_achievements -
                (alice_achievements.union(charlie_achievements)))
    charlie_rare = (charlie_achievements -
                    (bob_achievements.union(alice_achievements)))
    rare_achievements = set.union(alice_rare, bob_rare, charlie_rare)
    print("Rare achievements (1 player): ", rare_achievements)
    print()

    print("Alice vs Bob common: ",
          alice_achievements.intersection(bob_achievements))
    print("Alice unique:", alice_achievements.difference(bob_achievements))
    print("Bob unique:", bob_achievements.difference(alice_achievements))


if __name__ == "__main__":
    track_achievements()
