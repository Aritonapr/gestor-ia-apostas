import streamlit as st

# ==============================================================================
# [SISTEMA DE SEGURANÇA GIAE-V17-ELITE-RECOVERY] - ESTADO: TRAVADO
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CSS CIRÚRGICO PARA EVITAR QUEBRAS ---
st.markdown("""
    <style>
    /* 1. RESET DE PADDING E MARGENS NATIVAS */
    [data-testid="stAppViewBlockContainer"] {
        padding-top: 4rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
        max-width: 100%;
    }
    [data-testid="stHeader"] { display: none !important; }
    [data-testid="stSidebarContent"] { padding-top: 0rem !important; }
    .stApp { background-color: #0b0e11 !important; }

    /* 2. NAVBAR SUPERIOR (FIXA E SEM QUEBRA) */
    .nav-bar {
        position: fixed; top: 0; left: 0; width: 100%; height: 55px;
        background-color: #000000; display: flex; align-items: center;
        padding: 0 30px; border-bottom: 1px solid #1e293b; z-index: 999999;
    }
    .logo { font-weight: 900; font-size: 20px; color: white; margin-right: 40px; }
    .nav-links { display: flex; gap: 20px; font-size: 10px; color: #cbd5e1; text-transform: uppercase; font-weight: 600; }
    
    /* 3. LADO ESQUERDO (SIDEBAR) - IDENTICO À IMAGEM */
    [data-testid="stSidebar"] {
        background-color: #0b0e11 !important;
        border-right: 1px solid #1e293b !important;
        width: 260px !important;
    }
    /* Estilo dos itens da lista lateral */
    .side-item {
        color: #94a3b8;
        padding: 15px 25px;
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        border-bottom: 1px solid #1a202c;
        cursor: pointer;
        display: block;
        text-decoration: none;
    }
    .side-item:hover {
        background-color: #161b22;
        color: white;
    }

    /* 4. BOTÃO EXECUTAR (BRANCO) */
    div.stButton > button {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-weight: 800 !important;
        border-radius: 4px !important;
        padding: 10px 30px !important;
        border: none !important;
        text-transform: uppercase;
        font-size: 12px;
    }

    /* 5. FOOTER FIXO */
    .footer-status {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: #000; padding: 6px 20px; font-size: 9px;
        color: #475569; border-top: 1px solid #1e293b;
        display: flex; justify-content: space-between; z-index: 999999;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ESTRUTURA HTML DA NAVBAR ---
st.markdown("""
    <div class="nav-bar">
        <div class="logo">GESTOR IA</div>
        <div class="nav-links">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Estatísticas Avançadas</span>
            <span>Mercado Probabilístico</span>
            <span>Assertividade IA</span>
        </div>
        <div style="margin-left: auto; display: flex; gap: 10px;">
            <div style="border: 1px solid #334155; padding: 6px 15px; border-radius: 4px; font-size: 10px; font-weight: 700; color:white;">REGISTRADOR</div>
            <div style="background: #00cc66; color: white; padding: 6px 20px; border-radius: 4px; font-size: 10px; font-weight: 800;">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- LADO ESQUERDO (SIDEBAR) ---
with st.sidebar:
    st.markdown('<div style="height: 60px;"></div>', unsafe_allow_html=True) # Espaço para a navbar
    menus = [
        "JOGOS DO DIA", "PRÓXIMOS JOGOS", "VENCEDORES DA COMPETIÇÃO",
        "APOSTAS POR ODDS", "APOSTAS POR GOLS", "APOSTAS POR ESCANTEIOS",
        "APOSTAS POR CARTÕES", "ÁRBITRO DA PARTIDA"
    ]
    for m in menus:
        st.markdown(f'<a class="side-item">{m}</a>', unsafe_allow_html=True)

# --- CONTEÚDO CENTRAL ---
st.markdown('<h2 style="font-weight: 900; letter-spacing: -1px; margin-top: 20px;">ANÁLISE MÉTRICA DOS JOGOS</h2>', unsafe_allow_html=True)

# Filtros em Colunas
c1, c2, c3 = st.columns(3)
with c1: st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
with c2: st.selectbox("CATEGORIA", ["Brasileirão", "Copa do Brasil"])
with c3: st.selectbox("CAMPEONATO", ["Série A", "Série B"])

st.markdown("<br><h4 style='font-size: 15px; font-weight: 800;'>Confronto: Série A</h4>", unsafe_allow_html=True)

# Times
t1, t2 = st.columns(2)
with t1: st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "Botafogo"])
with t2: st.selectbox("TIME FORA", ["Flamengo", "Vasco", "Palmeiras"])

# Botão Executar
st.button("EXECUTAR ALGORITMO")

# --- FOOTER ---
st.markdown("""
    <div class="footer-status">
        <div>STATUS: ● IA OPERACIONAL | DESIGN V17.0 | KEY: GIAE-V17-ELITE-RECOVERY</div>
        <div>GESTOR IA PRO v18.0</div>
    </div>
    """, unsafe_allow_html=True)
