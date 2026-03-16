# ************************************************************************** #
#                                                                            #
#                                                         :::      ::::::::  #
#    ft_inventory_system.py                             :+:      :+:    :+:  #
#                                                     +:+ +:+         +:+    #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+       #
#                                                 +#+#+#+#+#+   +#+          #
#    Created: 2025/12/29 14:41:32 by ayman             #+#    #+#            #
#    Updated: 2026/01/06 15:44:09 by ayhammou         ###   ########.fr      #
#                                                                            #
# ************************************************************************** #

import sys


def inventory_master(argv: list[str]) -> None:
    """Analyzes game inventory from command line arguments using dictionaries.
    """
    print("=== Inventory System Analysis ===")
    inventory = {}
    for arg in argv[1:]:
        try:
            name, qty = arg.split(":")
            inventory[name] = int(qty)
        except ValueError:
            continue
    if not inventory:
        print("No items to analyze.")
        return
    total = sum(inventory.values())
    types = len(inventory)
    print("Total items in inventory:", total)
    print("Unique item types:", types)
    print()
    print("=== Current Inventory ===")
    for x, y in inventory.items():
        percentage = (y / total) * 100
        print(f"{x}: {y} units ({percentage:.1f}%)")
    print()
    print("=== Inventory Statistics ===")
    max_qty = -1
    max1 = ""
    for name, qty in inventory.items():
        if qty > max_qty:
            max_qty = qty
            max1 = name
    min_qty = 10000
    min1 = ""
    for name, qty in inventory.items():
        if qty < min_qty:
            min_qty = qty
            min1 = name
    print(f"Most abundant: {max1} ({inventory[max1]} units)")
    print(f"Least abundant: {min1} ({inventory[min1]} units)")
    print()
    print("=== Item Categories ===")
    categories = {"Moderate": {}, "Scarce": {}}
    restock = []
    for x, y in inventory.items():
        if y >= 5:
            categories["Moderate"][x] = y
        else:
            categories["Scarce"][x] = y
            if y < 2:
                restock.append(x)
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")
    print()
    print("=== Management Suggestions ===")
    print("Restock needed:", restock)
    print()
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    sword_count = inventory.get("sword", 0)
    print(f"Sample lookup - 'sword' in inventory: {sword_count > 0}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        inventory_master(sys.argv)
    else:
        print("No arguments provided !")
