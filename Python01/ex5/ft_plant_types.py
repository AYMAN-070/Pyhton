# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_types.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/23 12:59:18 by ayhammou          #+#    #+#             #
#    Updated: 2025/12/23 14:30:29 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    """Base class for all plants in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize common plant attributes."""
        self.name = name
        self.height = height
        self.age = age

    def info(self) -> str:
        """Return basic plant info."""
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    """Specialized plant type for flowers."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize flower with color."""
        super().__init__(name, height, age)
        self.color = color

    def info(self) -> str:
        """Return detailed flower info."""
        return (f"{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color")

    def bloom(self) -> str:
        """Display blooming message."""
        return (f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Specialized plant type for trees."""
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialize tree with trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def info(self) -> str:
        """Return detailed tree info."""
        return (f"{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        """Calculate and display shade area."""
        shade_area = self.trunk_diameter + 28
        return (f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    """Specialized plant type for vegetables."""
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """Initialize vegetable with season and nutrients."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def info(self) -> str:
        """Return detailed vegetable info."""
        return (f"{self.name} (Vegetable): {self.height}cm, "
                f"{self.age} days, {self.harvest_season} harvest\n"
                f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden PLant Types ===")
    print()
    flower = Flower("Rose", 25, 30, "red")
    tree = Tree("Oak", 500, 1825, 50)
    vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(flower.info())
    print(flower.bloom())
    print()
    print(tree.info())
    print(tree.produce_shade())
    print()
    print(vegetable.info())
