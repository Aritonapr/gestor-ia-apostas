import streamlit as st
import time
import random

# [VISION UI PROTECTION & ANALYSIS SYSTEM - V11.0]
st.set_page_config(page_title="GESTOR IA - VISION PRO", layout="wide", initial_sidebar_state="expanded")

# ==========================================
# 📊 BANCO DE DADOS INTEGRAL (PROTEGIDO)
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
    "Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Internacional", "Vasco", "Atlético-MG", "Fluminense", "Corinthians", "Grêmio", "Cruzeiro"],
    "Copa do Brasil": ["Flamengo", "Amazonas FC", "Bahia", "Grêmio", "Palmeiras", "Vasco", "Atlético-MG", "São Paulo"],
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Chelsea", "Tottenham"],
    "Eliminatórias Copa": ["Brasil", "Argentina", "França", "Inglaterra", "Alemanha", "Espanha", "Portugal"]
}

# --- INJEÇÃO DE CÓDIGO FONTE SUPREMO (V11.0 - BLINDAGEM TOTAL) ---
st.markdown("""
    <style>
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    /* SIDEBAR MILIMÉTRICA */
    [data-testid="stSidebar"] { background-color: #15191d !important; margin-top: 50px !important; width: 260px !important; border-right: 1px solid #2d3843 !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 6px !important; padding-top: 0px !important; margin-top: -55px !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child { margin-bottom: 35px !important; }

    /* NAVBAR BETANO STYLE (LARGURA AMPLIADA) */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 25px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 22px; font-style: italic; margin-right: 40px; }
    .nav-items { display: flex; gap: 28px; flex-grow: 1; color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; align-items: center; }
    
    .header-right { display: flex; align-items: center; gap: 15px; margin-left: auto; }
    .btn-registrar { border: 1px solid #adb5bd; color: white; padding: 5px 15px; border-radius: 3px; font-size: 11px; font-weight: bold; background: transparent; cursor: pointer; }
    .btn-entrar { background: #00cc66; color: white; padding: 6px 20px; border-radius: 3px; font-weight: bold; border: none; font-size: 11px; cursor: pointer; }

    /* PINTURA DOS CAMPOS DE SELEÇÃO (FIM DO BRANCO) */
    div[data-baseweb="select"] > div { background-color: #1a242d !important; color: white !important; border: 1px solid #2d3843 !important; }
    div[data-baseweb="select"] * { color: white !important; }
    
    /* BOTÕES LARANJAS SLIM COM LASER */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    div.stButton > button {
        background-color: #f64d23 !important; color: white !important; border-radius: 50px !important; height: 38px !important;
        border: none !important; font-weight: 900 !important; font-size: 11px !important; text-transform: uppercase !important;
        position: relative !important; overflow: hidden !important; width: 100% !important;
    }
    div.stButton > button::after { content: "" !important; position: absolute; top: 0; left: -100%; width: 60px; height: 100%; background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important; animation: laser-scan 2.5s infinite linear !important; }

    /* CARDS DE RESULTADO (2 LINHAS X 4 COLUNAS) */
    .vision-card-horiz { background: #15191d; border: 1px solid #2d3843; border-top: 3px solid #f64d23; padding: 12px; border-radius: 6px; text-align: center; margin-bottom: 10px; }
    .vision-stat-title { color: #f64d23; font-weight: 800; font-size: 10px; text-transform: uppercase; display: block; margin-bottom: 5px; }
    .vision-stat-value { color: #ffffff; font-weight: 900; font-size: 15px; display: block; }
    .vision-stat-sub { color: #94a3b8; font-size: 9px; font-weight: 600; display: block; margin-top: 4px; }
    
    .result-title { color: #ffffff; font-weight: 900; font-size: 22px; text-transform: uppercase; border-left: 5px solid #f64d23; padding-left: 15px; margin: 30px 0 15px 0; }
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR (ESTILO BETANO INTEGRAL) ---
st.markdown(f"""
    <div class="betano-header">
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-items">
            <span>Apostas Esportivas</span><span>Apostas ao Vivo</span>
            <span>Cassino</span><span>Cassino ao Vivo</span>
            <span>Estatísticas Avançadas</span><span>Mercado Probabilístico</span>
            <span>Apostas Encontradas</span><span>Assertividade IA</span>
        </div>
        <div class="header-right">
            <span style="color:#94a3b8; font-size:18px; cursor:pointer;">🔍</span>
            <button class="btn-registrar">REGISTRAR</button>
            <button class="btn-entrar">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (RENOMEADA) ---
with st.sidebar:
    st.button("FERRAMENTA IA")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- CONTEÚDO PRINCIPAL ---
st.markdown('<div style="color:white; font-weight:900; font-size:24px; margin-bottom:20px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1: reg_sel = st.selectbox("REGIÃO", list(db_global.keys()))
with c2: cat_sel = st.selectbox("CATEGORIA", list(db_global[reg_sel].keys()))
with c3: comp_sel = st.selectbox("CAMPEONATO", db_global[reg_sel][cat_sel])

st.divider()
st.markdown(f'<div style="color:white; font-weight:900; font-size:16px; text-transform:uppercase;">Confronto: {comp_sel}</div>', unsafe_allow_html=True)

elenco = times_db.get(comp_sel, ["Aguardando...", "Equipe A", "Equipe B"])
t1, t2 = st.columns(2)
with t1: casa = st.selectbox("TIME CASA", elenco)
with t2: fora = st.selectbox("TIME FORA", [t for t in elenco if t != casa] if len(elenco)>1 else elenco)

# --- BOTÃO DE DISPARO ---
btn_col, _ = st.columns([1, 2])
with btn_col:
    if st.button("EXECUTAR ALGORITMO"):
        with st.status("VISÃO: Sincronizando 8 camadas de dados...", expanded=False):
            time.sleep(1.2)
        
        st.markdown(f'<div class="result-title">RESULTADO ALGORITMO: {casa} vs {fora}</div>', unsafe_allow_html=True)
        
        # LINHA 1 DE 4 RESULTADOS
        r1_1, r1_2, r1_3, r1_4 = st.columns(4)
        with r1_1: st.markdown(f'<div class="vision-card-horiz"><span class="vision-stat-title">Vencedor Prob.</span><span class="vision-stat-value">{casa}</span><span class="vision-stat-sub">Confiança: 72%</span></div>', unsafe_allow_html=True)
        with r1_2: st.markdown(f'<div class="vision-card-horiz"><span class="vision-stat-title">Gols Total / Tempos</span><span class="vision-stat-value">Over 2.5 Gols</span><span class="vision-stat-sub">1ºT: Sim | 2ºT: Sim</span></div>', unsafe_allow_html=True)
        with r1_3: st.markdown(f'<div class="vision-card-horiz"><span class="vision-stat-title">Cartões (Total/Tempos)</span><span class="vision-stat-value">Over 4.5</span><span class="vision-stat-sub">HT: 1.5 | FT: 3.0</span></div>', unsafe_allow_html=True)
        with r1_4: st.markdown(f'<div class="vision-card-horiz"><span class="vision-stat-title">Escanteios</span><span class="vision-stat-value">10.5 Total</span><span class="vision-stat-sub">{casa}: 6 | {fora}: 4</span></div>', unsafe_allow_html=True)

        # LINHA 2 DE 4 RESULTADOS (RESTAURADOS)
        r2_1, r2_2, r2_3, r2_4 = st.columns(4)
        with r2_1: st.markdown(f'<div class="vision-card-horiz"><span class="vision-stat-title">Tiros de Meta</span><span class="vision-stat-value">14.0 Total</span><span class="vision-stat-sub">HT: 6 | FT: 8</span></div>', unsafe_allow_html=True)
        with r2_2: st.markdown(f'<div class="vision-card-horiz"><span class="vision-stat-title">Chutes no Gol (SOG)</span><span class="vision-stat-value">9.5 Total</span><span class="vision-stat-sub">HT: 4 | FT: 5.5</span></div>', unsafe_allow_html=True)
        with r2_3: st.markdown(f'<div class="vision-card-horiz"><span class="vision-stat-title">Defesas Goleiro</span><span class="vision-stat-value">7.2 Total</span><span class="vision-stat-sub">{casa}: 3 | {fora}: 4</span></div>', unsafe_allow_html=True)
        with r2_4: st.markdown(f'<div class="vision-card-horiz" style="border-top:3px solid #00cc66;"><span class="vision-stat-title" style="color:#00cc66;">V-Insight</span><span class="vision-stat-value" style="color:#00cc66;">Alta Assertividade</span><span class="vision-stat-sub">Mercado de Cantos</span></div>', unsafe_allow_html=True)

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● VISÃO ON-LINE | 8 MÉTRICAS RESTAURADAS</div><div>GESTOR IA PRO v11.0</div></div>""", unsafe_allow_html=True)
