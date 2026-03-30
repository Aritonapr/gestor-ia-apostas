import streamlit as st
import pandas as pd
import os
import requests
import io
from datetime import datetime

# ==============================================================================
# PROTOCOLO JARVIS v65.0 - CLONE VISUAL COMPLETO (RESTAURAÇÃO TOTAL)
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- ARQUITETURA DE ESTILO CSS (IDÊNTICO À IMAGEM v60.0) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* Configurações Globais */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: #ffffff !important;
    }

    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 90px 45px 20px 45px !important; }

    /* Barra Superior (Fiel à Imagem) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 70px; 
        background-color: #001133 !important; border-bottom: 1px solid rgba(255,255,255,0.08); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 50px; z-index: 10000; 
    }
    .logo-area { color: #9d54ff !important; font-weight: 900; font-size: 26px; letter-spacing: -1.5px; display: flex; align-items: center; }
    .nav-links-container { display: flex; gap: 22px; align-items: center; margin-left: 30px; }
    .nav-link-item { color: #ffffff; font-size: 10.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; cursor: pointer; white-space: nowrap; }
    .header-right { display: flex; align-items: center; gap: 15px; }
    .btn-registrar { border: 1px solid #ffffff; color: white; padding: 7px 18px; border-radius: 20px; font-size: 10px; font-weight: 800; }
    .btn-entrar-neon { background: linear-gradient(90deg, #6d28d9, #06b6d4); color: white; padding: 9px 28px; border-radius: 6px; font-weight: 900; font-size: 11px; }

    /* Menu Lateral (Sidebar) */
    [data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 1px solid #1e293b !important; width: 320px !important; }
    .stButton > button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        text-align: left !important; width: 100% !important; padding: 14px 25px !important; 
        font-size: 13.5px !important; font-weight: 600 !important; text-transform: uppercase !important;
        border-bottom: 1px solid #161b22 !important; border-radius: 0px !important; transition: 0.2s;
    }
    .stButton > button:hover { color: #06b6d4 !important; background-color: #161b22 !important; border-left: 4px solid #6d28d9 !important; }

    /* Grid de Cards (Igual à v60.0) */
    .kpi-box {
        background: #11151c; border: 1px solid #1c2533; padding: 35px 20px;
        border-radius: 12px; text-align: center; margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .kpi-label { color: #64748b; font-size: 10px; font-weight: 800; text-transform: uppercase; margin-bottom: 18px; letter-spacing: 1px; }
    .kpi-hero-text { color: #ffffff; font-size: 24px; font-weight: 900; margin-bottom: 20px; }
    .neon-bar-container { background: #1c2533; height: 5px; width: 85%; margin: 0 auto; border-radius: 10px; overflow: hidden; }
    .neon-bar-fill { height: 100%; border-radius: 10px; background: linear-gradient(90deg, #6d28d9, #06b6d4); }

    /* Footer */
    .status-bar { position: fixed; bottom: 0; left: 0; width: 100%; background: #0b0e11; height: 28px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 25px; font-size: 9.5px; color: #475569; z-index: 10000; }
    </style>
""", unsafe_allow_html=True)

# --- MOTOR DE DADOS ---
def get_daily_data():
    try:
        url = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
        df = pd.read_csv(f"{url}?t={datetime.now().timestamp()}")
        df.columns = [c.upper() for c in df.columns]
        return df
    except: return None

df_data = get_daily_data()

# --- HEADER SUPERIOR (CLONE v60) ---
st.markdown("""
    <div class="betano-header">
        <div style="display: flex; align-items: center;">
            <div class="logo-area">GESTOR IA</div>
            <div class="nav-links-container">
                <div class="nav-link-item">APOSTAS ESPORTIVAS</div>
                <div class="nav-link-item">APOSTAS AO VIVO</div>
                <div class="nav-link-item">APOSTAS ENCONTRADAS</div>
                <div class="nav-link-item">ESTATÍSTICAS AVANÇADAS</div>
                <div class="nav-link-item">MERCADO PROBABILÍSTICO</div>
                <div class="nav-link-item">ASSERTIVIDADE IA</div>
            </div>
        </div>
        <div class="header-right">
            <div class="btn-registrar">REGISTRAR</div>
            <div class="btn-entrar-neon">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:80px;"></div>', unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_atual = "scanner"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_atual = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_atual = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_atual = "calls"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_atual = "bilhete"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_atual = "win"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_atual = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_atual = "corners"

# --- RENDERIZADOR DE CARDS v60 ---
def card_v60(label, value, progress):
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-label">{label}</div>
            <div class="kpi-hero-text">{value}</div>
            <div class="neon-bar-container">
                <div class="neon-bar-fill" style="width: {progress}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO ---
if 'aba_atual' not in st.session_state: st.session_state.aba_atual = "bilhete"

if st.session_state.aba_atual == "bilhete":
    st.markdown("<h2 style='font-size:32px; font-weight:800; color:white; margin-bottom:40px;'><img src='https://cdn-icons-png.flaticon.com/512/2693/2693507.png' width='35'> BILHETE OURO</h2>", unsafe_allow_html=True)
    
    # Grid de 8 Cards idêntico à imagem enviada
    r1_c1, r1_c2, r1_c3, r1_c4 = st.columns(4)
    with r1_c1: card_v60("BANCA ATUAL", "R$ 1.000,00", 100)
    with r1_c2: card_v60("ASSERTIVIDADE", "92.4%", 92)
    with r1_c3: card_v60("SUGESTÃO", "OVER 2.5", 75)
    with r1_c4: card_v60("IA STATUS", "ONLINE", 100)
    
    r2_c1, r2_c2, r2_c3, r2_c4 = st.columns(4)
    with r2_c1: card_v60("VOL. GLOBAL", "ALTO", 85)
    with r2_c2: card_v60("STAKE PADRÃO", "1.0%", 10)
    with r2_c3: card_v60("VALOR ENTRADA", "R$ 10,00", 100)
    with r2_c4: card_v60("SISTEMA", "JARVIS v60.0", 100)

    st.markdown("<br><h3 style='color:white; font-size:20px; font-weight:700;'>📝 ANÁLISE COMPLETA DO DIA</h3>", unsafe_allow_html=True)
    if df_data is not None:
        st.dataframe(df_data, use_container_width=True)

# --- FOOTER ---
st.markdown("""<div class="status-bar"><div>STATUS: ● IA OPERACIONAL | v60.0</div><div>JARVIS TRADING SYSTEMS © 2026</div></div>""", unsafe_allow_html=True)
