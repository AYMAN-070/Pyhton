# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_pathway_debate.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/14 12:22:56 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/14 12:22:57 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===")
    print()
    print("Testing Absolute Imports (from basic.py):")
    import alchemy.Transmutation.basic
    print("lead_to_gold(): ", alchemy.Transmutation.basic.lead_to_gold())
    print("stone_to_gem(): ", alchemy.Transmutation.basic.stone_to_gem())
    print()
    print("Testing Relative Imports (from advanced.py):")
    from alchemy.Transmutation import advanced
    print("philosophers_stone(): ", advanced.philosophers_stone())
    print("elixir_of_life(): ", advanced.elixir_of_life())
    print()
    import alchemy.Transmutation
    print("Testing Package Access:")
    print("alchemy.transmutation.lead_to_gold(): ", alchemy.Transmutation.
          lead_to_gold())
    print("alchemy.transmutation.philosophers_stone():", alchemy.Transmutation.
          philosophers_stone())
    print()
    print("Both pathways work! Absolute: clear, Relative: concise")
