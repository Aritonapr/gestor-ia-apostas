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

# --- 2. CSS AVANÇADO (DESIGN OTIMIZADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stSidebarCollapse"] { display: none !important; }
    button[kind="headerNoPadding"] { display: none !important; }
    
    .block-container { padding-top: 1rem !important; }
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    /* --- HEADER PRINCIPAL À ESQUERDA --- */
    .main-logo-container {
        display: flex; align-items: center; justify-content: flex-start;
        gap: 15px; margin-bottom: 15px; padding-left: 5px;
    }
    .ai-icon-small {
        position: relative; width: 42px; height: 42px;
        display: flex; align-items: center; justify-content: center;
    }
    .hexagon-small {
        position: absolute; width: 100%; height: 100%;
        fill: none; stroke: #f05a22; stroke-width: 3;
        filter: drop-shadow(0 0 5px #f05a22);
    }
    .core-small {
        width: 14px; height: 14px; background-color: #f05a22;
        clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
        animation: pulse-core 2s infinite ease-in-out;
    }
    @keyframes pulse-core {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.3); opacity: 1; }
    }
    .main-title-text {
        color: #f05a22; font-family: 'Orbitron', sans-serif;
        font-size: 24px; font-weight: 900; letter-spacing: 2px;
    }

    /* --- SIDEBAR ULTRA-COMPACTA --- */
    [data-testid="stSidebar"] { background-color: #0f171e; border-right: 1px solid #f05a22; width: 280px !important; }
    
    .cat-label { 
        color: #5a6b79; font-size: 9px; font-weight: 800; 
        margin-top: 12px; margin-bottom: 6px; text-transform: uppercase; 
        letter-spacing: 1px; text-align: center; width: 100%; display: block;
        border-bottom: 1px solid #1a242d; padding-bottom: 3px;
    }

    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: 700 !important; height: 32px !important;
        border-radius: 4px !important; text-transform: uppercase; font-size: 8.5px !important;
        width: 100% !important; margin-bottom: 1px !important; transition: 0.2s;
    }
    .stButton > button:hover { border-color: #f05a22 !important; color: #f05a22 !important; }
    .stButton > button[kind="primary"] {
        background-color: rgba(240,90,34,0.1) !important; color: #f05a22 !important; border: 1px solid #f05a22 !important;
    }

    /* --- CARDS DE RESULTADOS --- */
    .card-principal { 
        background-color: #1a242d; padding: 15px; border-radius: 12px; 
        border-bottom: 4px solid #f05a22; margin-bottom: 10px; text-align: center; 
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 22px; font-weight: 800; }
    .prob-container { display: flex; justify-content: space-around; background: rgba(0,0,0,0.3); border-radius: 10px; padding: 10px 0; margin: 10px 0; }
    .val-prob { color: #f05a22; font-size: 26px; font-weight: 900; }
    .mini-card { background-color: #111a21; padding: 10px; border-radius: 8px; border: 1px solid #2d3748; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LÓGICA DE DADOS ---
if 'liga_ativa' not in st.session_state: 
    st.session_state.update(liga_ativa='BRA_A', nome_liga='BRASILEIRÃO SÉRIE A')

@st.cache_data(ttl=3600)
def load_data(liga):
    # Simulando dados para as novas ligas
    times_map = {
        'BRA_A': ['Palmeiras', 'Flamengo', 'Bahia', 'Corinthians', 'Vasco', 'Botafogo'],
        'BRA_B': ['Santos', 'Sport', 'Goiás', 'Coritiba', 'Ceará', 'Amazonas'],
        'SP': ['São Paulo', 'Palmeiras', 'Corinthians', 'Santos', 'Bragantino'],
        'RJ': ['Flamengo', 'Fluminense', 'Vasco', 'Botafogo', 'Nova Iguaçu']
    }
    times = times_map.get(liga, ['Time A', 'Time B', 'Time C', 'Time D', 'Time E'])
    data = [[np.random.choice(times), np.random.choice(times), np.random.randint(0,4), np.random.randint(0,3)] for _ in range(50)]
    return pd.DataFrame(data, columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

# --- 4. BARRA LATERAL (ORGANIZAÇÃO SOLICITADA) ---
with st.sidebar:
    def s_btn(label, vid):
        if st.button(label, key=f"s_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid
            st.session_state.nome_liga = label
            st.rerun()

    # --- BRASILEIRÃO ORDENADO ---
    st.markdown('<p class="cat-label">BRASILEIRÃO</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: s_btn("SÉRIE A", "BRA_A"); s_btn("SÉRIE C", "BRA_C")
    with c2: s_btn("SÉRIE B", "BRA_B"); s_btn("SÉRIE D", "BRA_D")

    # --- COPAS NACIONAIS ---
    st.markdown('<p class="cat-label">COPAS BRASIL</p>', unsafe_allow_html=True)
    c3, c4 = st.columns(2)
    with c3: s_btn("COPA DO BRASIL", "CDB")
    with c4: s_btn("SUPERCOPA BR", "SUPER")

    # --- ESTADUAIS ---
    st.markdown('<p class="cat-label">CAMPEONATOS ESTADUAIS</p>', unsafe_allow_html=True)
    c5, c6 = st.columns(2)
    with c5: s_btn("PAULISTÃO", "SP"); s_btn("MINEIRO", "MG")
    with c6: s_btn("CARIOCA", "RJ"); s_btn("GAÚCHO", "RS")

    # --- REGIONAL ---
    st.markdown('<p class="cat-label">REGIONAL</p>', unsafe_allow_html=True)
    s_btn("COPA DO NORDESTE", "CNE")

    # --- CONTINENTAIS (BR) ---
    st.markdown('<p class="cat-label">CONTINENTAIS (CLUBS BR)</p>', unsafe_allow_html=True)
    c7, c8 = st.columns(2)
    with c7: s_btn("LIBERTADORES", "LIB")
    with c8: s_btn("SUL-AMERICANA", "SUL")

    # --- INTERNACIONAIS ---
    st.markdown('<p class="cat-label">LIGAS EUROPEIAS</p>', unsafe_allow_html=True)
    c9, c10 = st.columns(2)
    with c9: s_btn("PREMIER LEAGUE", "E0"); s_btn("BUNDESLIGA", "D1")
    with c10: s_btn("LA LIGA", "SP1"); s_btn("SERIE A TIM", "I1")

# --- 5. ÁREA PRINCIPAL ---

# HEADER À ESQUERDA
st.markdown("""
    <div class="main-logo-container">
        <div class="ai-icon-small">
            <svg class="hexagon-small" viewBox="0 0 100 100">
                <path d="M50 5 L90 25 L90 75 L50 95 L10 75 L10 25 Z" />
            </svg>
            <div class="core-small"></div>
        </div>
        <div class="main-title-text">GESTOR IA</div>
    </div>
""", unsafe_allow_html=True)

df = load_data(st.session_state.liga_ativa)
times = sorted(df['HomeTeam'].unique())

col_a, col_b, col_c = st.columns([3, 3, 2.5])
with col_a: t_casa = st.selectbox("Mandante", times, label_visibility="collapsed")
with col_b: t_fora = st.selectbox("Visitante", [t for t in times if t != t_casa], label_visibility="collapsed")
with col_c: executar = st.button("🔥 EXECUTAR ALGORITMO", use_container_width=True, type="primary")

if executar:
    st.markdown(f'<div style="background:rgba(26,36,45,0.6); padding:5px 15px; border-radius:5px; margin-bottom:10px; border-left:4px solid #f05a22; font-size:11px;">📡 Análise: <b>{st.session_state.nome_liga}</b></div>', unsafe_allow_html=True)

    st.markdown(f"""
        <div class="card-principal">
            <div class="match-title">{t_casa.upper()} VS {t_fora.upper()}</div>
            <div class="prob-container">
                <div><p class="val-prob">44.2%</p><p style="font-size:9px; color:#8899a6; text-transform:uppercase;">Mandante</p></div>
                <div><p class="val-prob">22.8%</p><p style="font-size:9px; color:#8899a6; text-transform:uppercase;">Empate</p></div>
                <div><p class="val-prob">33.0%</p><p style="font-size:9px; color:#8899a6; text-transform:uppercase;">Visitante</p></div>
            </div>
            <div style="display:flex; justify-content:space-around; font-size:11px; color:#00ffc3; font-weight:700;">
                <span>ODD JUSTA: @2.10</span>
                <span>VALOR ESPERADO: +12.5%</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    m = st.columns(6)
    metrics = [("⚽ GOLS +2.5", "62%"), ("🚩 CANTOS +9.5", "75%"), ("👞 CHUTES +22", "81%"), 
               ("🎯 NO GOL +8", "58%"), ("⚠️ FALTAS +24", "85%"), ("🟨 CARTÕES +4", "72%")]
    
    for i, (label, val) in enumerate(metrics):
        with m[i]:
            st.markdown(f"<div class='mini-card'><p style='color:#8899a6; font-size:8px; margin-bottom:4px;'>{label}</p><p style='color:#00ffc3; font-size:16px; font-weight:900; margin:0;'>{val}</p></div>", unsafe_allow_html=True)
else:
    st.markdown("<div style='height:150px; display:flex; align-items:center; justify-content:center; border:1px dashed #2d3748; border-radius:10px; color:#5a6b79; font-size:14px;'>Aguardando seleção...</div>", unsafe_allow_html=True)
