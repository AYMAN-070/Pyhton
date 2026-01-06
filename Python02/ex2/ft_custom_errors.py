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
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_error():
    print("Testing PlantError...")
    try:
        plant_status = "dead"
        if plant_status == "dead":
            raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PLantError: {e}")
    print("Testing WaterError...")
    try:
        Water_status = "Drought"
        if Water_status == "Drought":
            raise WaterError("caught WaterError: "
                             "Not enough water in the tank!")
    except WaterError as e:
        print(e)
    print("Testing catching all garden errors...")
    try:
        plant_status = "dead"
        if plant_status == "dead":
            raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        Water_status = "Drought"
        if Water_status == "Drought":
            raise WaterError("caught a garden error: "
                             "Not enough water in the tank!")
    except GardenError as e:
        print(e)


if __name__ == "__main__":
    test_error()
