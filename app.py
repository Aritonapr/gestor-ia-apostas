import streamlit as st
import time
import random

# [VISION UI PROTECTION & ANALYSIS SYSTEM - V10.2]
st.set_page_config(page_title="GESTOR IA - VISION PRO", layout="wide", initial_sidebar_state="expanded")

# ==========================================
# 📊 BANCO DE DADOS GLOBAL GIAE (RESTAURADO)
# ==========================================
db_global = {
    "🇧🇷 BR COMPETIÇÕES BRASILEIRAS": {
        "Brasileirão": ["Série A", "Série B", "Série C", "Série D"],
        "Copas Nacionais": ["Copa do Brasil", "Supercopa do Brasil"],
        "Estaduais": ["Paulistão", "Carioca", "Mineiro", "Gaúcho", "Paranaense", "Pernambucano"],
        "Regionais": ["Copa do Nordeste", "Copa Verde"]
    },
    "🇪🇺 EU ELITE EUROPEIA (BIG 5)": {
        "Inglaterra": ["Premier League", "FA Cup", "EFL Cup"],
        "Espanha": ["La Liga", "Copa del Rey"],
        "Alemanha": ["Bundesliga", "DFB-Pokal"],
        "Itália": ["Serie A", "Coppa Italia"],
        "França": ["Ligue 1"]
    },
    "🌎 AMÉRICAS (SUL / CENTRAL)": {
        "Continentais": ["Copa Libertadores", "Copa Sul-Americana"],
        "Nacionais": ["Liga MX (México)", "Liga Profesional (Argentina)", "Primera Div. (Chile)"]
    },
    "🏆 TORNEIOS INTERNACIONAIS": {
        "UEFA": ["Champions League", "Europa League", "Conference League"],
        "FIFA": ["Mundial de Clubes", "Eliminatórias Copa"]
    }
}

times_db = {
    "Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Internacional", "Cruzeiro", "Bahia", "Vasco", "Atlético-MG", "Fluminense", "Corinthians", "Grêmio"],
    "Copa do Brasil": ["Flamengo", "Amazonas FC", "Bahia", "Grêmio", "Palmeiras", "Vasco", "Atlético-MG", "São Paulo"],
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Aston Villa", "Chelsea", "Tottenham", "Newcastle"],
    "La Liga": ["Real Madrid", "Barcelona", "Atlético Madrid", "Girona", "Real Sociedad"],
    "Eliminatórias Copa": ["Brasil", "Argentina", "França", "Inglaterra", "Alemanha", "Espanha", "Portugal", "Uruguai", "Colômbia"]
}

# --- INJEÇÃO DE CÓDIGO FONTE SUPREMO (V10.2 - RESTAURAÇÃO DE CABEÇALHO) ---
st.markdown("""
    <style>
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    /* SIDEBAR BLINDADA */
    [data-testid="stSidebar"] { background-color: #15191d !important; margin-top: 50px !important; width: 260px !important; border-right: 1px solid #2d3843 !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 6px !important; padding-top: 0px !important; margin-top: -55px !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child { margin-bottom: 35px !important; }

    /* NAVBAR DEFINITIVA - TERMOS TÉCNICOS RESTAURADOS */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; margin-right: 25px; }
    .nav-items { display: flex; gap: 15px; flex-grow: 1; color: white; font-size: 9px; font-weight: 700; text-transform: uppercase; align-items: center; }
    
    .header-right { display: flex; align-items: center; gap: 12px; margin-left: auto; }
    .search-icon { color: #94a3b8; font-size: 15px; cursor: pointer; margin-right: 5px; }
    .btn-registrar { border: 1px solid #adb5bd; color: white; padding: 4px 12px; border-radius: 3px; font-size: 9px; font-weight: bold; cursor: pointer; background: transparent; }
    .btn-entrar { background: #00cc66; color: white; padding: 5px 18px; border-radius: 3px; font-weight: bold; border: none; font-size: 9px; cursor: pointer; }

    /* BOTÕES CÁPSULA SLIM COM EFEITO LASER */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    div.stButton > button {
        background-color: #f64d23 !important; color: white !important; border-radius: 50px !important; height: 38px !important;
        border: none !important; font-weight: 900 !important; font-size: 11px !important; text-transform: uppercase !important;
        position: relative !important; overflow: hidden !important; width: 100% !important;
    }
    div.stButton > button::after { content: "" !important; position: absolute; top: 0; left: -100%; width: 60px; height: 100%; background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important; animation: laser-scan 2.5s infinite linear !important; }

    /* BOTÕES SIDEBAR */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:not(:first-child) button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-left: 2px solid transparent !important;
        text-align: left !important; font-weight: 700 !important; font-size: 10px !important; padding: 8px 15px !important; height: 32px !important;
        width: 100% !important; border-radius: 0px !important;
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:not(:first-child) button:hover { color: white !important; border-left: 2px solid #f64d23 !important; background-color: rgba(255,255,255,0.03) !important; }

    /* CARDS DE RESULTADO */
    .vision-card-horiz { background: #15191d; border: 1px solid #2d3843; border-top: 3px solid #f64d23; padding: 12px; border-radius: 6px; text-align: center; }
    .vision-stat-title { color: #f64d23; font-weight: 800; font-size: 10px; text-transform: uppercase; display: block; margin-bottom: 5px; }
    .vision-stat-value { color: #ffffff; font-weight: 900; font-size: 16px; display: block; }
    
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR (UNINDO SEU DESENHO COM A INTELIGÊNCIA DO VISÃO) ---
st.markdown(f"""
    <div class="betano-header">
        <div style="width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px;"></div>
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-items">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span style="color:#f64d23;">Estatísticas Avançadas</span>
            <span style="color:#f64d23;">Mercado Probabilístico</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div class="header-right">
            <span class="search-icon">🔍</span>
            <button class="btn-registrar">REGISTRAR</button>
            <button class="btn-entrar">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (CONFORME SEU RASCUNHO) ---
with st.sidebar:
    st.button("PROCESSAR ALGORITMO")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- CONTEÚDO PRINCIPAL ---
st.markdown('<div style="color:white; font-weight:900; font-size:24px; margin-bottom:20px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1: reg_sel = st.selectbox("REGIÃO", list(db_global.keys()))
with col2: cat_sel = st.selectbox("CATEGORIA", list(db_global[reg_sel].keys()))
with col3: comp_sel = st.selectbox("CAMPEONATO", db_global[reg_sel][cat_sel])

st.divider()
st.markdown(f'<div style="color:white; font-weight:900; font-size:16px; text-transform:uppercase;">Confronto: {comp_sel}</div>', unsafe_allow_html=True)

elenco = times_db.get(comp_sel, ["Aguardando...", "Equipe A", "Equipe B"])
t1, t2 = st.columns(2)
with t1: casa = st.selectbox("TIME CASA", elenco)
with t2: fora = st.selectbox("TIME FORA", [t for t in elenco if t != casa] if len(elenco)>1 else elenco)

if st.button("EXECUTAR ANÁLISE"):
    with st.status("VISÃO: Processando redes neurais estatísticas...", expanded=False):
        time.sleep(1)
    
    st.markdown(f'### RESULTADO ALGORITMO: {casa} vs {fora}')
    r1, r2, r3, r4 = st.columns(4)
    with r1: st.markdown('<div class="vision-card-horiz"><span class="vision-stat-title">Vencedor</span><span class="vision-stat-value">Analisando...</span></div>', unsafe_allow_html=True)
    with r2: st.markdown('<div class="vision-card-horiz"><span class="vision-stat-title">Gols Total</span><span class="vision-stat-value">Calculando...</span></div>', unsafe_allow_html=True)
    with r3: st.markdown('<div class="vision-card-horiz"><span class="vision-stat-title">Cartões</span><span class="vision-stat-value">Simulando...</span></div>', unsafe_allow_html=True)
    with r4: st.markdown('<div class="vision-card-horiz"><span class="vision-stat-title">Escanteios</span><span class="vision-stat-value">Processando...</span></div>', unsafe_allow_html=True)

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● VISÃO ON-LINE | CABEÇALHO RESTAURADO</div><div>GESTOR IA PRO v10.2</div></div>""", unsafe_allow_html=True)
