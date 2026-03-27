import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v58.2 - INTEGRAÇÃO DATA-AUTOMATION]
# DIRETRIZ 6: FILTRAGEM GEOGRÁFICA RESTRITA (SEM MISTURA DE LIGAS)
# DIRETRIZ 7: TRAVA DE DUPLICIDADE (FLAMENGO X FLAMENGO BLOQUEADO)
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

# --- FUNÇÃO DE CARREGAMENTO DE DADOS ---
def carregar_jogos_diarios():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try: return pd.read_csv(path)
        except: return None
    return None

df_diario = carregar_jogos_diarios()

# 2. CAMADA DE ESTILO CSS (MANTIDA INTEGRAL v57.35)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important; font-family: 'Inter', sans-serif;
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

# 3. HEADER E SIDEBAR
with st.sidebar:
    st.markdown("""<div class="betano-header"><div class="logo-link">GESTOR IA</div><div style="background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 8px 22px; border-radius: 5px; font-weight: 800; font-size: 9.5px;">SISTEMA ATIVO</div></div><div style="height:65px;"></div>""", unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"

def draw_card(title, value, perc, color="#6d28d9"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- LÓGICA DE TELAS ---

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA (MUNDO)</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        st.dataframe(df_diario, use_container_width=True)
    else:
        st.warning("Aguardando sincronização de dados...")

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    # --- ORGANIZAÇÃO GEOGRÁFICA RESTRITA ---
    db_paises = {
        "BRASIL 🇧🇷": ["SÉRIE A", "SÉRIE B", "ESTADUAIS", "COPA DO BRASIL"],
        "INGLATERRA 🏴󠁧󠁢󠁥󠁮󠁧󠁿": ["PREMIER LEAGUE", "CHAMPIONSHIP"],
        "ESPANHA 🇪🇸": ["LA LIGA"],
        "ALEMANHA 🇩🇪": ["BUNDESLIGA"]
    }

    # Times Estritamente Ligados ao seu País
    db_times_geograficos = {
        "BRASIL 🇧🇷": ["Flamengo", "Palmeiras", "Vasco", "São Paulo", "Corinthians", "Fluminense", "Botafogo", "Grêmio", "Internacional", "Atlético-MG", "Bahia", "Santos"],
        "INGLATERRA 🏴󠁧󠁢󠁥󠁮󠁧󠁿": ["Man City", "Arsenal", "Liverpool", "Chelsea", "Man United", "Tottenham", "Aston Villa", "Newcastle"],
        "ESPANHA 🇪🇸": ["Real Madrid", "Barcelona", "Atlético Madrid", "Sevilla", "Girona", "Real Betis"],
        "ALEMANHA 🇩🇪": ["Bayer Leverkusen", "Bayern Munchen", "Dortmund", "RB Leipzig"]
    }

    # 1. Seleção de Região
    sel_pais = st.selectbox("🌎 REGIÃO / PAÍS", list(db_paises.keys()))
    
    # 2. Seleção de Competição (Filtra apenas as ligas do país selecionado)
    sel_comp = st.selectbox("🏆 COMPETIÇÃO", db_paises[sel_pais])

    st.markdown("<div style='margin-top:20px; border-bottom: 1px solid #1e293b;'></div>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:white; margin-top:15px;'>⚔️ DEFINIR CONFRONTO</h4>", unsafe_allow_html=True)

    # --- LÓGICA DE TRAVA DE DUPLICIDADE ---
    # Busca a lista de times correspondente apenas àquela região
    lista_times_possiveis = db_times_geograficos.get(sel_pais, ["Time A", "Time B"])

    c1, c2 = st.columns(2)
    with c1:
        # Time da Casa
        t_casa = st.selectbox("🏠 TIME DA CASA", lista_times_possiveis)
    
    with c2:
        # Time de Fora (Remove o time da casa da lista para evitar Flamengo x Flamengo)
        lista_fora_filtrada = [time for time in lista_times_possiveis if time != t_casa]
        t_fora = st.selectbox("🚀 TIME DE FORA", lista_fora_filtrada)

    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        # Aqui o robô JARVIS processa a análise
        st.session_state.analise_bloqueada = {
            "casa": t_casa, "fora": t_fora, "data": datetime.now().strftime("%H:%M")
        }
        st.success(f"Análise processada para {t_casa} x {t_fora}")

# Mantém o footer
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v58.2</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
