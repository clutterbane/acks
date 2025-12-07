import random
from proficiencies_data import general_proficiencies, proficiency_limits, class_proficiency_lists, proficiency_progression, class_starting_general_proficiencies

# ----------------------------------------------------
# BASIC HELPERS
# ----------------------------------------------------

def can_take_proficiency(prof_name, char_profs, limits):
    """Check if proficiency can be taken given limit table."""
    limit = limits.get(prof_name, None)
    current = char_profs.get(prof_name, 0)
    return limit is None or current < limit


def add_proficiency(prof_name, char_profs, limits):
    """Add proficiency if allowed."""
    if not can_take_proficiency(prof_name, char_profs, limits):
        return False
    char_profs[prof_name] = char_profs.get(prof_name, 0) + 1
    return True


def general_proficiency_bonus(INT):
    """Bonus general proficiencies from INT."""
    if 13 <= INT <= 15:
        return 1
    if 16 <= INT <= 17:
        return 2
    if INT == 18:
        return 3
    return 0


def pick_limited_from_pool(pool, char_profs, limits):
    """Randomly picks a proficiency from the pool, respecting limits."""
    pool = pool[:]  # local copy
    random.shuffle(pool)
    for prof in pool:
        if can_take_proficiency(prof, char_profs, limits):
            char_profs[prof] = char_profs.get(prof, 0) + 1
            return prof
    return None


# ----------------------------------------------------
# AUTO PROFICIENCIES (class-based, at level X)
# ----------------------------------------------------

def apply_auto_proficiencies(final_class, level, char_profs, limits, auto_table):
    """
    Apply class-based auto proficiencies from table:
    class_starting_general_proficiencies.
    """
    gained = []
    table = auto_table.get(final_class, {})

    for lvl, entry in table.items():
        if level < lvl:
            continue

        # AUTO
        for prof in entry.get("auto", []):
            if add_proficiency(prof, char_profs, limits):
                gained.append((lvl, "auto", prof))

        # CHOOSE_ONE (Venturer style)
        for group in entry.get("choose_one", []):
            chosen = random.choice(group)
            if add_proficiency(chosen, char_profs, limits):
                gained.append((lvl, "choose_one", chosen))

        # CHOOSE_GROUP (Barbarian culture groups)
        group_table = entry.get("choose_group")
        if group_table:
            chosen_region = random.choice(list(group_table.keys()))
            for prof in group_table[chosen_region]:
                if add_proficiency(prof, char_profs, limits):
                    gained.append((lvl, "choose_group", prof))

    return gained


# ----------------------------------------------------
# PROFICIENCIES FROM LEVEL PROGRESSION
# ----------------------------------------------------

def apply_level_proficiencies(
    final_class,
    level,
    char_profs,
    limits,
    progression_table,
    class_proficiency_lists,
    general_proficiencies
):
    """
    Apply proficiencies gained at each level from proficiency_progression.
    """
    gained_log = []

    if final_class not in progression_table:
        return gained_log

    prog = progression_table[final_class]

    for lvl in range(2, level + 1):
        if lvl not in prog:
            continue

        entry = prog[lvl]

        # class proficiencies
        for _ in range(entry.get("class", 0)):
            pool = class_proficiency_lists[final_class]
            prof = pick_limited_from_pool(pool, char_profs, limits)
            if prof:
                gained_log.append((lvl, "class", prof))

        # general proficiencies
        for _ in range(entry.get("general", 0)):
            pool = general_proficiencies
            prof = pick_limited_from_pool(pool, char_profs, limits)
            if prof:
                gained_log.append((lvl, "general", prof))

    return gained_log


# ----------------------------------------------------
# FIRST-LEVEL CLASS PROFICIENCY CHOICE
# ----------------------------------------------------

def choose_class_proficiency(final_class, char_profs, proficiency_limits, class_proficiency_lists):
    """
    Selects one class proficiency at level 1.
    """
    options = class_proficiency_lists[final_class][:]
    random.shuffle(options)

    for prof in options:
        if add_proficiency(prof, char_profs, proficiency_limits):
            return prof

    return None
