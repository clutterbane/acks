# physical_features.py

import random

# ---------------------------------------------------------
# TABLES
# ---------------------------------------------------------

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
    "Hands - Tattooed Knuckles",
    "Legs - Peg Leg",
    "Legs - Skinny",
    "Legs - Short",
    "Mouth - Deviated Septum",
    "Mouth - Diastema",
    "Mouth - Lip Piercing",
    "Mouth - Missing Tooth",
    "Mouth - Replacement Tooth",
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
    "ROLL_TWICE",
]


# ---------------------------------------------------------
# CHA → modifier
# ---------------------------------------------------------

def cha_modifier(score):
    if score == 3: return -3
    if 4 <= score <= 5: return -2
    if 6 <= score <= 8: return -1
    if 9 <= score <= 12: return 0
    if 13 <= score <= 15: return +1
    if 16 <= score <= 17: return +2
    if score == 18: return +3


# ---------------------------------------------------------
# MAIN API FUNCTION
# ---------------------------------------------------------

def generate_physical_features(CHA):
    """Generates a list of physical traits based on CHA."""

    # Determine core type & count
    if CHA == 3:
        feature_type = "negative"; num = 3
    elif 4 <= CHA <= 5:
        feature_type = "negative"; num = 2
    elif 6 <= CHA <= 8:
        feature_type = "negative"; num = 1
    elif 9 <= CHA <= 12:
        feature_type = "average"; num = 1
    elif 13 <= CHA <= 15:
        feature_type = "positive"; num = 1
    elif 16 <= CHA <= 17:
        feature_type = "positive"; num = 2
    elif CHA == 18:
        feature_type = "positive"; num = 3

    # Positive with ROLL_TWICE support
    def pick_positive(n):
        chosen = []
        while len(chosen) < n:
            feat = random.choice(positive_features)
            if feat == "ROLL_TWICE":
                chosen.append(random.choice(positive_features[:-1]))
                chosen.append(random.choice(positive_features[:-1]))
            else:
                chosen.append(feat)
        return chosen[:n]

    # Core features
    if feature_type == "negative":
        features = random.sample(negative_features, num)
    elif feature_type == "average":
        features = random.sample(average_features, num)
    else:
        features = pick_positive(num)

    # Modifier = extra average feature
    if cha_mod := cha_modifier(CHA):
        if cha_mod != 0:
            features.append(random.choice(average_features))

    return features