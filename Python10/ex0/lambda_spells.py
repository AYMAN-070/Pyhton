def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort artifacts by power (descending)"""
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filters a list of mages to include only those with
    power >= min_power"""
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Transforms a list of spell names by decorating each spell string"""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """basic statistics of mages' power levels: maximum, minimum,
    and average"""
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    powers = list(map(lambda m: m['power'], mages))
    max_m = max(powers)
    min_m = min(powers)
    avg_m = round(sum(powers) / len(powers), 2)
    return {'max_power': max_m, 'min_power': min_m, 'avg_power': avg_m}


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'}
    ]
    mages = [
        {'name': 'Albus', 'power': 90, 'element': 'fire'},
        {'name': 'Luna', 'power': 40, 'element': 'moon'}
    ]
    spells = ["fireball", "heal"]

    print("--- Testing Lambda Sanctum ---")
    sorted_art = artifact_sorter(artifacts)
    print(f"Sorted: {sorted_art[0]['name']} ({sorted_art[0]['power']})")
    print(f"Sorted: {sorted_art[1]['name']} ({sorted_art[1]['power']})")

    powerful = power_filter(mages, 50)
    print(f"Powerful mages: {[m['name'] for m in powerful]}")

    print(f"Spells: {spell_transformer(spells)}")

    print(f"Stats: {mage_stats(mages)}")
