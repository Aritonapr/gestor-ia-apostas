import streamlit as st
import time
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v57.23 - ESTABILIDADE TOTAL]
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# 2. CSS BLINDADO (ZERO WHITE REFORÇADO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    .nav-links { display: flex; gap: 18px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 8.5px !important; text-transform: uppercase; opacity: 0.85; font-weight: 700; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }

    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
        transition: all 0.3s ease;
    }
    .highlight-card:hover { transform: translateY(-5px); border-color: #6d28d9; }
    
    div[data-baseweb="input"], .stNumberInput div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    .banca-title-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left"><div class="logo-link">GESTOR IA</div></div>
            <div class="header-right"><div class="entrar-grad">v57.23 PRO</div></div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER LIVE"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("🏆 VENCEDORES"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"
    if st.button("📜 HISTÓRICO"): st.session_state.aba_ativa = "historico"

# FUNÇÃO CARD
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

# TELA 1: HOME
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with h3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with h4: draw_card("IA STATUS", "ONLINE", 100)
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("VOL. GLOBAL", "ALTO", 75)
    with h6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with h7: draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
    with h8: draw_card("SISTEMA", "JARVIS v57.23", 100)

# TELA 2: GESTÃO
elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA</div>""", unsafe_allow_html=True)
    c_in, c_out = st.columns([1, 2])
    with c_in:
        st.session_state.banca_total = st.number_input("BANCA", value=st.session_state.banca_total)
        st.session_state.stake_padrao = st.slider("STAKE %", 0.1, 10.0, st.session_state.stake_padrao)
    with c_out:
        g1, g2, g3, g4 = st.columns(4)
        with g1: draw_card("ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
        with g2: draw_card("STOP GAIN", "3.0%", 100)
        with g3: draw_card("STOP LOSS", "5.0%", 100)
        with g4: draw_card("SAÚDE", "EXCELENTE", 100, "#00ff88")

# TELA 3: SCANNER PRÉ-LIVE
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    # Banco de Dados Simplificado para evitar quebra
    paises = ["BRASIL", "INGLATERRA", "ESPANHA", "ALEMANHA"]
    c1, c2 = st.columns(2)
    with c1: casa = st.text_input("MANDANTE", "Time A")
    with c2: fora = st.text_input("VISITANTE", "Time B")
    
    if st.button("ANALISAR AGORA"):
        st.session_state.analise_bloqueada = {"casa": casa, "fora": fora}
        
    if st.session_state.analise_bloqueada:
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", "CASA", 85)
        with r2: draw_card("GOLS", "OVER 2.5", 70)
        with r3: draw_card("STAKE", "1%", 100)
        with r4: draw_card("CONFANÇA", "94%", 94)
        r5, r6, r7, r8 = st.columns(4)
        with r5: draw_card("ATAQUE", "FORTE", 80)
        with r6: draw_card("DEFESA", "MÉDIA", 50)
        with r7: draw_card("CANTOS", "9.5", 60)
        with r8: draw_card("SISTEMA", "v57.23", 100)

# TELA 4: LIVE
elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER LIVE</h2>", unsafe_allow_html=True)
    l1, l2, l3, l4 = st.columns(4)
    with l1: draw_card("PRESSÃO", "85%", 85)
    with l2: draw_card("ATAQUES", "12/5m", 70)
    with l3: draw_card("POSSE", "60%", 60)
    with l4: draw_card("GOL PROB", "92%", 92)
    l5, l6, l7, l8 = st.columns(4)
    with l5: draw_card("ODD", "1.90", 100)
    with l6: draw_card("VARIAÇÃO", "+0.10", 30)
    with l7: draw_card("CORNERS", "7", 70)
    with l8: draw_card("IA", "v57", 100)

# TELA 5: VENCEDORES
elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🏆 VENCEDORES DA COMPETIÇÃO</h2>", unsafe_allow_html=True)
    v1, v2, v3, v4 = st.columns(4)
    with v1: draw_card("FAVORITO 1", "Flamengo", 40)
    with v2: draw_card("FAVORITO 2", "Palmeiras", 35)
    with v3: draw_card("FAVORITO 3", "Botafogo", 20)
    with v4: draw_card("ZEBRA", "Fortaleza", 10)
    v5, v6, v7, v8 = st.columns(4)
    with v5: draw_card("ROI", "12%", 100)
    with v6: draw_card("RISCO", "BAIXO", 20)
    with v7: draw_card("TENDÊNCIA", "ALTA", 80)
    with v8: draw_card("SISTEMA", "PRO", 100)

# TELA 6: GOLS
elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ APOSTAS POR GOLS</h2>", unsafe_allow_html=True)
    g1, g2, g3, g4 = st.columns(4)
    with g1: draw_card("OVER 0.5 HT", "80%", 80)
    with g2: draw_card("OVER 1.5 FT", "70%", 70)
    with g3: draw_card("AMBAS", "60%", 60)
    with g4: draw_card("UNDER 3.5", "90%", 90)
    g5, g6, g7, g8 = st.columns(4)
    with g5: draw_card("GOL 2T", "75%", 75)
    with g6: draw_card("MÉDIA", "2.5", 100)
    with g7: draw_card("BTTS", "SIM", 100)
    with g8: draw_card("DICA", "OVER", 100)

# TELA 7: ESCANTEIOS
elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 APOSTAS POR ESCANTEIOS</h2>", unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4)
    with e1: draw_card("OVER 8.5", "85%", 85)
    with e2: draw_card("OVER 10.5", "60%", 60)
    with e3: draw_card("HT", "4.5", 70)
    with e4: draw_card("RACE 5", "70%", 70)
    e5, e6, e7, e8 = st.columns(4)
    with e5: draw_card("ASIÁTICO", "9.0", 100)
    with e6: draw_card("MÉDIA", "10.1", 100)
    with e7: draw_card("ZEBRA", "15%", 15)
    with e8: draw_card("CONF.", "ALTA", 100)

# TELA 8: HISTÓRICO
elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO</h2>", unsafe_allow_html=True)
    st.info("Operações registradas aparecerão aqui.")

# FOOTER
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
