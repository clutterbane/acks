import random
from treasure.roller import roll

# ------------------------------------------------------------
# JEWELRY TABLES – based on ACKS Jewelry Tables
# ------------------------------------------------------------

TRINKET_TABLE = [
    (1, 10, "2d20", ["Bone", "Scrimshaw", "Beast Parts"]),
    (11, 25, "2d10*10", ["Glass", "Shells", "Wrought Copper", "Brass", "Bronze"]),
    (26, 40, "2d4*100", ["Fine Wood", "Porcelain", "Wrought Silver"]),
    (41, 70, "2d6*100", ["Alabaster", "Chryselephantine", "Ivory", "Wrought Gold"]),
    (71, 80, "3d6*100", ["Carved Jade", "Wrought Platinum"]),
    (81, 95, "1d4*1000", ["Wrought Orichalcum", "Silver studded w/ Turquoise",
                          "Silver studded w/ Moonstone", "Silver studded w/ Opal"]),
    (96, 100, "2d4*1000", ["Silver studded w/ Jet", "Silver studded w/ Amber",
                           "Silver studded w/ Pearl"]),
]

JEWELRY_TABLE = [
    (101, 125, "3d4*1000", ["Gold studded w/ Topaz", "Gold studded w/ Jacinth", "Gold studded w/ Ruby"]),
    (126, 145, "2d8*1000", ["Platinum studded w/ Diamond", "Platinum studded w/ Sapphire",
                            "Platinum studded w/ Emerald"]),
    (146, 155, "3d6*1000", ["Electrum Pendant w/ Pearls & Star Rubies",
                            "Silver Pendant w/ Pearls & Star Rubies"]),
    (156, 165, "2d20*1000", ["Gold w/ Diamonds & Sapphires",
                             "Platinum w/ Diamonds & Sapphires"]),
    (166, 175, "1d4*10000", ["Gold encrusted w/ Flawless Facet-cut Diamonds"]),
    (176, 180, "1d8*10000", ["Platinum encrusted w/ Flawless Black Sapphires",
                             "Platinum encrusted w/ Flawless Blue Diamonds"]),
]


# ------------------------------------------------------------
# INTERNAL HELPERS WITH AUDIT
# ------------------------------------------------------------

def _log(audit, msg):
    if audit is not None:
        audit.append(msg)


def _resolve_formula(expr: str, audit=None) -> int:
    """Parse formulas like '2d4*1000' or '3d6*100', with audit logging."""
    if "*" in expr:
        dice, mult = expr.split("*")
        rolled = roll(dice, audit=audit, note=f"{expr} dice")
        total = rolled * int(mult)
        _log(audit, f" → {expr}: {rolled} * {mult} = {total}")
        return total
    else:
        total = roll(expr, audit=audit, note=f"{expr} dice")
        return total


def _lookup_jewelry(table, roll_value, audit=None):
    for low, high, formula, types in table:
        if low <= roll_value <= high:
            _log(audit, f" → Table match: {low}-{high}, formula={formula}")

            value = _resolve_formula(formula, audit=audit)
            jtype = random.choice(types)
            _log(audit, f" → Selected type: {jtype}")

            return value, jtype

    raise RuntimeError(f"Jewelry table roll failed for roll={roll_value}")


# ------------------------------------------------------------
# PUBLIC GENERATORS (WITH AUDIT)
# ------------------------------------------------------------

def generate_trinket(audit=None):
    """Equivalent to Trinket (2d20 gp avg). Uses TRINKET_TABLE (1–100)."""
    roll_value = random.randint(1, 100)
    _log(audit, f"Trinket roll: {roll_value}")

    value, jtype = _lookup_jewelry(TRINKET_TABLE, roll_value, audit=audit)

    _log(audit, f" → Trinket: {jtype} ({value} gp)")

    return {
        "category": "trinkets",
        "value_gp": value,
        "type": jtype,
    }


def generate_jewelry(audit=None):
    """Standard Jewelry: d100 (1–100) or extended (101–180)."""
    roll_value = random.randint(1, 180)
    _log(audit, f"Jewelry roll: {roll_value}")

    if roll_value <= 100:
        value, jtype = _lookup_jewelry(TRINKET_TABLE, roll_value, audit=audit)
    else:
        value, jtype = _lookup_jewelry(JEWELRY_TABLE, roll_value, audit=audit)

    _log(audit, f" → Jewelry: {jtype} ({value} gp)")

    return {
        "category": "jewelry",
        "value_gp": value,
        "type": jtype,
    }


def generate_regalia(audit=None):
    """Regalia = d100+80 → 81–180."""
    roll_value = random.randint(81, 180)
    _log(audit, f"Regalia roll: {roll_value}")

    if roll_value <= 100:
        value, jtype = _lookup_jewelry(TRINKET_TABLE, roll_value, audit=audit)
    else:
        value, jtype = _lookup_jewelry(JEWELRY_TABLE, roll_value, audit=audit)

    _log(audit, f" → Regalia: {jtype} ({value} gp)")

    return {
        "category": "regalia",
        "value_gp": value,
        "type": jtype,
    }
