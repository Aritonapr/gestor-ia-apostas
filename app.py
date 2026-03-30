import streamlit as st
import pandas as pd
import os
import requests
import io
from datetime import datetime

# ==============================================================================
# PROTOCOLO JARVIS v64.0 - RESTAURAÇÃO VISUAL TOTAL + MOTOR ESTÁVEL
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CAMADA DE ESTILO CSS (IDÊNTICO À IMAGEM ENVIADA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800;900&display=swap');
    
    /* Fundo e Fonte Global */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: white !important;
    }

    /* Esconder Header Padrão do Streamlit */
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 80px 40px 20px 40px !important; }

    /* Cabeçalho Superior Personalizado */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px; z-index: 10000; 
    }
    .logo-text { color: #9d54ff !important; font-weight: 900; font-size: 24px; letter-spacing: -1px; }
    .nav-top-links { display: flex; gap: 20px; align-items: center; }
    .nav-top-item { color: #ffffff; font-size: 10px; font-weight: 700; text-transform: uppercase; opacity: 0.8; }
    .btn-entrar { background: linear-gradient(90deg, #6d28d9, #06b6d4); color: white; padding: 8px 25px; border-radius: 5px; font-weight: 800; font-size: 11px; text-transform: uppercase; }

    /* Menu Lateral (Sidebar) */
    [data-testid="stSidebar"] { background-color: #11151a !important; border-right: 1px solid #1e293b !important; min-width: 300px !important; }
    .st-emotion-cache-16q986n { background-color: transparent !important; }
    
    /* Botões da Sidebar Customizados */
    .sidebar-btn-container div.stButton > button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        text-align: left !important; width: 100% !important; padding: 12px 20px !important; 
        font-size: 13px !important; font-weight: 600 !important; text-transform: uppercase !important;
        border-bottom: 1px solid #1a202c !important; border-radius: 0px !important;
    }
    .sidebar-btn-container div.stButton > button:hover { color: #06b6d4 !important; background-color: #1e293b !important; }

    /* Cards do Bilhete Ouro (Igual à Imagem) */
    .kpi-card {
        background: #11151a; border: 1px solid #1e293b; padding: 25px 15px;
        border-radius: 12px; text-align: center; height: 160px;
    }
    .kpi-title { color: #64748b; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .kpi-value { color: white; font-size: 22px; font-weight: 900; margin-bottom: 15px; }
    .progress-bg { background: #1e293b; height: 4px; width: 70%; margin: 0 auto; border-radius: 10px; position: relative; }
    .progress-fill { position: absolute; left: 0; top: 0; height: 100%; border-radius: 10px; background: linear-gradient(90deg, #6d28d9, #06b6d4); }

    /* Footer de Status */
    .footer-status { position: fixed; bottom: 0; left: 0; width: 100%; background: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 1000; }
    </style>
""", unsafe_allow_html=True)

# --- INICIALIZAÇÃO DE ESTADO ---
if 'aba' not in st.session_state: st.session_state.aba = "bilhete"

# --- FUNÇÕES DE MOTOR ESTÁVEL ---
def carregar_diario():
    try:
        url = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
        df = pd.read_csv(f"{url}?v={datetime.now().timestamp()}")
        df.columns = [c.upper() for c in df.columns]
        return df
    except: return None

def carregar_hist():
    if os.path.exists('data/historico_5_temporadas.csv'):
        df = pd.read_csv('data/historico_5_temporadas.csv')
        df.columns = [c.upper() for c in df.columns]
        return df
    return None

df_hoje = carregar_diario()
df_hist = carregar_hist()

# --- HEADER SUPERIOR ---
st.markdown("""
    <div class="betano-header">
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-top-links">
            <div class="nav-top-item">APOSTAS ESPORTIVAS</div>
            <div class="nav-top-item">APOSTAS AO VIVO</div>
            <div class="nav-top-item">ESTATÍSTICAS AVANÇADAS</div>
            <div class="btn-entrar">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR PERSONALIZADA ---
with st.sidebar:
    st.markdown('<div style="height:60px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-btn-container">', unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba = "scanner"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba = "gestao"
    if st.button("📅 BILHETE OURO"): st.session_state.aba = "bilhete"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba = "calls"
    st.markdown('</div>', unsafe_allow_html=True)

# --- FUNÇÃO PARA DESENHAR OS CARDS DA IMAGEM ---
def draw_kpi(title, value, progress_width):
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">{title}</div>
            <div class="kpi-value">{value}</div>
            <div class="progress-bg">
                <div class="progress-fill" style="width: {progress_width}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- CONTEÚDO PRINCIPAL ---
if st.session_state.aba == "bilhete":
    st.markdown("<h1 style='font-size:32px; font-weight:800; margin-bottom:30px;'>📅 BILHETE OURO</h1>", unsafe_allow_html=True)
    
    # Primeira Linha de Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_kpi("BANCA ATUAL", "R$ 1.000,00", 100)
    with c2: draw_kpi("ASSERTIVIDADE", "92.4%", 92)
    with c3: draw_kpi("SUGESTÃO", "OVER 2.5", 75)
    with c4: draw_kpi("IA STATUS", "ONLINE", 100)
    
    # Segunda Linha de Cards
    c5, c6, c7, c8 = st.columns(4)
    with c5: draw_kpi("VOL. GLOBAL", "ALTO", 85)
    with c6: draw_kpi("STAKE PADRÃO", "1.0%", 10)
    with c7: draw_kpi("VALOR ENTRADA", "R$ 10,00", 100)
    with c8: draw_kpi("SISTEMA", "JARVIS v64.0", 100)

    st.markdown("<br><h3 style='font-size:18px; font-weight:700;'>📋 ANÁLISE COMPLETA DO DIA</h3>", unsafe_allow_html=True)
    if df_hoje is not None:
        st.dataframe(df_hoje, use_container_width=True)
    else:
        st.info("Sincronizando banco de dados...")

elif st.session_state.aba == "scanner":
    st.markdown("<h1 style='font-size:32px; font-weight:800; margin-bottom:30px;'>🎯 SCANNER PRÉ-LIVE</h1>", unsafe_allow_html=True)
    if df_hoje is not None:
        # Usa iloc para evitar erros de nomes de colunas que sumiram antes
        lista_times = sorted(list(set(df_hoje.iloc[:,2].astype(str).unique().tolist() + df_hoje.iloc[:,3].astype(str).unique().tolist())))
        
        col1, col2 = st.columns(2)
        with col1: t1 = st.selectbox("🏠 TIME DA CASA", lista_times)
        with col2: t2 = st.selectbox("🚀 TIME DE FORA", [t for t in lista_times if t != t1])
        
        if st.button("🚀 EXECUTAR ALGORITIMO"):
            st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
            r1, r2, r3, r4 = st.columns(4)
            with r1: draw_kpi("PROB. VITÓRIA", "68%", 68)
            with r2: draw_kpi("GOLS", "OVER 1.5", 94)
            with r3: draw_kpi("CANTOS", "9.5+", 82)
            with r4: draw_kpi("IA CONF.", "96.8%", 96)

# --- RODAPÉ DE STATUS ---
st.markdown(f"""
    <div class="footer-status">
        <div>STATUS: ● IA OPERACIONAL | v64.0</div>
        <div>JARVIS PROTECT © 2026</div>
    </div>
""", unsafe_allow_html=True)
