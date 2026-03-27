import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. CONFIGURAÇÃO INICIAL (OBRIGATÓRIO SER A PRIMEIRA LINHA)
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide")

# 2. FUNÇÃO DE VERIFICAÇÃO DE DADOS
def carregar_dados():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            if not df.empty:
                return df
        except:
            return None
    return None

df = carregar_dados()

# 3. ESTILO CSS PARA O HEADER BETANO
st.markdown("""
    <style>
    [data-testid="stHeader"] { visibility: hidden; }
    .stApp { background-color: #0b0e11 !important; color: white; }
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 2px solid #9d54ff; 
        display: flex; align-items: center; justify-content: center; 
        z-index: 10000;
    }
    .main-content { padding-top: 80px; }
    </style>
    <div class="betano-header">
        <div style="color:#9d54ff; font-weight:900; font-size:22px;">GESTOR IA - TRADING PRO</div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-content"></div>', unsafe_allow_html=True)

# 4. TELA DE CARREGAMENTO OU CONTEÚDO
if df is None:
    st.error("🚨 SISTEMA EM SINCRONIZAÇÃO INICIAL")
    st.info("Senhor, o JARVIS está baixando as 5 temporadas e processando os jogos de hoje. Isso ocorre apenas na primeira vez. Por favor, aguarde 30 segundos e clique no botão abaixo.")
    if st.button("🔄 ATUALIZAR SISTEMA"):
        st.rerun()
else:
    st.success(f"✅ SISTEMA ONLINE - {len(df)} JOGOS ANALISADOS")
    
    # --- AQUI VAI O SEU CÓDIGO DAS ABAS ---
    aba = st.sidebar.selectbox("MENU", ["🎟️ BILHETE DO DIA", "🎯 SCANNER"])
    
    if aba == "🎟️ BILHETE DO DIA":
        st.write("### 🎟️ BILHETE MESTRE IA")
        st.dataframe(df, use_container_width=True)
    
    # ... (Restante da sua lógica de abas pode ser colada aqui)
