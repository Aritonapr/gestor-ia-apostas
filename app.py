import streamlit as st
import pandas as pd
import os
import requests
import io
from bs4 import BeautifulSoup
from datetime import datetime

# ==============================================================================
# PROTOCOLO JARVIS v67.0 - SCANNER EM TEMPO REAL (LIVE) + DESIGN v60
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- ESTILO CSS (RESTAURAÇÃO TOTAL E REMOÇÃO DE ROLAGEM) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800;900&display=swap');
    
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

    /* Barra Superior Azul */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 70px; 
        background-color: #001133 !important; border-bottom: 1px solid rgba(255,255,255,0.08); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 50px; z-index: 10000; 
    }
    .logo-area { color: #9d54ff !important; font-weight: 900; font-size: 26px; letter-spacing: -1.5px; }
    .btn-entrar-neon { background: linear-gradient(90deg, #6d28d9, #06b6d4); color: white; padding: 9px 28px; border-radius: 6px; font-weight: 900; font-size: 11px; }

    /* Menu Lateral */
    [data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 1px solid #1e293b !important; width: 320px !important; }
    .stButton > button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        text-align: left !important; width: 100% !important; padding: 14px 25px !important; 
        font-size: 13.5px !important; font-weight: 600 !important; text-transform: uppercase !important;
        border-bottom: 1px solid #161b22 !important; border-radius: 0px !important;
    }
    .stButton > button:hover { color: #06b6d4 !important; background-color: #161b22 !important; border-left: 4px solid #6d28d9 !important; }

    /* Cards KPI */
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

# --- FUNÇÃO DO SCANNER LIVE (BUSCA JOGOS AGORA) ---
def buscar_jogos_ao_vivo():
    jogos = []
    try:
        header = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get("https://www.placardefutebol.com.br/", headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        container_jogos = soup.find_all('div', class_='match-card')
        for item in container_jogos:
            status = item.find('span', class_='status').text.strip() if item.find('span', class_='status') else "Agendado"
            time_casa = item.find('div', class_='team-home').text.strip()
            time_fora = item.find('div', class_='team-away').text.strip()
            placar = item.find('div', class_='match-score').text.strip().replace('\n', ' ') if item.find('div', class_='match-score') else "0 x 0"
            
            jogos.append({"Status": status, "Casa": time_casa, "Placar": placar, "Fora": time_fora})
    except:
        pass
    return pd.DataFrame(jogos) if jogos else None

# --- CARREGAMENTO DE DADOS DIÁRIOS ---
@st.cache_data(ttl=600)
def carregar_diario():
    try:
        url = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
        df = pd.read_csv(f"{url}?t={datetime.now().timestamp()}")
        df.columns = [c.upper() for c in df.columns]
        return df
    except: return None

# --- NAVEGAÇÃO ---
if 'aba' not in st.session_state: st.session_state.aba = "bilhete"

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:80px;"></div>', unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba = "scanner"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba = "live"
    if st.button("📅 BILHETE OURO"): st.session_state.aba = "bilhete"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba = "gestao"

# --- HEADER ---
st.markdown("""<div class="betano-header"><div class="logo-area">GESTOR IA</div><div class="btn-entrar-neon">ENTRAR</div></div>""", unsafe_allow_html=True)

# --- FUNÇÃO DE CARDS ---
def desenhar_card(label, valor, porcentagem):
    st.markdown(f"""<div class="kpi-box"><div class="kpi-label">{label}</div><div class="kpi-hero-text">{valor}</div>
    <div class="neon-bar-container"><div class="neon-bar-fill" style="width: {porcentagem}%;"></div></div></div>""", unsafe_allow_html=True)

# --- TELAS ---
if st.session_state.aba == "bilhete":
    st.markdown("<h2 style='font-size:32px; font-weight:800;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: desenhar_card("BANCA", "R$ 1.000,00", 100)
    with c2: desenhar_card("ASSERTIVIDADE", "92.4%", 92)
    with c3: desenhar_card("SUGESTÃO", "OVER 2.5", 75)
    with c4: desenhar_card("IA STATUS", "ONLINE", 100)
    
    df = carregar_diario()
    if df is not None: st.dataframe(df, use_container_width=True)

elif st.session_state.aba == "live":
    st.markdown("<h2 style='font-size:32px; font-weight:800;'>📡 AO VIVO AGORA</h2>", unsafe_allow_html=True)
    with st.spinner("Buscando jogos nos estádios..."):
        df_live = buscar_jogos_ao_vivo()
        if df_live is not None:
            st.dataframe(df_live, use_container_width=True)
        else:
            st.info("Nenhum jogo rolando agora. Tente novamente em instantes.")

# --- FOOTER ---
st.markdown("""<div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #0b0e11; height: 28px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 25px; font-size: 9.5px; color: #475569; z-index: 10000;">
    <div>STATUS: ● IA LIVE OPERACIONAL | v67.0</div><div>JARVIS © 2026</div></div>""", unsafe_allow_html=True)
