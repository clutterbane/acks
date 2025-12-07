# occupations_data.py

OCCUPATIONS = {
    "Entertainer": [
        {
            "name": "Actor",
            "proficiencies": [
                {"name": "Performance", "specialization": "acting"},
                {"name": "Folkways"},
                {"name": "Streetwise"},
                {"name": "Weapon Proficiency", "weapons": ["swords", "daggers"]},
            ]
        },
        {
            "name": "Dancer",
            "proficiencies": [
                {"name": "Performance", "specialization": "dance"},
                {"name": "Folkways"},
                {"name": "Seduction"},
                {"name": "Streetwise"},
            ]
        },
        {
            "name": "Musician",
            "proficiencies": [
                {"name": "Performance", "specialization": "sing/instrument"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Streetwise"},
            ]
        },
        {
            "name": "Singer",
            "proficiencies": [
                {"name": "Performance", "specialization": "sing/instrument"},
                {"name": "Folkways"},
                {"name": "Seduction"},
                {"name": "Streetwise"},
            ]
        },
        {
            "name": "Carouser",
            "proficiencies": [
                {"name": "Gambling"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Streetwise"},
            ]
        },
    ],

    # ---------------------------------------------------------------------------------------

     "Merchant": [
        {
            "name": "Bookseller",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Craft", "specialization": "scribe"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Chandler/Upholder",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Craft", "specialization": "candlemaking"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Coppermonger",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Craft", "specialization": "coppersmithing"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Cornmonger",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Labor", "specialization": "farming"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Draper",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Craft", "specialization": "weaving"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Fishmonger",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Labor", "specialization": "fishing"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Fripperer",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Craft", "specialization": "tailoring"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Furrier",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Trapping"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Greengrocer",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Labor", "specialization": "farming"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Horsemonger",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Animal Training"},
                {"name": "Bargaining"},
                {"name": "Riding"},
            ]
        },
        {
            "name": "Ironmonger",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Craft", "specialization": "blacksmithing"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Lawyer",
            "proficiencies": [
                {"name": "Profession", "specialization": "lawyer"},
                {"name": "Bargaining"},
                {"name": "Diplomacy"},
                {"name": "Intimidation"},
            ]
        },
        {
            "name": "Lumbermonger",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Bargaining"},
                {"name": "Labor", "specialization": "lumberjacking"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Mercer",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Craft", "specialization": "weaving"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Oilmonger",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Craft", "specialization": "bottling"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Peltmonger / Skinner",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Craft", "specialization": "tanning"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Poulterer",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Animal Husbandry"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Salter / Pepperer",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Craft", "specialization": "cooking"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Vintner",
            "proficiencies": [
                {"name": "Profession", "specialization": "merchant"},
                {"name": "Craft", "specialization": "winemaking"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
    ],

    "Artisan": [
        {
            "name": "Apothecary",
            "proficiencies": [
                {"name": "Craft", "specialization": "herbalist"},
                {"name": "Folkways"},
                {"name": "Naturalism"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Armorer",
            "proficiencies": [
                {"name": "Craft", "specialization": "armorsmithing"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Weapon Proficiency", "weapons": ["bludgeons"]},
            ]
        },
        {
            "name": "Baker",
            "proficiencies": [
                {"name": "Craft", "specialization": "baking"},
                {"name": "Labor", "specialization": "scullery"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Blacksmith",
            "proficiencies": [
                {"name": "Craft", "specialization": "blacksmithing"},
                {"name": "Labor", "specialization": "bellows"},
                {"name": "Folkways"},
                {"name": "Weapon Proficiency", "weapons": ["bludgeons"]},
            ]
        },
        {
            "name": "Bookbinder",
            "proficiencies": [
                {"name": "Craft", "specialization": "bookbinding"},
                {"name": "Art", "specialization": "embossing"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Bowyer/Fletcher",
            "proficiencies": [
                {"name": "Craft", "specialization": "fletching"},
                {"name": "Folkways"},
                {"name": "Naturalism"},
                {"name": "Weapon Proficiency", "weapons": ["bows", "crossbows"]},
            ]
        },
        {
            "name": "Brewer",
            "proficiencies": [
                {"name": "Craft", "specialization": "brewing"},
                {"name": "Labor", "specialization": "milling/mashing"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Brickmaker",
            "proficiencies": [
                {"name": "Craft", "specialization": "brickmaking"},
                {"name": "Folkways"},
                {"name": "Labor", "specialization": "bricklaying"},
                {"name": "Weapon Proficiency", "weapons": ["bludgeons"]},
            ]
        },
        {
            "name": "Butcher",
            "proficiencies": [
                {"name": "Labor", "specialization": "butchery"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Weapon Proficiency", "weapons": ["swords", "daggers"]},
            ]
        },
        {
            "name": "Cabinetmaker",
            "proficiencies": [
                {"name": "Craft", "specialization": "cabinetmaking"},
                {"name": "Folkways"},
                {"name": "Labor", "specialization": "installation"},
                {"name": "Weapon Proficiency", "weapons": ["axes", "bludgeons"]},
            ]
        },
        {
            "name": "Candlemaker",
            "proficiencies": [
                {"name": "Craft", "specialization": "candlemaking"},
                {"name": "Labor", "specialization": "rendering"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Capper/Hatter",
            "proficiencies": [
                {"name": "Craft", "specialization": "hatting"},
                {"name": "Art", "specialization": "ornamentation"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Carpenter",
            "proficiencies": [
                {"name": "Craft", "specialization": "carpentry"},
                {"name": "Labor", "specialization": "installation"},
                {"name": "Folkways"},
                {"name": "Weapon Proficiency", "weapons": ["axes", "bludgeons"]},
            ]
        },
        {
            "name": "Chaloner/Tapicer",
            "proficiencies": [
                {"name": "Craft", "specialization": "upholstering"},
                {"name": "Labor", "specialization": "heaving/stowing"},
                {"name": "Folkways"},
                {"name": "Weapon Proficiency", "weapons": ["bludgeons"]},
            ]
        },
        {
            "name": "Clothmaker",
            "proficiencies": [
                {"name": "Craft", "specialization": "weaving"},
                {"name": "Craft", "specialization": "spinning"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Cobbler/Cordwainer",
            "proficiencies": [
                {"name": "Craft", "specialization": "cobblery"},
                {"name": "Art", "specialization": "ornamentation"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Confectioner",
            "proficiencies": [
                {"name": "Craft", "specialization": "confectionary"},
                {"name": "Labor", "specialization": "scullery"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Cooper",
            "proficiencies": [
                {"name": "Craft", "specialization": "cooping"},
                {"name": "Labor", "specialization": "heaving/stowing"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Coppersmith",
            "proficiencies": [
                {"name": "Craft", "specialization": "coppersmithing"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Weapon Proficiency", "weapons": ["bludgeons"]},
            ]
        },
        {
            "name": "Corder/Ropemaker",
            "proficiencies": [
                {"name": "Craft", "specialization": "ropemaking"},
                {"name": "Labor", "specialization": "heaving/stowing"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Decorative Artist",
            "proficiencies": [
                {"name": "Art", "specialization": "any"},
                {"name": "Craft", "specialization": "related to art"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Florist",
            "proficiencies": [
                {"name": "Art", "specialization": "floral arrangement"},
                {"name": "Folkways"},
                {"name": "Naturalism"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Gemcutter",
            "proficiencies": [
                {"name": "Craft", "specialization": "gemcutting"},
                {"name": "Art", "specialization": "ornamentation"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Glassworker",
            "proficiencies": [
                {"name": "Craft", "specialization": "glassworking"},
                {"name": "Art", "specialization": "ornamentation"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Goldsmith",
            "proficiencies": [
                {"name": "Craft", "specialization": "goldsmithing"},
                {"name": "Art", "specialization": "ornamentation"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Hornworker",
            "proficiencies": [
                {"name": "Craft", "specialization": "hornworking"},
                {"name": "Art", "specialization": "ornamentation"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Illuminator",
            "proficiencies": [
                {"name": "Art", "specialization": "illumination"},
                {"name": "Craft", "specialization": "scribe"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Jeweler",
            "proficiencies": [
                {"name": "Art", "specialization": "jewelry"},
                {"name": "Craft", "specialization": "goldsmithing or silversmithing"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Locksmith",
            "proficiencies": [
                {"name": "Craft", "specialization": "locksmithing"},
                {"name": "Lockpicking", "as": "1st level thief"},
                {"name": "Folkways"},
                {"name": "Streetwise"},
            ]
        },
        {
            "name": "Mason",
            "proficiencies": [
                {"name": "Craft", "specialization": "masonry"},
                {"name": "Endurance"},
                {"name": "Folkways"},
                {"name": "Labor", "specialization": "bricklaying"},
            ]
        },
        {
            "name": "Parchmentmaker",
            "proficiencies": [
                {"name": "Craft", "specialization": "parchmentmaking"},
                {"name": "Labor", "specialization": "butchery"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Perfumer",
            "proficiencies": [
                {"name": "Craft", "specialization": "perfumery"},
                {"name": "Folkways"},
                {"name": "Naturalism"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Potter",
            "proficiencies": [
                {"name": "Craft", "specialization": "pottery"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Saddler/Fuster",
            "proficiencies": [
                {"name": "Craft", "specialization": "saddlery"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Riding"},
            ]
        },
        {
            "name": "Scribe",
            "proficiencies": [
                {"name": "Craft", "specialization": "scribe"},
                {"name": "Art", "specialization": "illumination"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Shipwright",
            "proficiencies": [
                {"name": "Craft", "specialization": "shipwrighting"},
                {"name": "Folkways"},
                {"name": "Seafaring"},
                {"name": "Siege Engineering"},
            ]
        },
        {
            "name": "Silversmith",
            "proficiencies": [
                {"name": "Craft", "specialization": "silversmithing"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
                {"name": "Weapon Proficiency", "weapons": ["bludgeons"]},
            ]
        },
        {
            "name": "Spinner",
            "proficiencies": [
                {"name": "Craft", "specialization": "spinning"},
                {"name": "Craft", "specialization": "weaving"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Tailor/Seamstress",
            "proficiencies": [
                {"name": "Craft", "specialization": "tailoring"},
                {"name": "Craft", "specialization": "weaving"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Tanner/Tawer",
            "proficiencies": [
                {"name": "Craft", "specialization": "tanning"},
                {"name": "Labor", "specialization": "butchery"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Taxidermist",
            "proficiencies": [
                {"name": "Craft", "specialization": "taxidermy"},
                {"name": "Labor", "specialization": "butchery"},
                {"name": "Animal Husbandry"},
                {"name": "Naturalism"},
            ]
        },
        {
            "name": "Tinker/Toymaker",
            "proficiencies": [
                {"name": "Craft", "specialization": "toymaking"},
                {"name": "Folkways"},
                {"name": "Performance", "specialization": "puppetry"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Wainwright",
            "proficiencies": [
                {"name": "Craft", "specialization": "wainwrighting"},
                {"name": "Driving"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Weaponsmith",
            "proficiencies": [
                {"name": "Craft", "specialization": "weaponsmithing"},
                {"name": "Folkways"},
                {"name": "Weapon Proficiency", "weapons": ["any 2"]},
            ]
        },
        {
            "name": "Wheelwright",
            "proficiencies": [
                {"name": "Craft", "specialization": "wheelwrighting"},
                {"name": "Driving"},
                {"name": "Folkways"},
                {"name": "Revelry"}]
        },
    ],
    "Hosteller": [
        {
            "name": "Brothelkeeper",
            "proficiencies": [
                {"name": "Profession", "specialization": "brothelkeeper"},
                {"name": "Folkways"},
                {"name": "Intimidation"},
                {"name": "Streetwise"},
                {"name": "Weapon Proficiency", "weapons": ["club", "dagger", "sap", "whip"]},
            ]
        },
        {
            "name": "Cantinakeeper",
            "proficiencies": [
                {"name": "Profession", "specialization": "cantinakeeper"},
                {"name": "Folkways"},
                {"name": "Labor", "specialization": "cooking"},
                {"name": "Revelry"},
                {"name": "Streetwise"},
            ]
        },
        {
            "name": "Innkeeper",
            "proficiencies": [
                {"name": "Profession", "specialization": "innkeeper"},
                {"name": "Craft", "specialization": "brewing"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Streetwise"},
            ]
        },
        {
            "name": "Tavernkeeper",
            "proficiencies": [
                {"name": "Profession", "specialization": "tavernkeeper"},
                {"name": "Craft", "specialization": "brewing"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Streetwise"},
            ]
        },
    ],
    "Laborer": [
        {
            "name": "Barber",
            "proficiencies": [
                {"name": "Labor", "specialization": "barbering"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Weapon Proficiency", "weapons": ["swords", "daggers"]},
            ]
        },
        {
            "name": "Bath Attendant/Masseuse",
            "proficiencies": [
                {"name": "Labor", "specialization": "massage"},
                {"name": "Labor", "specialization": "valeting"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Bricklayer",
            "proficiencies": [
                {"name": "Labor", "specialization": "bricklaying"},
                {"name": "Endurance"},
                {"name": "Folkways"},
                {"name": "Weapon Proficiency", "weapons": ["bludgeons"]},
            ]
        },
        {
            "name": "Cook",
            "proficiencies": [
                {"name": "Labor", "specialization": "cooking"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Weapon Proficiency", "weapons": ["swords", "daggers"]},
            ]
        },
        {
            "name": "Dockworker",
            "proficiencies": [
                {"name": "Labor", "specialization": "heaving/stowing"},
                {"name": "Folkways"},
                {"name": "Streetwise"},
                {"name": "Weapon Proficiency", "weapons": ["club", "hand axe", "net", "staff"]},
            ]
        },
        {
            "name": "Fuller/Launderer",
            "proficiencies": [
                {"name": "Labor", "specialization": "fulling"},
                {"name": "Labor", "specialization": "laundry"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Gondolier/Rower",
            "proficiencies": [
                {"name": "Seafaring"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Weapon Proficiency", "weapons": ["club", "hand axe", "net", "staff"]},
            ]
        },
        {
            "name": "Gongfarmer/Streetcleaner",
            "proficiencies": [
                {"name": "Labor", "specialization": "gongfarming"},
                {"name": "Endurance"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Hawker",
            "proficiencies": [
                {"name": "Labor", "specialization": "hawking"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Hostler/Stablehand",
            "proficiencies": [
                {"name": "Labor", "specialization": "grooming"},
                {"name": "Driving"},
                {"name": "Folkways"},
                {"name": "Riding"},
            ]
        },
        {
            "name": "Maidservant",
            "proficiencies": [
                {"name": "Labor", "specialization": "housekeeping"},
                {"name": "Labor", "specialization": "laundry"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Prostitute",
            "proficiencies": [
                {"name": "Seduction"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Streetwise"},
            ]
        },
        {
            "name": "Ratcatcher",
            "proficiencies": [
                {"name": "Tracking"},
                {"name": "Trapping"},
                {"name": "Folkways"},
                {"name": "Streetwise"},
            ]
        },
        {
            "name": "Roofer/Tiler",
            "proficiencies": [
                {"name": "Labor", "specialization": "roofing/tiling"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Weapon Proficiency", "weapons": ["bludgeons"]},
            ]
        },
        {
            "name": "Sailor/Fisher",
            "proficiencies": [
                {"name": "Seafaring"},
                {"name": "Labor", "specialization": "heaving/stowing"},
                {"name": "Revelry"},
                {"name": "Weapon Proficiency", "weapons": ["club", "hand axe", "net", "staff"]},
            ]
        },
        {
            "name": "Scullion",
            "proficiencies": [
                {"name": "Labor", "specialization": "scullery"},
                {"name": "Endurance"},
                {"name": "Folkways"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Sawyer/Woodcutter",
            "proficiencies": [
                {"name": "Labor", "specialization": "woodcutting"},
                {"name": "Endurance"},
                {"name": "Fighting Style Proficiency", "style": "two-handed weapon"},
                {"name": "Weapon Proficiency", "weapons": ["axes"]},
            ]
        },
        {
            "name": "Teamster",
            "proficiencies": [
                {"name": "Driving"},
                {"name": "Labor", "specialization": "heaving/stowing"},
                {"name": "Folkways"},
                {"name": "Streetwise"},
            ]
        },
        {
            "name": "Tavernworker",
            "proficiencies": [
                {"name": "Labor", "specialization": "tavernworking"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Streetwise"},
            ]
        },
        {
            "name": "Unskilled Laborer",
            "proficiencies": [
                {"name": "Endurance"},
                {"name": "Folkways"},
                {"name": "Revelry"},
                {"name": "Streetwise"},
            ]
        },
    ],

    "Minor Ecclesiastics": [
        {
            "name": "Almsgiver/Missionary",
            "proficiencies": [
                {"name": "Divine Health"},
                {"name": "Diplomacy"},
                {"name": "Theology", "rank": 2},
            ]
        },
        {
            "name": "Anchorite",
            "proficiencies": [
                {"name": "Contemplation"},
                {"name": "Endurance"},
                {"name": "Survival"},
                {"name": "Theology"},
            ]
        },
        {
            "name": "Cultist/Heretic",
            "proficiencies": [
                {"name": "Syncretism"},
                {"name": "Knowledge", "specialization": "occult"},
                {"name": "Theology"},
                {"name": "Weapon Proficiency", "weapons": ["dagger", "dart", "staff", "whip"]},
            ]
        },
        {
            "name": "Hospitalist/Medician",
            "proficiencies": [
                {"name": "Laying on Hands"},
                {"name": "Healing", "rank": 2},
                {"name": "Theology"},
            ]
        },
        {
            "name": "Inquisitor",
            "proficiencies": [
                {"name": "Sensing Evil"},
                {"name": "Intimidation"},
                {"name": "Theology"},
                {"name": "Weapon Proficiency", "weapons": ["bludgeons"]},
            ]
        },
        {
            "name": "Oracle",
            "proficiencies": [
                {"name": "Prophecy"},
                {"name": "Performance", "specialization": "storytelling"},
                {"name": "Theology"},
                {"name": "Theology"},
            ]
        },
        {
            "name": "Sacred Courtesan",
            "proficiencies": [
                {"name": "Mystic Aura"},
                {"name": "Performance", "specialization": "dance"},
                {"name": "Seduction"},
                {"name": "Theology"},
            ]
        },
        {
            "name": "Seminarian",
            "proficiencies": [
                {"name": "Divine Blessing"},
                {"name": "Theology", "rank": 2},
                {"name": "Weapon Proficiency", "weapons": ["bludgeons"]},
            ]
        },
        {
            "name": "Village Witch",
            "proficiencies": [
                {"name": "Beast Friendship"},
                {"name": "Animal Husbandry"},
                {"name": "Naturalism"},
                # SPECJALNY WARUNEK: 85% Alchemy / 15% Poisoning
                {"name": "Alchemy", "chance": 0.85, "alternative": "Poisoning"},
            ]
        },
    ],

    "Minor Magicians": [
        {
            "name": "Apprentice Mage",
            "proficiencies": [
                {"name": "Arcane Dabbling"},
                {"name": "Collegiate Wizardry"},
                {"name": "Knowledge", "specialization": "history", "rank": 2},
            ]
        },
        {
            "name": "Apprentice Warlock",
            "proficiencies": [
                {"name": "Black Lore of Zahar"},
                {"name": "Knowledge", "specialization": "occultism", "rank": 3},
            ]
        },
        {
            "name": "Astrologer",
            "proficiencies": [
                {"name": "Soothsaying"},
                {"name": "Knowledge", "specialization": "astrology", "rank": 3},
            ]
        },
        {
            "name": "Augur",
            "proficiencies": [
                {"name": "Soothsaying"},
                {"name": "Animal Husbandry"},
                {"name": "Performance", "specialization": "chanting", "rank": 2},
            ]
        },
        {
            "name": "Charlatan",
            "proficiencies": [
                {"name": "Mystic Aura"},
                {"name": "Alchemy"},
                {"name": "Bargaining"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Failed Apprentice",
            "proficiencies": [
                {"name": "Arcane Dabbling"},
                {"name": "Collegiate Wizardry"},
                {"name": "Knowledge", "specialization": "history"},
                {"name": "Revelry"},
            ]
        },
        {
            "name": "Hedge Magician",
            "proficiencies": [
                {"name": "Mastery of Enchantment & Illusions"},
                {"name": "Healing"},
                {"name": "Naturalism"},
                {"name": "Folkways"},
            ]
        },
        {
            "name": "Occultist",
            "proficiencies": [
                {"name": "Mastery of Conjuration & Summoning"},
                {"name": "Knowledge", "specialization": "occultism", "rank": 3},
            ]
        },
        {
            "name": "Prestidigitator",
            "proficiencies": [
                {"name": "Prestidigitation"},
                {"name": "Performance", "specialization": "juggling", "rank": 2},
                {"name": "Folkways"},
            ]
        },
    ],

    "Military": [
        {
            "name": "Light Infantry",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "light"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "weapon & shield"},
                {"name": "Manual of Arms"},
                {"name": "Weapon Proficiency", "weapons": ["dagger", "javelin", "short sword", "spear"]},
            ]
        },
        {
            "name": "Heavy Infantry",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "heavy"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "weapon & shield"},
                {"name": "Manual of Arms"},
                {"name": "Weapon Proficiency", "weapons": ["swords/daggers", "spears/polearms"]},
            ]
        },
        {
            "name": "Slingers",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "light"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "missile"},
                {"name": "Manual of Arms"},
                {"name": "Weapon Proficiency", "weapons": ["dagger", "short sword", "sling", "sling-staff"]},
            ]
        },
        {
            "name": "Bowmen",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "light"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "missile"},
                {"name": "Manual of Arms"},
                {"name": "Weapon Proficiency", "weapons": ["dagger", "short sword", "short bow", "staff"]},
            ]
        },
        {
            "name": "Crossbowmen",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "medium"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "missile"},
                {"name": "Manual of Arms"},
                {"name": "Weapon Proficiency", "weapons": ["arbalest", "crossbow", "dagger", "short sword"]},
            ]
        },
        {
            "name": "Composite Bowmen",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "medium"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "missile"},
                {"name": "Manual of Arms"},
                {"name": "Weapon Proficiency", "weapons": ["composite bow", "dagger", "short bow", "short sword"]},
            ]
        },
        {
            "name": "Longbowmen",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "medium"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "missile"},
                {"name": "Manual of Arms"},
                {"name": "Weapon Proficiency", "weapons": ["dagger", "long bow", "short bow", "short sword"]},
            ]
        },
        {
            "name": "Light Cavalry",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "light"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "weapon & shield"},
                {"name": "Manual of Arms"},
                {"name": "Riding"},
                {"name": "Weapon Proficiency", "weapons": ["swords/daggers", "spears/polearms"]},
            ]
        },
        {
            "name": "Mounted Crossbowmen",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "medium"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "weapon & shield"},
                {"name": "Manual of Arms"},
                {"name": "Riding"},
                {"name": "Weapon Proficiency", "weapons": ["bows/crossbows", "swords/daggers"]},
            ]
        },
        {
            "name": "Horse Archers",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "light"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "missile weapon"},
                {"name": "Manual of Arms"},
                {"name": "Riding"},
                {"name": "Weapon Proficiency", "weapons": ["bows/crossbows", "swords/daggers"]},
            ]
        },
        {
            "name": "Medium Cavalry",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "heavy"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "weapon & shield"},
                {"name": "Manual of Arms"},
                {"name": "Riding"},
                {"name": "Weapon Proficiency", "weapons": ["spears/polearms", "swords/daggers"]},
            ]
        },
        {
            "name": "Heavy Cavalry",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "heavy"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "weapon & shield"},
                {"name": "Manual of Arms"},
                {"name": "Riding"},
                {"name": "Weapon Proficiency", "weapons": ["spears/polearms", "swords/daggers"]},
            ]
        },
        {
            "name": "Cataphract Cavalry",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "heavy"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "missile weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "weapon & shield"},
                {"name": "Manual of Arms"},
                {"name": "Riding"},
                {"name": "Weapon Proficiency", "weapons": ["bows/crossbows", "spears/polearms", "swords/daggers"]},
            ]
        },
        {
            "name": "Camel Archers",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "light"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "missile weapon"},
                {"name": "Manual of Arms"},
                {"name": "Riding"},
                {"name": "Weapon Proficiency", "weapons": ["bows/crossbows", "swords/daggers"]},
            ]
        },
        {
            "name": "Camel Lancers",
            "proficiencies": [
                {"name": "Armor Proficiency", "specialization": "medium"},
                {"name": "Fighting Style Proficiency", "specialization": "single weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "missile weapon"},
                {"name": "Fighting Style Proficiency", "specialization": "weapon & shield"},
                {"name": "Manual of Arms"},
                {"name": "Riding"},
                {"name": "Weapon Proficiency", "weapons": ["bows/crossbows", "spears/polearms", "swords/daggers"]},
            ]
        },
    ],

    "Specialists": [
        # --- Alchemists ---
        {
            "name": "Alchemist (Apprentice)",
            "proficiencies": [
                {"name": "Alchemy", "rank": 1},
                {"name": "Collegiate Wizardry"},
                {"name": "Labor", "specialization": "scullery"},
                {"name": "Naturalism"},
            ]
        },
        {
            "name": "Alchemist (Assistant)",
            "proficiencies": [
                {"name": "Alchemy", "rank": 2},
                {"name": "Collegiate Wizardry"},
                {"name": "Labor", "specialization": "scullery"},
                {"name": "Naturalism"},
            ]
        },
        {
            "name": "Alchemist",
            "proficiencies": [
                {"name": "Alchemy", "rank": 3},
                {"name": "Collegiate Wizardry"},
                {"name": "Labor", "specialization": "scullery"},
                {"name": "Naturalism"},
            ]
        },

        # --- Animal Trainers ---
        {
            "name": "Animal Trainer (Domestic)",
            "proficiencies": [
                {"name": "Animal Training", "rank": 1},
                {"name": "Animal Husbandry"},
                {"name": "Labor", "specialization": "grooming"},
                {"name": "Riding"},
            ]
        },
        {
            "name": "Animal Trainer (Wild)",
            "proficiencies": [
                {"name": "Animal Training", "rank": 2},
                {"name": "Animal Husbandry"},
                {"name": "Labor", "specialization": "grooming"},
                {"name": "Riding"},
            ]
        },
        {
            "name": "Animal Trainer (Giant)",
            "proficiencies": [
                {"name": "Animal Training", "rank": 3},
                {"name": "Animal Husbandry"},
                {"name": "Labor", "specialization": "grooming"},
                {"name": "Riding"},
            ]
        },
        {
            "name": "Animal Trainer (Fantastic)",
            "proficiencies": [
                {"name": "Animal Training", "rank": 4},
                {"name": "Animal Husbandry"},
                {"name": "Labor", "specialization": "grooming"},
                {"name": "Riding"},
            ]
        },

        # --- Artillerist ---
        {
            "name": "Artillerist",
            "proficiencies": [
                {"name": "Siege Engineering"},
                {"name": "Fighting Style Proficiency", "specialization": "missile weapon"},
                {"name": "Weapon Proficiency", "weapons": ["arbalest", "crossbow", "sling", "sling-staff"]},
            ]
        },

        # --- Engineers ---
        {
            "name": "Engineer (Apprentice)",
            "proficiencies": [
                {"name": "Engineering", "rank": 2},
                {"name": "Craft", "specialization": "masonry"},
                {"name": "Knowledge", "specialization": "mathematics"},
            ]
        },
        {
            "name": "Engineer (Assistant)",
            "proficiencies": [
                {"name": "Engineering", "rank": 3},
                {"name": "Craft", "specialization": "masonry"},
                {"name": "Knowledge", "specialization": "mathematics"},
            ]
        },
        {
            "name": "Engineer",
            "proficiencies": [
                {"name": "Engineering", "rank": 4},
                {"name": "Art", "specialization": "drawing"},
                {"name": "Craft", "specialization": "masonry"},
                {"name": "Knowledge", "specialization": "mathematics"},
            ]
        },

        # --- Healers ---
        {
            "name": "Healer",
            "proficiencies": [
                {"name": "Healing", "rank": 1},
                {"name": "Naturalism"},
                {"name": "Folkways"},
                {"name": "Theology"},
            ]
        },
        {
            "name": "Healer (Physicker)",
            "proficiencies": [
                {"name": "Healing", "rank": 2},
                {"name": "Naturalism"},
                {"name": "Folkways"},
                {"name": "Theology"},
            ]
        },
        {
            "name": "Healer (Chirugeon)",
            "proficiencies": [
                {"name": "Healing", "rank": 3},
                {"name": "Naturalism"},
                {"name": "Folkways"},
                {"name": "Theology"},
            ]
        },

        # --- Marshals (inherited from Military types) ---
        {
            "name": "Marshal (Light Infantry)",
            "inherits": "Light Infantry",
            "extra_proficiencies": [
                {"name": "Manual of Arms", "rank": 2},
            ]
        },
        {
            "name": "Marshal (Bow)",
            "inherits": "Bowmen",
            "extra_proficiencies": [
                {"name": "Manual of Arms", "rank": 2},
                {"name": "Weapon Focus", "specialization": "bows & crossbows"},
            ]
        },
        {
            "name": "Marshal (Heavy Infantry)",
            "inherits": "Heavy Infantry",
            "extra_proficiencies": [
                {"name": "Manual of Arms", "rank": 3},
            ]
        },
        {
            "name": "Marshal (Light Cavalry)",
            "inherits": "Light Cavalry",
            "extra_proficiencies": [
                {"name": "Manual of Arms", "rank": 2},
                {"name": "Mounted Combat"},
            ]
        },
        {
            "name": "Marshal (Heavy Cavalry)",
            "inherits": "Heavy Cavalry",
            "extra_proficiencies": [
                {"name": "Manual of Arms", "rank": 3},
                {"name": "Mounted Combat"},
            ]
        },
        {
            "name": "Marshal (Horse Archer)",
            "inherits": "Horse Archers",
            "extra_proficiencies": [
                {"name": "Manual of Arms", "rank": 2},
                {"name": "Mounted Combat"},
                {"name": "Weapon Focus", "specialization": "bows & crossbows"},
            ]
        },
        {
            "name": "Marshal (Cataphract)",
            "inherits": "Cataphract Cavalry",
            "extra_proficiencies": [
                {"name": "Manual of Arms", "rank": 3},
                {"name": "Mounted Combat"},
                {"name": "Weapon Focus", "specialization": "bows & crossbows"},
            ]
        },

        # --- Navigator ---
        {
            "name": "Navigator",
            "proficiencies": [
                {"name": "Navigation"},
                {"name": "Seafaring", "rank": 2},
                {"name": "Mapping"},
                {"name": "Weapon Proficiency", "weapons": ["club", "hand axe", "net", "staff"]},
            ]
        },

        # --- Quartermaster ---
        {
            "name": "Quartermaster",
            "inherits": "Light Infantry",
            "extra_proficiencies": [
                {"name": "Profession", "specialization": "quartermaster", "rank": 3},
                {"name": "Driving"},
            ]
        },

        # --- Sages ---
        {
            "name": "Sage (Apprentice)",
            "proficiencies": [
                {"name": "Magical Engineering", "rank": 1},
                {"name": "Knowledge", "specialization": "chosen field", "rank": 1},
                {"name": "Collegiate Wizardry"},
                {"name": "Loremastery"},
            ]
        },
        {
            "name": "Sage (Assistant)",
            "proficiencies": [
                {"name": "Magical Engineering", "rank": 2},
                {"name": "Knowledge", "specialization": "chosen field", "rank": 2},
                {"name": "Collegiate Wizardry"},
                {"name": "Loremastery"},
            ]
        },
        {
            "name": "Sage",
            "proficiencies": [
                {"name": "Magical Engineering", "rank": 3},
                {"name": "Knowledge", "specialization": "chosen field", "rank": 3},
                {"name": "Collegiate Wizardry"},
                {"name": "Loremastery"},
            ]
        },

        # --- Siege Engineer ---
        {
            "name": "Siege Engineer",
            "proficiencies": [
                {"name": "Siege Engineering", "rank": 2},
                {"name": "Fighting Style Proficiency", "specialization": "missile weapon"},
                {"name": "Weapon Proficiency", "weapons": ["arbalest", "crossbow", "sling", "sling-staff"]},
            ]
        },

        # --- Ship Captain ---
        {
            "name": "Ship Captain",
            "proficiencies": [
                {"name": "Seafaring", "rank": 2},
                {"name": "Command"},
                {"name": "Leadership"},
                {"name": "Weapon Proficiency", "weapons": ["club", "hand axe", "net", "staff"]},
            ]
        },
    ]

}

