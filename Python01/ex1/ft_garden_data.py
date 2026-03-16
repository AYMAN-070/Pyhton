# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_data.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/22 12:45:14 by ayman             #+#    #+#             #
#    Updated: 2026/01/06 13:17:49 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    """Blueprint for a garden plant."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant attributes with type safety."""
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("=== Garden PLant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")
    print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
    print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")
