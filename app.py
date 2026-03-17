import streamlit as st
import time

# ==============================================================================
# [GIAE KERNEL SHIELD v50.0 - ULTIMATE EFFECT RESTORATION]
# FIX: TICKER ANIMATION | NAVBAR NEON EFFECTS | HEADER ALIGNMENT | INPUT LABELS
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- [01] ESTABILIZAÇÃO DE SESSÃO ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'analise_pronta' not in st.session_state: st.session_state.analise_pronta = False

# --- [02] BLOCO DE SEGURANÇA CSS (JARVIS ULTIMATE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [RESET E FUNDO] */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }

    /* [SIDEBAR LOCK] */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    /* [BOTÕES SIDEBAR] */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; 
        font-size: 10px !important; text-transform: uppercase !important; white-space: nowrap !important;
    }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }

    /* [NAVBAR SUPERIOR - RESTAURAÇÃO DE EFEITOS] */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; 
    }
    .header-left { display: flex; align-items: center; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; margin-right: 35px; transition: 0.3s; }
    .logo-link:hover { text-shadow: 0 0 15px #9d54ff; filter: brightness(1.2); }

    .nav-items { display: flex; gap: 15px; }
    .nav-items span { 
        color: #ffffff; font-size: 8px !important; text-transform: uppercase; 
        opacity: 0.6; white-space: nowrap; transition: 0.3s; cursor: pointer;
    }
    .nav-items span:hover { opacity: 1; color: #9d54ff; text-shadow: 0 0 8px #9d54ff; }

    .header-right { display: flex; align-items: center; gap: 15px; min-width: 320px; justify-content: flex-end; }
    .search-icon { color: #ffffff; font-size: 16px; cursor: pointer; transition: 0.3s; margin-right: 5px; }
    .search-icon:hover { transform: scale(1.2); color: #9d54ff; }

    .registrar-pill { 
        color: #ffffff !important; font-size: 9px !important; font-weight: 700; border: 1px solid #ffffff !important; 
        padding: 6px 18px !important; border-radius: 20px !important; text-decoration: none !important; transition: 0.3s;
    }
    .registrar-pill:hover { background: #ffffff !important; color: #002366 !important; }

    .entrar-grad { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: white !important; padding: 7px 22px !important; border-radius: 4px !important; 
        font-weight: 800; font-size: 9px !important; transition: 0.3s; cursor: pointer;
    }
    .entrar-grad:hover { filter: brightness(1.2); box-shadow: 0 0 15px rgba(109, 40, 217, 0.4); }

    /* [NEWS TICKER ANIMADO - RESTAURAÇÃO TOTAL] */
    .news-ticker-container {
        background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 12px; 
        margin-bottom: 20px; border-radius: 4px; overflow: hidden; position: relative;
    }
    .ticker-content {
        display: inline-block; white-space: nowrap; padding-left: 100%;
        animation: ticker-move 25s linear infinite;
        color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase;
        text-shadow: 0 0 5px rgba(6, 182, 212, 0.5);
    }
    @keyframes ticker-move {
        0% { transform: translate(0, 0); }
        100% { transform: translate(-100%, 0); }
    }

    /* [INPUTS E CARDS] */
    div[data-baseweb="select"] > div { background-color: #11151a !important; color: white !important; border: 1px solid #1e293b !important; }
    label p { color: #94a3b8 !important; font-size: 10px !important; text-transform: uppercase !important; font-weight: 700 !important; }

    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 25px 15px; border-radius: 8px; text-align: center; height: 160px; margin-bottom: 15px; transition: 0.3s; }
    .highlight-card:hover { border-color: #6d28d9; transform: translateY(-3px); }
    .card-label { color: #64748b; font-size: 9px; text-transform: uppercase; margin-bottom: 10px; }
    .card-value { color: white; font-size: 16px; font-weight: 900; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 15px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    /* [BOTÃO EXECUTAR] */
    [data-testid="stMainBlockContainer"] .stButton > button {
        background: linear-gradient(90deg, #6d28d9 0%, #4f46e5 100%) !important;
        color: white !important; border: none !important; font-weight: 900 !important;
        padding: 12px 30px !important; border-radius: 6px !important; text-transform: uppercase;
        animation: btn-glow 2s infinite !important;
    }
    @keyframes btn-glow { 0% { box-shadow: 0 0 5px #6d28d9; } 50% { box-shadow: 0 0 15px #6d28d9; } 100% { box-shadow: 0 0 5px #6d28d9; } }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- [03] HIERARQUIA DE DADOS ---
DADOS_HIEARARQUIA = {
    "BRASIL": {"Nacional": {"Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo", "São Paulo", "Grêmio", "Atlético-MG", "Fluminense", "Internacional", "Corinthians", "Bahia"]}},
    "EUROPA": {"Ligas": {"Premier League": ["Man. City", "Arsenal", "Liverpool", "Aston Villa"]}}
}

# --- [04] CABEÇALHO ---
st.markdown("""
    <div class="betano-header">
        <div class="header-left">
            <div class="logo-link">GESTOR IA</div>
            <div class="nav-items">
                <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Oportunidades IA</span>
                <span>Estatísticas Avançadas</span><span>Probabilidades Reais</span><span>Assertividade IA</span>
            </div>
        </div>
        <div class="header-right">
            <div class="search-icon">🔍</div>
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- [05] SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE"): 
        st.session_state.aba_ativa = "analise"
        st.session_state.analise_pronta = False
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "scanner_live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    st.button("📅 JOGOS DO DIA")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("⚽ APOSTAS POR GOLS")

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- [06] TELA HOME ---
if st.session_state.aba_ativa == "home":
    st.markdown('<div class="news-ticker-container"><div class="ticker-content">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE ● ALERTA: ODDS EM QUEDA ● ANALISANDO TENDÊNCIAS EM TEMPO REAL ●</div></div>', unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: st.markdown('<div class="highlight-card"><div class="card-label">Destaque Live</div><div class="card-value">FLAMENGO x PALMEIRAS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)
    with h2: st.markdown('<div class="highlight-card"><div class="card-label">Sugestão</div><div class="card-value">OVER 2.5 GOLS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:88%;"></div></div></div>', unsafe_allow_html=True)
    with h3: st.markdown('<div class="highlight-card"><div class="card-label">IA Education</div><div class="card-value">GESTÃO 3%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)
    with h4: st.markdown('<div class="highlight-card"><div class="card-label">Tendência</div><div class="card-value">ODDS EM QUEDA</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:75%;"></div></div></div>', unsafe_allow_html=True)
    # ... (Cards 5 a 8 seguem a mesma lógica)

# --- [07] TELA SCANNER ---
elif st.session_state.aba_ativa == "analise":
    c_cat, c_tip, c_cmp = st.columns(3)
    with c_cat: cat = st.selectbox("🌎 CATEGORIA", list(DADOS_HIEARARQUIA.keys()))
    with c_tip: tip = st.selectbox("📂 TIPO", list(DADOS_HIEARARQUIA[cat].keys()))
    with c_cmp: cmp = st.selectbox("🏆 CAMPEONATO", list(DADOS_HIEARARQUIA[cat][tip].keys()))

    t1, t2 = st.columns(2)
    with t1: casa = st.selectbox("🏠 CASA", DADOS_HIEARARQUIA[cat][tip][cmp])
    with t2: fora = st.selectbox("🚀 VISITANTE", [t for t in DADOS_HIEARARQUIA[cat][tip][cmp] if t != casa])

    if st.button("⚡ EXECUTAR ALGORITIMO"):
        st.session_state.analise_pronta = True

    if st.session_state.analise_pronta:
        st.markdown(f'<div style="color:#9d54ff; font-weight:900; font-size:16px; margin: 20px 0; text-transform: uppercase;">RESULTADO ALGORITIMO: {casa} vs {fora}</div>', unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: st.markdown(f'<div class="highlight-card"><div class="card-label">VENCEDOR</div><div class="card-value">{casa}</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:76%;"></div></div></div>', unsafe_allow_html=True)
        with r2: st.markdown(f'<div class="highlight-card"><div class="card-label">MERCADO GOLS</div><div class="card-value">OVER 1.5 REAL</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:85%;"></div></div></div>', unsafe_allow_html=True)
        with r3: st.markdown(f'<div class="highlight-card"><div class="card-label">STAKE RECOMENDADA</div><div style="color:#22c55e; font-size:18px; font-weight:900; margin-top:10px;">R$ 10.00</div></div>', unsafe_allow_html=True)
        with r4: st.markdown(f'<div class="highlight-card" style="border: 1px solid #6d28d9;"><div class="card-label">ESCANTEIOS</div><div class="card-value">MAIS DE 9.5</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:82%;"></div></div></div>', unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | NEON SYSTEM ACTIVE</div><div>GESTOR IA PRO v50.0 | JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
