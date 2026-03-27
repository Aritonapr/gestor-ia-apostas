import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE RESTAURAÇÃO TOTAL v58.3 - 100% INTEGRAL]
# DIRETRIZ: MANTER TODAS AS FUNÇÕES E APLICAR FILTRO GEOGRÁFICO
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# --- FUNÇÃO DE CARREGAMENTO DE DADOS ---
def carregar_jogos_diarios():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            return df
        except:
            return None
    return None

df_diario = carregar_jogos_diarios()

# 2. CAMADA DE ESTILO CSS (SISTEMA ZERO WHITE)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important;
    }

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
    }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER E SIDEBAR (RESTAURADOS)
with st.sidebar:
    st.markdown("""<div class="betano-header"><div class="logo-link">GESTOR IA</div><div style="background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 8px 22px; border-radius: 5px; font-weight: 800; font-size: 9.5px;">SISTEMA v58.3</div></div><div style="height:65px;"></div>""", unsafe_allow_html=True) 
    
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc, color="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- LÓGICA DE TELAS ---

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        h1, h2, h3, h4 = st.columns(4)
        with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
        with h2: draw_card("ASSERTIVIDADE", "92.4%", 92)
        with h3: draw_card("SUGESTÃO", "OVER 2.5", 88)
        with h4: draw_card("IA STATUS", "ONLINE", 100)
        st.dataframe(df_diario, use_container_width=True)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
    st.session_state.stake_padrao = st.slider("STAKE (%)", 0.5, 10.0, st.session_state.stake_padrao)
    st.write(f"Valor por entrada: R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}")

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    # --- NOVO FILTRO GEOGRÁFICO INTEGRADO ---
    db_geografia = {
        "BRASIL": {
            "ligas": ["SERIE A", "SERIE B", "COPA DO BRASIL", "ESTADUAIS"],
            "times": ["Flamengo", "Palmeiras", "Vasco", "Corinthians", "Sao Paulo", "Gremio", "Inter", "Atletico-MG", "Fluminense", "Botafogo"]
        },
        "EUROPA": {
            "ligas": ["PREMIER LEAGUE", "LA LIGA", "BUNDESLIGA", "SERIE A TIM", "CHAMPIONS"],
            "times": ["Man City", "Arsenal", "Liverpool", "Real Madrid", "Barcelona", "Bayern", "PSG", "Inter Milan"]
        }
    }

    col_geo1, col_geo2 = st.columns(2)
    with col_geo1:
        sel_regiao = st.selectbox("🌎 SELECIONE A REGIÃO", list(db_geografia.keys()))
    with col_geo2:
        sel_liga = st.selectbox("🏆 COMPETIÇÃO", db_geografia[sel_regiao]["ligas"])

    lista_times = db_geografia[sel_regiao]["times"]
    
    c1, c2 = st.columns(2)
    with c1:
        t_casa = st.selectbox("🏠 TIME DA CASA", lista_times)
    with c2:
        # TRAVA: Remove o time da casa da lista de fora
        lista_fora = [t for t in lista_times if t != t_casa]
        t_fora = st.selectbox("🚀 TIME DE FORA", lista_fora)

    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        st.info(f"Análise processada: {t_casa} x {t_fora}")

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    st.info("Aguardando jogos ao vivo...")

elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🏆 VENCEDORES DA COMPETIÇÃO</h2>", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ APOSTAS POR GOLS</h2>", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 APOSTAS POR ESCANTEIOS</h2>", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    if not st.session_state.historico_calls: st.write("Nenhuma call salva.")

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v58.3</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
