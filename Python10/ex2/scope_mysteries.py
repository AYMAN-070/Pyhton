def mage_counter() -> callable:
    count = 0

    def call() -> int:
        nonlocal count
        count += 1
        return count
    return call


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def power_(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return power_


"""mon_sort = spell_accumulator(10) # initial_power = 10
print(mon_sort(5))  # amount = 5, total_power devient 15
print(mon_sort(20)) # amount = 20, total_power devient 35"""


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item_name: str) -> str:
        return (f"{enchantment_type} {item_name}")
    return enchant


def memory_vault() -> dict[str, callable]:
    storage = {}

    def store(key: str, value: any) -> None:
        storage[key] = value

    def recall(key: str) -> any:
        return storage.get(key, "Memory not found")
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("\n--- Testing Memory Depths ---")

    counter = mage_counter()
    print(f"Count 1: {counter()}, Count 2: {counter()}")

    acc = spell_accumulator(100)
    print(f"Accumulated: {acc(50)}")

    fire_factory = enchantment_factory("Flaming")
    print(f"Enchant: {fire_factory('Sword')}")

    vault = memory_vault()
    vault['store']("secret", "Mana Crystal")
    print(f"Recall: {vault['recall']('secret')}")
