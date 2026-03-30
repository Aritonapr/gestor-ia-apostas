import streamlit as st
import pandas as pd
import requests
from datetime import datetime
from io import StringIO

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# --- CARREGAMENTO DE DADOS VIVOS ---
def carregar_dados_vivos():
    url_d = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    url_h = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/historico_5_temporadas.csv"
    try:
        ts = datetime.now().timestamp()
        r_d = requests.get(f"{url_d}?v={ts}", timeout=10)
        r_h = requests.get(f"{url_h}?v={ts}", timeout=10)
        d = pd.read_csv(StringIO(r_d.text)) if r_d.status_code == 200 else None
        h = pd.read_csv(StringIO(r_h.text)) if r_h.status_code == 200 else None
        return d, h
    except: return None, None

df_diario, df_hist = carregar_dados_vivos()

# 2. ESTILO CSS (REMOÇÃO DE SCROLLBAR SIDEBAR + ZERO WHITE)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    [data-testid="stSidebar"] > div:first-child { overflow-y: hidden !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; display: flex; align-items: center; justify-content: space-between; padding: 0 40px !important; z-index: 1000000; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600; padding: 0 10px; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 11px !important; text-transform: uppercase !important; font-weight: 600 !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SUPERIOR
with st.sidebar:
    st.markdown("""<div class="betano-header"><div style="display:flex; align-items:center; gap:25px;"><a href="#" class="logo-link">GESTOR IA</a><div style="display:flex;"><div class="nav-item">ESPORTIVAS</div><div class="nav-item">AO VIVO</div><div class="nav-item">ESTATÍSTICAS</div></div></div><div style="display:flex; align-items:center; gap:15px;"><div class="entrar-grad">ENTRAR</div></div></div><div style="height:65px;"></div>""", unsafe_allow_html=True) 
    if st.button("🎯  SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡  SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰  GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜  HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅  BILHETE OURO"): st.session_state.aba_ativa = "home"

def draw_card(title, value, perc):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# 4. LÓGICA DE TELAS
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with c2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with c3: draw_card("IA STATUS", "ONLINE", 100)
    with c4: draw_card("SISTEMA", "JARVIS v63.0", 100)
    if df_diario is not None: st.dataframe(df_diario, use_container_width=True)

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    if df_diario is not None: st.dataframe(df_diario, use_container_width=True, hide_index=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v63.0</div><div>PONTE TEMPORAL ATIVA [2025 -> 2026]</div></div>""", unsafe_allow_html=True)
