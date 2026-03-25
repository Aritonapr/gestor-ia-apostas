import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE RESTAURAÇÃO TOTAL v61.00 - FIDELIDADE VISUAL IMAGEM 1 E 2]
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- NAVEGAÇÃO POR LINK (MENU SUPERIOR) ---
query_params = st.query_params
if "go" in query_params:
    st.session_state.aba_ativa = query_params["go"]

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None

# --- CARREGAMENTO DE DADOS ---
def carregar_dados():
    path_db = "data/database_diario.csv"
    path_hist = "data/historico_permanente.csv"
    df_d = pd.read_csv(path_db) if os.path.exists(path_db) else None
    df_h = pd.read_csv(path_hist) if os.path.exists(path_hist) else pd.DataFrame()
    return df_d, df_h

df_diario, df_historico_full = carregar_dados()

# 2. CAMADA DE ESTILO CSS (IDÊNTICO AO SEU ORIGINAL)
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
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    .nav-item-top { color: #ffffff !important; font-size: 11px; text-transform: uppercase; font-weight: 600; text-decoration: none; margin-left: 20px; transition: 0.3s; }
    .nav-item-top:hover { color: #06b6d4 !important; }

    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: all 0.2s ease !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important;
    }

    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: white !important; font-weight: 900 !important; text-transform: uppercase !important;
        border-radius: 6px !important; width: 100% !important; border: none !important; padding: 15px !important;
    }

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
    }
    
    /* FUNDO ESCURO PARA INPUTS */
    div[data-baseweb="input"], .stNumberInput div, div[data-baseweb="select"] > div { background-color: #1a202c !important; color: white !important; }
    input { color: white !important; }
