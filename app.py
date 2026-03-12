import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v9.0]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- INJEÇÃO DE CÓDIGO FONTE SUPREMO (HARMONIZAÇÃO VISUAL) ---
st.markdown("""
    <style>
    /* 1. LIMPEZA TOTAL DE INTERFACE */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    /* 2. SIDEBAR MILIMÉTRICA (260PX / TOP -35PX) */
    [data-testid="stSidebar"] { 
        background-color: #15191d !important; 
        margin-top: 50px !important; 
        width: 260px !important; 
        min-width: 260px !important;
        border-right: 1px solid #2d3843 !important;
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; margin-top: -35px !important; }

    /* 3. NAVBAR SUPERIOR PROFISSIONAL */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    .nav-items { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    @keyframes pulse-hex { 0%, 100% { transform: scale(0.9); } 50% { transform: scale(1.1); } }
    .logo-hex { width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px; animation: pulse-hex 2s infinite ease-in-out; }

    /* 4. BOTÕES GÊMEOS (CÁPSULAS LARANJAS) */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    @keyframes plasma-glow { 0%, 100% { box-shadow: 0 0 5px #f64d23; } 50% { box-shadow: 0 0 15px #f64d23; } }

    div.stButton > button, [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button {
        background-color: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        height: 50px !important;
        border: none !important;
        font-weight: 900 !important;
        font-size: 12px !important;
        text-transform: uppercase !important;
        position: relative !important;
        overflow: hidden !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        animation: plasma-glow 3s infinite ease-in-out !important;
        text-align: center !important;
    }

    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button {
        width: 180px !important;
        margin: 10px auto 25px auto !important;
    }

    /* 5. HARMONIZAÇÃO DOS COMPONENTES DE SELEÇÃO (FIM DO FUNDO BRANCO) */
    div[data-baseweb="select"] > div {
        background-color: #1a242d !important;
        color: white !important;
        border: 1px solid #2d3843 !important;
        border-radius: 8px !important;
    }

    /* Estilização das Labels (Títulos dos Selects) */
    [data-testid="stWidgetLabel"] p {
        color: #94a3b8 !important;
        font-size: 10px !important;
        text-transform: uppercase !important;
        font-weight: 800 !important;
        margin-bottom: 5px !important;
    }

    /* Cor do texto dentro dos campos de seleção */
    div[data-testid="stSelectbox"] div {
        color: #ffffff !important;
    }

    /* Estilização dos Métricas (Cards de Resultado) */
    [data-testid="stMetric"] {
        background-color: #15191d !important;
        border: 1px solid #2d3843 !important;
        padding: 15px !important;
        border-radius: 10px !important;
    }

    /* 6. TÍTULOS E ESTILOS DE TEXTO */
    .white-title { color: white !important; font-weight: 900; font-size: 26px !important; margin-bottom: 25px !important; }
    .standard-text { color: #e2e8f0 !important; font-weight: 700; font-size: 18px !important; margin-top: 15px !important; }
    
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR (FIXADA NO TOPO) ---
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

# --- SIDEBAR (ALINHAMENTO PROTEGIDO) ---
with st.sidebar:
    if st.button("FERRAMENTA IA"): 
        st.session_state.app_state = "processar"
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")

# --- ÁREA CENTRAL (COCKPIT HARMONIZADO) ---
if "app_state" not in st.session_state: st.session_state.app_state = "home"

if st.session_state.app_state == "processar":
    st.markdown('<div class="white-title">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    
    # Grid de Seleção Harmonizada
    c1, c2, c3 = st.columns(3)
    with c1: st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
    with c2: st.selectbox("CATEGORIA", ["Copas Nacionais", "Série A"])
    with c3: st.selectbox("CAMPEONATO", ["Copa do Brasil", "Brasileirão"])

    st.divider()
    st.markdown('<div class="standard-text">Confronto: Copa do Brasil</div>', unsafe_allow_html=True)
    
    t1, t2 = st.columns(2)
    with t1: st.selectbox("TIME CASA", ["Flamengo", "Palmeiras", "Bahia"])
    with t2: st.selectbox("TIME FORA", ["Amazonas FC", "Botafogo", "Vasco"])

    if st.button("PROCESSAR ALGORITMO"):
        st.success("Algoritmo em execução...")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN FINAL BLINDADO</div><div>GESTOR IA PRO v9.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
