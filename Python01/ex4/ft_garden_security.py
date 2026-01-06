# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_security.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayman <ayman@student.42.fr>                +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/22 19:19:15 by ayman             #+#    #+#             #
#    Updated: 2025/12/22 20:02:03 by ayman            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age

    def info(self):
        return f"{self.name} ({self._height}cm, {self._age} days)"

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, new_height):
        if new_height < 0:
            print("Security: Negative height rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm [OK]")

    def set_age(self, new_age):
        if new_age < 0:
            print("Security: Negative age rejected")
        else:
            self._age = new_age
            print(f"Age updated: {new_age}days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", 0, 0)
    plant1.set_height(25)
    plant1.set_age(30)
    print("Invalid operation attempted: height -5cm")
    plant1.set_height(-5)
    print(f"Current plant: {plant1.info()}")
