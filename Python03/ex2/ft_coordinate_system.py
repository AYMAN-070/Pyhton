# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_coordinate_system.py                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/28 22:38:14 by ayman             #+#    #+#             #
#    Updated: 2026/01/06 15:37:18 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import math
import sys


def calculate_distance(p1: tuple[float, ...], p2: tuple[float, ...]) -> float:
    """Calculates Euclidean distance between two 3D points."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


if __name__ == "__main__":
    origin: tuple[int, int, int] = (0, 0, 0)
    if len(sys.argv) == 1:
        print("=== Game Coordinate System ===")
        print()
        pos1: tuple[int, int, int] = (10, 20, 5)
        distance = calculate_distance(origin, pos1)
        print(f"Position created: {pos1}")
        print(f"Distance between {origin} and {pos1}: {distance:.2f}")
        print()

        print("Parsing coordinates: \"3,4,0\"")
        input_str = "3,4,0"
        data = input_str.split(",")
        tmp = []
        for num in data:
            tmp.append(int(num))
        coordinates = tuple(tmp)
        print("Parsed position: ", coordinates)
        distance2 = calculate_distance(coordinates, origin)
        print(f"Distance between (0, 0, 0) and (3, 4, 0): {distance2:.1f}")
        print()

        print("Parsing invalid coordinates: \"abc,def,ghi\"")
        try:
            input_str2 = "abc,def,ghi"
            data = input_str2.split(",")
            tmp = []
            for num in data:
                tmp.append(int(num))
            print("Parsing invalid coordinates: \"abc,def,ghi\"")
            coordinates1 = tuple(tmp)
            print("Parsed position: ", coordinates1)
            distance3 = calculate_distance(coordinates1, origin)
            print(f"Distance between {origin} and (3, 4, 0): {distance3:.2f}")
            print()
        except ValueError as e:
            print("Error parsing coordinates: invalid literal for int() with "
                  "base 10: 'abc")
            print("Error details - Type: ValueError,  Args: ", e)
        print()

        print("Unpacking demonstration:")
        x, y, z = coordinates
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: x={x}, y={y}, z={z}")

    if len(sys.argv) > 1:
        try:
            user_pos = sys.argv[1]
            data = user_pos.split(",")
            tmp = []
            for num in data:
                tmp.append(int(num))
            coordinates3 = tuple(tmp)
            dist = calculate_distance(coordinates3, origin)
            print("Parsed position: ", coordinates3)
            print(f"Distance between {origin} and {coordinates3}: {dist:.2f}")
        except ValueError as e:
            print("Error parsing coordinates:", e)
