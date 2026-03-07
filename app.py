import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="GESTOR IA APOSTAS", 
    layout="wide", 
    page_icon="⚽",
    initial_sidebar_state="expanded"
)

# --- 2. CSS DE ALTO NÍVEL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stSidebarCollapse"] { display: none !important; }
    button[kind="headerNoPadding"] { display: none !important; }
    .block-container { padding-top: 1rem !important; }
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    [data-testid="stSidebar"] { 
        background-color: #0b1218; 
        border-right: 1px solid rgba(240, 90, 34, 0.2); 
        width: 300px !important; 
    }
    
    .stButton > button {
        background-color: rgba(26, 36, 45, 0.4) !important; color: #cbd5e0 !important; 
        border: none !important; border-left: 2px solid transparent !important;
        font-weight: 700 !important; height: 32px !important; text-transform: uppercase; 
        font-size: 7.2pt !important; width: 100% !important; border-radius: 4px !important;
        margin-bottom: 2px !important;
    }

    .cat-button > div > button {
        background-color: rgba(240, 90, 34, 0.05) !important;
        color: #ffffff !important;
        border-bottom: 1px solid rgba(240, 90, 34, 0.2) !important;
        font-size: 8.2pt !important; height: 38px !important; letter-spacing: 1px;
    }

    .stButton > button[kind="primary"] { 
        background-color: rgba(240, 90, 34, 0.1) !important; 
        color: #f05a22 !important; border-left: 3px solid #f05a22 !important; 
    }

    .card-principal { 
        background-color: #1a242d; padding: 15px 20px; border-radius: 12px; 
        border-bottom: 4px solid #f05a22; text-align: center; 
        margin-top: 25px !important; margin-bottom: 15px !important;
    }

    .mini-card { 
        background-color: #111a21; padding: 10px 5px; border-radius: 8px; 
        border: 1px solid #2d3748; text-align: center; width: 100%; height: 100px;
        display: flex; flex-direction: column; justify-content: center;
    }
    .mini-label { color: #ffffff !important; font-size: 8.5px !important; font-weight: 800 !important; text-transform: uppercase; margin-bottom: 8px !important; }
    .mini-val { color: #00ffc3 !important; font-weight: 900 !important; font-size: 19px !important; text-shadow: 0 0 10px rgba(0, 255, 195, 0.2); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LÓGICA DE ESTADO ---
if 'liga_ativa' not in st.session_state: 
    st.session_state.update(liga_ativa='BRA_A', nome_liga='BRASILEIRÃO SÉRIE A')
if 'menu_aberto' not in st.session_state:
    st.session_state.menu_aberto = 'BRASIL'

# --- 4. BARRA LATERAL ORGANIZADA ---
with st.sidebar:
    def s_btn(display, full, vid):
        if st.button(display, key=f"s_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid; st.session_state.nome_liga = full; st.rerun()

    def cat_btn(label, menu_id):
        st.markdown('<div class="cat-button">', unsafe_allow_html=True)
        if st.button(f" {label}", key=f"cat_{menu_id}"):
            st.session_state.menu_aberto = menu_id if st.session_state.menu_aberto != menu_id else None
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIA: BRASIL ---
    cat_btn("🇧🇷 FUTEBOL BRASILEIRO", "BRASIL")
    if st.session_state.menu_aberto == "BRASIL":
        c1, c2 = st.columns(2)
        with c1: s_btn("SÉRIE A", "BRASILEIRÃO A", "BRA_A"); s_btn("SÉRIE C", "BRASILEIRÃO C", "BRA_C"); s_btn("COPA BRASIL", "COPA DO BRASIL", "CDB")
        with c2: s_btn("SÉRIE B", "BRASILEIRÃO B", "BRA_B"); s_btn("SÉRIE D", "BRASILEIRÃO D", "BRA_D"); s_btn("NORDESTE", "COPA NORDESTE", "CNE")

    # --- CATEGORIA: ELITE EUROPA (LIGAS) ---
    cat_btn("⚽ ELITE EUROPA (LIGAS)", "EURO_LIGAS")
    if st.session_state.menu_aberto == "EURO_LIGAS":
        s_btn("🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE", "PREMIER LEAGUE", "ENG_P")
        s_btn("🇪🇸 LA LIGA", "LA LIGA (ESPANHA)", "ESP_L")
        s_btn("🇮🇹 SERIE A", "SERIE A (ITÁLIA)", "ITA_A")
        s_btn("🇩🇪 BUNDESLIGA", "BUNDESLIGA (ALEMANHA)", "GER_B")
        s_btn("🇫🇷 LIGUE 1", "LIGUE 1 (FRANÇA)", "FRA_L")

    # --- CATEGORIA: COPAS NACIONAIS ---
    cat_btn("🏆 COPAS NACIONAIS (EURO)", "EURO_COPAS")
    if st.session_state.menu_aberto == "EURO_COPAS":
        c1, c2 = st.columns(2)
        with c1: 
            s_btn("FA CUP", "COPA DA INGLATERRA", "ENG_FA")
            s_btn("COPA DO REI", "COPA DO REI (ESP)", "ESP_CR")
        with c2: 
            s_btn("CARABAO CUP", "COPA DA LIGA (ING)", "ENG_CC")
            s_btn("COPA ITÁLIA", "COPA DA ITÁLIA", "ITA_CI")

    # --- CATEGORIA: CONTINENTAIS UEFA ---
    cat_btn("🌍 COMPETIÇÕES UEFA", "UEFA")
    if st.session_state.menu_aberto == "UEFA":
        s_btn("⭐ CHAMPIONS LEAGUE", "UEFA CHAMPIONS LEAGUE", "UCL")
        s_btn("🇪🇺 EUROPA LEAGUE", "UEFA EUROPA LEAGUE", "UEL")
        s_btn("🏟️ CONFERENCE LEAGUE", "UEFA CONFERENCE LEAGUE", "UECL")
        s_btn("🛡️ EUROCOPA", "EUROCOPA 2024/2028", "EURO_C")

    # --- CATEGORIA: AMÉRICA DO SUL ---
    cat_btn("🔥 AMÉRICA DO SUL", "SUL_AM")
    if st.session_state.menu_aberto == "SUL_AM":
        s_btn("🏆 LIBERTADORES", "COPA LIBERTADORES", "LIB")
        s_btn("🛰️ SUL-AMERICANA", "COPA SUL-AMERICANA", "SUL")

# --- 5. ÁREA PRINCIPAL ---
st.markdown("""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
        <div style="position: relative; width: 38px; height: 38px; display: flex; align-items: center; justify-content: center;">
            <svg style="position: absolute; width: 100%; height: 100%; fill: none; stroke: #f05a22; stroke-width: 3;" viewBox="0 0 100 100">
                <path d="M50 5 L90 25 L90 75 L50 95 L10 75 L10 25 Z" />
            </svg>
            <div style="width: 12px; height: 12px; background-color: #f05a22; clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);"></div>
        </div>
        <div style="color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 20px; font-weight: 900; letter-spacing: 2px;">GESTOR IA</div>
    </div>
""", unsafe_allow_html=True)

times = ['Real Madrid', 'Man. City', 'Liverpool', 'Barcelona', 'Bayern', 'Inter Milão', 'PSG', 'Arsenal']
col_a, col_b, col_btn = st.columns([3, 3, 2.5])
with col_a: t_casa = st.selectbox("Mandante", sorted(times), label_visibility="collapsed")
with col_b: t_fora = st.selectbox("Visitante", sorted([t for t in times if t != t_casa]), label_visibility="collapsed")
with col_btn: executar = st.button("🔥 EXECUTAR ALGORITMO", use_container_width=True, type="primary")

if executar:
    st.markdown(f'<div style="font-size:10px; color:#f05a22; font-family:Orbitron; margin-bottom:10px; border-left:4px solid #f05a22; padding-left:10px;">📡 ANALISANDO: {st.session_state.nome_liga}</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="card-principal">
            <div style="color: #ffffff; font-family: 'Orbitron', sans-serif; font-size: 22px; font-weight: 800; margin-bottom: 20px;">{t_casa.upper()} VS {t_fora.upper()}</div>
            <div style="display: flex; justify-content: space-around; background: rgba(0,0,0,0.3); border-radius: 10px; padding: 15px 0;">
                <div><p style="color: #f05a22; font-size: 26px; font-weight: 900; margin:0;">44.2%</p><p style="color:#cbd5e0; font-size:10px; font-weight:700; text-transform:uppercase; margin-top:5px;">Mandante</p></div>
                <div><p style="color: #f05a22; font-size: 26px; font-weight: 900; margin:0;">22.8%</p><p style="color:#cbd5e0; font-size:10px; font-weight:700; text-transform:uppercase; margin-top:5px;">Empate</p></div>
                <div><p style="color: #f05a22; font-size: 26px; font-weight: 900; margin:0;">33.0%</p><p style="color:#cbd5e0; font-size:10px; font-weight:700; text-transform:uppercase; margin-top:5px;">Visitante</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    m1, m2, m3, m4, m5, m6 = st.columns(6)
    metrics = [
        ("⚽ GOLS +2.5", "62%"), ("🚩 ESCANTEIOS +9.5", "75%"), ("👞 CHUTES +22", "81%"), 
        ("🎯 NO GOL +8", "58%"), ("⚠️ FALTAS +24", "85%"), ("🟨 CARTÕES +4", "72%")
    ]
    
    cols = [m1, m2, m3, m4, m5, m6]
    for i, (label, val) in enumerate(metrics):
        with cols[i]:
            st.markdown(f"""
                <div class="mini-card">
                    <span class="mini-label">{label}</span>
                    <p class="mini-val">{val}</p>
                </div>
            """, unsafe_allow_html=True)
else:
    st.markdown("<div style='height:150px;'></div>", unsafe_allow_html=True)
