# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/22 15:37:28 by ayman             #+#    #+#              #
#    Updated: 2025/12/22 15:57:16 by ayman            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def grow(self, cm):
        self.height = self.height + cm
    def get_older(self, days):
        self.age = self.age + days
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"
if __name__ == "__main__":
    print("Day 1 ===")
    p1 = Plant("Rose", 25, 30)
    print(p1.get_info())
    p1.grow(6)
    p1.get_older(6)
    print("===Day 7")
    print(p1.get_info())
    print("Growth this week: +6cm")