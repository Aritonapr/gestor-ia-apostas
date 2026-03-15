import streamlit as st
import time
import random

# ==============================================================================
# [GIAE KERNEL SHIELD v48.0 - RESTAURAÇÃO DE IDENTIDADE VISUAL]
# ESTADO: 100% FIEL À IMAGEM DE REFERÊNCIA (6 CARDS HOME | SIDEBAR FLAT)
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

# --- [LOCK] BLOCO DE SEGURANÇA CSS (IDENTIDADE ORIGINAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET E FUNDO TOTAL DARK */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }

    /* [02] NAVBAR SUPERIOR AZUL ROYAL (80PX MARGIN) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 40px !important; z-index: 999999; 
    }
    .logo-link { 
        color: #9d54ff !important; font-weight: 900; font-size: 22px !important; 
        text-transform: uppercase; letter-spacing: 1px; margin-right: 80px !important; 
        text-decoration: none !important; transition: 0.3s;
    }
    .nav-items span { color: #ffffff; font-size: 10px !important; text-transform: uppercase; white-space: nowrap; margin-right: 15px; opacity: 0.7; }
    .nav-items span:hover { color: #9d54ff; opacity: 1; }

    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { color: white; font-size: 10px; font-weight: 700; border: 1px solid white; padding: 6px 18px; border-radius: 20px; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 7px 20px !important; border-radius: 4px !important; font-weight: 800 !important; font-size: 10px !important; }

    /* [03] SIDEBAR ORIGINAL (SEM SCROLL | BOTÕES FLAT) */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; border-radius: 0px !important;
        text-align: left !important; width: 100% !important; padding: 18px 25px !important; 
        font-size: 10px !important; text-transform: uppercase !important; white-space: nowrap !important;
    }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }

    /* [04] EFEITO SUPERNOVA (BOTÃO EXECUTAR ÚNICO) */
    .stButton > button {
        width: auto !important; padding: 10px 30px !important;
        background: linear-gradient(-45deg, #6d28d9, #06b6d4, #6d28d9, #06b6d4) !important;
        background-size: 400% 400% !important;
        animation: supernova-bg 3s ease infinite, supernova-glow 2s infinite !important;
        border: none !important; color: white !important; font-weight: 900 !important;
    }
    @keyframes supernova-bg { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    @keyframes supernova-glow { 0% { box-shadow: 0 0 5px rgba(109, 40, 217, 0.4); } 50% { box-shadow: 0 0 15px rgba(6, 182, 212, 0.6); } 100% { box-shadow: 0 0 5px rgba(109, 40, 217, 0.4); } }

    /* [05] CARDS DASHBOARD (GRID 3x2) */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    /* [06] REMOVER FUNDO BRANCO SELECTS */
    div[data-baseweb="select"] > div { background-color: #11151a !important; border: 1px solid #1e293b !important; color: white !important; }
    div[data-baseweb="select"] * { background-color: transparent !important; color: white !important; }
    
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DADOS ---
DADOS_H = {"BRASIL": {"Estadual": {"Paulistão": ["Palmeiras", "São Paulo", "Corinthians", "Santos"]}, "Nacional": {"Brasileirão Série A": ["Flamengo", "Botafogo", "Palmeiras"]}}}

# --- HEADER (RESTAURADO) ---
st.markdown(f"""<div class="betano-header"><div class="header-left"><div class="logo-link">GESTOR IA</div><div class="nav-items"><span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Apostas Encontradas</span><span>IA Assertividade</span></div></div><div class="header-right"><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div></div>""", unsafe_allow_html=True)

# --- SIDEBAR (IDENTICA À IMAGEM) ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("📊 LOCALIZAR APOSTA"): st.session_state.aba_active = "analise"; st.session_state.analise_pronta = False
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    st.button("⏰ PRÓXIMOS JOGOS")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("✅ APOSTAS POR ODDS")
    st.button("⚽ APOSTAS POR GOLS")
    st.button("🚩 APOSTAS POR ESCANTEIOS")
    st.button("⚖️ ÁRBITRO DA PARTIDA")

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- HOME / DASHBOARD (6 CARDS - GRID 3x2 - FIEL À IMAGEM) ---
if st.session_state.aba_ativa == "home":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:10px;">HOME / DASHBOARD</div>', unsafe_allow_html=True)
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    titulos = ["FLAMENGO x PALMEIRAS", "OVER 2.5 GOLS", "GESTÃO 3%"]
    for i, col in enumerate([c1, c2, c3]):
        with col: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px;">DESTAQUE</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{titulos[i]}</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:88%;"></div></div></div>', unsafe_allow_html=True)
    
    st.markdown('<div style="height:15px;"></div>', unsafe_allow_html=True)
    
    c4, c5, c6 = st.columns(3)
    titulos2 = ["ODDS DESAJUSTADAS", "ALTA PRESSÃO (HT)", "ASSERTIVIDADE 92%"]
    for i, col in enumerate([c4, c5, c6]):
        with col: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px;">MÉTRICA</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{titulos2[i]}</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:92%;"></div></div></div>', unsafe_allow_html=True)

# --- ANÁLISE MÉTRICA (PROXIMO NÍVEL) ---
elif st.session_state.aba_active == "analise":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns(3)
    with col_a: p = st.selectbox("🌎 PAÍS", list(DADOS_H.keys()))
    with col_b: t = st.selectbox("📂 TIPO", list(DADOS_H[p].keys()))
    with col_c: c = st.selectbox("🏆 CAMPEONATO", list(DADOS_H[p][t].keys()))
    
    t1, t2 = st.columns(2)
    with t1: casa = st.selectbox("🏠 CASA", DADOS_H[p][t][c])
    with t2: fora = st.selectbox("🚀 VISITANTE", [x for x in DADOS_H[p][t][c] if x != casa])

    if st.button("⚡ EXECUTAR ALGORITIMO"):
        with st.spinner("PROCESSANDO..."): time.sleep(1.2); st.session_state.analise_pronta = True

    if st.session_state.analise_pronta:
        st.markdown(f'<div style="color:#9d54ff; font-weight:900; font-size:18px; margin: 25px 0 10px 0;">RESULTADO ALGORITIMO: {casa} vs {fora}</div>', unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        for col in [r1, r2, r3, r4]:
            with col: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">MÉTRICA IA</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">DADO REAL</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:75%;"></div></div></div>', unsafe_allow_html=True)
        st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
        r5, r6, r7, r8 = st.columns(4)
        for col in [r5, r6, r7, r8]:
            with col: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">MÉTRICA IA</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">DADO REAL</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:85%;"></div></div></div>', unsafe_allow_html=True)

# --- [LOCK] FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v48.0 | JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
