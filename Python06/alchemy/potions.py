# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    potions.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/13 17:06:09 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/13 17:06:10 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from .elements import create_fire, create_water, create_air, create_earth


def healing_potion():
    return (f"Healing potion brewed with {create_fire()} and {create_water()}")


def strength_potion():
    return (f"Strength potion brewed with {create_earth()} and "
            f"{create_fire()}")


def invisibility_potion():
    return (f"Invisibility potion brewed with {create_air()} and "
            f"{create_water()}")


def wisdom_potion():
    return (f"Wisdom potion brewed with all elements: {create_water()}, "
            f"{create_fire()}, {create_earth()}, {create_air()}")
