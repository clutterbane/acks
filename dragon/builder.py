import random
from dragon.data import (
    HABITATS,
    BODY_FORMS,
    AGE_DATA,
    ENCOUNTER_DATA,
    SPECIAL_ABILITIES,
    BREATH_WEAPONS,
    BREATH_USE_MODES,
    LEGENDARY_RULES,
)
from dragon.utils import roll, parse_dice


# ============================================================
# Helper: apply legendary growth based on real age
# ============================================================

def apply_legendary_growth(base_stats: dict, age_years: int) -> dict:
    """Adds legendary AC/HD/damage scaling if age > 701."""

    min_age = LEGENDARY_RULES["increment_years"]
    increments = 0

    if age_years and age_years > min_age:
        increments = (age_years - min_age) // min_age

    if increments <= 0:
        return base_stats

    new_stats = base_stats.copy()
    new_stats["legendary_increments"] = increments
    new_stats["hd"] = base_stats["hd"] + increments * LEGENDARY_RULES["hd_per_increment"]
    new_stats["ac"] = base_stats["ac"] + increments * LEGENDARY_RULES["ac_per_increment"]

    # damage scaling is applied later on per body form
    new_stats["extra_damage_per_increment"] = (
        increments * LEGENDARY_RULES["extra_damage_per_increment"]
    )

    return new_stats


# ============================================================
# Helper: choose allowed special abilities
# ============================================================

def filter_abilities(dragon, chosen):
    allowed = []

    for name, spec in SPECIAL_ABILITIES.items():
        req = spec["requires"]

        # speech requirement
        if req.get("speech") and dragon["speech_chance"] <= 0:
            continue

        # alignment restriction
        if "alignment" in req:
            if dragon["alignment"] not in req["alignment"]:
                continue

        # claws/tail
        if "body_forms" in req:
            if dragon["body_form"] not in req["body_forms"]:
                continue

        if req.get("tail_attack") and not dragon["has_tail"]:
            continue

        # breath weapon
        if req.get("breath_weapon") and not dragon["has_breath_weapon"]:
            continue

        # spellcasting
        if req.get("spellcasting") and not dragon["spellcasting"]:
            continue

        allowed.append(name)

    return allowed


# ============================================================
# Main Builder
# ============================================================

def build_dragon(
    habitat: str,
    body_form: str,
    age_category: str,
    real_age_years: int = None,
    breath_mode: str = None,
    random_specials: bool = True,
):
    """
    Creates a complete dragon stat block.
    """

    # ---------------------------
    # BASE LOOKUP
    # ---------------------------

    habitat_data = HABITATS[habitat]
    age_data = AGE_DATA[age_category]
    form_data = BODY_FORMS[body_form]
    encounter_data = ENCOUNTER_DATA[age_category]

    # ---------------------------
    # RANDOMIZE COLOR
    # ---------------------------
    color = random.choice(habitat_data["colors"])

    # ---------------------------
    # DETERMINE ALIGNMENT
    # ---------------------------
    alignment = random.choice(habitat_data["alignment"])

    # ---------------------------
    # BREATH WEAPON
    # ---------------------------
    breath_weapon = BREATH_WEAPONS[habitat]
    has_breath_weapon = True

    # random limited vs recharging
    if breath_mode is None:
        breath_mode = "limited" if random.randint(1, 6) <= 4 else "recharging"

    breath_usage = BREATH_USE_MODES[breath_mode]

    # ---------------------------
    # AGE & BASE STATS
    # ---------------------------

    stats = {
        **age_data,  # copy all primary stats
        "age_category": age_category,  # ← DODAJ TO
        "alignment": alignment,
        "habitat": habitat,
        "color": color,
        "body_form": body_form,
        "attack_routine": form_data["routine"],
        "damage_profile": form_data["damage"][age_category],
        "has_tail": form_data["has_tail"],
        "has_claws": form_data["has_claws"],
        "winged": form_data["winged"],
        "has_breath_weapon": has_breath_weapon,
        "breath_weapon": breath_weapon,
        "breath_use": breath_usage,
        "encounter": encounter_data,
    }

    # ---------------------------
    # LEGENDARY HANDLING
    # ---------------------------

    if real_age_years:
        stats = apply_legendary_growth(stats, real_age_years)

    # ---------------------------
    # SPELLCASTING FLAG
    # ---------------------------
    stats["spellcasting"] = any(x > 0 for x in stats["spells"])

    # ---------------------------
    # SPECIAL ABILITIES SELECTION
    # ---------------------------
    max_specials = stats["special_abilities"]

    if random_specials:
        allowed = filter_abilities(stats, SPECIAL_ABILITIES)
        chosen = random.sample(allowed, min(max_specials, len(allowed)))
    else:
        chosen = []

    stats["special_abilities_list"] = chosen

    # ---------------------------
    # RETURN THE FINAL DRAGON
    # ---------------------------
    return stats
