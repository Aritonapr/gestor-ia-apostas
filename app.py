import streamlit as st
import pandas as pd
import os

# ==============================================================================
# [PROTOCOLO JARVIS v65.0 - NÚCLEO DE RESSURREIÇÃO]
# DIRETRIZ: BOOT IMEDIATO E TRATAMENTO DE 2026
# ==============================================================================

# 1. BOOT PRIORITÁRIO
st.set_page_config(page_title="GESTOR IA", layout="wide")

# 2. MEMÓRIA DE SEGURANÇA
if 'aba' not in st.session_state: st.session_state['aba'] = "home"
if 'banca' not in st.session_state: st.session_state['banca'] = 1000.0

# 3. INTERFACE SIMPLIFICADA (ESTILO BETANO)
st.markdown("""
    <style>
    .stApp { background-color: #0b0e11; color: white; }
    [data-testid="stHeader"] { display: none; }
    .card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# 4. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color:#9d54ff;'>GESTOR IA</h2>", unsafe_allow_html=True)
    st.write("---")
    if st.button("📅 BILHETE OURO"): st.session_state.aba = "home"
    if st.button("💰 GESTÃO"): st.session_state.aba = "gestao"

# 5. CARREGAMENTO DE DADOS (2026)
def check_data():
    if os.path.exists("data/database_diario.csv"):
        try: return pd.read_csv("data/database_diario.csv")
        except: return None
    return None

df = check_data()

# 6. TELAS
if st.session_state.aba == "home":
    st.markdown("## 📅 BILHETE OURO - MARÇO 2026")
    
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown('<div class="card">BANCA<br><b>R$ %.2f</b></div>' % st.session_state.banca, unsafe_allow_html=True)
    with col2: st.markdown('<div class="card">STATUS<br><b>IA ONLINE</b></div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="card">ANO<br><b>2026</b></div>', unsafe_allow_html=True)

    if df is not None:
        st.write("### 📋 JOGOS ENCONTRADOS")
        st.dataframe(df, use_container_width=True)
    else:
        st.info("🤖 Jarvis: Aguardando sincronização do GitHub Actions...")

elif st.session_state.aba == "gestao":
    st.markdown("## 💰 GESTÃO DE BANCA")
    st.session_state.banca = st.number_input("BANCA TOTAL", value=st.session_state.banca)

st.markdown("<br><br><p style='font-size:10px; color:gray;'>JARVIS v65.0 | PROTECT MODE</p>", unsafe_allow_html=True)
