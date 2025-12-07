import random
from occupations_data import OCCUPATIONS
from physical_features import generate_physical_features
from proficiencies_data import general_proficiencies
from proficiency_helpers import add_proficiency, can_take_proficiency, general_proficiency_bonus




# ============================================================
#  ATTRIBUTE ROLLER (3d6)
# ============================================================

def roll_3d6():
    return sum(random.randint(1, 6) for _ in range(3))


def generate_attributes():
    stats = {
        "STR": roll_3d6(),
        "DEX": roll_3d6(),
        "CON": roll_3d6(),
        "INT": roll_3d6(),
        "WIS": roll_3d6(),
        "CHA": roll_3d6(),
    }
    return stats


# ============================================================
#  INT BONUSES
# ============================================================

def int_bonus(INT):
    if 13 <= INT <= 15:
        return 1
    if 16 <= INT <= 17:
        return 2
    if INT == 18:
        return 3
    return 0


# ============================================================
#  RANDOM GENERAL PROFICIENCIES (POOL)
# ============================================================

def pick_random_general_proficiencies(INT):
    picks = 4 + general_proficiency_bonus(INT)
    pool = general_proficiencies[:]  # prawdziwa pula z proficiencies_data
    random.shuffle(pool)
    return pool[:picks]



# ============================================================
#  OCCUPATION PICKING
# ============================================================

def pick_random_occupation_category():
    return random.choice(list(OCCUPATIONS.keys()))


def pick_random_occupation_from_category(category):
    return random.choice(OCCUPATIONS[category])


def get_occupation_proficiencies(occupation_entry):
    profs = []

    # Add all proficiencies from the OCCUPATIONS entry
    for p in occupation_entry["proficiencies"]:
        if "rank" in p:
            profs.append(f"{p['name']} {p['rank']}")
        elif "specialization" in p:
            profs.append(f"{p['name']} ({p['specialization']})")
        elif "weapons" in p:
            profs.append(f"{p['name']} {', '.join(p['weapons'])}")
        else:
            profs.append(p["name"])

    # If inherits exists, add inherited military profs
    if "inherits" in occupation_entry:
        inherited = occupation_entry["inherits"]
        for occ in OCCUPATIONS["Military"]:
            if occ["name"] == inherited:
                for p in occ["proficiencies"]:
                    if "rank" in p:
                        profs.append(f"{p['name']} {p['rank']}")
                    elif "specialization" in p:
                        profs.append(f"{p['name']} ({p['specialization']})")
                    elif "weapons" in p:
                        profs.append(f"{p['name']} {', '.join(p['weapons'])}")
                    else:
                        profs.append(p["name"])
                break

    # Extra profs (Marshal, Quartermaster, etc.)
    if "extra_proficiencies" in occupation_entry:
        for p in occupation_entry["extra_proficiencies"]:
            if "rank" in p:
                profs.append(f"{p['name']} {p['rank']}")
            elif "specialization" in p:
                profs.append(f"{p['name']} ({p['specialization']})")
            elif "weapons" in p:
                profs.append(f"{p['name']} {', '.join(p['weapons'])}")
            else:
                profs.append(p["name"])

    return profs


# ============================================================
#  PHYSICAL FEATURES
# ============================================================




# ============================================================
#  RACE + HIT POINTS
# ============================================================

RACE_OPTIONS = ["Human", "Dwarf", "Elf"]

def roll_hp(race, is_military):
    """
    ACKS Zero-level HD:
    - Humans: 1/2 HD (1d4), OR 1-1 HD if military (1d6-1)
    - Dwarves: 1d4 OR 1d6-1 if militia
    - Elves: 1d6-1 OR 1d6 if militia
    """

    # Noncombatants
    if random.random() < 0.02:
        return 1

    if race == "Human":
        if is_military:
            return max(1, random.randint(1, 8) - 1)
        else:
            return random.randint(1, 4)

    if race == "Dwarf":
        if is_military:
            return max(1, random.randint(1, 8) - 1)
        else:
            return random.randint(1, 4)

    if race == "Elf":
        if is_military:
            return random.randint(1, 8)
        else:
            return max(1, random.randint(1, 8) - 1)

    return 1


# ============================================================
#  MAIN ZERO-LEVEL GENERATOR
# ============================================================

def generate_zero_level_character(
    mode="random_proficiencies",
    chosen_category=None,
    chosen_occupation=None,
    race_override=None
):
    """
    mode:
      - "random_proficiencies" → 4 + INT-bonus proficiencies
      - "category" → choose random occupation from category
      - "occupation" → choose specific occupation
    """

    stats = generate_attributes()

    # --- Determine proficiencies ---
    if mode == "random_proficiencies":
        profs = pick_random_general_proficiencies(stats["INT"])
        occupation = None

    elif mode == "category":
        occupation = pick_random_occupation_from_category(chosen_category)
        profs = get_occupation_proficiencies(occupation)

        # add INT bonus profs
        bonus_count = general_proficiency_bonus(stats["INT"])
        if bonus_count > 0:
            pool = general_proficiencies[:]
            random.shuffle(pool)
            profs += pool[:bonus_count]

    elif mode == "occupation":
        occupation = chosen_occupation
        profs = get_occupation_proficiencies(occupation)

        # add INT bonus profs
        bonus_count = int_bonus(stats["INT"])
        if bonus_count > 0:
            profs += random.sample(general_proficiencies, bonus_count)

    # --- race + HP ---
    if race_override:
        race = race_override
    else:
        race = random.choice(RACE_OPTIONS)
    is_military = occupation and any(
        category == "Military" for category, entries in OCCUPATIONS.items()
        if occupation in entries
    )

    hp = roll_hp(race, is_military)

    features = generate_physical_features(stats["CHA"])

    def roll_alignment():
        d = random.randint(1, 6)
        if d in (1, 2):
            return "Lawful"
        elif d in (3, 4, 5):
            return "Neutral"
        else:
            return "Chaotic"

    alignment = roll_alignment()

    # Final result
    return {
        "stats": stats,
        "race": race,
        "alignment": alignment,
        "hp": hp,
        "features": features,
        "mode": mode,
        "occupation_category": chosen_category,
        "occupation": occupation["name"] if occupation else None,
        "proficiencies": profs,
    }
