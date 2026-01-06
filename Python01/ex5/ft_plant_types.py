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
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def info(self):
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def info(self):
        return (f"{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color")

    def bloom(self):
        return (f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def info(self):
        return (f"{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        shade_area = self.trunk_diameter + 28
        return (f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season}")
        return (f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden PLant Types ===")
    flower = Flower("Rose", 25, 30, "red")
    tree = Tree("Oak", 500, 1825, 50)
    vegetable = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
    print(flower.info())
    print(flower.bloom())
    print(tree.info())
    print(tree.produce_shade())
    print(vegetable.info())
