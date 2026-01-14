# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_circular_curse.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/14 14:10:26 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/14 14:10:27 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

if __name__ == "__main__":
    print("=== Circular Curse Breaking ===")
    print()
    print("Testing ingredient validation:")
    from alchemy.grimoire import validate_ingredients
    print("validate_ingredients(\"fire air\"): ",
          validate_ingredients("fire air"))
    print("validate_ingredients(\"dragon scales\"): ",
          validate_ingredients("dragon scales"))
    print()
    print("Testing spell recording with validation:")
    from alchemy.grimoire import record_spell
    print("record_spell(\"Fireball\", \"fire air\"): ",
          record_spell("Fireball", "fire air"))
    print("record_spell(\"Dark Magic\", \"shadow\"): ",
          record_spell("Dark Magic", "shadow"))
    print()
    print("Testing late import technique:")
    from alchemy.grimoire import spellbook
    print("record_spell(\"Lightning\", \"air\"): ",
          spellbook.record_spell("Lightning", "air"))
    print()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
