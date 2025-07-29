import streamlit as st

st.title("Hello, World!")
st.write("Toto je moje první aplikace ve Streamlitu.")


# Seznam barev, které může uživatel vybrat
colors = {
    "Černá": "black",
    "Červená": "red",
    "Zelená": "green",
    "Modrá": "blue",
    "Fialová": "purple",
    "Oranžová": "orange"
}

# Výběr barvy pomocí comboboxu
selected_color_name = st.selectbox("Vyber barvu písma", list(colors.keys()))
selected_color = colors[selected_color_name]

# Vložení CSS pro změnu barvy fontu
st.markdown(
    f"""
    <style>
    .custom-text {{
        color: {selected_color};
        font-size: 24px;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Zobrazení textu s aplikovanou třídou
st.markdown('<div class="custom-text">Hello, World!</div>', unsafe_allow_html=True)
