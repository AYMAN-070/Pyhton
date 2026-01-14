# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    advanced.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/14 12:25:49 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/14 12:25:50 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone():
    return (f"Philosopher’s stone created using {lead_to_gold()} and "
            f"{healing_potion()}")


def elixir_of_life():
    return ("Elixir of life: eternal youth achieved!")
