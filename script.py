import random
from npc_magic_items import generate_magic_items_for_level


ALL_CLASSES = {
        "Mage", "Thief", "Crusader", "Fighter", "Explorer", "Venturer",
        "Bard", "Bladedancer", "Assassin", "Priestess", "Shaman", "Barbarian",
        "Warlock", "Witch", "Paladin",
        "Dwarven Craftpriest", "Dwarven Vaultguard",
        "Elven Nightblade", "Elven Spellsword",
        "Nobiran Wonderworker", "Zaharan Ruinguard"
    }

# --------------------------------------------------------------------
#  ACKS CLASS TABLE (exact reproduction of probabilities)
# --------------------------------------------------------------------
ACKS_TABLE = [
    # row_min, row_max, 8-column class block
    (1, 10,  ["Mage", "Mage", "Mage", "Mage", "Elven Spellsword", "Warlock", "Warlock", "Nobiran Wonderworker"]),
    (11, 30, ["Thief", "Bard", "Assassin", "Thief", "Elven Nightblade", "Special", "Special", "Special"]),
    (31, 50, ["Crusader", "Bladedancer", "Priestess", "Shaman", "Dwarven Craftpriest", "Witch", "Witch", "Special"]),
    (51, 75, ["Fighter", "Fighter", "Fighter", "Barbarian", "Dwarven Vaultguard", "Paladin", "Paladin", "Zaharan Ruinguard"]),
    (76, 90, ["Explorer", "Explorer", "Explorer", "Explorer", "Special", "Special", "Special", "Special"]),
    (91, 100,["Venturer", "Venturer", "Venturer", "Venturer", "Special", "Special", "Special", "Special"]),
]

def get_column_index(col_roll):
    """Maps 1d100 roll to ACKS column index."""
    if col_roll <= 40:
        return 0
    elif col_roll <= 60:
        return 1
    elif col_roll <= 80:
        return 2
    elif col_roll <= 90:
        return 3
    elif col_roll <= 94:
        return 4
    elif col_roll <= 96:
        return 5
    elif col_roll <= 98:
        return 6
    else:
        return 7

def roll_class_from_ACKS():
    """Rolls class exactly according to the ACKS NPC class table."""
    row_roll = random.randint(1, 100)

    # find row
    for row_min, row_max, row_classes in ACKS_TABLE:
        if row_min <= row_roll <= row_max:
            break

    # roll column, reroll if "Special"
    while True:
        col_roll = random.randint(1, 100)
        idx = get_column_index(col_roll)
        cls = row_classes[idx]

        if cls != "Special":
            return cls

corrupting_weaknesses = {
    "Disfigured": {"limit": None},        # unlimited
    "Distrusted": {"limit": None},        # unlimited
    "Enervated": {"limit": None},         # unlimited
    "Frightening to Beasts": {"limit": 1},
    "Haunted": {"limit": None},           # unlimited
    "Mad": {"limit": 1},
    "Mutated": {"limit": None},           # unlimited
    "Nocturnal": {"limit": None},         # unlimited
    "Obsessed": {"limit": None},          # unlimited
    "Sleepless": {"limit": 5},
}

mutations_table = {
    1: "Size Shift: Shrink to half size or grow to giant size; DEX becomes 3 and recovers by 1 per week.",
    2: "Animalistic Traits: Gain attributes of an appropriate animal; +2 to three attributes, -2 to three others.",
    3: "Thick Hide: +2 AC, but -1 DEX and -1 CHA.",
    4: "Delicate Beauty: +4 CHA (max 18) but -4 STR (min 3).",
    5: "Third Eye: Gain telepathy 3/day; -3 to reaction rolls from normal humans.",
    6: "Deathly Pallor: -4 reaction with living creatures, undead treat you as one of them.",
    7: "Claws: Gain claw attack (1d4), but -1 to fine manipulation throws.",
    8: "Fanged Maw: Gain bite (1d6), but cannot speak normally (can still cast spells).",
    9: "Tentacle Arm: Tentacle attack (1d8), -3 CHA, -4 to fine manipulation, cannot use bows or two-handed weapons.",
    10: "Monstrous Transformation: Become a sapient monster fitting your alignment & temperament.",
    11: "Oppositional Monstrous Transformation: Become a monster opposite your alignment & temperament.",
    12: "Daily Amnesia: Each day Save vs Spells or forget your identity for 1d6 days.",
    13: "Recurring Madness: Suffer random actions like incite madness for 1d6 days; 5% daily recurrence chance.",
    14: "Bleeding Curse: Below 1/2 HP you bleed 1 HP/round unless healed; bleeding resumes after next injury.",
    15: "Instant Aging: Age to halfway of max racial age; Save vs Death or die.",
    16: "Degeneration: Permanently lose 1d3 STR, DEX, CON; speed halved.",
    17: "Hollow Bones: CON halved; take double bludgeoning/fall damage; weight -30%.",
    18: "Wasting Disease: Permanently lose 1d3 CHA and CON, then lose 1 CHA and CON daily.",
    19: "Rotting Flesh: CHA becomes 3; speed halved; no natural healing.",
    20: "Ochre Ooze: Transform into sentient ochre ooze; cannot cast, speak, or use items; equipment destroyed.",
}

# WITCH TRADITIONS

witch_traditions = {
    "Antiquarian Witch": {
        1: "Traditional Medicine",
        2: "Healing Arts",
        3: "Second Sight",
        4: "Magic Mirror",
    },
    "Chtonic Witch": {
        1: "Bedazzling Glamour",
        2: "Decadent Arts",
        3: "Subtle Beguilement",
        4: "Evil Eye",
    },
    "Sylvan Witch": {
        1: "Friends of Birds and Beasts",
        2: "Natural Arts",
        3: "Close Friend of Birds and Beasts",
        4: "Enchanted Forest",
    },
}

def choose_witch_tradition():
    return random.choice(list(witch_traditions.keys()))

# ================================
# WARLOCK DARK PATHS (SUBCLASSES)

warlock_paths = {
        "Demonologist": {
            1: "Conjure Dark Powers",
            2: "Theology",
            3: "Conjure Hellion",
            4: "Expanded Repertoire",
            5: "Words of Command and Obedience",
            6: "Power of Sacrifice"
        },
        "Necromancer": {
            1: "Secrets of the Dark Arts",
            2: "Mortuary Science",
            3: "Speak with Dead",
            4: "Expanded Repertoire",
            5: "Lordship Over the Undead",
            6: "Secrets of Life and Death"
        },
        "Transmogrification": {
            1: "Grotesque Arts of Transformation",
            2: "Alchemy",
            3: "Skinchange",
            4: "Expanded Repertoire",
            5: "Hideous Servant",
            6: "Shape Flesh and Bone"
        },
    }

def choose_warlock_path():
    """Losuje ścieżkę Warlocka."""
    return random.choice(list(warlock_paths.keys()))

def run_generator(final_class, level, mode="heroic", style="ancient_myth"):
    import io
    out = io.StringIO()

    def p(*args, **kwargs):
        print(*args, file=out, **kwargs)

    # --------------------------------------------------------
    # If class=Random → choose using ACKS class table
    # --------------------------------------------------------
    if final_class == "Random":
        final_class = roll_class_from_ACKS()

    warlock_path = None
    if final_class == "Warlock":
        warlock_path = choose_warlock_path()

    witch_tradition = None
    if final_class == "Witch":
        witch_tradition = choose_witch_tradition()

    # -----------------------
    # GENEROWANIE POSTACI
    # -----------------------

    def roll_and_drop(dice, drop):
        rolls = [random.randint(1, 6) for _ in range(dice)]
        rolls.sort(reverse=True)
        return sum(rolls[:-drop])

    def generate_attributes():
        results = []

        # 5d6 drop 2 → minimum 13
        r1 = roll_and_drop(5, 2)
        if r1 < 13:
            r1 = 13
        results.append(r1)

        # 4d6 drop 1 → minimum 9
        r2 = roll_and_drop(4, 1)
        if r2 < 9:
            r2 = 9
        results.append(r2)

        # drugie 4d6 drop 1 → również minimum 9
        r3 = roll_and_drop(4, 1)
        if r3 < 9:
            r3 = 9
        results.append(r3)

        # pozostałe 3 staty to zwykłe 3d6
        results.append(sum(random.randint(1, 6) for _ in range(3)))
        results.append(sum(random.randint(1, 6) for _ in range(3)))
        results.append(sum(random.randint(1, 6) for _ in range(3)))

        stats_order = ["STR", "DEX", "CON", "INT", "WIL", "CHA"]
        random.shuffle(results)
        return dict(zip(stats_order, results))

    # przykład
    stats = generate_attributes()

    # --------------------------------------------
    # MAGICZNE PRZEDMIOTY (ACKS NPC WEALTH TABLE)
    # --------------------------------------------
    magic_items = generate_magic_items_for_level(level, "heroic", style)


    # MAKSYMALNE POZIOMY KLAS
    class_max_level = {
        "Assassin": 14,
        "Barbarian": 14,
        "Bard": 14,
        "Bladedancer": 14,
        "Crusader": 14,
        "Dwarven Craftpriest": 10,
        "Dwarven Vaultguard": 13,
        "Elven Nightblade": 11,
        "Elven Spellsword": 10,
        "Explorer": 14,
        "Fighter": 14,
        "Mage": 14,
        "Nobiran Wonderworker": 12,
        "Paladin": 14,
        "Priestess": 14,
        "Shaman": 14,
        "Thief": 14,
        "Venturer": 14,
        "Warlock": 14,
        "Witch": 14,
        "Zaharan Ruinguard": 12
    }

    # (opcjonalnie) przycięcie poziomu do max dla danej klasy:
    max_lvl = class_max_level.get(final_class, 14)
    if level > max_lvl:
        level = max_lvl

    ALL_CLASSES = {
        "Mage", "Thief", "Crusader", "Fighter", "Explorer", "Venturer",
        "Bard", "Bladedancer", "Assassin", "Priestess", "Shaman", "Barbarian",
        "Warlock", "Witch", "Paladin",
        "Dwarven Craftpriest", "Dwarven Vaultguard",
        "Elven Nightblade", "Elven Spellsword",
        "Nobiran Wonderworker", "Zaharan Ruinguard"
    }

    # TYTUŁY KLASOWE

    class_titles = {
        "Fighter": {
            1: "Man-at-Arms",
            2: "Warrior",
            3: "Swordmaster",
            4: "Hero",
            5: "Exemplar",
            6: "Myrmidon",
            7: "Champion",
            8: "Epic Hero",
            9: "Warlord",
            10: "Warlord, 10th lvl",
            11: "Warlord, 11th lvl",
            12: "Warlord, 12th lvl",
            13: "Warlord, 13th lvl",
            14: "Overlord",
        },

        "Explorer": {
            1: "Scout",
            2: "Outrider",
            3: "Forester",
            4: "Explorer",
            5: "Guide",
            6: "Tracker",
            7: "Wayfinder",
            8: "Ranger",
            9: "Warden",
            10: "Warden, 10th lvl",
            11: "Warden, 11th lvl",
            12: "Warden, 12th lvl",
            13: "Warden, 13th lvl",
            14: "Lord Warden",
        },

        "Thief": {
            1: "Footpad",
            2: "Hood",
            3: "Robber",
            4: "Burglar",
            5: "Rogue",
            6: "Scoundrel",
            7: "Pilferer",
            8: "Thief",
            9: "Master Thief",
            10: "Master Thief, 10th level",
            11: "Master Thief, 11th level",
            12: "Master Thief, 12th level",
            13: "Master Thief, 13th level",
            14: "Prince of Thieves",
        },

        "Mage": {
            1: "Arcanist",
            2: "Seer",
            3: "Theurgist",
            4: "Magician",
            5: "Thaumaturge",
            6: "Enchanter",
            7: "Sorcerer",
            8: "Mage",
            9: "Wizard",
            10: "Wizard, 10th lvl",
            11: "Wizard, 11th lvl",
            12: "Wizard, 12th lvl",
            13: "Wizard, 13th lvl",
            14: "Archmage",
        },

        "Crusader": {
            1: "Catechist",
            2: "Acolyte",
            3: "Priest",
            4: "Curate",
            5: "Vicar",
            6: "Rector",
            7: "Prelate",
            8: "Bishop",
            9: "Patriarch",
            10: "Patriarch, 10th lvl",
            11: "Patriarch, 11th lvl",
            12: "Patriarch, 12th lvl",
            13: "Patriarch, 13th lvl",
            14: "Theocrat",
        },

        "Venturer": {
            1: "Tinker",
            2: "Trader",
            3: "Arbitrager",
            4: "Commissary",
            5: "Mercantilist",
            6: "Enterpriser",
            7: "Venturer",
            8: "Merchant Venturer",
            9: "Merchant Prince",
            10: "Merchant Prince, 10th lvl",
            11: "Merchant Prince, 11th lvl",
            12: "Merchant Prince, 12th lvl",
            13: "Merchant Prince, 13th lvl",
            14: "Mogul",
        },

        "Assassin": {
            1: "Thug",
            2: "Enforcer",
            3: "Torturer",
            4: "Slayer",
            5: "Destroyer",
            6: "Executioner",
            7: "Blackguard",
            8: "Assassin",
            9: "Master Assassin",
            10: "Master Assassin, 10th lvl",
            11: "Master Assassin, 11th lvl",
            12: "Master Assassin, 12th lvl",
            13: "Master Assassin, 13th lvl",
            14: "Grandfather of Assassins",
        },

        "Barbarian": {
            1: "Hunter",
            2: "Raider",
            3: "Marauder",
            4: "Plunderer",
            5: "Reaver",
            6: "Bloodletter",
            7: "Menace",
            8: "Scourge",
            9: "Warchief",
            10: "Warchief, 10th lvl",
            11: "Warchief, 11th lvl",
            12: "Warchief, 12th lvl",
            13: "Warchief, 13th lvl",
            14: "Great Chieftain",
        },

        "Bard": {
            1: "Reciter",
            2: "Versifier",
            3: "Archivist",
            4: "Annalist",
            5: "Chronicler",
            6: "Panegyrist",
            7: "Skald",
            8: "Rhapsodist",
            9: "Bard",
            10: "Bard, 10th lvl",
            11: "Bard, 11th lvl",
            12: "Bard, 12th lvl",
            13: "Bard, 13th lvl",
            14: "Master Bard",
        },

        "Bladedancer": {
            1: "Blade-Initiate",
            2: "Blade-Daughter",
            3: "Blade-Singer",
            4: "Blade-Weaver",
            5: "Blade-Sister",
            6: "Blade-Adept",
            7: "Blade-Dancer",
            8: "Blade-Priestess",
            9: "Blade-Mistress",
            10: "Blade-Mistress, 10th lvl",
            11: "Blade-Mistress, 11th lvl",
            12: "Blade-Mistress, 12th lvl",
            13: "Blade-Mistress, 13th lvl",
            14: "Mistress of All Blades",
        },

        "Paladin": {
            1: "Bulwark",
            2: "Warder",
            3: "Defender",
            4: "Protector",
            5: "Guardian",
            6: "Sentinel",
            7: "Justiciar",
            8: "Paladin",
            9: "Paladin Lord",
            10: "Paladin Lord, 10th lvl",
            11: "Paladin Lord, 11th lvl",
            12: "Paladin Lord, 12th lvl",
            13: "Paladin Lord, 13th lvl",
            14: "Lord Protector",
        },

        "Priestess": {
            1: "Novice",
            2: "Daughter",
            3: "Sister-Initiate",
            4: "Sister",
            5: "Sister-Disciple",
            6: "Priestess",
            7: "Mother",
            8: "Revered Mother",
            9: "Matriarch",
            10: "Matriarch, 10th lvl",
            11: "Matriarch, 11th lvl",
            12: "Matriarch, 12th lvl",
            13: "Matriarch, 13th lvl",
            14: "High Priestess",
        },

        "Shaman": {
            1: "Spirit Whisperer",
            2: "Village Healer",
            3: "Tribal Priest",
            4: "Medicine Man",
            5: "Totem Bearer",
            6: "Witch Doctor",
            7: "Spirit Walker",
            8: "Tribal Elder",
            9: "Shaman",
            10: "Shaman, 10th lvl",
            11: "Shaman, 11th lvl",
            12: "Shaman, 12th lvl",
            13: "Shaman, 13th lvl",
            14: "Grandfather of Totems",
        },

        "Warlock": {
            1: "Medium",
            2: "Occultist",
            3: "Spiritualist",
            4: "Hexgiver",
            5: "Cursebringer",
            6: "Maleficus",
            7: "Infernalist",
            8: "Warlock",
            9: "Dread Lord",
            10: "Dread Lord, 10th lvl",
            11: "Dread Lord, 11th lvl",
            12: "Dread Lord, 12th lvl",
            13: "Dread Lord, 13th lvl",
            14: "Dread King",
        },

        "Witch": {
            1: "Initiate",
            2: "Seeress",
            3: "Siren",
            4: "Pythoness",
            5: "Sibyl",
            6: "Enchantress",
            7: "Sorceress",
            8: "Incantrix",
            9: "Witch",
            10: "Witch, 10th lvl",
            11: "Witch, 11th lvl",
            12: "Witch, 12th lvl",
            13: "Witch, 13th lvl",
            14: "Witch Queen",
        },

        "Dwarven Craftpriest": {
            1: "Craft-Catechist",
            2: "Craft-Acolyte",
            3: "Craft-Priest",
            4: "Craft-Curate",
            5: "Craft-Vicar",
            6: "Craft-Rector",
            7: "Craft-Prelate",
            8: "Craft-Bishop",
            9: "Craft-Lord",
            10: "Craft-Lord, 10th lvl",
        },

        "Dwarven Vaultguard": {
            1: "Sentry",
            2: "Warden",
            3: "Shieldbearer",
            4: "Defender",
            5: "Sentinel",
            6: "Guardian",
            7: "Champion",
            8: "Vaultguard",
            9: "Vaultlord",
            10: "Vaultlord, 10th lvl",
            11: "Vaultlord, 11th lvl",
            12: "Vaultlord, 12th lvl",
            13: "Vaultlord, 13th lvl",
        },

        "Elven Nightblade": {
            1: "Arcanist-Avenger",
            2: "Seer-Enforcer",
            3: "Theurgist-Torturer",
            4: "Magician-Slayer",
            5: "Thaumaturge-Destroyer",
            6: "Enchanter-Executioner",
            7: "Sorcerer-Blackguard",
            8: "Mage-Assassin",
            9: "Nightblade",
            10: "Nightblade, 10th lvl",
            11: "Nightblade, 11th lvl",
        },

        "Elven Spellsword": {
            1: "Arcanist-Guardian",
            2: "Warrior-Seer",
            3: "Theurgist-Swordmaster",
            4: "Magician-Hero",
            5: "Thaumaturge-Exemplar",
            6: "Myrmidon-Enchanter",
            7: "Sorcerer-Champion",
            8: "Epic Hero-Mage",
            9: "Wizard-Lord",
            10: "Wizard-Lord, 10th lvl",
            11: "Wizard-Lord, 11th lvl",
        },

        "Nobiran Wonderworker": {
            1: "Divine Arcanist",
            2: "Divine Seer",
            3: "Divine Theurgist",
            4: "Divine Magician",
            5: "Divine Thaumaturge",
            6: "Divine Enchanter",
            7: "Divine Sorcerer",
            8: "Divine Mage",
            9: "Divine Wizard",
            10: "Divine Wizard, 10th lvl",
            11: "Divine Wizard, 11th lvl",
            12: "Divine Wizard, 12th lvl",
        },

        "Zaharan Ruinguard": {
            1: "Insignificant",
            2: "Ruinborn",
            3: "Ruinchild",
            4: "Son of Ruin",
            5: "Ruinwielder",
            6: "Ruinscourge",
            7: "Ruinmaster",
            8: "Father of Ruin",
            9: "Lord of Ruin",
            10: "Lord of Secrets",
            11: "Lord of Bindings",
            12: "Prince of Ruin",
        },
    }


    def get_class_title(final_class, level):
        titles = class_titles[final_class]
        if level in titles:
            return titles[level]
        return titles[max(titles.keys())]


    class_title = get_class_title(final_class, level)

    # -----------------------
    # 3. PRIME REQUISITES & EXTRA REQUIREMENTS
    # -----------------------

    prime_requisites = {
        "Fighter": ["STR"],
        "Explorer": ["CON"],
        "Thief": ["DEX"],
        "Mage": ["INT"],
        "Crusader": ["WIL"],
        "Venturer": ["CHA"],
        "Assassin": ["STR", "DEX"],
        "Barbarian": ["STR", "CON"],
        "Bard": ["DEX", "CHA"],
        "Bladedancer": ["WIL", "DEX"],
        "Paladin": ["STR", "CHA"],
        "Priestess": ["WIL", "CHA"],
        "Shaman": ["WIL", "CON"],
        "Warlock": ["INT", "WIL"],
        "Witch": ["INT", "WIL"],
        "Dwarven Craftpriest": ["WIL"],
        "Dwarven Vaultguard": ["STR"],
        "Elven Nightblade": ["DEX", "INT"],
        "Elven Spellsword": ["STR", "INT"],
        "Nobiran Wonderworker": ["INT", "WIL"],
        "Zaharan Ruinguard": ["STR", "INT"],
    }


    def meets_prime_requisites(pc_class, stats):
        return all(stats[pr] >= 9 for pr in prime_requisites[pc_class])


    def extra_requirements(pc_class, stats):
        if pc_class == "Nobiran Wonderworker":
            return all(v >= 11 for v in stats.values())
        if pc_class in ("Dwarven Craftpriest", "Dwarven Vaultguard"):
            return stats["CON"] >= 9
        if pc_class == "Zaharan Ruinguard":
            return stats["INT"] >= 9 and stats["WIL"] >= 9 and stats["CHA"] >= 9
        return True

    # Reroll stats until the character is eligible for the chosen class
    while not (meets_prime_requisites(final_class, stats) and extra_requirements(final_class, stats)):
        stats = generate_attributes()


    # -----------------------
    # HIT DICE I HP
    # -----------------------

    hit_dice = {
        "Fighter": 8,
        "Explorer": 6,
        "Thief": 4,
        "Mage": 4,
        "Crusader": 6,
        "Venturer": 6,
        "Assassin": 6,
        "Barbarian": 8,
        "Bard": 4,
        "Bladedancer": 6,
        "Paladin": 8,
        "Priestess": 4,
        "Shaman": 6,
        "Warlock": 4,
        "Witch": 4,
        "Dwarven Craftpriest": 6,
        "Dwarven Vaultguard": 8,
        "Elven Nightblade": 6,
        "Elven Spellsword": 6,
        "Nobiran Wonderworker": 4,
        "Zaharan Ruinguard": 6,
    }


    def con_modifier(CON):
        if CON == 3: return -3
        if 4 <= CON <= 5: return -2
        if 6 <= CON <= 8: return -1
        if 9 <= CON <= 12: return 0
        if 13 <= CON <= 15: return +1
        if 16 <= CON <= 17: return +2
        if CON == 18: return +3


    def roll_hp_level1(pc_class, CON):
        hd = hit_dice[pc_class]
        con_mod = con_modifier(CON)
        raw_roll = random.randint(1, hd)
        if raw_roll < 4:
            raw_roll = 4
        hp = max(1, raw_roll + con_mod)
        return hp, raw_roll, con_mod


    # -----------------------
    # CECHY FIZYCZNE
    # -----------------------

    # --- DEFINICJE CECH FIZYCZNYCH ---

    negative_features = [
        "Build - Obese",
        "Build - Hunchback",
        "Build - Skeletal",
        "Ears - Crumpled",
        "Ears - Huge",
        "Ears - Missing",
        "Ears - Torn",
        "Eyes - Bulging",
        "Eyes - Cross-Eyed",
        "Eyes - One Eye (Mass Scar Tissue)",
        "Eyes - One Eye (Stitched Up)",
        "Eyes - Wall-Eyed",
        "Eyes - Wandering Eyes",
        "Hands - Misshapen",
        "Hands - Missing Many Fingers",
        "Face - Badly Burned",
        "Face - Chinless",
        "Face - Disfiguring Facial Scar",
        "Face - Patchy Facial Hair",
        "Face - Wispy Facial Hair",
        "Hair - Dirty/Greasy",
        "Hair - Lank and Thin",
        "Hair - Lice-Ridden",
        "Hair - Tangled/Knotted",
        "Legs - Club Foot",
        "Legs - Misshapen",
        "Mouth - Constantly Drooling",
        "Mouth - Discolored Teeth",
        "Mouth - Filed Teeth",
        "Mouth - Frog-Like",
        "Mouth - Huge Overbite",
        "Mouth - Huge Underbite",
        "Mouth - Large Buck Teeth",
        "Mouth - Large Snaggletooth",
        "Mouth - Missing Many Teeth",
        "Mouth - Toothless",
        "Nose - Encrusted",
        "Nose - Huge",
        "Nose - Smashed",
        "Nose - Missing",
        "Nose - Warty",
        "Skin - Covered in Boils",
        "Skin - Covered in Scarification",
        "Skin - Covered in Crude Tattoos",
        "Skin - Heavily Scarred",
        "Skin - Filthy",
        "Skin - Peeling",
        "Skin - Scabrous",
        "Skin - Pock Marked",
        "Skin - Warty",
    ]

    average_features = [
        "Build - Barrel-Chested",
        "Build - Chubby",
        "Build - Skinny",
        "Build - Stocky",
        "Build - Tiny",
        "Ears - Large",
        "Ears - Small",
        "Eyes - Different Colors",
        "Eyes - Large",
        "Eyes - Narrow",
        "Eyes - One Eye (Eye Patch)",
        "Eyes - Unusual Color",
        "Face - Heavy Frown/Laugh Lines",
        "Face - Obvious Birthmark",
        "Face - Obvious Mole",
        "Face - Piercing",
        "Face - Tattooed",
        "Hair - Mallen Streak",
        "Hair - Prematurely Greying",
        "Hair - Receding/Thin",
        "Hands - Callused",
        "Hands - Long Nails",
        "Hands - Missing Finger",
        "Hands - Missing Hand (Capped)",
        "Hands - Missing Hand (Carved Prosthetic)",
        "Hands - Missing Hand (Hook)",
        "Hands - Tattooed Knuckles (e.g. Hold/Fast, Love/Hate)",
        "Legs - Peg Leg",
        "Legs - Skinny",
        "Legs - Short",
        "Mouth - Deviated Septum",
        "Mouth - Diastema",
        "Mouth - Lip Piercing",
        "Mouth - Missing Tooth",
        "Mouth - Replacement Tooth (e.g. Bone, Wood)",
        "Mouth - Thin Lips",
        "Nose - Aquiline",
        "Nose - Broken",
        "Nose - Large",
        "Nose - Pierced",
        "Nose - Small",
        "Nose - Upturned",
        "Skin - Deeply Tanned",
        "Skin - Freckled",
        "Skin - Hirsute",
        "Skin - Minor Scars",
        "Skin - Ruddy",
        "Skin - Tattooed",
        "Skin - Unusually Pale",
        "Skin - Weather-Beaten",
    ]

    positive_features = [
        "Build - Athletic",
        "Build - Broad-Chested/Bosomy",
        "Build - Good Posture",
        "Build - Slim",
        "Build - Well-Proportioned",
        "Eyes - Clear",
        "Eyes - Commanding Gaze",
        "Eyes - Mesmerizing Gaze",
        "Eyes - Piercing Gaze",
        "Eyes - Striking Color",
        "Hands - Graceful",
        "Hands - Strong",
        "Face - Beauty Spot",
        "Face - Dashing Facial Scar",
        "Face - Distinguished Features",
        "Face - Chiseled/Fine Features",
        "Face - Heroic/Graceful Jawline",
        "Face - Honest",
        "Face - Striking/Beautifying Tattoo",
        "Face - Youthful Countenance",
        "Hair - Glossy",
        "Hair - Lustrous",
        "Hair - Luxurious/Silken",
        "Legs - Long",
        "Legs - Muscular/Well-Toned",
        "Legs - Slim",
        "Mouth - Charming/Winning Smile",
        "Mouth - Dazzling Smile",
        "Mouth - Full/Sensuous Lips",
        "Mouth - Perfect Teeth",
        "Skin - Flawless",
        "Skin - Glossy",
        "Skin - Healthy Complexion",
        "ROLL_TWICE"  # 00 on table
    ]

    # 1) Pobierz CHA z wygenerowanych atrybutów
    CHA = stats["CHA"]

    # 2) Określ liczbę i rodzaj cech na podstawie CHA
    if CHA == 3:
        feature_type = "negative"
        num_features = 3
    elif 4 <= CHA <= 5:
        feature_type = "negative"
        num_features = 2
    elif 6 <= CHA <= 8:
        feature_type = "negative"
        num_features = 1
    elif 9 <= CHA <= 12:
        feature_type = "average"
        num_features = 1
    elif 13 <= CHA <= 15:
        feature_type = "positive"
        num_features = 1
    elif 16 <= CHA <= 17:
        feature_type = "positive"
        num_features = 2
    elif CHA == 18:
        feature_type = "positive"
        num_features = 3


    # 3) Funkcja uwzględniająca ROLL_TWICE
    def pick_positive_features(num):
        picked = []

        while len(picked) < num:
            feat = random.choice(positive_features)

            if feat == "ROLL_TWICE":
                # dwie dodatkowe cechy (bez ROLL_TWICE)
                sub1 = random.choice(positive_features[:-1])
                sub2 = random.choice(positive_features[:-1])
                picked.extend([sub1, sub2])
            else:
                picked.append(feat)

        return picked[:num]


    # 4) Losowanie właściwych cech (główna pula)
    if feature_type == "negative":
        features = random.sample(negative_features, num_features)
    elif feature_type == "average":
        features = random.sample(average_features, num_features)
    else:
        features = pick_positive_features(num_features)


    # 5) Dodatkowy average feature, jeśli CHA ma modyfikator (− lub +)

    def cha_modifier(score):
        if score == 3:
            return -3
        elif 4 <= score <= 5:
            return -2
        elif 6 <= score <= 8:
            return -1
        elif 9 <= score <= 12:
            return 0
        elif 13 <= score <= 15:
            return +1
        elif 16 <= score <= 17:
            return +2
        elif score == 18:
            return +3


    cha_mod = cha_modifier(CHA)

    if cha_mod != 0:
        extra_avg = random.choice(average_features)
        features.append(extra_avg)





    # ALIGNMENT

    def roll_alignment(final_class):
        """Losuje alignment biorąc pod uwagę ograniczenia klasowe."""

        # 1) Najpierw normalny rzut:
        roll = random.randint(1, 6)
        if roll <= 2:
            alignment = "Lawful"
        elif roll <= 5:
            alignment = "Neutral"
        else:
            alignment = "Chaotic"

        # 2) Ograniczenia klasowe:

        # Paladin → zawsze Lawful
        if final_class == "Paladin":
            return "Lawful"

        # Crusader / Bladedancer / Priestess:
        # tylko Lawful lub Chaotic (Neutral odpada)
        if final_class in ("Crusader", "Bladedancer", "Priestess"):
            if alignment == "Neutral":
                return random.choice(["Lawful", "Chaotic"])
            return alignment

        # Warlock → nie może być Lawful
        if final_class == "Warlock":
            if alignment == "Lawful":
                return random.choice(["Neutral", "Chaotic"])
            return alignment

        # 3) Pozostałe klasy → bez zmian
        return alignment


    # GENERAL PROFICIENCIES

    general_proficiencies = [
        "Alchemy",
        "Animal Husbandry",
        "Animal Training",
        "Art",
        "Bargaining",
        "Caving",
        "Collegiate Wizardry",
        "Craft",
        "Diplomacy",
        "Disguise",
        "Driving",
        "Endurance",
        "Engineering",
        "Folkways",
        "Gambling",
        "Healing",
        "Intimidation",
        "Knowledge",
        "Labor",
        "Language",
        "Leadership",
        "Lip Reading",
        "Manual of Arms",
        "Mapping",
        "Military Strategy",
        "Mimicry",
        "Mountaineering",
        "Naturalism",
        "Navigation",
        "Performance",
        "Profession",
        "Revelry",
        "Riding",
        "Seafaring",
        "Seduction",
        "Siege Engineering",
        "Signaling",
        "Streetwise",
        "Survival",
        "Swimming",
        "Theology",
        "Tracking",
        "Trapping",
    ]

    general_proficiency_limits = {
        "Alchemy": 3,
        "Animal Husbandry": 1,
        "Animal Training": 1,
        "Art": None,
        "Craft": None,
        "Bargaining": None,
        "Caving": None,
        "Collegiate Wizardry": None,
        "Driving": 1,
        "Diplomacy": 1,
        "Disguise": None,
        "Endurance": 1,
        "Engineering": None,
        "Folkways": None,
        "Gambling": None,
        "Healing": 3,
        "Intimidation": 1,
        "Knowledge": None,
        "Labor": None,
        "Language": None,
        "Leadership": 1,
        "Lip Reading": 1,
        "Mapping": None,
        "Manual of Arms": 3,
        "Military Strategy": 3,
        "Mimicry": None,
        "Mountaineering": 1,
        "Naturalism": None,
        "Navigation": 1,
        "Performance": None,
        "Profession": None,
        "Revelry": 1,
        "Riding": 1,
        "Seafaring": 3,
        "Seduction": 1,
        "Siege Engineering": 2,
        "Signaling": None,
        "Streetwise": None,
        "Survival": 1,
        "Theology": None,
        "Tracking": None,
        "Trapping": 1,
        "Swimming": 1,
    }

    proficiency_limits = {
        "Alchemy": 3,
        "Animal Husbandry": 1,
        "Animal Training": 1,
        "Art": None,
        "Craft": None,
        "Bargaining": None,
        "Caving": None,
        "Collegiate Wizardry": None,
        "Driving": 1,
        "Diplomacy": 1,
        "Disguise": None,
        "Endurance": 1,
        "Engineering": None,
        "Folkways": None,
        "Gambling": None,
        "Healing": 3,
        "Intimidation": 1,
        "Knowledge": None,
        "Labor": None,
        "Language": None,
        "Leadership": 1,
        "Lip Reading": 1,
        "Mapping": None,
        "Manual of Arms": 3,
        "Military Strategy": 3,
        "Mimicry": None,
        "Mountaineering": 1,
        "Naturalism": None,
        "Navigation": 1,
        "Performance": None,
        "Profession": None,
        "Revelry": 1,
        "Riding": 1,
        "Seafaring": 3,
        "Seduction": 1,
        "Siege Engineering": 2,
        "Signaling": None,
        "Streetwise": None,
        "Survival": 1,
        "Theology": None,
        "Tracking": None,
        "Trapping": 1,
        "Swimming": 1,
        "Adventuring": None,  # każda postać to ma zawsze
        # tu dodasz limity dla class proficiencies również:
        "Acrobatics": 1,
        "Alertness": 1,
        "Ambushing": 1,
        "Arcane Dabbling": 1,
        "Armor Training": 1,
        "Battle Magic": 1,
        "Beast Friendship": 1,
        "Berserkergang": 1,
        "Black Lore of Zahar": 1,
        "Blind Fighting": 1,
        "Bright Lore of Aura": 1,
        "Cat Burglary": 1,
        "Climbing": 1,
        "Combat Ferocity": 1,
        "Combat Reflexes": 1,

        # Combat Trickery — JUŻ ROZBITE
        "Combat Trickery (Disarm)": 1,
        "Combat Trickery (Force Back)": 1,
        "Combat Trickery (Incapacitate)": 1,
        "Combat Trickery (Knock Down)": 1,
        "Combat Trickery (Overrun)": 1,
        "Combat Trickery (Sunder)": 1,
        "Combat Trickery (Wrestling)": 1,

        "Command": 1,
        "Contemplation": 1,
        "Contortionism": 1,
        "Counterspelling": 1,
        "Divine Blessing": 1,
        "Divine Health": 1,
        "Dungeonbashing Expertise": 1,
        "Dwarven Brewing": 1,
        "Eavesdropping": 1,
        "Elementalism": 4,
        "Expanded Repertoire": 1,
        "Experimenting": 1,
        "Familiar": 1,
        "Fighting Style Specialization": 5,
        "Goblin-slaying": 1,
        "Illusion Resistance": 1,
        "Kin-slaying": 1,
        "Land Surveying": 1,
        "Laying on Hands": None,
        "Lockpicking Expertise": 1,
        "Loremastery": 1,
        "Magical Engineering": None,
        "Magical Music": None,
        "Martial Training": 7,
        "Mastery of Conjuration & Summoning": 1,
        "Mastery of Enchantments & Illusions": 1,
        "Mounted Combat": 1,
        "Mystic Aura": 1,
        "Passing without Trace": 1,
        "Poisoning": 1,
        "Precise Shooting": 3,
        "Prestidigitation": 1,
        "Prophecy": 1,
        "Prospecting": 1,
        "Quiet Magic": 1,
        "Reliquarianism": 1,
        "Righteous Rebuke": 1,
        "Running": 1,
        "Sensing Evil": 1,
        "Sensing Good": 1,
        "Sensing Power": 1,
        "Skirmishing": 1,
        "Skulking": 1,
        "Sniping": 1,
        "Soothsaying": 1,
        "Swashbuckling": 1,
        "Syncretism": 1,
        "Transmogrification": 1,
        "Trapfinding": 1,
        "Unarmed Fighting": 1,
        "Unflappable Casting": 1,
        "Vermin-slaying": 1,
        "Wakefulness": 1,
        "Weapon Finesse": 1,
        "Weapon Focus": 7
    }

    # KLASOWE PROFKI

    class_proficiency_lists = {
        "Assassin": [
            "Acrobatics", "Alchemy", "Alertness", "Arcane Dabbling",
            "Armor Training", "Bribery", "Cat Burglary", "Climbing",
            "Combat Reflexes", "Combat Trickery (Disarm)",
            "Combat Trickery (Incapacitate)", "Contortionism", "Disguise",
            "Eavesdropping", "Fighting Style Specialization", "Gambling",
            "Intimidation", "Kin-slaying", "Mimicry", "Poisoning",
            "Precise Shooting", "Running", "Skirmishing", "Skulking",
            "Sniping", "Swashbuckling", "Weapon Finesse", "Weapon Focus"
        ],

        "Barbarian": [
            "Alertness", "Ambushing", "Armor Training", "Beast Friendship",
            "Berserkergang", "Blind Fighting", "Climbing", "Combat Ferocity",
            "Combat Reflexes", "Combat Trickery (Force Back)",
            "Combat Trickery (Knock Down)", "Combat Trickery (Overrun)",
            "Combat Trickery (Wrestling)", "Command",
            "Fighting Style Specialization", "Martial Training",
            "Mountaineering", "Mounted Combat", "Passing without Trace",
            "Precise Shooting", "Riding", "Running", "Seafaring",
            "Skirmishing", "Sniping", "Swashbuckling",
            "Weapon Finesse", "Weapon Focus"
        ],

        "Bard": [
            "Acrobatics", "Art", "Bargaining", "Beast Friendship", "Bribery",
            "Combat Trickery (Disarm)", "Command", "Diplomacy",
            "Elven Bloodline", "Fighting Style Specialization", "Healing",
            "Knowledge", "Language", "Leadership", "Lip Reading",
            "Magical Engineering", "Magical Music", "Mimicry", "Mystic Aura",
            "Performance", "Precise Shooting", "Prestidigitation", "Running",
            "Seduction", "Skirmishing", "Swashbuckling", "Weapon Finesse",
            "Weapon Focus"
        ],

        "Bladedancer": [
            "Acrobatics", "Battle Magic", "Beast Friendship",
            "Combat Reflexes", "Combat Trickery (Disarm)",
            "Combat Trickery (Knock Down)", "Contemplation", "Diplomacy",
            "Divine Blessing", "Divine Health", "Elven Bloodline",
            "Fighting Style Specialization", "Laying on Hands",
            "Magical Music", "Martial Training", "Mounted Combat",
            "Mystic Aura", "Prestidigitation", "Prophecy", "Quiet Magic",
            "Running", "Seduction", "Skirmishing", "Swashbuckling",
            "Syncretism", "Unarmed Fighting", "Unflappable Casting",
            "Weapon Focus"
        ],

        "Crusader": [
            "Battle Magic", "Beast Friendship",
            "Combat Trickery (Force Back)", "Combat Trickery (Overrun)",
            "Combat Trickery (Sunder)", "Command", "Contemplation",
            "Diplomacy", "Divine Blessing", "Divine Health",
            "Fighting Style Specialization", "Healing", "Laying on Hands",
            "Leadership", "Loremastery", "Magical Engineering",
            "Martial Training", "Mounted Combat", "Prestidigitation",
            "Prophecy", "Quiet Magic", "Righteous Rebuke",
            "Sensing Evil", "Sensing Power", "Syncretism", "Theology",
            "Unflappable Casting", "Weapon Focus"
        ],

        "Dwarven Craftpriest": [
            "Alchemy", "Battle Magic", "Caving", "Collegiate Wizardry",
            "Contemplation", "Craft", "Diplomacy", "Divine Blessing",
            "Divine Health", "Dwarven Brewing", "Engineering",
            "Expanded Repertoire", "Experimenting",
            "Fighting Style Specialization", "Goblin-slaying", "Healing",
            "Illusion Resistance", "Knowledge", "Laying on Hands",
            "Loremastery", "Magical Engineering", "Mapping",
            "Prestidigitation", "Profession (judge)", "Prophecy",
            "Quiet Magic", "Reliquarianism", "Righteous Rebuke",
            "Sensing Evil", "Siege Engineering", "Theology",
            "Unflappable Casting", "Weapon Focus"
        ],

        "Dwarven Vaultguard": [
            "Alertness", "Berserkergang", "Blind Fighting", "Caving",
            "Combat Ferocity", "Combat Reflexes",
            "Combat Trickery (Force Back)", "Combat Trickery (Knock Down)",
            "Combat Trickery (Overrun)", "Combat Trickery (Sunder)",
            "Combat Trickery (Wrestling)", "Command",
            "Dungeonbashing Expertise", "Dwarven Brewing",
            "Fighting Style Specialization", "Goblin-slaying",
            "Illusion Resistance", "Intimidation", "Land Surveying",
            "Leadership", "Military Strategy", "Mountaineering",
            "Precise Shooting", "Prospecting", "Running",
            "Siege Engineering", "Vermin-slaying", "Weapon Focus"
        ],

        "Elven Nightblade": [
            "Battle Magic", "Beast Friendship", "Black Lore of Zahar",
            "Blind Fighting", "Combat Reflexes", "Contortionism",
            "Counterspelling", "Eavesdropping", "Elementalism",
            "Expanded Repertoire", "Familiar",
            "Fighting Style Specialization", "Kin-slaying",
            "Magical Engineering", "Mastery of Enchantments & Illusions",
            "Mystic Aura", "Passing without Trace", "Poisoning",
            "Precise Shooting", "Prestidigitation", "Running",
            "Sensing Power", "Skirmishing", "Skulking", "Sniping",
            "Swashbuckling", "Unflappable Casting", "Unarmed Fighting",
            "Wakefulness", "Weapon Focus", "Weapon Finesse"
        ],

        "Elven Spellsword": [
            "Battle Magic", "Beast Friendship", "Black Lore of Zahar",
            "Blind Fighting", "Combat Reflexes",
            "Combat Trickery (Disarm)", "Combat Trickery (Knock Down)",
            "Command", "Counterspelling", "Elementalism",
            "Expanded Repertoire", "Experimenting", "Familiar",
            "Fighting Style Specialization", "Loremastery",
            "Magical Engineering", "Magical Music",
            "Mastery of Enchantments & Illusions", "Mounted Combat",
            "Mystic Aura", "Quiet Magic", "Precise Shooting",
            "Prestidigitation", "Running", "Sensing Power",
            "Skirmishing", "Soothsaying", "Swashbuckling",
            "Unflappable Casting", "Wakefulness",
            "Weapon Focus", "Weapon Finesse"
        ],

        "Explorer": [
            "Beast Friendship", "Climbing", "Combat Reflexes",
            "Combat Ferocity", "Combat Trickery (Disarm)",
            "Combat Trickery (Knock Down)", "Driving", "Eavesdropping",
            "Elven Bloodline", "Fighting Style Specialization",
            "Illusion Resistance", "Land Surveying", "Mapping",
            "Mountaineering", "Mounted Combat", "Naturalism",
            "Navigation", "Passing without Trace", "Precise Shooting",
            "Prospecting", "Riding", "Running", "Seafaring",
            "Skirmishing", "Sniping", "Swashbuckling",
            "Weapon Finesse", "Weapon Focus"
        ],

        "Fighter": [
            "Acrobatics", "Alertness", "Berserkergang", "Blind Fighting",
            "Combat Ferocity", "Combat Reflexes",
            "Combat Trickery (Disarm)", "Combat Trickery (Force Back)",
            "Combat Trickery (Knock Down)", "Combat Trickery (Overrun)",
            "Combat Trickery (Sunder)", "Combat Trickery (Wrestling)",
            "Command", "Dungeonbashing Expertise",
            "Fighting Style Specialization", "Leadership", "Manual of Arms",
            "Military Strategy", "Mounted Combat", "Precise Shooting",
            "Riding", "Running", "Siege Engineering", "Skirmishing",
            "Swashbuckling", "Unarmed Fighting", "Weapon Finesse",
            "Weapon Focus"
        ],

        "Mage": [
            "Alchemy", "Battle Magic", "Beast Friendship",
            "Black Lore of Zahar", "Bright Lore of Aura",
            "Counterspelling", "Diplomacy", "Elementalism",
            "Elven Bloodline", "Engineering", "Expanded Repertoire",
            "Experimenting", "Familiar", "Healing", "Illusion Resistance",
            "Knowledge", "Language", "Loremastery",
            "Magical Engineering",
            "Mastery of Enchantments & Illusions",
            "Mastery of Conjuration & Summoning",
            "Mystic Aura", "Quiet Magic", "Prestidigitation",
            "Sensing Power", "Soothsaying", "Transmogrification",
            "Unflappable Casting"
        ],

        "Nobiran Wonderworker": [
            "Alchemy", "Battle Magic", "Black Lore of Zahar",
            "Beast Friendship", "Bright Lore of Aura", "Command",
            "Contemplation", "Counterspelling", "Elementalism",
            "Expanded Repertoire", "Experimenting", "Familiar", "Healing",
            "Illusion Resistance", "Laying on Hands", "Loremastery",
            "Magical Engineering", "Martial Training",
            "Mastery of Enchantments & Illusions",
            "Mastery of Conjuration & Summoning",
            "Mystic Aura", "Prestidigitation", "Prophecy", "Quiet Magic",
            "Sensing Evil", "Sensing Power", "Soothsaying",
            "Syncretism", "Transmogrification", "Unflappable Casting"
        ],

        "Paladin": [
            "Alertness", "Beast Friendship", "Berserkergang",
            "Blind Fighting", "Combat Ferocity", "Combat Reflexes",
            "Combat Trickery (Force Back)",
            "Combat Trickery (Incapacitate)",
            "Combat Trickery (Overrun)", "Combat Trickery (Sunder)",
            "Command", "Diplomacy", "Divine Blessing",
            "Dungeonbashing Expertise", "Fighting Style Specialization",
            "Goblin-slaying", "Healing", "Illusion Resistance",
            "Laying on Hands", "Leadership", "Manual of Arms",
            "Martial Training", "Military Strategy", "Mounted Combat",
            "Mystic Aura", "Riding", "Running", "Weapon Focus"
        ],

        "Priestess": [
            "Alchemy", "Animal Husbandry", "Arcane Dabbling",
            "Armor Training", "Beast Friendship", "Bright Lore of Aura",
            "Contemplation", "Divine Blessing", "Familiar", "Healing",
            "Illusion Resistance", "Knowledge", "Laying on Hands",
            "Loremastery", "Magical Engineering", "Magical Music",
            "Mastery of Enchantments & Illusions",
            "Mystic Aura", "Naturalism", "Performance",
            "Prestidigitation", "Profession", "Prophecy", "Quiet Magic",
            "Sensing Evil", "Sensing Power", "Syncretism",
            "Unflappable Casting"
        ],

        "Shaman": [
            "Animal Husbandry", "Animal Training", "Battle Magic",
            "Beast Friendship", "Berserkergang", "Command", "Diplomacy",
            "Divine Blessing", "Divine Health", "Elementalism",
            "Fighting Style Specialization", "Healing", "Laying on Hands",
            "Leadership", "Loremastery", "Magical Engineering",
            "Magical Music", "Naturalism", "Passing without Trace",
            "Prestidigitation", "Quiet Magic", "Sensing Evil",
            "Sensing Power", "Syncretism", "Theology", "Tracking",
            "Unflappable Casting", "Weapon Focus"
        ],

        "Thief": [
            "Acrobatics", "Alertness", "Arcane Dabbling", "Bribery",
            "Cat Burglary", "Combat Reflexes",
            "Combat Trickery (Disarm)",
            "Combat Trickery (Incapacitate)", "Contortionism",
            "Fighting Style Specialization", "Gambling", "Intimidation",
            "Lip Reading", "Lockpicking Expertise", "Mapping",
            "Poisoning", "Precise Shooting", "Riding", "Running",
            "Seafaring", "Skirmishing", "Skulking", "Sniping",
            "Swashbuckling", "Trapfinding", "Unarmed Fighting",
            "Weapon Finesse", "Weapon Focus"
        ],

        "Venturer": [
            "Alertness", "Ambushing", "Arcane Dabbling", "Bargaining",
            "Climbing", "Combat Reflexes",
            "Combat Trickery (Disarm)",
            "Combat Trickery (Incapacitate)", "Command", "Driving",
            "Eavesdropping", "Elven Bloodline", "Intimidation",
            "Land Surveying", "Leadership", "Lip Reading",
            "Magical Engineering", "Mapping", "Mountaineering",
            "Mounted Combat", "Passing without Trace",
            "Precise Shooting", "Prospecting", "Riding", "Running",
            "Seafaring", "Skirmishing", "Swashbuckling",
            "Weapon Finesse"
        ],

        "Warlock": [
            "Alchemy", "Battle Magic", "Beast Friendship",
            "Black Lore of Zahar", "Counterspelling", "Divine Blessing",
            "Elementalism", "Elven Bloodline", "Expanded Repertoire",
            "Experimenting", "Familiar", "Illusion Resistance",
            "Knowledge", "Language", "Loremastery",
            "Magical Engineering",
            "Mastery of Enchantments & Illusions",
            "Mastery of Conjuration & Summoning",
            "Mystic Aura", "Naturalism", "Poisoning",
            "Prestidigitation", "Quiet Magic", "Sensing Good",
            "Sensing Power", "Soothsaying", "Transmogrification",
            "Unflappable Casting"
        ],

        "Witch": [
            "Alchemy", "Arcane Dabbling", "Beast Friendship",
            "Black Lore of Zahar", "Contemplation", "Divine Blessing",
            "Divine Health", "Elementalism", "Elven Bloodline",
            "Expanded Repertoire", "Familiar", "Illusion Resistance",
            "Laying on Hands", "Loremastery", "Magical Engineering",
            "Magical Music", "Mastery of Enchantments & Illusions",
            "Mystic Aura", "Naturalism", "Passing without Trace",
            "Poisoning", "Prestidigitation", "Prophecy", "Quiet Magic",
            "Sensing Power", "Soothsaying", "Transmogrification",
            "Unflappable Casting"
        ],

        "Zaharan Ruinguard": [
            "Alertness", "Ambushing", "Battle Magic", "Berserkergang",
            "Black Lore of Zahar", "Blind Fighting", "Combat Ferocity",
            "Combat Trickery (Force Back)", "Combat Trickery (Knock Down)",
            "Combat Trickery (Overrun)", "Combat Trickery (Sunder)",
            "Command", "Dungeonbashing Expertise", "Elementalism",
            "Familiar", "Fighting Style Specialization", "Kin-slaying",
            "Leadership", "Martial Training",
            "Mastery of Conjuration & Summoning", "Military Strategy",
            "Mounted Combat", "Mystic Aura", "Sensing Good",
            "Sensing Power", "Transmogrification", "Unflappable Casting",
            "Wakefulness"
        ]
    }

    # PROFICIENCIES NA WYŻSZYCH POZIOMACH

    proficiency_progression = {
        "Assassin": {
            3: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            6: {"class": 1, "general": 0},
            9: {"class": 1, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Barbarian": {
            3: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            6: {"class": 1, "general": 0},
            9: {"class": 1, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Bard": {
            3: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            6: {"class": 1, "general": 0},
            9: {"class": 1, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Bladedancer": {
            4: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            8: {"class": 1, "general": 0},
            9: {"class": 0, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Crusader": {
            4: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            8: {"class": 1, "general": 0},
            9: {"class": 0, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Dwarven Craftpriest": {
            4: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            8: {"class": 1, "general": 0},
            9: {"class": 0, "general": 1},
        },

        "Dwarven Vaultguard": {
            3: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            6: {"class": 1, "general": 0},
            9: {"class": 1, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Elven Nightblade": {
            4: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            8: {"class": 1, "general": 0},
            9: {"class": 0, "general": 1},
        },

        "Elven Spellsword": {
            3: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            6: {"class": 1, "general": 0},
            9: {"class": 1, "general": 1},
        },

        "Explorer": {
            3: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            6: {"class": 1, "general": 0},
            9: {"class": 1, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Fighter": {
            3: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            6: {"class": 1, "general": 0},
            9: {"class": 1, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Mage": {
            5: {"class": 0, "general": 1},
            6: {"class": 1, "general": 0},
            9: {"class": 0, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Nobiran Wonderworker": {
            5: {"class": 0, "general": 1},
            6: {"class": 1, "general": 0},
            9: {"class": 0, "general": 1},
            12: {"class": 1, "general": 0},
        },

        "Paladin": {
            3: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            6: {"class": 1, "general": 0},
            9: {"class": 1, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Priestess": {
            4: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            8: {"class": 1, "general": 0},
            9: {"class": 0, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Shaman": {
            4: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            8: {"class": 1, "general": 0},
            9: {"class": 0, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Thief": {
            4: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            8: {"class": 1, "general": 0},
            9: {"class": 0, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Venturer": {
            4: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            8: {"class": 1, "general": 0},
            9: {"class": 0, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Warlock": {
            5: {"class": 0, "general": 1},
            6: {"class": 1, "general": 0},
            9: {"class": 0, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Witch": {
            4: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            8: {"class": 1, "general": 0},
            9: {"class": 0, "general": 1},
            12: {"class": 1, "general": 0},
            13: {"class": 0, "general": 1},
        },

        "Zaharan Ruinguard": {
            3: {"class": 1, "general": 0},
            5: {"class": 0, "general": 1},
            6: {"class": 1, "general": 0},
            9: {"class": 1, "general": 1},
            12: {"class": 1, "general": 0},
        },

        # np. miejsca na inne klasy
        # "Fighter": {...},
        # "Mage": {...},
    }


    def general_proficiency_bonus(INT):
        if 13 <= INT <= 15:
            return 1
        elif 16 <= INT <= 17:
            return 2
        elif INT == 18:
            return 3
        return 0


    def pick_random_proficiency(current_list):
        while True:
            prof = random.choice(list(general_proficiency_limits.keys()))
            limit = general_proficiency_limits[prof]

            # ile razy już wzięliśmy tę prof?
            count = current_list.count(prof)

            # sprawdzamy limit
            if limit is None:  # unlimited
                return prof
            elif count < limit:
                return prof
            # else: reroll until we hit allowed choice


    # LOSOWANIE GENERAL PROFICIENCY

    def generate_starting_proficiencies(INT):
        total = 1 + general_proficiency_bonus(INT)  # 1 base + INT bonus

        picked = []

        # Losujemy wszystkie poza Adventuring
        for _ in range(total):
            prof = pick_random_proficiency(picked)
            picked.append(prof)

        # Dodajemy Adventuring jako automatyczne proficiency
        picked.insert(0, "Adventuring")

        return picked


    starting_proficiencies = generate_starting_proficiencies(stats["INT"])

    # ------------------------------------------
    # PROFICIENCIES: CLASS + GENERAL (+ Adventuring)
    # ------------------------------------------

    # AUTOMATYCZNE GENERAL PROFICIENCIES DLA KLAS
    class_starting_general_proficiencies = {
        "Fighter": {
            1: {
                "auto": ["Manual of Arms"]
            }
        },

        "Explorer": {
            1: {
                "auto": ["Ambushing", "Endurance"]
            }
        },

        "Venturer": {
            1: {
                "auto": ["Diplomacy", "Bargaining"],
                "choose_one": [
                    ["Driving", "Seafaring"]  # → wybierz 1
                ]
            }
        },

        "Barbarian": {
            1: {
                "choose_group": {
                    "Jutland": ["Climbing", "Seafaring"],
                    "Skysostan": ["Precise Shooting", "Riding"],
                    "Ivory Kingdoms": ["Running", "Endurance"]
                }
            }
        },

        "Bard": {
            1: {
                "auto": ["Loremastery", "Language", "Performance"]
            }
        },

        "Bladedancer": {
            1: {
                "auto": ["Theology, Weapon Finesse"]
            }
        },

        "Paladin": {
            1: {
                "auto": ["Lay on Hands", "Manual of Arms", "Divine Health", "Sense Evil"]
            }
        },

        "Priestess": {
            1: {
                "auto": ["Diplomacy", "Lay on Hands", "Divine Health", "Theology"]
            }
        },

        "Shaman": {
            1: {
                "auto": ["Theology"]
            }
        },

        "Warlock": {
            1: {
                "auto": ["Knowledge"]
            }
        },

        "Dwarven Craftpriest": {
            1: {
                "auto": ["Craft", "Theology"]
            }
        },

        "Dwarven Vaultguard": {
            1: {
                "auto": ["Manual of Arms"]
            }
        },

        "Elven Nightblade": {
            1: {
                "auto": ["Acrobatics", "Streetwise"]
            },
            2: {
                "auto": ["Quiet Magic"]
            },
        },

        "Mage": {
            1: {
                "auto": ["Collegiate Wizardry"]
            }
        },

        "Elven Spellsword": {
            1: {
                "auto": ["Collegiate Wizardry"]
            }
        },

        "Nobiran Wonderworker": {
            1: {
                "auto": ["Collegiate Wizardry", "Lay on Hands", "Divine Health"]
            }
        },

        "Zaharan Ruinguard": {
            1: {
                "auto": ["Manual of Arms", "Weapon Focus"]
            }
        },

    }


    # --- helper: sprawdzanie limitów i dodawanie profek ---
    def can_take_proficiency(prof_name, char_profs, limits):
        limit = limits.get(prof_name, None)
        current = char_profs.get(prof_name, 0)
        return limit is None or current < limit


    def add_proficiency(prof_name, char_profs, limits):
        if not can_take_proficiency(prof_name, char_profs, limits):
            return False
        char_profs[prof_name] = char_profs.get(prof_name, 0) + 1
        return True


    character_proficiencies = {}  # nazwa → liczba razy wybrana
    proficiency_log = []


    # --- helper: sprawdzanie limitów i dodawanie profek ---
    def can_take_proficiency(prof_name, char_profs, limits):
        limit = limits.get(prof_name, None)
        current = char_profs.get(prof_name, 0)
        return limit is None or current < limit


    def add_proficiency(prof_name, char_profs, limits):
        if not can_take_proficiency(prof_name, char_profs, limits):
            return False
        char_profs[prof_name] = char_profs.get(prof_name, 0) + 1
        return True


    # --- FUNKCJA AUTO-PROFKI, DZIAŁA NA DOWOLNYCH POZIOMACH ---
    def apply_auto_proficiencies(final_class, level, char_profs, limits):
        gained = []
        table = class_starting_general_proficiencies.get(final_class, {})

        for lvl, entry in table.items():
            if level < lvl:
                continue

            # 1) AUTO – proste, zawsze wchodzą
            for prof in entry.get("auto", []):
                if add_proficiency(prof, char_profs, limits):
                    gained.append((lvl, "auto", prof))

            # 2) CHOOSE_ONE – np. Venturer: wybierz 1 z każdej grupy
            for group in entry.get("choose_one", []):
                chosen = random.choice(group)
                if add_proficiency(chosen, char_profs, limits):
                    gained.append((lvl, "choose_one", chosen))

            # 3) CHOOSE_GROUP – np. Barbarian: losujemy region, bierzemy cały pakiet
            group_table = entry.get("choose_group")
            if group_table:
                chosen_region = random.choice(list(group_table.keys()))
                for prof in group_table[chosen_region]:
                    if add_proficiency(prof, char_profs, limits):
                        gained.append((lvl, "choose_group", prof))

        return gained


    auto_general_log = apply_auto_proficiencies(
        final_class,
        level,
        character_proficiencies,
        proficiency_limits
    )


    # ---- helper: INT bonuses ----

    def general_proficiency_bonus(INT):
        if 13 <= INT <= 15:
            return 1
        if 16 <= INT <= 17:
            return 2
        if INT == 18:
            return 3
        return 0


    # ---- helper: can take ----

    # def can_take_proficiency(prof_name, char_profs, limits):
    # limit = limits.get(prof_name, None)  # None = unlimited
    # current = char_profs.get(prof_name, 0)
    # if limit is None:
    # return True
    # return current < limit


    # ---- helper: add proficiency ----

    # def add_proficiency(prof_name, char_profs, limits):
    # if not can_take_proficiency(prof_name, char_profs, limits):
    # return False
    # char_profs[prof_name] = char_profs.get(prof_name, 0) + 1
    # return True

    def pick_limited_from_pool(pool, char_profs):
        """Losuje proficiency z puli respektując limity."""
        random.shuffle(pool)
        for prof in pool:
            if can_take_proficiency(prof, char_profs, proficiency_limits):
                char_profs[prof] = char_profs.get(prof, 0) + 1
                return prof
        return None


    # --- AUTOMATYCZNE GENERAL PROFICIENCIES WEDŁUG POZIOMU ---

    def apply_level_proficiencies(final_class, level, char_profs):
        """
        Nadaje proficiencies z rozpiski levelowej i zwraca log:
        [ (poziom, "class"/"general", nazwa_proficiency), ... ]
        """
        gained_log = []

        if final_class not in proficiency_progression:
            return gained_log  # brak rozpiski → nic nie robić

        prog = proficiency_progression[final_class]

        for lvl in range(2, level + 1):
            if lvl not in prog:
                continue

            entry = prog[lvl]

            # --- CLASS PROFICIENCIES ---
            for _ in range(entry.get("class", 0)):
                pool = class_proficiency_lists[final_class]
                prof = pick_limited_from_pool(pool, char_profs)
                if prof:
                    gained_log.append((lvl, "class", prof))

            # --- GENERAL PROFICIENCIES ---
            for _ in range(entry.get("general", 0)):
                pool = general_proficiencies
                prof = pick_limited_from_pool(pool, char_profs)
                if prof:
                    gained_log.append((lvl, "general", prof))

        return gained_log


    # ---- 1. CLASS PROFICIENCY (1 sztuka) ----

    def choose_class_proficiency(final_class, char_profs):
        options = class_proficiency_lists[final_class][:]
        random.shuffle(options)

        for prof in options:
            if add_proficiency(prof, char_profs, proficiency_limits):
                return prof
        return None


    class_prof = choose_class_proficiency(final_class, character_proficiencies)

    # ---- 2. GENERAL PROFICIENCIES (1 + INT bonus) ----

    general_slots = 1 + general_proficiency_bonus(stats["INT"])
    general_picks = []

    pool = general_proficiencies[:]  # to jest prawidłowa pula general profek
    random.shuffle(pool)

    for prof in pool:
        if len(general_picks) >= general_slots:
            break
        if add_proficiency(prof, character_proficiencies, proficiency_limits):
            general_picks.append(prof)

    # ---- 3. ADVENTURING — automatyczne, ale pokazujemy razem z general ----

    add_proficiency("Adventuring", character_proficiencies, proficiency_limits)
    general_picks.append("Adventuring")  # pokazujemy w grupie general

    # -------------------------------
    # APPLY PROFICIENCY PROGRESSION
    # -------------------------------

    level_gains_log = apply_level_proficiencies(final_class, level, character_proficiencies)

    # LOSOWANIE ALIGNMENT

    alignment = roll_alignment(final_class)

    # HP

    # -------------------------------
    # FULL ACKS HP PROGRESSION SYSTEM
    # -------------------------------

    # Każda klasa → hit die type
    hit_die_type = {
        "Fighter": 8,
        "Explorer": 6,
        "Thief": 4,
        "Mage": 4,
        "Crusader": 6,
        "Venturer": 6,
        "Assassin": 6,
        "Barbarian": 8,
        "Bard": 4,
        "Bladedancer": 6,
        "Paladin": 8,
        "Priestess": 4,
        "Shaman": 6,
        "Warlock": 4,
        "Witch": 4,
        "Dwarven Craftpriest": 6,
        "Dwarven Vaultguard": 8,
        "Elven Nightblade": 6,
        "Elven Spellsword": 6,
        "Nobiran Wonderworker": 4,
        "Zaharan Ruinguard": 6,
    }

    # Poziomy 10–14 → bonus fixed (po 9 HD)
    post_9_bonus = {
        # Fighter, d8
        ("Fighter", 10): 2, ("Fighter", 11): 4, ("Fighter", 12): 6, ("Fighter", 13): 8, ("Fighter", 14): 10,

        # Explorer, d6
        ("Explorer", 10): 2, ("Explorer", 11): 4, ("Explorer", 12): 6, ("Explorer", 13): 8, ("Explorer", 14): 10,

        # Thief, d4
        ("Thief", 10): 2, ("Thief", 11): 4, ("Thief", 12): 6, ("Thief", 13): 8, ("Thief", 14): 10,

        # Mage, d4
        ("Mage", 10): 1, ("Mage", 11): 2, ("Mage", 12): 3, ("Mage", 13): 4, ("Mage", 14): 5,

        # Crusader, d6
        ("Crusader", 10): 1, ("Crusader", 11): 2, ("Crusader", 12): 3, ("Crusader", 13): 4, ("Crusader", 14): 5,

        # Venturer, d6
        ("Venturer", 10): 2, ("Venturer", 11): 4, ("Venturer", 12): 6, ("Venturer", 13): 8, ("Venturer", 14): 10,

        # Assassin, d6
        ("Assassin", 10): 2, ("Assassin", 11): 4, ("Assassin", 12): 6, ("Assassin", 13): 8, ("Assassin", 14): 10,

        # Barbarian, d8
        ("Barbarian", 10): 2, ("Barbarian", 11): 4, ("Barbarian", 12): 6, ("Barbarian", 13): 8, ("Barbarian", 14): 10,

        # Bard, d4
        ("Bard", 10): 2, ("Bard", 11): 4, ("Bard", 12): 6, ("Bard", 13): 8, ("Bard", 14): 10,

        # Bladedancer, d6
        ("Bladedancer", 10): 1, ("Bladedancer", 11): 2, ("Bladedancer", 12): 3, ("Bladedancer", 13): 4,
        ("Bladedancer", 14): 5,

        # Paladin, d8
        ("Paladin", 10): 2, ("Paladin", 11): 4, ("Paladin", 12): 6, ("Paladin", 13): 8, ("Paladin", 14): 10,

        # Priestess, d4
        ("Priestess", 10): 1, ("Priestess", 11): 2, ("Priestess", 12): 3, ("Priestess", 13): 4, ("Priestess", 14): 5,

        # Shaman, d6
        ("Shaman", 10): 1, ("Shaman", 11): 2, ("Shaman", 12): 3, ("Shaman", 13): 4, ("Shaman", 14): 5,

        # Warlock, d4
        ("Warlock", 10): 1, ("Warlock", 11): 2, ("Warlock", 12): 3, ("Warlock", 13): 4, ("Warlock", 14): 5,

        # Witch, d4
        ("Witch", 10): 1, ("Witch", 11): 2, ("Witch", 12): 3, ("Witch", 13): 4, ("Witch", 14): 5,

        # Dwarven Craftpriest, d6
        ("Dwarven Craftpriest", 10): 2,

        # Dwarven Vaultguard, d8
        ("Dwarven Vaultguard", 10): 3, ("Dwarven Vaultguard", 11): 6, ("Dwarven Vaultguard", 12): 9,
        ("Dwarven Vaultguard", 13): 12,

        # Elven Nightblade, d6
        ("Elven Nightblade", 10): 2, ("Elven Nightblade", 11): 4,

        # Elven Spellsword, d6
        ("Elven Spellsword", 10): 2,

        # Nobiran Wonderworker, d4
        ("Nobiran Wonderworker", 10): 1, ("Nobiran Wonderworker", 11): 2, ("Nobiran Wonderworker", 12): 3,

        # Zaharan Ruinguard, d6
        ("Zaharan Ruinguard", 10): 2, ("Zaharan Ruinguard", 11): 4, ("Zaharan Ruinguard", 12): 6,
    }


    def calculate_hp_progression_table(final_class, CON, level):
        con_mod = con_modifier(CON)
        hd = hit_die_type[final_class]

        hp_gains = []  # przyrost HP na poziom
        total_hp = 0  # aktualny całkowity HP
        roll_log = []  # suma rzutów kośćmi (bez CON) na poziomie
        con_log = []  # łączny mod z CON na poziomie
        bonus_log = []  # stały bonus po 9 poziomie (z tabeli)

        for level in range(1, level + 1):

            # ile kości: do 9. poziomu = lvl, potem zawsze 9
            dice_count = level if level <= 9 else 9

            # rzuty kośćmi ZAWSZE są wykonywane
            rolls = [random.randint(1, hd) for _ in range(dice_count)]

            # 1. poziom – każda kość minimum 4
            if level == 1:
                rolls = [max(r, 4) for r in rolls]

            roll_sum = sum(rolls)

            # CON działa tylko do 9. poziomu
            if level <= 9:
                con_total = con_mod * dice_count
                bonus = 0
            else:
                con_total = 0
                bonus = post_9_bonus.get((final_class, level), 0)

            # propozycja całkowitego HP na tym poziomie
            proposed_total = roll_sum + con_total + bonus

            # musi być przynajmniej +1 więcej niż poprzednio
            if proposed_total <= total_hp:
                proposed_total = total_hp + 1

            gain = proposed_total - total_hp
            total_hp = proposed_total

            # logi
            hp_gains.append(gain)
            roll_log.append(roll_sum)
            con_log.append(con_total)
            bonus_log.append(bonus)

        return total_hp, hp_gains, roll_log, con_log, bonus_log


    # --------------------------------
    # CLASS POWERS
    # --------------------------------

    class_powers_progression = {
        "Fighter": {
            1: ["Manual of Arms"],
            5: ["Battlefield Prowess"],
            9: ["Castle"],
        },

        "Explorer": {
            1: [
                "Alertness",
                "Ambushing",
                "Animal Reflexes",
                "Endurance",
                "Evasion",
                "Pathfinding",
                "Natural Stealth"
            ],
            5: ["Experience and Hardiness"],
            9: ["Border Fort"],
        },

        "Thief": {
            1: [
                "Backstabbing",
                "Climbing",
                "Hiding",
                "Listening",
                "Lockpicking",
                "Pickpocketing",
                "Searching",
                "Shadowy Senses",
                "Sneaking",
                "Streetwise",
                "Trapbreaking"
            ],
            4: ["Deciphering"],
            9: ["Hideout"],
            10: ["Scrollreading"],
        },

        "Mage": {
            1: [
                "Arcane Magic",
                "Collegiate Wizardry",
            ],
            5: ["Minor Magical Research"],
            9: [
                "Major Magical Research",
                "Sanctum",
            ],
            11: ["Supreme Magical Research"],
        },

        "Crusader": {
            1: [
                "Divine Magic",
                "Theology",
                "Rebuke Undead",
            ],
            5: ["Minor Magical Research"],
            9: [
                "Major Magical Research",
                "Fortified Church",
            ],
            11: ["Supreme Magical Research"],
        },

        "Venturer": {
            1: [
                "Bribery",
                "Diplomacy",
                "Expert Bargaining",
                "Expert Travelling",
                "Mercantile Network",
                "Multilingual",
                "Pathfinding",
                "Treachery"
            ],
            2: ["Steady Trade Route"],
            4: ["Rumormongering"],
            6: ["Steady Trade Route"],
            8: ["Access to Capital"],
            9: ["Guildhouse"],
            10: ["Steady Trade Route"],
            12: ["Monopoly Power"],
        },

        "Assassin": {
            1: [
                "Backstabbing",
                "Hiding",
                "Shadowy Senses",
                "Sneaking",
                "Streetwise",
            ],
            9: ["Hideout"],
        },

        "Barbarian": {
            1: [
                "Animal Reflexes",
                "Natural Proficiency",
                "Natural Stealth",
                "Savage Resilience",
            ],
            5: ["Animal Magnetism"],
            9: ["Chieftain's Hall"],
        },

        "Bard": {
            1: [
                "Arcane Dabbling",
                "Inspire Courage",
                "Jack of All Trades",
                "Listening",
                "Loremastery",
                "Multilingual",
                "Performance"
            ],
            3: ["Jack of All Trades II"],
            4: ["Deciphering"],
            5: ["Chronicles of Battle"],
            6: ["Jack of All Trades III"],
            7: ["Inspire Hope"],
            8: ["Jack of All Trades IV"],
            9: ["Great Hall"],
            10: ["Scrollreading"],
            11: ["Jack of All Trades V"],
        },

        "Bladedancer": {
            1: [
                "Graceful Fighting",
                "Divine Magic",
                "Strength of Faith",
                "Theology",
                "Weapon Finesse",
            ],
            5: ["Minor Magical Research"],
            9: [
                "Major Magical Research",
                "Temple"
            ],
            11: ["Supreme Magical Research"],
        },

        "Paladin": {
            1: [
                "Aura of Protection",
                "Lay on Hands",
                "Manual of Arms",
                "Sanctified Body",
                "Sense Evil",
            ],
            5: ["Holy Fervor"],
            9: ["Fortress"],
        },

        "Priestess": {
            1: [
                "Consolation",
                "Diplomacy",
                "Divine Magic",
                "Lay on Hands",
                "Purity of the Body",
                "Theology"
            ],
            5: ["Minor Magical Research"],
            9: [
                "Cloister",
                "Major Magical Research"
            ],
            11: ["Supreme Magical Research"],
        },

        "Shaman": {
            1: [
                "Commune with Spirits",
                "Divine Magic",
                "Totem Animal"
            ],
            3: ["Spiritual Ritual"],
            5: [
                "Minor Magical Research",
                "Shapechanging"
            ],
            7: ["Spiritwalking"],
            9: [
                "Major Magical Research",
                "Medicine Lodge",
            ],
            11: ["Supreme Magical Research"],
        },

        "Warlock": {
            1: [
                "Arcane Magic",
                "Corrupting Weakness 1",
                "Dark Path 1",
                "Occultism"
            ],
            3: [
                "Corrupting Weakness 2",
                "Dark Path 2"
            ],
            5: [
                "Corrupting Weakness 3",
                "Dark Path 3",
                "Minor Magical Research"
            ],
            7: [
                "Corrupting Weakness 4",
                "Dark Path 4"
            ],
            9: [
                "Corrupting Weakness 5",
                "Dark Path 5",
                "Major Magical Research",
                "Sanctum"
            ],
            11: [
                "Corrupting Weakness 6",
                "Dark Path 6",
                "Supreme Magical Research"
            ],
        },

        "Witch": {
            1: [
                "Studious Divine Magic",
                "Tradition",
                "Village Wisdom",
                "Tradition Feature 1"
            ],
            3: [
                "Brew Potions",
                "Tradition Feature 2"
            ],
            5: [
                "Minor Magical Research",
                "Tradition Feature 3"
            ],
            7: [
                "Scribe Scrolls",
                "Tradition Feature 4"
            ],
            9: [
                "Witch's Cottage",
                "Major Magical Research"
            ],
            11: ["Supreme Magical Research"],
        },

        "Dwarven Craftpriest": {
            1: [
                "Attention to Detail",
                "Crafting",
                "Rebuke Undead",
                "Studious Divine Magic",
                "Theology",
                "Dwarf Tongues",
                "Hardy",
                "Sensitivity to Rock and Stone"
            ],
            5: ["Minor Magical Research"],
            9: [
                "Major Magical Research",
                "Vault"
            ],
        },

        "Dwarven Vaultguard": {
            1: [
                "Manual of Arms",
                "Dwarf Tongues",
                "Hardy",
                "Sensitivity to Rock and Stone"
            ],
            5: ["Battlefield Prowess"],
            9: ["Vault"],
        },

        "Elven Nightblade": {
            1: [
                "Acrobatics",
                "Backstabbing",
                "Climbing",
                "Hiding",
                "Shadowy Senses",
                "Sneaking",
                "Attunement to Nature",
                "Connection to Nature",
                "Elf Tongues"
            ],
            2: [
                "Arcane Magic",
                "Quiet Magic"
            ],
            7: ["Minor Magical Research"],
            9: ["Hideout"]
        },

        "Elven Spellsword": {
            1: [
                "Arcane Magic",
                "Collegiate Wizardry",
                "Attunement to Nature",
                "Connection to Nature",
                "Elf Tongues"
            ],
            5: ["Minor Magical Research"],
            9: [
                "Major Magical Research",
                "Fastness"
            ]
        },

        "Nobiran Wonderworker": {
            1: [
                "Arcane Magic",
                "Collegiate Wizardry",
                "Divine Magic",
                "Divine Health",
                "Lay on Hands",
                "Blood of Ancient Kings",
                "Favor of the Empyrean Powers",
                "Longeval"
            ],
            5: ["Minor Magical Research"],
            9: [
                "Major Magical Research",
                "Sanctum"
            ],
            11: ["Supreme Magical Research"]
        },

        "Zaharan Ruinguard": {
            1: [
                "Dark Blessing",
                "Manual of Arms",
                "Prenaturnal Quickening",
                "Weapon Focus",
                "After the Flesh",
                "Ancient Pacts",
                "Dark Souls"
            ],
            2: [
                "Arcane Magic",
                "Arcane Striking"
            ],
            4: ["Death Healing"],
            5: ["Dark Charisma"],
            7: ["Minor Magical Research"],
            9: [
                "Dark Fortress",
                "Spell Storing"
            ],
            12: ["Major Magical Research"]
        },
        # tu dodasz kolejne klasy
    }

    #CORRUPTING WEAKNESSES
    def roll_corrupting_weakness(owned):
        """
        Zwraca jedną wylosowaną Corrupting Weakness z uwzględnieniem limitów.
        owned – dict z aktualną liczbą posiadanych słabości:
            {"Disfigured": 2, "Sleepless": 1, ...}
        """
        candidates = []

        for weakness, data in corrupting_weaknesses.items():
            limit = data["limit"]
            current = owned.get(weakness, 0)

            # jeśli ma limit i jest osiągnięty → pomijamy
            if limit is not None and current >= limit:
                continue

            candidates.append(weakness)

        if not candidates:
            return None  # teoretycznie niemożliwe, ale bezpieczne

        return random.choice(candidates)

    mutation_log = []  # lista krotek: (index, roll, description)

    def roll_mutation(mutated_count):
        """
        Zwraca wynik z tabeli mutacji.
        mutated_count = ile razy już wylosowano 'Mutated'

        Pierwsza mutacja → 1d10
        Druga → 1d10+1
        Trzecia → 1d10+2
        ...

        Maksimum to 1d20.
        """
        base_roll = random.randint(1, 10)
        modified = base_roll + mutated_count  # przesunięcie

        if modified > 20:
            modified = 20  # sufit tabeli

        return modified, mutations_table[modified]


    def apply_class_powers(final_class, level, warlock_path=warlock_path, witch_tradition=witch_tradition):
        """
        Zwraca:
          powers — lista wszystkich posiadanych class powers
          log    — lista wpisów (level, "Class Power", nazwa)
        """
        powers = []
        log = []

        if final_class not in class_powers_progression:
            return powers, log

        prog = class_powers_progression[final_class]

        for power_level in range(1, level + 1):
            if power_level not in prog:
                continue

            for power in prog[power_level]:

                # --- WARLOCK: CORRUPTING WEAKNESS ---
                # licznik mutacji
                if "mutated_counter" not in locals():
                    mutated_counter = 0

                # --- WARLOCK: CORRUPTING WEAKNESS ---
                if final_class == "Warlock" and "Corrupting Weakness" in power:

                    if "weakness_count" not in locals():
                        weakness_count = {}

                    weakness = roll_corrupting_weakness(weakness_count)

                    if weakness:
                        weakness_count[weakness] = weakness_count.get(weakness, 0) + 1

                        # Specjalny przypadek: Mutated
                        if weakness == "Mutated":
                            mutated_counter += 1

                            roll, mutation_effect = roll_mutation(mutated_counter)

                            # Dodajemy wpis tylko „Mutated” do Class Powers:
                            powers.append("Mutated")
                            log.append((power_level, "Class Power", "Mutated"))

                            # Pełny opis dodajemy do mutation_log:
                            mutation_log.append({
                                "index": mutated_counter,
                                "roll": roll,
                                "effect": mutation_effect
                            })

                            continue

                        # reszta słabości
                        powers.append(weakness)
                        log.append((power_level, "Class Power", weakness))

                    continue

                # ---- SPECJALNA OBSŁUGA WARLOCKA ----
                if final_class == "Warlock" and "Dark Path" in power:
                    # Wyciągnij numer (np. "Dark Path III" → 3)
                    index = power.replace("Dark Path", "").strip()
                    index = 1 if index == "" else int(index)

                    subclass_power_warlock = warlock_paths[warlock_path][index]

                    powers.append(subclass_power_warlock)
                    log.append((power_level, "Class Power", subclass_power_warlock))
                    continue

                # ---- SPECJALNA OBSŁUGA WARLOCKA ----
                if final_class == "Witch" and "Tradition Feature" in power:
                    # Wyciągnij numer (np. "Dark Path III" → 3)
                    index = power.replace("Tradition Feature", "").strip()
                    index = 1 if index == "" else int(index)

                    subclass_power_witch = witch_traditions[witch_tradition][index]

                    powers.append(subclass_power_witch)
                    log.append((power_level, "Class Power", subclass_power_witch))
                    continue

                # Normalna ścieżka dla innych mocy
                powers.append(power)
                log.append((power_level, "Class Power", power))

        return powers, log


    class_powers, class_powers_log = apply_class_powers(
        final_class,
        level,
        warlock_path=warlock_path,
        witch_tradition=witch_tradition
    )

    # ZAKLĘCIA

    spell_slots_progression = {

        "Mage": {
            1: [1],
            2: [2],
            3: [2, 1],
            4: [2, 2],
            5: [2, 2, 1],
            6: [2, 2, 2],
            7: [3, 2, 2, 1],
            8: [3, 3, 2, 2],
            9: [3, 3, 3, 2, 1],
            10: [3, 3, 3, 3, 2],
            11: [4, 3, 3, 3, 2, 1],
            12: [4, 4, 3, 3, 3, 2],
            13: [4, 4, 4, 3, 3, 2],
            14: [4, 4, 4, 4, 3, 3],
        },

        "Crusader": {
            1: [1],
            2: [2],
            3: [2, 1],
            4: [2, 2],
            5: [2, 2, 1],
            6: [2, 2, 2],
            7: [3, 2, 2, 1],
            8: [3, 3, 2, 2],
            9: [3, 3, 3, 2, 1],
            10: [3, 3, 3, 3, 2],
            11: [4, 3, 3, 3, 2, 1],
            12: [4, 4, 3, 3, 3, 2],
            13: [4, 4, 4, 3, 3, 2],
            14: [4, 4, 4, 4, 3, 3],
        },

        "Bladedancer": {
            1: [1],
            2: [2],
            3: [2, 1],
            4: [2, 2],
            5: [2, 2, 1],
            6: [2, 2, 2],
            7: [3, 2, 2, 1],
            8: [3, 3, 2, 2],
            9: [3, 3, 3, 2, 1],
            10: [3, 3, 3, 3, 2],
            11: [4, 3, 3, 3, 2, 1],
            12: [4, 4, 3, 3, 3, 2],
            13: [4, 4, 4, 3, 3, 2],
            14: [4, 4, 4, 4, 3, 3],
        },

        "Priestess": {
            1: [2],
            2: [3],
            3: [3, 2],
            4: [3, 3],
            5: [3, 3, 2],
            6: [3, 3, 3],
            7: [5, 3, 3, 2],
            8: [5, 5, 3, 3],
            9: [5, 5, 5, 3, 2],
            10: [5, 5, 5, 5, 3],
            11: [6, 5, 5, 5, 3, 2],
            12: [6, 6, 5, 5, 5, 3],
            13: [6, 6, 6, 5, 5, 3],
            14: [6, 6, 6, 6, 5, 5],
        },

        "Shaman": {
            1: [1],
            2: [2],
            3: [2, 1],
            4: [2, 2],
            5: [2, 2, 1],
            6: [2, 2, 2],
            7: [3, 2, 2, 1],
            8: [3, 3, 2, 2],
            9: [3, 3, 3, 2, 1],
            10: [3, 3, 3, 3, 2],
            11: [4, 3, 3, 3, 2, 1],
            12: [4, 4, 3, 3, 3, 2],
            13: [4, 4, 4, 3, 3, 2],
            14: [4, 4, 4, 4, 3, 3],
        },

        "Warlock": {
            1: [1],
            2: [2],
            3: [2, 1],
            4: [2, 2],
            5: [2, 2, 1],
            6: [2, 2, 2],
            7: [3, 2, 2, 1],
            8: [3, 3, 2, 2],
            9: [3, 3, 3, 2, 1],
            10: [3, 3, 3, 3, 2],
            11: [4, 3, 3, 3, 2, 1],
            12: [4, 4, 3, 3, 3, 2],
            13: [4, 4, 4, 3, 3, 2],
            14: [4, 4, 4, 4, 3, 3],
        },

        "Witch": {
            1: [2],
            2: [3],
            3: [3, 2],
            4: [3, 3],
            5: [3, 3, 2],
            6: [3, 3, 3],
            7: [5, 3, 3, 2],
            8: [5, 5, 3, 3],
            9: [5, 5, 5, 3, 2],
            10: [5, 5, 5, 5, 3],
            11: [6, 5, 5, 5, 3, 2],
            12: [6, 6, 5, 5, 5, 3],
            13: [6, 6, 6, 5, 5, 3],
            14: [6, 6, 6, 6, 5, 5],
        },

        "Dwarven Craftpriest": {
            1: [1],
            2: [2],
            3: [2, 1],
            4: [2, 2],
            5: [2, 2, 1],
            6: [2, 2, 2],
            7: [3, 2, 2, 1],
            8: [3, 3, 2, 2],
            9: [3, 3, 3, 2, 1],
            10: [3, 3, 3, 3, 2],
        },

        "Elven Nightblade": {
            2: [1],
            3: [2],
            5: [2, 1],
            6: [2, 2],
            7: [2, 2, 1],
            8: [3, 2, 2, 1],
            9: [4, 2, 2, 2],
            10: [4, 3, 2, 2],
            11: [4, 3, 3, 2, 1],
        },

        "Elven Spellsword": {
            2: [2],
            3: [2, 1],
            4: [2, 2],
            5: [2, 2, 1],
            6: [2, 2, 2],
            7: [3, 2, 2, 1],
            8: [3, 3, 2, 2],
            9: [3, 3, 3, 2, 1],
            10: [3, 3, 3, 3, 2],
            11: [4, 3, 3, 3, 2, 1],
        },

        "Nobiran Wonderworker": {
            "arcane": {
                1: [1],
                2: [2],
                3: [2, 1],
                4: [2, 2],
                5: [2, 2, 1],
                6: [2, 2, 2],
                7: [3, 2, 2, 1],
                8: [3, 3, 2, 2],
                9: [3, 3, 3, 2, 1],
                10: [3, 3, 3, 3, 2],
                11: [4, 3, 3, 3, 2, 1],
                12: [4, 4, 3, 3, 3, 2],
            },
            "divine": {
                1: [1],
                2: [2],
                3: [2, 1],
                4: [2, 2],
                5: [2, 2, 1],
                6: [2, 2, 2],
                7: [3, 2, 2, 1],
                8: [3, 3, 2, 2],
                9: [3, 3, 3, 2, 1],
                10: [3, 3, 3, 3, 2],
                11: [4, 3, 3, 3, 2, 1],
                12: [4, 4, 3, 3, 3, 2],
            }
        },

        "Zaharan Ruinguard": {
            1: [],
            2: [1],
            3: [2],
            4: [2, 2],
            5: [2, 2, 1],
            6: [2, 2, 2],
            7: [2, 2, 1],
            8: [3, 2, 2, 1],
            9: [4, 2, 2, 2],
            10: [4, 3, 2, 2],
            11: [4, 3, 3, 2, 1],
            12: [4, 4, 3, 2, 1],
        },
    }

    spell_slots = spell_slots_progression.get(final_class, {}).get(level, [])

    arcane_spells = {
        1: [
            "Arcane Armor", "Auditory Illusion", "Beguile Humanoid", "Blinding Flash",
            "Chameleon", "Choking Grip", "Conjure Cacodemon Spawn", "Counterspell",
            "Desiccate", "Discern Gist", "Discern Magic", "Earth’s Excrescence",
            "Faithful Companion", "Fan of Flames", "Frighten Humanoid", "Ice Floe",
            "Illumination", "Illusory Figment", "Infuriate Humanoid", "Kindle Flame",
            "Leaping", "Mage Missile", "Seal Portal", "Sharpness", "Shatter Blade",
            "Silent Step", "Slicing Blow", "Slickness", "Sling Stone", "Slumber",
            "Spider Climbing", "Summon Manes", "Thunderclap", "Unliving Puppet",
            "Wall of Smoke", "Weave Smoke"
        ],

        2: [
            "Adjust Self", "Battering Ram", "Bewitch Humanoid", "Bloody Flux",
            "Burning Sparks", "Circling Winds", "Conjure Imp", "Conjure Petty Elemental",
            "Dark Whisper", "Deathless Minion", "Discern Invisible", "Dominate Humanoid",
            "Earth’s Wave", "Energy Protection", "Frostbite", "Gale of Wind",
            "Halt Humanoids", "Hypnotic Sigil", "Illusory Duplicates",
            "Illusory Interior", "Levitation", "Locate Object", "Magic Lock",
            "Necromantic Potence", "Ogre Strength", "Phantasmal Figment",
            "Physical Protection", "Rain of Vitriol", "Shrouding Fog",
            "Sudden Staircase", "Summon Insect Swarm", "Sunflare", "Swimming",
            "Vitriolic Infusion", "Warp Wood", "Webbing"
        ],

        3: [
            "Avian Messenger", "Bewitch Crowd", "Boil Blood", "Chimerical Figment",
            "Clairaudiency", "Clairvoyancy", "Cone of Frost", "Conjure Hellion",
            "Create Chasm", "Deflect Ordinary Missiles", "Dismember", "Dispel Magic",
            "Dominate Monster", "Earth’s Teeth", "Fireball", "Flight",
            "Force of Impetus", "Growth", "Ice Sheet", "Illumination Perpetual",
            "Inaudibility", "Incite Madness", "Infuriate Crowd", "Invisibility",
            "Lightless Vision", "Lightning Strike", "Rune of Warding", "Skinchange",
            "Speak with Dead", "Spellward", "Strengthen the Unliving",
            "Summon Hellhounds", "Thunderbolt", "Wall of Thunder",
            "Water Breathing", "Weave Fire"
        ],

        4: [
            "Animate Undead", "Arcane Shift", "Bewitch Monster", "Cloud of Poison",
            "Cone of Fear", "Conjure Incubus", "Conjure Major Elemental",
            "Earth’s Tremor", "Energy Invulnerability", "Flesh to Ash", "Giant Strength",
            "Growth Plant", "Guise Self", "Halt Monsters", "Hidden Host",
            "Illusory Terrain", "Indiscernibility", "Inferno", "Iron Maiden",
            "Locate Treasure", "Magic Carpet", "Physical Invulnerability", "Safe Travels",
            "Scouring Zephyr", "Scry", "Shrieking Skull", "Slumber (Deep)",
            "Spectral Figment", "Spellward Other", "Sphere of Invulnerability Lesser",
            "Summon Shadow", "Sunder Structure", "Telepathy", "Wall of Flame",
            "Wall of Frost", "Weave Water"
        ],

        5: [
            "Blast Ward", "Capsizing Wave", "Carnage", "Circle of Agony",
            "Cone of Paralysis", "Conjure Dybbuk", "Conjure Supreme Elemental",
            "Contact Other Sphere", "Control Winds", "Curse of the Swine",
            "Deflect Ordinary Weapons", "Dominate Plants", "Earth’s Mire",
            "Fillet and Serve", "Firestorm", "Flay the Slain", "Forest Enchantment",
            "Forgetfulness", "Guise Other", "Ice Storm", "Lay of the Land",
            "Life Transfer", "Lightless Vision (Mass)", "Locate Haunting", "Mirage",
            "Phantasmal Horror", "Rouse the Fallen", "Selective Fire", "Soul Swap",
            "Spectral Legion", "Summon Ooze", "Summon Weather", "Telekinesis",
            "Teleportation", "Wall of Stone", "X-Ray Vision"
        ],

        6: [
            "Anti-Magic Sphere", "Banner of Invincibility", "Body Swap",
            "Clairaudiency Greater", "Clairvoyancy Greater", "Conflagration",
            "Conjure Fiend", "Conjure Genie", "Control Weather",
            "Disfigure Body and Soul", "Disintegration", "Earth’s Movement",
            "Enslave Humanoid", "Level Water", "Locate Distant Object",
            "Locate Place of Power", "Madness of Crowds", "Necromantic Invulnerability",
            "Panic", "Passageway", "Perpetual Figment", "Petrification",
            "Programmatic Figment", "Quest", "Reveal Ritual Magic",
            "Soul Eating", "Spellwarded Zone", "Sphere of Invulnerability Greater",
            "Summon Invisible Stalker", "Torpor", "Transform Other",
            "Transform Self", "Trollblood", "Wall of Annihilation",
            "Wall of Corpses", "Wall of Force"
        ]
    }

    REPERTOIRE_CLASSES = {
        "Mage",  # arcane
        "Warlock",  # arcane
        "Dwarven Craftpriest",  # divine
        "Elven Nightblade",  # arcane
        "Elven Spellsword",  # arcane
        "Nobiran Wonderworker",  # tylko arcane!
        "Zaharan Ruinguard",  # arcane
    }


    def calculate_known_spells(final_class, level, INT, spell_slots_progression):
        """
        Zwraca dict:
        {
            1: [...list of spells...],
            2: [...],
            ...
        }
        """
        # klasy bez repertuaru
        if final_class not in REPERTOIRE_CLASSES:
            return {}

        # pobierz sloty na tym poziomie
        # dla Nobirana: arcane część
        if final_class == "Nobiran Wonderworker":
            slots = spell_slots_progression["Nobiran Wonderworker"]["arcane"].get(level, [])
        else:
            slots = spell_slots_progression.get(final_class, {}).get(level, [])

        known = {}

        # INT wpływa na liczbę znanych zaklęć
        int_bonus = 0
        if INT >= 13:
            if 13 <= INT <= 15:
                int_bonus = 1
            elif 16 <= INT <= 17:
                int_bonus = 2
            elif INT == 18:
                int_bonus = 3

        # iterate spell levels
        for spell_level, slot_count in enumerate(slots, start=1):

            # ile zaklęć będzie znał?
            num_known = slot_count + int_bonus

            # pula zaklęć dla danego poziomu
            available = arcane_spells.get(spell_level, [])

            if not available:
                continue

            # wybieramy bez powtórzeń
            picks = random.sample(available, min(num_known, len(available)))

            known[spell_level] = picks

        return known


    known_spells = calculate_known_spells(final_class, level, stats["INT"], spell_slots_progression)

    # SHAMAN SPELLS
    shaman_divine_spells = {
        1: [
            "Call of the Wolf", "Counterspell", "Cure Light Injury", "Frighten Beast",
            "Infuriate Beast", "Kindle Flame", "Locate Animal or Plant",
            "Pass Without Trace", "Predict Weather", "Purify Food and Water"
        ],
        2: [
            "Bewitch Beast", "Call of the Wolf Pack", "Circling Winds",
            "Dominate Beast", "Energy Protection", "Holy Blessing", "Holy Chant",
            "Physical Protection", "Speak with Beasts", "Transform Beast"
        ],
        3: [
            "Avian Messenger", "Call of the Wild Bear", "Cure Disease",
            "Dispel Magic", "Growth (Beast)", "Lightning Strike",
            "Rune of Warding", "Spellward", "Water Breathing", "Winged Flight"
        ],
        4: [
            "Call of the Galloping Herd", "Create Water", "Cure Serious Injury",
            "Energy Invulnerability", "Neutralize Poison",
            "Physical Invulnerability", "Protection from Temperature",
            "Repair Disfigurement & Dismemberment", "Skinchange",
            "Speak with Plants"
        ],
        5: [
            "Blast Ward", "Call of the Great Cats", "Control Winds", "Create Food",
            "Fiery Pillar", "Lay of the Land", "Restore Life and Limb",
            "Safe Travels", "Summon Insect Plague", "Vigor"
        ],
        6: [
            "Blast Ward (Greater)", "Call of the Aerophract Steeds",
            "Call of the Ancient Tusk", "Clairaudiency Greater",
            "Clairvoyancy (Greater)", "Locate Place of Power",
            "Prophetic Dream", "Quest", "Salvific Rain", "Summon Weather"
        ]
    }


    def calculate_shaman_spells(level, spell_slots_progression):
        """
        Zwraca dict:
        {
            1: [...wszystkie zaklęcia z poziomu 1...],
            2: [...],
            ...
        }
        """
        known = {}

        # Pobierz sloty Shamana
        slots = spell_slots_progression["Shaman"].get(level, [])

        # iterujemy po poziomach zaklęć Shamana
        for spell_level, slot_count in enumerate(slots, start=1):
            if slot_count > 0:
                # jeśli ma chociaż jedną komórkę → zna wszystkie zaklęcia
                known[spell_level] = shaman_divine_spells.get(spell_level, [])

        return known


    # PRIESTESS_SPELLS

    priestess_divine_spells = {
        1: [
            "Allure", "Angelic Choir", "Counterspell", "Cure Light Injury",
            "Delay Disease", "Discern Evil", "Discern Magic",
            "Holy Circle", "Illumination", "Purify Food and Water",
            "Remove Fear", "Salving Rest", "Sanctuary", "Shatter Blade",
            "Word of Command"
        ],

        2: [
            "Augury", "Bewitch Beast", "Cure Moderate Injury", "Delay Poison",
            "Divine Armor", "Divine Grace", "Discern Bewitchment", "Energy Protection",
            "Halt Humanoids", "Holy Blessing", "Holy Chant",
            "Noiselessness", "Physical Protection", "Slumber",
            "Speak with Beasts"
        ],

        3: [
            "Avian Messenger", "Cure Blindness", "Cure Disease",
            "Cure Major Injury", "Deflect Ordinary Missiles",
            "Discern Curse", "Dispel Magic",
            "Holy Circle, Sustained", "Holy Prayer",
            "Illumination, Perpetual", "Remove Curse",
            "Rune of Warding", "Speak with Dead",
            "Spellward", "Water Walking"
        ],

        4: [
            "Angelic Aura", "Create Water", "Cure Serious Injury",
            "Death Ward", "Divination", "Energy Invulnerability",
            "Inspire Awe", "Neutralize Poison",
            "Physical Invulnerability", "Repair Disfigurement & Dismemberment",
            "Smite Undead", "Snakes to Staffs", "Spellward Other",
            "Spirit of Healing", "Tongues"
        ],

        5: [
            "Atonement", "Blast Ward", "Communion",
            "Cone of Fear", "Create Food", "Cure Critical Injury",
            "Deflect Ordinary Weapons", "Dominate Monster",
            "Fate", "Healing Circle", "Restore Life and Limb",
            "Scry", "Strength of Mind", "Summon Insect Plague",
            "True Seeing"
        ],

        6: [
            "Anti-Magic Sphere", "Banner of Invincibility",
            "Bath of the Goddess", "Blast Ward (Greater)",
            "Clairaudiency, Greater", "Clairvoyancy, Greater",
            "Dispel Evil", "Home Ward", "Locate Place of Power",
            "Level Water", "Prophetic Dream", "Quest",
            "Salvific Rain", "Spellwarded Zone",
            "Summon Winged Herald"
        ]
    }


    def calculate_priestess_spells(level, spell_slots_progression):
        """
        Zwraca dict:
        {
            1: [...lista zaklęć dostępnych Priestess...],
            2: [...],
            ...
        }
        Priestess – jeśli ma chociaż jedną komórkę zaklęć danego poziomu,
        zna wszystkie zaklęcia tego poziomu.
        """
        known = {}

        slots = spell_slots_progression["Priestess"].get(level, [])

        for spell_level, slot_count in enumerate(slots, start=1):
            if slot_count > 0:
                known[spell_level] = priestess_divine_spells.get(spell_level, [])

        return known


    # CRUSADER SPELLS

    crusader_divine_spells = {
        1: [
            "Counterspell", "Cure Light Injury", "Destroy Dead",
            "Discern Evil", "Discern Magic", "Holy Circle",
            "Illumination", "Remove Fear", "Sling Stone",
            "Word of Command"
        ],

        2: [
            "Augury", "Delay Poison", "Energy Protection",
            "Halt Humanoids", "Holy Blessing", "Holy Chant",
            "Noiselessness", "Physical Protection",
            "Righteous Wrath", "Spiritual Weapon"
        ],

        3: [
            "Dispel Magic", "Divine Protection",
            "Holy Circle, Sustained", "Holy Prayer",
            "Illumination, Perpetual", "Invulnerability to Evil",
            "Remove Curse", "Rune of Warding",
            "Spellward", "Striking"
        ],

        4: [
            "Angelic Aura", "Call of the Regal Pride",
            "Cure Serious Injury", "Energy Invulnerability",
            "Inspire Awe", "Neutralize Poison",
            "Physical Invulnerability",
            "Repair Disfigurement & Dismemberment",
            "Smite Undead", "Sunflare"
        ],

        5: [
            "Atonement", "Blast Ward", "Communion",
            "Fiery Pillar", "Locate Haunting",
            "Restore Life and Limb", "Strength of Mind",
            "True Seeing", "Turn to Dust", "Vigor"
        ],

        6: [
            "Arrows of the Sun", "Banner of Invincibility",
            "Blast Ward (Greater)", "Dispel Evil",
            "Hidden Host", "Phoenix Aura",
            "Prophetic Dream", "Quest",
            "Salvific Rain", "Summon Winged Herald"
        ]
    }


    def calculate_crusader_spells(level, spell_slots_progression):
        """
        Zwraca dict:
        {
            1: [...lista zaklęć dostępnych Crusaderowi...],
            2: [...],
            ...
        }
        Crusader – jeśli ma chociaż jedną komórkę zaklęć danego poziomu,
        zna wszystkie zaklęcia tego poziomu.
        """
        known = {}

        slots = spell_slots_progression["Crusader"].get(level, [])

        for spell_level, slot_count in enumerate(slots, start=1):
            if slot_count > 0:
                known[spell_level] = crusader_divine_spells.get(spell_level, [])

        return known


    # BLEJDDENCERKA

    bladedancer_divine_spells = {
        1: [
            "Allure", "Angelic Choir", "Bane-Rune", "Counterspell",
            "Cure Light Injury", "Discern Evil", "Discern Magic",
            "Holy Circle", "Illumination", "Remove Fear"
        ],

        2: [
            "Augury", "Divine Armor", "Energy Protection",
            "Holy Blessing", "Halt Humanoids", "Holy Chant",
            "Physical Protection", "Shimmer", "Spiritual Weapon",
            "Swift Sword"
        ],

        3: [
            "Dispel Magic", "Holy Circle, Sustained", "Holy Prayer",
            "Illumination, Perpetual", "Invulnerability to Evil",
            "Rune of Warding", "Spellward", "Striking",
            "Swift Sword, Sustained", "Winged Flight"
        ],

        4: [
            "Angelic Aura", "Call of the Regal Pride",
            "Cure Serious Injury", "Divination",
            "Energy Invulnerability", "Inspire Awe",
            "Neutralize Poison", "Physical Invulnerability",
            "Repair Disfigurement & Dismemberment", "Tongues"
        ],

        5: [
            "Atonement", "Blast Ward", "Communion",
            "Cone of Fear", "Fiery Pillar",
            "Restore Life and Limb", "Strength of Mind",
            "Sword of Fire", "True Seeing", "Vigor"
        ],

        6: [
            "Banner of Invincibility", "Barrier of Blades",
            "Bath of the Goddess", "Blast Ward (Greater)",
            "Dispel Evil", "Hidden Host", "Phoenix Aura",
            "Prophetic Dream", "Quest", "Summon Winged Herald"
        ]
    }


    def calculate_bladedancer_spells(level, spell_slots_progression):
        known = {}
        slots = spell_slots_progression["Bladedancer"].get(level, [])

        for spell_level, slot_count in enumerate(slots, start=1):
            if slot_count > 0:
                known[spell_level] = bladedancer_divine_spells.get(spell_level, [])

        return known


    # WIEDŹMA

    witch_divine_spells = {
        1: [
            "Allure", "Angelic Choir", "Bane-Rune", "Call of the Wolf", "Counterspell",
            "Cure Light Injury", "Delay Disease", "Destroy Dead", "Discern Evil",
            "Discern Gist", "Discern Magic", "Discern Poison", "Faithful Companion",
            "Frighten Beast", "Infuriate Beast", "Kindle Flame", "Locate Animal or Plant",
            "Pass Without Trace", "Predict Weather", "Purify Food and Water",
            "Remove Fear", "Salving Rest", "Sanctuary", "Seal Portal", "Shatter Blade",
            "Sling Stone", "Unliving Puppet", "Word of Command"
        ],

        2: [
            "Augury", "Beguile Humanoid", "Bewitch Beast", "Call of the Wolf Pack",
            "Choking Grip", "Circling Winds", "Cure Moderate Injury", "Dark Whisper",
            "Deathless Minion", "Delay Poison", "Discern Bewitchment", "Divine Armor",
            "Divine Grace", "Dominate Beasts", "Energy Protection", "Halt Humanoids",
            "Holy Blessing", "Holy Chant", "Magic Lock", "Necromantic Potence",
            "Noiselessness", "Physical Protection", "Righteous Wrath", "Shimmer",
            "Slicing Blow", "Speak with Beasts", "Spiritual Weapon", "Swift Sword",
            "Transform Beast"
        ],

        3: [
            "Avian Messenger", "Bewitch Humanoid", "Call of the Wild Bear",
            "Clairaudiency", "Clairvoyancy", "Cure Blindness", "Cure Disease",
            "Cure Major Injury", "Deflect Ordinary Missiles", "Discern Curse",
            "Discern Invisible", "Dispel Magic", "Divine Protection",
            "Growth (Beast)", "Holy Circle, Sustained", "Holy Prayer",
            "Illumination, Perpetual", "Invulnerability to Evil", "Lightning Strike",
            "Phantasmal Figment", "Remove Curse", "Rune of Warding", "Speak with Dead",
            "Spellward", "Strengthen the Unliving", "Striking",
            "Swift Sword, Sustained", "Water Breathing", "Water Walking",
            "Winged Flight"
        ],

        4: [
            "Angelic Aura", "Call of the Galloping Herd", "Call of the Regal Pride",
            "Crafting", "Create Water", "Cure Serious Injury", "Death Ward",
            "Dismember", "Divination", "Energy Invulnerability", "Gale of Wind",
            "Growth", "Inaudibility", "Indiscernibility", "Inspire Awe",
            "Invisibility", "Lightless Vision", "Neutralize Poison",
            "Physical Invulnerability", "Protection from Temperature",
            "Repair Disfigurement & Dismemberment", "Skinchange", "Smite Undead",
            "Snakes to Staffs", "Speak with Plants", "Spellward Other",
            "Sphere of Invulnerability (Lesser)", "Spirit of Healing", "Sunflare",
            "Tongues"
        ],

        5: [
            "Atonement", "Blast Ward", "Boil Blood", "Call of the Great Cats",
            "Communion", "Cone of Fear", "Control Winds", "Create Food",
            "Cure Critical Injury", "Curse of the Swine", "Deflect Ordinary Weapons",
            "Dominate Monster", "Fate", "Fiery Pillar", "Giant Strength",
            "Growth (Plant)", "Guise Self", "Healing Circle", "Lay of the Land",
            "Locate Haunting", "Restore Life and Limb", "Safe Travels", "Scry",
            "Spiritwalk", "Strength of Mind", "Sword of Fire", "True Seeing",
            "Turn to Dust", "Vigor"
        ],

        6: [
            "Anti-Magic Sphere", "Arrows of the Sun", "Banner of Invincibility",
            "Barrier of Blades", "Bath of the Goddess", "Bewitch Monster",
            "Blast Ward (Greater)", "Call of the Ancient Tusk",
            "Call of the Aerophract Steeds", "Clairaudiency (Greater)",
            "Clairvoyancy (Greater)", "Dispel Evil", "Fillet and Serve",
            "Flesh to Ash", "Guise Other", "Hidden Host", "Home Ward",
            "Illusory Terrain", "Level Water", "Locate Place of Power",
            "Phoenix Aura", "Prophetic Dream", "Quest", "Salvific Rain",
            "Slumber (Deep)", "Spectral Figment", "Spellwarded Zone",
            "Sphere of Invulnerability (Greater)", "Summon Weather",
            "Summon Winged Herald"
        ]
    }


    def calculate_witch_repertoire(level, INT, spell_slots_progression, witch_spells):
        slots = spell_slots_progression["Witch"].get(level, [])
        int_bonus = general_proficiency_bonus(INT)  # Mage-style INT bonus

        repertoire = {}

        for spell_level, slot_count in enumerate(slots, start=1):
            if slot_count <= 0:
                continue

            max_known = slot_count + int_bonus
            available_spells = witch_spells.get(spell_level, [])

            # losujemy bez powtórzeń
            known = random.sample(available_spells, min(max_known, len(available_spells)))
            repertoire[spell_level] = known

        return repertoire




    # GENEROWANIE REZULTATU
    p("--- CLASS AND LEVEL---")
    p(f"Class: {final_class}")
    p(f"Class Title: {class_title}")
    p(f"Level: {level}")
    p("Alignment:", alignment)

    if final_class == "Warlock":
        p(f"Dark Path: {warlock_path} ")

    if final_class == "Witch":
        p(f"Witch Tradition: {witch_tradition}")

    p("\n--- PRIME REQUISITES ---")
    p(prime_requisites[final_class])

    p("\n--- EXTRA REQUIREMENTS ---")
    if final_class == "Nobiran Wonderworker":
        p("All abilities must be at least 11")
    elif final_class in ("Dwarven Craftpriest", "Dwarven Vaultguard"):
        p("CON must be at least 9")
    elif final_class == "Zaharan Ruinguard":
        p("INT, WIL, CHA must be at least 9")
    else:
        p("None")

    total_hp, hp_gains, roll_log, con_log, bonus_log = calculate_hp_progression_table(final_class, stats["CON"], level)

    p("\n--- HIT POINTS ---")
    p(f"Final HP: {total_hp}")
    p("HP by level:")

    running = 0
    for lvl in range(1, level + 1):
        gain = hp_gains[lvl - 1]
        roll_sum = roll_log[lvl - 1]
        con_total = con_log[lvl - 1]
        bonus = bonus_log[lvl - 1]
        running += gain

        if lvl <= 9:
            # np. „Level 2: rolls 5 (2d4) + CON(+4) = +9 → 15 total”
            p(f" Level {lvl}: rolls {roll_sum} + CON total({con_total:+d})"
                  f"{' + bonus ' + str(bonus) if bonus else ''} = +{gain} → {running} total")
        else:
            p(f" Level {lvl}: rolls {roll_sum} + CON total({con_total:+d})"
                  f" + bonus {bonus} = +{gain} → {running} total")

    p("\n--- ATTRIBUTES ---")
    for k, v in stats.items():
        p(f"{k}: {v}")

    p("\n--- PHYSICAL FEATURES ---")
    p(f"CHA: {CHA} (modifier {cha_mod:+d})")
    for f in features:
        p(f" - {f}")

    p("\n--- LEVEL 1 PROFICIENCIES ---")

    p("\nClass Proficiency:")
    p(f" - {class_prof}")

    p("\nGeneral Proficiencies:")
    for g in general_picks:
        p(f" - {g}")

    # rozdziel auto-proficiencje z 1 poziomu i wyższych
    level1_auto = [prof for lvl, ptype, prof in auto_general_log if lvl == 1]
    auto_after_lvl1 = [(lvl, ptype, prof) for lvl, ptype, prof in auto_general_log if lvl > 1]

    if level1_auto:
        p("\nAutomatic Proficiencies from Class Powers:")
        for prof in level1_auto:
            p(f" - {prof}")

    if level > 1:
        p("\n--- PROFICIENCIES BY LEVEL ---")

        # auto_after_lvl1 zdefiniowaliśmy wyżej przy LEVEL 1
        combined_log = level_gains_log[:]  # kopia
        for lvl, ptype, prof in auto_after_lvl1:
            combined_log.append((lvl, "general_auto", prof))

        combined_log.sort(key=lambda x: x[0])

        if not combined_log:
            p("No additional proficiencies gained after level 1.")
        else:
            current_level = None
            for lvl, ptype, prof in combined_log:
                if lvl != current_level:
                    p(f"\nLevel {lvl}:")
                    current_level = lvl

                if ptype == "class":
                    p(f"  [Class]         {prof}")
                elif ptype == "general":
                    p(f"  [General]       {prof}")
                else:  # general_auto
                    p(f"  [General - Auto] {prof}")

    p("\n--- CLASS POWERS ---")

    if not class_powers_log:
        p("No class powers for this class.")
    else:
        current_level = None
        current_powers = []

        for pl, category, power in class_powers_log:
            if pl != current_level:
                if current_level is not None:
                    p(f"Level {current_level}: " + ", ".join(current_powers))
                current_level = pl
                current_powers = [power]
            else:
                current_powers.append(power)

        # flush ostatniego poziomu
        if current_level is not None:
            p(f"Level {current_level}: " + ", ".join(current_powers))

    # --- MUTATION DEEP DIVE ---
    if final_class == "Warlock" and mutation_log:
        p("\n--- WARLOCK MUTATIONS (Deep Dive) ---")
        for entry in mutation_log:
            idx = entry["index"]
            roll = entry["roll"]
            effect = entry["effect"]
            p(f"Mutation #{idx} (Roll {roll}): {effect}")

    known = calculate_known_spells(final_class, level, stats["INT"], spell_slots_progression)

    # -----------------------------
    # SPELL REPERTOIRE (conditional)
    # -----------------------------

    # Klasy mające repertuar arkany
    ARCANE_CLASSES = {
        "Mage", "Warlock",
        "Elven Nightblade", "Elven Spellsword",
        "Nobiran Wonderworker", "Zaharan Ruinguard"
    }

    # Klasy mające wiedzę w formie divine spell lists
    DIVINE_LIST_CLASSES = {
        "Shaman", "Priestess", "Crusader", "Bladedancer"
    }

    # Witch ma specjalny divine repertoire
    WITCH_CLASS = "Witch"

    # --- ARCANE REPERTOIRE ---
    if final_class in ARCANE_CLASSES:
        p("\n--- ARCANE REPERTOIRE (Known Spells) ---")

        known_spells = calculate_known_spells(
            final_class, level, stats["INT"], spell_slots_progression
        )

        if not known_spells:
            p("No arcane spells available at this level.")
        else:
            for lvl in sorted(known_spells.keys()):
                p(f"Level {lvl} spells ({len(known_spells[lvl])} known):")
                for s in known_spells[lvl]:
                    p(f"  • {s}")

    # --- SHAMAN ---
    if final_class == "Shaman":
        shaman_spells = calculate_shaman_spells(level, spell_slots_progression)
        p("\n--- SHAMAN DIVINE SPELLS KNOWN ---")
        for lvl in sorted(shaman_spells.keys()):
            p(f"Level {lvl} spells ({len(shaman_spells[lvl])} known):")
            for s in shaman_spells[lvl]:
                p(f"  • {s}")

    # --- PRIESTESS ---
    if final_class == "Priestess":
        priestess_spells = calculate_priestess_spells(level, spell_slots_progression)
        p("\n--- PRIESTESS DIVINE SPELLS KNOWN ---")
        for lvl in sorted(priestess_spells.keys()):
            p(f"Level {lvl} spells ({len(priestess_spells[lvl])} known):")
            for s in priestess_spells[lvl]:
                p(f"  • {s}")

    # --- CRUSADER ---
    if final_class == "Crusader":
        crusader_spells = calculate_crusader_spells(level, spell_slots_progression)
        p("\n--- CRUSADER DIVINE SPELLS KNOWN ---")
        for lvl in sorted(crusader_spells.keys()):
            p(f"Level {lvl} spells ({len(crusader_spells[lvl])} known):")
            for s in crusader_spells[lvl]:
                p(f"  • {s}")

    # --- BLADEDANCER ---
    if final_class == "Bladedancer":
        spells_known = calculate_bladedancer_spells(level, spell_slots_progression)
        p("\n--- BLADEDANCER DIVINE SPELLS KNOWN ---")
        for lvl in sorted(spells_known):
            p(f"Level {lvl} spells ({len(spells_known[lvl])} known):")
            for s in spells_known[lvl]:
                p(f"  • {s}")

    # --- WITCH (special divine repertoire) ---
    if final_class == "Witch":
        repertoire = calculate_witch_repertoire(
            level, stats["INT"], spell_slots_progression, witch_divine_spells
        )
        p("\n--- WITCH REPERTOIRE (Divine) ---")
        for lvl in sorted(repertoire):
            p(f"Level {lvl} spells ({len(repertoire[lvl])} known):")
            for s in repertoire[lvl]:
                p(f"  • {s}")

    # CLASS TEMPLATE / STARTOWE GP

    def roll_3d6():
        return sum(random.randint(1, 6) for _ in range(3))

    if level == 1:
        template_roll = roll_3d6()
        class_template_value = template_roll
        gold_pieces_value = template_roll * 10

        p("\n--- CLASS TEMPLATE OR STARTING GOLD PIECES ---")
        p(f"\nClass Template roll (3d6): {class_template_value}")
        p(f"Gold Pieces option (3d6 * 10): {gold_pieces_value} gp")
        p("Player chooses one of the above options.")

    p("\n--- MAGICAL ITEMS ---")

    if not magic_items:
        p("None")
    else:
        for item in magic_items:
            rarity = item["rarity"].replace("_", " ").title()
            name = item["name"]
            p(f"{rarity}: {name}")

    return out.getvalue()