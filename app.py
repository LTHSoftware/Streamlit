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


col1, col2 = st.sidebar.columns(2)
col1.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=80)
col2.image("https://upload.wikimedia.org/wikipedia/commons/4/44/Google-flutter-logo.svg", width=80)

st.write("""
<div direction="row" class="stHorizontalBlock st-emotion-cache-rra9ig e1msl4mp2" data-testid="stHorizontalBlock" data-test-scroll-behavior="normal"><div class="stColumn st-emotion-cache-1i94pul e1msl4mp1" data-testid="stColumn"><div direction="column" height="100%" class="stVerticalBlock st-emotion-cache-ko87jo e1msl4mp2" data-testid="stVerticalBlock"><div class="stElementContainer element-container st-emotion-cache-v3w3zg e1msl4mp0" data-testid="stElementContainer" data-stale="false" width="100%" height="auto" overflow="visible"><div data-testid="stFullScreenFrame" class="st-emotion-cache-8atqhb e1q5ojhd0"><div width="94" class="st-emotion-cache-p75nl5 e1y9jy7j2"><div class="stElementToolbar st-emotion-cache-14d5v98 e1y9jy7j0" data-testid="stElementToolbar" target=".e1y9jy7j2"><div data-testid="stElementToolbarButtonContainer" class="st-emotion-cache-1pv7pew e1y9jy7j1"><div data-testid="stElementToolbarButton"><div data-testid="stTooltipHoverTarget" class="stTooltipHoverTarget" id="bui4__anchor" style="display: flex; flex-direction: row; justify-content: flex-end; width: auto;"><button kind="elementToolbar" data-testid="stBaseButton-elementToolbar" aria-label="Fullscreen" class="st-emotion-cache-d0v1h0 el4r43z20"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="currentColor" xmlns="http://www.w3.org/2000/svg" data-testid="stElementToolbarButtonIcon" class="e10vaf9m1 st-emotion-cache-1u2dcfn ex0cdmw0"><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"></path></svg></button></div></div></div></div><div class="stImage st-emotion-cache-1dvmtd8 evl31sl0" data-testid="stImage"><div data-testid="stImageContainer" class="st-emotion-cache-7czcpc evl31sl1"><img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" alt="0" style="width: 80px; max-width: 100%;"></div></div></div></div></div></div></div><div class="stColumn st-emotion-cache-1i94pul e1msl4mp1" data-testid="stColumn"><div direction="column" height="100%" class="stVerticalBlock st-emotion-cache-ko87jo e1msl4mp2" data-testid="stVerticalBlock"><div class="stElementContainer element-container st-emotion-cache-v3w3zg e1msl4mp0" data-testid="stElementContainer" data-stale="false" width="100%" height="auto" overflow="visible"><div data-testid="stFullScreenFrame" class="st-emotion-cache-8atqhb e1q5ojhd0"><div width="94" class="st-emotion-cache-p75nl5 e1y9jy7j2"><div class="stElementToolbar st-emotion-cache-14d5v98 e1y9jy7j0" data-testid="stElementToolbar" target=".e1y9jy7j2"><div data-testid="stElementToolbarButtonContainer" class="st-emotion-cache-1pv7pew e1y9jy7j1"><div data-testid="stElementToolbarButton"><div data-testid="stTooltipHoverTarget" class="stTooltipHoverTarget" id="bui5__anchor" style="display: flex; flex-direction: row; justify-content: flex-end; width: auto;"><button kind="elementToolbar" data-testid="stBaseButton-elementToolbar" aria-label="Fullscreen" class="st-emotion-cache-d0v1h0 el4r43z20"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="currentColor" xmlns="http://www.w3.org/2000/svg" data-testid="stElementToolbarButtonIcon" class="e10vaf9m1 st-emotion-cache-1u2dcfn ex0cdmw0"><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"></path></svg></button></div></div></div></div><div class="stImage st-emotion-cache-1dvmtd8 evl31sl0" data-testid="stImage"><div data-testid="stImageContainer" class="st-emotion-cache-7czcpc evl31sl1"><img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Google-flutter-logo.svg" alt="0" style="width: 80px; max-width: 100%;"></div></div></div></div></div></div></div></div>
         """, unsafe_allow_html=True)

st.divider()
# Pak můžeš pokračovat dalším obsahem sidebaru
st.sidebar.title("Navigace")
st.sidebar.radio("Vyber stránku", ["Domů", "O aplikaci", "Kontakt"])
