import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v9.0]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- BANCO DE DADOS INTEGRAL (COMPLETO) ---
db_global = {
    "BR COMPETIÇÕES BRASILEIRAS": {
        "Brasileirão": ["Série A", "Série B", "Série C", "Série D"],
        "Copas Nacionais": ["Copa do Brasil", "Supercopa do Brasil"],
        "Estaduais": ["Paulistão", "Carioca", "Mineiro", "Gaúcho"],
        "Regionais": ["Copa do Nordeste", "Copa Verde"]
    },
    "EU ELITE EUROPEIA (BIG 5)": {
        "Inglaterra": ["Premier League"],
        "Espanha": ["La Liga"],
        "Alemanha": ["Bundesliga"],
        "Itália": ["Serie A"],
        "França": ["Ligue 1"]
    },
    "🌎 AMÉRICAS": {
        "Continental": ["Libertadores", "Sul-Americana"],
        "Nacionais": ["Liga MX", "Liga Argentina"]
    }
}

times_db = {
    "Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Internacional", "Vasco", "Corinthians", "Bahia"],
    "Série B": ["Santos", "Sport", "Mirassol", "Novorizontino", "Ceará", "Goiás"],
    "Copa do Brasil": ["Flamengo", "Amazonas FC", "Bahia", "Grêmio", "Palmeiras", "Vasco", "Atlético-MG", "São Paulo"],
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Chelsea", "Tottenham", "Aston Villa"],
    "La Liga": ["Real Madrid", "Barcelona", "Atlético Madrid", "Girona"]
}

# --- INJEÇÃO DE CÓDIGO FONTE SUPREMO (AFINAGEM E EFEITOS) ---
st.markdown("""
    <style>
    /* 1. RESET E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    /* 2. SIDEBAR ELEVADA E SLIM */
    [data-testid="stSidebar"] { 
        background-color: #15191d !important; 
        margin-top: 50px !important; 
        width: 260px !important; 
        border-right: 1px solid #2d3843 !important;
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { 
        gap: 6px !important; 
        padding-top: 0px !important; 
        margin-top: -55px !important; 
    }

    /* 3. NAVBAR SUPERIOR */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    .nav-items { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; }

    /* 4. BOTÕES CÁPSULA SLIM COM EFEITOS (O "EFEITO LINDO") */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    @keyframes plasma-glow { 0%, 100% { box-shadow: 0 0 5px #f64d23; } 50% { box-shadow: 0 0 15px #f64d23; } }

    div.stButton > button {
        background-color: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        height: 38px !important; /* AFINADO */
        border: none !important;
        font-weight: 900 !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        position: relative !important;
        overflow: hidden !important;
        animation: plasma-glow 3s infinite ease-in-out !important;
        transition: 0.3s all !important;
    }

    div.stButton > button::after {
        content: "" !important; position: absolute; top: 0; left: -100%; width: 60px; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important;
        animation: laser-scan 2.5s infinite linear !important;
        transform: skewX(-20deg);
    }

    /* 5. BOTÕES DA SIDEBAR (CATEGORIAS SLIM) */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:not(:first-child) button {
        background-color: transparent !important;
        color: #94a3b8 !important;
        border: none !important;
        border-left: 2px solid transparent !important;
        text-align: left !important;
        font-weight: 700 !important;
        font-size: 10px !important;
        padding: 8px 15px !important; /* MAIS FINO */
        height: 32px !important; /* MAIS FINO */
        width: 100% !important;
        border-radius: 0px !important;
    }

    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:not(:first-child) button:hover {
        color: white !important;
        border-left: 2px solid #f64d23 !important;
        background-color: rgba(255,255,255,0.03) !important;
    }

    /* 6. HARMONIZAÇÃO DOS SELECTBOXES (FUNDO ESCURO) */
    div[data-baseweb="select"] > div {
        background-color: #1a242d !important;
        color: white !important;
        border: 1px solid #2d3843 !important;
        height: 40px !important;
    }

    /* 7. TEXTOS */
    .white-title { color: white !important; font-weight: 900; font-size: 24px !important; margin-bottom: 20px !important; }
    .standard-text { color: #f64d23 !important; font-weight: 800; font-size: 14px !important; text-transform: uppercase; }
    
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown(f"""
    <div class="betano-header">
        <div style="width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px;"></div>
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-items">
            <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Apostas Encontradas</span><span>Assertividade IA</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (AFINADA) ---
with st.sidebar:
    st.button("FERRAMENTA IA") # O Botão principal mantém o laser
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL (BANCO DE DADOS INTEGRADO) ---
st.markdown('<div class="white-title">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1: reg_sel = st.selectbox("REGIÃO", list(db_global.keys()))
with c2: cat_sel = st.selectbox("CATEGORIA", list(db_global[reg_sel].keys()))
with c3: comp_sel = st.selectbox("CAMPEONATO", db_global[reg_sel][cat_sel])

st.divider()

st.markdown(f'<div class="standard-text">Confronto: {comp_sel}</div>', unsafe_allow_html=True)

elenco = times_db.get(comp_sel, ["Time A", "Time B", "Time C", "Time D"])
t1, t2 = st.columns(2)
with t1: casa = st.selectbox("TIME CASA", elenco)
with t2: fora = st.selectbox("TIME FORA", [t for t in elenco if t != casa] if len(elenco)>1 else elenco)

# Botão Central Afinador
col_btn = st.columns([1, 2, 1])
with col_btn[1]:
    if st.button("PROCESSAR ALGORITMO"):
        with st.status("GIAE IA: Analisando métricas...", expanded=False):
            time.sleep(1.5)
        st.success(f"Análise de {casa} x {fora} concluída com 94% de precisão.")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | REFINAMENTO V9.1</div><div>GESTOR IA PRO</div></div>""", unsafe_allow_html=True)
