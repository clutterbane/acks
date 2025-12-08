import random
import re


# ============================================================
# Roll a dice expression: "1d6", "2d8+1", "1d4-2"
# ============================================================

def roll(expr: str) -> int:
    """
    Roll dice expression like "1d6", "2d8+3", "3d10-2".
    Always returns an integer.
    """
    dice = parse_dice(expr)
    total = 0
    for _ in range(dice["n"]):
        total += random.randint(1, dice["die"])
    total += dice["mod"]
    return total


# ============================================================
# Parse dice expression into components
# ============================================================

def parse_dice(expr: str):
    """
    Parses "2d6+3" into dict: {"n": 2, "die": 6, "mod": 3}
    Supports: XdY, XdY+Z, XdY-Z
    """

    expr = expr.strip().lower()

    pattern = r"(\d+)d(\d+)([+-]\d+)?"
    match = re.fullmatch(pattern, expr)

    if not match:
        raise ValueError(f"Invalid dice expression: {expr}")

    n = int(match.group(1))
    die = int(match.group(2))
    mod = int(match.group(3)) if match.group(3) else 0

    return {"n": n, "die": die, "mod": mod}


# ============================================================
# Utility: roll table from dict with ranges
# Example table:
#   { (1,3): "Goblin", (4,6): "Orc" }
# ============================================================

def roll_from_ranges(table: dict) -> str:
    """
    table: { (low, high): value }
    Rolls 1-100 unless you pre-adjust ranges.
    """
    r = random.randint(1, 100)
    for (low, high), value in table.items():
        if low <= r <= high:
            return value
    return None


# ============================================================
# Utility: roll N times and return list
# ============================================================

def roll_multiple(expr: str, times: int):
    return [roll(expr) for _ in range(times)]
