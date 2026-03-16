# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_management.py                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/27 15:38:35 by ayman             #+#    #+#             #
#    Updated: 2025/12/28 12:23:49 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


class GardenError(Exception):
    """Base class for all garden exceptions."""
    pass


class PlantError(GardenError):
    """Exception for plant-related issues."""
    pass


class WaterError(GardenError):
    """Exception for irrigation-related issues."""
    pass


class GardenManager:
    """A management system for agricultural data pipelines."""
    def add_plants(self, plant_list: list) -> list[str]:
        """Validates raw plant data and returns a cleaned list."""
        print("Adding plants to garden...")
        valid_plant = []
        try:
            for plant in plant_list:
                if not isinstance(plant, str) or plant == "":
                    raise ValueError("Plant name cannot be empty!\n")
                valid_plant.append(plant)
                print(f"Added {plant} successfully")
        except ValueError as e:
            print("Error adding plant: ", e)
        return valid_plant

    def water_plants(self, plant_list: list) -> None:
        """Simulates the watering process for a list of plants."""
        print("Watering plants...")
        print("Opening watering system")
        try:
            for plant in plant_list:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (Cleanup)\n")

    def checking_health(self, plant: str, water_level: int,
                        sun_hours: int) -> None:
        """Monitors plant health based on environmental thresholds."""
        try:
            if water_level < 1:
                raise ValueError(f"Error checking {plant}: Water level "
                                 f"{water_level} is too low (min 1)")
            if water_level > 10:
                raise ValueError(f"Error checking {plant}: Water level "
                                 f"{water_level} is too high (max 10)")
            if sun_hours < 2:
                raise ValueError(f"Error checking {plant}: Sunlight hours "
                                 f"{sun_hours} is too low (min 2)")
            if sun_hours > 12:
                raise ValueError(f"Error checking {plant}: Sunlight hours "
                                 f"{sun_hours} is too high (max 12)")
            print(f"{plant}: healthy (water: {water_level}, "
                  f"sun: {sun_hours})")
        except ValueError as e:
            print(f"{e}")


def test_garden_management() -> None:
    """Demonstration function"""
    print("=== Garden Management System ===")
    print()
    manager = GardenManager()
    plant_list = ["tomato", "lettuce", ""]
    valid_list = manager.add_plants(plant_list)
    manager.water_plants(valid_list)
    print("Checking plant health...")
    manager.checking_health("tomato", 5, 8)
    manager.checking_health("lettuce", 15, 8)
    print()
    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print("Caught GardenError: ", e)
    finally:
        print("System recovered and continuing...\n")
        print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
