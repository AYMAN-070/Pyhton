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
    """A plant class with protected attributes and data validation."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the secure plant."""
        self.name = name
        self._height = height
        self._age = age

    def info(self):
        """Return formatted plant information."""
        return f"{self.name} ({self._height}cm, {self._age} days)"

    def get_height(self):
        """Return the plant's height."""
        return self._height

    def get_age(self):
        """Return the plant's age."""
        return self._age

    def set_height(self, new_height):
        """Update height with validation."""
        if new_height < 0:
            print(f"Invalid operation attempted: height {new_height}cm "
                  "[REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm [OK]")

    def set_age(self, new_age):
        """Update age with validation."""
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} days "
                  "[REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = new_age
            print(f"Age updated: {new_age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", 0, 0)
    print("Plant created:", plant1.name)
    plant1.set_height(25)
    plant1.set_age(30)
    print()
    plant1.set_height(-5)
    print()
    print(f"Current plant: {plant1.info()}")
