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

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """Validates plant health parameters and raises ValueError"""
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
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Demonstrates catching errors raised by check_plant_health."""
    print("=== Garden Plant Health Checker ===")
    print()
    test = [
        ("Good values", ("tomato", 5, 8)),
        ("Empty name", ("", 5, 8)),
        ("Bad water", ("tomato", 15, 8)),
        ("Bad sunlight", ("tomato", 5, 0))
    ]
    for x, y in test:
        print("Testing", x)
        try:
            result = check_plant_health(*y)
            print(result)
        except ValueError as e:
            print("Error", e)
        print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
