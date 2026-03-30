import streamlit as st
import pandas as pd
import requests
from datetime import datetime
try:
    from bs4 import BeautifulSoup
except ImportError:
    st.error("Aguardando instalação das ferramentas. Verifique o arquivo requirements.txt")

# ==============================================================================
# PROTOCOLO JARVIS v68.0 - SCANNER AO VIVO + BILHETE OURO 2026
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- ESTILO VISUAL FIXO (SEM BARRA DE ROLAGEM LATERAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap');
    html, body, [data-testid="stAppViewContainer"] { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; color: white !important; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 90px 45px 20px 45px !important; }
    [data-testid="stSidebar"] > div:first-child { overflow: hidden !important; }
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 70px; background-color: #001133 !important; border-bottom: 1px solid rgba(255,255,255,0.08); display: flex; align-items: center; justify-content: space-between; padding: 0 50px; z-index: 10000; }
    .logo-area { color: #9d54ff !important; font-weight: 900; font-size: 26px; letter-spacing: -1.5px; }
    .btn-entrar-neon { background: linear-gradient(90deg, #6d28d9, #06b6d4); color: white; padding: 9px 28px; border-radius: 6px; font-weight: 900; font-size: 11px; }
    [data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 1px solid #1e293b !important; }
    .stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; text-align: left !important; width: 100% !important; padding: 14px 25px !important; font-size: 13px !important; font-weight: 600; border-bottom: 1px solid #161b22 !important; border-radius: 0px !important; }
    .stButton > button:hover { color: #06b6d4 !important; background-color: #161b22 !important; border-left: 4px solid #6d28d9 !important; }
    .kpi-box { background: #11151c; border: 1px solid #1c2533; padding: 35px 20px; border-radius: 12px; text-align: center; margin-bottom: 20px; }
    .kpi-label { color: #64748b; font-size: 10px; font-weight: 800; text-transform: uppercase; margin-bottom: 18px; }
    .kpi-hero-text { color: #ffffff; font-size: 24px; font-weight: 900; margin-bottom: 20px; }
    .neon-bar { height: 5px; width: 85%; margin: 0 auto; border-radius: 10px; background: #1c2533; position: relative; overflow: hidden; }
    .neon-fill { position: absolute; left: 0; top: 0; height: 100%; background: linear-gradient(90deg, #6d28d9, #06b6d4); }
    </style>
""", unsafe_allow_html=True)

# --- FUNÇÃO DO SCANNER LIVE (BUSCA REAL AGORA) ---
def buscar_live():
    lista = []
    try:
        header = {'User-Agent': 'Mozilla/5.0'}
        res = requests.get("https://www.placardefutebol.com.br/", headers=header, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        for jogo in soup.select('.match-card'):
            try:
                stt = jogo.select_one('.status').text.strip()
                csa = jogo.select_one('.team-home').text.strip()
                fra = jogo.select_one('.team-away').text.strip()
                plc = jogo.select_one('.match-score').text.strip().replace('\n', ' ')
                lista.append({"STATUS": stt, "CASA": csa, "PLACAR": plc, "FORA": fra})
            except: continue
    except: pass
    return pd.DataFrame(lista) if lista else None

# --- NAVEGAÇÃO ---
if 'pg' not in st.session_state: st.session_state.pg = "bilhete"

with st.sidebar:
    st.markdown('<div style="height:80px;"></div>', unsafe_allow_html=True)
    if st.button("📅 BILHETE OURO"): st.session_state.pg = "bilhete"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.pg = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.pg = "gestao"

# --- INTERFACE ---
st.markdown('<div class="betano-header"><div class="logo-area">GESTOR IA</div><div class="btn-entrar-neon">ENTRAR</div></div>', unsafe_allow_html=True)

def draw_kpi(lbl, val, pct):
    st.markdown(f'<div class="kpi-box"><div class="kpi-label">{lbl}</div><div class="kpi-hero-text">{val}</div><div class="neon-bar"><div class="neon-fill" style="width:{pct}%"></div></div></div>', unsafe_allow_html=True)

if st.session_state.pg == "bilhete":
    st.markdown("<h2 style='font-size:32px; font-weight:800;'>📅 BILHETE OURO - 2026</h2>", unsafe_allow_html=True)
    cols = st.columns(4)
    with cols[0]: draw_kpi("BANCA", "R$ 1.000,00", 100)
    with cols[1]: draw_kpi("ASSERTIVIDADE", "92.4%", 92)
    with cols[2]: draw_kpi("SUGESTÃO", "OVER 2.5", 75)
    with cols[3]: draw_kpi("IA STATUS", "ONLINE", 100)
    
    # Carrega dados do GitHub (Pré-Live)
    try:
        url = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
        df_hoje = pd.read_csv(url)
        st.dataframe(df_hoje, use_container_width=True)
    except: st.info("Sincronizando jogos do dia...")

elif st.session_state.pg == "live":
    st.markdown("<h2 style='font-size:32px; font-weight:800;'>📡 AO VIVO AGORA</h2>", unsafe_allow_html=True)
    with st.spinner("Conectando aos estádios..."):
        df_live = buscar_live()
        if df_live is not None:
            st.dataframe(df_live, use_container_width=True)
        else:
            st.info("Buscando partidas em andamento...")

st.markdown('<div style="position:fixed; bottom:0; left:0; width:100%; background:#0b0e11; height:28px; border-top:1px solid #1e293b; display:flex; justify-content:space-between; align-items:center; padding:0 25px; font-size:9.5px; color:#475569; z-index:10000;"><div>STATUS: ● IA OPERACIONAL | v68.0</div><div>JARVIS © 2026</div></div>', unsafe_allow_html=True)
