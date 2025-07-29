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

st.sidebar.markdown("""
    <style>
    .sidebar-header {
        padding: 10px 0 15px 0;
        border-bottom: 1px solid #ddd;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;  /* <-- tady je klíč k vert. zarovnání */
    }
    .sidebar-header img {
        display: block;
        max-height: 60px;   /* případně uprav podle potřeby */
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="sidebar-header">
    <img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" alt="Logo 1" width="80">
    <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Google-flutter-logo.svg" alt="Logo 2" width="80">
</div>
""", unsafe_allow_html=True)

# Pak můžeš pokračovat dalším obsahem sidebaru
st.sidebar.title("Navigace")
st.sidebar.radio("Vyber stránku", ["Domů", "O aplikaci", "Kontakt"])
