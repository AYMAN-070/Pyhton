# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/21 19:31:28 by ayman             #+#    #+#              #
#    Updated: 2025/12/21 19:35:29 by ayman            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
    name = input("Enter garden name: ")
    number = int(input("Enter number of plants: "))
    print("Garden:", name)
    print("Plants:", number)
    print("Status: Growing well!")