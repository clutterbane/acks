# treasure/special/special_treasure.py
import random

from treasure.roller import roll, chance
from treasure.utils import coin_gp_value, coin_weight_st, coin_amount_from_gp

# ================================================================
# UTILITY
# ================================================================

def _log(audit, msg):
    if audit is not None:
        audit.append(msg)


def _make_item(name, value_gp, stone, coins=None, coin_type=None):
    """Uniform special treasure entry format."""
    return {
        "name": name,
        "value_gp": value_gp,
        "stone": stone,
        "coins": coins,
        "coin_type": coin_type,
    }


def _ensure_list(x):
    """Ensures the return value is always a list of dicts."""
    if x is None:
        return []
    if isinstance(x, list):
        return x
    if isinstance(x, dict):
        return [x]

    # If someone accidentally returned a string or other type, wrap safely:
    return [{
        "name": str(x),
        "value_gp": 0,
        "stone": 0
    }]


def _roll_list(count, builder):
    """Repeat builder(count) times — builder returns list or item."""
    results = []
    for _ in range(count):
        r = builder()
        r = _ensure_list(r)
        results.extend(r)
    return results


def _make_coin_item(coin_type: str, gp_value: float, label: str | None = None, audit=None):
    """Helper for any special treasure that turns into piles of coins."""
    amount = coin_amount_from_gp(coin_type, gp_value)
    stone = coin_weight_st(amount)
    name = label if label is not None else f"{coin_type.title()} pieces"
    _log(audit, f"Coin conversion: {gp_value} gp → {amount} {coin_type} (stone {stone})")

    return _make_item(
        name=name,
        value_gp=gp_value,
        stone=stone,
        coins=amount,
        coin_type=coin_type,
    )

# ================================================================
# SPECIAL TREASURE TABLES — COINS
# ================================================================

def special_from_cp(audit=None):
    r = roll("1d20", audit=audit, note="CP table roll")

    if r == 1:
        num = roll("2d20", audit=audit, note="Grain/vegetables qty")
        return [_make_item("Bag of grain/vegetables", 0.5, 4) for _ in range(num)]

    if r == 2:
        num = roll("4d6", audit=audit, note="Salt bricks qty") * 10
        return [_make_item("Brick of salt", 0.07, 0.5) for _ in range(num)]

    if r == 3:
        num = roll("2d10", audit=audit, note="Beer amphora qty")
        return [_make_item("Amphora of beer", 1, 7) for _ in range(num)]

    if r == 4:
        num = roll("6d6", audit=audit, note="Pottery crate qty")
        return [_make_item("Crate of pottery", 0.5, 3.5) for _ in range(num)]

    if r == 5:
        num = roll("2d10", audit=audit, note="Hardwood logs qty")
        return [_make_item("Bundle of hardwood logs", 1, 6) for _ in range(num)]

    if r == 6:
        num = roll("2d10", audit=audit, note="Wine amphora qty")
        return [_make_item("Amphora of wine/spirits", 1, 5) for _ in range(num)]

    if r == 7:
        num = roll("4d20", audit=audit, note="Cheese wheel qty")
        return [_make_item("Wheel of cheese", 0.25, 0.5) for _ in range(num)]

    if r == 8:
        num = roll("2d6", audit=audit, note="Oil amphora qty")
        return [_make_item("Amphora of oil/sauce", 1.5, 5) for _ in range(num)]

    if r == 9:
        num = roll("1d3", audit=audit, note="Preserved fish qty")
        return [_make_item("Amphora of preserved fish", 4.5, 10) for _ in range(num)]

    if r == 10:
        num = roll("1d3", audit=audit, note="Preserved meat qty")
        return [_make_item("Small amphora of preserved meat", 5, 5) for _ in range(num)]

    if r == 11:
        num = roll("1d2", audit=audit, note="Glassware crate qty")
        return [_make_item("Crate of glassware", 7.5, 5) for _ in range(num)]

    if r == 12:
        num = roll("3d6", audit=audit, note="Metal ingot qty")
        return [_make_item("Common metal ingot", 1, 0.5) for _ in range(num)]

    if r == 13:
        num = roll("2d4", audit=audit, note="Rare wood qty")
        return [_make_item("Bundle of rare wood", 2, 1) for _ in range(num)]

    if 14 <= r <= 19:
        return [_make_coin_item("copper", 10, label="Copper pieces", audit=audit)]

    if r == 20:
        return [_make_coin_item("silver", 100, label="Silver pieces", audit=audit)]

    return []


def special_from_sp(audit=None):
    r = roll("1d20", audit=audit, note="SP table roll")

    if r == 1:
        return [_make_coin_item("copper", 100, label="Copper pieces", audit=audit)]

    if r == 2:
        num = roll("2d6", audit=audit, note="Fur pelt qty")
        return [_make_item("Common fur pelt", 15, 3) for _ in range(num)]

    if r == 3:
        num = roll("1d6", audit=audit, note="Textile roll qty")
        return [_make_item("Roll of woven textiles", 30, 4) for _ in range(num)]

    if r == 4:
        num = roll("1d3", audit=audit, note="Dye jar qty")
        return [_make_item("Jar of dyes", 50, 5) for _ in range(num)]

    if r == 5:
        num = roll("1d2", audit=audit, note="Herb bag qty")
        return [_make_item("Bag of herbs", 75, 5) for _ in range(num)]

    if r == 6:
        num = roll("1d2", audit=audit, note="Clothing bag qty")
        return [_make_item("Bag of clothing", 75, 5) for _ in range(num)]

    if r == 7:
        num = roll("1d2", audit=audit, note="Tools crate qty")
        return [_make_item("Crate of tools", 75, 5) for _ in range(num)]

    if r == 8:
        return [_make_item("Crate of armor & weapons", 110, 5)]

    if r == 9:
        num = roll("4d8", audit=audit, note="Horn/tusk qty")
        return [_make_item("Animal horn/tusk", roll("1d10", audit=audit, note="Animal horn value"), 1) for _ in range(num)]

    if r == 10:
        num = roll("1d4", audit=audit, note="Enslaved laborer qty")
        return [_make_item("Enslaved laborer", 40, 15) for _ in range(num)]

    if r == 11:
        return [_make_item("Enslaved domestic servant", 100, 15)]

    if 12 <= r <= 19:
        return [_make_coin_item("silver", 100, label="Silver pieces", audit=audit)]

    if r == 20:
        return [_make_coin_item("gold", 100, label="Gold pieces", audit=audit)]

    return []


def special_from_ep(audit=None):
    r = roll("1d20", audit=audit, note="EP table roll")

    if r == 1:
        return [_make_coin_item("silver", 500, label="Silver pieces", audit=audit)]

    if r == 2:
        num = roll("2d100", audit=audit, note="Fine wine qty")
        return [_make_item("Fine wine bottle", 5, 0.2) for _ in range(num)]

    if r == 3:
        num = roll("3d12", audit=audit, note="Common fur rug qty")
        return [_make_item("Common fur rug", roll("2d4", audit=audit, note="Rug value") * 5, 1) for _ in range(num)]

    if r == 4:
        num = roll("2d4", audit=audit, note="Feather qty") * 500
        return [_make_item("Bird feather", 0.1, 1 / 150) for _ in range(num)]

    if r == 5:
        num = roll("3d4", audit=audit, note="Large pelt qty")
        return [_make_item("Large fur pelt", roll("1d8", audit=audit, note="Pelt value") * 15, 1) for _ in range(num)]

    if r == 6:
        num = roll("1d12", audit=audit, note="Uncommon tusk qty")
        return [_make_item("Uncommon tusk", roll("3d4", audit=audit, note="Tusk value") * 10, 1) for _ in range(num)]

    if r == 7:
        num = roll("1d4", audit=audit, note="Books qty")
        return [_make_item("Collection of books", roll("1d3", audit=audit, note="Book value") * 100, 1) for _ in range(num)]

    if r == 8:
        num = roll("1d3", audit=audit, note="Uncommon pelt qty")
        return [_make_item("Uncommon fur pelt", roll("2d4", audit=audit, note="Pelt value") * 50, 1) for _ in range(num)]

    if r == 9:
        num = roll("1d3", audit=audit, note="Captured craftsman qty")
        return [_make_item("Captured craftsman", roll("1d4", audit=audit, note="Craftsman value") * 100, 15) for _ in range(num)]

    if 10 <= r <= 19:
        return [_make_coin_item("electrum", 100, label="Electrum pieces", audit=audit)]

    if r == 20:
        return [_make_coin_item("gold", 500, label="Gold pieces", audit=audit)]

    return []


def special_from_gp(audit=None):
    r = roll("1d20", audit=audit, note="GP table roll")

    if r == 1:
        return [_make_coin_item("silver", 1000, label="Silver pieces", audit=audit)]

    if r == 2:
        return [_make_item("Metamphora of special components", roll("5d6", audit=audit, note="Component value") * 60, 1)]

    if r == 3:
        num = roll("1d6", audit=audit, note="Monster carcass qty")
        return [_make_item("Monster carcass", roll("1d10", audit=audit, note="Carcass value") * 50, 1) for _ in range(num)]

    if r == 4:
        num = roll("1d12", audit=audit, note="Feather qty") * 12
        return [_make_item("Monster feather", roll("3d6", audit=audit, note="Feather value"), 1 / 80) for _ in range(num)]

    if r == 5:
        num = roll("1d8", audit=audit, note="Horn qty")
        return [_make_item("Monster horn/tusk", roll("1d8", audit=audit, note="Horn value") * 50, 1 / 80) for _ in range(num)]

    if r == 6:
        num = roll("1d3", audit=audit, note="Rare pelt qty")
        return [_make_item("Rare fur pelt", roll("2d4", audit=audit, note="Pelt value") * 100, 1) for _ in range(num)]

    if r == 7:
        num = roll("2d20", audit=audit, note="Ivory qty")
        return [_make_item("Elephant ivory piece", roll("4d4", audit=audit, note="Ivory value") * 10, 1) for _ in range(num)]

    if r == 8:
        num = roll("1d3", audit=audit, note="Trophy qty")
        return [_make_item("Mounted trophy", roll("2d4", audit=audit, note="Trophy value") * 100, 1) for _ in range(num)]

    if r == 9:
        num = roll("4d4", audit=audit, note="Spice amphora qty")
        return [_make_item("Amphora of spices", 100, 1) for _ in range(num)]

    if r == 10:
        num = roll("1d3", audit=audit, note="Porcelain crate qty")
        return [_make_item("Crate of fine porcelain", 500, 5) for _ in range(num)]

    if r == 11:
        num = roll("4d10", audit=audit, note="Ingot qty")
        return [_make_item("Precious metal ingot", 50, 0.5) for _ in range(num)]

    if r == 12:
        num = roll("4d6", audit=audit, note="Fur rug qty")
        return [_make_item("Large fur rug", roll("1d4", audit=audit, note="Rug value") * 30, 1) for _ in range(num)]

    if r == 13:
        return [_make_item("Captured noble retainer", roll("2d4", audit=audit, note="Retainer value") * 200, 15)]

    if 14 <= r <= 19:
        return [_make_coin_item("gold", 1000, label="Gold pieces", audit=audit)]

    if r == 20:
        return [_make_coin_item("platinum", 200, label="Platinum pieces", audit=audit)]

    return []


def special_from_pp(audit=None):
    r = roll("1d20", audit=audit, note="PP table roll")

    if r == 1:
        return [_make_coin_item("gold", 5000, label="Gold pieces", audit=audit)]

    if r == 2:
        num = roll("4d6+1", audit=audit, note="Silk qty")
        return [_make_item("Roll of silk", 333, 1) for _ in range(num)]

    if r == 3:
        num = roll("6d10", audit=audit, note="Rare book qty")
        return [_make_item("Rare book", 150, 0.5) for _ in range(num // 2)]

    if r == 4:
        num = roll("5d10", audit=audit, note="Fur cape qty")
        return [_make_item("Common fur cape", roll("1d6", audit=audit, note="Cape value") * 50, 1) for _ in range(num)]

    if r == 5:
        num = roll("2d6+1", audit=audit, note="Rug qty")
        return [_make_item("Uncommon fur rug", roll("1d4", audit=audit, note="Rug value") * 250, 1) for _ in range(num)]

    if r == 6:
        num = roll("2d12", audit=audit, note="Rare horn qty")
        return [_make_item("Rare horn piece", roll("1d4", audit=audit, note="Horn value") * 150, 1) for _ in range(num)]

    if r == 7:
        num = roll("2d8", audit=audit, note="Fur coat qty")
        return [_make_item("Common fur coat", roll("1d6", audit=audit, note="Coat value") * 150, 1) for _ in range(num)]

    if r == 8:
        num = roll("4d4", audit=audit, note="Ivory qty")
        return [_make_item("Unicorn/Narwhal ivory", roll("2d4", audit=audit, note="Ivory value") * 100, 1) for _ in range(num)]

    if r == 9:
        return [_make_item("Captured squire/damsel", roll("2d4", audit=audit, note="Value") * 1000, 15)]

    if 10 <= r <= 20:
        return [_make_coin_item("platinum", 1000, label="Platinum pieces", audit=audit)]

    return []


def special_from_ornamental(original, audit=None):
    r = roll("1d12", audit=audit, note="Ornamental conversion")

    if r == 1:
        num = roll("1d12", audit=audit, note="Silver arrow qty")
        return [_make_item("Silver arrow", 5, 0.1) for _ in range(num)]

    if r == 2:
        num = roll("1d12", audit=audit, note="Lungwort qty")
        return [_make_item("Pouch of lungwort/willowbark", 5, 0.1) for _ in range(num)]

    if r == 3:
        num = roll("1d6", audit=audit, note="Healing herb qty")
        return [_make_item("Pouch of healing herbs", 10, 0.1) for _ in range(num)]

    if r == 4:
        num = roll("1d6", audit=audit, note="Dangerous herb qty")
        return [_make_item("Pouch of dangerous herbs", 10, 0.1) for _ in range(num)]

    if r == 5:
        num = roll("1d4", audit=audit, note="Horsetail qty")
        return [_make_item("Pouch of horsetail", 15, 0.1) for _ in range(num)]

    if r == 6:
        num = roll("1d2", audit=audit, note="Holy water qty")
        return [_make_item("Vial of holy water", 25, 0.1) for _ in range(num)]

    # fallback
    return [original]


def special_from_gem(original, audit=None):
    r = roll("1d10", audit=audit, note="Gem conversion")

    if r == 1:
        return [_make_item("Expanded thieves’ tools", 200, 0.1)]

    if r == 2:
        num = roll("1d4", audit=audit, note="Engraved teeth qty")
        return [_make_item("Engraved teeth", roll("2d6", audit=audit, note="Tooth value") * 10, 0.1) for _ in range(num)]

    if r == 3:
        num = roll("1d3", audit=audit, note="Perfume qty")
        return [_make_item("Rare perfume", roll("1d6", audit=audit, note="Perfume value") * 25, 0.1) for _ in range(num)]

    if r == 4:
        num = roll("2d10", audit=audit, note="Incense qty")
        return [_make_item("Stick of rare incense", roll("5d6", audit=audit, note="Incense value"), 0.01) for _ in range(num)]

    return [original]


def special_from_brilliant(original, audit=None):
    r = roll("1d8", audit=audit, note="Brilliant conversion")

    if r == 1:
        num = roll("2d20", audit=audit, note="Jade carving qty")
        return [_make_item("Jade carving", 200, 0.1) for _ in range(num)]

    if r == 2:
        num = roll("1d4", audit=audit, note="Superior tools qty")
        return [_make_item("Superior thieves’ tools", 1600, 0.1) for _ in range(num)]

    if r == 3:
        num = roll("2d4", audit=audit, note="Opal cameo qty")
        return [_make_item("Opal cameo portrait", 800, 0.1) for _ in range(num)]

    if r == 4:
        num = roll("1d6", audit=audit, note="Cylinder seal qty")
        return [_make_item("Amethyst cylinder seal", 1200, 0.1) for _ in range(num)]

    return [original]


def special_from_trinket(original, audit=None):
    r = roll("1d10", audit=audit, note="Trinket conversion")

    if r == 1:
        num = roll("3d6", audit=audit, note="Bone fetish qty")
        return [_make_item("Bone fetish", roll("2d20", audit=audit, note="Fetish value"), 0.1) for _ in range(num)]

    if r == 2:
        num = roll("2d6", audit=audit, note="Glass lens qty")
        return [_make_item("Glass eye/lens/prism", roll("1d6", audit=audit, note="Lens value") * 10, 0.1) for _ in range(num)]

    if r == 3:
        num = roll("1d4", audit=audit, note="Masterwork item qty")
        return [_make_item("Masterwork item", 70 + roll("5d6", audit=audit, note="Masterwork roll"), 0.1) for _ in range(num)]

    if r == 4:
        num = roll("1d4", audit=audit, note="Holy symbol qty")
        return [_make_item("Silver holy symbol", roll("2d8", audit=audit, note="Symbol value") * 10, 0.1) for _ in range(num)]

    return [original]


def special_from_jewelry(original, audit=None):
    r = roll("1d10", audit=audit, note="Jewelry conversion")

    if r == 1:
        num = roll("1d8", audit=audit, note="Trinket qty")
        return [_make_item("Trinket", 225, 0.1) for _ in range(num)]

    if r == 2:
        return [_make_item("Cape of animal fur", roll("2d4", audit=audit, note="Cape value") * 200, 1)]

    if r == 3:
        num = roll("1d10", audit=audit, note="Poison vial qty")
        return [_make_item("Common poison vial", roll("2d6", audit=audit, note="Poison value") * 25, 0.1) for _ in range(num)]

    if r == 4:
        num = roll("1d3", audit=audit, note="Statuette qty")
        return [_make_item("Statuette", roll("1d10", audit=audit, note="Statuette value") * 100, 1) for _ in range(num)]

    if r == 5:
        num = roll("1d2", audit=audit, note="Masterwork jewelry qty")
        return [_make_item("Masterwork jewelry", roll("2d6", audit=audit, note="Jewelry value") * 100, 0.1) for _ in range(num)]

    return [original]


def special_from_regalia(original, audit=None):
    r = roll("1d12", audit=audit, note="Regalia conversion")

    if r == 1:
        num = roll("4d8", audit=audit, note="Jewelry piece qty")
        return [_make_item("Jewelry piece", 1000, 0.1) for _ in range(num)]

    if r == 2:
        num = roll("1d6", audit=audit, note="Rare fur cape qty")
        return [_make_item("Rare fur cape", roll("1d6", audit=audit, note="Cape value") * 1000, 1) for _ in range(num)]

    if r == 3:
        num = roll("1d4", audit=audit, note="Large coat qty")
        return [_make_item("Large animal coat", (roll("1d6", audit=audit, note="Coat value") + 1) * 1000, 1) for _ in range(num)]

    if r == 4:
        num = roll("2d10", audit=audit, note="Rare poison qty")
        return [_make_item("Rare poison vial", roll("4d4", audit=audit, note="Poison value") * 100, 0.1) for _ in range(num)]

    if r == 5:
        num = roll("2d10", audit=audit, note="Game piece qty")
        return [_make_item("Game piece", roll("3d6", audit=audit, note="Game value") * 100, 0.1) for _ in range(num)]

    if r == 6:
        return [_make_item("Rare fur coat", roll("2d10", audit=audit, note="Coat value") * 1000, 1)]

    if r == 7:
        num = roll("1d8", audit=audit, note="Ivory figurine qty")
        return [_make_item("Ivory figurine", roll("1d4", audit=audit, note="Figurine value") * 1000, 0.1) for _ in range(num)]

    if r == 8:
        num = roll("1d4", audit=audit, note="Reliquary qty")
        return [_make_item("Platinum reliquary", roll("1d8", audit=audit, note="Reliquary value") * 1000, 0.1) for _ in range(num)]

    return [original]