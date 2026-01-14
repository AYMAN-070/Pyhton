# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    __init__.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/01/13 15:29:20 by ayhammou          #+#    #+#             #
#    Updated: 2026/01/13 15:29:21 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from .elements import create_fire, create_water

__version__ = "1.0.0"
__author__ = "Master Pythonicus"

__all__ = [
    "create_fire",
    "create_water"
]
