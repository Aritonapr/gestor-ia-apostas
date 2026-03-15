import streamlit as st
import time
import random

# ==============================================================================
# [GIAE KERNEL SHIELD v49.0 - PROTOCOLO JARVIS ELITE]
# ESTADO: SIMETRIA TOTAL | EFEITO EXCLUSIVO NO BOTÃO CENTRAL | DARK MODE ABSOLUTO
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

    /* [01] RESET E FUNDO TOTAL DARK */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }

    /* [02] NAVBAR SUPERIOR AZUL ROYAL (EFEITOS RESTAURADOS) */
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
    .logo-link:hover { text-shadow: 0 0 15px #9d54ff; filter: brightness(1.2); }
    .nav-items span { color: #ffffff; font-size: 10px !important; text-transform: uppercase; cursor: pointer; white-space: nowrap; transition: 0.2s; opacity: 0.8; }
    .nav-items span:hover { color: #9d54ff; opacity: 1; }

    .header-right { display: flex; align-items: center; gap: 20px; }
    .registrar-pill { color: white; font-size: 10px; font-weight: 700; border: 1px solid white; padding: 6px 18px; border-radius: 20px; transition: 0.3s; }
    .registrar-pill:hover { background: white; color: #002366; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 7px 25px !important; border-radius: 4px !important; font-weight: 800 !important; font-size: 10px !important; transition: 0.3s; }
    .entrar-grad:hover { filter: brightness(1.2); box-shadow: 0 0 15px rgba(109, 40, 217, 0.4); }

    /* [03] SIDEBAR LOCK (320PX) - SEM SCROLL E BOTÕES FLAT */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; border-radius: 0px !important;
        text-align: left !important; width: 100% !important; padding: 18px 25px !important; 
        font-size: 10px !important; text-transform: uppercase !important; white-space: nowrap !important;
    }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }

    /* [04] EFEITO SUPERNOVA EXCLUSIVO - BOTÃO EXECUTAR ALGORITIMO */
    .stButton > button {
        width: auto !important; padding: 12px 35px !important;
        background: linear-gradient(-45deg, #6d28d9, #06b6d4, #6d28d9, #06b6d4) !important;
        background-size: 400% 400% !important;
        animation: grad-anim 3s ease infinite, pulse-glow 2s infinite !important;
        border: none !important; color: white !important; font-weight: 900 !important; border-radius: 6px !important;
        transition: 0.3s !important;
    }
    @keyframes grad-anim { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    @keyframes pulse-glow { 0% { box-shadow: 0 0 5px rgba(109, 40, 217, 0.4); } 50% { box-shadow: 0 0 15px rgba(6, 182, 212, 0.6); } 100% { box-shadow: 0 0 5px rgba(109, 40, 217, 0.4); } }

    /* [05] REMOÇÃO DE FUNDO BRANCO EM SELECTS */
    div[data-baseweb="select"] > div { background-color: #11151a !important; border: 1px solid #1e293b !important; color: white !important; }
    div[data-baseweb="select"] * { background-color: transparent !important; color: white !important; }
    div[role="listbox"] { background-color: #11151a !important; border: 1px solid #6d28d9 !important; }

    /* [06] CARDS DASHBOARD E RESULTADOS */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; transition: 0.3s; }
    .highlight-card:hover { border-color: #6d28d9; transform: translateY(-3px); }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DADOS HIERÁRQUICA ---
DADOS_H = {
    "BRASIL": {
        "Estadual": {"Paulistão": ["Palmeiras", "São Paulo", "Corinthians", "Santos"], "Carioca": ["Flamengo", "Fluminense", "Vasco"]},
        "Nacional": {"Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo"]}
    },
    "INGLATERRA": {"Nacional": {"Premier League": ["Man City", "Arsenal", "Liverpool", "Chelsea"]}}
}

# --- HEADER (RESTAURADO) ---
st.markdown(f"""
    <div class="betano-header">
        <div class="header-left">
            <div class="logo-link">GESTOR IA</div>
            <div class="nav-items">
                <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Apostas Encontradas</span><span>Estatísticas Avançadas</span>
            </div>
        </div>
        <div class="header-right">
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (MANTIDA ORIGINAL) ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("📊 LOCALIZAR APOSTA"): 
        st.session_state.aba_ativa = "analise"
        st.session_state.analise_pronta = False
    st.button("📅 JOGOS DO DIA")
    st.button("⏰ PRÓXIMOS JOGOS")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("📈 APOSTAS POR ODDS")
    st.button("⚽ APOSTAS POR GOLS")
    st.button("🚩 APOSTAS POR ESCANTEIOS")

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- HOME / DASHBOARD (8 CARDS) ---
if st.session_state.aba_ativa == "home":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:10px;">HOME / DASHBOARD</div>', unsafe_allow_html=True)
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE</div>', unsafe_allow_html=True)
    
    h1, h2, h3, h4 = st.columns(4)
    titles = ["FLAMENGO x PALMEIRAS", "MAN CITY x ARSENAL", "OVER 2.5 GOLS", "STAKE 3% BANCA"]
    for i, col in enumerate([h1, h2, h3, h4]):
        with col: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px;">DESTAQUE</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{titles[i]}</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:85%;"></div></div></div>', unsafe_allow_html=True)
    
    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
    h5, h6, h7, h8 = st.columns(4)
    titles2 = ["OVER 9.5 CANTOS", "ODDS DESAJUSTADAS", "ASSERTIVIDADE 94%", "JARVIS SUPREME"]
    for i, col in enumerate([h5, h6, h7, h8]):
        with col: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px;">MÉTRICA</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{titles2[i]}</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:92%;"></div></div></div>', unsafe_allow_html=True)

# --- ANÁLISE MÉTRICA (PROXIMO NÍVEL) ---
elif st.session_state.aba_ativa == "analise":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    
    col_p, col_t, col_c = st.columns(3)
    with col_p: p = st.selectbox("🌎 PAÍS", list(DADOS_H.keys()))
    with col_t: t = st.selectbox("📂 TIPO", list(DADOS_H[p].keys()))
    with col_c: c = st.selectbox("🏆 CAMPEONATO", list(DADOS_H[p][t].keys()))
    
    tm1, tm2 = st.columns(2)
    with tm1: casa = st.selectbox("🏠 CASA", DADOS_H[p][t][c])
    with tm2: fora = st.selectbox("🚀 VISITANTE", [x for x in DADOS_H[p][t][c] if x != casa])

    # BOTÃO EXECUTAR (RENOMEADO E AJUSTADO)
    if st.button("⚡ EXECUTAR ALGORITIMO"):
        with st.spinner("PROCESSANDO MÉTRICAS..."):
            time.sleep(1.2)
            st.session_state.analise_pronta = True

    if st.session_state.analise_pronta:
        st.markdown(f'<div style="color:#9d54ff; font-weight:900; font-size:18px; margin: 25px 0 10px 0; text-transform: uppercase;">RESULTADO ALGORITIMO: {casa} vs {fora}</div>', unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        met1 = ["VENCEDOR", "MERCADO GOLS", "CARTÕES", "ESCANTEIOS"]
        val1 = [f"{casa}", "OVER 1.5 REAL", "MAIS DE 4.5", "MAIS DE 9.5"]
        for i, col in enumerate([r1, r2, r3, r4]):
            with col: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px;">{met1[i]}</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">{val1[i]}</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:78%;"></div></div></div>', unsafe_allow_html=True)
        st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
        r5, r6, r7, r8 = st.columns(4)
        met2 = ["TIROS DE META", "CHUTES AO GOL", "DEFESAS", "ÍNDICE PRESSÃO"]
        val2 = ["14-16 TOTAIS", "CASA +5.5", "VISITANTE 4+", "GOL MADURO 68%"]
        for i, col in enumerate([r5, r6, r7, r8]):
            with col: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px;">{met2[i]}</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">{val2[i]}</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:82%;"></div></div></div>', unsafe_allow_html=True)

# --- [LOCK] FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v49.0 | JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
