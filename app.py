import streamlit as st
import pandas as pd
import os
import requests
import io
from datetime import datetime

# ==============================================================================
# PROTOCOLO JARVIS v66.0 - VERSÃO FINAL (SEM ROLAGEM + VISUAL v60)
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- BLOCO DE ESTILO (AQUI ESTÁ A CORREÇÃO DA BARRA LATERAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800;900&display=swap');
    
    /* Fundo Escuro Total */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: white !important;
    }

    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 90px 45px 20px 45px !important; }

    /* REMOVER BARRA DE ROLAGEM DA ESQUERDA */
    [data-testid="stSidebar"] > div:first-child { overflow: hidden !important; }
    [data-testid="stSidebarNav"] { overflow: hidden !important; }
    section[data-testid="stSidebar"] .st-emotion-cache-16q986n { overflow: hidden !important; }

    /* Barra Superior Azul (Fiel à sua foto) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 70px; 
        background-color: #001133 !important; border-bottom: 1px solid rgba(255,255,255,0.08); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 50px; z-index: 10000; 
    }
    .logo-area { color: #9d54ff !important; font-weight: 900; font-size: 26px; letter-spacing: -1.5px; }
    .nav-links-container { display: flex; gap: 22px; align-items: center; margin-left: 30px; }
    .nav-link-item { color: #ffffff; font-size: 10.5px; font-weight: 700; text-transform: uppercase; opacity: 0.9; }
    .btn-registrar { border: 1px solid #ffffff; color: white; padding: 7px 18px; border-radius: 20px; font-size: 10px; font-weight: 800; }
    .btn-entrar-neon { background: linear-gradient(90deg, #6d28d9, #06b6d4); color: white; padding: 9px 28px; border-radius: 6px; font-weight: 900; font-size: 11px; }

    /* Menu Lateral Customizado */
    [data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 1px solid #1e293b !important; width: 320px !important; }
    .stButton > button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        text-align: left !important; width: 100% !important; padding: 14px 25px !important; 
        font-size: 13.5px !important; font-weight: 600 !important; text-transform: uppercase !important;
        border-bottom: 1px solid #161b22 !important; border-radius: 0px !important;
    }
    .stButton > button:hover { color: #06b6d4 !important; background-color: #161b22 !important; border-left: 4px solid #6d28d9 !important; }

    /* Cards KPI (Idênticos à sua foto v60) */
    .kpi-box {
        background: #11151c; border: 1px solid #1c2533; padding: 35px 20px;
        border-radius: 12px; text-align: center; margin-bottom: 20px;
    }
    .kpi-label { color: #64748b; font-size: 10px; font-weight: 800; text-transform: uppercase; margin-bottom: 18px; }
    .kpi-hero-text { color: #ffffff; font-size: 24px; font-weight: 900; margin-bottom: 20px; }
    .neon-bar-container { background: #1c2533; height: 5px; width: 85%; margin: 0 auto; border-radius: 10px; overflow: hidden; position: relative;}
    .neon-bar-fill { position: absolute; left: 0; top: 0; height: 100%; background: linear-gradient(90deg, #6d28d9, #06b6d4); }
    </style>
""", unsafe_allow_html=True)

# --- CARREGAMENTO DE DADOS (MOTOR SEGURO) ---
@st.cache_data(ttl=600)
def carregar_dados_seguros():
    try:
        url = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
        # O 'timestamp' força o sistema a sempre pegar os jogos novos do dia
        df = pd.read_csv(f"{url}?t={datetime.now().timestamp()}")
        df.columns = [c.upper() for c in df.columns]
        return df
    except: return None

df_hoje = carregar_dados_seguros()

# --- HEADER SUPERIOR ---
st.markdown(f"""
    <div class="betano-header">
        <div style="display: flex; align-items: center;">
            <div class="logo-area">GESTOR IA</div>
            <div class="nav-links-container">
                <div class="nav-link-item">APOSTAS ESPORTIVAS</div>
                <div class="nav-link-item">APOSTAS AO VIVO</div>
                <div class="nav-link-item">ESTATÍSTICAS AVANÇADAS</div>
                <div class="nav-link-item">ASSERTIVIDADE IA</div>
            </div>
        </div>
        <div class="header-right">
            <div class="btn-registrar">REGISTRAR</div>
            <div class="btn-entrar-neon">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR (SISTEMA DE NAVEGAÇÃO) ---
if 'pagina' not in st.session_state: st.session_state.pagina = "bilhete"

with st.sidebar:
    st.markdown('<div style="height:80px;"></div>', unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.pagina = "scanner"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.pagina = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.pagina = "gestao"
    if st.button("📅 BILHETE OURO"): st.session_state.pagina = "bilhete"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.pagina = "calls"

# --- FUNÇÃO PARA DESENHAR OS CARDS ---
def desenhar_card(label, valor, porcentagem):
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-label">{label}</div>
            <div class="kpi-hero-text">{valor}</div>
            <div class="neon-bar-container">
                <div class="neon-bar-fill" style="width: {porcentagem}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- TELA: BILHETE OURO (ONDE OS JOGOS REAIS APARECEM) ---
if st.session_state.pagina == "bilhete":
    st.markdown("<h2 style='font-size:32px; font-weight:800; color:white; margin-bottom:40px;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    
    # Primeira Linha de Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1: desenhar_card("BANCA ATUAL", "R$ 1.000,00", 100)
    with c2: desenhar_card("ASSERTIVIDADE", "92.4%", 92)
    with c3: desenhar_card("SUGESTÃO", "OVER 2.5", 75)
    with c4: desenhar_card("IA STATUS", "ONLINE", 100)
    
    # Segunda Linha de Cards
    c5, c6, c7, c8 = st.columns(4)
    with c5: desenhar_card("VOL. GLOBAL", "ALTO", 85)
    with c6: desenhar_card("STAKE PADRÃO", "1.0%", 10)
    with c7: desenhar_card("VALOR ENTRADA", "R$ 10,00", 100)
    with c8: desenhar_card("SISTEMA", "JARVIS v66.0", 100)

    st.markdown("<br><h3 style='color:white; font-size:20px; font-weight:700;'>📋 ANÁLISE COMPLETA DO DIA (JOGOS REAIS)</h3>", unsafe_allow_html=True)
    if df_hoje is not None:
        st.dataframe(df_hoje, use_container_width=True)
    else:
        st.warning("Aguardando os jogos serem carregados pelo GitHub Actions...")

# --- RODAPÉ DE STATUS ---
st.markdown("""<div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #0b0e11; height: 28px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 25px; font-size: 9.5px; color: #475569; z-index: 10000;">
    <div>STATUS: ● IA OPERACIONAL | v66.0</div><div>JARVIS TRADING SYSTEMS © 2026</div></div>""", unsafe_allow_html=True)
