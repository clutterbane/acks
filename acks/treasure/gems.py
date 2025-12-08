import random

# ------------------------------------------------------------
# GEM TABLES – based on ACKS Gem Tables
# ------------------------------------------------------------

ORNAMENTAL_TYPES = [
    (1, 10, 10, ["Azurite", "Hematite", "Malachite", "Obsidian", "Quartz"]),
    (11, 25, 25, ["Agate", "Lapis Lazuli", "Tiger Eye", "Turquoise"]),
    (26, 40, 50, ["Bloodstone", "Crystal", "Citrine", "Jasper", "Moonstone", "Onyx"]),
    (41, 55, 75, ["Carnelian", "Chalcedony", "Sardonyx", "Zircon"]),
    (56, 70, 100, ["Amber", "Amethyst", "Coral", "Jade", "Jet", "Tourmaline"]),
    (71, 80, 250, ["Garnet", "Pearl", "Spinel"]),
    (81, 90, 500, ["Aquamarine", "Alexandrite", "Topaz"]),
    (91, 95, 750, ["Opal", "Star Ruby", "Star Sapphire", "Sunset Amethyst", "Imperial Topaz"]),
    (96, 100, 1000, ["Black Sapphire", "Diamond", "Emerald", "Jacinth", "Ruby"]),
]

HIGH_VALUE_GEMS = [
    (101, 110, 1500, ["Amber with Preserved Creature", "Whorled Nephrite Jade"]),
    (111, 125, 2000, ["Black Pearl", "Baroque Pearl", "Crystal Geode"]),
    (126, 145, 4000, ["Facet-cut Imperial Topaz", "Flawless Diamond"]),
    (146, 165, 6000, ["Facet-cut Star Sapphire", "Facet-cut Star Ruby"]),
    (166, 175, 8000, ["Flawless Diamond", "Flawless Emerald", "Flawless Jacinth", "Flawless Ruby"]),
    (176, 180, 10000, ["Flawless Black Sapphire", "Flawless Blue Diamond"]),
]


# ------------------------------------------------------------
# HELPERS
# ------------------------------------------------------------

def _log(audit, msg):
    if audit is not None:
        audit.append(msg)

def _roll_on_weighted_table(table, roll, audit=None):
    """
    Given a combined table (tuple ranges) and a roll, choose value/type.
    """
    for low, high, gp, types in table:
        if low <= roll <= high:
            t = random.choice(types)
            _log(audit, f" → Result: {gp} gp {t}")
            return gp, t

    raise RuntimeError(f"Gem table roll failed for roll={roll}")


# ------------------------------------------------------------
# GENERATORS (WITH AUDIT)
# ------------------------------------------------------------

def generate_ornamental(audit=None):
    """
    Ornamental = 1–100 roll, value per table
    """
    r = random.randint(1, 100)
    _log(audit, f"Ornamental gem roll: {r}")

    gp, gtype = _roll_on_weighted_table(ORNAMENTAL_TYPES, r, audit)

    gem = {
        "category": "ornamentals",
        "value_gp": gp,
        "type": gtype,
    }

    _log(audit, f" → Ornamental gem: {gtype} ({gp} gp)")
    return gem


def generate_gem(audit=None):
    """
    Standard Gem (1–180)
    """
    r = random.randint(1, 180)
    _log(audit, f"Gem roll: {r}")

    if r <= 100:
        gp, gtype = _roll_on_weighted_table(ORNAMENTAL_TYPES, r, audit)
    else:
        gp, gtype = _roll_on_weighted_table(HIGH_VALUE_GEMS, r, audit)

    gem = {
        "category": "gems",
        "value_gp": gp,
        "type": gtype,
    }

    _log(audit, f" → Gem: {gtype} ({gp} gp)")
    return gem


def generate_brilliant(audit=None):
    """
    Brilliant = always from HIGH_VALUE_GEMS range (101–180)
    """
    r = random.randint(101, 180)
    _log(audit, f"Brilliant roll: {r}")

    gp, gtype = _roll_on_weighted_table(HIGH_VALUE_GEMS, r, audit)

    gem = {
        "category": "brilliants",
        "value_gp": gp,
        "type": gtype,
    }

    _log(audit, f" → Brilliant: {gtype} ({gp} gp)")
    return gem
