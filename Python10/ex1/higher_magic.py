def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Combine two spell functions into a single function"""
    def combined(*args, **wkargs) -> tuple:
        return (spell1(*args, **wkargs), spell2(*args, **wkargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """Return a new function that multiplies the base spell’s
    result by multiplier"""
    def multiply(*args, **kwargs) -> int | float:
        return (base_spell(*args, **kwargs) * multiplier)
    return multiply


def conditional_caster(condition: callable, spell: callable) -> callable:
    """Return a function that only casts the spell if condition returns True"""
    def cast(*args, **kwargs) -> any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[callable]) -> callable:
    """function that casts all spells in order"""
    def cast(*args, **kwargs) -> list:
        return [s(*args, **kwargs) for s in spells]
    return cast


if __name__ == "__main__":
    def fireball(target: str) -> str: return f"Fireball hits {target}"
    def heal(target: str) -> str: return f"Heals {target}"
    def basic_damage(target: str) -> int: return 10
    def is_dragon(target: str) -> bool: return target == "Dragon"

    print("\n--- Testing Higher Realm ---")
    combined = spell_combiner(fireball, heal)
    print(f"Combined: {combined('Dragon')}")

    mega_spell = power_amplifier(basic_damage, 3)
    print(f"Amplified: {mega_spell('Dragon')}")

    dragon_only = conditional_caster(is_dragon, fireball)
    print(f"On Dragon: {dragon_only('Dragon')}")
    print(f"On Human: {dragon_only('Human')}")
    test = spell_sequence([fireball, heal])
    result = test("Dragon")
    print("Sequence result : ", result)
