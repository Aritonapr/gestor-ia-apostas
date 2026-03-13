import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v5.5]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS DE ALTA PERFORMANCE VISUAL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    /* 1. RESET E FUNDO */
    header, [data-testid="stHeader"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif !important; }
    
    /* Ajuste de margem superior para a Navbar fixa */
    .main .block-container { padding-top: 70px !important; padding-left: 50px !important; padding-right: 50px !important; }

    /* 2. NAVBAR SUPERIOR */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 55px; 
        background-color: #1a242d; border-bottom: 2px solid #f64d23; 
        display: flex; align-items: center; padding: 0 25px; z-index: 999999; 
    }
    .logo-text { color: #f64d23; font-weight: 800; font-size: 20px; font-style: italic; letter-spacing: -1px; }
    .nav-items { display: flex; gap: 20px; margin-left: 35px; flex-grow: 1; color: #adb5bd; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    .logo-hex { width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px; }

    /* 3. CUSTOMIZAÇÃO DOS SELECTBOXES (ESTILO DARK) */
    div[data-baseweb="select"] > div {
        background-color: #1a242d !important;
        border: 1px solid #2d3843 !important;
        color: white !important;
        border-radius: 8px !important;
    }
    div[data-testid="stSelectbox"] label {
        color: #64748b !important;
        font-size: 12px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        margin-bottom: 8px !important;
    }
    div[data-baseweb="select"] * { color: white !important; font-size: 14px !important; }

    /* 4. BOTÕES CÁPSULA (ORANGE GLOW) */
    div[data-testid="stButton"] button {
        background: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        height: 50px !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(246, 77, 35, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stButton"] button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(246, 77, 35, 0.5) !important;
        border: none !important;
    }

    /* 5. SIDEBAR DESIGN */
    [data-testid="stSidebar"] { background-color: #11151a !important; border-right: 1px solid #2d3843 !important; }
    [data-testid="stSidebarContent"] { padding-top: 20px !important; }
    
    /* Botões da Sidebar que não são o principal */
    .side-menu-item div[data-testid="stButton"] button {
        background: transparent !important;
        color: #94a3b8 !important;
        border-radius: 0px !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        justify-content: flex-start !important;
        font-size: 11px !important;
        box-shadow: none !important;
        height: 45px !important;
    }
    .side-menu-item div[data-testid="stButton"] button:hover {
        color: #f64d23 !important;
        background: #1a242d !important;
        border-left: 3px solid #f64d23 !important;
    }

    /* 6. TÍTULOS E DIVISORES */
    .main-title { color: white; font-size: 26px; font-weight: 800; margin-bottom: 30px; letter-spacing: -0.5px; }
    .section-label { color: white; font-size: 16px; font-weight: 700; margin: 25px 0 15px 0; }
    hr { border-color: #2d3843 !important; }

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
            <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Radar IA</span><span>Assertividade</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:12px; align-items:center;">
            <div style="color:#adb5bd; font-size:11px; font-weight:700; cursor:pointer;">REGISTRAR</div>
            <div style="background:#f64d23; color:white; padding:7px 18px; border-radius:4px; font-weight:800; font-size:11px; cursor:pointer;">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<div style='margin-top:20px'></div>", unsafe_allow_html=True)
    if st.button("🔥 FERRAMENTA IA"): st.session_state.app_state = "processar"
    
    st.markdown('<div class="side-menu-item">', unsafe_allow_html=True)
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")
    st.markdown('</div>', unsafe_allow_html=True)

# --- CONTEÚDO PRINCIPAL ---
st.markdown('<div class="main-title">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)

# Grid de Seleção Superior
c1, c2, c3 = st.columns(3)
with c1: st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA ELITE"])
with c2: st.selectbox("CATEGORIA", ["Brasileirão", "Copa do Brasil"])
with c3: st.selectbox("CAMPEONATO", ["Série A", "Série B"])

st.markdown("<hr>", unsafe_allow_html=True)

# Seção de Confronto
st.markdown('<div class="section-label">Confronto: Série A</div>', unsafe_allow_html=True)

t1, t2 = st.columns(2)
with t1: st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "Botafogo"])
with t2: st.selectbox("TIME FORA", ["Flamengo", "Palmeiras", "Vasco"])

# Botão de Ação Centralizado
st.markdown("<div style='margin-top:30px; width: 300px;'>", unsafe_allow_html=True)
if st.button("PROCESSAR ALGORITMO"):
    with st.status("Processando dados...", expanded=False):
        time.sleep(1)
st.markdown("</div>", unsafe_allow_html=True)

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN V5.5 PREMIUM</div><div>GESTOR IA PRO v5.5 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
