# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    basic.py                                           :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/14 12:24:02 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/14 12:24:03 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    return (f"Lead transmuted to gold using {create_fire()}")


def stone_to_gem() -> str:
    return (f"Stone transmuted to gem using {create_earth()}")
