import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v4.1]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS DE ALTA FIDELIDADE (TRAVADO E BLINDADO) ---
st.markdown("""
    <style>
    /* RESET TOTAL E OCULTAÇÃO DE HEADER */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    /* NAVBAR SUPERIOR FIXA */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    .nav-items { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    
    @keyframes pulse-hex { 0%, 100% { transform: scale(0.9); filter: drop-shadow(0 0 2px #f64d23); } 50% { transform: scale(1.1); filter: drop-shadow(0 0 10px #f64d23); } }
    .logo-hex { width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px; animation: pulse-hex 2s infinite ease-in-out; }

    /* SIDEBAR MILIMÉTRICA: 260PX / -35PX TOP / SEM SCROLL */
    [data-testid="stSidebar"] { 
        background-color: #15191d !important; 
        margin-top: 50px !important; 
        border-right: 1px solid #2d3843 !important; 
        width: 260px !important; 
        min-width: 260px !important;
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; margin-top: -35px !important; }
    
    /* ANIMAÇÕES DE BOTÃO */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    @keyframes plasma-glow { 0%, 100% { box-shadow: 0 0 10px #f64d23; } 50% { box-shadow: 0 0 20px #f64d23; } }
    
    /* UNIFICAÇÃO DE ESTILO: BOTÕES CÁPSULA (SIDEBAR E CENTRAL) */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button,
    .main div.stButton > button {
        background: #f64d23 !important; 
        color: white !important; 
        border-radius: 30px !important; 
        height: 52px !important; /* Altura aumentada para melhor proporção */
        width: 95% !important; 
        display: flex !important; 
        align-items: center !important; 
        justify-content: center !important;
        font-weight: 900 !important; 
        font-size: 13px !important; /* Texto levemente maior */
        position: relative !important; 
        overflow: hidden !important; 
        border: none !important;
        text-align: center !important; 
        padding: 0px !important;
        animation: plasma-glow 3s infinite ease-in-out !important;
        white-space: nowrap !important;
        box-shadow: none !important;
        outline: none !important;
    }

    /* REMOÇÃO TOTAL DE EFEITOS DE HOVER (QUADRADOS E ALTERAÇÃO DE COR) */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button:hover,
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button:active,
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button:focus,
    .main div.stButton > button:hover,
    .main div.stButton > button:active,
    .main div.stButton > button:focus {
        background: #f64d23 !important;
        color: white !important;
        border: none !important;
        outline: none !important;
        box-shadow: 0 0 20px #f64d23 !important; /* Mantém apenas o brilho, sem quadrado */
        border-radius: 30px !important;
    }

    /* BOTÃO CENTRAL - LARGURA */
    .main div.stButton > button { width: 300px !important; margin-top: 20px !important; }

    /* SCANNER LASER */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::after,
    .main div.stButton > button::after {
        content: "" !important; 
        position: absolute !important; 
        top: 0 !important; 
        left: -100% !important; 
        width: 60px !important; 
        height: 100% !important;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important; 
        animation: laser-scan 2.5s infinite linear !important;
    }

    /* BOTÕES SECUNDÁRIOS SIDEBAR */
    [data-testid="stSidebar"] button { 
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
        text-transform: uppercase; 
    }
    
    /* ESTILOS DE TEXTO */
    .white-title { color: #e2e8f0 !important; font-weight: 900; font-size: 24px !important; margin-bottom: 20px !important; }
    .standard-text { color: #e2e8f0 !important; font-weight: 700; font-size: 18px !important; margin-top: 10px !important; }

    /* FOOTER */
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
            <div style="border:1px solid #adb5bd; color:white; padding:4px 12px; border-radius:3px; font-size:11px; font-weight:bold; cursor:pointer;">REGISTRAR</div>
            <button style="background:#00cc66; color:white; padding:6px 20px; border-radius:3px; font-weight:bold; border:none; font-size:11px; cursor:pointer;">ENTRAR</button>
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
if "app_state" not in st.session_state: st.session_state.app_state = "home"

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
        with st.status("IA: Processando...", expanded=True) as s:
            time.sleep(1.2); s.update(label="analise de algoritimo concluida", state="complete")
        st.success(f"🤖 Análise métrica de {casa} vs {fora} finalizada.")
else:
    st.markdown("### 🤖 Cockpit de Comando Ativado")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | HOVER FIX: ON</div><div>GESTOR IA PRO v4.1 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
