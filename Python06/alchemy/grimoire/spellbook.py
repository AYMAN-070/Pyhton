# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    spellbook.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/14 14:11:35 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/14 14:11:36 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def record_spell(spell_name: str, ingredients: str) -> str:
    from . import validator
    check = validator.validate_ingredients(ingredients)
    if check == f"{ingredients} - VALID":
        return (f"Spell recorded: {spell_name} ({check})")
    else:
        return (f"Spell rejected: {spell_name} ({check})")
