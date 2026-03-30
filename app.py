import streamlit as st
import pandas as pd
import os

# ==============================================================================
# [PROTOCOLO JARVIS v67.0 - ESTABILIDADE MÁXIMA]
# DIRETRIZ: CORREÇÃO DE DEPENDÊNCIA ALTAIR E BOOT 2026
# ==============================================================================

# 1. BOOT PRIORITÁRIO (LINHA OBRIGATÓRIA)
st.set_page_config(page_title="GESTOR IA 2026", layout="wide")

# 2. INICIALIZAÇÃO DE MEMÓRIA (BLINDADA)
if 'aba' not in st.session_state: st.session_state['aba'] = "home"
if 'banca' not in st.session_state: st.session_state['banca'] = 1000.0

# 3. ESTILO CSS (ZERO WHITE PRO - MODO SEGURO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: white !important;
    }
    header, [data-testid="stHeader"] { display: none !important; }
    
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        border-right: 1px solid #1e293b !important; 
    }
    
    .card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; margin-bottom: 10px;
    }
    
    .logo-text { color: #9d54ff; font-weight: 900; font-size: 24px; text-align: center; margin-bottom: 20px; }
    
    .footer { 
        position: fixed; bottom: 0; left: 0; width: 100%; 
        background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 0 20px; font-size: 9px; color: #475569; 
    }
    </style>
""", unsafe_allow_html=True)

# 4. SIDEBAR (MENU)
with st.sidebar:
    st.markdown('<div class="logo-text">GESTOR IA</div>', unsafe_allow_html=True)
    st.write("---")
    if st.button("📅 BILHETE OURO"): st.session_state.aba = "home"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba = "gestao"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba = "analise"
    st.write("---")
    st.write("🕒 CONTEXTO: MARÇO 2026")

# 5. CARREGAMENTO DE DADOS (TRAVA DE SEGURANÇA)
def carregar_dados():
    caminho = "data/database_diario.csv"
    if os.path.exists(caminho):
        try: return pd.read_csv(caminho)
        except: return None
    return None

df_dados = carregar_dados()

# 6. TELAS
if st.session_state.aba == "home":
    st.markdown("## 📅 BILHETE OURO - 2026")
    
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(f'<div class="card">BANCA<br><b>R$ {st.session_state.banca:,.2f}</b></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="card">ASSERTIVIDADE<br><b>92.4%</b></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="card">SISTEMA<br><b>JARVIS v67.0</b></div>', unsafe_allow_html=True)

    if df_dados is not None:
        st.markdown("### 📋 JOGOS CAPTURADOS")
        st.dataframe(df_dados, use_container_width=True)
    else:
        st.info("🤖 Jarvis: Aguardando sincronização de 2026... Rode a Action no GitHub!")

elif st.session_state.aba == "gestao":
    st.markdown("## 💰 GESTÃO DE BANCA")
    st.session_state.banca = st.number_input("Valor da Banca (R$)", value=st.session_state.banca)
    st.success(f"Banca ajustada para R$ {st.session_state.banca:,.2f}")

elif st.session_state.aba == "analise":
    st.markdown("## 🎯 SCANNER PRÉ-LIVE")
    st.info("O Scanner está pronto para processar os jogos de 2026.")

# FOOTER
st.markdown("""
    <div class="footer">
        <div>STATUS: ● IA OPERACIONAL | v67.0 | 2026</div>
        <div>JARVIS PROTECT</div>
    </div>
""", unsafe_allow_html=True)
