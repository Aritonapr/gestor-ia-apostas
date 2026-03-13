import streamlit as st
import time

# [GIAE ULTRA-SHIELD v14.0 - ESTÉTICA ESPORTIVA ELITE]
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- BLOCO DE SEGURANÇA CSS (FOCO EM TIPOGRAFIA ESPORTIVA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800;900&display=swap');

    /* 1. RESET E BLINDAGEM */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; }

    /* 2. NAVBAR SUPERIOR (DIFERENCIAL ESPORTIVO: ESPAÇAMENTO E PESO) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 55px; 
        background-color: #121212 !important; 
        border-bottom: 2px solid #f64d23; 
        display: flex; align-items: center; padding: 0 30px; z-index: 999999; 
    }
    .logo-text { 
        color: #ffffff !important; 
        font-weight: 900; 
        font-size: 22px; 
        text-transform: uppercase; 
        margin-right: 40px; 
        letter-spacing: -1.2px; /* Logo mais compacto e moderno */
    }
    .nav-items { 
        display: flex; 
        gap: 28px; 
        flex-grow: 1; 
        color: #ffffff !important; 
        font-size: 12px !important; /* Tamanho Betano */
        font-weight: 800 !important; /* Peso Betano */
        text-transform: uppercase; 
        letter-spacing: 0.8px; /* O DIFERENCIAL ESPORTIVO AQUI */
    }
    .nav-items span:hover { color: #f64d23; cursor: pointer; }

    /* BOTÕES DA NAVBAR */
    .btn-registrar { border: 1px solid #475569; color: white; padding: 6px 15px; border-radius: 4px; font-size: 11px; font-weight: 800; cursor: pointer; letter-spacing: 0.5px; }
    .btn-entrar { background: #00cc66 !important; color: white !important; padding: 8px 22px; border-radius: 4px; font-weight: 800; border: none; font-size: 11px; cursor: pointer; letter-spacing: 0.5px; }

    /* 3. SIDEBAR (PROTEÇÃO DE LISTA E TIPOGRAFIA COERENTE) */
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        border-right: 1px solid #2d3843 !important;
        margin-top: 55px !important;
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; padding-top: 0px !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        color: #94a3b8 !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        border-radius: 0px !important;
        text-align: left !important;
        justify-content: flex-start !important;
        width: 100% !important;
        padding: 14px 20px !important;
        font-weight: 800 !important; /* Coerência com o menu superior */
        font-size: 11px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.6px; /* Toque esportivo na lateral também */
    }
    [data-testid="stSidebar"] button:hover { color: #f64d23 !important; background-color: #1a242d !important; border-left: 3px solid #f64d23 !important; }

    /* 4. ÁREA CENTRAL (EXECUTAR ALGORITMO) */
    [data-testid="stAppViewBlockContainer"] { padding-top: 15px !important; padding-left: 3rem !important; padding-right: 3rem !important; }

    section.main div.stButton > button {
        background-color: #f64d23 !important;
        color: #ffffff !important;
        border-radius: 50px !important;
        height: 44px !important;
        width: 250px !important;
        font-weight: 900 !important; /* Força máxima no botão de ação */
        font-size: 13px !important;
        text-transform: uppercase !important;
        letter-spacing: 1px; /* Máxima legibilidade esportiva */
        border: none !important;
        margin-top: 20px !important;
        box-shadow: 0 4px 12px rgba(246, 77, 35, 0.3) !important;
    }

    /* 5. SELECTBOXES DARK (ESTÉTICA DE TERMINAL) */
    div[data-baseweb="select"] > div { background-color: #1a242d !important; border: 1px solid #2d3843 !important; }
    div[data-baseweb="select"] * { color: #e2e8f0 !important; font-weight: 600 !important; }

    /* FOOTER */
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #121212; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #64748b; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR (VERSÃO ELITE ESPORTIVA) ---
st.markdown(f"""
    <div class="betano-header">
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-items">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Estatísticas Avançadas</span>
            <span>Mercado Probabilístico</span>
            <span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:15px; align-items:center;">
            <div class="btn-registrar">REGISTRAR</div>
            <div class="btn-entrar">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.button("JOGOS DO DIA")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL ---
st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:20px; letter-spacing: -0.5px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1: st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
with c2: st.selectbox("CATEGORIA", ["Brasileirão", "Copa do Brasil"])
with c3: st.selectbox("CAMPEONATO", ["Série A", "Série B"])

st.markdown("<hr style='border: 0.1px solid #2d3843; opacity: 0.3; margin: 15px 0;'>", unsafe_allow_html=True)
st.markdown('<div style="color:white; font-weight:700; font-size:18px; margin-bottom:15px;">Confronto: Série A</div>', unsafe_allow_html=True)

t1, t2 = st.columns(2)
with t1: st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "Botafogo"])
with t2: st.selectbox("TIME FORA", ["Flamengo", "Vasco", "Palmeiras"])

if st.button("EXECUTAR ALGORITMO"):
    with st.status("GIAE IA: Processando...", expanded=False):
        time.sleep(1)
    st.success("🤖 Análise finalizada!")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN V14.0 ELITE</div><div>GESTOR IA PRO v14.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
