import streamlit as st
import time
import pandas as pd
import os
import requests
from io import StringIO

# ==============================================================================
# [GIAE KERNEL SHIELD v46.1 - STABLE RESTORATION]
# FIX: SESSION STATE LOCK | DIRECTORY REUSE | ERROR PREVENTION
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- [01] INICIALIZAÇÃO SEGURA (EVITA O ERRO DA IMAGEM) ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'analise_pronta' not in st.session_state:
    st.session_state.analise_pronta = False
if 'banca_atual' not in st.session_state:
    st.session_state.banca_atual = 1000.0

# --- [02] DIRETÓRIOS DE DADOS ---
DATA_DIR = "giae_core_data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
DB_PATH = os.path.join(DATA_DIR, "historico_estatistico.csv")

# --- [03] BLOCO DE SEGURANÇA CSS (RIGOROSAMENTE MANTIDO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; }
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; text-decoration: none !important; }
    .nav-items span { color: #ffffff; font-size: 10px !important; text-transform: uppercase; margin-right: 15px; opacity: 0.8; }
    .registrar-pill { color: #ffffff !important; font-size: 10px !important; font-weight: 700; border: 1px solid #ffffff !important; padding: 6px 15px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 7px 20px !important; border-radius: 4px !important; font-weight: 800; font-size: 10px !important; }
    [data-testid="stSidebar"] button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; }
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; transition: 0.3s; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- [04] FUNÇÃO DE DADOS (SIMPLIFICADA) ---
def sync_data():
    """Busca dados e salva no CSV da pasta ja criada."""
    try:
        url = "https://www.football-data.co.uk/mmz4281/2324/E0.csv" # Exemplo estável
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            df = pd.read_csv(StringIO(res.text))
            # Processa apenas o básico para não pesar
            stats = []
            teams = pd.unique(df[['HomeTeam', 'AwayTeam']].values.ravel('K'))
            for t in teams:
                stats.append({'time': t, 'win_rate': 0.65, 'gols_pro': 1.8})
            pd.DataFrame(stats).to_csv(DB_PATH, index=False)
            return True
    except: return False
    return False

# --- [05] CABEÇALHO ---
st.markdown("""
    <div class="betano-header">
        <div class="header-left">
            <a class="logo-link">GESTOR IA</a>
            <div class="nav-items"><span>Apostas Esportivas</span><span>Estatísticas Avançadas</span></div>
        </div>
        <div class="header-right">
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- [06] SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "scanner_live"
    st.markdown("---")
    if st.button("🔄 ATUALIZAR BANCO DE DADOS"):
        if sync_data(): st.success("DADOS SINCRONIZADOS!")
        else: st.error("ERRO NA CONEXÃO.")

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- [07] LOGICA DE TELAS ---
if st.session_state.aba_ativa == "home":
    st.markdown('<div class="news-ticker">● SISTEMA OPERACIONAL | AGUARDANDO COMANDO</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    for c in [c1, c2, c3, c4]:
        with c: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">STATUS</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">AGUARDANDO</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:10%;"></div></div></div>', unsafe_allow_html=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">🎯 SCANNER PRÉ-LIVE</div>', unsafe_allow_html=True)
    
    # Se o CSV existir, usa ele. Se não, usa lista padrão.
    if os.path.exists(DB_PATH):
        df_local = pd.read_csv(DB_PATH)
        times = sorted(df_local['time'].tolist())
    else:
        times = ["Flamengo", "Palmeiras", "Real Madrid", "Arsenal"]

    t1, t2 = st.columns(2)
    with t1: casa = st.selectbox("🏠 CASA", times)
    with t2: fora = st.selectbox("🚀 VISITANTE", times)

    if st.button("⚡ EXECUTAR"):
        st.session_state.analise_pronta = True

    if st.session_state.analise_pronta:
        st.markdown(f'<div class="news-ticker">ANÁLISE: {casa} vs {fora}</div>', unsafe_allow_html=True)
        # 8 CARDS DE RESULTADO (ESTRUTURA FIXA)
        r1, r2, r3, r4 = st.columns(4)
        for r in [r1, r2, r3, r4]:
            with r: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">INDICADOR</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">CALCULADO</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:80%;"></div></div></div>', unsafe_allow_html=True)
        
        st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
        
        r5, r6, r7, r8 = st.columns(4)
        for r in [r5, r6, r7, r8]:
            with r: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">MERCADO</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">DETECTADO</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)

# --- [08] FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL</div><div>GESTOR IA PRO v46.1 | JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
