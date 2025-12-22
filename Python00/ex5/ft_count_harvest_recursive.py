# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/21 19:25:12 by ayman             #+#    #+#              #
#    Updated: 2025/12/21 19:30:58 by ayman            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    def loop(x):
        if x > days:
            print("Harvest time!")
        else:
            print("Day", x)
            loop(x + 1)
    loop(1)