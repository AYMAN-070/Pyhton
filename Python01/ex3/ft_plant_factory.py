# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_factory.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/22 18:51:48 by ayman             #+#    #+#             #
#    Updated: 2025/12/22 19:15:02 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    """Blueprint for a plant in the factory."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant attributes."""
        self.name = name
        self.height = height
        self.age = age

    def info(self) -> str:
        """Return the formatted string of the plant creation."""
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


def plant_factory() -> None:
    """Instantiate and display multiple plants."""
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    for plant in plants:
        print(plant.info())
    print()
    print("Total plants created:", len(plants))


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant_factory()
