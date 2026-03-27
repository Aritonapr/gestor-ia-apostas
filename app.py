import streamlit as st
import pandas as pd
import os

# ==============================================================================
# 🔒 [PROTOCOLO JARVIS v97.1 - REFINO FINAL DE INTERFACE]
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CARREGAMENTO DE DADOS ---
def carregar_dados():
    path = "data/database_diario.csv"
    if os.path.exists(path): return pd.read_csv(path)
    return None

df = carregar_dados()

# --- CSS DE ALTA PRECISÃO (REMOÇÃO DE FUNDO BRANCO E AJUSTE NEON) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;900&display=swap');
    
    /* Reset Geral */
    html, body, .stApp { background-color: #0b0e11 !important; color: white !important; font-family: 'Inter', sans-serif; }
    [data-testid="stHeader"] { visibility: hidden; }
    ::-webkit-scrollbar { display: none; }

    /* Estilização da Sidebar (Fundo Escuro) */
    section[data-testid="stSidebar"] { background-color: #060d17 !important; border-right: 1px solid #1e293b; }
    
    /* BOTÕES DA SIDEBAR - REMOVENDO O BRANCO */
    section[data-testid="stSidebar"] div.stButton > button {
        background-color: #111827 !important;
        color: #94a3b8 !important;
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
        width: 100% !important;
        text-align: left !important;
        padding: 12px 15px !important;
        font-size: 11px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        margin-bottom: -10px !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        border-color: #9d54ff !important;
        color: #9d54ff !important;
        background-color: #1e293b !important;
    }

    /* HEADER BETANO FIXO */
    .betano-header {
        position: fixed; top: 0; left: 0; width: 100%; height: 60px;
        background-color: #060d17; border-bottom: 1px solid #1e293b;
        display: flex; align-items: center; justify-content: space-between;
        padding: 0 30px; z-index: 10000;
    }
    .nav-links span { color: #94a3b8; font-size: 10px; font-weight: 700; margin: 0 15px; text-transform: uppercase; cursor: pointer; }
    .nav-links span:hover { color: white; }

    /* CARDS DE MÉTRICAS */
    .metric-card {
        background: #111827; border: 1px solid #1e293b; border-radius: 10px;
        padding: 15px; text-align: center; margin-bottom: 15px;
    }
    .m-label { color: #64748b; font-size: 9px; font-weight: 800; text-transform: uppercase; margin-bottom: 5px; }
    .m-value { color: white; font-size: 18px; font-weight: 900; }
    .progress-container { background: #1f2937; height: 3px; border-radius: 5px; width: 100%; margin-top: 10px; }
    .progress-fill { background: #9d54ff; height: 3px; border-radius: 5px; box-shadow: 0 0 10px #9d54ff; }

    /* Ajuste de Conteúdo */
    .main-box { padding-top: 50px; }
    
    /* Estilo da Tabela */
    .stDataFrame { background: #060d17 !important; border-radius: 10px; border: 1px solid #1e293b; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SUPERIOR ---
st.markdown("""
    <div class="betano-header">
        <div style="color:#9d54ff; font-weight:900; font-size:22px;">GESTOR IA</div>
        <div class="nav-links">
            <span>APOSTAS ESPORTIVAS</span>
            <span>APOSTAS AO VIVO</span>
            <span>ESTATÍSTICAS AVANÇADAS</span>
            <span>MERCADO PROBABILÍSTICO</span>
        </div>
        <div style="display:flex; gap:10px;">
            <div style="background:#6d28d9; padding:8px 20px; border-radius:5px; font-size:10px; font-weight:900; cursor:pointer;">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:70px;"></div>', unsafe_allow_html=True)
    st.button("🎯 SCANNER PRÉ-LIVE")
    st.button("💰 GESTÃO DE BANCA")
    st.button("📅 JOGOS DO DIA")
    st.button("🏆 VENCEDORES")
    st.button("⚽ APOSTAS POR GOLS")
    st.button("🚩 ESCANTEIOS")

# --- CONTEÚDO ---
st.markdown('<div class="main-box"></div>', unsafe_allow_html=True)

if df is not None:
    st.markdown("<h2 style='font-size:24px; font-weight:900;'>📋 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    
    # Grid de Cards (Linha 1)
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown('<div class="metric-card"><div class="m-label">BANCA ATUAL</div><div class="m-value">R$ 1.000,00</div><div class="progress-container"><div class="progress-fill" style="width:70%;"></div></div></div>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="metric-card"><div class="m-label">ASSERTIVIDADE</div><div class="m-value">92.4%</div><div class="progress-container"><div class="progress-fill" style="width:92%;"></div></div></div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="metric-card"><div class="m-label">SUGESTÃO</div><div class="m-value">OVER 2.5</div><div class="progress-container"><div class="progress-fill" style="width:85%;"></div></div></div>', unsafe_allow_html=True)
    with col4: st.markdown('<div class="metric-card"><div class="m-label">IA STATUS</div><div class="m-value">ONLINE</div><div class="progress-container"><div class="progress-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)
    
    # Grid de Cards (Linha 2)
    col5, col6, col7, col8 = st.columns(4)
    with col5: st.markdown('<div class="metric-card"><div class="m-label">VOL. GLOBAL</div><div class="m-value">ALTO</div><div class="progress-container"><div class="progress-fill" style="width:80%;"></div></div></div>', unsafe_allow_html=True)
    with col6: st.markdown('<div class="metric-card"><div class="m-label">STAKE PADRÃO</div><div class="m-value">1.0%</div><div class="progress-container"><div class="progress-fill" style="width:10%;"></div></div></div>', unsafe_allow_html=True)
    with col7: st.markdown('<div class="metric-card"><div class="m-label">VALOR ENTRADA</div><div class="m-value">R$ 10,00</div><div class="progress-container"><div class="progress-fill" style="width:40%;"></div></div></div>', unsafe_allow_html=True)
    with col8: st.markdown('<div class="metric-card"><div class="m-label">SISTEMA</div><div class="m-value">JARVIS v97.1</div><div class="progress-container"><div class="progress-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)

    st.markdown("### 📋 ANÁLISE DETALHADA (7 NÍVEIS)")
    st.dataframe(df, use_container_width=True)
