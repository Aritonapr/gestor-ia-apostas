import streamlit as st
import time
import random

# [VISION UI PROTECTION & ANALYSIS SYSTEM - V9.5]
st.set_page_config(page_title="GESTOR IA - VISION PRO", layout="wide", initial_sidebar_state="expanded")

# --- BANCO DE DADOS INTEGRAL (BLINDADO) ---
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
    "Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Internacional", "Cruzeiro", "Bahia", "Vasco", "Atlético-MG"],
    "Copa do Brasil": ["Flamengo", "Amazonas FC", "Bahia", "Grêmio", "Palmeiras", "Vasco", "Atlético-MG", "São Paulo"],
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Aston Villa", "Chelsea", "Tottenham"],
    "Eliminatórias Copa": ["Brasil", "Argentina", "França", "Inglaterra", "Alemanha", "Espanha", "Portugal"],
    "Bundesliga": ["Bayer Leverkusen", "Bayern Munich", "Stuttgart", "RB Leipzig", "Dortmund"]
}

# --- ESTILIZAÇÃO VISÃO (ESTRUTURA PROTEGIDA) ---
st.markdown("""
    <style>
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    [data-testid="stSidebar"] { background-color: #15191d !important; margin-top: 50px !important; width: 260px !important; border-right: 1px solid #2d3843 !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 6px !important; padding-top: 0px !important; margin-top: -55px !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child { margin-bottom: 35px !important; }

    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    .nav-items { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; }

    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    @keyframes plasma-glow { 0%, 100% { box-shadow: 0 0 5px #f64d23; } 50% { box-shadow: 0 0 15px #f64d23; } }

    div.stButton > button {
        background-color: #f64d23 !important; color: white !important; border-radius: 50px !important; height: 38px !important;
        border: none !important; font-weight: 900 !important; font-size: 11px !important; text-transform: uppercase !important;
        position: relative !important; overflow: hidden !important; animation: plasma-glow 3s infinite ease-in-out !important; width: 100% !important;
    }
    div.stButton > button::after { content: "" !important; position: absolute; top: 0; left: -100%; width: 60px; height: 100%; background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important; animation: laser-scan 2.5s infinite linear !important; }

    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:not(:first-child) button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-left: 2px solid transparent !important;
        text-align: left !important; font-weight: 700 !important; font-size: 10px !important; padding: 8px 15px !important; height: 32px !important;
        width: 100% !important; border-radius: 0px !important;
    }
    
    div[data-baseweb="select"] > div { background-color: #1a242d !important; color: white !important; border: 1px solid #2d3843 !important; }
    .confronto-label { color: #ffffff !important; font-weight: 900 !important; font-size: 16px !important; text-transform: uppercase; letter-spacing: 1px; }
    .white-title { color: white !important; font-weight: 900; font-size: 24px !important; margin-bottom: 20px !important; }
    
    /* ESTILO DOS CARDS DE RESULTADO VISÃO */
    .vision-card {
        background: #15191d; border-left: 4px solid #f64d23; padding: 15px; border-radius: 5px; margin-bottom: 10px;
    }
    .vision-stat-title { color: #f64d23; font-weight: 800; font-size: 12px; text-transform: uppercase; }
    .vision-stat-value { color: #ffffff; font-weight: 900; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown(f"""<div class="betano-header"><div style="width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px;"></div><div class="logo-text">GESTOR IA (VISÃO)</div><div class="nav-items"><span>Estatísticas Avançadas</span><span>Mercado Probabilístico</span></div></div>""", unsafe_allow_html=True)

# --- SIDEBAR ---
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
st.markdown('<div class="white-title">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1: reg_sel = st.selectbox("REGIÃO", list(db_global.keys()))
with col2: cat_sel = st.selectbox("CATEGORIA", list(db_global[reg_sel].keys()))
with col3: comp_sel = st.selectbox("CAMPEONATO", db_global[reg_sel][cat_sel])

st.divider()
st.markdown(f'<div class="confronto-label">Confronto: {comp_sel}</div>', unsafe_allow_html=True)

elenco = times_db.get(comp_sel, ["Equipe A", "Equipe B", "Equipe C"])
t1, t2 = st.columns(2)
with t1: casa = st.selectbox("TIME CASA", elenco)
with t2: fora = st.selectbox("TIME FORA", [t for t in elenco if t != casa] if len(elenco)>1 else elenco)

# ==========================================
# 🚀 MOTOR DE INTELIGÊNCIA "VISÃO"
# ==========================================
c_btn = st.columns([1, 1, 1])
with c_btn[1]:
    if st.button("PROCESSAR ALGORITMO"):
        with st.status("VISÃO: Sincronizando variáveis matemáticas...", expanded=False):
            time.sleep(1.5)
        
        st.markdown(f"### 🛡️ RELATÓRIO DE INTELIGÊNCIA: {casa} vs {fora}")
        
        # 1. Probabilidade Vencedor
        prob_casa = random.randint(30, 85)
        prob_fora = 100 - prob_casa - random.randint(10, 20)
        vencedor = casa if prob_casa > prob_fora else fora

        # Interface de Resultados (Somente Alta Probabilidade)
        res_col1, res_col2 = st.columns(2)

        with res_col1:
            st.markdown(f"""<div class="vision-card"><span class="vision-stat-title">Probabilidade Vencedor</span><br><span class="vision-stat-value">{vencedor} ({max(prob_casa, prob_fora)}%)</span></div>""", unsafe_allow_html=True)
            
            # 2. Gols
            st.markdown(f"""<div class="vision-card"><span class="vision-stat-title">Gols Total / Tempos</span><br><span class="vision-stat-value">Over 2.5 (Prob: 78%)<br>1º Tempo: Sim | 2º Tempo: Sim</span></div>""", unsafe_allow_html=True)
            
            # 3. Cartões
            st.markdown(f"""<div class="vision-card"><span class="vision-stat-title">Cartões (Média 4.5)</span><br><span class="vision-stat-value">HT: 1.5 | FT: 3.0 | Total: 4+</span></div>""", unsafe_allow_html=True)
            
            # 4. Escanteios
            st.markdown(f"""<div class="vision-card"><span class="vision-stat-title">Escanteios</span><br><span class="vision-stat-value">Total: 10.5 | {casa}: 6.5 | {fora}: 4.0</span></div>""", unsafe_allow_html=True)

        with res_col2:
            # 5. Tiros de Meta
            st.markdown(f"""<div class="vision-card"><span class="vision-stat-title">Tiros de Meta</span><br><span class="vision-stat-value">Total: 14.5 | HT: 6.0 | FT: 8.5</span></div>""", unsafe_allow_html=True)
            
            # 6. Chutes no Gol
            st.markdown(f"""<div class="vision-card"><span class="vision-stat-title">Chutes no Gol (SOG)</span><br><span class="vision-stat-value">Total: 9.5 | HT: 4.0 | FT: 5.5</span></div>""", unsafe_allow_html=True)
            
            # 7. Defesas Goleiro
            st.markdown(f"""<div class="vision-card"><span class="vision-stat-title">Defesas Goleiro</span><br><span class="vision-stat-value">Goleiro {casa}: 3.5 | Goleiro {fora}: 4.2</span></div>""", unsafe_allow_html=True)
            
            # INSIGHT DO VISÃO (A MAIS)
            st.warning("⚡ INSIGHT VISÃO: Alta pressão nos primeiros 15 minutos do 2º tempo detectada.")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● VISÃO ON-LINE | ESTRUTURA BLINDADA</div><div>GESTOR IA PRO v9.5 | 18+</div></div>""", unsafe_allow_html=True)
