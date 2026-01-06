# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_different_errors.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/25 11:56:37 by ayman             #+#    #+#             #
#    Updated: 2025/12/25 15:08:27 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def garden_operation(function):
    if function == "ValueError":
        int("abc")
    elif function == "ZeroDivisionError":
        10 / 0
    elif function == "FileNotFoundError":
        open("test.txt")
    elif function == "KeyError":
        dict = {}
        dict["rien"]


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print()
    print("Testing ValueError...")
    try:
        garden_operation("ValueError")
    except ValueError as e:
        print("Caught ValueError: ", e)
        print()
    print("Testing ZeroDivisionError...")
    try:
        garden_operation("ZeroDivisionError")
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
        print()
    print("Testing FileNotFoundError")
    try:
        garden_operation("FileNotFoundError")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)
        print()
    print("Testing KeyError")
    try:
        garden_operation("KeyError")
    except KeyError as e:
        print("Caught KeyError:", e)
        print()
    print("Testing multiple errors together...")
    try:
        garden_operation("ValueError")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


if __name__ == "__main__":
    test_error_types()
