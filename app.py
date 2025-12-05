import streamlit as st
from script import run_generator, ALL_CLASSES   # ← IMPORTUJESZ NORMALNIE

st.set_page_config(page_title="ACKS NPC Generator", layout="wide")

st.title("ACKS NPC Generator")

class_list = sorted(ALL_CLASSES)

final_class = st.selectbox("Wybierz klasę:", class_list)
level = st.number_input("Wybierz poziom:", min_value=1, max_value=14, value=1)

if st.button("Generuj NPC"):
    st.write("🔍 Wywołuję run_generator...")
    result = run_generator(final_class, level)
    st.write("✔ run_generator działa")
    st.text_area("Wynik:", result, height=800)