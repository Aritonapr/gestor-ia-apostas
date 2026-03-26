import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime
import time

# ==============================================================================
# 🔒 [DIRETRIZ DE PROTEÇÃO JARVIS v93.00 - SISTEMA DE MEMÓRIA E MONITORAMENTO]
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- FUNÇÃO DE VERIFICAÇÃO DE DADOS (NOVO) ---
def get_status_dados():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        # Captura a data de modificação do arquivo
        mtime = os.path.getmtime(path)
        dt_mod = datetime.fromtimestamp(mtime)
        agora = datetime.now()
        
        # Se o arquivo foi modificado hoje, fica Verde, senão Alerta (Laranja/Vermelho)
        cor_status = "#4ade80" if dt_mod.date() == agora.date() else "#fb923c"
        return dt_mod.strftime("%d/%m %H:%M"), cor_status
    return "SEM DADOS", "#ef4444"

ultima_sync, cor_sync = get_status_dados()

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba' not in st.session_state: st.session_state.aba = "bilhete"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

def carregar_dados():
    path = "data/database_diario.csv"
    if os.path.exists(path): return pd.read_csv(path)
    return None

df = carregar_dados()

# --- CAMADA DE ESTILO CSS (RESTAURAÇÃO TOTAL + FIX TABELA) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar {{ display: none !important; }}
    html, body, .stApp {{ background-color: #0b0e11 !important; color: white; font-family: 'Inter', sans-serif; }}
    header {{ display: none !important; }}
    
    .betano-header {{ 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.1); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px; z-index: 1000000;
    }}
    .logo-ia {{ color: #9d54ff !important; font-weight: 900; font-size: 21px; text-transform: uppercase; text-decoration: none; }}
    
    .status-badge {{
        background: rgba(255,255,255,0.05);
        padding: 5px 12px;
        border-radius: 20px;
        border: 1px solid {cor_sync};
        color: {cor_sync};
        font-size: 10px;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .dot {{ height: 8px; width: 8px; background-color: {cor_sync}; border-radius: 50%; display: inline-block; }}

    [data-testid="stSidebar"] {{ min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b; }}
    section[data-testid="stSidebar"] div.stButton > button {{ 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 16px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }}
    section[data-testid="stSidebar"] div.stButton > button:hover {{ background-color: #1e293b !important; color: #06b6d4 !important; border-left: 4px solid #6d28d9 !important; }}

    .stDataFrame {{ background: #161b22; border-radius: 8px; border: 1px solid #30363d; padding: 10px; }}
    .metric-card {{ background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; margin-bottom: 15px; }}
    .bilhete-master {{ background: #ffffff !important; color: #111 !important; padding: 25px; border-radius: 8px; max-width: 500px; margin: 0 auto; border-top: 10px solid #9d54ff; box-shadow: 0 10px 40px rgba(0,0,0,0.8); }}
    .ticket-row {{ display: flex; justify-content: space-between; font-size: 11px; border-bottom: 1px solid #f2f2f2; padding: 8px 0; color: #111 !important; }}
    .history-card {{ background: #161b22; border-left: 4px solid #9d54ff; padding: 15px; border-radius: 6px; margin-bottom: 10px; }}
    </style>
""", unsafe_allow_html=True)

# --- HEADER FIXO COM MONITOR DE ATUALIZAÇÃO ---
st.markdown(f"""
    <div class="betano-header">
        <div class="logo-ia">GESTOR IA</div>
        <div style="display:flex; gap:20px; align-items:center;">
            <div class="status-badge"><span class="dot"></span> BANCO DE DADOS: {ultima_sync}</div>
            <span style="color:white; font-size:10px; font-weight:700; opacity:0.6;">APOSTAS ESPORTIVAS</span>
            <span style="color:white; font-size:10px; font-weight:700; opacity:0.6;">ESTATÍSTICAS 7 NÍVEIS</span>
        </div>
        <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:8px 25px; border-radius:5px; font-size:9px; font-weight:900; cursor:pointer;">SISTEMA ONLINE</div>
    </div>
""", unsafe_allow_html=True)

# ... (Restante do código das abas continua igual)
