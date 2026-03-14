import streamlit as st
import time
import random

# ==============================================================================
# [GIAE KERNEL SHIELD v33.0 - PROTOCOLO JARVIS ELITE]
# ESTADO: DESIGN PREMIUM RESTAURADO | SISTEMA DE PASTAS ESTILIZADO
# FIX: NEWS TICKER, HEADER SPACING, GLASS-CARD BUTTONS
# CHAVE DE SEGURANÇA: GIAE-JARVIS-ULTIMATE-RECOVERY
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- [LOCK] CONTROLE DE ESTADO ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'cat_selecionada' not in st.session_state: st.session_state.cat_selecionada = None
if 'liga_selecionada' not in st.session_state: st.session_state.liga_selecionada = None

# --- [LOCK] BLOCO DE SEGURANÇA CSS (NUNCA ALTERAR) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET E BLINDAGEM */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }

    /* [02] SIDEBAR LOCK (320PX) */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    /* [03] NAVBAR SUPERIOR AZUL ROYAL (TRAVADA) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 40px !important; z-index: 999999; 
    }
    .header-left { display: flex; align-items: center; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 22px !important; text-transform: uppercase; text-decoration: none !important; cursor: pointer; margin-right: 50px; }
    .nav-items { display: flex; gap: 20px; }
    .nav-items span { color: #ffffff; font-size: 11px !important; text-transform: uppercase; cursor: pointer; white-space: nowrap; transition: 0.2s; }
    .nav-items span:hover { color: #9d54ff; text-shadow: 0 0 10px #9d54ff; }

    /* HEADER DIREITO */
    .header-right { display: flex; align-items: center; gap: 20px; }
    .search-icon { color: #ffffff !important; cursor: pointer !important; font-size: 18px !important; transition: 0.3s !important; }
    .registrar-pill { color: #ffffff !important; font-size: 10px !important; font-weight: 700 !important; border: 1px solid #ffffff !important; padding: 7px 20px !important; border-radius: 20px !important; cursor: pointer !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 25px !important; border-radius: 4px !important; font-weight: 800 !important; font-size: 11px !important; cursor: pointer !important; }

    /* [04] SIDEBAR BOTÕES */
    [data-testid="stSidebar"] button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; white-space: nowrap !important; }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }

    /* [05] DASHBOARD ELEMENTS (RESTAURADOS) */
    .news-ticker { background: rgba(0, 35, 102, 0.4); border: 1px solid #1e293b; padding: 12px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 20px; border-radius: 4px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 25px; border-radius: 8px; text-align: center; height: 160px; transition: 0.3s; }
    .highlight-card:hover { border-color: #6d28d9; transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.4); }
    .pulse-dot { height: 6px; width: 6px; background-color: #22c55e; border-radius: 50%; display: inline-block; margin-right: 5px; animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }

    /* [06] ESTILIZAÇÃO DAS PASTAS (ELITE FOLDER DESIGN) */
    div.stButton > button {
        background: #11151a !important;
        color: #ffffff !important;
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
        padding: 20px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        transition: 0.3s !important;
        font-size: 11px !important;
    }
    div.stButton > button:hover {
        border-color: #9d54ff !important;
        background: #1a1d23 !important;
        box-shadow: 0 0 15px rgba(157, 84, 255, 0.3) !important;
        color: #9d54ff !important;
    }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- [UI] CABEÇALHO ---
st.markdown(f"""
    <div class="betano-header">
        <div class="header-left">
            <a href="/" target="_self" class="logo-link">GESTOR IA</a>
            <div class="nav-items">
                <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Estatísticas Avançadas</span>
            </div>
        </div>
        <div class="header-right">
            <div class="search-icon">🔍</div><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- [UI] SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("📊 LOCALIZAR APOSTA"): 
        st.session_state.aba_ativa = "analise"
        st.session_state.cat_selecionada = None
        st.session_state.liga_selecionada = None
    st.button("📅 JOGOS DO DIA")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("⚽ APOSTAS POR GOLS")
    st.button("🚩 APOSTAS POR ESCANTEIOS")

st.markdown('<div style="height: 75px;"></div>', unsafe_allow_html=True)

# --- NAVEGAÇÃO CENTRAL ---

if st.session_state.aba_ativa == "home":
    # Dashboard Restaurado
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:10px; letter-spacing:-1px;">HOME / DASHBOARD</div>', unsafe_allow_html=True)
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE ● ALERTA: ODDS EM QUEDA ● DICA: GESTÃO DE BANCA ATUALIZADA</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;"><span class="pulse-dot"></span>Destaque Live</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">FLAMENGO x PALMEIRAS</div><div style="color:#06b6d4; font-size:10px; margin-top:5px;">BRASILEIRÃO - AO VIVO</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Sugestão</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">OVER 2.5 GOLS</div><div style="color:#00cc66; font-size:10px; margin-top:5px;">88% CONFIDÊNCIA</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">IA Education</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">GESTÃO 3%</div><div style="color:#9d54ff; font-size:10px; margin-top:5px;">PROTEÇÃO DE BANCA</div></div>', unsafe_allow_html=True)
    
    st.markdown('<div style="height:15px;"></div>', unsafe_allow_html=True)
    c4, c5, c6 = st.columns(3)
    for i in range(4, 7):
        with eval(f"c{i}"): st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Métrica Jarvis</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">EM ANÁLISE...</div></div>', unsafe_allow_html=True)

elif st.session_state.aba_ativa == "analise":
    
    # Nível 1: Pastas de Categorias
    if st.session_state.cat_selecionada is None:
        st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:20px;">CATEGORIAS DE COMPETIÇÃO</div>', unsafe_allow_html=True)
        
        cats = ["🇧🇷 BR COMPETIÇÕES", "🌎 CLUBES SUL-AM", "🇪🇺 LIGAS NACIONAIS EUROPA", "🏆 COMPETIÇÕES UEFA", "📅 INTERNACIONAIS 25/26"]
        cols = st.columns(3)
        for i, cat in enumerate(cats):
            with cols[i % 3]:
                if st.button(cat, use_container_width=True):
                    st.session_state.cat_selecionada = cat
                    st.rerun()

    # Nível 2: Campeonatos dentro da Pasta
    elif st.session_state.liga_selecionada is None:
        st.markdown(f'<div style="color:white; font-weight:900; font-size:26px; margin-bottom:20px;">{st.session_state.cat_selecionada}</div>', unsafe_allow_html=True)
        
        ligas_dict = {
            "🇧🇷 BR COMPETIÇÕES": ["Série A", "Série B", "Série C", "Série D", "Copa do Brasil", "Estaduais", "Copa Nordeste"],
            "🌎 CLUBES SUL-AM": ["Libertadores", "Sul-Americana"],
            "🇪🇺 LIGAS NACIONAIS EUROPA": ["Premier League", "La Liga", "Serie A", "Bundesliga", "Ligue 1"],
            "🏆 COMPETIÇÕES UEFA": ["Champions League", "Europa League", "Conference League"],
            "📅 INTERNACIONAIS 25/26": ["Copa da Inglaterra", "Eurocopa", "Copa do Rei"]
        }
        
        lista = ligas_dict.get(st.session_state.cat_selecionada, [])
        cols = st.columns(3)
        for i, liga in enumerate(lista):
            with cols[i % 3]:
                if st.button(liga, use_container_width=True):
                    st.session_state.liga_selecionada = liga
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⬅ VOLTAR PARA CATEGORIAS", use_container_width=False):
            st.session_state.cat_selecionada = None
            st.rerun()

    # Nível 3: Seleção de Times
    else:
        st.markdown(f'<div style="color:white; font-weight:900; font-size:26px; margin-bottom:20px;">{st.session_state.liga_selecionada}</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1: mandante = st.selectbox("TIME MANDANTE", ["Escolha...", "Flamengo", "Real Madrid", "Man. City"])
        with col2: visitante = st.selectbox("TIME VISITANTE", ["Escolha...", "Palmeiras", "Barcelona", "Arsenal"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        c_btn1, c_btn2 = st.columns([1, 4])
        with c_btn1: st.button("⚡ EXECUTAR GIAE")
        with c_btn2: 
            if st.button("⬅ TROCAR CAMPEONATO"):
                st.session_state.liga_selecionada = None
                st.rerun()

# --- [LOCK] FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v33.0 | JARVIS PROTECT V33</div></div>""", unsafe_allow_html=True)
