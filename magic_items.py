import random

# -----------------------------------------------------------
# DEFINICJA TRYBÓW GENEROWANIA
# -----------------------------------------------------------

MAGIC_ITEM_MODES = {"Classic", "Heroic", "Gritty"}

def normalize_mode(mode: str) -> str:
    """
    Zwraca poprawny tryb losowania lub rzuca wyjątek.
    Heroic == Gritty pod względem logiki magic items.
    """
    mode = mode.capitalize()
    if mode not in MAGIC_ITEM_MODES:
        raise ValueError(f"Invalid magic item mode: {mode}")
    return mode

# ============================================================
# SUBTABLE DEFINITIONS — COMMON POTIONS 1
# ============================================================

COMMON_POTIONS_1 = [
    (1, 6,  {"name": "Healing Salve", "cues": "smell of camphor and wormwood"}),
    (7, 14, {"name": "Midnight Oil", "cues": "dark oil, opaque with no gloss"}),
    (15, 27, {"name": "Oil of Bane-Rune", "cues": "dark oil, silver sheen and metallic scent"}),
    (28, 33, {"name": "Oil of Ooze", "cues": "gooey grey, acidic"}),
    (34, 36, {"name": "Oil of Relaxing Respite", "cues": "lavender aroma"}),
    (37, 37, {"name": "Oil of Rust", "cues": "dark oil, red-orange flakes within"}),
    (38, 46, {"name": "Oil of Sealing", "cues": "mustard-yellow oil, highly viscous"}),
    (47, 60, {"name": "Oil of Sharpness", "cues": "dark oil, metallic scent"}),
    (61, 71, {"name": "Oil of Slickness", "cues": "pitch black, greasy smell"}),
    (72, 78, {"name": "Oil of Unliving Puppetry", "cues": "dark brown oil, smells of embalming fluids"}),
    (79, 79, {"name": "Potion of Adjust Self", "cues": "slowly changes hue each turn"}),
    (80, 89, {"name": "Potion of Allure", "cues": "soft pink, warm to touch"}),
    (90, 90, {"name": "Potion of Antivenom", "cues": "opaque violet, taste and smell of meat cooking"}),
    (91, 100, {"name": "Potion of Arcane Armor", "cues": "shimmering blue tint, savory"}),
]

def roll_from_common_potions_1():
    roll = random.randint(1, 100)
    for lo, hi, data in COMMON_POTIONS_1:
        if lo <= roll <= hi:
            return {
                "type": "Potion",
                "subtable": "Common Potions 1",
                "name": data["name"],
                "cues": data["cues"],
                "roll": roll
            }
    return None

COMMON_POTIONS_2 = [
    (1, 1,  {"name": "Potion of Bottomless Appetite", "cues": "smells like a hearty meal"}),
    (2, 7,  {"name": "Potion of Captain’s Presence", "cues": "green, sweet"}),
    (8, 16, {"name": "Potion of Comprehension", "cues": "smells like musty books and burned candles"}),
    (17, 38, {"name": "Potion of Cure Light Injury", "cues": "golden, honey-scented"}),
    (39, 40, {"name": "Potion of Cure Moderate Injury", "cues": "pink, gooey"}),
    (41, 44, {"name": "Potion of Deathly Appearance", "cues": "black, smell of licorice"}),
    (45, 56, {"name": "Potion of Delay Disease", "cues": "pale red, taste of stale bread"}),
    (57, 58, {"name": "Potion of Delay Poison", "cues": "green and violet emulsion"}),
    (59, 69, {"name": "Potion of Discern Evil", "cues": "muted yellow, sour smell"}),
    (70, 70, {"name": "Potion of Discern Invisible", "cues": "clear, acrid"}),
    (71, 81, {"name": "Potion of Discern Magic", "cues": "bright purple, smell of mint"}),
    (82, 82, {"name": "Potion of Divine Armor", "cues": "deep red, thick chunky mix"}),
    (83, 83, {"name": "Potion of Dragon Control", "cues": "murky, smell of sweat and burning flesh"}),
    (84, 84, {"name": "Potion of Eagle Eyes", "cues": "clear, fluid lenses"}),
    (85, 87, {"name": "Potion of Energy Protection", "cues": "muted blue, tasteless"}),
    (88, 94, {"name": "Potion of Freezing", "cues": "clear, light blue at center"}),
    (95, 95, {"name": "Potion of Giant Control", "cues": "sediment-filled, potent smell"}),
    (96, 96, {"name": "Potion of Great Hearing", "cues": "translucent blue, sloshes readily"}),
    (97, 97, {"name": "Potion of Guilelessness", "cues": "pale blue"}),
    (98, 100, {"name": "Potion of Hallucination", "cues": "(imitates potion it copies)"}),
]

def roll_from_common_potions_2():
    roll = random.randint(1, 100)
    for lo, hi, data in COMMON_POTIONS_2:
        if lo <= roll <= hi:
            return {
                "type": "Potion",
                "subtable": "Common Potions 2",
                "name": data["name"],
                "cues": data["cues"],
                "roll": roll
            }
    return None

COMMON_POTIONS_3 = [
    (1, 13,  {"name": "Potion of Hallucination", "cues": "(imitates potion copied)"}),
    (14, 19, {"name": "Potion of Halting", "cues": "yellow orange, viscous as molasses"}),
    (20, 20, {"name": "Potion of Heir Loss", "cues": "blue"}),
    (21, 26, {"name": "Potion of Homicidal Homage", "cues": "pale violet"}),
    (27, 36, {"name": "Potion of Leaping", "cues": "orange tint, smell of burning fat"}),
    (37, 39, {"name": "Potion of Lesser Magic Discernment", "cues": "yellow tint, sour"}),
    (40, 40, {"name": "Potion of Levitation", "cues": "deep purple, constantly bubbling"}),
    (41, 41, {"name": "Potion of Lizard Skin", "cues": "green, suspension of lizard scales"}),
    (42, 42, {"name": "Potion of Locate Object", "cues": "amber-gold, impossible-to-place scent"}),
    (43, 43, {"name": "Potion of Necromantic Potence", "cues": "grey tint, smell of myrrh"}),
    (44, 44, {"name": "Potion of Night Terrors", "cues": "(imitates potion copied)"}),
    (45, 48, {"name": "Potion of Ogre Rage", "cues": "bright orange"}),
    (49, 49, {"name": "Potion of Ogre Strength", "cues": "bright orange, pungent smell of chives"}),
    (50, 50, {"name": "Potion of Passion", "cues": "clear, slightly sweet"}),
    (51, 51, {"name": "Potion of Peaceful Imperceptibility", "cues": "clear, overly sweet"}),
    (52, 54, {"name": "Potion of Physical Protection", "cues": "muted red, taste of olive oil"}),
    (55, 62, {"name": "Potion of Quiet Footfalls", "cues": "thick green"}),
    (63, 63, {"name": "Potion of Shimmer", "cues": "yellow tint, glows slightly, tasteless"}),
    (64, 70, {"name": "Potion of Simmering Rage", "cues": "red, frothy"}),
    (71, 71, {"name": "Potion of Snakeform", "cues": "dark green"}),
    (72, 72, {"name": "Potion of Speak With Beasts", "cues": "opaque red, smell of raw meat"}),
    (73, 82, {"name": "Potion of Spider Climbing", "cues": "clear with small fibers floating throughout"}),
    (83, 91, {"name": "Potion of Sprinting", "cues": "gold hue"}),
    (92, 96, {"name": "Potion of Swarm Control", "cues": "grimy, almost bottled sewage"}),
    (97, 97, {"name": "Potion of Swift Sword", "cues": "overpowering mocha scent"}),
    (98, 98, {"name": "Potion of Swimming", "cues": "blue tint, taste of brine"}),
    (99, 99, {"name": "Potion of Troublesome Tormina", "cues": "strong liquor"}),
    (100, 100, {"name": "Potion of Vermin Domination", "cues": "dark green"}),
]

def roll_from_common_potions_3():
    roll = random.randint(1, 100)
    for lo, hi, data in COMMON_POTIONS_3:
        if lo <= roll <= hi:
            return {
                "type": "Potion",
                "subtable": "Common Potions 3",
                "name": data["name"],
                "cues": data["cues"],
                "roll": roll
            }
    return None

UNCOMMON_POTIONS_1 = [
    (1, 1,   {"name": "Bottle of Air", "cues": "white tinted, bubbly"}),
    (2, 2,   {"name": "Bottled Billow", "cues": "salt water with slight foam on top"}),
    (3, 3,   {"name": "Bottled Fountain", "cues": "water in glass vial, wire holding down bulging cork"}),
    (4, 4,   {"name": "Dryad’s Nectar", "cues": "alternates between consistency of sap and spirits"}),
    (5, 5,   {"name": "Elixir of Stolen Life", "cues": "sweet liqueur"}),
    (6, 6,   {"name": "Ivorean War-Paint", "cues": "chunky blue pigment"}),
    (7, 8,   {"name": "Kraken Ink", "cues": "black ink"}),
    (9, 9,   {"name": "Mead of Inspiration", "cues": "mead"}),
    (10, 11, {"name": "Oil of Excavation", "cues": "yellow oil with acidic smell"}),
    (12, 16, {"name": "Oil of Extra-Sharpness", "cues": "dark oil, potent metallic smell"}),
    (17, 18, {"name": "Oil of Invisibility", "cues": "clear oil"}),
    (19, 19, {"name": "Oil of Liquefaction", "cues": "clear odorless oil, viscous"}),
    (20, 21, {"name": "Oil of Scrying", "cues": "highly reflective oil with metallic sheen"}),
    (22, 23, {"name": "Oil of Superior Slickness", "cues": "pitch black oil, smell of ripe olives"}),
    (24, 24, {"name": "Oil of the Saint’s Touch", "cues": "nearly-transparent oil with silver tint"}),
    (25, 28, {"name": "Oil of the Secret Fire", "cues": "appears to be lantern oil"}),
    (29, 30, {"name": "Potion of Aging", "cues": "(imitates potion copied)"}),
    (31, 31, {"name": "Potion of Alacrity", "cues": "white tint, incredibly sweet"}),
    (32, 34, {"name": "Potion of Angelic Aura", "cues": "pale white, smell of frankincense"}),
    (35, 36, {"name": "Potion of Apiculture", "cues": "emulsion of honey in water"}),
    (37, 37, {"name": "Potion of Aquatic Adaptation", "cues": "deep blue, smell of salt and soil"}),
    (38, 40, {"name": "Potion of Blast Ward", "cues": "bright blue, sulfurous scent"}),
    (41, 41, {"name": "Potion of Blindness", "cues": "opaque black"}),
    (42, 42, {"name": "Potion of Brilliant Restoration", "cues": "bright red with emulsion of silver"}),
    (43, 44, {"name": "Potion of Burglary", "cues": "light grey, smells of buttery oil"}),
    (45, 48, {"name": "Potion of Clairaudiency", "cues": "momentary ringing in ears when tasted"}),
    (49, 49, {"name": "Potion of Clairsapiency", "cues": "clear, iridescent"}),
    (50, 53, {"name": "Potion of Clairvoyancy", "cues": "clear, momentary vertigo when tasted"}),
    (54, 54, {"name": "Potion of Commotion", "cues": "bright blue, sloshes loudly"}),
    (55, 55, {"name": "Potion of Counter-Shifting", "cues": "bright red, unexpectedly viscous"}),
    (56, 60, {"name": "Potion of Cure Critical Injury", "cues": "brown, scent of ginger"}),
    (61, 68, {"name": "Potion of Cure Disease", "cues": "vivid red, strong taste of onion"}),
    (69, 77, {"name": "Potion of Cure Major Injury", "cues": "crimson, taste of red wine"}),
    (78, 85, {"name": "Potion of Cure Serious Injury", "cues": "rust-orange, cloyingly sweet"}),
    (86, 89, {"name": "Potion of Death Ward", "cues": "dark grey, musty smell"}),
    (90, 95, {"name": "Potion of Deflect Ordinary Missiles", "cues": "light grey, pickled smell"}),
    (96, 99, {"name": "Potion of Deflect Ordinary Weapons", "cues": "brown tint, taste of blood"}),
    (100, 100, {"name": "Potion of Depetrification", "cues": "grey, earthy smell"}),
]

def roll_from_uncommon_potions_1():
    roll = random.randint(1, 100)
    for lo, hi, data in UNCOMMON_POTIONS_1:
        if lo <= roll <= hi:
            return {
                "type": "Potion",
                "subtable": "Uncommon Potions 1",
                "name": data["name"],
                "cues": data["cues"],
                "roll": roll
            }
    return None

UNCOMMON_POTIONS_2 = [
    (1, 2,   {"name": "Potion of Depetrification", "cues": "grey, earthy smell"}),
    (3, 3,   {"name": "Potion of Desperate Valiance", "cues": "blood red, variable smell depending on user but tastes of blood and ash"}),
    (4, 4,   {"name": "Potion of Dire Skinchanging", "cues": "dark green, incredibly strong musk"}),
    (5, 6,   {"name": "Potion of Disappearing", "cues": "transparent"}),
    (7, 9,   {"name": "Potion of Divine Protection", "cues": "dark grey, hint of nutmeg"}),
    (10, 10, {"name": "Potion of Dream Reading", "cues": "brown tint, sour"}),
    (11, 11, {"name": "Potion of Elemental Aegis", "cues": "chalky, pale blue"}),
    (12, 17, {"name": "Potion of Energy Invulnerability", "cues": "blue green, soapy texture"}),
    (18, 18, {"name": "Potion of Escape", "cues": "emulsion of quicksilver in oil"}),
    (19, 19, {"name": "Potion of Extra Luck", "cues": "light green, thick, tastes of vanilla and mint"}),
    (20, 21, {"name": "Potion of False Residence", "cues": "clear, soapy"}),
    (22, 25, {"name": "Potion of Flight", "cues": "white tint, smell of mountain air"}),
    (26, 28, {"name": "Potion of Freedom", "cues": "woad-blue"}),
    (29, 31, {"name": "Potion of Gaseous Form", "cues": "cloudy white, odorless"}),
    (32, 35, {"name": "Potion of Giant Strength", "cues": "yellow-green tint, smell of leeks"}),
    (36, 38, {"name": "Potion of Growth", "cues": "dark green, smell of spinach"}),
    (39, 42, {"name": "Potion of Guise Self", "cues": "amber, jasmine and vanilla scent"}),
    (43, 47, {"name": "Potion of Inaudibility", "cues": "opaque blue"}),
    (48, 50, {"name": "Potion of Indiscernibility", "cues": "iridescent sheen on top"}),
    (51, 51, {"name": "Potion of Infiltration", "cues": "mottled grey, appears as stone when stationary"}),
    (52, 59, {"name": "Potion of Invisibility", "cues": "clear, smell of sharp cheese"}),
    (60, 64, {"name": "Potion of Invulnerability to Evil", "cues": "opaque ashy hue, taste of bread"}),
    (65, 65, {"name": "Potion of Jumbled Thoughts", "cues": "smells of cinnamon"}),
    (66, 70, {"name": "Potion of Lightless Vision", "cues": "opaque black, odorless"}),
    (71, 71, {"name": "Potion of Litheness", "cues": "yellow, oily, settles into layers"}),
    (72, 76, {"name": "Potion of Locate Treasure", "cues": "glittering flecks, sweet then bitter taste"}),
    (77, 77, {"name": "Potion of Lodeskin", "cues": "dull grey suspension of metal dust in acrid fluid"}),
    (78, 80, {"name": "Potion of Madness", "cues": "tastes like watered down, earthy wine"}),
    (81, 81, {"name": "Potion of Measured Mitigation", "cues": "thick crimson, smell and taste of blood but salty"}),
    (82, 82, {"name": "Potion of Mighty Breath", "cues": "fog thick enough to be liquid"}),
    (83, 83, {"name": "Potion of Monstrous Form", "cues": "clear"}),
    (84, 84, {"name": "Potion of Motion", "cues": "clear, moves too much when swirled"}),
    (85, 87, {"name": "Potion of Necromantic Invulnerability", "cues": "black, smell of rotting flesh"}),
    (88, 94, {"name": "Potion of Neutralize Poison", "cues": "opaque purple, chalky taste"}),
    (95, 95, {"name": "Potion of Occlusion", "cues": "clear, smell of baking bread"}),
    (96, 97, {"name": "Potion of Petrification", "cues": "opaque grey, chalky"}),
    (98, 98, {"name": "Potion of Phantom Wings", "cues": "slight taste of rainwater, crystal owl-carved flask"}),
    (99, 99, {"name": "Potion of Phoenix Wings", "cues": "bright red, suspension of gold flakes"}),
    (100,100,{"name": "Potion of Physical Invulnerability", "cues": "dark red, taste of spiced rum"}),
]

def roll_from_uncommon_potions_2():
    roll = random.randint(1, 100)
    for lo, hi, data in UNCOMMON_POTIONS_2:
        if lo <= roll <= hi:
            return {
                "type": "Potion",
                "subtable": "Uncommon Potions 2",
                "name": data["name"],
                "cues": data["cues"],
                "roll": roll
            }
    return None

UNCOMMON_POTIONS_3 = [
    (1, 5,   {"name": "Potion of Physical Invulnerability", "cues": "dark red, taste of spiced rum"}),
    (6, 10,  {"name": "Potion of Poison", "cues": "slight green tint, subtle sour taste"}),
    (11, 11, {"name": "Potion of Precise Poisoning", "cues": "red, emulsion of silver flakes"}),
    (12, 15, {"name": "Potion of Recuperation", "cues": "bubbly, taste of fermenting apple cider"}),
    (16, 16, {"name": "Potion of Relocation", "cues": "white tint"}),
    (17, 24, {"name": "Potion of Remove Curse", "cues": "bright pink, odorless"}),
    (25, 25, {"name": "Potion of Rootedness", "cues": "thick brown syrup"}),
    (26, 26, {"name": "Potion of Sense-Swapping", "cues": "clear"}),
    (27, 29, {"name": "Potion of Shrinking", "cues": "light blue, smell of overripe fruit"}),
    (30, 32, {"name": "Potion of Skinchange", "cues": "deep green, reeks of musk"}),
    (33, 34, {"name": "Potion of Speak with Plants", "cues": "chunky brown mix, smell of cut grass"}),
    (35, 39, {"name": "Potion of Spellward", "cues": "pink, nutty taste"}),
    (40, 40, {"name": "Potion of Still Mind", "cues": "clear, smells sweet, slight taste of rust"}),
    (41, 43, {"name": "Potion of Supreme Valiance", "cues": "blood-red, variable smell depending on user"}),
    (44, 45, {"name": "Potion of Swarmshape", "cues": "light brown"}),
    (46, 50, {"name": "Potion of Swift Sword, Sustained", "cues": "silver-gold iridescence"}),
    (51, 52, {"name": "Potion of Telekinesis", "cues": "clear, speckled with flakes of silver"}),
    (53, 54, {"name": "Potion of Telepathy", "cues": "murky brown, sour"}),
    (55, 56, {"name": "Potion of Tongues", "cues": "iridescent yellow, slightly sweet"}),
    (57, 58, {"name": "Potion of Tranquility", "cues": "white, viscous, smells of cherry blossoms"}),
    (59, 62, {"name": "Potion of Transform Self", "cues": "clear, numbing chill when tasted"}),
    (63, 66, {"name": "Potion of Trollblood", "cues": "sickly green, pulsing"}),
    (67, 69, {"name": "Potion of True Seeing", "cues": "grey tint, lasting bitter taste"}),
    (70, 70, {"name": "Potion of Undetected Passage", "cues": "clear, some things invisible when viewed through"}),
    (71, 71, {"name": "Potion of Unseen Sights", "cues": "clear, slight soapy taste, foam"}),
    (72, 77, {"name": "Potion of Valiance", "cues": "clear, variable taste depending on user"}),
    (78, 81, {"name": "Potion of Vigor", "cues": "silver tint, euphoric sensation when tasted"}),
    (82, 84, {"name": "Potion of Water Breathing", "cues": "dark blue, extremely salty"}),
    (85, 87, {"name": "Potion of Water Walking", "cues": "light blue tint, odorless"}),
    (88, 89, {"name": "Potion of Weapon Resistance", "cues": "oily, smell of metal and sweat"}),
    (90, 90, {"name": "Potion of Wild Regeneration", "cues": "green, blinking bubbles"}),
    (91, 93, {"name": "Potion of Winged Flight", "cues": "red, taste of beef, bubbles when opened"}),
    (94, 96, {"name": "Potion of X-Ray Vision", "cues": "inverts colors seen through it"}),
    (97, 97, {"name": "Ruinous Remedy", "cues": "pale red"}),
    (98, 98, {"name": "Stone Balm", "cues": "brown-grey ointment"}),
    (99, 99, {"name": "Suspension of Disbelief", "cues": "silver dust in golden fluid, sweet smell"}),
    (100,100,{"name": "Witch’s Ointment", "cues": "grey ointment, smell of spring air"}),
]

def roll_from_uncommon_potions_3():
    roll = random.randint(1, 100)
    for lo, hi, data in UNCOMMON_POTIONS_3:
        if lo <= roll <= hi:
            return {
                "type": "Potion",
                "subtable": "Uncommon Potions 3",
                "name": data["name"],
                "cues": data["cues"],
                "roll": roll
            }
    return None

VERY_RARE_POTIONS = [
    (1, 25, {
        "name": "Oil of Permanency",
        "cues": "dark oil with spots of light"
    }),
    (26, 50, {
        "name": "Potion of Fickle Beauty",
        "cues": "smell of flowers, feels chill"
    }),
    (51, 75, {
        "name": "Potion of True Immunity",
        "cues": "liquid gold, sweet"
    }),
    (76, 100, {
        "name": "Potion of Youth",
        "cues": "smells of flowers and early spring"
    }),
]

def roll_from_very_rare_potions():
    roll = random.randint(1, 100)
    for lo, hi, data in VERY_RARE_POTIONS:
        if lo <= roll <= hi:
            return {
                "type": "Potion",
                "subtable": "Very Rare Potions",
                "name": data["name"],
                "cues": data["cues"],
                "roll": roll
            }
    return None

UNCOMMON_RINGS = [
    (1, 7,  "Bezoar Ring"),
    (8, 16, "Ring of Callousness"),
    (17, 23, "Ring of Cold Repose"),
    (24, 27, "Ring of Degeneration^"),
    (28, 31, "Ring of Enslavement^"),
    (32, 35, "Ring of Feebleness^"),
    (36, 44, "Ring of Fire Walking"),
    (45, 50, "Ring of Flesh"),
    (51, 54, "Ring of Frailty^"),
    (55, 59, "Ring of Hallucination^"),
    (60, 63, "Ring of Horrific Death^"),
    (64, 68, "Ring of Messages"),
    (69, 73, "Ring of Molting"),
    (74, 77, "Ring of Restriction^"),
    (78, 82, "Ring of Sealing, Lesser"),
    (83, 87, "Ring of Sparks"),
    (88, 91, "Ring of the Sewer Spider^"),
    (92, 100, "Ring of Vitality"),
]

def roll_uncommon_ring():
    roll = random.randint(1, 100)
    for lo, hi, name in UNCOMMON_RINGS:
        if lo <= roll <= hi:
            return {
                "type": "Ring",
                "rarity": "Uncommon",
                "name": name,
                "roll": roll
            }
    return None

RARE_RINGS_1 = [
    (1, 12, "Band of Beguilement"),
    (13, 13, "Dragon Seal of the Sorcerer-King"),
    (14, 14, "Legionary's Ring"),
    (15, 16, "Ring Against the Wolf"),
    (17, 18, "Ring of Arcane Adversary"),
    (19, 19, "Ring of Attuned Protection"),
    (20, 21, "Ring of Blessing"),
    (22, 23, "Ring of Elasticity"),
    (24, 30, "Ring of Fickle Flame"),
    (31, 31, "Ring of Fiend Conjuring"),
    (32, 33, "Ring of Fire Protection"),
    (34, 34, "Ring of Forewarning"),
    (35, 38, "Ring of Genie Summoning"),
    (39, 50, "Ring of Imp Conjuring"),
    (51, 60, "Ring of Last Breaths"),
    (61, 62, "Ring of Life Protection"),
    (63, 64, "Ring of Lightless Vision"),
    (65, 76, "Ring of Many Faces"),
    (77, 79, "Ring of Penumbral Perception"),
    (79, 100, "Ring of Protection +1"),
]

def roll_rare_ring_1():
    roll = random.randint(1, 100)
    for lo, hi, name in RARE_RINGS_1:
        if lo <= roll <= hi:
            return {
                "type": "Ring",
                "rarity": "Rare (Table 1)",
                "name": name,
                "roll": roll
            }
    return None

RARE_RINGS_2 = [
    (1, 6, "Ring of Protection +1"),
    (7, 15, "Ring of Protection +2"),
    (16, 27, "Ring of Remission"),
    (28, 29, "Ring of Return"),
    (30, 31, "Ring of Ruination"),
    (32, 41, "Ring of Sealing, Greater"),
    (42, 48, "Ring of Selfless Protection"),
    (49, 50, "Ring of Serpents' Council"),
    (51, 52, "Ring of Seven Grudges"),
    (53, 54, "Ring of the Black Gate"),
    (55, 56, "Ring of the Cornered Beast"),
    (57, 60, "Ring of the Earth*"),
    (61, 72, "Ring of the Golden Serpent"),
    (73, 75, "Ring of the Jackal"),
    (76, 85, "Ring of the Leviathan"),
    (86, 87, "Ring of the Open Sky"),
    (88, 89, "Ring of the Seasons"),
    (90, 93, "Ring of the Sky*"),
    (94, 95, "Ring of the Slavedriver"),
    (96, 97, "Ring of Unseen Focus"),
    (98, 99, "Ring of Vengeful Spirits"),
    (100, 100, "Ring of Wailing"),
]

def roll_rare_ring_2():
    roll = random.randint(1, 100)
    for lo, hi, name in RARE_RINGS_2:
        if lo <= roll <= hi:
            return {
                "type": "Ring",
                "rarity": "Rare (Table 2)",
                "name": name,
                "roll": roll
            }
    return None

VERY_RARE_RINGS = [
    (1, 3, "Ring of Absence"),
    (4, 7, "Ring of Anti-Magic"),
    (8, 8, "Ring of Arcane Abjuration"),
    (9, 12, "Ring of Beast Control"),
    (13, 13, "Ring of Bestial Form"),
    (14, 14, "Ring of Calamity"),
    (15, 15, "Ring of Dark Potence"),
    (16, 16, "Ring of Death"),
    (17, 17, "Ring of Decline^"),
    (18, 18, "Ring of Disillusionment"),
    (19, 20, "Ring of Elemental Mastery"),
    (21, 26, "Ring of Elemental Servants"),
    (27, 28, "Ring of Eternal Atrophy"),
    (29, 29, "Ring of Fast Talk"),
    (30, 30, "Ring of Flame's Favor"),
    (31, 32, "Ring of Forcewalls"),
    (33, 33, "Ring of Generous Invisibility"),
    (34, 34, "Ring of Growth"),
    (35, 37, "Ring of Humanoid Control"),
    (38, 38, "Ring of Immunity to Certain Doom"),
    (39, 39, "Ring of Inscrutability"),
    (40, 46, "Ring of Invisibility"),
    (47, 47, "Ring of Luck"),
    (48, 49, "Ring of Merchant's Fortune"),
    (50, 50, "Ring of Near Sighting"),
    (51, 56, "Ring of Plant Control"),
    (57, 59, "Ring of Protection +2, 5' Radius"),
    (60, 62, "Ring of Protection +3"),
    (63, 64, "Ring of Protection +3, 5' Radius"),
    (65, 65, "Ring of Radiance"),
    (66, 66, "Ring of Razor Ramparts"),
    (67, 67, "Ring of Reflection"),
    (68, 68, "Ring of Replacement"),
    (69, 69, "Ring of Revelation"),
    (70, 70, "Ring of Seven Walls"),
    (71, 71, "Ring of Shadows"),
    (72, 72, "Ring of Shrinking"),
    (73, 74, "Ring of Stable Stance"),
    (75, 76, "Ring of Stable Substance"),
    (77, 79, "Ring of Sun and Shadow"),
    (80, 80, "Ring of Sylvankind"),
    (81, 81, "Ring of Telekinetic Force"),
    (82, 82, "Ring of the Blessed Life"),
    (83, 83, "Ring of the Crypt Keeper"),
    (84, 84, "Ring of the Eye"),
    (85, 86, "Ring of the Master Conjurer"),
    (87, 87, "Ring of the Mountain Goat"),
    (88, 88, "Ring of the Scribe"),
    (89, 90, "Ring of the Tower"),
    (91, 91, "Ring of the Warmage"),
    (92, 92, "Ring of Venery"),
    (93, 93, "Ring of Virtue's Shield"),
    (94, 94, "Ring of Water Walking"),
    (95, 100, "Ring of X-Ray Vision"),
]




def roll_very_rare_ring():
    roll = random.randint(1, 100)
    for lo, hi, name in VERY_RARE_RINGS:
        if lo <= roll <= hi:
            return {
                "type": "Ring",
                "rarity": "Very Rare",
                "name": name,
                "roll": roll
            }
    return None

LEGENDARY_RINGS = [
    (1, 8, "Ring of Arcane Alignment"),
    (9, 18, "Ring of Regeneration"),
    (19, 27, "Ring of Rust"),
    (28, 36, "Ring of the Boundless Prison"),
    (37, 45, "Ring of the Frost Tyrant"),
    (46, 53, "Ring of the Lucky Scoundrel"),
    (54, 62, "Ring of the Plaguelord"),
    (63, 70, "Ring of the Queen’s Heart"),
    (71, 78, "Ring of the Umbral Mastiff"),
    (79, 91, "Ring of Wishes"),
    (92, 100, "Seal of Chaos"),
]

def roll_legendary_ring():
    roll = random.randint(1, 100)
    for lo, hi, name in LEGENDARY_RINGS:
        if lo <= roll <= hi:
            return {
                "type": "Ring",
                "rarity": "Legendary",
                "name": name,
                "roll": roll
            }
    return None

COMMON_SCROLLS = [
    (1, 16, "Creature Warding"),
    (17, 82, "Spell Scroll (1 level)"),
    (83, 92, "Spell Scroll (2 levels)"),
    (93, 100, "Treasure Map (Treasure Type B)"),
]

def roll_common_scroll():
    roll = random.randint(1, 100)
    for lo, hi, result in COMMON_SCROLLS:
        if lo <= roll <= hi:
            return {
                "type": "Scroll",
                "rarity": "Common",
                "result": result,
                "roll": roll
            }
    return None


UNCOMMON_SCROLLS = [
    (1, 8, "Cursed Scroll^"),
    (9, 13, "Magic Warding"),
    (14, 14, "Scroll of Anyspell, Lesser"),
    (15, 15, "Scroll of Mapping"),
    (16, 17, "Scroll of Ward-Runes"),
    (18, 44, "Spell Scroll (3 levels)"),
    (45, 64, "Spell Scroll (4 levels)"),
    (65, 71, "Spell Scroll (5 levels)"),
    (72, 77, "Spell Scroll (6 levels)"),
    (78, 81, "Spell Scroll (7 levels)"),
    (82, 84, "Spell Scroll (8 levels)"),
    (85, 86, "Spell Scroll (9 levels)"),
    (87, 87, "Spell Scroll (10 levels)"),
    (88, 100, "Treasure Map (Treasure Type D)"),
]

def roll_uncommon_scroll():
    roll = random.randint(1, 100)
    for lo, hi, result in UNCOMMON_SCROLLS:
        if lo <= roll <= hi:
            return {
                "type": "Scroll",
                "rarity": "Uncommon",
                "result": result,
                "roll": roll
            }
    return None


RARE_SCROLLS = [
    (1, 1, "Scroll of Pledges"),
    (2, 5, "Spell Scroll (12 levels)"),
    (6, 9, "Spell Scroll (14 levels)"),
    (10, 13, "Spell Scroll (16 levels)"),
    (14, 17, "Spell Scroll (18 levels)"),
    (18, 21, "Spell Scroll (20 levels)"),
    (22, 25, "Spell Scroll (22 levels)"),
    (26, 28, "Spell Scroll (24 levels)"),
    (29, 52, "Treasure Map (Treasure Type H)"),
    (53, 76, "Treasure Map (Treasure Type N)"),
    (77, 100, "Treasure Map (Treasure Type Q)"),
]

def roll_rare_scroll():
    roll = random.randint(1, 100)
    for lo, hi, result in RARE_SCROLLS:
        if lo <= roll <= hi:
            return {
                "type": "Scroll",
                "rarity": "Rare",
                "result": result,
                "roll": roll
            }
    return None

VERY_RARE_SCROLLS = [
    (1, 1, "Scroll of Anyspell, Greater"),
    (2, 44, "Spell Scroll (Ritual, 7th level)"),
    (45, 57, "Spell Scroll (Ritual, 8th level)"),
    (58, 80, "Treasure Map (Treasure Type Q,N)"),
    (81, 94, "Treasure Map (Treasure Type R)"),
    (95, 100, "Treasure Map (Treasure Type R,N)"),
]

def roll_very_rare_scroll():
    roll = random.randint(1, 100)
    for lo, hi, result in VERY_RARE_SCROLLS:
        if lo <= roll <= hi:
            return {
                "type": "Scroll",
                "rarity": "Very Rare",
                "result": result,
                "roll": roll
            }
    return None

LEGENDARY_SCROLLS = [
    (1, 21, "Spell Scroll (Ritual, 9th level)"),
    (22, 48, "Spell Scrolls (1d4 × Ritual 7th level)"),
    (49, 67, "Spell Scrolls (1d4 × Ritual 8th level)"),
    (68, 76, "Spell Scrolls (1d4 × Ritual 9th level)"),
    (77, 91, "Treasure Map (4 × Treasure Type R)"),
    (92, 100, "Treasure Maps (1d6 maps totalling 8 × Treasure Type R)"),
]

def roll_legendary_scroll():
    roll = random.randint(1, 100)
    for lo, hi, result in LEGENDARY_SCROLLS:
        if lo <= roll <= hi:
            return {
                "type": "Scroll",
                "rarity": "Legendary",
                "result": result,
                "roll": roll
            }
    return None





SUBTABLE_ROLLERS = {
    "Common Potions 1": roll_from_common_potions_1,
    "Common Potions 2": roll_from_common_potions_2,
    "Common Potions 3": roll_from_common_potions_3,
    "Uncommon Potions 1": roll_from_uncommon_potions_1,
    "Uncommon Potions 2": roll_from_uncommon_potions_2,
    "Uncommon Potions 3": roll_from_uncommon_potions_3,
    "Very Rare Potions": roll_from_very_rare_potions,
    "Uncommon Rings": roll_uncommon_ring,
    "Rare Rings 1": roll_rare_ring_1,
    "Rare Rings 2": roll_rare_ring_2,
    "Very Rare Rings": roll_very_rare_ring,
    "Legendary Rings": roll_legendary_ring,
    "Common Scrolls": roll_common_scroll,
    "Uncommon Scrolls": roll_uncommon_scroll,
    "Rare Scrolls": roll_rare_scroll,
    "Very Rare Scrolls": roll_very_rare_scroll,
    "Legendary Scrolls": roll_legendary_scroll,
}

# -----------------------------------------------------------
# MAPOWANIE TRYBÓW NA LOGIKĘ
# -----------------------------------------------------------

def get_item_generation_logic(mode: str):
    """
    Classic → używa logiki 'classic_magic_item_rolls'
    Heroic/Gritty → używają tej samej logiki 'heroic_magic_item_rolls'
    """
    mode = normalize_mode(mode)

    if mode == "Classic":
        return classic_magic_item_rolls
    else:
        # Heroic i Gritty = identyczne
        return heroic_magic_item_rolls

def classic_magic_item_rolls(level: int):
    """
    Placeholder — tutaj trafi prawdziwa logika losowania magic items
    dla trybu Classic.
    """
    return {
        "mode": "Classic",
        "level": level,
        "items": ["TODO: classic logic not implemented"]
    }

def heroic_magic_item_rolls(level: int):
    """
    Placeholder — Heroic i Gritty działają tak samo.
    """
    return {
        "mode": "Heroic/Gritty",
        "level": level,
        "items": ["TODO: heroic/gritty logic not implemented"]
    }

# ============================================================
# 1. Rarity → subtables mapping
# ============================================================

RARITY_TABLES = {
    "Common": [
        (1, 15, "Common Potions 1"),
        (16, 30, "Common Potions 2"),
        (31, 45, "Common Potions 3"),
        (46, 90, "Common Scrolls"),
        (91, 100, "Common Miscellaneous Items"),
    ],

    # kolejne rarity dodamy później:
    # "Uncommon": [...],
    # "Rare": [...],
    # "Very Rare": [...],
    # "Legendary": [...],
}


def roll_on_subtable(table):
    """
    Otrzymuje listę krotek (min_roll, max_roll, result)
    Zwraca nazwę sub-tabeli, np. "Common Potions 2"
    """
    roll = random.randint(1, 100)
    for low, high, result in table:
        if low <= roll <= high:
            return result
    # shouldn't happen:
    return None


# ============================================================
# 2. Główna funkcja: losowanie X przedmiotów danej rzadkości
# ============================================================

def roll_items_by_rarity(rarity: str, count: int):
    rarity = rarity.capitalize()

    if rarity not in RARITY_TABLES:
        raise ValueError(f"Unknown rarity: {rarity}")

    subtables = RARITY_TABLES[rarity]

    results = []
    for _ in range(count):
        sub = roll_on_subtable(subtables)
        item = roll_magic_item_from_subtable(sub)
        results.append(item)

    return results

# -----------------------------------------------------------
# GŁÓWNA FUNKCJA API
# -----------------------------------------------------------

def roll_magic_items(mode: str, level: int):
    """
    Publiczny punkt wejścia:
    run_generator() będzie to wywoływać dla postaci na wyższym poziomie.
    """
    logic_fn = get_item_generation_logic(mode)
    return logic_fn(level)

# ============================================================
# Public API dla generatora postaci
# ============================================================

def roll_magic_items_heroic(level: int, rarity_counts: dict):
    """
    rarity_counts: np. {"Common": 3, "Uncommon": 1}
    Zwraca słownik:
    {
        "Common": [ ... ],
        "Uncommon": [ ... ]
    }

    Generator postaci może przekazać ile danego rarity otrzymuje NPC/postać.
    """

    output = {}

    for rarity, count in rarity_counts.items():
        output[rarity] = roll_items_by_rarity(rarity, count)

    return output

def roll_magic_item_from_subtable(name: str):
    if name not in SUBTABLE_ROLLERS:
        return {"subtable": name, "error": "No implementation yet"}
    return SUBTABLE_ROLLERS[name]()