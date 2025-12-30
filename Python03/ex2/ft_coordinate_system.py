# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_coordinate_system.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/28 22:38:14 by ayman             #+#    #+#              #
#    Updated: 2025/12/29 13:22:05 by ayman            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math
if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    print("Position created: (10, 20, 5)")
    distance = math.sqrt((10 - 0)**2 + (20 - 0)**2 + (5 - 0)**2)
    print(f"Distance between (0, 0, 0) and (10, 20, 5): {distance:.2f}")
    print()
    
    print("Parsing coordinates: \"3,4,0\"")
    input_str = "3,4,0"
    data = input_str.split(",")
    tmp = []
    for num in data:
        tmp.append(int(num))
    coordinates = tuple(tmp)
    print("parsed position: ", coordinates)
    distance2 = math.sqrt((3 - 0)**2 + (4 - 0)**2)
    print(f"Distance between (0, 0, 0) and (3, 4, 0): {distance2:.2f}")
    print()
    
    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    try:
        input_str2 = "abc,def,ghi"
        data = input_str2.split(",")
        tmp = []
        for num in data:
            tmp = int(num)
        print("Parsing invalid coordinates: \"abc,def,ghi\"")
        coordinates1 = tuple(tmp)
        print("parsed position: ", coordinates1)
        distance3 = math.sqrt((coordinates1[0] - 0)**2 + (coordinates1[1] - 0)**2 + (coordinates1[2] - 0)**2)
        print(f"Distance between (0, 0, 0) and (3, 4, 0): {distance3:.2f}")
        print()
    except ValueError as e:
        print("Error parsing coordinates: invalid literal for int() with base 10: 'abc")
        print("Error details - Type: ValueError,  Args: ", e)
    print()
        
    print("Unpacking demonstration:")
    x, y, z = coordinates
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: x={x}, y={y}, z={z}")