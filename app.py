import streamlit as st
import pandas as pd
import os
from datetime import datetime

# CONFIGURAÇÃO DE PÁGINA (Deve ser a primeira linha de código)
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide")

# --- FUNÇÃO DE CARREGAMENTO SEGURO ---
def carregar_dados_seguro():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try:
            return pd.read_csv(path)
        except:
            return None
    return None

df = carregar_dados_seguro()

# --- FUNÇÃO DE STATUS ---
def get_status_dados():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        mtime = os.path.getmtime(path)
        dt_mod = datetime.fromtimestamp(mtime)
        return dt_mod.strftime("%d/%m %H:%M"), "#4ade80"
    return "AGUARDANDO SYNC", "#fb923c"

ultima_sync, cor_sync = get_status_dados()

# --- CSS (MANTIDO) ---
st.markdown(f"""
    <style>
    [data-testid="stHeader"] {{ visibility: hidden; }}
    .stApp {{ background-color: #0b0e11 !important; color: white; }}
    .betano-header {{ 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 2px solid {cor_sync}; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px; z-index: 10000;
    }}
    .main-content {{ padding-top: 80px; }}
    </style>
    <div class="betano-header">
        <div style="color:#9d54ff; font-weight:900; font-size:20px;">GESTOR IA</div>
        <div style="color:{cor_sync}; font-size:12px; font-weight:bold; border:1px solid {cor_sync}; padding:5px 10px; border-radius:5px;">
            📡 STATUS: {ultima_sync}
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-content"></div>', unsafe_allow_html=True)

# --- LÓGICA DE EXIBIÇÃO ---
if df is None:
    st.warning("⚠️ **SISTEMA EM INICIALIZAÇÃO:** O JARVIS está baixando os dados históricos de 5 temporadas e gerando os primeiros bilhetes. Por favor, aguarde 1 minuto e atualize a página.")
    if st.button("🔄 TENTAR RECARREGAR AGORA"):
        st.rerun()
else:
    # AQUI ENTRA O RESTANTE DO SEU CÓDIGO DAS ABAS (O que já tínhamos)
    st.success("SISTEMA OPERACIONAL")
    # ... (cole aqui as abas: bilhete, scanner, etc)
