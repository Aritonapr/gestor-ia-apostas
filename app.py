import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random
import requests

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v96.1 - INTEGRAL - IA CONSULTA]
# ESTADO: ALTA PERFORMANCE | TEMA: ZERO WHITE PRO | VERSÃO: v96.1
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA (OBRIGATÓRIO)
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA (STATE) ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state:
    st.session_state.banca_total = 1000.00
if 'consulta_ia_input' not in st.session_state:
    st.session_state.consulta_ia_input = ""

# --- MOTOR DE CARREGAMENTO DE DADOS ---
@st.cache_data(ttl=600)
def carregar_dados_v96():
    url_base = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    try:
        ts = datetime.now().timestamp()
        df = pd.read_csv(f"{url_base}?v={ts}")
        return df
    except:
        return pd.DataFrame()

df_diario = carregar_dados_v96()

# ==============================================================================
# 2. CAMADA DE ESTILO CSS (BLINDAGEM ZERO WHITE PRO)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    header, [data-testid="stHeader"] { display: none !important; }
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }

    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
        transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    
    .logo-ia { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-decoration: none !important; border-bottom: 2px solid #9d54ff; }
    .nav-links { display: flex; gap: 20px; margin-left: 30px; }
    .nav-item { color: #ffffff !important; font-size: 10px !important; text-transform: uppercase; font-weight: 700 !important; text-decoration: none !important; }
    
    .registrar-btn { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 6px 14px !important; border-radius: 20px !important; }
    .entrar-btn { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 10px; }

    [data-testid="stSidebar"] { min-width: 300px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 4px solid #6d28d9 !important; }
    
    .card-ia { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 10px; margin-bottom: 15px; }
    .metric-row { display: flex; justify-content: space-between; font-size: 11px; margin: 8px 0; color: #94a3b8; }
    .metric-row b { color: #ffffff; }
    
    .ia-box { background: #1a202c; border: 2px solid #334155; border-radius: 12px; padding: 25px; margin-top: 20px; }
    .suggestion-card { background: rgba(109, 40, 217, 0.1); border: 1px solid #6d28d9; border-radius: 8px; padding: 12px; margin-bottom: 10px; }
    
    .footer-fixed { position: fixed; bottom: 0; left: 0; width: 100%; height: 35px; background: #0b0e11; border-top: 1px solid #1e293b; display: flex; align-items: center; justify-content: space-between; padding: 0 20px; font-size: 10px; color: #475569; z-index: 9999; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER FIXO ---
st.markdown("""
    <div class="betano-header">
        <div style="display: flex; align-items: center;">
            <a href="?go=home" class="logo-ia">GESTOR IA</a>
            <div class="nav-links">
                <a href="?go=home" class="nav-item">APOSTAS ESPORTIVAS</a>
                <a href="#" class="nav-item">APOSTAS AO VIVO</a>
                <a href="?go=assertividade" class="nav-item">ASSERTIVIDADE IA</a>
            </div>
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">
            <div class="registrar-btn">REGISTRAR</div>
            <div class="entrar-btn">ENTRAR</div>
        </div>
    </div>
    <div style="height:20px;"></div>
""", unsafe_allow_html=True)

# 3. SIDEBAR DE NAVEGAÇÃO
with st.sidebar:
    st.markdown("<div style='height:70px;'></div>", unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"):
        st.session_state.aba_ativa = "home"
    if st.button("📡 SCANNER EM TEMPO REAL"):
        st.session_state.aba_ativa = "live"
    if st.button("🤖 IA CONSULTA"):
        st.session_state.aba_ativa = "ia_consulta"
    if st.button("💰 GESTÃO DE BANCA"):
        st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"):
        st.session_state.aba_ativa = "historico"
    if st.button("⚽ APOSTAS POR GOLS"):
        st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"):
        st.session_state.aba_ativa = "escanteios"

# ==============================================================================
# 4. LÓGICA DAS ABAS
# ==============================================================================

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white; margin-bottom:20px;'>📅 BILHETE OURO - TOP 20 ANALISES IA</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    for i in range(8):
        with [c1, c2, c3, c4][i % 4]:
            st.markdown('<div class="card-ia"><div style="color:#9d54ff; font-size:10px; font-weight:900;">IA CONFIANÇA: 98%</div><div style="color:white; font-size:14px; font-weight:800; margin-top:5px;">Confronto Exemplo</div><hr style="border:0.5px solid #1e293b; margin:15px 0;"><div class="metric-row">🏆 VENCEDOR: <b>72%</b></div><div class="metric-row">⚽ GOLS: <b>1.5+</b></div><div class="metric-row">🚩 CANTOS: <b>9.5+</b></div></div>', unsafe_allow_html=True)

elif st.session_state.aba_ativa == "ia_consulta":
    st.markdown("<h2 style='color:white; margin-bottom:5px;'>🤖 IA CONSULTA</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:12px; margin-bottom:30px;'>Consulte histórico real e peça sugestões de tendências ao cérebro Jarvis.</p>", unsafe_allow_html=True)
    
    # Bloco de Sugestões
    s1, s2, s3 = st.columns(3)
    with s1: st.markdown('<div class="suggestion-card"><b style="color:white; font-size:11px;">🔥 TENDÊNCIA GOLS</b><br><span style="color:#94a3b8; font-size:10px;">Bundesliga hoje com 88% padrão Over 2.5.</span></div>', unsafe_allow_html=True)
    with s2: st.markdown('<div class="suggestion-card"><b style="color:white; font-size:11px;">🚩 RADAR CANTOS</b><br><span style="color:#94a3b8; font-size:10px;">Palmeiras mantém média de 7.2 cantos pró.</span></div>', unsafe_allow_html=True)
    with s3: st.markdown('<div class="suggestion-card"><b style="color:white; font-size:11px;">📈 EVOLUÇÃO</b><br><span style="color:#94a3b8; font-size:10px;">Assertividade em escanteios subiu 12%.</span></div>', unsafe_allow_html=True)

    st.markdown('<div class="ia-box">', unsafe_allow_html=True)
    pergunta = st.text_input("DIGITE SUA PERGUNTA OU COLE O TEXTO DO ÁUDIO:", placeholder="Ex: Qual o retrospecto de Palmeiras x Flamengo?")
    
    b1, b2 = st.columns([1, 4])
    with b1: 
        if st.button("🎤 ÁUDIO"): st.toast("Acessando microfone...")
    with b2:
        if st.button("🔍 CONSULTAR"): st.session_state.consulta_ia_input = pergunta
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.consulta_ia_input:
        st.markdown(f"<p style='color:#06b6d4; font-weight:800; margin-top:30px;'>RELATÓRIO JARVIS: {st.session_state.consulta_ia_input.upper()}</p>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: st.markdown('<div class="card-ia"><div style="color:#00ff88; font-size:10px; font-weight:900;">HISTÓRICO</div><div style="color:white; font-size:12px; font-weight:800; margin:10px 0;">FLAMENGO 2 X 0 VASCO</div><div class="metric-row">GOLS: <b>2</b></div><div class="metric-row">CANTOS: <b>12</b></div></div>', unsafe_allow_html=True)
        with r2: st.markdown('<div class="card-ia" style="text-align:center;"><div style="color:#94a3b8; font-size:9px;">VITÓRIA</div><div style="color:white; font-size:22px; font-weight:900; margin:10px 0;">65%</div><div style="background:#1e293b; height:4px; border-radius:10px;"><div style="background:#6d28d9; width:65%; height:100%;"></div></div></div>', unsafe_allow_html=True)
        with r3: st.markdown('<div class="card-ia" style="text-align:center;"><div style="color:#94a3b8; font-size:9px;">MÉDIA GOLS</div><div style="color:white; font-size:22px; font-weight:900; margin:10px 0;">2.4</div><div style="background:#1e293b; height:4px; border-radius:10px;"><div style="background:#06b6d4; width:70%; height:100%;"></div></div></div>', unsafe_allow_html=True)
        with r4: st.markdown('<div class="card-ia" style="text-align:center;"><div style="color:#94a3b8; font-size:9px;">MÉDIA CANTOS</div><div style="color:white; font-size:22px; font-weight:900; margin:10px 0;">10.5</div><div style="background:#1e293b; height:4px; border-radius:10px;"><div style="background:#9d54ff; width:85%; height:100%;"></div></div></div>', unsafe_allow_html=True)

# FOOTER
st.markdown("""
    <div style="height:100px;"></div>
    <div class="footer-fixed">
        <span>STATUS: ● IA OPERACIONAL | v96.1</span>
        <span>GESTOR IA © 2026</span>
    </div>
""", unsafe_allow_html=True)
