import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {"add": operator.add, "multiply": operator.mul,
                  "max": max, "min": min
                  }
    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {'fire_enchant': functools.partial(base_enchantment, power=50,
                                              element='fire'),
            'ice_enchant': functools.partial(base_enchantment, power=50,
                                             element='ice'),
            'lightning_enchant': functools.partial(base_enchantment, power=50,
                                                   element='lightning')
            }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def dispatcher(spell):
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell: int):
        return f"Casting damage spell: {spell} points"

    @dispatcher.register(str)
    def _(spell: str):
        return f"Casting enchantment: {spell}"

    @dispatcher.register(list)
    def _(spell: list):
        return f"Multi-casting {len(spell)} spells"

    return dispatcher


if __name__ == "__main__":
    print("\n--- Testing Ancient Library ---")

    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")

    def base(power, element, target): return f"{element} ({power}) on {target}"
    enchants = partial_enchanter(base)
    print(f"Partial: {enchants['fire_enchant'](target='Hydra')}")

    print(f"Fib(10): {memoized_fibonacci(10)}")

    dispatch = spell_dispatcher()
    print(f"Int dispatch: {dispatch(100)}")
    print(f"Str dispatch: {dispatch('Invisibility')}")
