import streamlit as st
import time

# ==============================================================================
# [GIAE KERNEL SHIELD v18.0 - PROTOCOLO CRIZAL REFINED]
# ESTADO: ATIVO (LOGO ROXO | NAVBAR COMPLETA | SUBTITULO BRANCO)
# CHAVE DE RECONHECIMENTO: GIAE-V17-ELITE-RECOVERY
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- BLOCO DE SEGURANÇA CSS (PALETA CRIZAL ATUALIZADA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');

    /* [01] RESET E FUNDO GERAL */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { 
        display: none !important; visibility: hidden !important; 
    }
    .stApp { background-color: #0b0e11 !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; padding-top: 0px !important; }

    /* [02] NAVBAR SUPERIOR (ESTRUTURA COMPLETA) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 55px; 
        background-color: #0d0d12 !important; 
        border-bottom: 1px solid #1e293b !important; 
        display: flex; align-items: center; 
        padding: 0 40px !important; 
        z-index: 999999; 
    }
    /* LOGO GESTOR IA EM ROXO HARMÔNICO (CRIZAL) */
    .logo-text { 
        color: #9d54ff !important; 
        font-weight: 900; font-size: 20px; 
        text-transform: uppercase; margin-right: 40px; 
        letter-spacing: -1px; 
    }
    .nav-items { 
        display: flex; gap: 20px; flex-grow: 1; 
        color: #ffffff !important; 
        font-size: 10px !important; 
        font-weight: 600 !important;
        text-transform: uppercase; 
        letter-spacing: 0.8px; 
    }

    /* ELEMENTOS DA DIREITA (LUPA, REGISTRAR, ENTRAR) */
    .header-right {
        display: flex; align-items: center; gap: 20px;
    }
    .search-icon { color: #ffffff; cursor: pointer; font-size: 16px; }
    .registrar-text { 
        color: #ffffff; font-size: 11px; font-weight: 700; 
        text-transform: uppercase; cursor: pointer;
    }
    .entrar-btn {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%);
        color: white; padding: 8px 22px; border-radius: 4px;
        font-weight: 800; font-size: 11px; cursor: pointer;
        text-transform: uppercase;
    }

    /* [03] SIDEBAR (GRAFITE PROTEGIDO) */
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        border-right: 1px solid #1e293b !important;
        margin-top: 50px !important;
    }
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        color: #94a3b8 !important;
        border: none !important;
        border-bottom: 1px solid #1a202c !important;
        border-radius: 0px !important;
        text-align: left !important;
        justify-content: flex-start !important;
        width: 100% !important;
        padding: 15px 20px !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
    }
    [data-testid="stSidebar"] button:hover { 
        color: #ffffff !important; 
        background: linear-gradient(90deg, rgba(109,40,217,0.2) 0%, rgba(6,182,212,0.1) 100%) !important;
        border-left: 4px solid #6d28d9 !important; 
    }

    /* [04] BOTÃO EXECUTAR (CRIZAL GRADIENTE) */
    section.main div.stButton > button {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important;
        border-radius: 6px !important;
        height: 40px !important; 
        width: 220px !important; 
        font-weight: 800 !important;
        font-size: 12px !important;
        text-transform: uppercase !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important;
    }

    /* SELECTS */
    div[data-baseweb="select"] > div { background-color: #1a1b23 !important; border: 1px solid #2d3843 !important; }
    div[data-baseweb="select"] * { color: #e2e8f0 !important; }

    /* FOOTER */
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- ESTRUTURA NAVBAR ATUALIZADA ---
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
        <div class="header-right">
            <div class="search-icon">🔍</div>
            <div class="registrar-text">REGISTRAR</div>
            <div class="entrar-btn">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (CONTEÚDO) ---
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
st.markdown('<div style="height: 60px;"></div>', unsafe_allow_html=True)
st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:5px; letter-spacing: -1px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
# MANTIDO EM BRANCO CONFORME SOLICITADO
st.markdown('<div style="color:#ffffff; font-size:10px; font-weight:700; margin-bottom:25px; text-transform:uppercase; opacity: 0.8;">Protocolo de Análise Crizal Active</div>', unsafe_allow_html=True)

# Filtros
c1, c2, c3 = st.columns(3)
with c1: st.selectbox("REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
with c2: st.selectbox("CATEGORIA", ["Brasileirão", "Copa do Brasil"])
with c3: st.selectbox("CAMPEONATO", ["Série A", "Série B"])

st.markdown("<hr style='border: 0.1px solid #1e293b; margin: 20px 0;'>", unsafe_allow_html=True)

# Seleção de Times
t1, t2 = st.columns(2)
with t1: st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "Botafogo"])
with t2: st.selectbox("TIME FORA", ["Flamengo", "Vasco", "Palmeiras"])

# Botão Executar
if st.button("EXECUTAR ALGORITMO GIAE"):
    st.toast("Calculando Probabilidades Crizal...", icon="🔮")
    time.sleep(1)
    st.success("Análise Metrics Concluída!")

# FOOTER PROTEGIDO
st.markdown("""<div class="betano-footer"><div>STATUS: <span style="color:#06b6d4;">● IA OPERACIONAL</span> | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v18.0 | CRIZAL HARMONY DESIGN</div></div>""", unsafe_allow_html=True)
