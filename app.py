import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# 🔒 [PROTOCOLO JARVIS v97.0 - RESTAURAÇÃO DE INTERFACE PREMIUM]
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- MEMÓRIA DE NAVEGAÇÃO ---
if 'aba' not in st.session_state: st.session_state.aba = "jogos"

# --- CARREGAMENTO DE DADOS ---
def carregar_dados():
    path = "data/database_diario.csv"
    if os.path.exists(path): return pd.read_csv(path)
    return None

df = carregar_dados()

# --- ESTILO CSS AVANÇADO (CÓPIA FIEL DA IMAGEM 2) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, .stApp { background-color: #0b0e11 !important; color: white; font-family: 'Inter', sans-serif; }
    [data-testid="stHeader"] { visibility: hidden; }
    ::-webkit-scrollbar { display: none; }

    /* HEADER ESTILO BETANO */
    .betano-header {
        position: fixed; top: 0; left: 0; width: 100%; height: 60px;
        background-color: #060d17; border-bottom: 1px solid #1e293b;
        display: flex; align-items: center; justify-content: space-between;
        padding: 0 30px; z-index: 10000;
    }
    .logo { color: #9d54ff; font-weight: 900; font-size: 22px; letter-spacing: -1px; }
    .nav-links { display: flex; gap: 20px; color: #94a3b8; font-size: 11px; font-weight: 600; text-transform: uppercase; }

    /* SIDEBAR CUSTOMIZADA */
    [data-testid="stSidebar"] { background-color: #060d17 !important; border-right: 1px solid #1e293b; min-width: 260px !important; }
    .sidebar-btn {
        display: flex; align-items: center; padding: 12px 20px;
        color: #94a3b8; font-size: 12px; font-weight: 600;
        text-transform: uppercase; cursor: pointer; border-left: 3px solid transparent;
        transition: 0.3s; margin-bottom: 5px;
    }
    .sidebar-btn:hover { background: #1e293b; color: #9d54ff; border-left: 3px solid #9d54ff; }

    /* CARDS DE MÉTRICAS (ESTILO IMAGEM 2) */
    .metric-container {
        background: #111827; border: 1px solid #1e293b; border-radius: 12px;
        padding: 20px; text-align: center; position: relative; overflow: hidden;
    }
    .metric-label { color: #64748b; font-size: 10px; text-transform: uppercase; font-weight: 800; margin-bottom: 10px; }
    .metric-value { color: white; font-size: 22px; font-weight: 900; margin-bottom: 15px; }
    .progress-bar-bg { background: #1f2937; height: 4px; border-radius: 10px; width: 80%; margin: 0 auto; }
    .progress-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 4px; border-radius: 10px; }

    .main-content { padding-top: 80px; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SUPERIOR ---
st.markdown("""
    <div class="betano-header">
        <div class="logo">GESTOR IA</div>
        <div class="nav-links">
            <span>APOSTAS ESPORTIVAS</span>
            <span>APOSTAS AO VIVO</span>
            <span>ESTATÍSTICAS AVANÇADAS</span>
            <span>MERCADO PROBABILÍSTICO</span>
        </div>
        <div style="display:flex; gap:10px;">
            <div style="border:1px solid #334155; padding:5px 15px; border-radius:20px; font-size:10px;">REGISTRAR</div>
            <div style="background:#6d28d9; padding:5px 20px; border-radius:5px; font-size:10px; font-weight:800;">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR COM BOTÕES ---
with st.sidebar:
    st.markdown('<div style="height:80px;"></div>', unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba = "scanner"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba = "banca"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba = "jogos"
    if st.button("🏆 VENCEDORES"): st.session_state.aba = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba = "gols"
    if st.button("🚩 ESCANTEIOS"): st.session_state.aba = "cantos"

st.markdown('<div class="main-content"></div>', unsafe_allow_html=True)

# --- CONTEÚDO PRINCIPAL ---
if df is not None:
    if st.session_state.aba == "jogos":
        st.markdown("<h2 style='margin-bottom:30px;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
        
        # GRID DE CARDS (IGUAL IMAGEM 2)
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown('<div class="metric-container"><div class="metric-label">BANCA ATUAL</div><div class="metric-value">R$ 1.000,00</div><div class="progress-bar-bg"><div class="progress-bar-fill" style="width:70%;"></div></div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="metric-container"><div class="metric-label">ASSERTIVIDADE</div><div class="metric-value">92.4%</div><div class="progress-bar-bg"><div class="progress-bar-fill" style="width:92%;"></div></div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="metric-container"><div class="metric-label">SUGESTÃO</div><div class="metric-value">OVER 2.5</div><div class="progress-bar-bg"><div class="progress-bar-fill" style="width:85%;"></div></div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown('<div class="metric-container"><div class="metric-label">IA STATUS</div><div class="metric-value">ONLINE</div><div class="progress-bar-bg"><div class="progress-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        c5, c6, c7, c8 = st.columns(4)
        with c5:
            st.markdown('<div class="metric-container"><div class="metric-label">VOL. GLOBAL</div><div class="metric-value">ALTO</div><div class="progress-bar-bg"><div class="progress-bar-fill" style="width:80%;"></div></div></div>', unsafe_allow_html=True)
        with c6:
            st.markdown('<div class="metric-container"><div class="metric-label">STAKE PADRÃO</div><div class="metric-value">1.0%</div><div class="progress-bar-bg"><div class="progress-bar-fill" style="width:10%;"></div></div></div>', unsafe_allow_html=True)
        with c7:
            st.markdown('<div class="metric-container"><div class="metric-label">VALOR ENTRADA</div><div class="metric-value">R$ 10,00</div><div class="progress-bar-bg"><div class="progress-bar-fill" style="width:40%;"></div></div></div>', unsafe_allow_html=True)
        with c8:
            st.markdown('<div class="metric-container"><div class="metric-label">SISTEMA</div><div class="metric-value">JARVIS v97.0</div><div class="progress-bar-bg"><div class="progress-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)

        st.markdown("### 📋 ANÁLISE DETALHADA (7 NÍVEIS)")
        st.dataframe(df, use_container_width=True)

else:
    st.error("ERRO: Banco de dados não encontrado. Rodar sync_data.py primeiro.")
