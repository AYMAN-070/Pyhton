# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_management.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/27 15:38:35 by ayman             #+#    #+#              #
#    Updated: 2025/12/27 20:28:41 by ayman            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenManager:
    @staticmethod
    def add_plants(plant_list):
        print("Adding plants to garden...")
        try:
            for plant in plant_list:
                if not isinstance(plant, str) or len(plant) < 1:
                    raise ValueError ("Plant name cannot be empty!\n")
                print(f"Added {plant} successfully")
        except ValueError as e:
            print("Error adding plant: ", e)
    @staticmethod     
    def water_plants(plant_list):
        print("Watering plants...")
        print("Opening watering system")
        for plant in plant_list:
            if len(plant) > 0:
                print(f"Watering {plant} - success")
        print("Closing watering system (Cleanup)\n")
     
    @staticmethod   
    def checking_health(plant_list, water_level, sun_hours):
        print("Checking plant health...")
        try:
            if isinstance (plant_list, str):
                plant_list = [plant_list]
            for plant in plant_list:
                if water_level < 1:
                    raise ValueError(f"Error checking {plant}: Water level {water_level} is too low (min 1)\n")
                if water_level > 10:
                    raise ValueError(f"Error checking {plant}: Water level {water_level} is too high (max 10)\n")
                if sun_hours < 2:
                    raise ValueError(f"Error checking {plant}: Sunlight hours {sun_hours} is too low (min 2)\n")
                if sun_hours > 12:
                    raise ValueError(f"Error checking {plant}: Sunlight hours {sun_hours} is too high (max 12)\n")
                print(f"{plant}: healthy (water: {water_level}, sun: {sun_hours})\n")
        except ValueError as e:
            print(e)
            
    @staticmethod
    def testing_error(water_status):
        print("Testing error recovery...")
        try:
            if water_status == "Drought":
                raise ValueError ("Caught GardenError: Not enough water in tank")
        except ValueError as e:
            print(e)
        finally:
            print("System recovered and continuing...\n")
            print("Garden management system test complete!")   

if __name__ == "__main__":
    
    plant_list = ["tomato", "lettuce", ""]
    GardenManager.add_plants(plant_list)
    GardenManager.water_plants(plant_list)
    GardenManager.checking_health("tomato", 5, 8)
    GardenManager.testing_error("Drought")