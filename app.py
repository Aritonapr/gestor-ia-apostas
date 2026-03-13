import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v7.5 - BLINDAGEM DE DESIGN]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- BLOCO DE PROTEÇÃO CSS (PROTEÇÃO CONTRA DESFAZIMENTO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* 1. RESET E OCULTAR SCROLLBAR */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Inter', sans-serif !important; }
    
    /* REMOÇÃO TOTAL DA BARRA DE ROLAGEM DA SIDEBAR */
    [data-testid="stSidebarContent"] { 
        overflow: hidden !important; 
        -ms-overflow-style: none !important; 
        scrollbar-width: none !important; 
    }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }

    /* 2. NAVBAR SUPERIOR (PROTEÇÃO LARANJA) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 50px; 
        background-color: #f64d23 !important; 
        display: flex; align-items: center; padding: 0 25px; z-index: 999999; 
    }
    .logo-text { color: white !important; font-weight: 900; font-size: 20px; letter-spacing: -1px; text-transform: uppercase; margin-right: 35px; }
    .nav-items { display: flex; gap: 15px; flex-grow: 1; color: white; font-size: 10px; font-weight: 700; text-transform: uppercase; }

    /* BOTÕES DA NAVBAR */
    .btn-registrar { border: 1px solid white; color: white; padding: 5px 12px; border-radius: 3px; font-size: 11px; font-weight: bold; }
    .btn-entrar { background: #00cc66 !important; color: white !important; padding: 6px 20px; border-radius: 3px; font-weight: bold; border: none; font-size: 11px; }

    /* 3. SIDEBAR: TODA A LISTA COM O MESMO PADRÃO (INCLUINDO JOGOS DO DIA) */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; }
    
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        color: #adb5bd !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        justify-content: flex-start !important;
        font-weight: 700 !important;
        font-size: 11px !important;
        padding: 15px 20px !important;
        width: 100% !important;
        border-radius: 0px !important;
        transition: 0.2s !important;
        text-transform: uppercase !important;
    }

    /* EFEITO DE HOVER PARA TODOS OS ITENS DA LISTA */
    [data-testid="stSidebar"] button:hover {
        color: #f64d23 !important;
        background-color: #1a242d !important;
        border-left: 3px solid #f64d23 !important;
    }

    /* 4. BOTÃO CENTRAL: EXECUTAR ALGORITMO (CÁPSULA LARANJA BLINDADA) */
    .main .stButton button {
        background-color: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        height: 55px !important;
        width: 300px !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        border: none !important;
        margin-top: 30px !important;
        box-shadow: 0 4px 15px rgba(246, 77, 35, 0.4) !important;
        justify-content: center !important;
        text-align: center !important;
    }
    .main .stButton button:hover {
        box-shadow: 0 0 25px #f64d23 !important;
        transform: scale(1.02) !important;
        background-color: #ff6b4a !important;
    }

    /* 5. SELECTBOXES DARK */
    div[data-baseweb="select"] > div { background-color: #1a242d !important; border: 1px solid #2d3843 !important; }
    div[data-baseweb="select"] div { color: white !important; }

    /* FOOTER */
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR ---
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
        <div style="margin-left:auto; display:flex; gap:12px; align-items:center;">
            <div class="btn-registrar">REGISTRAR</div>
            <div class="btn-entrar">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (RESTAURADA E SEM SCROLL) ---
with st.sidebar:
    st.button("JOGOS DO DIA") # Agora com o mesmo estilo dos outros
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL ---
st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:25px; margin-top:20px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)

# Filtros
c1, c2, c3 = st.columns(3)
with c1: st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
with c2: st.selectbox("CATEGORIA", ["Brasileirão", "Copa do Brasil"])
with c3: st.selectbox("CAMPEONATO", ["Série A", "Série B"])

st.markdown("<hr style='border: 0.5px solid #2d3843; opacity: 0.5;'>", unsafe_allow_html=True)
st.markdown('<div style="color:white; font-weight:700; font-size:18px; margin:20px 0;">Confronto: Série A</div>', unsafe_allow_html=True)

t1, t2 = st.columns(2)
with t1: st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "Botafogo"])
with t2: st.selectbox("TIME FORA", ["Flamengo", "Vasco", "Palmeiras"])

# BOTÃO EXECUTAR ALGORITMO (LARANJA CÁPSULA)
if st.button("EXECUTAR ALGORITMO"):
    with st.status("GIAE IA: Executando processamento...", expanded=False):
        time.sleep(1.2)
    st.success("🤖 Processamento concluído!")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN V7.5 BLINDADO</div><div>GESTOR IA PRO v7.5 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
