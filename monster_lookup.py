import random

def roll_1d100():
    return random.randint(1, 100)

def lookup_monster(monster_table, rarity):
    """
    monster_table: dict {"Common": [(lo, hi, name)...], ...}
    rarity: "Common" / "Uncommon" / "Rare" / "Very Rare"
    """
    roll = roll_1d100()

    for low, high, monster in monster_table[rarity]:
        if low <= roll <= high:
            return monster, roll

    raise ValueError(f"No monster range found for roll {roll} in rarity {rarity}")
