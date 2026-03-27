import streamlit as st
import pandas as pd
import os

# 1. Configuração inicial (Deve ser a primeira!)
st.set_page_config(page_title="GESTOR IA v96.3", layout="wide")

# 2. CSS Blindado (Identidade Betano)
st.markdown("""
    <style>
    [data-testid="stHeader"] { visibility: hidden; }
    .stApp { background-color: #0b0e11 !important; color: white; }
    .header-fix {
        position: fixed; top: 0; left: 0; width: 100%; height: 60px;
        background-color: #001a4d; border-bottom: 2px solid #9d54ff;
        display: flex; align-items: center; justify-content: center;
        z-index: 999;
    }
    .spacer { padding-top: 70px; }
    </style>
    <div class="header-fix">
        <h2 style="color:#9d54ff; margin:0;">GESTOR IA - TRADING PRO</h2>
    </div>
    <div class="spacer"></div>
""", unsafe_allow_html=True)

# 3. Carregamento de Dados
path = "data/database_diario.csv"
if os.path.exists(path):
    df = pd.read_csv(path)
    st.success(f"📈 Sistema Online: {len(df)} jogos processados.")
    st.dataframe(df, use_container_width=True)
else:
    st.warning("⏳ JARVIS: Sincronizando dados históricos... Por favor, aguarde o primeiro processamento do sync_data.py no GitHub Actions.")
    st.info("DICA: Verifique a aba 'Actions' no seu GitHub para ver se o robô já terminou de baixar as 5 temporadas.")
