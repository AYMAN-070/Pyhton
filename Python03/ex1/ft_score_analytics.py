# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_score_analytics.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/28 13:04:39 by ayman             #+#    #+#             #
#    Updated: 2026/01/06 15:36:56 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys
if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    """Analyzes player scores from command line arguments."""
    score_list = []
    i = 1
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:

        while i < len(sys.argv):
            try:
                score = int(sys.argv[i])
                score_list.append(score)
                i += 1
            except ValueError as e:
                print("Error :", e)
                i += 1
        if len(score_list) > 0:
            print("Score processed: ", score_list)
            print("Total players: ", len(score_list))
            total = sum(score_list)
            print("Total score: ", total)
            print("Average score: ", (total / len(score_list)))
            max_num = max(score_list)
            print("High score: ", max_num)
            min_num = min(score_list)
            print("Low score: ", min_num)
            print("Score range: ", (max_num - min_num))
        else:
            print("Aucun score valide trouvé.")
