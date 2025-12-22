# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#     ft_seed_inventory.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/21 19:40:10 by ayman             #+#    #+#              #
#    Updated: 2025/12/21 19:54:33 by ayman            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name = seed_type.capitalize()
    if unit == "packets":
        print(name, "seeds:", quantity, "packets available")
    elif unit == "grams":
        print(name, "seeds:", quantity, "grams total")
    elif unit == "area":
        print(name, "seeds: covers", quantity, "square meters")
    else:  
        print("Unknown unit type")