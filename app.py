import streamlit as st
from script import run_generator, ALL_CLASSES   # ← IMPORTUJESZ NORMALNIE
from item_generator import generate_item


st.set_page_config(page_title="ACKS Generators", layout="wide")

# --- SIDEBAR ---
st.sidebar.title("Options")

mode = st.sidebar.selectbox(
    "Generator selector",
    ["NPC Generator", "Treasure Tome Magic Items"]
)

st.title("ACKS Generators")

if mode == "NPC Generator":

    st.header("ACKS NPC Generator")

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

elif mode == "Treasure Tome Magic Items":

    st.header("Treasure Tome Magic Items")

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
