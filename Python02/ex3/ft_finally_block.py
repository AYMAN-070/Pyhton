# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_finally_block.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/27 12:31:53 by ayman             #+#    #+#             #
#    Updated: 2026/01/06 15:28:16 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def water_plants(plant_list):
    print("Opening watering system")
    i = 0
    try:
        for plant in plant_list:
            if not isinstance(plant, str) or plant == "":
                raise ValueError
            print("watering ", plant)
            i += 1
    except ValueError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)\n")
        if i == len(plant_list):
            print("Watering completed successfully!\n")
        else:
            print("Cleanup always happens, even with errors!")


def test_watering_system():
    print("=== Garden Watering system ===")
    print()
    print("Testing normal watering...")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    print("Testing with error...")
    plant_list = ["tomato", ""]
    water_plants(plant_list)


if __name__ == "__main__":
    test_watering_system()
