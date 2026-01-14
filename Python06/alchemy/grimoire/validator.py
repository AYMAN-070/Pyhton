# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    validator.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/14 14:11:55 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/14 14:11:56 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def validate_ingredients(ingredients: str) -> str:
    if ("fire" in ingredients or "water" in ingredients or
            "earth" in ingredients or "air" in ingredients):
        return (f"{ingredients} - VALID")
    else:
        return (f"{ingredients} - INVALID")
