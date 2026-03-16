import streamlit as st
import time
import random

# ==============================================================================
# [GIAE KERNEL SHIELD v42.3 - EFEITO ISOLADO NO BOTÃO EXECUTAR]
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CONTROLE DE NAVEGAÇÃO ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'analise_pronta' not in st.session_state:
    st.session_state.analise_pronta = False

# --- [LOCK] BLOCO DE SEGURANÇA CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    
    [data-testid="stMainBlockContainer"] { 
        padding-top: 0rem !important; 
        padding-bottom: 1rem !important;
        padding-left: 60px !important;
    }

    /* FIX PARA FUNDO ESCURO NOS MENUS */
    div[data-baseweb="select"] > div {
        background-color: #11151a !important;
        color: white !important;
        border: 1px solid #1e293b !important;
    }
    div[role="listbox"] { background-color: #11151a !important; }
    div[data-testid="stSelectbox"] label p { color: white !important; }

    /* [EFEITO EXCLUSIVO] SOMENTE PARA O BOTÃO EXECUTAR (DENTRO DO CONTEÚDO PRINCIPAL) */
    [data-testid="stMainBlockContainer"] div.stButton > button {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: white !important;
        border: none !important;
        font-weight: 800 !important;
        padding: 10px 25px !important;
        transition: 0.4s all !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important;
    }
    [data-testid="stMainBlockContainer"] div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 0 25px rgba(6, 182, 212, 0.5) !important;
        filter: brightness(1.2) !important;
    }

    /* [02] SIDEBAR BOTÕES (RESTAURADOS PARA TRANSPARENTE) */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    [data-testid="stSidebar"] button {
        background-color: transparent !important; /* Força a volta para o transparente */
        color: #94a3b8 !important; 
        border: none !important;
        border-bottom: 1px solid #1a202c !important; 
        border-radius: 0px !important;
        text-align: left !important; 
        width: 100% !important; 
        padding: 18px 25px !important; 
        font-size: 10px !important; 
        text-transform: uppercase !important;
        box-shadow: none !important; /* Remove o brilho da lateral */
    }
    [data-testid="stSidebar"] button:hover { 
        color: #ffffff !important; 
        border-left: 4px solid #6d28d9 !important; 
        background: rgba(26, 36, 45, 0.8) !important; 
    }

    /* [03] NAVBAR SUPERIOR */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; text-decoration: none !important; }
    .nav-items span { color: #ffffff; font-size: 10px !important; text-transform: uppercase; margin-right: 15px; opacity: 0.8; }
    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { color: #ffffff !important; font-size: 10px !important; font-weight: 700 !important; border: 1px solid #ffffff !important; padding: 6px 15px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 7px 20px !important; border-radius: 4px !important; font-weight: 800 !important; font-size: 10px !important; }

    /* [04] CARDS */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- DADOS ---
DADOS_HIEARARQUIA = {
    "BRASIL": {
        "Estadual": {"Paulistão": ["Palmeiras", "São Paulo", "Corinthians", "Santos"], "Carioca": ["Flamengo", "Fluminense", "Vasco"]},
        "Nacional": {"Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo"]}
    }
}

# --- HEADER ---
st.markdown(f"""<div class="betano-header"><div class="header-left"><a href="#" class="logo-link">GESTOR IA</a><div class="nav-items" style="display:inline; margin-left:40px;"><span>Apostas Esportivas</span><span>Apostas ao Vivo</span></div></div><div class="header-right"><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div></div>""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("📊 LOCALIZAR APOSTA"): 
        st.session_state.aba_ativa = "analise"
        st.session_state.analise_pronta = False
    if st.button("🏠 HOME / DASHBOARD"):
        st.session_state.aba_ativa = "home"
    st.button("📅 JOGOS DO DIA")
    st.button("⏰ PRÓXIMOS JOGOS")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- TELA HOME ---
if st.session_state.aba_ativa == "home":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:10px;">HOME / DASHBOARD</div>', unsafe_allow_html=True)
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE</div>', unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    for h in [h1, h2, h3, h4]:
        with h: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">Destaque</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">JOGO EM ANÁLISE</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)

# --- TELA ANÁLISE ---
elif st.session_state.aba_ativa == "analise":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1: pais = st.selectbox("🌎 CATEGORIA", list(DADOS_HIEARARQUIA.keys()))
    with col2: tipo = st.selectbox("📂 TIPO", list(DADOS_HIEARARQUIA[pais].keys()))
    with col3: camp = st.selectbox("🏆 CAMPEONATO", list(DADOS_HIEARARQUIA[pais][tipo].keys()))
    
    t1, t2 = st.columns(2)
    with t1: casa = st.selectbox("🏠 CASA", DADOS_HIEARARQUIA[pais][tipo][camp])
    with t2: fora = st.selectbox("🚀 VISITANTE", [t for t in DADOS_HIEARARQUIA[pais][tipo][camp] if t != casa])

    # BOTÃO EXECUTAR (SÓ ESTE TERÁ O EFEITO)
    if st.button("⚡ EXECUTAR ALGORITIMO"):
        with st.spinner("PROCESSANDO..."):
            time.sleep(1.2)
            st.session_state.analise_pronta = True

    if st.session_state.analise_pronta:
        st.markdown(f'<div style="color:#9d54ff; font-weight:900; font-size:18px; margin-top:20px;">RESULTADO: {casa} vs {fora}</div>', unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        for r in [r1, r2, r3, r4]:
            with r: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">MÉTRICA</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">DADOS IA</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:75%;"></div></div></div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL</div><div>GESTOR IA PRO v42.3</div></div>""", unsafe_allow_html=True)
