# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_growth.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/22 15:37:28 by ayman             #+#    #+#             #
#    Updated: 2026/01/06 13:18:39 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    """Blueprint for a plant that can grow and age."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant attributes."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm):
        """Increase the height of the plant."""
        self.height = self.height + cm

    def get_older(self, days):
        """Increase the age of the plant."""
        self.age = self.age + days

    def get_info(self):
        """Return the current status of the plant."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    print("=== Day 1 ===")
    p1 = Plant("Rose", 25, 30)
    print(p1.get_info())
    p1.grow(6)
    p1.get_older(6)
    print("=== Day 7 ===")
    print(p1.get_info())
    print("Growth this week: +6cm")
