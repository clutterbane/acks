import random
import item_generator
from item_generator import generate_magic_by_category, _finalize_item_subtype
from treasure.roller import roll, chance
from treasure.gems import generate_ornamental, generate_gem, generate_brilliant
from treasure.jewelry import generate_trinket, generate_jewelry, generate_regalia
from treasure.special.special_treasure import (
    special_from_cp, special_from_sp, special_from_ep,
    special_from_gp, special_from_pp,
    special_from_ornamental, special_from_gem,
    special_from_brilliant, special_from_trinket,
    special_from_jewelry, special_from_regalia
)
from treasure.utils import coin_gp_value, coin_weight_st


# ============================================================
# SPECIAL MAPS
# ============================================================

SPECIAL_MAP_COINS = {
    "copper":   special_from_cp,
    "silver":   special_from_sp,
    "electrum": special_from_ep,
    "gold":     special_from_gp,
    "platinum": special_from_pp,
}

SPECIAL_MAP_GEMLIKE = {
    "ornamentals": special_from_ornamental,
    "gems":        special_from_gem,
    "brilliants":  special_from_brilliant,
    "trinkets":    special_from_trinket,
    "jewelry":     special_from_jewelry,
    "regalia":     special_from_regalia,
}

# ============================================================
# HELPERS WITH AUDIT SUPPORT
# ============================================================

def _roll_with_audit(expr, audit, label=""):
    value = roll(expr, audit=audit, note=label)
    return value


def _chance_with_audit(pct, audit, label=""):
    return chance(pct, audit=audit, note=label)

def apply_special_to_gemlike(items, audit, special_chance):
    out = []
    for item in items:
        cat = item.get("category")
        name = item.get("type", item.get("name"))
        func = SPECIAL_MAP_GEMLIKE.get(cat)

        audit(f"Gem/Jewelry '{name}' category={cat}")

        if func is None:
            audit(" → No special conversion available, keeping original.")
            out.append(item)
            continue

        if "name" not in item:
            item["name"] = item.get("type", "Unknown")

        # UI chance
        if not chance(special_chance):
            audit(f" → Not converted (rolled under {special_chance}%)")
            out.append(item)
            continue

        audit(f" → Converting using {func.__name__}")

        converted_list = func(item)

        for c in converted_list:
            # SAFE NAME EXTRACTION
            name = c.get("name") if isinstance(c, dict) else str(c)
            audit(f"     Added special gem/jewelry cargo: {name}")

        out.extend(converted_list)

    return out

def apply_special_to_coins(coins_dict, audit, special_pct):
    out = []
    for coin, amount in coins_dict.items():
        thousands = amount // 1000
        if thousands == 0:
            continue

        audit(f"Coin type '{coin}' has {amount} → {thousands} × 1000-packs")
        func = SPECIAL_MAP_COINS[coin]

        for i in range(thousands):
            if _chance_with_audit(special_pct, audit,
                                  f"Convert {coin} pack #{i+1} ({special_pct}%)?"):
                audit(f" → Converting using {func.__name__}")
                converted = func()
                for c in converted:
                    audit(f"     Added special coin cargo: {c.get('name')}")
                out.extend(converted)
            else:
                gp = coin_gp_value(coin, 1000)
                st = 1
                audit(f" → Keeping as basic coin cargo: {coin} x1000")
                out.append({
                    "name": f"{coin.title()} pieces",
                    "coin_type": coin,
                    "coins": 1000,
                    "value_gp": gp,
                    "stone": st,
                })

    return out

CLASSIC_TREASURE = {

    # --------------------------------------------------
    # A — Incidental (275gp)
    # --------------------------------------------------
    "A": {
        "copper":   {"chance": 0,  "dice": None},
        "silver":   {"chance": 30, "dice": "1d4"},
        "electrum": {"chance": 0,  "dice": None},
        "gold":     {"chance": 0,  "dice": None},
        "platinum": {"chance": 0,  "dice": None},
        "gems":     {"chance": 30, "dice": "1d4", "category": "ornamentals"},
        "jewelry":  {"chance": 30, "dice": "1d4", "category": "trinkets"},
        "magic":    {"chance": 1,  "qty": 1, "table": "any"},
    },

    # --------------------------------------------------
    # B — Hoarder (500gp)
    # --------------------------------------------------
    "B": {
        "copper":   {"chance": 0,  "dice": None},
        "silver":   {"chance": 80, "dice": "1d6"},
        "electrum": {"chance": 0,  "dice": None},
        "gold":     {"chance": 0,  "dice": None},
        "platinum": {"chance": 0,  "dice": None},
        "gems":     {"chance": 70, "dice": "1d4", "category": "ornamentals"},
        "jewelry":  {"chance": 30, "dice": "1d4", "category": "trinkets"},
        "magic":    {"chance": 5,  "qty": 2, "table": "any"},
    },

    # --------------------------------------------------
    # C — Incidental (700gp)
    # --------------------------------------------------
    "C": {
        "copper":   {"chance": 0,  "dice": None},
        "silver":   {"chance": 0,  "dice": None},
        "electrum": {"chance": 15, "dice": "1d4"},
        "gold":     {"chance": 0,  "dice": None},
        "platinum": {"chance": 0,  "dice": None},
        "gems":     {"chance": 40, "dice": "1d6", "category": "gems"},
        "jewelry":  {"chance": 30, "dice": "1d6", "category": "trinkets"},
        "magic":    {"chance": 5,  "qty": 1, "table": "any"},
    },

    # --------------------------------------------------
    # D — Hoarder (1000gp)
    # --------------------------------------------------
    "D": {
        "copper":   {"chance": 0,  "dice": None},
        "silver":   {"chance": 80, "dice": "1d6"},
        "electrum": {"chance": 20, "dice": "1d4"},
        "gold":     {"chance": 0,  "dice": None},
        "platinum": {"chance": 0,  "dice": None},
        "gems":     {"chance": 80, "dice": "1d6", "category": "ornamentals"},
        "jewelry":  {"chance": 70, "dice": "1d4", "category": "trinkets"},
        "magic":    {"chance": 15,  "qty": 2, "table": "any"},
    },

    # --------------------------------------------------
    # E — Raider (1250gp)
    # --------------------------------------------------
    "E": {
        "copper":   {"chance": 80, "dice": "2d20"},
        "silver":   {"chance": 70, "dice": "3d6"},
        "electrum": {"chance": 0,  "dice": None},
        "gold":     {"chance": 0,  "dice": None},
        "platinum": {"chance": 0,  "dice": None},
        "gems":     {"chance": 60, "dice": "1d4", "category": "ornamentals"},
        "jewelry":  {"chance": 40, "dice": "1d4", "category": "trinkets"},
        "magic": {
            "weapon_armor": {"chance": 15, "qty": 1},
            "potion":       {"chance": 15, "qty": 1},
            "any":          {"chance": 5,  "qty": 1},
        }
    },

    # --------------------------------------------------
    # F — Incidental (1500gp)
    # --------------------------------------------------
    "F": {
        "copper":   {"chance": 0,  "dice": None},
        "silver":   {"chance": 30, "dice": "1d4"},
        "electrum": {"chance": 0,  "dice": None},
        "gold":     {"chance": 15, "dice": "1d4"},
        "platinum": {"chance": 0,  "dice": None},
        "gems":     {"chance": 40, "dice": "1d6", "category": "gems"},
        "jewelry":  {"chance": 30, "dice": "1d4", "category": "jewelry"},
        "magic":    {"chance": 7, "qty": 1, "table": "any"},
    },

    # --------------------------------------------------
    # G — Raider (2000gp)
    # --------------------------------------------------
    "G": {
        "copper":   {"chance": 70, "dice": "2d20"},
        "silver":   {"chance": 70, "dice": "3d6"},
        "electrum": {"chance": 50, "dice": "1d4"},
        "gold":     {"chance": 0,  "dice": None},
        "platinum": {"chance": 0,  "dice": None},
        "gems":     {"chance": 50, "dice": "1d6", "category": "ornamentals"},
        "jewelry":  {"chance": 50, "dice": "1d6", "category": "trinkets"},
        "magic": {
            "weapon_armor": {"chance": 25, "qty": 1},
            "potion":       {"chance": 25, "qty": 1},
            "any":          {"chance": 10, "qty": 1},
        }
    },

    # --------------------------------------------------
    # H — Hoarder (2500gp)
    # --------------------------------------------------
    "H": {
        "copper":   {"chance": 0,  "dice": None},
        "silver":   {"chance": 25, "dice": "1d6"},
        "electrum": {"chance": 70, "dice": "1d6"},
        "gold":     {"chance": 0,  "dice": None},
        "platinum": {"chance": 0,  "dice": None},
        "gems":     {"chance": 80, "dice": "1d6", "category": "gems"},
        "jewelry":  {"chance": 80, "dice": "1d6", "category": "trinkets"},
        "magic": {
            "any":     {"chance": 25, "qty": 3},
            "potion":  {"chance": 25, "qty": 1},
            "scroll":  {"chance": 25, "qty": 1},
        }
    },

    # --------------------------------------------------
    # I — Incidental (3250gp)
    # --------------------------------------------------
    "I": {
        "copper":   {"chance": 0,  "dice": None},
        "silver":   {"chance": 25, "dice": "1d4"},
        "electrum": {"chance": 0,  "dice": None},
        "gold":     {"chance": 25, "dice": "1d6"},
        "platinum": {"chance": 0,  "dice": None},
        "gems":     {"chance": 50, "dice": "2d4", "category": "gems"},
        "jewelry":  {"chance": 40, "dice": "1d8", "category": "jewelry"},
        "magic":    {"chance": 20, "qty": 1, "table": "any"},
    },

    # --------------------------------------------------
    # J — Raider (4000gp)
    # --------------------------------------------------
    "J": {
        "copper":   {"chance": 50, "dice": "3d6"},
        "silver":   {"chance": 70, "dice": "2d20"},
        "electrum": {"chance": 70, "dice": "1d8"},
        "gold":     {"chance": 0,  "dice": None},
        "platinum": {"chance": 0,  "dice": None},
        "gems":     {"chance": 50, "dice": "1d6", "category": "gems"},
        "jewelry":  {"chance": 50, "dice": "1d8", "category": "trinkets"},
        "magic": {
            "weapon_armor": {"chance": 50, "qty": 1},
            "potion":       {"chance": 45, "qty": 1},
            "any":          {"chance": 20, "qty": 1},
        }
    },

    # --------------------------------------------------
    # K — Incidental (5000gp)
    # --------------------------------------------------
    "K": {
        "copper":   {"chance": 0, "dice": None},
        "silver":   {"chance": 0, "dice": None},
        "electrum": {"chance": 30, "dice": "1d4"},
        "gold":     {"chance": 25, "dice": "1d6"},
        "platinum": {"chance": 0, "dice": None},
        "gems":     {"chance": 25, "dice": "1d4", "category": "brilliants"},
        "jewelry":  {"chance": 50, "dice": "1d4", "category": "jewelry"},
        "magic":    {"chance": 40, "qty": 1, "table": "any"},
    },

    # --------------------------------------------------
    # L — Raider (6000gp)
    # --------------------------------------------------
    "L": {
        "copper":   {"chance": 40, "dice": "3d6"},
        "silver":   {"chance": 60, "dice": "2d10"},
        "electrum": {"chance": 75, "dice": "3d6"},
        "gold":     {"chance": 0,  "dice": None},
        "platinum": {"chance": 0,  "dice": None},
        "gems":     {"chance": 60, "dice": "1d6", "category": "gems"},
        "jewelry":  {"chance": 40, "dice": "1d4", "category": "jewelry"},
        "magic": {
            "weapon_armor": {"chance": 75, "qty": 1},
            "potion":       {"chance": 75, "qty": 1},
            "any":          {"chance": 30, "qty": 1},
        }
    },

    # --------------------------------------------------
    # M — Incidental (8000gp)
    # --------------------------------------------------
    "M": {
        "copper":   {"chance": 0, "dice": None},
        "silver":   {"chance": 0, "dice": None},
        "electrum": {"chance": 25, "dice": "1d4"},
        "gold":     {"chance": 0, "dice": None},
        "platinum": {"chance": 15, "dice": "1d4"},
        "gems":     {"chance": 30, "dice": "1d6", "category": "brilliants"},
        "jewelry":  {"chance": 50, "dice": "1d6", "category": "jewelry"},
        "magic":    {"chance": 30, "qty": 2, "table": "any"},
    },

    # --------------------------------------------------
    # N — Hoarder (9000gp)
    # --------------------------------------------------
    "N": {
        "copper":   {"chance": 0, "dice": None},
        "silver":   {"chance": 60, "dice": "1d8"},
        "electrum": {"chance": 60, "dice": "2d4"},
        "gold":     {"chance": 80, "dice": "1d6"},
        "platinum": {"chance": 0,  "dice": None},
        "gems":     {"chance": 80, "dice": "1d8", "category": "gems"},
        "jewelry":  {"chance": 80, "dice": "1d8", "category": "jewelry"},
        "magic": {
            "any":    {"chance": 50, "qty": 4},
            "potion": {"chance": 50, "qty": 1},
            "scroll": {"chance": 50, "qty": 1},
        }
    },

    # --------------------------------------------------
    # O — Raider (12000gp)
    # --------------------------------------------------
    "O": {
        "copper":   {"chance": 30, "dice": "3d6"},
        "silver":   {"chance": 50, "dice": "3d6"},
        "electrum": {"chance": 60, "dice": "3d6"},
        "gold":     {"chance": 60, "dice": "2d6"},
        "platinum": {"chance": 0,  "dice": None},
        "gems":     {"chance": 30, "dice": "1d4", "category": "brilliants"},
        "jewelry":  {"chance": 60, "dice": "1d4", "category": "jewelry"},
        "magic": {
            "weapon_armor": {"chance": 75, "qty": 1},
            "potion":       {"chance": 75, "qty": 2},
            "any":          {"chance": 50, "qty": 2},
        }
    },

    # --------------------------------------------------
    # P — Incidental (17000gp)
    # --------------------------------------------------
    "P": {
        "copper":   {"chance": 0, "dice": None},
        "silver":   {"chance": 0, "dice": None},
        "electrum": {"chance": 0, "dice": None},
        "gold":     {"chance": 30, "dice": "1d4"},
        "platinum": {"chance": 30, "dice": "1d4"},
        "gems":     {"chance": 40, "dice": "1d4", "category": "brilliants"},
        "jewelry":  {"chance": 30, "dice": "1d4", "category": "regalia"},
        "magic":    {"chance": 40, "qty": 3, "table": "any"},
    },

    # --------------------------------------------------
    # Q — Hoarder (22000gp)
    # --------------------------------------------------
    "Q": {
        "copper":   {"chance": 0, "dice": None},
        "silver":   {"chance": 0, "dice": None},
        "electrum": {"chance": 50, "dice": "1d8"},
        "gold":     {"chance": 80, "dice": "2d6"},
        "platinum": {"chance": 40, "dice": "1d4"},
        "gems":     {"chance": 60, "dice": "1d6", "category": "brilliants"},
        "jewelry":  {"chance": 80, "dice": "1d4", "category": "jewelry"},
        "magic": {
            "potion": {"qty": "1d4"},   # ALWAYS
            "scroll": {"qty": "1d4"},   # ALWAYS
            "any":    {"chance": 50, "qty": 6},
        }
    },

    # --------------------------------------------------
    # R — Hoarder (45000gp)
    # --------------------------------------------------
    "R": {
        "copper":   {"chance": 0, "dice": None},
        "silver":   {"chance": 0, "dice": None},
        "electrum": {"chance": 50, "dice": "1d6"},
        "gold":     {"chance": 60, "dice": "1d6"},
        "platinum": {"chance": 80, "dice": "1d8"},
        "gems":     {"chance": 70, "dice": "1d4", "category": "brilliants"},
        "jewelry":  {"chance": 60, "dice": "1d4", "category": "regalia"},
        "magic": {
            "potion": {"qty": "2d4"},
            "scroll": {"qty": "2d4"},
            "broad": {
                "chance": 75,
                "qty": "1d3",
                "categories": [
                    "swords",
                    "armor",
                    "misc_weapons",
                    "implements",
                    "misc_items",
                    "rings"
                ]
            }
        }
    },
}


BROAD_MAP = {
    "swords": "sword",
    "armor": "armor",
    "misc_weapons": "misc_weapon",
    "implements": "implement",
    "misc_items": "misc_item",
    "rings": "ring",
}

WEAPON_ARMOR_TABLE = ["sword", "misc_weapon", "armor"]

ANY_TABLE = [
    "sword",
    "misc_weapon",
    "armor",
    "potion",
    "scroll",
    "implement",
    "misc_item",
    "ring",
]


# ============================================================
#  HELPERS
# ============================================================

def _gen_magic_item(category: str, campaign_style: str, audit):
    audit(f"Generating magic item in category '{category}'")
    item = generate_magic_by_category(category, campaign_style)
    item = _finalize_item_subtype(item, campaign_style)
    audit(f" → Magic item: {item.get('name')}")
    return item


def _maybe_roll_coins(entry, audit, coin_name):
    """Roll 1000 × dice if chance succeeds."""
    chance_pct = entry["chance"]
    dice_expr = entry["dice"]

    if chance_pct == 0 or dice_expr is None:
        return 0

    # chance
    if not _chance_with_audit(chance_pct, audit, f"Coins {coin_name}?"):
        return 0

    # roll dice
    qty_thousands = _roll_with_audit(dice_expr, audit, f"{coin_name} dice")

    total = qty_thousands * 1000
    audit(f" → Result: {total} {coin_name}")
    return total

def _generate_gem_by_category(cat, audit):
    audit(f"Generating gem in category '{cat}'")
    if cat == "ornamentals":
        g = generate_ornamental()
    elif cat == "gems":
        g = generate_gem()
    elif cat == "brilliants":
        g = generate_brilliant()
    else:
        raise ValueError(f"Unknown gem category: {cat}")

    audit(f" → Generated gem: {g.get('type')} ({g.get('value_gp')} gp)")
    return g


def _generate_jewelry_by_category(cat, audit):
    audit(f"Generating jewelry in category '{cat}'")
    if cat == "trinkets":
        j = generate_trinket()
    elif cat == "jewelry":
        j = generate_jewelry()
    elif cat == "regalia":
        j = generate_regalia()
    else:
        raise ValueError(f"Unknown jewelry category: {cat}")

    audit(f" → Generated jewelry: {j.get('type')} ({j.get('value_gp')} gp)")
    return j


# ============================================================
# MAIN GENERATOR
# ============================================================

def generate_classic_treasure(
        t_type: str,
        campaign_style: str = "ancient_myth",
        special_chance: int = 50,
):
    entry = CLASSIC_TREASURE[t_type]

    audit_log = []

    def audit(msg):
        audit_log.append(msg)

    audit(f"=== Generating Treasure Type {t_type} ===")

    result = {
        "coins": {},
        "gems": [],
        "jewelry": [],
        "magic_items": [],
        "special_coins": [],
        "special_gems": [],
        "special_jewelry": [],
        "audit": audit_log,
    }

    # ---------------------------------------
    # COINS
    # ---------------------------------------

    for coin in ["copper", "silver", "electrum", "gold", "platinum"]:
        e = entry[coin]
        if e["chance"] == 0:
            result["coins"][coin] = 0
            continue

        qty = _maybe_roll_coins(e, audit, coin)
        result["coins"][coin] = qty

    # ---------------------------------------
    # GEMS
    # ---------------------------------------
    if "gems" in entry:
        if _chance_with_audit(entry["gems"]["chance"], audit, "Gems?"):
            n = _roll_with_audit(entry["gems"]["dice"], audit, "Gem count")
            cat = entry["gems"]["category"]
            for _ in range(n):
                result["gems"].append(_generate_gem_by_category(cat, audit))
        else:
            audit(" → No gems")

    # ---------------------------------------
    # JEWELRY
    # ---------------------------------------
    if "jewelry" in entry:
        if _chance_with_audit(entry["jewelry"]["chance"], audit, "Jewelry?"):
            n = _roll_with_audit(entry["jewelry"]["dice"], audit, "Jewelry count")
            cat = entry["jewelry"]["category"]
            for _ in range(n):
                result["jewelry"].append(_generate_jewelry_by_category(cat, audit))
        else:
            audit(" → No jewelry")

    # ---------------------------------------
    # MAGIC ITEMS
    # ---------------------------------------
    if "magic" in entry:
        audit("Rolling for magic items...")
        result["magic_items"] = _generate_magic_items_from_entry(entry["magic"], campaign_style, audit)

    # ---------------------------------------
    # SPECIAL CONVERSIONS
    # ---------------------------------------
    audit("Applying special coin conversions...")
    result["special_coins"] = apply_special_to_coins(result["coins"], audit, special_chance)

    audit("Applying special gem conversions...")
    result["special_gems"] = apply_special_to_gemlike(result["gems"], audit, special_chance)

    audit("Applying special jewelry conversions...")
    result["special_jewelry"] = apply_special_to_gemlike(result["jewelry"], audit, special_chance)

    audit("=== Treasure Generation Completed ===")

    return result


# ============================================================
# MAGIC ITEM GENERATION (WITH AUDIT)
# ============================================================

def _generate_magic_items_from_entry(magic_entry: dict, campaign_style: str, audit):
    results = []

    # SIMPLE FORMAT
    if "chance" in magic_entry and "qty" in magic_entry:
        if _chance_with_audit(magic_entry["chance"], audit, "Magic items?"):
            qty = _roll_with_audit(magic_entry["qty"], audit, "Magic qty") if isinstance(magic_entry["qty"], str) else magic_entry["qty"]
            audit(f" → Generating {qty} magic items")
            table = magic_entry["table"]
            for _ in range(qty):
                category = random.choice(ANY_TABLE) if table == "any" else table
                audit(f" → Chose magic category: {category}")
                results.append(_gen_magic_item(category, campaign_style, audit))
        else:
            audit(" → No magic items")
        return results

    # COMPLEX FORMAT
    for key, spec in magic_entry.items():

        # weapon_armor
        if key == "weapon_armor":
            if _chance_with_audit(spec["chance"], audit, "weapon_armor?"):
                qty = _roll_with_audit(spec["qty"], audit, "weapon_armor qty")
                for _ in range(qty):
                    category = random.choice(WEAPON_ARMOR_TABLE)
                    audit(f" → Chose magic category: {category}")
                    results.append(_gen_magic_item(category, campaign_style, audit))
            continue

        # any
        if key == "any" and "chance" in spec:
            if _chance_with_audit(spec["chance"], audit, "any-table?"):
                qty = _roll_with_audit(spec["qty"], audit, "any qty")
                for _ in range(qty):
                    category = random.choice(ANY_TABLE)
                    audit(f" → Chose magic category: {category}")
                    results.append(_gen_magic_item(category, campaign_style, audit))
            continue

        # always potion/scroll
        if key in ("potion", "scroll") and "qty" in spec:
            qty = _roll_with_audit(spec["qty"], audit, f"{key} qty")
            for _ in range(qty):
                audit(f" → Chose magic category: {key}")
                results.append(_gen_magic_item(key, campaign_style, audit))
            continue

        # broad
        if key == "broad":
            if _chance_with_audit(spec["chance"], audit, "broad?"):
                qty = _roll_with_audit(spec["qty"], audit, "broad qty")
                for _ in range(qty):
                    raw = random.choice(spec["categories"])
                    category = BROAD_MAP[raw]
                    audit(f" → Chose magic category: {category}")
                    results.append(_gen_magic_item(category, campaign_style, audit))
            continue

        # default (chance + qty)
        if "chance" in spec and "qty" in spec:
            if _chance_with_audit(spec["chance"], audit, f"{key}?"):
                qty = _roll_with_audit(spec["qty"], audit, f"{key} qty")
                for _ in range(qty):
                    results.append(_gen_magic_item(key, campaign_style, audit))
            continue

    return results