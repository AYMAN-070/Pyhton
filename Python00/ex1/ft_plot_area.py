# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/21 11:20:14 by ayman             #+#    #+#              #
#    Updated: 2025/12/21 16:54:36 by ayman            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
        longueur = int(input("Enter length: "))
        largeur = int(input("Enter width: "))
        area = longueur * largeur
        print("Plot area:", area)