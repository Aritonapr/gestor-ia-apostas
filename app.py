import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v6.0 - CABEÇALHO LARANJA EDITION]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS DE ALTA ESPECIFICIDADE ---
st.markdown("""
    <style>
    /* 1. RESET GERAL E SIDEBAR */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    [data-testid="stSidebar"] { 
        background-color: #15191d !important; 
        margin-top: 50px !important; 
        width: 260px !important; 
        min-width: 260px !important;
        border-right: 1px solid #2d3843 !important;
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; margin-top: -35px !important; }

    /* 2. NAVBAR SUPERIOR (CORREÇÃO: FUNDO LARANJA E TEXTO BRANCO) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 50px; 
        background-color: #f64d23; /* Cor do botão agora no fundo */
        display: flex; align-items: center; padding: 0 20px; z-index: 999999; 
        border-bottom: none;
    }
    .logo-text { color: #ffffff !important; font-weight: 900; font-size: 19px; font-style: italic; }
    .nav-items { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    
    .logo-hex { 
        width:20px; height:24px; background: white; /* Hexágono branco para contrastar */
        clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); 
        margin-right:10px; 
    }

    /* 3. CUSTOMIZAÇÃO DOS SELECTBOXES (PARA FICAREM DARK) */
    div[data-baseweb="select"] > div {
        background-color: #1a242d !important;
        border: 1px solid #2d3843 !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="select"] div { color: white !important; }
    div[data-testid="stSelectbox"] label p {
        color: #94a3b8 !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
    }

    /* 4. BOTÕES CÁPSULA (SIDEBAR E CENTRAL) */
    div[data-testid="stVerticalBlock"] button, .stButton button {
        background-color: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        outline: none !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: none !important;
    }

    /* BOTÃO FERRAMENTA IA (SIDEBAR) */
    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button {
        height: 60px !important;
        width: 95% !important;
        font-size: 15px !important;
        margin: 0px auto 25px 10px !important;
    }

    /* BOTÃO PROCESSAR ALGORITMO (CENTRAL) */
    .main .stButton button {
        height: 60px !important;
        width: 320px !important;
        font-size: 15px !important;
        margin-top: 20px !important;
    }

    /* REMOÇÃO TOTAL DO QUADRADO NO HOVER */
    div[data-testid="stVerticalBlock"] button:hover, .stButton button:hover {
        background-color: #ff6b4a !important;
        box-shadow: 0 0 20px #f64d23 !important;
        border-radius: 50px !important;
    }

    /* 5. BOTÕES SECUNDÁRIOS DA SIDEBAR */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:not(:first-child) button {
        background-color: transparent !important;
        color: #e2e8f0 !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        font-weight: 700 !important;
        font-size: 11px !important;
        padding: 12px 15px !important;
        width: 100% !important;
        border-radius: 0px !important;
    }

    /* 6. TÍTULOS */
    .white-title { color: white !important; font-weight: 900; font-size: 26px !important; margin-bottom: 25px !important; }
    .standard-text { color: #e2e8f0 !important; font-weight: 700; font-size: 18px !important; margin-top: 10px !important; }

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
        <div style="margin-left:auto; display:flex; gap:12px; align-items:center;">
            <div style="border:1px solid white; color:white; padding:4px 12px; border-radius:3px; font-size:11px; font-weight:bold; cursor:pointer;">REGISTRAR</div>
            <button style="background:white; color:#f64d23; padding:6px 20px; border-radius:3px; font-weight:bold; border:none; font-size:11px; cursor:pointer;">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS (PRESERVADO) ---
db_global = {
    "BR COMPETIÇÕES BRASILEIRAS": {
        "Brasileirão": ["Série A", "Série B", "Série C", "Série D"],
        "Copas Nacionais": ["Copa do Brasil", "Supercopa do Brasil"],
        "Estaduais": ["Paulistão", "Carioca", "Mineiro", "Gaúcho"]
    },
    "EU ELITE EUROPEIA (BIG 5)": {
        "Inglaterra": ["Premier League"], "Espanha": ["La Liga"], "Alemanha": ["Bundesliga"], "Itália": ["Serie A"], "França": ["Ligue 1"]
    }
}

times_db = {
    "Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Internacional"],
    "Carioca": ["Flamengo", "Vasco", "Fluminense", "Botafogo"],
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Chelsea", "Tottenham"]
}

# --- SIDEBAR ---
with st.sidebar:
    if st.button("FERRAMENTA IA"): st.session_state.app_state = "processar"
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL ---
if "app_state" not in st.session_state: st.session_state.app_state = "processar"

if st.session_state.app_state == "processar":
    st.markdown('<div class="white-title">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1: reg_sel = st.selectbox("SELECIONE A REGIÃO", list(db_global.keys()))
    with c2: cat_sel = st.selectbox("CATEGORIA", list(db_global[reg_sel].keys()))
    with c3: comp_sel = st.selectbox("CAMPEONATO", db_global[reg_sel][cat_sel])

    st.divider()
    st.markdown(f'<div class="standard-text">Confronto: {comp_sel}</div>', unsafe_allow_html=True)
    
    elenco = times_db.get(comp_sel, [f"Time A ({comp_sel})", f"Time B ({comp_sel})"])
    t1, t2 = st.columns(2)
    with t1: casa = st.selectbox("TIME CASA", elenco)
    with t2: fora = st.selectbox("TIME FORA", [t for t in elenco if t != casa])

    if st.button("PROCESSAR ALGORITMO"):
        with st.status("GIAE IA: Processando...", expanded=True) as s:
            time.sleep(1.2); s.update(label="Análise de algoritmo concluída", state="complete")
        st.success(f"🤖 Análise concluída.")
else:
    st.markdown("### 🤖 Cockpit de Comando Ativado")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN V6.0 BLINDADO</div><div>GESTOR IA PRO v6.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
