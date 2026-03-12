import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v9.0]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- BANCO DE DADOS INTEGRAL (RESTAURADO) ---
db_global = {
    "BR COMPETIÇÕES BRASILEIRAS": {
        "Brasileirão": ["Série A", "Série B", "Série C", "Série D"],
        "Copas Nacionais": ["Copa do Brasil", "Supercopa do Brasil"],
        "Estaduais": ["Paulistão", "Carioca", "Mineiro", "Gaúcho"]
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
    "Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Vasco", "Corinthians"],
    "Copa do Brasil": ["Flamengo", "Amazonas FC", "Bahia", "Grêmio", "Palmeiras", "Atlético-MG"],
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Chelsea", "Tottenham"]
}

# --- INJEÇÃO DE CÓDIGO FONTE SUPREMO (ARQUITETURA BLINDADA) ---
st.markdown("""
    <style>
    /* 1. LIMPEZA TOTAL E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    /* 2. SIDEBAR MILIMÉTRICA (SUBIDA PARA -55PX) */
    [data-testid="stSidebar"] { 
        background-color: #15191d !important; 
        margin-top: 50px !important; 
        width: 260px !important; 
        min-width: 260px !important;
        border-right: 1px solid #2d3843 !important;
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { 
        gap: 10px !important; 
        padding-top: 0px !important; 
        margin-top: -55px !important; /* SUBIDA SOLICITADA */
    }

    /* 3. NAVBAR SUPERIOR */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    .nav-items { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    .logo-hex { width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px; }

    /* 4. BOTÕES GÊMEOS (CÁPSULAS LARANJAS) */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    
    div.stButton > button, [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button {
        background-color: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        height: 48px !important;
        border: none !important;
        font-weight: 900 !important;
        font-size: 12px !important;
        text-transform: uppercase !important;
        position: relative !important;
        overflow: hidden !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
    }

    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button {
        width: 180px !important;
        margin: 10px auto 20px auto !important;
    }

    /* 5. BOTÕES DE CATEGORIA DA SIDEBAR (RECUPERANDO FUNÇÃO DE BOTÃO) */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:not(:first-child) button {
        background-color: #1e293b !important; /* Fundo visível para parecer botão */
        color: #e2e8f0 !important;
        border: 1px solid #2d3843 !important;
        text-align: left !important;
        font-weight: 700 !important;
        font-size: 10px !important;
        padding: 12px 15px !important;
        width: 100% !important;
        border-radius: 6px !important;
        text-transform: uppercase;
        margin-bottom: 2px !important;
        transition: 0.3s;
    }

    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:not(:first-child) button:hover {
        border-color: #f64d23 !important;
        background-color: #2d3843 !important;
        color: #f64d23 !important;
    }

    /* 6. CORREÇÃO DOS SELECTBOXES (FUNDO ESCURO PROTEGIDO) */
    div[data-baseweb="select"] > div {
        background-color: #1a242d !important;
        color: white !important;
        border: 1px solid #2d3843 !important;
        border-radius: 4px !important;
    }
    
    div[role="listbox"] {
        background-color: #1a242d !important;
        color: white !important;
    }

    /* 7. TEXTOS E TÍTULOS */
    .white-title { color: white !important; font-weight: 900; font-size: 26px !important; margin-bottom: 25px !important; }
    .standard-text { color: #e2e8f0 !important; font-weight: 700; font-size: 18px !important; margin-top: 15px !important; }
    
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown(f"""
    <div class="betano-header">
        <div class="logo-hex"></div>
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-items">
            <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Apostas Encontradas</span><span>Assertividade IA</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (RESTAURADA E ELEVADA) ---
with st.sidebar:
    st.button("FERRAMENTA IA")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL (COM LOGICA DE SELEÇÃO RECUPERADA) ---
st.markdown('<div class="white-title">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)

# Logica de Seleção Dinâmica
c1, c2, c3 = st.columns(3)
with c1: 
    reg_sel = st.selectbox("SELECIONE A REGIÃO", list(db_global.keys()))
with c2: 
    cat_sel = st.selectbox("CATEGORIA", list(db_global[reg_sel].keys()))
with c3: 
    comp_sel = st.selectbox("CAMPEONATO", db_global[reg_sel][cat_sel])

st.divider()

st.markdown(f'<div class="standard-text">Confronto: {comp_sel}</div>', unsafe_allow_html=True)

# Logica de Times
elenco = times_db.get(comp_sel, ["Time A", "Time B"])
t1, t2 = st.columns(2)
with t1: casa = st.selectbox("TIME CASA", elenco)
with t2: fora = st.selectbox("TIME FORA", [t for t in elenco if t != casa] if len(elenco) > 1 else elenco)

if st.button("PROCESSAR ALGORITMO"):
    with st.status("Processando...", expanded=False):
        time.sleep(1)
    st.success(f"Análise de {casa} vs {fora} concluída.")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN FINAL BLINDADO</div><div>GESTOR IA PRO v9.0</div></div>""", unsafe_allow_html=True)
