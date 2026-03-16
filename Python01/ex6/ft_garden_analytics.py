# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_analytics.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/23 14:31:15 by ayhammou          #+#    #+#             #
#    Updated: 2025/12/25 00:55:42 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    """Base class for the analytics system."""
    def __init__(self, name: str, height: int, type: str) -> None:
        self.name = name
        self.height = height
        self.type = type

    def grow(self, cm: int) -> None:
        """Increments height and logs growth."""
        self.height = self.height + cm
        print(f"{self.name}: grew {cm}cm")

    def info(self) -> str:
        """Returns basic info."""
        return (f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """Adds blooming status to a plant."""
    def __init__(self, name: str, height: int, type: str,
                 blooming: bool = True):
        super().__init__(name, height, type)
        self.blooming = blooming

    def info(self):
        status = "bloomig" if self.blooming else "not blooming"
        return f"- {self.name}: {self.height}cm, {status}"


class PrizeFlower(FloweringPlant):
    """Adds prize points to a flowering plant."""
    def __init__(self, name: str, height: int, points: int, type: str):
        super().__init__(name, height, type, blooming=True)
        self.points = points

    def info(self):
        return (f"- {self.name}: {self.height}cm, "
                f"blooming, Prize points: {self.points}")


class GardenManager:
    """Manages multiple gardens and analyzes data."""
    total_gardens = 0

    class GardenStats:
        """Nested helper for calculations."""
        @staticmethod
        def calculate_growth(days: int) -> int:
            return days * 1

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.valid_height = True
        self.plants_added = 0
        self.total_growth = 0
        self.regular = 0
        self.flowering = 0
        self.prize_flowers = 0
        GardenManager.total_gardens += 1

    def add_plants(self, plant: Plant) -> None:
        """Adds a plant to the collection."""
        self.plants.append(plant)
        self.plants_added += 1
        if plant.type == "Regular":
            self.regular += 1
        if plant.type == "Flowering":
            self.flowering += 1
        if plant.type == "Prize_Flower":
            self.prize_flowers += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all_plants(self, days: int) -> None:
        """Simulates growth for all plants."""
        growth_in_cm = self.GardenStats.calculate_growth(days)
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(growth_in_cm)
            self.total_growth += growth_in_cm

    def score(self) -> int:
        """Calculates total garden score."""
        total = 0
        for plant in self.plants:
            total += plant.height
            if plant.type == "Prize_Flower":
                total += plant.points
        return total

    def report(self) -> None:
        """Displays full analytics report"""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if plant.height < 0:
                self.valid_height = False
            print(plant.info())
        print()
        print(f"Plants_added: {self.plants_added}, "
              f"Total growth: {self.total_growth}cm")
        print(f"PLant types: {self.regular} regular, "
              f"{self.flowering} flowering, "
              f"{self.prize_flowers} prize flowers")
        print()
        print("Heigh validation test: ", self.valid_height)
        total = self.score()
        print(f"Garden scores - {self.owner} : {total}")
        print("Total gardens managed: ", GardenManager.total_gardens)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()
    manager = GardenManager("Alice")
    p1 = Plant("Oak Tree", 100, "Regular")
    p2 = FloweringPlant("Rose", 25, "Flowering")
    p3 = PrizeFlower("Sunflower", 50, 10, "Prize_Flower")
    manager.add_plants(p1)
    manager.add_plants(p2)
    manager.add_plants(p3)
    print()
    manager.grow_all_plants(1)
    print()
    manager.report()
