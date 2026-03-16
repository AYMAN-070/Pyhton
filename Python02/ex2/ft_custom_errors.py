# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_custom_errors.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/25 21:24:12 by ayman             #+#    #+#             #
#    Updated: 2025/12/27 12:24:02 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    """Base class for all exceptions in this garden module."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-specific issues."""
    pass


class WaterError(GardenError):
    """Exception raised for irrigation-specific issues."""
    pass


def test_error() -> None:
    """Demonstrates how to raise and catch custom exceptions."""
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        plant_status = "dead"
        if plant_status == "dead":
            raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        water_status = "Drought"
        if water_status == "Drought":
            raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        plant_status = "dead"
        if plant_status == "dead":
            raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        water_status = "Drought"
        if water_status == "Drought":
            raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_error()
