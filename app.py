import streamlit as st
import time

# [GIAE ULTRA-SHIELD v12.0 - PALETA GRAFITE & PROTEÇÃO DE ESTRUTURA]
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- SISTEMA DE PROTEÇÃO CSS (NÃO ALTERAR) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* 1. RESET DE INTERFACE E REMOÇÃO DE SETAS/HEADERS */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; }

    /* 2. NAVBAR SUPERIOR (NOVA PALETA: GRAFITE PROFISSIONAL) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 50px; 
        background-color: #121212 !important; /* Grafite Profissional */
        border-bottom: 2px solid #f64d23;    /* Linha de acento laranja */
        display: flex; align-items: center; padding: 0 25px; z-index: 999999; 
    }
    .logo-text { color: #ffffff !important; font-weight: 900; font-size: 20px; text-transform: uppercase; margin-right: 35px; letter-spacing: -1px; }
    .nav-items { display: flex; gap: 18px; flex-grow: 1; color: #adb5bd; font-size: 10px; font-weight: 700; text-transform: uppercase; }
    .nav-items span:hover { color: #f64d23; cursor: pointer; }

    /* BOTÕES DA NAVBAR */
    .btn-registrar { border: 1px solid #475569; color: white; padding: 5px 12px; border-radius: 4px; font-size: 11px; font-weight: bold; cursor: pointer; }
    .btn-entrar { background: #00cc66 !important; color: white !important; padding: 7px 20px; border-radius: 4px; font-weight: bold; border: none; font-size: 11px; cursor: pointer; }

    /* 3. PROTEÇÃO DA SIDEBAR (ELEVAÇÃO MÁXIMA E FUNDO LIMPO) */
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        border-right: 1px solid #2d3843 !important;
        margin-top: 50px !important;
    }
    [data-testid="stSidebarContent"] { 
        overflow: hidden !important; 
        padding-top: 0px !important; 
    }
    
    /* Puxa "JOGOS DO DIA" para o topo absoluto (Elevação Lateral) */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { 
        margin-top: -45px !important; 
        gap: 0px !important; 
    }

    /* ESTILO LISTA DA SIDEBAR (PROTEÇÃO CONTRA FUNDO BRANCO) */
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        background: transparent !important;
        color: #94a3b8 !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        border-radius: 0px !important;
        text-align: left !important;
        justify-content: flex-start !important;
        width: 100% !important;
        padding: 12px 20px !important;
        font-weight: 700 !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        box-shadow: none !important;
    }
    [data-testid="stSidebar"] button:hover {
        color: #f64d23 !important;
        background-color: #1a242d !important;
        border-left: 3px solid #f64d23 !important;
    }

    /* 4. PROTEÇÃO ÁREA CENTRAL (ELEVAÇÃO DO TÍTULO) */
    [data-testid="stAppViewBlockContainer"] {
        padding-top: 10px !important; /* Sobe o título para encostar na navbar */
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }

    /* 5. BOTÃO EXECUTAR ALGORITMO (LARANJA, VISÍVEL E PROPORCIONAL) */
    section.main div.stButton > button {
        background-color: #f64d23 !important;
        color: #ffffff !important;
        border-radius: 50px !important;
        height: 42px !important;
        width: 240px !important;
        font-weight: 800 !important;
        font-size: 12px !important;
        text-transform: uppercase !important;
        border: none !important;
        margin-top: 15px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 0 4px 12px rgba(246, 77, 35, 0.3) !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
    section.main div.stButton > button:hover {
        background-color: #ff6b4a !important;
        box-shadow: 0 0 15px #f64d23 !important;
    }

    /* 6. SELECTBOXES DARK PROFISSIONAIS */
    div[data-baseweb="select"] > div { background-color: #1a242d !important; border: 1px solid #2d3843 !important; border-radius: 6px !important; }
    div[data-baseweb="select"] * { color: #e2e8f0 !important; font-size: 13px !important; }
    div[data-testid="stSelectbox"] label p { color: #64748b !important; font-size: 10px !important; font-weight: 700; text-transform: uppercase; margin-bottom: 4px; }

    /* DIVISORES */
    hr { margin: 15px 0 !important; border-bottom: 1px solid #2d3843 !important; opacity: 0.3; }

    /* FOOTER */
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #121212; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #64748b; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR ATUALIZADA (ESTÉTICA GRAFITE) ---
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

# --- SIDEBAR (SUBIDA AO MÁXIMO + PROTEÇÃO) ---
with st.sidebar:
    st.button("JOGOS DO DIA")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL (SUBIDA AO MÁXIMO + PROTEÇÃO) ---
st.markdown('<div style="color:white; font-weight:900; font-size:24px; margin-bottom:15px; letter-spacing: -0.5px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)

# Grid de Filtros Compacto
c1, c2, c3 = st.columns(3)
with c1: st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
with c2: st.selectbox("CATEGORIA", ["Brasileirão", "Copa do Brasil"])
with c3: st.selectbox("CAMPEONATO", ["Série A", "Série B"])

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div style="color:white; font-weight:700; font-size:16px; margin-bottom:10px;">Confronto: Série A</div>', unsafe_allow_html=True)

t1, t2 = st.columns(2)
with t1: st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "Botafogo"])
with t2: st.selectbox("TIME FORA", ["Flamengo", "Vasco", "Palmeiras"])

# BOTÃO EXECUTAR (CORRIGIDO E BLINDADO)
if st.button("EXECUTAR ALGORITMO"):
    with st.status("GIAE IA: Processando algoritmos...", expanded=False):
        time.sleep(1)
    st.success("🤖 Análise concluída com sucesso!")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN V12.0 GRAFITE</div><div>GESTOR IA PRO v12.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
