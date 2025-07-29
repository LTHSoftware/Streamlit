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

# Sidebar
st.sidebar.header("Header Of SideBar")
st.sidebar.title("Navigace")
page = st.sidebar.radio("Vyber stránku", ["Domů", "O aplikaci", "Kontakt"])

# Hlavní obsah podle výběru
st.title(page)
st.write(f"Toto je stránka {page}")

# Vytvoříme dva sloupce v sidebaru s poměrem 1:1 (tedy 50 % každý)
col1, col2 = st.sidebar.columns(2)

# Obrázek/logo v prvním sloupci
col1.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=80)

# Obrázek/logo v druhém sloupci
col2.image("https://upload.wikimedia.org/wikipedia/commons/4/44/Google-flutter-logo.svg", width=80)
