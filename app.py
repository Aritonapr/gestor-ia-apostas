import streamlit as st
import time
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v57.23 - PROTEÇÃO ATIVA JARVIS]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO POR SESSION_STATE + GATILHO LOGO HOME (FIXED)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO)
# DIRETRIZ 5: EXPANSÃO TOTAL DE COLUNAS (SEM PONTO E VÍRGULA OU INLINE)
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
    
    /* HEADER PREMIUM (BARRA AZUL FIXA) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 999999; 
        transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    
    /* POSICIONAMENTO DOS MENUS PARA NÃO BATER NO LOGO */
    .nav-links-container {
        position: fixed; top: 0; left: 180px; height: 60px;
        display: flex; align-items: center; gap: 18px; z-index: 1000000;
    }
    
    .nav-item { 
        color: #ffffff !important; font-size: 8.5px !important; 
        text-transform: uppercase; opacity: 0.8; font-weight: 700; 
        letter-spacing: 0.8px; white-space: nowrap; cursor: pointer;
    }

    /* BOTÃO LOGO HOME (FIXADO ABSOLUTAMENTE PARA NÃO QUEBRAR O FLEX) */
    div[data-testid="stSidebar"] div.stButton > button[key="logo_home"] {
        position: fixed !important;
        top: 15px !important;
        left: 40px !important;
        background: transparent !important;
        border: none !important;
        color: #9d54ff !important;
        font-weight: 900 !important;
        font-size: 21px !important;
        text-transform: uppercase !important;
        z-index: 1000001 !important;
        padding: 0 !important;
        width: auto !important;
        box-shadow: none !important;
    }
    
    /* BOTÕES DA DIREITA (FIXADOS) */
    .header-right-container {
        position: fixed; top: 0; right: 40px; height: 60px;
        display: flex; align-items: center; gap: 15px; z-index: 1000000;
    }

    .registrar-pill { 
        color: #ffffff !important; font-size: 9px !important; font-weight: 800; 
        border: 1.5px solid #ffffff !important; padding: 7px 18px !important; 
        border-radius: 20px !important;
    }
    
    .entrar-grad { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: white !important; padding: 8px 22px !important; border-radius: 5px !important; 
        font-weight: 800; font-size: 9.5px;
    }

    /* SIDEBAR NAVIGATION */
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: 10px !important; gap: 0px !important; }
    
    section[data-testid="stSidebar"] div.stButton > button:not([key="logo_home"]) { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: all 0.2s ease !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:not([key="logo_home"]):hover {
        background-color: #1e293b !important; color: #06b6d4 !important; padding-left: 35px !important; border-left: 3px solid #6d28d9 !important;
    }

    /* ZERO WHITE - INPUTS E SLIDERS */
    div[data-baseweb="input"], .stNumberInput div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    div[data-baseweb="input"] input { background-color: #1a202c !important; color: white !important; }
    
    /* KPI CARDS (OS QUADRADOS) */
    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
        transform: translate3d(0,0,0);
    }
    
    /* BANNER TÍTULO GESTÃO (IMAGEM 3) */
    .banca-title-banner {
        background-color: #003399 !important;
        padding: 15px 25px; border-radius: 5px; color: white !important;
        font-size: 24px; font-weight: 800; margin-bottom: 35px;
    }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. [DIRETRIZ 1] HEADER E LOGO HOME
with st.sidebar:
    # 1. Desenha a barra azul e os menus fixos via HTML
    st.markdown("""
        <div class="betano-header"></div>
        <div class="nav-links-container">
            <div class="nav-item">APOSTAS ESPORTIVAS</div>
            <div class="nav-item">APOSTAS AO VIVO</div>
            <div class="nav-item">APOSTAS ENCONTRADAS</div>
            <div class="nav-item">ESTATÍSTICAS AVANÇADAS</div>
            <div class="nav-item">MERCADO PROBABILÍSTICO</div>
            <div class="nav-item">ASSERTIVIDADE IA</div>
        </div>
        <div class="header-right-container">
            <div style="color:white; font-size:15px;">🔍</div>
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    """, unsafe_allow_html=True)
    
    # 2. Insere o botão LOGO (ele será posicionado pelo CSS key="logo_home")
    if st.button("GESTOR IA", key="logo_home"):
        st.session_state.aba_ativa = "home"
        st.rerun()

    st.markdown('<div style="height:60px;"></div>', unsafe_allow_html=True)

    # --- INICIALIZAÇÃO DE MEMÓRIA ---
    if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
    if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
    if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
    if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
    if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
    if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

    # --- NAVEGAÇÃO LATERAL ---
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

# FUNÇÃO CARD GENÉRICA
def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;">
                <div style="background:{color_footer}; height:100%; width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- LÓGICA DE TELAS ---

# TELA 1: HOME (IMAGEM 1)
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1:
        draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2:
        draw_card("ASSERTIVIDADE", "92.4%", 92)
    with h3:
        draw_card("SUGESTÃO", "OVER 2.5", 88)
    with h4:
        draw_card("IA STATUS", "ONLINE", 100)
    
    h5, h6, h7, h8 = st.columns(4)
    with h5:
        draw_card("VOL. GLOBAL", "ALTO", 75)
    with h6:
        draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with h7:
        draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
    with h8:
        draw_card("SISTEMA", "JARVIS v57.23", 100)

# TELA 2: GESTÃO DE BANCA PRO (IMAGEM 3)
elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>""", unsafe_allow_html=True)
    col_in, col_dis = st.columns([1.2, 2.5])
    with col_in:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
        st.session_state.stake_padrao = st.slider("STAKE POR OPERAÇÃO (%)", 0.1, 10.0, st.session_state.stake_padrao)
        st.session_state.meta_diaria = st.slider("META DIÁRIA - STOP GAIN (%)", 1.0, 30.0, st.session_state.meta_diaria)
        st.session_state.stop_loss = st.slider("LIMITE DE PERDA - STOP LOSS (%)", 1.0, 30.0, st.session_state.stop_loss)

    vs = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    vm = (st.session_state.banca_total * st.session_state.meta_diaria / 100)
    vl = (st.session_state.banca_total * st.session_state.stop_loss / 100)
    
    with col_dis:
        g1, g2, g3, g4 = st.columns(4)
        with g1:
            draw_card("VALOR ENTRADA", f"R$ {vs:,.2f}", 100, "#00d2ff")
        with g2:
            draw_card("STOP GAIN (R$)", f"R$ {vm:,.2f}", 100, "#00d2ff")
        with g3:
            draw_card("STOP LOSS (R$)", f"R$ {vl:,.2f}", 100, "#00d2ff")
        with g4:
            draw_card("ALVO FINAL", f"R$ {(st.session_state.banca_total + vm):,.2f}", 100, "#00d2ff")
        g5, g6, g7, g8 = st.columns(4)
        with g5:
            draw_card("RISCO TOTAL", f"{st.session_state.stake_padrao}%", 100, "#00d2ff")
        with g6:
            draw_card("ENTRADAS/META", f"{int(vm/vs) if vs > 0 else 0}", 100, "#00d2ff")
        with g7:
            draw_card("ENTRADAS/LOSS", f"{int(vl/vs) if vs > 0 else 0}", 100, "#00d2ff")
        with g8:
            draw_card("SAÚDE BANCA", "EXCELENTE", 100, "#00d2ff")

# TELA 3: SCANNER PRÉ-LIVE (IMAGEM 2)
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    st.markdown('<div style="background: linear-gradient(90deg, #6d28d9, #06b6d4); padding: 15px; border-radius: 5px; text-align: center; color: white; font-weight: bold; margin-bottom: 25px;">⚡ EXECUTAR ALGORITIMO</div>', unsafe_allow_html=True)
    st.markdown("### RESULTADO: Flamengo vs Palmeiras")
    r1, r2, r3, r4 = st.columns(4)
    with r1: draw_card("VENCEDOR", "Casa", 85)
    with r2: draw_card("GOLS", "OVER 1.5", 70)
    with r3: draw_card("STAKE", "R$ 10.00", 100)
    with r4: draw_card("CANTOS", "9.5+", 65)
    r5, r6, r7, r8 = st.columns(4)
    with r5: draw_card("IA CONF.", "94%", 94)
    with r6: draw_card("PRESSÃO", "ALTA", 88)
    with r7: draw_card("TENDÊNCIA", "SUBINDO", 60)
    with r8: draw_card("SISTEMA", "v57.23", 100)

# TELAS RESTANTES
else:
    st.info(f"Módulo {st.session_state.aba_ativa.upper()} em desenvolvimento...")

# FOOTER
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.23</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
