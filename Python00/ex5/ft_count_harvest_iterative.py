# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#     ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/21 19:14:40 by ayman             #+#    #+#              #
#    Updated: 2025/12/21 19:24:24 by ayman            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print("Day", i)
    print("Harvest time!")