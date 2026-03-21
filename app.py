import streamlit as st
import time
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v57.23 - PROTEÇÃO ATIVA]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADA)
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. [CAMADA DE PROTEÇÃO 1] - CSS INTEGRAL E BLINDADO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* RESET DE SCROLL E FUNDOS */
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }

    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    /* [DIRETRIZ 2] HEADER PREMIUM ORIGINAL */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
        transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    
    .header-left { display: flex; align-items: center; gap: 25px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; letter-spacing: 0.5px; }
    
    .nav-links { display: flex; gap: 18px; align-items: center; }
    .nav-item { 
        color: #ffffff !important; font-size: 8.5px !important; 
        text-transform: uppercase; opacity: 0.85; font-weight: 700; 
        letter-spacing: 0.8px; transition: 0.3s ease; cursor: pointer;
    }

    /* SIDEBAR NAVIGATION */
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important;
    }

    /* [DIRETRIZ 4] ZERO WHITE REFORÇADA - INPUTS */
    div[data-baseweb="input"], .stNumberInput div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    input { background-color: transparent !important; color: white !important; }
    .stNumberInput button { background-color: #1a202c !important; color: white !important; border: none !important; }

    /* ESTILO TÍTULO INTELIGENTE (HIGHLIGHT BLUE) */
    .title-highlight {
        background-color: #0044cc;
        color: white;
        padding: 5px 15px;
        display: inline-block;
        font-weight: 800;
        font-size: 28px;
        border-radius: 4px;
        margin-bottom: 30px;
    }

    /* KPI CARDS ESTILO IMAGEM */
    .kpi-card {
        background: #11151a;
        border: 1px solid #1e293b;
        padding: 20px 10px;
        border-radius: 8px;
        text-align: center;
        height: 140px;
        margin-bottom: 10px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .kpi-label { color: #64748b; font-size: 9px; text-transform: uppercase; font-weight: 600; margin-bottom: 15px; }
    .kpi-value { color: white; font-size: 18px; font-weight: 900; }
    
    /* BARRAS COLORIDAS ABAIXO DOS VALORES */
    .bar-cyan { background: #00d4ff; height: 3px; width: 50px; margin-top: 8px; border-radius: 10px; }
    .bar-purple { background: #9d54ff; height: 3px; width: 50px; margin-top: 8px; border-radius: 10px; }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. [DIRETRIZ 1] HEADER ANCORADO NA SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <div class="logo-link">GESTOR IA</div>
                <div class="nav-links">
                    <div class="nav-item">ESPORTES</div>
                    <div class="nav-item">AO VIVO</div>
                    <div class="nav-item">VIRTUAIS</div>
                    <div class="nav-item">E-SPORTS</div>
                    <div class="nav-item">OPORTUNIDADES IA</div>
                </div>
            </div>
            <div class="header-right">
                <div style="color:white; margin-right:15px; cursor:pointer;">🔍</div>
                <div style="color:white; border:1px solid white; padding:5px 15px; border-radius:20px; font-size:10px; margin-right:10px;">REGISTRAR</div>
                <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:6px 20px; border-radius:5px; font-size:10px; font-weight:800;">ENTRAR</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    # --- MEMÓRIA ---
    if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "gestao"
    if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
    if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
    if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
    if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0
    if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []

    # --- NAVEGAÇÃO ---
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

# FUNÇÃO PARA DESENHAR OS CARDS DA IMAGEM
def draw_kpi(label, value, color_class):
    bar = "bar-cyan" if color_class == "cyan" else "bar-purple"
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="{bar}"></div>
        </div>
    """, unsafe_allow_html=True)

# --- LÓGICA DE TELA: GESTÃO DE BANCA ---
if st.session_state.aba_ativa == "gestao":
    # Título com Highlight Azul
    st.markdown("""<div style='display:flex; align-items:center; gap:15px;'>
                    <span style='font-size:35px;'>💰</span> 
                    <span class="title-highlight">GESTÃO DE BANCA INTELIGENTE</span>
                </div>""", unsafe_allow_html=True)

    # Layout Principal: Esquerda (Inputs) | Direita (Cards)
    col_input, col_kpis = st.columns([1, 2.2])

    with col_input:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total, step=50.0)
        st.write("")
        st.session_state.stake_padrao = st.slider("STAKE POR OPERAÇÃO (%)", 0.1, 10.0, st.session_state.stake_padrao)
        st.write("")
        st.session_state.meta_diaria = st.slider("META DIÁRIA - STOP GAIN (%)", 1.0, 30.0, st.session_state.meta_diaria)
        st.write("")
        st.session_state.stop_loss = st.slider("LIMITE DE PERDA - STOP LOSS (%)", 1.0, 30.0, st.session_state.stop_loss)

    with col_kpis:
        # Cálculos
        v_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        v_meta = (st.session_state.banca_total * st.session_state.meta_diaria / 100)
        v_loss = (st.session_state.banca_total * st.session_state.stop_loss / 100)
        alvo = st.session_state.banca_total + v_meta

        # Linha 1 de Cards
        k1, k2, k3, k4 = st.columns(4)
        with k1: draw_kpi("VALOR ENTRADA", f"R$ {v_stake:,.2f}", "cyan")
        with k2: draw_kpi("STOP GAIN (R$)", f"R$ {v_meta:,.2f}", "cyan")
        with k3: draw_kpi("STOP LOSS (R$)", f"R$ {v_loss:,.2f}", "purple")
        with k4: draw_kpi("ALVO FINAL", f"R$ {alvo:,.2f}", "purple")

        # Linha 2 de Cards
        k5, k6, k7, k8 = st.columns(4)
        with k5: draw_kpi("RISCO TOTAL", f"{st.session_state.stake_padrao}%", "cyan")
        with k6: draw_kpi("ENTRADAS/META", f"{int(v_meta/v_stake) if v_stake > 0 else 0}", "cyan")
        with k7: draw_kpi("ENTRADAS/LOSS", f"{int(v_loss/v_stake) if v_stake > 0 else 0}", "purple")
        with k8: 
            # Card Saúde da Banca Especial
            st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-label">SAÚDE BANCA</div>
                    <div class="kpi-value" style="color:#facc15; font-size:14px;">EXCELENTE</div>
                </div>
            """, unsafe_allow_html=True)

# --- OUTRAS TELAS (MANTENDO SIMETRIA) ---
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    st.selectbox("🏆 VENCEDORES DA COMPETIÇÃO", ["Rodada Atual", "Finais"])
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        st.success("Análise Concluída.")

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    st.info("Histórico pronto para registro.")

# FOOTER
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.23</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
