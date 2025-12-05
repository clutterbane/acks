import random
import re
from magic_items import (
    choose_from_table,
    get_creature_type,

    COMMON_POTIONS_1, COMMON_POTIONS_2, COMMON_POTIONS_3,
    COMMON_SCROLLS, COMMON_MISC_ITEMS,

    UNCOMMON_POTIONS_1, UNCOMMON_POTIONS_2, UNCOMMON_POTIONS_3,
    UNCOMMON_RINGS, UNCOMMON_SCROLLS, UNCOMMON_MISC_ITEMS,

    UNCOMMON_SWORDS, UNCOMMON_MISC_WEAPONS, UNCOMMON_ARMOR,

    # RARE
    RARE_RINGS_1, RARE_RINGS_2,
    RARE_SCROLLS,
    RARE_IMPLEMENT_1, RARE_IMPLEMENT_2,
    RARE_MISC_ITEMS_1, RARE_MISC_ITEMS_2, RARE_MISC_ITEMS_3,
    RARE_MISC_ITEMS_4, RARE_MISC_ITEMS_5,
    RARE_SWORDS, RARE_MISC_WEAPONS, RARE_ARMOR,

    # VERY RARE
    VERY_RARE_POTIONS,
    VERY_RARE_RINGS,
    VERY_RARE_SCROLLS,
    VERY_RARE_IMPLEMENT_1, VERY_RARE_IMPLEMENT_2, VERY_RARE_IMPLEMENT_3,
    VERY_RARE_MISC_ITEMS_1, VERY_RARE_MISC_ITEMS_2,
    VERY_RARE_SWORDS, VERY_RARE_MISC_WEAPONS, VERY_RARE_ARMOR,

    # LEGENDARY
    LEGENDARY_RINGS,
    LEGENDARY_SCROLLS,
    LEGENDARY_IMPLEMENT,
    LEGENDARY_MISC_ITEMS,
    LEGENDARY_SWORDS,
    LEGENDARY_MISC_WEAPONS,
    LEGENDARY_ARMOR,

    CREATURE_TYPES,
    MISC_WEAPON_TYPES,
    ARMOR_TYPES,
    AMMO_TYPES,
    AXE_TYPES,
    BLUDGEON_TYPES,
    BOW_TYPES,
    SPEAR_TYPES,
    SWORD_TYPES,
    OTHER_WEAPON_TYPES,


)


# =====================================================================
# KONFIGURACJE TRYBÓW GENEROWANIA
# =====================================================================

GENERATION_MODES = ["classic", "heroic", "gritty"]

# Heroic i Gritty są identyczne → trzymamy je w jednym branchu
MODES_WITH_RARITY = ["heroic", "gritty"]

# =====================================================================
# GŁÓWNA FUNKCJA GENERUJĄCA
# =====================================================================

def generate_item(mode: str, campaign_style: str, rarity: str | None = None):
    """
    Główna funkcja API do generowania przedmiotu.

    Parametry:
    - mode: 'classic', 'heroic', lub 'gritty'
    - campaign_style: np. 'ancient_myth'
    - rarity: None dla Classic; dla Heroic/Gritty wymagane (np. 'common', 'uncommon', 'rare', 'very_rare', 'legendary')

    Zwraca strukturę:
    {
        "mode": ...,
        "style": ...,
        "rarity": ...,
        "item": {
            "name": ...,
            "details": ...
        }
    }
    """

    mode = mode.lower()
    if mode not in GENERATION_MODES:
        raise ValueError(f"Unknown mode '{mode}'. Must be one of: {GENERATION_MODES}")

    # -----------------------------
    # CLASSIC → Rzadkość ignorowana
    # -----------------------------
    if mode == "classic":
        if rarity is not None:
            print("Warning: Classic mode ignores rarity parameter.")
        item = generate_item_classic(campaign_style)
        return {
            "mode": mode,
            "style": campaign_style,
            "rarity": None,
            "item": item,
        }

    # -----------------------------
    # HEROIC / GRITTY → Wymaga rzadkości
    # -----------------------------
    if mode in MODES_WITH_RARITY:
        if rarity is None:
            raise ValueError("Heroic and Gritty modes require explicit rarity selection.")

        rarity = rarity.lower()
        allowed = ["common", "uncommon", "rare", "very_rare", "legendary"]
        if rarity not in allowed:
            raise ValueError(f"Invalid rarity '{rarity}'. Must be one of: {allowed}")

        item = generate_item_with_rarity(campaign_style, rarity)
        return {
            "mode": mode,
            "style": campaign_style,
            "rarity": rarity,
            "item": item,
        }

    raise RuntimeError("Internal error: mode not resolved.")


# =====================================================================
# GENERATORY DLA TRYBÓW
# =====================================================================

def generate_item_classic(style: str):
    roll = random.randint(1, 100)

    if 1 <= roll <= 20:
        item = _classic_potions(style)
    elif 21 <= roll <= 25:
        item = _classic_rings(style)
    elif 26 <= roll <= 56:
        item = _classic_scrolls(style)
    elif 57 <= roll <= 61:
        item = _classic_implements(style)
    elif 62 <= roll <= 66:
        item = _classic_misc_items(style)
    elif 67 <= roll <= 87:
        item = _classic_swords(style)
    elif 88 <= roll <= 92:
        item = _classic_misc_weapons(style)
    elif 93 <= roll <= 100:
        item = _classic_armors(style)
    else:
        raise RuntimeError("Random Magic Item Type roll out of range.")

    return _finalize_item_subtype(item, style)


def generate_item_with_rarity(campaign_style: str, rarity: str):
    """
    Heroic / Gritty mode: rarity is chosen by user.
    """

    if rarity == "common":
        item = generate_common_item(campaign_style)
    elif rarity == "uncommon":
        item = generate_uncommon_item(campaign_style)
    elif rarity == "rare":
        item = generate_rare_item(campaign_style)
    elif rarity == "very_rare":
        item = generate_very_rare_item(campaign_style)
    elif rarity == "legendary":
        item = generate_legendary_item(campaign_style)
    else:
        raise RuntimeError("Unknown rarity during generation.")

    # ← TU poprawiamy generiki typu Weapon, Sword, Armor
    return _finalize_item_subtype(item, campaign_style)



# =====================================================================
# HEROIC / GRITTY GENERATION TABLES
# =====================================================================

# ------------------------------
# COMMON
# ------------------------------

def generate_common_item(style: str):
    """
    Common rarity dla trybów Heroic / Gritty.
    """
    roll = random.randint(1, 100)

    if 1 <= roll <= 15:
        return roll_common_potions_1(style)
    elif 16 <= roll <= 30:
        return roll_common_potions_2(style)
    elif 31 <= roll <= 45:
        return roll_common_potions_3(style)
    elif 46 <= roll <= 90:
        return roll_common_scrolls(style)
    elif 91 <= roll <= 100:
        return roll_common_misc_items(style)

    raise RuntimeError("Common item roll out of range.")

# ------------------------------
# UNCOMMON
# ------------------------------

def generate_uncommon_item(style: str):
    roll = random.randint(1, 100)

    if 1 <= roll <= 16:
        return roll_uncommon_potions_1(style)
    elif 17 <= roll <= 32:
        return roll_uncommon_potions_2(style)
    elif 33 <= roll <= 48:
        return roll_uncommon_potions_3(style)
    elif 49 <= roll <= 51:
        return roll_uncommon_rings(style)
    elif 52 <= roll <= 76:
        return roll_uncommon_scrolls(style)
    elif 77 <= roll <= 82:
        return roll_uncommon_misc_items(style)
    elif 83 <= roll <= 88:
        return roll_uncommon_swords(style)
    elif 89 <= roll <= 94:
        return roll_uncommon_misc_weapons(style)
    elif 95 <= roll <= 100:
        return roll_uncommon_armors(style)

    raise RuntimeError("Uncommon item roll out of range.")

# ------------------------------
# RARE
# ------------------------------

def generate_rare_item(style: str):
    roll = random.randint(1, 100)

    if 1 <= roll <= 3:
        return roll_rare_rings_1(style)
    elif 4 <= roll <= 6:
        return roll_rare_rings_2(style)
    elif 7 <= roll <= 25:
        return roll_rare_scrolls(style)
    elif 26 <= roll <= 29:
        return roll_rare_implements_1(style)
    elif 30 <= roll <= 33:
        return roll_rare_implements_2(style)
    elif 34 <= roll <= 38:
        return roll_rare_misc_items_1(style)
    elif 39 <= roll <= 43:
        return roll_rare_misc_items_2(style)
    elif 44 <= roll <= 48:
        return roll_rare_misc_items_3(style)
    elif 49 <= roll <= 53:
        return roll_rare_misc_items_4(style)
    elif 54 <= roll <= 58:
        return roll_rare_misc_items_5(style)
    elif 59 <= roll <= 72:
        return roll_rare_swords(style)
    elif 73 <= roll <= 86:
        return roll_rare_misc_weapons(style)
    elif 87 <= roll <= 100:
        return roll_rare_armors(style)

    raise RuntimeError("Rare item roll out of range.")


# ------------------------------
# VERY RARE
# ------------------------------

def generate_very_rare_item(style: str):
    roll = random.randint(1, 100)

    if roll == 1:
        return roll_very_rare_potions(style)
    elif 2 <= roll <= 14:
        return roll_very_rare_rings(style)
    elif 15 <= roll <= 24:
        return roll_very_rare_scrolls(style)
    elif 25 <= roll <= 29:
        return roll_very_rare_implements_1(style)
    elif 30 <= roll <= 34:
        return roll_very_rare_implements_2(style)
    elif 35 <= roll <= 39:
        return roll_very_rare_implements_3(style)
    elif 40 <= roll <= 59:
        return roll_very_rare_misc_items_1(style)
    elif 60 <= roll <= 79:
        return roll_very_rare_misc_items_2(style)
    elif 80 <= roll <= 86:
        return roll_very_rare_swords(style)
    elif 87 <= roll <= 93:
        return roll_very_rare_misc_weapons(style)
    elif 94 <= roll <= 100:
        return roll_very_rare_armors(style)

    raise RuntimeError("Very Rare item roll out of range.")


# ------------------------------
# LEGENDARY
# ------------------------------

def generate_legendary_item(style: str):
    roll = random.randint(1, 100)

    if 1 <= roll <= 7:
        return roll_legendary_rings(style)
    elif 8 <= roll <= 33:
        return roll_legendary_scrolls(style)
    elif 34 <= roll <= 51:
        return roll_legendary_implements(style)
    elif 52 <= roll <= 85:
        return roll_legendary_misc_items(style)
    elif 86 <= roll <= 90:
        return roll_legendary_swords(style)
    elif 91 <= roll <= 95:
        return roll_legendary_misc_weapons(style)
    elif 96 <= roll <= 100:
        return roll_legendary_armors(style)

    raise RuntimeError("Legendary item roll out of range.")

# =====================================================================
# OGÓLNE HELPERY DO BUDOWANIA PRZEDMIOTÓW
# =====================================================================

def _normalize_entry(entry):
    """
    Przyjmuje wpis z tabeli:
    - dict z kluczami "name", "cues", ew. dodatkowymi polami
    - albo zwykły string

    Zwraca: (name, cues, extra_dict)
    """
    if isinstance(entry, dict):
        name = entry.get("name", "")
        cues = entry.get("cues")
        extra = {k: v for k, v in entry.items() if k not in ("name", "cues")}
    else:
        name = str(entry)
        cues = None
        extra = {}
    return name, cues, extra


def _make_item(name, category, rarity, style, subtype=None, cues=None, extra=None):
    """
    Standardowy format zwracanego przedmiotu.
    """
    return {
        "name": name,
        "category": category,      # np. "potion", "scroll", "ring", "weapon", "armor", "wondrous"
        "rarity": rarity,          # "common", "uncommon", "rare", "very_rare", "legendary"
        "style": style,            # np. "ancient_myth"
        "subtype": subtype,        # np. "Short Sword", "Leather Armor", "Bow, Long"
        "cues": cues,              # opis sensoryczny (oleje, mikstury itd.)
        "extra": extra or {},      # np. {"versus": ["Undead"], "bonus_vs": "+2"}
    }


# =====================================================================
# HELPERY DO PARSOWANIA NAZW BRONI / PANCERZY / "VERSUS X"
# =====================================================================

_VERSUS_X_RE = re.compile(
    r"^(?P<prefix>.*?),\s*\+(?P<bonus_vs>\d+)\s+versus X\s*$"
)

def _extract_versus_x(name):
    """
    Jeśli nazwa ma format '... , +2 versus X' → wycina tę część
    i zwraca (oczyszczona_nazwa, extra_dict).
    extra_dict zawiera:
      - "versus": lista typów stworzeń (z CREATURE_TYPES)
      - "bonus_vs": np. "+2"
    """
    m = _VERSUS_X_RE.match(name)
    if not m:
        return name, {}

    prefix = m.group("prefix").strip()
    bonus_vs = m.group("bonus_vs")
    creature_types = get_creature_type()  # już istniejący helper, zwraca listę typów
    extra = {
        "versus": creature_types,
        "bonus_vs": f"+{bonus_vs}",
    }
    return prefix, extra


def _infer_subtype_from_name(name: str) -> str | None:
    """
    Z nazwy typu:
      'Sword +1, Hatred^' → 'Sword'
      'Leather Armor +1, Abiding' → 'Leather Armor'
      'Shield +2' → 'Shield'
      'Weapon +1' → 'Weapon'
    """
    # ucinamy wszystko po pierwszym przecinku (np. ", Hatred^")
    base = name.split(",")[0].strip()
    base = base.rstrip("^").strip()

    # Jeśli jest bonus w stylu '+1', ucinamy to
    parts = base.split("+", 1)
    if len(parts) > 1:
        base = parts[0].strip()

    return base or None

def _finalize_item_subtype(item: dict, style: str) -> dict:
    """
    Globalny post-processing: jeśli przedmiot ma generyczny subtype
    (Weapon, Sword, Armor), to losujemy właściwy subtype i poprawiamy nazwę.
    """
    category = item["category"]
    name = item["name"]
    subtype = item["subtype"]

    # --- GENERIC WEAPON ---
    if category == "weapon" and subtype == "Weapon":
        new_subtype = _choose_misc_weapon_subtype(style)
        # podmiana w nazwie
        new_name = name.replace("Weapon", new_subtype, 1)

        item["name"] = new_name
        item["subtype"] = new_subtype
        return item

    # --- GENERIC SWORD ---
    if category == "weapon" and subtype == "Sword":
        new_subtype = _choose_sword_subtype(style)
        new_name = name.replace("Sword", new_subtype, 1)

        item["name"] = new_name
        item["subtype"] = new_subtype
        return item

    # --- GENERIC ARMOR ---
    if category == "armor" and subtype == "Armor":
        new_subtype = _choose_armor_subtype(style)
        new_name = name.replace("Armor", new_subtype, 1)

        item["name"] = new_name
        item["subtype"] = new_subtype
        return item

    return item

# =====================================================================
# COMMON (Heroic / Gritty) – subtabele
# =====================================================================

def roll_common_potions_1(style: str):
    entry = choose_from_table(COMMON_POTIONS_1)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(
        name=name,
        category="potion",
        rarity="common",
        style=style,
        subtype=None,
        cues=cues,
        extra=extra,
    )


def roll_common_potions_2(style: str):
    entry = choose_from_table(COMMON_POTIONS_2)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(
        name=name,
        category="potion",
        rarity="common",
        style=style,
        subtype=None,
        cues=cues,
        extra=extra,
    )


def roll_common_potions_3(style: str):
    entry = choose_from_table(COMMON_POTIONS_3)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(
        name=name,
        category="potion",
        rarity="common",
        style=style,
        subtype=None,
        cues=cues,
        extra=extra,
    )

def roll_common_scrolls(style: str):
    entry = choose_from_table(COMMON_SCROLLS)
    name, cues, extra = _normalize_entry(entry)
    # Treasure Map / Spell Scroll nie ma tu rozbijania – idzie jako "scroll"
    return _make_item(
        name=name,
        category="scroll",
        rarity="common",
        style=style,
        subtype=None,
        cues=cues,
        extra=extra,
    )

def roll_common_misc_items(style: str):
    entry = choose_from_table(COMMON_MISC_ITEMS)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(
        name=name,
        category="wondrous",  # "niebroń / niemikstura" – ogólne magiczne przedmioty
        rarity="common",
        style=style,
        subtype=None,
        cues=cues,
        extra=extra,
    )

# =====================================================================
# UNCOMMON – subtabele (bez broni/pancerzy na razie)
# =====================================================================

def roll_uncommon_potions_1(style: str):
    entry = choose_from_table(UNCOMMON_POTIONS_1)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(
        name=name,
        category="potion",
        rarity="uncommon",
        style=style,
        subtype=None,
        cues=cues,
        extra=extra,
    )


def roll_uncommon_potions_2(style: str):
    entry = choose_from_table(UNCOMMON_POTIONS_2)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(
        name=name,
        category="potion",
        rarity="uncommon",
        style=style,
        subtype=None,
        cues=cues,
        extra=extra,
    )


def roll_uncommon_potions_3(style: str):
    entry = choose_from_table(UNCOMMON_POTIONS_3)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(
        name=name,
        category="potion",
        rarity="uncommon",
        style=style,
        subtype=None,
        cues=cues,
        extra=extra,
    )


def roll_uncommon_rings(style: str):
    entry = choose_from_table(UNCOMMON_RINGS)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(
        name=name,
        category="ring",
        rarity="uncommon",
        style=style,
        subtype="Ring",
        cues=cues,
        extra=extra,
    )

def roll_uncommon_scrolls(style: str):
    entry = choose_from_table(UNCOMMON_SCROLLS)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(
        name=name,
        category="scroll",
        rarity="uncommon",
        style=style,
        subtype=None,
        cues=cues,
        extra=extra,
    )

def roll_uncommon_misc_items(style: str):
    entry = choose_from_table(UNCOMMON_MISC_ITEMS)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(
        name=name,
        category="wondrous",
        rarity="uncommon",
        style=style,
        subtype=None,
        cues=cues,
        extra=extra,
    )

def roll_uncommon_swords(style: str):
    raw = choose_from_table(UNCOMMON_SWORDS)
    name, cues, extra = _normalize_entry(raw)

    # wyciągamy ", +X versus X"
    name, extra_vs = _extract_versus_x(name)
    extra.update(extra_vs)

    subtype = _infer_subtype_from_name(name)

    return _make_item(
        name=name,
        category="weapon",
        rarity="uncommon",
        style=style,
        subtype=subtype,
        cues=cues,
        extra=extra,
    )


def roll_uncommon_misc_weapons(style: str):
    raw = choose_from_table(UNCOMMON_MISC_WEAPONS)
    name, cues, extra = _normalize_entry(raw)

    name, extra_vs = _extract_versus_x(name)
    extra.update(extra_vs)

    subtype = _infer_subtype_from_name(name)

    return _make_item(
        name=name,
        category="weapon",
        rarity="uncommon",
        style=style,
        subtype=subtype,
        cues=cues,
        extra=extra,
    )


def roll_uncommon_armors(style: str):
    raw = choose_from_table(UNCOMMON_ARMOR)
    name, cues, extra = _normalize_entry(raw)

    name, extra_vs = _extract_versus_x(name)
    extra.update(extra_vs)

    subtype = _infer_subtype_from_name(name)

    return _make_item(
        name=name,
        category="armor",
        rarity="uncommon",
        style=style,
        subtype=subtype,
        cues=cues,
        extra=extra,
    )

def roll_rare_rings_1(style: str):
    entry = choose_from_table(RARE_RINGS_1)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "ring", "rare", style, "Ring", cues, extra)


def roll_rare_rings_2(style: str):
    entry = choose_from_table(RARE_RINGS_2)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "ring", "rare", style, "Ring", cues, extra)


def roll_rare_scrolls(style: str):
    entry = choose_from_table(RARE_SCROLLS)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "scroll", "rare", style, None, cues, extra)


def roll_rare_implements_1(style: str):
    entry = choose_from_table(RARE_IMPLEMENT_1)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "implement", "rare", style, None, cues, extra)


def roll_rare_implements_2(style: str):
    entry = choose_from_table(RARE_IMPLEMENT_2)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "implement", "rare", style, None, cues, extra)


def roll_rare_misc_items_1(style: str):
    entry = choose_from_table(RARE_MISC_ITEMS_1)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "wondrous", "rare", style, None, cues, extra)


def roll_rare_misc_items_2(style: str):
    entry = choose_from_table(RARE_MISC_ITEMS_2)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "wondrous", "rare", style, None, cues, extra)


def roll_rare_misc_items_3(style: str):
    entry = choose_from_table(RARE_MISC_ITEMS_3)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "wondrous", "rare", style, None, cues, extra)


def roll_rare_misc_items_4(style: str):
    entry = choose_from_table(RARE_MISC_ITEMS_4)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "wondrous", "rare", style, None, cues, extra)


def roll_rare_misc_items_5(style: str):
    entry = choose_from_table(RARE_MISC_ITEMS_5)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "wondrous", "rare", style, None, cues, extra)


def roll_rare_swords(style: str):
    raw = choose_from_table(RARE_SWORDS)
    name, cues, extra = _normalize_entry(raw)

    name, extra_vs = _extract_versus_x(name)
    extra.update(extra_vs)

    subtype = _infer_subtype_from_name(name)

    return _make_item(name, "weapon", "rare", style, subtype, cues, extra)


def roll_rare_misc_weapons(style: str):
    raw = choose_from_table(RARE_MISC_WEAPONS)
    name, cues, extra = _normalize_entry(raw)

    name, extra_vs = _extract_versus_x(name)
    extra.update(extra_vs)

    subtype = _infer_subtype_from_name(name)

    return _make_item(name, "weapon", "rare", style, subtype, cues, extra)


def roll_rare_armors(style: str):
    raw = choose_from_table(RARE_ARMOR)
    name, cues, extra = _normalize_entry(raw)

    name, extra_vs = _extract_versus_x(name)
    extra.update(extra_vs)

    subtype = _infer_subtype_from_name(name)

    return _make_item(name, "armor", "rare", style, subtype, cues, extra)

def roll_very_rare_potions(style: str):
    entry = choose_from_table(VERY_RARE_POTIONS)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "potion", "very_rare", style, None, cues, extra)


def roll_very_rare_rings(style: str):
    entry = choose_from_table(VERY_RARE_RINGS)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "ring", "very_rare", style, "Ring", cues, extra)


def roll_very_rare_scrolls(style: str):
    entry = choose_from_table(VERY_RARE_SCROLLS)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "scroll", "very_rare", style, None, cues, extra)


def roll_very_rare_implements_1(style: str):
    entry = choose_from_table(VERY_RARE_IMPLEMENT_1)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "implement", "very_rare", style, None, cues, extra)


def roll_very_rare_implements_2(style: str):
    entry = choose_from_table(VERY_RARE_IMPLEMENT_2)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "implement", "very_rare", style, None, cues, extra)


def roll_very_rare_implements_3(style: str):
    entry = choose_from_table(VERY_RARE_IMPLEMENT_3)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "implement", "very_rare", style, None, cues, extra)


def roll_very_rare_misc_items_1(style: str):
    entry = choose_from_table(VERY_RARE_MISC_ITEMS_1)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "wondrous", "very_rare", style, None, cues, extra)


def roll_very_rare_misc_items_2(style: str):
    entry = choose_from_table(VERY_RARE_MISC_ITEMS_2)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "wondrous", "very_rare", style, None, cues, extra)


def roll_very_rare_swords(style: str):
    raw = choose_from_table(VERY_RARE_SWORDS)
    name, cues, extra = _normalize_entry(raw)

    name, extra_vs = _extract_versus_x(name)
    extra.update(extra_vs)

    subtype = _infer_subtype_from_name(name)

    return _make_item(name, "weapon", "very_rare", style, subtype, cues, extra)


def roll_very_rare_misc_weapons(style: str):
    raw = choose_from_table(VERY_RARE_MISC_WEAPONS)
    name, cues, extra = _normalize_entry(raw)

    name, extra_vs = _extract_versus_x(name)
    extra.update(extra_vs)

    subtype = _infer_subtype_from_name(name)

    return _make_item(name, "weapon", "very_rare", style, subtype, cues, extra)


def roll_very_rare_armors(style: str):
    raw = choose_from_table(VERY_RARE_ARMOR)
    name, cues, extra = _normalize_entry(raw)

    name, extra_vs = _extract_versus_x(name)
    extra.update(extra_vs)

    subtype = _infer_subtype_from_name(name)

    return _make_item(name, "armor", "very_rare", style, subtype, cues, extra)

def roll_legendary_rings(style: str):
    entry = choose_from_table(LEGENDARY_RINGS)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "ring", "legendary", style, "Ring", cues, extra)


def roll_legendary_scrolls(style: str):
    entry = choose_from_table(LEGENDARY_SCROLLS)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "scroll", "legendary", style, None, cues, extra)


def roll_legendary_implements(style: str):
    entry = choose_from_table(LEGENDARY_IMPLEMENT)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "implement", "legendary", style, None, cues, extra)


def roll_legendary_misc_items(style: str):
    entry = choose_from_table(LEGENDARY_MISC_ITEMS)
    name, cues, extra = _normalize_entry(entry)
    return _make_item(name, "wondrous", "legendary", style, None, cues, extra)


def roll_legendary_swords(style: str):
    raw = choose_from_table(LEGENDARY_SWORDS)
    name, cues, extra = _normalize_entry(raw)

    name, extra_vs = _extract_versus_x(name)
    extra.update(extra_vs)

    subtype = _infer_subtype_from_name(name)

    return _make_item(name, "weapon", "legendary", style, subtype, cues, extra)


def roll_legendary_misc_weapons(style: str):
    raw = choose_from_table(LEGENDARY_MISC_WEAPONS)
    name, cues, extra = _normalize_entry(raw)

    name, extra_vs = _extract_versus_x(name)
    extra.update(extra_vs)

    subtype = _infer_subtype_from_name(name)

    return _make_item(name, "weapon", "legendary", style, subtype, cues, extra)


def roll_legendary_armors(style: str):
    raw = choose_from_table(LEGENDARY_ARMOR)
    name, cues, extra = _normalize_entry(raw)

    name, extra_vs = _extract_versus_x(name)
    extra.update(extra_vs)

    subtype = _infer_subtype_from_name(name)

    return _make_item(name, "armor", "legendary", style, subtype, cues, extra)

# CLASSIC GENERATOR

def _classic_potions(style: str):
    roll = random.randint(1, 100)

    if 1 <= roll <= 19:
        return roll_common_potions_1(style)
    elif 20 <= roll <= 38:
        return roll_common_potions_2(style)
    elif 39 <= roll <= 57:
        return roll_common_potions_3(style)

    # Uncommon 1–3
    elif 58 <= roll <= 71:
        return roll_uncommon_potions_1(style)
    elif 72 <= roll <= 85:
        return roll_uncommon_potions_2(style)
    elif 86 <= roll <= 99:
        return roll_uncommon_potions_3(style)

    # roll = 100 → second table
    roll2 = random.randint(1, 100)

    if 1 <= roll2 <= 16:
        return roll_uncommon_potions_1(style)
    elif 17 <= roll2 <= 33:
        return roll_uncommon_potions_2(style)
    elif 34 <= roll2 <= 50:
        return roll_uncommon_potions_3(style)
    elif 51 <= roll2 <= 100:
        return roll_very_rare_potions(style)

    raise RuntimeError("Classic Potions error")

def _classic_rings(style: str):
    roll = random.randint(1, 100)

    if 1 <= roll <= 5:
        return roll_uncommon_rings(style)
    elif 6 <= roll <= 25:
        return roll_rare_rings_1(style)
    elif 26 <= roll <= 45:
        return roll_rare_rings_2(style)
    elif 46 <= roll <= 96:
        return roll_very_rare_rings(style)
    elif 97 <= roll <= 100:
        return roll_legendary_rings(style)


def _classic_scrolls(style: str):
    roll = random.randint(1, 100)

    if 1 <= roll <= 38:
        return roll_common_scrolls(style)
    elif 39 <= roll <= 80:
        return roll_uncommon_scrolls(style)
    elif 81 <= roll <= 96:
        return roll_rare_scrolls(style)
    elif 97 <= roll <= 99:
        return roll_very_rare_scrolls(style)

    # 100 → second table
    roll2 = random.randint(1, 100)

    if 1 <= roll2 <= 75:
        return roll_very_rare_scrolls(style)
    else:
        return roll_legendary_scrolls(style)

def _classic_implements(style: str):
    roll = random.randint(1, 100)

    if 1 <= roll <= 32:
        return roll_rare_implements_1(style)
    elif 33 <= roll <= 64:
        return roll_rare_implements_2(style)
    elif 65 <= roll <= 75:
        return roll_very_rare_implements_1(style)
    elif 76 <= roll <= 86:
        return roll_very_rare_implements_2(style)
    elif 87 <= roll <= 97:
        return roll_very_rare_implements_3(style)
    elif 98 <= roll <= 100:
        return roll_legendary_implements(style)

def _classic_misc_items(style: str):
    roll = random.randint(1, 100)

    if 1 <= roll <= 2:
        return roll_common_misc_items(style)
    elif 3 <= roll <= 6:
        return roll_uncommon_misc_items(style)
    elif 7 <= roll <= 11:
        return roll_rare_misc_items_1(style)
    elif 12 <= roll <= 16:
        return roll_rare_misc_items_2(style)
    elif 17 <= roll <= 21:
        return roll_rare_misc_items_3(style)
    elif 22 <= roll <= 26:
        return roll_rare_misc_items_4(style)
    elif 27 <= roll <= 31:
        return roll_rare_misc_items_5(style)
    elif 32 <= roll <= 61:
        return roll_very_rare_misc_items_1(style)
    elif 62 <= roll <= 91:
        return roll_very_rare_misc_items_2(style)
    elif 92 <= roll <= 100:
        return roll_legendary_misc_items(style)

def _classic_swords(style: str):
    roll = random.randint(1, 100)

    if 1 <= roll <= 50:
        return roll_uncommon_swords(style)
    elif 51 <= roll <= 84:
        return roll_rare_swords(style)
    elif 85 <= roll <= 99:
        return roll_very_rare_swords(style)
    elif 100 == roll:
        return roll_legendary_swords(style)

def _classic_misc_weapons(style: str):
    roll = random.randint(1, 100)

    if 1 <= roll <= 50:
        return roll_uncommon_misc_weapons(style)
    elif 51 <= roll <= 84:
        return roll_rare_misc_weapons(style)
    elif 85 <= roll <= 99:
        return roll_very_rare_misc_weapons(style)
    elif 100 == roll:
        return roll_legendary_misc_weapons(style)

def _classic_armors(style: str):
    roll = random.randint(1, 100)

    if 1 <= roll <= 50:
        return roll_uncommon_armors(style)
    elif 51 <= roll <= 84:
        return roll_rare_armors(style)
    elif 85 <= roll <= 99:
        return roll_very_rare_armors(style)
    elif 100 == roll:
        return roll_legendary_armors(style)

def _roll_from_weighted_table(table):
    """Generic: takes [(min, max, value), ...] and returns value."""
    roll = random.randint(1, 20)
    for lo, hi, val in table:
        if lo <= roll <= hi:
            return val
    raise RuntimeError("Weighted table roll failed.")

def _choose_sword_subtype(style: str):
    table = SWORD_TYPES.get(style)
    if not table:
        raise RuntimeError(f"No sword table for style: {style}")
    return _roll_from_weighted_table(table)

def _choose_misc_weapon_subtype(style: str):
    # Step 1: choose category (Axe / Bow / etc.)
    category = _roll_from_weighted_table(MISC_WEAPON_TYPES)

    if category == "Ammunition":
        return _roll_from_weighted_table(AMMO_TYPES[style])

    if category == "Axe":
        return _roll_from_weighted_table(AXE_TYPES[style])

    if category == "Bludgeon":
        return _roll_from_weighted_table(BLUDGEON_TYPES[style])

    if category == "Bow":
        return _roll_from_weighted_table(BOW_TYPES[style])

    if category == "Spear":
        return _roll_from_weighted_table(SPEAR_TYPES[style])

    if category == "Other":
        return _roll_from_weighted_table(OTHER_WEAPON_TYPES[style])

    raise RuntimeError(f"Unknown misc weapon category: {category}")

def _choose_armor_subtype(style: str):
    table = ARMOR_TYPES.get(style)
    if not table:
        raise RuntimeError(f"No armor table for style: {style}")
    return _roll_from_weighted_table(table)

def _roll_creature_type():
    roll = random.randint(1, 20)
    for lo, hi, name in CREATURE_TYPES:
        if lo <= roll <= hi:
            if name == "ROLL_TWICE":
                # dociągnięcie dwóch wyników, zawsze listy
                t1 = _roll_creature_type()
                t2 = _roll_creature_type()

                # normalizacja: oba wyniki zamieniamy na listy
                if isinstance(t1, str):
                    t1 = [t1]
                if isinstance(t2, str):
                    t2 = [t2]

                return t1 + t2

            # normalny wynik — zwracamy listę!
            return [name]

    raise RuntimeError("Creature type roll failed.")

def _extract_versus_x(name):
    m = _VERSUS_X_RE.match(name)
    if not m:
        return name, {}

    prefix = m.group("prefix").strip()
    bonus_vs = m.group("bonus_vs")

    # now → real creature type roll
    result = _roll_creature_type()
    if isinstance(result, str):
        versus_list = [result]
    else:
        versus_list = result

    extra = {
        "versus": versus_list,
        "bonus_vs": f"+{bonus_vs}",
    }
    return prefix, extra




#PRINT

if __name__ == "__main__":
    print("\n=== TEST: COMMON ===")
    for _ in range(3):
        result = generate_item("heroic", "ancient_myth", "common")
        print(result)

    print("\n=== TEST: UNCOMMON ===")
    for _ in range(3):
        result = generate_item("heroic", "ancient_myth", "uncommon")
        print(result)

    print("\n=== TEST: RARE ===")
    for _ in range(3):
        result = generate_item("heroic", "ancient_myth", "rare")
        print(result)

    print("\n=== TEST: VERY RARE ===")
    for _ in range(3):
        result = generate_item("heroic", "ancient_myth", "very_rare")
        print(result)

    print("\n=== TEST: LEGENDARY ===")
    for _ in range(3):
        result = generate_item("heroic", "ancient_myth", "legendary")
        print(result)

if __name__ == "__main__":
    print("\n=== TEST: COMMON ===")
    for _ in range(3):
        result = generate_item("heroic", "ancient_myth", "common")
        print(result)

    print("\n=== TEST: UNCOMMON ===")
    for _ in range(3):
        result = generate_item("heroic", "ancient_myth", "uncommon")
        print(result)

    print("\n=== TEST: RARE ===")
    for _ in range(3):
        result = generate_item("heroic", "ancient_myth", "rare")
        print(result)

    print("\n=== TEST: VERY RARE ===")
    for _ in range(3):
        result = generate_item("heroic", "ancient_myth", "very_rare")
        print(result)

    print("\n=== TEST: LEGENDARY ===")
    for _ in range(3):
        result = generate_item("heroic", "ancient_myth", "legendary")
        print(result)

    print("\n=== TEST: CLASSIC ===")
    for _ in range(10):
        result = generate_item("classic", "ancient_myth")
        print(result)

print("\n=== TEST WEAPON SUBTYPES ===")
for _ in range(10):
    print(_choose_misc_weapon_subtype("ancient_myth"))

print("\n=== TEST SWORD SUBTYPES ===")
for _ in range(10):
    print(_choose_sword_subtype("ancient_myth"))

print("\n=== TEST ARMOR SUBTYPES ===")
for _ in range(10):
    print(_choose_armor_subtype("ancient_myth"))

print("\n=== TEST VERSUS X ===")
for _ in range(10):
    name = "Sword +1, +2 versus X"
    cleaned, extra = _extract_versus_x(name)
    print(extra)
