import streamlit as st
from script import run_generator, ALL_CLASSES   # ← IMPORTUJESZ NORMALNIE

st.set_page_config(page_title="ACKS NPC Generator", layout="wide")

st.title("ACKS NPC Generator")

class_list = sorted(ALL_CLASSES)

final_class = st.selectbox("Choose class", ["Random"] + sorted(ALL_CLASSES))
level = st.number_input("Choose level:", min_value=1, max_value=14, value=1)

if st.button("Generate NPC"):
    st.write("🔍 Executing run_generator...")
    result = run_generator(final_class, level)
    st.write("✔ run_generator works")
    st.text_area("Result:", result, height=800)