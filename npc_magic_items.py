import random
import re
from treasure.item_generator import generate_item

# ===========================================
# MAGIC ITEM TABLE (ACKS NPC WEALTH)
# ===========================================

MAGIC_ITEM_TABLE = {
    0:  {"common": "1%"},
    1:  {"common": "30%"},
    2:  {"common": "90%"},
    3:  {"common": "1"},
    4:  {"common": "1d4-1"},
    5:  {"common": "2", "uncommon": "1"},
    6:  {"common": "4", "uncommon": "2"},
    7:  {"common": "4", "uncommon": "2", "rare": "66%"},
    8:  {"common": "5", "uncommon": "3", "rare": "1", "very_rare": "10%"},
    9:  {"common": "5", "uncommon": "3", "rare": "2", "very_rare": "50%"},
    10: {"common": "5", "uncommon": "5", "rare": "3", "very_rare": "75%"},
    11: {"common": "7", "uncommon": "7", "rare": "7", "very_rare": "2"},
    12: {"common": "8", "uncommon": "7", "rare": "7", "very_rare": "4"},
    13: {"common": "10", "uncommon": "10", "rare": "9", "very_rare": "5", "legendary": "1d4-1"},
    14: {"common": "10", "uncommon": "10", "rare": "10", "very_rare": "10", "legendary": "6"},
}

RARITY_ORDER = ["common", "uncommon", "rare", "very_rare", "legendary"]

# ===========================================
# PARSER: '3' / '66%' / '1d4-1'
# ===========================================

def parse_magic_item_count(expr: str) -> int:
    """
    Accepted formats:
    - '3'
    - '66%'
    - '1d4-1'
    - '1d2'
    """
    expr = expr.strip()

    # Probability: "66%"
    if expr.endswith("%"):
        chance = int(expr[:-1])
        return 1 if random.randint(1, 100) <= chance else 0

    # Dice expression: "1d4-1"
    m = re.match(r"(\d+)d(\d+)([+-]\d+)?", expr)
    if m:
        n = int(m.group(1))
        d = int(m.group(2))
        mod = int(m.group(3)) if m.group(3) else 0
        return sum(random.randint(1, d) for _ in range(n)) + mod

    # Pure integer
    return int(expr)


# ===========================================
# MAIN API: GENERATE MAGIC ITEMS FOR NPC LEVEL
# ===========================================

def generate_magic_items_for_level(level: int, mode: str, style: str):
    """
    Returns a list of generated magical items for an NPC of given level.
    Currently only supports Heroic/Gritty mode.
    Classic mode will be added later.
    """

    if mode not in ("heroic", "gritty"):
        return []  # Classic handled elsewhere later

    lvl = min(level, 14)
    row = MAGIC_ITEM_TABLE.get(lvl, {})

    results = []

    for rarity in RARITY_ORDER:
        if rarity not in row:
            continue

        count_expr = row[rarity]
        amount = parse_magic_item_count(count_expr)

        for _ in range(amount):
            item = generate_item(mode, style, rarity)["item"]
            results.append(item)

    return results


# ===========================================
# DEBUG TEST
# ===========================================

if __name__ == "__main__":
    for lvl in [1, 5, 8, 10, 13]:
        print(f"\n=== LEVEL {lvl} ===")
        items = generate_magic_items_for_level(lvl, "heroic", "ancient_myth")
        for it in items:
            print(f"- {it['rarity']:>10} | {it['name']}")

