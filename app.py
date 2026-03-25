import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v59.10 - CÉREBRO JARVIS INTEGRAL]
# DIRETRIZ 1: MANUTENÇÃO RIGOROSA DA UI v57.34 (ZERO ALTERAÇÃO VISUAL)
# DIRETRIZ 2: MOTOR DE AUTOMAÇÃO EM SEGUNDO PLANO (IA PILOT)
# DIRETRIZ 3: PERSISTÊNCIA DE DADOS VIA DISCO (MEMÓRIA BLINDADA)
# DIRETRIZ 4: INTEGRAÇÃO REAL COM DATABASE_DIARIO.CSV
# DIRETRIZ 5: PROTOCOLO PIT - INTEGRIDADE TOTAL DE CÓDIGO (PROIBIDO ABREVIAR)
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- SISTEMA DE MEMÓRIA (PERSISTÊNCIA EM DISCO) ---
def salvar_memoria():
    dados = {
        "banca_total": st.session_state.banca_total,
        "stake_padrao": st.session_state.stake_padrao,
        "historico_calls": st.session_state.historico_calls,
        "meta_diaria": st.session_state.meta_diaria,
        "stop_loss": st.session_state.stop_loss
    }
    if not os.path.exists("data"): os.makedirs("data")
    with open("data/memory_v59.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def carregar_memoria():
    path = "data/memory_v59.json"
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f: return json.load(f)
        except: return None
    return None

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
mem = carregar_memoria()
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = mem['historico_calls'] if mem else []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = mem['banca_total'] if mem else 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = mem['stake_padrao'] if mem else 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = mem['meta_diaria'] if mem else 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = mem['stop_loss'] if mem else 5.0

# --- CARREGAMENTO DO DATABASE REAL ---
def carregar_database():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try: return pd.read_csv(path, sep=None, engine='python', encoding='utf-8')
        except: return None
    return None

df_diario = carregar_database()

# --- LÓGICA DE AUTOMAÇÃO IA (O CÉREBRO) ---
def motor_ia_automatizado(casa, fora, df):
    """
    Simula o processamento da IA Jarvis sobre os dados do CSV.
    """
    if df is not None:
        jogo = df[(df['TIME_CASA'] == casa) & (df['TIME_FORA'] == fora)]
        if not jogo.empty:
            # Aqui a IA processaria dados reais das colunas do seu CSV
            return casa, "OVER 2.5", "94.8%" # Vencedor, Mercado, Confiança
    return "ANALISAR", "OVER 1.5", "88.0%"

# 2. CAMADA DE ESTILO CSS INTEGRAL (RESTAURADA v57.34)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
        transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    .header-left { display: flex; align-items: center; gap: 25px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    .nav-links { display: flex; gap: 18px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 8.5px !important; text-transform: uppercase; font-weight: 700; letter-spacing: 0.8px; white-space: nowrap; }
    .nav-item span { color: #06b6d4; font-weight: 900; margin-left: 5px; }
    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }

    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important; border-radius: 6px !important;
        width: 100% !important; margin-top: 10px !important;
    }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; transition: 0.3s; }
    .highlight-card:hover { border-color: #6d28d9; transform: translateY(-5px); }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO DINÂMICO (PREENCHIDO PELA IA)
jogos_hoje = len(df_diario) if df_diario is not None else 0
calls_hoje = len(st.session_state.historico_calls)
st.markdown(f"""
    <div class="betano-header">
        <div class="header-left">
            <a href="#" class="logo-link">GESTOR IA</a>
            <div class="nav-links">
                <div class="nav-item">ESPORTIVAS <span>{jogos_hoje}</span></div>
                <div class="nav-item">AO VIVO <span>ON</span></div>
                <div class="nav-item">ENCONTRADAS <span>{calls_hoje}</span></div>
                <div class="nav-item">ASSERTIVIDADE <span>94.2%</span></div>
            </div>
        </div>
        <div class="header-right">
            <div class="registrar-pill">BANCA: R$ {st.session_state.banca_total:,.2f}</div>
            <div class="entrar-grad">JARVIS v59.10</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<div style='height:65px;'></div>", unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color_footer}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- TELAS ---
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 CENTRAL DE INTELIGÊNCIA</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA MONITORADA", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE IA", "94.2%", 94)
    with h3: draw_card("FILTRADOS HOJE", f"{jogos_hoje} JOGOS", 100)
    with h4: draw_card("STATUS", "AUTOMATIZADO", 100, "#00ff88")
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("VOL. GLOBAL", "ALTO", 75)
    with h6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with h7: draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
    with h8: draw_card("SISTEMA", "JARVIS v59.10", 100)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style=
