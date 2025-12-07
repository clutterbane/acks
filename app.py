import streamlit as st
from character_generator import run_generator, ALL_CLASSES   # ← IMPORTUJESZ NORMALNIE
from item_generator import generate_item
from zero_level_generator import generate_zero_level_character, OCCUPATIONS
from rival_adventuring_parties import generate_rival_party, format_rival_party


st.set_page_config(page_title="ACKS Generators", layout="wide")

# --- SIDEBAR ---
st.sidebar.title("Options")

mode = st.sidebar.selectbox(
    "Generator selector",
    [
        "Leveled Character Generator",
        "Zero-Level Character Generator",
        "Rival Adventuring Party Generator",
        "Treasure Tome Magic Item Generator"]
)

st.title("ACKS Generators")

if mode == "Leveled Character Generator":

    st.header("Leveled Character Generator")

    class_list = sorted(ALL_CLASSES)

    final_class = st.selectbox("Choose class", ["Random"] + sorted(ALL_CLASSES))
    level = st.number_input("Choose level:", min_value=1, max_value=14, value=1)
    mode = "heroic"   # NPC zawsze używa heroic/gritty table
    style = st.selectbox("Campaign style (for magic items generation):", ["ancient_myth", "classical_epic", "northern_saga", "chivalric_romance", "arabian_adventure", "high_fantasy", "sword_and_sorcery"], index=0)

    if st.button("Generate NPC"):
        st.write("🔍 Executing run_generator...")
        result = run_generator(final_class, level, mode=mode, style=style)
        st.write("✔ run_generator works")
        st.text_area("Result:", result, height=800)

# MAGIC ITEM

elif mode == "Treasure Tome Magic Item Generator":

    st.header("Treasure Tome Magic Item Generator")

    mode_choice = st.selectbox(
        "Campaign type:",
        ["heroic", "classic", "gritty"]
    )

    rarity = None
    if mode_choice in ["heroic", "gritty"]:
        rarity = st.selectbox(
            "Rarity:",
            ["common", "uncommon", "rare", "very_rare", "legendary"]
        )

    # -------------------------
    # CLASSIC → choose item type
    # -------------------------
    if mode_choice == "classic":
        rarity = st.selectbox(
            "Magic item type:",
            [
                "random",
                "potions",
                "rings",
                "scrolls",
                "implements",
                "misc_items",
                "swords",
                "misc_weapons",
                "armor"
            ]
        )

    style = st.selectbox(
        "Campaign style:",
        [
            "ancient_myth",
            "classical_epic",
            "northern_saga",
            "chivalric_romance",
            "arabian_adventure",
            "high_fantasy",
            "sword_and_sorcery"
        ]
    )
    if st.button("Generate magic item"):
        item = generate_item(mode_choice, style, rarity)
        st.subheader("Result:")
        st.json(item)

# ============================================================
# ZERO-LEVEL CHARACTER GENERATOR
# ============================================================

elif mode == "Zero-Level Character Generator":

    st.header("Zero-Level Character Generator")

    # --- Race selection ---
    race_choice = st.selectbox(
        "Choose race:",
        ["Random", "Human", "Dwarf", "Elf"]
    )
    race_override = None if race_choice == "Random" else race_choice

    # --- Generation mode ---
    gen_mode = st.selectbox(
        "Generation mode:",
        [
            "Random Proficiencies",
            "Choose Category",
            "Choose Specific Occupation"
        ]
    )

    chosen_category = None
    chosen_occupation = None

    if gen_mode == "Choose Category":
        chosen_category = st.selectbox("Select category:", list(OCCUPATIONS.keys()))

    elif gen_mode == "Choose Specific Occupation":
        chosen_category = st.selectbox("Select category:", list(OCCUPATIONS.keys()))
        occ_names = [o["name"] for o in OCCUPATIONS[chosen_category]]
        chosen_name = st.selectbox("Select occupation:", occ_names)

        for occ in OCCUPATIONS[chosen_category]:
            if occ["name"] == chosen_name:
                chosen_occupation = occ
                break

    if st.button("Generate Zero-Level Character"):

        if gen_mode == "Random Proficiencies":
            result = generate_zero_level_character(
                mode="random_proficiencies",
                race_override=race_override
            )

        elif gen_mode == "Choose Category":
            result = generate_zero_level_character(
                mode="category",
                chosen_category=chosen_category,
                race_override=race_override
            )

        elif gen_mode == "Choose Specific Occupation":
            result = generate_zero_level_character(
                mode="occupation",
                chosen_occupation=chosen_occupation,
                race_override=race_override
            )

        st.subheader("Result")


        # ---- FORMATTER ----
        def format_zero_level_output(result):
            stats = result["stats"]
            features = result["features"]
            profs = result["proficiencies"]

            text = []
            text.append("--- RACE AND OCCUPATION---")
            text.append(f"Race: {result['race']}")
            text.append(f"Occupation: {result['occupation'] or 'None'}")
            text.append(f"Alignment: {result['alignment']}")

            text.append("\n--- HIT POINTS ---")
            text.append(f"Final HP: {result['hp']}")

            text.append("\n--- ATTRIBUTES ---")
            for key in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
                text.append(f"{key}: {stats[key]}")

            text.append("\n--- PHYSICAL FEATURES ---")
            for feat in features:
                text.append(f" - {feat}")

            text.append("\n--- PROFICIENCIES ---")
            for p in profs:
                text.append(f" - {p}")

            return "\n".join(text)


        st.text_area("Generated Character:", format_zero_level_output(result), height=600)

# RIVAL ADVENTURING PARTIES

elif mode == "Rival Adventuring Party Generator":

    st.header("Rival Adventuring Party Generator")

    location = st.selectbox("Encounter location:", ["dungeon", "wilderness", "settlement"])

    dungeon_level = None
    wilderness_max = None
    settlement_class = None

    if location == "dungeon":
        dungeon_level = st.number_input("Dungeon depth:", min_value=1, max_value=20, value=1)

    elif location == "wilderness":
        wilderness_max = st.number_input("Max dungeon level nearby:", min_value=1, max_value=20, value=1)

    elif location == "settlement":
        settlement_class = st.number_input("Settlement market class (1–6):", min_value=1, max_value=6, value=4)

    if st.button("Generate Rival Party"):
        party = generate_rival_party(
            location,
            dungeon_level=dungeon_level,
            wilderness_max=wilderness_max,
            settlement_class=settlement_class
        )
        st.text_area("Result:", format_rival_party(party), height=900)