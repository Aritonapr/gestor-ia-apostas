import streamlit as st
import time

# ==============================================================================
# [PROTOCOLO DE RECUPERAÇÃO GIAE-V17-ELITE-RECOVERY]
# RESTAURAÇÃO DE ESTRUTURA LATERAL (SIDEBAR LIST)
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CSS DE ALTA PRECISÃO (ESTRUTURA DA IMAGEM) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap');

    /* Fundo e Geral */
    .stApp { background-color: #0b0e11 !important; color: white !important; }
    header, [data-testid="stHeader"] { display: none !important; }

    /* NAVBAR SUPERIOR FIXA */
    .nav-bar {
        position: fixed; top: 0; left: 0; width: 100%; height: 55px;
        background-color: #0b0e11 !important;
        display: flex; align-items: center; padding: 0 25px;
        border-bottom: 1px solid #1e293b; z-index: 9999;
    }
    .logo { font-weight: 900; font-size: 20px; color: white; margin-right: 35px; }
    .nav-links { display: flex; gap: 20px; font-size: 10px; color: #94a3b8; font-weight: 600; text-transform: uppercase; }

    /* LADO ESQUERDO (SIDEBAR) - AJUSTE FINO CONFORME IMAGEM */
    [data-testid="stSidebar"] {
        background-color: #0b0e11 !important;
        border-right: 1px solid #1e293b !important;
        padding-top: 20px !important;
    }
    /* Remover espaços vazios do Streamlit na sidebar */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0px !important; padding: 0px !important;
    }

    /* ESTILO LISTA LATERAL (BOTÕES) */
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        border: none !important;
        border-bottom: 1px solid #1a202c !important; /* Linha separadora da imagem */
        color: #94a3b8 !important;
        border-radius: 0px !important;
        width: 100% !important;
        text-align: left !important;
        justify-content: flex-start !important;
        padding: 18px 25px !important; /* Espaçamento vertical da imagem */
        font-size: 11px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px;
    }
    [data-testid="stSidebar"] button:hover {
        color: #ffffff !important;
        background-color: #161b22 !important;
    }

    /* ÁREA CENTRAL - FILTROS */
    div[data-baseweb="select"] > div {
        background-color: #161b22 !important;
        border: 1px solid #2d3748 !important;
    }
    label { 
        color: #475569 !important; 
        font-size: 10px !important; 
        font-weight: 700 !important; 
        text-transform: uppercase !important;
        margin-bottom: 8px !important;
    }

    /* BOTÃO EXECUTAR (BRANCO CONFORME IMAGEM) */
    div.stButton > button {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 12px !important;
        padding: 10px 25px !important;
        border-radius: 6px !important;
        border: none !important;
        margin-top: 10px;
    }

    /* FOOTER */
    .footer-status {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: #000; padding: 6px 20px; font-size: 9px;
        color: #475569; border-top: 1px solid #1e293b;
        display: flex; justify-content: space-between; z-index: 9999;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER FIXO ---
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
            <div style="border: 1px solid #334155; padding: 6px 15px; border-radius: 4px; font-size: 11px; font-weight: 700;">REGISTRADOR</div>
            <div style="background: #00cc66; color: white; padding: 6px 20px; border-radius: 4px; font-size: 11px; font-weight: 800;">ENTRAR</div>
        </div>
    </div>
    <div style="margin-top: 70px;"></div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (LADO ESQUERDO AJUSTADO) ---
with st.sidebar:
    # Espaçamento para alinhar com o topo do conteúdo
    st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)
    st.button("JOGOS DO DIA")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- CONTEÚDO PRINCIPAL ---
st.markdown('<h2 style="font-weight: 900; letter-spacing: -1px; margin-bottom: 25px;">ANÁLISE MÉTRICA DOS JOGOS</h2>', unsafe_allow_html=True)

# Filtros Superiores
c1, c2, c3 = st.columns(3)
with c1: st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
with c2: st.selectbox("CATEGORIA", ["Brasileirão", "Copa do Brasil"])
with c3: st.selectbox("CAMPEONATO", ["Série A", "Série B"])

st.markdown("<br><h4 style='font-size: 15px; font-weight: 800; color: #f8fafc;'>Confronto: Série A</h4>", unsafe_allow_html=True)

# Seleção de Times
t1, t2 = st.columns(2)
with t1: st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "Botafogo"])
with t2: st.selectbox("TIME FORA", ["Flamengo", "Vasco", "Palmeiras"])

# Botão Executar (Estilizado Branco conforme print)
st.button("EXECUTAR ALGORITMO")

# --- FOOTER STATUS ---
st.markdown("""
    <div class="footer-status">
        <div>STATUS: ● IA OPERACIONAL | DESIGN V17.0 | KEY: GIAE-V17-ELITE-RECOVERY</div>
        <div>GESTOR IA PRO v18.0 | Lado Esquerdo Preservado</div>
    </div>
    """, unsafe_allow_html=True)
