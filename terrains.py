# terrains.py

# Canonical terrain groups (using RAW variants, not abstract categories)

TERRAIN_GROUPS = {
    "barrens": [
        "Barrens (Rocky/Sandy)",
        "Barrens (Tundra)"
    ],

    "desert": [
        "Desert (Rocky)",
        "Desert (Sandy)"
    ],

    "forest": [
        "Forest (Deciduous)",
        "Forest (Taiga)"
    ],

    "grassland": [
        "Grassland (Farmland/Prairie)",
        "Grassland (Savannah)",
        "Grassland (Steppe)"
    ],

    "hills": [
        "Hills (Forested)",
        "Hills (Rocky)"
    ],

    "jungle": [
        "Jungle (Any)"
    ],

    "mountains": [
        "Mountains (Forested)",
        "Mountains (Rocky)",
        "Mountains (Snowy)",
        "Mountains (Volcanic)"
    ],

    "rivers": [
        "River (Any But Desert or Jungle)",
        "River (Desert and Jungle)"
    ],

    "scrubland": [
        "Scrubland (Sparse)",
        "Scrubland (Dense)"
    ],

    "swamp": [
        "Swamp (Any)"
    ],
}

# Flat list of all canonical terrain types
TERRAINS = [t for group in TERRAIN_GROUPS.values() for t in group]

# For quick membership checks
TERRAIN_SET = set(TERRAINS)

# maps canonical names -> snake_case IDs
TERRAIN_ALIASES = {
    "Barrens (Rocky/Sandy)": "barrens_rocky_sandy",
    "Barrens (Tundra)": "barrens_tundra",

    "Desert (Rocky)": "desert_rocky",
    "Desert (Sandy)": "desert_sandy",

    "Forest (Deciduous)": "forest_deciduous",
    "Forest (Taiga)": "forest_taiga",

    "Grassland (Farmland/Prairie)": "grassland_farmland",
    "Grassland (Savannah)": "grassland_savannah",
    "Grassland (Steppe)": "grassland_steppe",

    "Hills (Forested)": "hills_forested",
    "Hills (Rocky)": "hills_rocky",

    "Jungle (Any)": "jungle",

    "Mountains (Forested)": "mountains_forested",
    "Mountains (Rocky)": "mountains_rocky",
    "Mountains (Snowy)": "mountains_snowy",
    "Mountains (Volcanic)": "mountains_volcanic",

    "River (Any But Desert or Jungle)": "river_temperate",
    "River (Desert and Jungle)": "river_exotic",

    "Scrubland (Sparse)": "scrubland_sparse",
    "Scrubland (Dense)": "scrubland_dense",

    "Swamp (Any)": "swamp",
}

# Reverse mapping for alias -> canonical name
ALIAS_TO_CANONICAL = {v: k for k, v in TERRAIN_ALIASES.items()}


def normalize_terrain(name: str) -> str:
    """
    Returns the canonical terrain name.
    Accepts either canonical names or snake_case aliases.
    Raises ValueError if unknown.
    """
    if name in TERRAIN_SET:
        return name

    if name in ALIAS_TO_CANONICAL:
        return ALIAS_TO_CANONICAL[name]

    raise ValueError(f"Unknown terrain name or alias: {name}")


def terrain_id(name: str) -> str:
    """
    Returns the snake_case terrain ID (alias).
    Accepts either canonical names or aliases.
    """
    if name in ALIAS_TO_CANONICAL:
        return name

    if name in TERRAIN_ALIASES:
        return TERRAIN_ALIASES[name]

    raise ValueError(f"Unknown terrain name or alias: {name}")
