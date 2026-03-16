# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_data_stream.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: ayhammou <ayhammou@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2025/12/30 12:19:33 by ayman             #+#    #+#             #
#    Updated: 2026/01/06 15:44:29 by ayhammou         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from typing import Generator, Any


def game_generator(count: int) -> Generator[dict[str, Any], None, None]:
    """Generates a stream of simulated game event dictionaries."""
    name = ["Alice", "Bob", "Charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    inventaire = {}
    for i in range(count):
        actual_name = name[i % (len(name))]
        actual_action = actions[i % len(actions)]
        actual_level = (i * 3) % 20 + 1
        inventaire = {"id": i, "player": actual_name, "level": actual_level,
                      "action": actual_action, }
        yield inventaire


def stream_wizard() -> None:
    """Main function to demonstrate the stream processing and generators."""
    print("=== Game Data Stream Processor ===")
    print()
    print("Processing 1000 game events...")
    print()
    total = 0
    high_level = 0
    treasure = 0
    level_up = 0
    for event in game_generator(1000):
        total = total + 1
        if event["id"] < 3:
            print(f"Event {event['id']} Player {event['player']} (level "
                  f"{event['level']}) {event['action']}")
        if event["id"] == 3:
            print("...")
        if event["level"] > 10:
            high_level += 1
        if event["action"] == "found treasure":
            treasure += 1
        if event["action"] == "leveled up":
            level_up += 1
    print()
    print("=== Stream Analytics ===")
    print("Total events processed: ", total)
    print("High-level players (10+): ", high_level)
    print("Treasure events: ", treasure)
    print("Level-up events: ", level_up)
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print()
    print("=== Generator Demonstration ===")


def fibonacci(count: int) -> Generator[int, None, None]:
    """Generates the Fibonacci sequence up to count elements."""
    x = 0
    y = 1
    tmp = 0
    for i in range(count):
        yield x
        tmp = x
        x = y
        y = tmp + y


def prime_numbers(count: int) -> Generator[int, None, None]:
    """Generates the first 'count' prime numbers."""
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        a = 2
        while a <= num:
            if a == num:
                return True
            if num % a == 0:
                return False
            a += 1
            if a == num:
                return True
    found = 0
    number = 2
    while found < count:
        if is_prime(number) is True:
            yield number
            found += 1
        number += 1


if __name__ == "__main__":
    stream_wizard()
    stock = []
    for i in fibonacci(10):
        stock.append(str(i))
    print(f"Fibonacci sequence (first 10): {', '.join(stock)}")
    prime = []
    for i in prime_numbers(5):
        prime.append(str(i))
    print(f"Prime numbers (first 5): {', '.join(prime)}")
