import streamlit as st

# --- Funkce definující obsah jednotlivých "stránek" ---
def page_home():
    st.title("Hello, World!")
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
        st.markdown('<div class="custom-text">Streamlit</div>', unsafe_allow_html=True)


def page_about():
    st.header("ℹ️ O aplikaci")
    st.write("Toto je stránka 'O aplikaci'.")

def page_contact():
    st.header("📬 Kontakt")
    st.write("Kontakt: example@example.com")

# --- Definice stránek jako objekty st.Page ---
pages = [
    st.Page(page_home, title="  Domů"),
    st.Page(page_about, title="  O aplikaci"),
    st.Page(page_contact, title="  Kontakt"),
]

# --- SIDEBAR ---
with st.sidebar:
    st.write("""
<div direction="row" class="stHorizontalBlock st-emotion-cache-rra9ig e1msl4mp2" data-testid="stHorizontalBlock" data-test-scroll-behavior="normal"><div class="stColumn st-emotion-cache-1i94pul e1msl4mp1" data-testid="stColumn"><div direction="column" height="100%" class="stVerticalBlock st-emotion-cache-ko87jo e1msl4mp2" data-testid="stVerticalBlock"><div class="stElementContainer element-container st-emotion-cache-v3w3zg e1msl4mp0" data-testid="stElementContainer" data-stale="false" width="100%" height="auto" overflow="visible"><div data-testid="stFullScreenFrame" class="st-emotion-cache-8atqhb e1q5ojhd0"><div width="94" class="st-emotion-cache-p75nl5 e1y9jy7j2"><div class="stElementToolbar st-emotion-cache-14d5v98 e1y9jy7j0" data-testid="stElementToolbar" target=".e1y9jy7j2"></div><div class="stImage st-emotion-cache-1dvmtd8 evl31sl0" data-testid="stImage"><div data-testid="stImageContainer" class="st-emotion-cache-7czcpc evl31sl1"><img src="https://upload.wikimedia.org/wikipedia/commons/c/cd/P%C4%8CR_seal_CMYK.svg" alt="0" style="width: 80px; max-width: 100%;"></div></div></div></div></div></div></div><div class="stColumn st-emotion-cache-1i94pul e1msl4mp1" data-testid="stColumn"><div direction="column" height="100%" class="stVerticalBlock st-emotion-cache-ko87jo e1msl4mp2" data-testid="stVerticalBlock" style="justify-content: center;"><div class="stElementContainer element-container st-emotion-cache-v3w3zg e1msl4mp0" data-testid="stElementContainer" data-stale="false" width="100%" height="auto" overflow="visible"><div data-testid="stFullScreenFrame" class="st-emotion-cache-8atqhb e1q5ojhd0"><div width="94" class="st-emotion-cache-p75nl5 e1y9jy7j2"><div class="stImage st-emotion-cache-1dvmtd8 evl31sl0" data-testid="stImage"><div data-testid="stImageContainer" class="st-emotion-cache-7czcpc evl31sl1"><img src="https://www.beafuture.com/www/public/images/logo.svg" alt="0" style="width: 80px; max-width: 100%;"></div></div></div></div></div></div></div></div>
         """, unsafe_allow_html=True)

# --- Inicializace navigace ---
nav = st.navigation({
    "Domů": st.Page(page_home, title="  Domů"),
    "-": [],
    "Navigace": pages,
}, position="sidebar", expanded=True)
# --- Spuštění vybrané stránky ---
nav.run()
