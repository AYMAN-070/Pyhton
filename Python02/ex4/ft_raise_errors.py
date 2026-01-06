# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_raise_errors.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/27 14:12:36 by ayman             #+#    #+#             #
#    Updated: 2025/12/28 12:11:05 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if not isinstance(plant_name, str) or plant_name == "":
            raise ValueError("Error: Plant name cannot be empty!\n")
        if water_level < 1:
            raise ValueError(f"Error: Water level {water_level} "
                             f"is too low (min 1)\n")
        if water_level > 10:
            raise ValueError(f"Error: Water level {water_level} "
                             f"is too high (max 10)\n")
        if sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)\n")
        if sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             f"is too high (max 12)\n")
        print(f"Plant {plant_name} is healthy!\n")
    except ValueError as e:
        print(e)


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("tomato", 4, 3)
    print("Testing empty plant name...")
    check_plant_health("", 3, 3)
    print("Testing bad water level...")
    check_plant_health("tomato", 15, 3)
    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 3, 0)
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
