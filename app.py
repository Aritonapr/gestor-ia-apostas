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

# --- 2. CSS REFINADO (GEOMETRIA E SIMETRIA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stSidebarCollapse"] { display: none !important; }
    button[kind="headerNoPadding"] { display: none !important; }
    .block-container { padding-top: 1rem !important; }
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    /* SIDEBAR - LARGURA SEGURA */
    [data-testid="stSidebar"] { 
        background-color: #0b1218; 
        border-right: 1px solid rgba(240, 90, 34, 0.2); 
        width: 300px !important; 
    }
    
    .cat-label { 
        color: #5a6b79; font-size: 8px; font-weight: 800; 
        margin-top: 15px; margin-bottom: 5px; text-transform: uppercase; 
        letter-spacing: 2px; text-align: center; display: block; 
    }

    /* BOTÕES DA SIDEBAR - AJUSTE PARA NOMES LONGOS */
    .stButton > button {
        background-color: rgba(26, 36, 45, 0.4) !important; color: #cbd5e0 !important; 
        border: none !important; border-left: 2px solid transparent !important;
        font-weight: 700 !important; height: 32px !important; text-transform: uppercase; 
        font-size: 7pt !important; /* Tamanho fixo em pontos para maior precisão */
        width: 100% !important; text-align: center !important; 
        padding-left: 2px !important; padding-right: 2px !important;
        white-space: nowrap !important; border-radius: 4px !important;
        overflow: hidden !important;
    }
    .stButton > button[kind="primary"] { background-color: rgba(240, 90, 34, 0.1) !important; color: #f05a22 !important; border-left: 2px solid #f05a22 !important; }

    /* ÁREA DE RESULTADOS - SIMETRIA DE ESPAÇAMENTO */
    .main-results-container {
        margin-top: 30px !important;
    }

    .card-principal { 
        background-color: #1a242d; padding: 20px; border-radius: 12px; 
        border-bottom: 4px solid #f05a22; text-align: center; 
        margin-bottom: 20px !important; /* DISTÂNCIA VERTICAL IGUAL À HORIZONTAL */
    }

    .prob-container { 
        display: flex; justify-content: space-around; align-items: center; 
        background: rgba(0,0,0,0.3); border-radius: 10px; padding: 15px 0; 
    }

    /* MINI CARDS (ESTATÍSTICAS) */
    [data-testid="stHorizontalBlock"] {
        gap: 20px !important; /* DISTÂNCIA HORIZONTAL ENTRE CARDS */
    }

    .mini-card { 
        background-color: #111a21; 
        padding: 15px 10px; 
        border-radius: 10px; 
        border: 1px solid #2d3748; 
        text-align: center;
        height: 110px;
        display: flex; flex-direction: column; justify-content: center;
    }
    .mini-label { 
        color: #ffffff !important; font-size: 10px !important; 
        font-weight: 800 !important; text-transform: uppercase; 
        margin-bottom: 12px !important; letter-spacing: 1px;
    }
    .mini-val { 
        color: #00ffc3 !important; font-weight: 900 !important; 
        font-size: 24px !important; text-shadow: 0 0 15px rgba(0, 255, 195, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGICA DE ESTADO ---
if 'liga_ativa' not in st.session_state: 
    st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A')

# --- 4. BARRA LATERAL ---
with st.sidebar:
    def s_btn(display, full, vid):
        if st.button(display, key=f"s_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid; st.session_state.nome_liga = full; st.rerun()

    st.markdown('<p class="cat-label">BRASILEIRÃO</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: s_btn("SÉRIE A", "BRASILEIRÃO SÉRIE A", "BRA_A"); s_btn("SÉRIE C", "BRASILEIRÃO SÉRIE C", "BRA_C")
    with c2: s_btn("SÉRIE B", "BRASILEIRÃO SÉRIE B", "BRA_B"); s_btn("SÉRIE D", "BRASILEIRÃO SÉRIE D", "BRA_D")

    st.markdown('<p class="cat-label">COPAS NACIONAIS</p>', unsafe_allow_html=True)
    c3, c4 = st.columns(2)
    with c3: s_btn("BRASIL", "COPA DO BRASIL", "CDB")
    with c4: s_btn("NORDESTE", "COPA DO NORDESTE", "CNE")
    s_btn("SUPERCOPA", "SUPERCOPA", "SUPER")

    st.markdown('<p class="cat-label">ESTADUAIS</p>', unsafe_allow_html=True)
    c5, c6 = st.columns(2)
    with c5: s_btn("PAULISTÃO", "CAMPEONATO PAULISTA", "SP"); s_btn("MINEIRO", "CAMPEONATO MINEIRO", "MG")
    with c6: s_btn("CARIOCA", "CAMPEONATO CARIOCA", "RJ"); s_btn("GAÚCHO", "CAMPEONATO GAÚCHO", "RS")

    st.markdown('<p class="cat-label">CONTINENTAIS</p>', unsafe_allow_html=True)
    c7, c8 = st.columns(2)
    with c7: s_btn("LIBERTADORES", "COPA LIBERTADORES", "LIB")
    with c8: s_btn("SUL-AMERICANA", "COPA SUL-AMERICANA", "SUL")

# --- 5. ÁREA PRINCIPAL ---
# HEADER
st.markdown("""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px; padding-left: 5px;">
        <div style="position: relative; width: 38px; height: 38px; display: flex; align-items: center; justify-content: center;">
            <svg style="position: absolute; width: 100%; height: 100%; fill: none; stroke: #f05a22; stroke-width: 3; filter: drop-shadow(0 0 5px #f05a22);" viewBox="0 0 100 100">
                <path d="M50 5 L90 25 L90 75 L50 95 L10 75 L10 25 Z" />
            </svg>
            <div style="width: 12px; height: 12px; background-color: #f05a22; clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%); animation: pulse-core 2s infinite ease-in-out;"></div>
        </div>
        <div style="color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 20px; font-weight: 900; letter-spacing: 2px;">GESTOR IA</div>
    </div>
""", unsafe_allow_html=True)

times = ['Flamengo', 'Palmeiras', 'Bahia', 'Corinthians', 'Vasco', 'Santos', 'Botafogo', 'Inter']
col_a, col_b, col_c = st.columns([3, 3, 2.5])
with col_a: t_casa = st.selectbox("Mandante", sorted(times), label_visibility="collapsed")
with col_b: t_fora = st.selectbox("Visitante", sorted([t for t in times if t != t_casa]), label_visibility="collapsed")
with col_c: executar = st.button("🔥 EXECUTAR ALGORITMO", use_container_width=True, type="primary")

if executar:
    st.markdown(f'<div style="font-size:10px; color:#f05a22; font-family:Orbitron; margin-bottom:12px; border-left:4px solid #f05a22; padding-left:10px;">📡 ANALISANDO: {st.session_state.nome_liga}</div>', unsafe_allow_html=True)
    
    # CARD PRINCIPAL
    st.markdown(f"""
        <div class="card-principal">
            <div style="color: #ffffff; font-family: 'Orbitron', sans-serif; font-size: 24px; font-weight: 800; margin-bottom: 20px;">{t_casa.upper()} VS {t_fora.upper()}</div>
            <div class="prob-container">
                <div><p style="color: #f05a22; font-size: 28px; font-weight: 900; margin:0;">44.2%</p><p style="color:#cbd5e0; font-size:11px; font-weight:700; text-transform:uppercase; margin-top:5px;">Mandante</p></div>
                <div><p style="color: #f05a22; font-size: 28px; font-weight: 900; margin:0;">22.8%</p><p style="color:#cbd5e0; font-size:11px; font-weight:700; text-transform:uppercase; margin-top:5px;">Empate</p></div>
                <div><p style="color: #f05a22; font-size: 28px; font-weight: 900; margin:0;">33.0%</p><p style="color:#cbd5e0; font-size:11px; font-weight:700; text-transform:uppercase; margin-top:5px;">Visitante</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # LINHA DE MINI-CARDS (SIMETRIA APLICADA VIA CSS)
    m = st.columns(6)
    metrics = [
        ("⚽ GOLS +2.5", "62%"), ("🚩 ESCANTEIOS +9.5", "75%"), ("👞 CHUTES +22", "81%"), 
        ("🎯 NO GOL +8", "58%"), ("⚠️ FALTAS +24", "85%"), ("🟨 CARTÕES +4", "72%")
    ]
    
    for i, (label, val) in enumerate(metrics):
        with m[i]:
            st.markdown(f"""
                <div class="mini-card">
                    <span class="mini-label">{label}</span>
                    <p class="mini-val">{val}</p>
                </div>
            """, unsafe_allow_html=True)
else:
    st.markdown("<div style='height:150px;'></div>", unsafe_allow_html=True)
