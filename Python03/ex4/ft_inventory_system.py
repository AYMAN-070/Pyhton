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

if __name__ == "__main__":
    inevntaire = {
        "sword": {"type": "weapon", "rarity": "rare", "quantity": 1,
                  "price": 500},
        "potion": {"type": "consumable", "rarity": "common", "quantity": 5,
                   "price": 50},
        "shield": {"type": "armor", "rarity": "uncommon", "quantity": 1,
                   "price": 200},
    }
    print("=== Player Inventory System ===")
    print()
    print("=== Alice's Inventory ===")
    for name, items in inevntaire.items():
        print(f"{name} ({items['type']}, {items['rarity']}): "
              f"{items['quantity']}x @ {items['price']} gold each = "
              f"{items['price'] * items['quantity']} gold")
    print()
    value = 0
    for items in inevntaire.values():
        value = value + (items["price"] * items["quantity"])
    print(f"Inventory value: {value} gold")
    count = 0
    for items in inevntaire.values():
        count = count + items["quantity"]
    print(f"Item count: {count} items")
    categories = {}
    for x in inevntaire.values():
        tp = x["type"]
        qty = x["quantity"]
        categories[tp] = categories.get(tp, 0) + qty
    display = []
    for x, y in categories.items():
        display.append(f"{x}({y})")
    print(f"Categories: {', '.join(display)}")
    print()
    print("=== Transaction: Alice gives Bob 2 potions ===")
    inevntaire["potion"]["quantity"] = inevntaire["potion"]["quantity"] - 2
    bob_inventaire = {}
    bob_inventaire["potion"] = inevntaire["potion"].copy()
    bob_inventaire["potion"]["quantity"] = 2
    print("Transaction successful !")
    print()
    print("=== Updated Inventories ===")
    print("Alice potion", inevntaire["potion"]["quantity"])
    print("Bob potion: ", bob_inventaire["potion"]["quantity"])
    print()
    print("=== Inventory Analytics ===")
    alice_value = 0
    alice_quantity = 0
    bob_value = 0
    bob_quantity = 0
    for item in bob_inventaire.values():
        bob_value = bob_value + (item["price"] * item["quantity"])
        bob_quantity += item["quantity"]
    for item in inevntaire.values():
        alice_value = alice_value + (item["price"] * item["quantity"])
        alice_quantity += item["quantity"]
    if alice_value >= bob_value:
        print(f"Most valuable player: Alice ({alice_value} gold)")
    else:
        print(f"Most valuable player: Alice ({bob_value} gold)")
    if alice_quantity >= bob_quantity:
        print(f"Most items: Alice ({alice_quantity} items)")
    else:
        print(f"Most items: Alice ({bob_quantity} items)")
    rare_item = []
    for name, details in inevntaire.items():
        if details["rarity"] == 'rare':
            rare_item.append(name)
    for name, details in bob_inventaire.items():
        if details["rarity"] == 'rare':
            rare_item.append(name)
    print(f"Rarest items: {', '.join(rare_item)}")
