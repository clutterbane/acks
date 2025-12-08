import random
from terrains import normalize_terrain
from terrains import terrain_id
from monster_lookup import lookup_monster
from monster_lookup import roll_1d100
import importlib
from monsters.barrens_rocky_sandy import MONSTER_TABLE

def load_monster_table(terrain_alias):
    """
    Loads MONSTER_TABLE from monsters/{terrain_alias}.py
    Example: alias 'barrens_rocky_sandy' → monsters/barrens_rocky_sandy.py
    """
    module_name = f"monsters.{terrain_alias}"
    module = importlib.import_module(module_name)
    return module.MONSTER_TABLE


# ============================================
# LAIRS PER HEX — RAW ACKS (final form)
# ============================================

LAIRS_PER_HEX = {
    "Barrens (Rocky/Sandy)": "1d4",
    "Barrens (Tundra)": "1d4",

    "Desert (Rocky)": "1d2",
    "Desert (Sandy)": "1d4",

    "Forest (Deciduous)": "2d4",
    "Forest (Taiga)": "2d4",

    "Grassland (Farmland/Prairie)": "1d3",
    "Grassland (Savannah)": "1d3-1",
    "Grassland (Steppe)": "1d3-1",

    "Hills (Forested)": "2d4",
    "Hills (Rocky)": "1d4",

    "Jungle (Any)": "2d8",

    "Mountains (Forested)": "2d4",
    "Mountains (Rocky)": "1d4+1",
    "Mountains (Snowy)": "1d4+1",
    "Mountains (Volcanic)": "1d4+1",

    "Scrubland (Sparse)": "1d2",
    "Scrubland (Dense)": "2d4",

    "Swamp (Any)": "2d4+1",
}


# ============================================
# DICE ROLLER
# ============================================

def roll_dice(expr: str) -> int:
    """
    Parses dice expressions like '2d4', '1d3-1', '1d4+1'
    """
    expr = expr.lower().replace(" ", "")

    if "+" in expr:
        dice, mod = expr.split("+")
        mod = int(mod)
    elif "-" in expr:
        dice, mod = expr.split("-")
        mod = -int(mod)
    else:
        dice, mod = expr, 0

    n, d = dice.split("d")
    n, d = int(n), int(d)

    total = sum(random.randint(1, d) for _ in range(n))
    return total + mod


# ============================================
# LAIR COUNT ROLLER
# ============================================

def roll_lairs(terrain: str) -> int:
    """
    Returns the number of lairs in a hex of the given terrain.
    """
    terrain = normalize_terrain(terrain)
    entry = LAIRS_PER_HEX[terrain]

    if isinstance(entry, str):
        return roll_dice(entry)
    elif isinstance(entry, dict):
        variant = random.choice(list(entry.keys()))
        return roll_dice(entry[variant])
    else:
        raise ValueError(f"Invalid lair entry for {terrain}: {entry}")


# ============================================
# RARITY ROLLER — RAW ACKS 1d20 table
# ============================================

def roll_rarity():
    """
    Rolls 1d20 to determine rarity category.

    1–8   → Common
    9–14  → Uncommon
    15–18 → Rare
    19–20 → Very Rare
    """
    roll = random.randint(1, 20)

    if 1 <= roll <= 8:
        rarity = "Common"
    elif 9 <= roll <= 14:
        rarity = "Uncommon"
    elif 15 <= roll <= 18:
        rarity = "Rare"
    else:
        rarity = "Very Rare"

    return rarity, roll


# ============================================
# FULL HEX LAIR GENERATOR
# ============================================

def generate_lairs_for_hex(terrain: str):
    terrain_name = normalize_terrain(terrain)
    num_lairs = roll_lairs(terrain_name)

    alias = terrain_id(terrain_name)
    monster_table = load_monster_table(alias)

    lairs = []
    for _ in range(num_lairs):
        rarity, rarity_roll = roll_rarity()
        monster_name, monster_roll = lookup_monster(monster_table, rarity)

        lairs.append({
            "rarity": rarity,
            "rarity_roll": rarity_roll,
            "monster": monster_name,
            "monster_roll": monster_roll,
        })

    return {
        "terrain": terrain_name,
        "num_lairs": num_lairs,
        "lairs": lairs
    }
