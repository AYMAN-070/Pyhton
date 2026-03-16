import time
import functools


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"SPELL COMPLETED IN {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    """ Decorator factory that ensures the first argument"""
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) > 1:
                power = args[2]
            else:
                power = kwargs.get("power", 0)
            if not isinstance(power, (int, float)):
                try:
                    power = int(power)
                except (ValueError, TypeError):
                    return "Invalid power value"
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for test in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if test < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {test}/{max_attempts})")
                    else:
                        print(f"Spell casting failed after"
                              f"{max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"successfully cast {spell_name} with power {power}"


if __name__ == "__main__":
    test_powers = [30, 9, 18, 17]
    spell_names = ['meteor', 'flash', 'tornado', 'earthquake']
    mage_names = ['River', 'Sage', 'Storm', 'Rowan', 'Kai', 'Casey']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']
    guild = MageGuild()
    print("Testing names")
    for name in mage_names:
        print(f"{name}: {guild.validate_mage_name(name)}")
    for name in invalid_names:
        print(f"{name}: {guild.validate_mage_name(name)}")
    print()
    print("Testing sorts")
    for i in range(len(test_powers)):
        res = guild.cast_spell(spell_names[i], test_powers[i])
        print(f"Sort: {spell_names[i]} (Power {test_powers[i]}) -> {res}")
    print()
    print("Testing Retry Spell")

    @retry_spell(max_attempts=3)
    def test():
        return "Fiiire!"
    print(test())

    @retry_spell(max_attempts=3)
    def test():
        raise ValueError("Failing")
    print(test())
