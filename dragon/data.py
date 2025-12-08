# ============================================================
# HABITATS — unified keys & full ACKS mapping
# ============================================================

HABITATS = {
    "Wyrm": {
        "name": "Wyrm",
        "habitat_tags": ["shadowed", "blighted", "forsaken"],
        "colors": ["purple taupe", "liver", "charcoal", "black"],
        "breath": {
            "shape": "cloud",
            "area": "40' × 40'",
            "effect": "fetid gas"
        },
        "alignment": ["Chaotic"],   # ACKS: Wyrms are always chaotic
    },

    "Metallic": {
        "name": "Metallic Dragon",
        "habitat_tags": ["illuminated", "hallowed", "sacrosanct"],
        "colors": ["bronze", "silver", "electrum", "gold"],
        "breath": {
            "shape": "cone",
            "area": "90' × 30'",
            "effect": "golden fire"
        },
        "alignment": ["Lawful", "Neutral"],
    },

    "Blue": {
        "name": "Blue Dragon",
        "habitat_tags": ["aerial", "hilly", "lofty", "mountainous"],
        "colors": ["sky blue", "slate grey", "cloud white"],
        "breath": {
            "shape": "line",
            "area": "120' × 5'",
            "effect": "lightning bolt"
        },
        "alignment": ["Chaotic"],
    },

    "Brown": {
        "name": "Brown Dragon",
        "habitat_tags": ["arid", "barren", "bleak", "desolate"],
        "colors": ["burnt orange", "copper", "sandy brown"],
        "breath": {
            "shape": "cone",
            "area": "90' × 30'",
            "effect": "concussive blast"
        },
        "alignment": ["Neutral", "Chaotic"],
    },

    "Sea": {
        "name": "Sea Dragon",
        "habitat_tags": ["coastal", "littoral", "riverine", "oceanic"],
        "colors": ["sea green", "teal", "cerulean blue"],
        "breath": {
            "shape": "cloud",
            "area": "90' × 30'",
            "effect": "blistering steam"
        },
        "alignment": ["Neutral"],
    },

    "White": {
        "name": "White Dragon",
        "habitat_tags": ["frigid", "glacial", "icy", "snowy"],
        "colors": ["ivory", "pearl", "snow white"],
        "breath": {
            "shape": "cloud",
            "area": "90' × 30'",
            "effect": "freezing vapor"
        },
        "alignment": ["Chaotic"],
    },

    "Red": {
        "name": "Red Dragon",
        "habitat_tags": ["fire-scarred", "sweltering", "volcanic"],
        "colors": ["flaming red", "burnt orange", "charcoal"],
        "breath": {
            "shape": "cone",
            "area": "90' × 30'",
            "effect": "flame"
        },
        "alignment": ["Chaotic"],
    },

    "Green": {
        "name": "Green Dragon",
        "habitat_tags": ["forested", "jungled", "overgrown", "wild"],
        "colors": ["moss green", "olive", "forest green"],
        "breath": {
            "shape": "cloud",
            "area": "40' × 40'",
            "effect": "poison vapor"
        },
        "alignment": ["Chaotic"],
    },

    "Black": {
        "name": "Black Dragon",
        "habitat_tags": ["swampy", "soggy", "pestilent", "wet"],
        "colors": ["green-grey", "midnight green", "black"],
        "breath": {
            "shape": "line",
            "area": "120' × 5'",
            "effect": "acid"
        },
        "alignment": ["Chaotic"],
    },
}

# ============================================================
# BODY FORMS — with metadata (tail/claws/winged)
# ============================================================

BODY_FORMS = {
    "Guivre": {
        "routine": ["bite", "tail"],
        "has_claws": False,
        "has_tail": True,
        "winged": False,
        "damage": {
            "Spawn": ("1d6", "1d6"),
            "Very Young": ("1d8", "1d8"),
            "Young": ("1d10", "1d10"),
            "Juvenile": ("2d6", "2d6"),
            "Adult": ("2d8", "2d8"),
            "Mature Adult": ("3d6", "3d6"),
            "Old": ("3d6+1", "3d6+1"),
            "Very Old": ("4d6", "4d6"),
            "Ancient": ("4d6+1", "4d6+1"),
            "Venerable": ("5d6", "5d6"),
        },
    },

    "Lindworm": {
        "routine": ["bite"],
        "has_claws": False,
        "has_tail": True,
        "winged": False,
        "damage": {
            "Spawn": "2d6",
            "Very Young": "2d8",
            "Young": "2d10",
            "Juvenile": "3d8",
            "Adult": "3d10",
            "Mature Adult": "6d6",
            "Old": "7d6",
            "Very Old": "8d6",
            "Ancient": "9d6",
            "Venerable": "10d6",
        },
    },

    "Wyvern": {
        "routine": ["bite", "tail"],
        "has_claws": True,
        "has_tail": True,
        "winged": True,
        "damage": {
            "Spawn": ("1d6", "1d6"),
            "Very Young": ("1d8", "1d8"),
            "Young": ("1d10", "1d10"),
            "Juvenile": ("2d6", "2d6"),
            "Adult": ("2d8", "2d8"),
            "Mature Adult": ("3d6", "3d6"),
            "Old": ("3d6+1", "3d6+1"),
            "Very Old": ("4d6", "4d6"),
            "Ancient": ("4d6+1", "4d6+1"),
            "Venerable": ("5d6", "5d6"),
        },
    },

    "Drake": {
        "routine": ["claw", "claw", "bite"],
        "has_claws": True,
        "has_tail": False,
        "winged": True,
        "damage": {
            "Spawn": ("1d2", "1d2", "2d3"),
            "Very Young": ("1d3", "1d3", "2d4"),
            "Young": ("1d4", "1d4", "2d6"),
            "Juvenile": ("1d6", "1d6", "2d8"),
            "Adult": ("2d3", "2d3", "2d10"),
            "Mature Adult": ("1d8", "1d8", "3d8"),
            "Old": ("2d4", "2d4", "3d10"),
            "Very Old": ("1d10", "1d10", "4d8"),
            "Ancient": ("1d12", "1d12", "4d10"),
            "Venerable": ("3d4", "3d4", "5d8"),
        },
    },
}

# ============================================================
# AGE CATEGORIES — cleaned (no Massive presets)
# ============================================================

AGE_DATA = {
    "Spawn": {
        "years": (1, 5),
        "size": "Large (40 st.)",
        "ac": 3,
        "hd": 2,
        "save_as": "F2",
        "morale": 0,
        "normal_load": 8,
        "speech_chance": 0.01,
        "special_abilities": 1,
        "spells": [1, 0, 0, 0, 0],
    },

    "Very Young": {
        "years": (6, 15),
        "size": "Huge (150 st.)",
        "ac": 4,
        "hd": 4,
        "save_as": "F4",
        "morale": 0,
        "normal_load": 30,
        "speech_chance": 0.02,
        "special_abilities": 1,
        "spells": [2, 0, 0, 0, 0],
    },

    "Young": {
        "years": (16, 25),
        "size": "Huge (330 st.)",
        "ac": 5,
        "hd": 6,
        "save_as": "F6",
        "morale": 0,
        "normal_load": 65,
        "speech_chance": 0.05,
        "special_abilities": 1,
        "spells": [2, 1, 0, 0, 0],
    },

    "Juvenile": {
        "years": (26, 50),
        "size": "Huge (590 st.)",
        "ac": 6,
        "hd": 8,
        "save_as": "F8",
        "morale": 0,
        "normal_load": 120,
        "speech_chance": 0.10,
        "special_abilities": 1,
        "spells": [2, 2, 0, 0, 0],
    },

    "Adult": {
        "years": (51, 75),
        "size": "Gigantic (900 st.)",
        "ac": 7,
        "hd": 10,
        "save_as": "F10",
        "morale": 1,
        "normal_load": 180,
        "speech_chance": 0.20,
        "special_abilities": 2,
        "spells": [2, 2, 1, 0, 0],
    },

    "Mature Adult": {
        "years": (76, 100),
        "size": "Gigantic (1,300 st.)",
        "ac": 8,
        "hd": 12,
        "save_as": "F12",
        "morale": 1,
        "normal_load": 260,
        "speech_chance": 0.35,
        "special_abilities": 2,
        "spells": [2, 2, 2, 0, 0],
    },

    "Old": {
        "years": (101, 200),
        "size": "Gigantic (1,775 st.)",
        "ac": 9,
        "hd": 14,
        "save_as": "F14",
        "morale": 1,
        "normal_load": 350,
        "speech_chance": 0.50,
        "special_abilities": 2,
        "spells": [3, 2, 2, 1, 0],
    },

    "Very Old": {
        "years": (201, 400),
        "size": "Colossal (2,300 st.)",
        "ac": 10,
        "hd": 16,
        "save_as": "F16",
        "morale": 2,
        "normal_load": 460,
        "speech_chance": 0.75,
        "special_abilities": 3,
        "spells": [3, 3, 2, 2, 0],
    },

    "Ancient": {
        "years": (401, 700),
        "size": "Colossal (3,000 st.)",
        "ac": 11,
        "hd": 18,
        "save_as": "F18",
        "morale": 2,
        "normal_load": 585,
        "speech_chance": 1.00,
        "special_abilities": 4,
        "spells": [3, 3, 3, 2, 1],
    },

    "Venerable": {
        "years": (701, None),
        "size": "Colossal (3,600 st.)",
        "ac": 12,
        "hd": 20,
        "save_as": "F20",
        "morale": 3,
        "normal_load": 720,
        "speech_chance": 1.00,
        "special_abilities": 5,
        "spells": [3, 3, 3, 3, 2],
    },
}

# ============================================================
# ENCOUNTER DATA — cleaned
# ============================================================

ENCOUNTER_DATA = {
    "Spawn": {
        "lair_chance": 0.90,
        "dungeon_enc": "1d4",
        "wilderness_enc": "1d4",
        "caught_asleep": 0.80,
        "treasure_type": ["B"],
        "xp_speechless": 38,
        "xp_speaking": 47,
    },

    "Very Young": {
        "lair_chance": 0.70,
        "dungeon_enc": "1d4",
        "wilderness_enc": "1d4",
        "caught_asleep": 0.70,
        "treasure_type": ["H"],
        "xp_speechless": 190,
        "xp_speaking": 245,
    },

    "Young": {
        "lair_chance": 0.50,
        "dungeon_enc": "1d4",
        "wilderness_enc": "1d4",
        "caught_asleep": 0.60,
        "treasure_type": ["N"],
        "xp_speechless": 820,
        "xp_speaking": 1070,
    },

    "Juvenile": {
        "lair_chance": 0.40,
        "dungeon_enc": "1d4",
        "wilderness_enc": "1d4",
        "caught_asleep": 0.50,
        "treasure_type": ["Q"],
        "xp_speechless": 1600,
        "xp_speaking": 2100,
    },

    "Adult": {
        "lair_chance": 0.40,
        "dungeon_enc": "1d4",
        "wilderness_enc": "1d4",
        "caught_asleep": 0.40,
        "treasure_type": ["Q", "N"],
        "xp_speechless": 2950,
        "xp_speaking": 3650,
    },

    "Mature Adult": {
        "lair_chance": 0.30,
        "dungeon_enc": "1d4",
        "wilderness_enc": "1d4",
        "caught_asleep": 0.30,
        "treasure_type": ["Q", "N"],
        "xp_speechless": 3900,
        "xp_speaking": 4800,
    },

    "Old": {
        "lair_chance": 0.40,
        "dungeon_enc": "1d2",
        "wilderness_enc": "1d2",
        "caught_asleep": 0.20,
        "treasure_type": ["R"],
        "xp_speechless": 4900,
        "xp_speaking": 6000,
    },

    "Very Old": {
        "lair_chance": 0.50,
        "dungeon_enc": "1d2",
        "wilderness_enc": "1d2",
        "caught_asleep": 0.10,
        "treasure_type": ["R"],
        "xp_speechless": 7200,
        "xp_speaking": 8500,
    },

    "Ancient": {
        "lair_chance": 0.70,
        "dungeon_enc": "1d2",
        "wilderness_enc": "1d2",
        "caught_asleep": 0.05,
        "treasure_type": ["R", "N"],
        "xp_speechless": None,
        "xp_speaking": 11400,
    },

    "Venerable": {
        "lair_chance": 0.90,
        "dungeon_enc": "1",
        "wilderness_enc": "1",
        "caught_asleep": 0.00,
        "treasure_type": ["R", "N"],
        "xp_speechless": None,
        "xp_speaking": 15400,
    },
}
# ============================================================
# SPECIAL ABILITIES — full structured dataset
# ============================================================

SPECIAL_ABILITIES = {
    "Breath Weapon": {
        "cost": 1,
        "requires": {
            "breath_weapon": True
        },
        "description": "The dragon gains the breath weapon appropriate to its habitat."
    },

    "Clutching Claws": {
        "cost": 0.5,
        "requires": {
            "body_forms": ["Drake", "Wyvern"],  # must have claws/talons
        },
        "description": (
            "Dragon may dive attack with claws/talons, dealing double damage. "
            "On hit with both claws vs smaller creature, Paralysis save or grabbed."
        ),
    },

    "Constriction": {
        "cost": 1,
        "requires": {
            "tail_attack": True,  # implied; body forms with tails: Guivre, Lindworm, Wyvern
        },
        "description": (
            "On a successful tail attack, restrains smaller creature, dealing tail damage each round."
        ),
    },

    "Decapitating Bite": {
        "cost": 1,
        "requires": {},
        "description": (
            "On unmodified 20, checks for decapitation (Death save or die). "
            "Gigantic: 19–20, Colossal: 18–20."
        ),
    },

    "Draconic Persuasion": {
        "cost": 1,
        "requires": {
            "speech": True
        },
        "description": (
            "Creatures must save vs Spells or be bewitched. Immune for 1 turn on success."
        ),
    },

    "Elemental Aura": {
        "cost": 1,
        "requires": {
            "breath_weapon": True
        },
        "description": (
            "Aura of habitat energy; radius 1'/HD (rounded to nearest 5'). "
            "Damages like drake claw attack each round."
        ),
    },

    "Gem-Encrusted Hide": {
        "cost": 1,
        "requires": {},
        "description": (
            "Hide coated in treasure. +4 AC (+5 at Very Old, +6 at Venerable). "
            "Land speed -30'."
        ),
    },

    "Horrific Stench": {
        "cost": 1,
        "requires": {},
        "description": (
            "Creatures within 20’ save vs Death or become queasy (−3 to attacks, proficiencies, damage). "
            "Penalty worsens by age."
        ),
    },

    "Lightning Reflexes": {
        "cost": 0.25,
        "requires": {},
        "description": "+2 to initiative rolls."
    },

    "Massive Size": {
        "cost": 1,
        "requires": {},
        "description": (
            "Dragon increases HD by +2 and damage scales accordingly. "
            "May be taken multiple times."
        ),
    },

    "Invulnerable": {
        "cost": 1,
        "requires": {},
        "description": "Immune to mundane damage."
    },

    "Paralyzing Blows": {
        "cost": 1,
        "requires": {
            "alignment": ["Chaotic"]
        },
        "description": (
            "Up to three attacks cause paralysis unless Paralysis save succeeds. "
            "Penalty depends on number of attacks."
        )
    },

    "Poisonous Blood": {
        "cost": 1,
        "requires": {},
        "description": (
            "Anyone striking the dragon in melee saves vs Death or dies from venomous blood. "
            "Penalty increases with age."
        )
    },

    "Proficiency": {
        "cost": 0.125,
        "requires": {},
        "description": "Dragon gains one class proficiency."
    },

    "Resistant": {
        "cost": 0.5,
        "requires": {},
        "description": "Dragon gains resistance to mundane damage."
    },

    "Stealthy": {
        "cost": 0.125,
        "requires": {},
        "description": (
            "Dragon is harder to detect in its natural habitat; -2 penalty to encounter surprise rolls."
        )
    },

    "Swallow Attack": {
        "cost": 1,
        "requires": {},
        "description": (
            "On unmodified 20 (modified by size), dragon may swallow targets two sizes smaller."
        )
    },

    "Swift": {
        "cost": 0.25,
        "requires": {},
        "description": (
            "Dragon moves rapidly; exploration and combat speeds improved."
        )
    },

    "Tail Lash": {
        "cost": 1,
        "requires": {
            "body_forms": ["Lindworm", "Drake"],
        },
        "description": (
            "Dragon gains an additional rear tail attack (guivre-form tail damage)."
        )
    },

    "Terrifying Charge": {
        "cost": 1,
        "requires": {},
        "description": (
            "Charge/dive forces Paralysis saves or fear; scaling effect depending on target HD."
        )
    },

    "Trample": {
        "cost": 0.25,
        "requires": {},
        "description": (
            "Dragon may trample instead of normal attacks; deals guivre-form bite damage."
        )
    },

    "Transformation": {
        "cost": 1,
        "requires": {
            "spellcasting": True
        },
        "description": (
            "Dragon can transform into humanoid or animal (guise self / skinchange)."
        )
    },

    "Venomous Bite or Tail": {
        "cost": 1,
        "requires": {},
        "description": (
            "Bite or tail delivers lethal poison (Death save, penalty increases by age)."
        )
    },

    "Wing/Arm Claws": {
        "cost": 1,
        "requires": {
            "body_forms": ["Guivre", "Lindworm", "Wyvern", "Drake"],
            # filtering handled later because each body form has winged/wingless variants
        },
        "description": (
            "Additional melee attacks with wing/arm claws (drake claw damage)."
        )
    },
}

# ============================================================
# BREATH WEAPONS — keys unified with HABITATS
# ============================================================

BREATH_WEAPONS = {
    "Wyrm": {
        "shape": "cloud",
        "area": "40' × 40'",
        "damage_type": "fetid gas",
    },

    "Metallic": {
        "shape": "cone",
        "area": "90' × 30'",
        "damage_type": "golden fire",
    },

    "Blue": {
        "shape": "line",
        "area": "120' × 5'",
        "damage_type": "lightning bolt",
    },

    "Brown": {
        "shape": "cone",
        "area": "90' × 30'",
        "damage_type": "concussive blast",
    },

    "Sea": {
        "shape": "cloud",
        "area": "90' × 30'",
        "damage_type": "blistering steam",
    },

    "White": {
        "shape": "cloud",
        "area": "90' × 30'",
        "damage_type": "freezing vapor",
    },

    "Red": {
        "shape": "cone",
        "area": "90' × 30'",
        "damage_type": "flame",
    },

    "Green": {
        "shape": "cloud",
        "area": "40' × 40'",
        "damage_type": "poison vapor",
    },

    "Black": {
        "shape": "line",
        "area": "120' × 5'",
        "damage_type": "acid",
    },
}

BREATH_USE_MODES = {
    "limited": {
        "label": "3/day",
    },
    "recharging": {
        "label": "recharges 1d6 rounds",
    }
}

# ============================================================
# LEGENDARY DRAGON RULES — unchanged
# ============================================================

LEGENDARY_RULES = {
    "increment_years": 700,
    "hd_per_increment": 2,
    "ac_per_increment": 1,
    "extra_damage_per_increment": 4,
}