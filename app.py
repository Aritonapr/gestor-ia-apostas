import streamlit as st
import time

# [GIAE PROTOCOLO SOBERANO v15.0 - PROTEÇÃO TOTAL E REFINAMENTO]
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- BLOCO DE SEGURANÇA E BLINDAGEM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');

    /* 1. ELIMINAÇÃO DE ELEMENTOS NATIVOS E SCROLL */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }

    /* 2. NAVBAR SUPERIOR (REFINADA: TEXTO FINO E LINHA SUAVE) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 50px; 
        background-color: #121212 !important; 
        border-bottom: 1px solid #2d3843 !important; /* LINHA SUAVE EM SLATE */
        display: flex; align-items: center; padding: 0 30px; z-index: 999999; 
    }
    .logo-text { 
        color: #ffffff !important; font-weight: 900; font-size: 20px; 
        text-transform: uppercase; margin-right: 40px; letter-spacing: -1px; 
    }
    .nav-items { 
        display: flex; gap: 28px; flex-grow: 1; 
        color: #ffffff !important; 
        font-size: 12px !important; 
        font-weight: 400 !important; /* REMOVIDO NEGRITO PARA ELEGÂNCIA */
        text-transform: uppercase; 
        letter-spacing: 1px; 
    }

    /* 3. SIDEBAR (ELEVAÇÃO EXTREMA E LISTA LIMPA) */
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        border-right: 1px solid #2d3843 !important;
        margin-top: 50px !important;
    }
    /* Puxar JOGOS DO DIA para o topo absoluto */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { 
        margin-top: -65px !important; 
        gap: 0px !important; 
    }
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
        font-weight: 400 !important; /* Tipografia fina também na lateral */
        font-size: 11px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.8px;
        box-shadow: none !important;
    }
    [data-testid="stSidebar"] button:hover { color: #f64d23 !important; border-left: 3px solid #f64d23 !important; }

    /* 4. CONTEÚDO CENTRAL (ELEVAÇÃO MÁXIMA) */
    [data-testid="stAppViewBlockContainer"] { 
        padding-top: 10px !important; 
        padding-left: 3rem !important; 
        padding-right: 3rem !important; 
    }

    /* 5. BOTÃO EXECUTAR ALGORITMO (BLINDAGEM LARANJA - FIM DO FUNDO BRANCO) */
    section.main div.stButton > button {
        background-color: #f64d23 !important; /* LARANJA OBRIGATÓRIO */
        background: #f64d23 !important;        /* REFORÇO DE FUNDO */
        color: #ffffff !important;           /* TEXTO BRANCO */
        border-radius: 50px !important;
        height: 40px !important;             /* TAMANHO PROPORCIONAL */
        width: 220px !important;             /* LARGURA PROPORCIONAL */
        font-weight: 700 !important;
        font-size: 12px !important;
        text-transform: uppercase !important;
        letter-spacing: 1px;
        border: none !important;
        margin-top: 15px !important;
        box-shadow: 0 4px 12px rgba(246, 77, 35, 0.2) !important;
        visibility: visible !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }
    section.main div.stButton > button:hover { background-color: #ff6b4a !important; box-shadow: 0 0 15px #f64d23 !important; }

    /* 6. SELECTBOXES DARK PROFISSIONAIS */
    div[data-baseweb="select"] > div { background-color: #1a242d !important; border: 1px solid #2d3843 !important; }
    div[data-baseweb="select"] * { color: #e2e8f0 !important; font-weight: 400 !important; }
    div[data-testid="stSelectbox"] label p { color: #64748b !important; font-size: 10px !important; text-transform: uppercase; margin-bottom: 2px; }

    /* FOOTER */
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #121212; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #64748b; z-index: 999999; }
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
        <div style="margin-left:auto; display:flex; gap:15px; align-items:center;">
            <div style="border:1px solid #475569; color:white; padding:5px 15px; border-radius:4px; font-size:11px; cursor:pointer;">REGISTRAR</div>
            <div style="background:#00cc66; color:white; padding:7px 20px; border-radius:4px; font-weight:800; font-size:11px; cursor:pointer;">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (ELEVAÇÃO MÁXIMA) ---
with st.sidebar:
    st.button("JOGOS DO DIA")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- CONTEÚDO CENTRAL ---
st.markdown('<div style="color:white; font-weight:900; font-size:24px; margin-bottom:15px; letter-spacing: -0.5px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1: st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
with c2: st.selectbox("CATEGORIA", ["Brasileirão", "Copa do Brasil"])
with c3: st.selectbox("CAMPEONATO", ["Série A", "Série B"])

st.markdown("<hr style='border: 0.1px solid #2d3843; opacity: 0.2; margin: 15px 0;'>", unsafe_allow_html=True)
st.markdown('<div style="color:white; font-weight:700; font-size:16px; margin-bottom:10px;">Confronto: Série A</div>', unsafe_allow_html=True)

t1, t2 = st.columns(2)
with t1: st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "Botafogo"])
with t2: st.selectbox("TIME FORA", ["Flamengo", "Vasco", "Palmeiras"])

# BOTÃO EXECUTAR (LARANJA BLINDADO E PROPORCIONAL)
if st.button("EXECUTAR ALGORITMO"):
    with st.status("GIAE IA: Processando...", expanded=False):
        time.sleep(1)
    st.success("🤖 Análise finalizada!")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN V15.0</div><div>GESTOR IA PRO v15.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
