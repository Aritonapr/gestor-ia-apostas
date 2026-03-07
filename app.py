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

# --- 2. CSS ULTRA-MODERNO (TEXTO INTEIRO & NO-WRAP) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    /* Limpeza de Interface */
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stSidebarCollapse"] { display: none !important; }
    button[kind="headerNoPadding"] { display: none !important; }
    .block-container { padding-top: 1rem !important; }
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    /* --- HEADER PRINCIPAL À ESQUERDA --- */
    .main-logo-container {
        display: flex; align-items: center; gap: 12px; margin-bottom: 20px; padding-left: 5px;
    }
    .ai-icon-small {
        position: relative; width: 38px; height: 38px;
        display: flex; align-items: center; justify-content: center;
    }
    .hexagon-small {
        position: absolute; width: 100%; height: 100%;
        fill: none; stroke: #f05a22; stroke-width: 3;
        filter: drop-shadow(0 0 5px #f05a22);
    }
    .core-small {
        width: 12px; height: 12px; background-color: #f05a22;
        clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
        animation: pulse-core 2s infinite ease-in-out;
    }
    @keyframes pulse-core {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.3); opacity: 1; }
    }
    .main-title-text {
        color: #f05a22; font-family: 'Orbitron', sans-serif;
        font-size: 20px; font-weight: 900; letter-spacing: 2px;
    }

    /* --- SIDEBAR: ESTILO "PAD" OTIMIZADO --- */
    [data-testid="stSidebar"] { 
        background-color: #0b1218; 
        border-right: 1px solid rgba(240, 90, 34, 0.2); 
        width: 280px !important; /* AUMENTADO PARA CABER OS NOMES */
    }
    
    .cat-label { 
        color: #4a5568; font-size: 8px; font-weight: 800; 
        margin-top: 15px; margin-bottom: 5px; text-transform: uppercase; 
        letter-spacing: 2px; text-align: left; padding-left: 10px;
    }

    /* PAD DOS CAMPEONATOS SEM QUEBRA DE LINHA */
    .stButton > button {
        background-color: rgba(26, 36, 45, 0.4) !important; 
        color: #a0aec0 !important; 
        border: none !important;
        border-left: 2px solid transparent !important;
        font-weight: 600 !important; 
        height: 28px !important;
        border-radius: 0px 4px 4px 0px !important; 
        text-transform: uppercase; 
        font-size: 7px !important; /* TAMANHO AJUSTADO */
        width: 100% !important; 
        margin-bottom: 2px !important; 
        text-align: left !important;
        padding-left: 8px !important;
        transition: 0.3s;
        white-space: nowrap !important; /* IMPEDE QUEBRA DE LINHA */
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }
    
    .stButton > button[kind="primary"] {
        background-color: rgba(240, 90, 34, 0.1) !important; 
        color: #f05a22 !important; 
        border-left: 2px solid #f05a22 !important;
    }

    .stButton > button:hover {
        color: #ffffff !important;
        background-color: rgba(240, 90, 34, 0.05) !important;
    }

    /* CARDS DE RESULTADOS */
    .card-principal { 
        background-color: #1a242d; padding: 15px; border-radius: 12px; 
        border-bottom: 4px solid #f05a22; text-align: center; 
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 22px; font-weight: 800; }
    .prob-container { display: flex; justify-content: space-around; background: rgba(0,0,0,0.3); border-radius: 10px; padding: 12px 0; margin: 15px 0; }
    .val-prob { color: #f05a22; font-size: 26px; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LÓGICA DE ESTADO ---
if 'liga_ativa' not in st.session_state: 
    st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A')

# --- 4. BARRA LATERAL (ORGANIZAÇÃO SOLICITADA) ---
with st.sidebar:
    def s_btn(label, vid):
        if st.button(label, key=f"s_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid
            st.session_state.nome_liga = label
            st.rerun()

    st.markdown('<p class="cat-label">BRASILEIRÃO</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: s_btn("SÉRIE A", "BRA_A"); s_btn("SÉRIE C", "BRA_C")
    with c2: s_btn("SÉRIE B", "BRA_B"); s_btn("SÉRIE D", "BRA_D")

    st.markdown('<p class="cat-label">COPAS NACIONAIS</p>', unsafe_allow_html=True)
    c3, c4 = st.columns(2)
    with c3: s_btn("COPA DO BRASIL", "CDB")
    with c4: s_btn("COPA NORDESTE", "CNE")
    s_btn("SUPERCOPA", "SUPER") # Removido BR para não quebrar

    st.markdown('<p class="cat-label">ESTADUAIS</p>', unsafe_allow_html=True)
    c5, c6 = st.columns(2)
    with c5: s_btn("PAULISTÃO", "SP"); s_btn("MINEIRO", "MG")
    with c6: s_btn("CARIOCA", "RJ"); s_btn("GAÚCHO", "RS")

    st.markdown('<p class="cat-label">CONTINENTAIS</p>', unsafe_allow_html=True)
    c7, c8 = st.columns(2)
    with c7: s_btn("LIBERTADORES", "LIB")
    with c8: s_btn("SUL-AMERICANA", "SUL") # Nome ajustado

    st.markdown('<p class="cat-label">LIGAS EUROPEIAS</p>', unsafe_allow_html=True)
    c9, c10 = st.columns(2)
    with c9: s_btn("PREMIER LEAGUE", "E0"); s_btn("BUNDESLIGA", "D1")
    with c10: s_btn("LA LIGA", "SP1"); s_btn("SERIE A", "I1")

# --- 5. ÁREA PRINCIPAL ---
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

# Seleção
times = ['Palmeiras', 'Flamengo', 'Corinthians', 'Vasco', 'Santos', 'Bahia', 'Botafogo', 'Inter']
col_a, col_b, col_c = st.columns([3, 3, 2.5])
with col_a: t_casa = st.selectbox("Mandante", sorted(times), label_visibility="collapsed")
with col_b: t_fora = st.selectbox("Visitante", sorted([t for t in times if t != t_casa]), label_visibility="collapsed")
with col_c: executar = st.button("🔥 EXECUTAR ALGORITMO", use_container_width=True, type="primary")

if executar:
    st.markdown(f'<div style="font-size:10px; color:#f05a22; font-family:Orbitron; margin-bottom:10px;">📡 ANALISANDO: {st.session_state.nome_liga}</div>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="card-principal">
            <div class="match-title">{t_casa.upper()} VS {t_fora.upper()}</div>
            <div class="prob-container">
                <div><p class="val-prob">44.2%</p><p style="font-size:9px; color:#8899a6; text-transform:uppercase;">Mandante</p></div>
                <div><p class="val-prob">22.8%</p><p style="font-size:9px; color:#8899a6; text-transform:uppercase;">Empate</p></div>
                <div><p class="val-prob">33.0%</p><p style="font-size:9px; color:#8899a6; text-transform:uppercase;">Visitante</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    m = st.columns(6)
    metrics = [("⚽ GOLS +2.5", "62%"), ("🚩 CANTOS +9.5", "75%"), ("👞 CHUTES +22", "81%"), 
               ("🎯 NO GOL +8", "58%"), ("⚠️ FALTAS +24", "85%"), ("🟨 CARTÕES +4", "72%")]
    for i, (l, v) in enumerate(metrics):
        with m[i]:
            st.markdown(f"<div style='background:#111a21; padding:8px; border-radius:6px; border:1px solid #2d3748; text-align:center;'><p style='color:#8899a6; font-size:8px; margin-bottom:2px;'>{l}</p><p style='color:#00ffc3; font-size:14px; font-weight:900; margin:0;'>{v}</p></div>", unsafe_allow_html=True)
else:
    st.markdown("<div style='height:150px;'></div>", unsafe_allow_html=True)
