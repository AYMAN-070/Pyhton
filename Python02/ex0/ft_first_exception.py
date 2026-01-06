# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_first_exception.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/25 01:15:28 by ayman             #+#    #+#             #
#    Updated: 2025/12/25 11:57:33 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def check_temperature(temp_str):
    try:
        total = int(temp_str)
        print(f"Testing temperature: {temp_str}")
        if total > -1 and total < 41:
            print(f"Temperature {temp_str} is perfect for plants!\n")
            return total
        elif total > 40:
            print(f"Error: {temp_str} is too hot for plants (max 40°C)\n")
        elif total < 1:
            print(f"Error: {temp_str} is too cold for plants (min 0°C)\n")
    except Exception:
        print(f"Testing temperature: {temp_str}")
        print(f"Error: {temp_str} is not a valid number\n")


def test_temperature_input():
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")


if __name__ == "__main__":
    test_temperature_input()
