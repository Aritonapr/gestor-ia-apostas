import streamlit as st
import time

# ==============================================================================
# [GIAE KERNEL SHIELD v52.0 - DEFINITIVE DATA RESTORATION]
# FIX: FULL DATA HIERARCHY | 8-CARDS SYNC | NEON INTERFACE | JARVIS PROTECT
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- [01] ESTABILIZAÇÃO DE SESSÃO ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'analise_pronta' not in st.session_state: st.session_state.analise_pronta = False

# --- [02] BLOCO DE SEGURANÇA CSS (MASTER JARVIS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }

    /* SIDEBAR LOCK */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    /* BOTÕES SIDEBAR UMA LINHA */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; 
        font-size: 10px !important; text-transform: uppercase !important; white-space: nowrap !important;
    }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }

    /* NAVBAR SUPERIOR NEON */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; margin-right: 40px; text-decoration: none !important; }
    .nav-items { display: flex; gap: 15px; }
    .nav-items span { color: #ffffff; font-size: 9px !important; text-transform: uppercase; opacity: 0.7; transition: 0.3s; cursor: pointer; }
    .nav-items span:hover { color: #9d54ff; opacity: 1; text-shadow: 0 0 10px #9d54ff; }

    .header-right { display: flex; align-items: center; gap: 15px; min-width: 350px; justify-content: flex-end; }
    .search-icon { color: #ffffff; font-size: 16px; cursor: pointer; transition: 0.3s; margin-right: 10px; }
    .registrar-pill { color: #ffffff !important; font-size: 10px !important; font-weight: 700; border: 1px solid #ffffff !important; padding: 6px 18px !important; border-radius: 20px !important; text-decoration: none !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 7px 22px !important; border-radius: 4px !important; font-weight: 800; font-size: 10px !important; transition: 0.3s; }

    /* TICKER MARQUEE */
    .ticker-wrap { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; border-radius: 4px; overflow: hidden; white-space: nowrap; padding: 12px; margin-bottom: 20px; }
    .ticker-move { display: inline-block; animation: marquee 30s linear infinite; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; }
    @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

    /* CARDS */
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 25px 15px; border-radius: 8px; text-align: center; height: 160px; margin-bottom: 15px; transition: 0.3s; }
    .card-label { color: #64748b; font-size: 9px; text-transform: uppercase; margin-bottom: 10px; font-weight: 700; }
    .card-value { color: white; font-size: 15px; font-weight: 900; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 15px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    /* SELECTBOX DARK */
    div[data-baseweb="select"] > div { background-color: #11151a !important; color: white !important; border: 1px solid #1e293b !important; }
    label p { color: #94a3b8 !important; font-size: 10px !important; text-transform: uppercase !important; font-weight: 700 !important; }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- [03] A BASE DE DADOS COMPLETA (DEFINITIVA) ---
DADOS_HIEARARQUIA = {
    "BRASIL": {
        "Nacional": {
            "Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo", "São Paulo", "Grêmio", "Atlético-MG", "Fluminense", "Internacional", "Corinthians", "Bahia", "Cruzeiro", "Vasco", "Athletico-PR", "Fortaleza", "Cuiabá", "Criciúma", "Juventude", "Vitória", "Bragantino", "Atlético-GO"],
            "Brasileirão Série B": ["Santos", "Sport", "Coritiba", "Goiás", "Ceará", "Novorizontino", "Vila Nova", "Amazonas", "Operário", "América-MG"],
            "Brasileirão Série C": ["Náutico", "Figueirense", "Remo", "CSA", "Volta Redonda", "Sampaio Corrêa", "ABC", "Botafogo-PB"],
            "Brasileirão Série D": ["Santa Cruz", "Inter de Limeira", "Anápolis", "Maringá", "Brasil de Pelotas", "Retrô", "Iguatu"]
        },
        "Copas": {
            "Copa do Brasil": ["Vasco", "Flamengo", "São Paulo", "Palmeiras", "Juventude", "Athletico-PR", "Bahia", "Corinthians"],
            "Copa do Nordeste": ["Fortaleza", "Bahia", "Ceará", "Sport", "Vitória", "CRB", "Sampaio Corrêa"]
        }
    },
    "EUROPA": {
        "Internacional": {
            "UEFA Champions League": ["Real Madrid", "Man. City", "Bayern Munique", "Arsenal", "Barcelona", "Inter de Milão", "PSG", "Dortmund", "Liverpool", "Juventus", "Bayer Leverkusen", "AC Milan"],
            "UEFA Europa League": ["AS Roma", "Benfica", "Ajax", "Porto", "Tottenham", "Man. United"]
        },
        "Ligas Nacionais": {
            "Premier League": ["Man. City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Newcastle", "West Ham"],
            "La Liga": ["Real Madrid", "Barcelona", "Girona", "Atlético Madrid", "Real Sociedad", "Athletic Bilbao"],
            "Bundesliga": ["Bayer Leverkusen", "Bayern Munique", "Stuttgart", "Dortmund", "RB Leipzig"],
            "Serie A (Itália)": ["Inter de Milão", "AC Milan", "Juventus", "Atalanta", "AS Roma", "Napoli"]
        }
    },
    "AMÉRICA DO SUL": {
        "Continental": {
            "Libertadores": ["Flamengo", "Palmeiras", "River Plate", "Boca Juniors", "Fluminense", "Atlético-MG", "Peñarol", "Colo-Colo"],
            "Sul-Americana": ["Internacional", "Cruzeiro", "Corinthians", "Racing Club", "Lanús", "Fortaleza"]
        }
    },
    "MERCADOS EMERGENTES": {
        "Arábia Saudita": {"Saudi Pro League": ["Al-Hilal", "Al-Nassr", "Al-Ittihad", "Al-Ahli", "Al-Ettifaq"]},
        "Estados Unidos": {"MLS": ["Inter Miami", "LA Galaxy", "Columbus Crew", "LAFC", "Seattle Sounders"]}
    }
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

# --- [06] TELA HOME (8 CARDS) ---
if st.session_state.aba_ativa == "home":
    st.markdown('<div class="ticker-wrap"><div class="ticker-move">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE ● ALERTA: ODDS EM QUEDA ● ANALISANDO TENDÊNCIAS GLOBAIS ●</div></div>', unsafe_allow_html=True)
    
    h1, h2, h3, h4 = st.columns(4)
    with h1: st.markdown('<div class="highlight-card"><div class="card-label">Destaque Live</div><div class="card-value">FLAMENGO x PALMEIRAS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)
    with h2: st.markdown('<div class="highlight-card"><div class="card-label">Sugestão</div><div class="card-value">OVER 2.5 GOLS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:88%;"></div></div></div>', unsafe_allow_html=True)
    with h3: st.markdown('<div class="highlight-card"><div class="card-label">IA Education</div><div class="card-value">GESTÃO 3%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)
    with h4: st.markdown('<div class="highlight-card"><div class="card-label">Tendência</div><div class="card-value">ODDS EM QUEDA</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:75%;"></div></div></div>', unsafe_allow_html=True)

    h5, h6, h7, h8 = st.columns(4)
    with h5: st.markdown('<div class="highlight-card"><div class="card-label">Scanner</div><div class="card-value">ALTA PRESSÃO (HT)</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:60%;"></div></div></div>', unsafe_allow_html=True)
    with h6: st.markdown('<div class="highlight-card"><div class="card-label">Performance</div><div class="card-value">ASSERTIVIDADE 92%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:92%;"></div></div></div>', unsafe_allow_html=True)
    with h7: st.markdown('<div class="highlight-card" style="border: 1px solid #6d28d9;"><div class="card-label">Volume</div><div class="card-value">MERCADO EM ALTA</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:80%;"></div></div></div>', unsafe_allow_html=True)
    with h8: st.markdown('<div class="highlight-card"><div class="card-label">Proteção</div><div class="card-value">JARVIS SUPREME</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)

# --- [07] TELA SCANNER (MATEMÁTICA INTEGRADA) ---
elif st.session_state.aba_ativa == "analise":
    # 3 COLUNAS DE SELEÇÃO HIERÁRQUICA
    c_cat, c_tip, c_cmp = st.columns(3)
    with c_cat: cat = st.selectbox("🌎 CATEGORIA", list(DADOS_HIEARARQUIA.keys()))
    with c_tip: tip = st.selectbox("📂 TIPO", list(DADOS_HIEARARQUIA[cat].keys()))
    with c_cmp: cmp = st.selectbox("🏆 CAMPEONATO", list(DADOS_HIEARARQUIA[cat][tip].keys()))

    t1, t2 = st.columns(2)
    lista_times = DADOS_HIEARARQUIA[cat][tip][cmp]
    with t1: casa = st.selectbox("🏠 CASA", lista_times)
    with t2: fora = st.selectbox("🚀 VISITANTE", [t for t in lista_times if t != casa])

    if st.button("⚡ EXECUTAR ALGORITIMO"):
        st.session_state.analise_pronta = True

    if st.session_state.analise_pronta:
        st.markdown(f'<div style="color:#9d54ff; font-weight:900; font-size:16px; margin: 20px 0; text-transform: uppercase;">RESULTADO: {casa} vs {fora}</div>', unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: st.markdown(f'<div class="highlight-card"><div class="card-label">VENCEDOR</div><div class="card-value">{casa}</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:76%;"></div></div></div>', unsafe_allow_html=True)
        with r2: st.markdown(f'<div class="highlight-card"><div class="card-label">MERCADO GOLS</div><div class="card-value">OVER 1.5 REAL</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:85%;"></div></div></div>', unsafe_allow_html=True)
        with r3: st.markdown(f'<div class="highlight-card"><div class="card-label">STAKE</div><div style="color:#22c55e; font-size:18px; font-weight:900; margin-top:10px;">R$ 10.00</div></div>', unsafe_allow_html=True)
        with r4: st.markdown(f'<div class="highlight-card" style="border: 1px solid #6d28d9;"><div class="card-label">ESCANTEIOS</div><div class="card-value">MAIS DE 9.5</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:82%;"></div></div></div>', unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | FULL DATA UNLOCKED</div><div>GESTOR IA PRO v52.0 | JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
