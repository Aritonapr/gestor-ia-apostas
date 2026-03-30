import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# Tenta carregar a ferramenta de busca para o Live
try:
    from bs4 import BeautifulSoup
except:
    pass

# ==============================================================================
# PROTOCOLO JARVIS v71.0 - REMOÇÃO DE SETA + MENU LATERAL COMPLETO (8 BOTÕES)
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- BLOCO DE ESTILO (ZERO WHITE PRO + REMOÇÃO DE SETA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800;900&display=swap');
    
    /* Fundo Escuro Total */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: white !important;
    }

    /* REMOVER SETA DE VOLTAR/RECOLHER E HEADER PADRÃO */
    header, [data-testid="stHeader"] { display: none !important; }
    button[kind="headerNoPadding"] { display: none !important; }
    [data-testid="collapsedControl"] { display: none !important; }

    [data-testid="stMainBlockContainer"] { padding: 100px 45px 20px 45px !important; }

    /* REMOVER BARRA DE ROLAGEM E AJUSTAR LARGURA SIDEBAR */
    [data-testid="stSidebar"] > div:first-child { overflow: hidden !important; }
    [data-testid="stSidebarNav"] { display: none !important; }
    [data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 1px solid #1e293b !important; width: 320px !important; }

    /* Barra Superior Azul Profissional */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 75px; 
        background-color: #001133 !important; border-bottom: 1px solid rgba(255,255,255,0.08); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px; z-index: 10000; 
    }
    .logo-area { color: #9d54ff !important; font-weight: 900; font-size: 28px; letter-spacing: -1.5px; }
    .btn-entrar-neon { background: linear-gradient(90deg, #6d28d9, #06b6d4); color: white; padding: 10px 30px; border-radius: 6px; font-weight: 900; font-size: 11px; }

    /* Estilo dos 8 Botões Laterais */
    .stButton > button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        text-align: left !important; width: 100% !important; padding: 12px 25px !important; 
        font-size: 11.5px !important; font-weight: 700 !important; text-transform: uppercase !important;
        border-bottom: 1px solid #161b22 !important; border-radius: 0px !important;
    }
    .stButton > button:hover { color: #06b6d4 !important; background-color: #161b22 !important; border-left: 4px solid #6d28d9 !important; }

    /* Cards KPI Neon */
    .kpi-box { background: #11151c; border: 1px solid #1c2533; padding: 30px 15px; border-radius: 12px; text-align: center; margin-bottom: 20px; min-height: 160px; }
    .kpi-label { color: #64748b; font-size: 9px; font-weight: 800; text-transform: uppercase; margin-bottom: 20px; }
    .kpi-hero-text { color: #ffffff; font-size: 22px; font-weight: 900; margin-bottom: 25px; }
    .neon-bar-container { background: #1c2533; height: 4px; width: 80%; margin: 0 auto; border-radius: 10px; overflow: hidden; position: relative;}
    .neon-bar-fill { position: absolute; left: 0; top: 0; height: 100%; background: linear-gradient(90deg, #6d28d9, #06b6d4); }
    </style>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO ---
if 'pg' not in st.session_state: st.session_state.pg = "bilhete"

# HEADER SUPERIOR
st.markdown('<div class="betano-header"><div class="logo-area">GESTOR IA</div><div class="btn-entrar-neon">ENTRAR</div></div>', unsafe_allow_html=True)

# SIDEBAR COM OS 8 BOTÕES RESTAURADOS
with st.sidebar:
    st.markdown('<div style="height:80px;"></div>', unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.pg = "scanner_pre"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.pg = "scanner_live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.pg = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.pg = "calls"
    if st.button("📅 BILHETE OURO"): st.session_state.pg = "bilhete"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.pg = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.pg = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.pg = "escanteios"

# FUNÇÃO AUXILIAR CARDS
def kpi_card(lbl, val, p):
    st.markdown(f'<div class="kpi-box"><div class="kpi-label">{lbl}</div><div class="kpi-hero-text">{val}</div><div class="neon-bar-container"><div class="neon-bar-fill" style="width:{p}%;"></div></div></div>', unsafe_allow_html=True)

# TELA PRINCIPAL (BILHETE OURO COMO PADRÃO)
if st.session_state.pg == "bilhete":
    st.markdown("<h2 style='font-weight:900;'>📅 BILHETE OURO - 2026</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: kpi_card("BANCA ATUAL", "R$ 1.000,00", 100)
    with c2: kpi_card("ASSERTIVIDADE", "92.4%", 92)
    with c3: kpi_card("SUGESTÃO", "OVER 2.5", 75)
    with c4: kpi_card("IA STATUS", "ONLINE", 100)
    
    c5, c6, c7, c8 = st.columns(4)
    with c5: kpi_card("VOL. GLOBAL", "ALTO", 85)
    with c6: kpi_card("STAKE PADRÃO", "1.0%", 10)
    with c7: kpi_card("VALOR ENTRADA", "R$ 10,00", 100)
    with c8: kpi_card("SISTEMA", "JARVIS v71.0", 100)

else:
    st.markdown(f"<h2 style='font-weight:900;'>{st.session_state.pg.upper().replace('_', ' ')}</h2>", unsafe_allow_html=True)
    st.info("Área em desenvolvimento pela IA...")

# RODAPÉ
st.markdown('<div style="position:fixed; bottom:0; left:0; width:100%; background:#0b0e11; height:28px; border-top:1px solid #1e293b; display:flex; justify-content:space-between; align-items:center; padding:0 25px; font-size:9px; color:#475569; z-index:10000;"><div>STATUS: ● JARVIS v71.0 OPERACIONAL</div><div>30/03/2026</div></div>', unsafe_allow_html=True)
