import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v6.1 - BETANO STYLE]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS DE ALTA ESPECIFICIDADE (ESTILO BETANO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* 1. RESET E TIPOGRAFIA GLOBAL */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { 
        background-color: #0b0e11 !important; 
        color: #e2e8f0 !important; 
        font-family: 'Inter', sans-serif !important; 
    }
    
    [data-testid="stSidebar"] { 
        background-color: #15191d !important; 
        margin-top: 50px !important; 
        border-right: 1px solid #2d3843 !important;
    }

    /* 2. NAVBAR SUPERIOR (ESTILO BETANO OFICIAL) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #f64d23; 
        display: flex; align-items: center; padding: 0 35px; z-index: 999999; 
    }
    
    .logo-text { 
        color: #ffffff !important; 
        font-weight: 900 !important; 
        font-size: 22px !important; 
        letter-spacing: -1px !important;
        text-transform: uppercase;
        /* A Betano não usa itálico no texto do logo principal, apenas um peso bem forte */
    }

    .nav-items { 
        display: flex; gap: 25px; margin-left: 45px; flex-grow: 1; 
        color: white; font-size: 12px; font-weight: 700; 
        text-transform: uppercase; 
        letter-spacing: 0.5px;
    }

    /* 3. BOTÕES DA NAVBAR */
    .btn-registrar { 
        border: 1px solid rgba(255,255,255,0.6); 
        color: white; padding: 6px 15px; border-radius: 4px; 
        font-size: 12px; font-weight: 800; cursor: pointer;
        text-transform: uppercase;
    }
    .btn-entrar { 
        background: white; color: #f64d23; padding: 8px 22px; 
        border-radius: 4px; font-weight: 800; border: none; 
        font-size: 12px; cursor: pointer;
        text-transform: uppercase;
    }

    /* 4. SELECTBOXES DARK */
    div[data-baseweb="select"] > div {
        background-color: #1a242d !important;
        border: 1px solid #2d3843 !important;
        border-radius: 4px !important;
    }
    div[data-baseweb="select"] div { color: white !important; font-size: 14px !important; }
    div[data-testid="stSelectbox"] label p {
        color: #94a3b8 !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
    }

    /* 5. BOTÕES CÁPSULA GIAE */
    div[data-testid="stVerticalBlock"] button, .stButton button {
        background-color: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        transition: transform 0.2s ease;
    }
    div[data-testid="stVerticalBlock"] button:hover, .stButton button:hover {
        transform: scale(1.02);
        background-color: #ff6b4a !important;
    }

    /* 6. SIDEBAR MENU */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:not(:first-child) button {
        background-color: transparent !important;
        color: #adb5bd !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        justify-content: flex-start !important;
        font-size: 11px !important;
        border-radius: 0px !important;
        padding: 15px !important;
    }

    /* FOOTER */
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 30px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 10px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR (ESTILO REFINADO) ---
st.markdown(f"""
    <div class="betano-header">
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-items">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:15px; align-items:center;">
            <div class="btn-registrar">Registrar</div>
            <div class="btn-entrar">Entrar</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS (PRESERVADO) ---
db_global = {
    "BR COMPETIÇÕES BRASILEIRAS": {
        "Brasileirão": ["Série A", "Série B", "Série C", "Série D"],
        "Copas Nacionais": ["Copa do Brasil", "Supercopa do Brasil"]
    },
    "EU ELITE EUROPEIA (BIG 5)": {
        "Inglaterra": ["Premier League"], "Espanha": ["La Liga"]
    }
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
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:25px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1: reg_sel = st.selectbox("SELECIONE A REGIÃO", list(db_global.keys()))
    with c2: cat_sel = st.selectbox("CATEGORIA", list(db_global[reg_sel].keys()))
    with c3: comp_sel = st.selectbox("CAMPEONATO", db_global[reg_sel][cat_sel])

    st.markdown("<hr style='border: 0.5px solid #2d3843;'>", unsafe_allow_html=True)
    st.markdown(f'<div style="color:white; font-weight:700; font-size:18px; margin-top:10px;">Confronto: {comp_sel}</div>', unsafe_allow_html=True)
    
    t1, t2 = st.columns(2)
    with t1: casa = st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "Botafogo"])
    with t2: fora = st.selectbox("TIME FORA", ["Flamengo", "Palmeiras", "Vasco"])

    if st.button("PROCESSAR ALGORITMO"):
        with st.status("GIAE IA: Processando...", expanded=True) as s:
            time.sleep(1.2); s.update(label="Análise concluída!", state="complete")
        st.success(f"🤖 Análise para {casa} x {fora} finalizada.")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN V6.1</div><div>GESTOR IA PRO v6.1 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
