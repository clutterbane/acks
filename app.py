import streamlit as st
from character_generator import run_generator, ALL_CLASSES   # ← IMPORTUJESZ NORMALNIE
from treasure.item_generator import generate_item
from zero_level_generator import generate_zero_level_character, OCCUPATIONS
from rival_adventuring_parties import generate_rival_party, format_rival_party
from terrains import TERRAINS, normalize_terrain, terrain_id
from lairs_per_hex import LAIRS_PER_HEX, generate_lairs_for_hex
from treasure.classic_types import generate_classic_treasure

st.set_page_config(page_title="ACKS Generators", layout="wide")

# --- SIDEBAR ---
st.sidebar.title("Options")

mode = st.sidebar.selectbox(
    "Generator selector",
    [
        "Leveled Character Generator",
        "Zero-Level Character Generator",
        "Rival Adventuring Party Generator",
        "Treasure Tome Magic Item Generator",
        "Classic Treasure Generator",
        "Hex Lairs Generator"]
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

# ============================================================
# HEX LAIR GENERATOR
# ============================================================

elif mode == "Hex Lairs Generator":

    st.header("Hex Lairs Generator")

    # Rzeki nie mają własnej gęstości legowisk – używa się bazowego terenu,
    # więc nie pokazujemy ich w tym generatorze.
    RIVER_TERRAINS = {
        "River (Any But Desert or Jungle)",
        "River (Desert and Jungle)",
    }

    terrain_options = [t for t in TERRAINS if t not in RIVER_TERRAINS]

    terrain_choice = st.selectbox("Choose terrain type (non-river):", terrain_options)

    # Normalize to canonical + alias
    canonical_name = normalize_terrain(terrain_choice)
    terrain_alias = terrain_id(canonical_name)

    # Retrieve dice expression for lairs
    lair_entry = LAIRS_PER_HEX[canonical_name]

    st.subheader("Lair Dice Formula")

    if isinstance(lair_entry, str):
        st.write(f"**Dice:** `{lair_entry}`")
    else:
        st.write("This terrain has multiple variants:")
        for variant, dice in lair_entry.items():
            st.write(f" - **{variant}** → `{dice}`")

    if st.button("Generate Lairs", key="generate_lairs_button"):
        data = generate_lairs_for_hex(canonical_name)

        st.subheader("Result")
        st.write(f"🎲 **Number of lairs in this hex:** `{data['num_lairs']}`")

        if data["num_lairs"] > 0:
            st.write("### Lairs, rarity and monsters:")

            for i, lair in enumerate(data["lairs"], start=1):
                st.write(
                    f"**Lair {i}:** {lair['rarity']} "
                    f"(roll {lair['rarity_roll']}) → "
                    f"**{lair['monster']}** "
                    f"(roll {lair['monster_roll']})"
                )
        else:
            st.write("No lairs generated.")

# ============================================================
# CLASSIC TREASURE GENERATOR (Tables A–R)
# ============================================================

elif mode == "Classic Treasure Generator":

    st.header("Classic Treasure Generator (ACKS Treasure Types A–R)")

    treasure_type = st.selectbox(
        "Choose treasure type:",
        ["A", "B", "C", "D", "E", "F", "G",
         "H", "I", "J", "K", "L", "M",
         "N", "O", "P", "Q", "R"]
    )

    style = st.selectbox(
        "Campaign style (for magic items):",
        [
            "ancient_myth",
            "classical_epic",
            "northern_saga",
            "chivalric_romance",
            "arabian_adventure",
            "high_fantasy",
            "sword_and_sorcery"
        ],
        index=0
    )

    special_pct = st.slider(
        "Special treasure conversion chance (%):",
        min_value=0,
        max_value=100,
        value=50,
        step=1
    )

    if st.button("Generate Classic Treasure"):
        treasure = generate_classic_treasure(
            treasure_type,
            campaign_style=style,
            special_chance=special_pct
        )

        st.subheader("Final Treasure")

        # ============================================================
        # PREPROCESSING — zbieramy WSZYSTKIE itemy w jedną listę
        # ============================================================

        final_items = []

        # Gems / Jewelry — bierzemy specjalne, jeśli istnieją
        final_items.extend(treasure.get("special_gems") or treasure.get("gems", []))
        final_items.extend(treasure.get("special_jewelry") or treasure.get("jewelry", []))

        # Specjalne konwersje monet, futer, porcelany, wszystkiego
        final_items.extend(treasure.get("special_coins", []))

        # Magic items dostaną swoją sekcję oddzielnie, ale *nie idą do GP/ST sum*
        magic_items = treasure.get("magic_items", [])

        # Coins surowe – ale wrzucamy je do final_items jako JEDEN item per coin block
        for coin_type, amount in treasure["coins"].items():
            if amount <= 0:
                continue

            # zachowujemy zgodność z ACKS monetami
            if coin_type == "copper":
                gp = amount / 100
            elif coin_type == "silver":
                gp = amount / 10
            elif coin_type == "electrum":
                gp = amount / 5
            elif coin_type == "gold":
                gp = amount
            elif coin_type == "platinum":
                gp = amount * 5
            else:
                gp = 0

            final_items.append({
                "name": f"{coin_type.title()} pieces",
                "value_gp": gp,
                "stone": amount / 1000
            })

        # ============================================================
        # RENDERER — każdy item osobno, brak ×2 agregacji
        # ============================================================

        total_value = 0.0
        total_stone = 0.0

        # liczymy sumy tylko z treasure, NIE magic items
        for it in final_items:
            if isinstance(it, dict):
                total_value += it.get("value_gp", 0) or 0
                total_stone += it.get("stone", 0) or 0
            else:  # string / fallback
                total_value += 0
                total_stone += 0

        # Nagłówek
        st.markdown(
            f"**TOTAL VALUE:** {total_value:.0f} gp\n\n"
            f"**TOTAL WEIGHT:** {total_stone:.1f} st\n\n"
            f"### Treasure"
        )

        # Lista skarbów w formacie granularnym
        for it in final_items:

            # ---------------------------
            # SAFETY NORMALIZATION
            # ---------------------------
            if isinstance(it, str):
                # rare fallback – shouldn't happen, but safe
                name = it
                gp = None
                stn = None
            else:
                name = it.get("name", "Unknown Item")
                gp = it.get("value_gp")
                stn = it.get("stone")

            # ---------------------------
            # RENDER
            # ---------------------------
            if stn is not None:
                st.write(f"- {name}, {gp} gp, {stn:.1f} st")
            elif gp is not None:
                st.write(f"- {name}, {gp} gp")
            else:
                st.write(f"- {name}")

        # ============================================================
        # 4. AUDIT TRAIL (debug / inspection)
        # ============================================================

        audit = treasure.get("audit", [])

        if audit:
            with st.expander("📜 Audit Trail (Show Rolls)"):
                for entry in audit:
                    st.write(f"- {entry}")

        # ============================================================
        # MAGIC ITEMS — osobna sekcja
        # ============================================================

        st.markdown("### Magic Items")
        if magic_items:
            for item in magic_items:
                st.write(f"- {item.get('name', 'Unknown Item')}")
        else:
            st.write("_None_")