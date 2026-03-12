import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v9.0]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- BANCO DE DADOS INTEGRAL (PROTEGIDO) ---
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
    }
}

times_db = {
    "Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Vasco", "Corinthians", "Bahia", "Internacional", "Cruzeiro"],
    "Copa do Brasil": ["Flamengo", "Amazonas FC", "Bahia", "Grêmio", "Palmeiras", "Vasco", "Atlético-MG", "São Paulo"],
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Chelsea", "Tottenham"]
}

# --- INJEÇÃO DE CÓDIGO FONTE SUPREMO (REFINAMENTO FINAL V9.2) ---
st.markdown("""
    <style>
    /* 1. RESET E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    /* 2. SIDEBAR ELEVADA E DISTANCIAMENTO */
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

    /* DISTÂNCIA ENTRE FERRAMENTA IA E PRÓXIMOS JOGOS */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child {
        margin-bottom: 35px !important; /* Espaço solicitado pelo Comandante */
    }

    /* 3. NAVBAR SUPERIOR */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    .nav-items { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; }

    /* 4. BOTÕES CÁPSULA SLIM COM EFEITOS */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    @keyframes plasma-glow { 0%, 100% { box-shadow: 0 0 5px #f64d23; } 50% { box-shadow: 0 0 15px #f64d23; } }

    div.stButton > button {
        background-color: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        height: 38px !important;
        border: none !important;
        font-weight: 900 !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        position: relative !important;
        overflow: hidden !important;
        animation: plasma-glow 3s infinite ease-in-out !important;
        width: 100% !important;
    }

    div.stButton > button::after {
        content: "" !important; position: absolute; top: 0; left: -100%; width: 60px; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important;
        animation: laser-scan 2.5s infinite linear !important;
    }

    /* 5. BOTÕES DA SIDEBAR (CATEGORIAS) */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:not(:first-child) button {
        background-color: transparent !important;
        color: #94a3b8 !important;
        border: none !important;
        border-left: 2px solid transparent !important;
        text-align: left !important;
        font-weight: 700 !important;
        font-size: 10px !important;
        padding: 8px 15px !important;
        height: 32px !important;
        width: 100% !important;
        border-radius: 0px !important;
    }

    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:not(:first-child) button:hover {
        color: white !important;
        border-left: 2px solid #f64d23 !important;
        background-color: rgba(255,255,255,0.03) !important;
    }

    /* 6. SELECTBOXES HARMONIZADOS */
    div[data-baseweb="select"] > div {
        background-color: #1a242d !important;
        color: white !important;
        border: 1px solid #2d3843 !important;
    }

    /* 7. TEXTO DO CONFRONTO (COR BRANCA SOLICITADA) */
    .confronto-label { 
        color: #ffffff !important; /* MUDANÇA PARA BRANCO */
        font-weight: 900 !important; 
        font-size: 16px !important; 
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .white-title { color: white !important; font-weight: 900; font-size: 24px !important; margin-bottom: 20px !important; }
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

# --- SIDEBAR ---
with st.sidebar:
    st.button("FERRAMENTA IA")
    # O espaçamento de 35px foi aplicado após o botão acima
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

# TEXTO CONFRONTO AGORA EM BRANCO
st.markdown(f'<div class="confronto-label">Confronto: {comp_sel}</div>', unsafe_allow_html=True)

elenco = times_db.get(comp_sel, ["Selecione o Campeonato", "Time A", "Time B"])
t1, t2 = st.columns(2)
with t1: casa = st.selectbox("TIME CASA", elenco)
with t2: fora = st.selectbox("TIME FORA", [t for t in elenco if t != casa] if len(elenco)>1 else elenco)

c_btn = st.columns([1, 1, 1])
with c_btn[1]:
    if st.button("PROCESSAR ALGORITMO"):
        with st.status("GIAE IA: Processando dados...", expanded=False):
            time.sleep(1)
        st.success(f"Análise de {casa} x {fora} finalizada.")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | AJUSTE V9.2</div><div>GESTOR IA PRO</div></div>""", unsafe_allow_html=True)
