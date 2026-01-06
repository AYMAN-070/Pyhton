# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_harvest_total.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/21 18:59:52 by ayman             #+#    #+#             #
#    Updated: 2026/01/06 12:57:42 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total():
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    total = day1 + day2 + day3
    print("Total harvest:", total)
