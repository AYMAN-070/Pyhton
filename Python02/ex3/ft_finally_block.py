# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_finally_block.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/27 12:31:53 by ayman             #+#    #+#              #
#    Updated: 2025/12/27 14:01:33 by ayman            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def water_plants(plant_list):
    print("Opening watering system")
    i = 0
    try:
        for plant in plant_list:
            if not isinstance(plant, str) or len(plant) < 1:
                raise ValueError
            print("watering ", plant)
            i += 1
    except ValueError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")
        if i == len(plant_list):
            print("Watering completed successfully!\n")
        else:
            print("\nCleanup always happens, even with errors!") 
        
def test_watering_system():
    print("=== Garden Watering system ===")
    print("Testing normal watering...")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    print("Testing with error...")
    plant_list = ["tomato", ""]
    water_plants(plant_list)

if __name__ == "__main__":
    test_watering_system()