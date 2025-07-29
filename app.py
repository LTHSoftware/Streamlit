import streamlit as st

st.title("Hello, World!")
st.write("Toto je moje první aplikace ve Streamlitu.")
st.divider()

# Seznam barev
colors = {
    "Černá": "black",
    "Červená": "red",
    "Zelená": "green",
    "Modrá": "blue",
    "Fialová": "purple",
    "Oranžová": "orange"
}

# Vytvoř dva sloupce
col1, col2 = st.columns([1, 1])

with col1:
    selected_color_name = st.selectbox(" ", list(colors.keys()), label_visibility="collapsed")
    selected_color = colors[selected_color_name]

# Vložíme CSS styl pro vybranou barvu
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

with col2:
    st.markdown('<div class="custom-text">Hello, World!</div>', unsafe_allow_html=True)

st.divider()

# Vložení dvou sloupců hned na začátku sidebaru (jakýsi "header")
col1, col2 = st.sidebar.columns(2)

col1.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" style="width: 80px; max-width: 100%;">
    </div>
    """,
    unsafe_allow_html=True
)

col2.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Google-flutter-logo.svg" style="width: 80px; max-width: 100%;">
    </div>
    """,
    unsafe_allow_html=True
)


# Pak můžeš pokračovat dalším obsahem sidebaru
st.sidebar.title("Navigace")
st.sidebar.radio("Vyber stránku", ["Domů", "O aplikaci", "Kontakt"])
