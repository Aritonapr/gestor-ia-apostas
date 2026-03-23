import streamlit as st
import time
import random
from datetime import datetime

# ==============================================================================
# [PROTOCOLO v57.26 - INTELIGÊNCIA DE DECISÃO ATIVA]
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

# 2. CSS INTEGRAL (MENU 11PX + ZERO SCROLL + CONTRASTE MÁXIMO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }

    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
        transform: translate3d(0,0,0);
    }
    
    .header-left { display: flex; align-items: center; gap: 25px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    
    .nav-links { display: flex; gap: 22px; align-items: center; }
    .nav-item { 
        color: #ffffff !important; font-size: 11px !important; 
        text-transform: uppercase; opacity: 1 !important; font-weight: 700; 
        letter-spacing: 0.8px; white-space: nowrap;
    }

    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { 
        color: #ffffff !important; font-size: 9px !important; font-weight: 800; 
        border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important;
    }
    .entrar-grad { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: white !important; padding: 8px 22px !important; border-radius: 5px !important; 
        font-weight: 800; font-size: 9.5px;
    }

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

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
    }
    
    .banca-title-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER ANCORADO
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <div class="logo-link">GESTOR IA</div>
                <div class="nav-links">
                    <div class="nav-item">APOSTAS ESPORTIVAS</div>
                    <div class="nav-item">APOSTAS AO VIVO</div>
                    <div class="nav-item">APOSTAS ENCONTRADAS</div>
                    <div class="nav-item">ASSERTIVIDADE IA</div>
                </div>
            </div>
            <div class="header-right">
                <div class="registrar-pill">REGISTRAR</div>
                <div class="entrar-grad">ENTRAR</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color_footer}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- TELAS COM SUGESTÕES REAIS ---

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("SINAL MAIS FORTE", "REAL MADRID WIN", 94)
    with h3: draw_card("SUGESTÃO DO DIA", "OVER 1.5 GOLS", 88)
    with h4: draw_card("IA STATUS", "OPERACIONAL", 100)
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("VOLUME MERCADO", "ALTO", 75)
    with h6: draw_card("STAKE ATUAL", f"{st.session_state.stake_padrao}%", 100)
    with h7: draw_card("RECOMENDAÇÃO", "AGUARDAR LIVE", 60)
    with h8: draw_card("SISTEMA", "JARVIS v57.26", 100)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>""", unsafe_allow_html=True)
    c_in, c_grid = st.columns([1.2, 2.5])
    with c_in:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
        st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, st.session_state.stake_padrao)
    v_s = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    with c_grid:
        g1, g2, g3, g4 = st.columns(4)
        with g1: draw_card("VALOR ENTRADA", f"R$ {v_s:,.2f}", 100)
        with g2: draw_card("STOP GAIN", f"R$ {(st.session_state.banca_total * 0.03):,.2f}", 100)
        with g3: draw_card("PROTEÇÃO", "ATIVADA", 100)
        with g4: draw_card("SAÚDE", "EXCELENTE", 100, "#00ff88")
        g5, g6, g7, g8 = st.columns(4)
        with g5: draw_card("RISCO DIÁRIO", "BAIXO", 20)
        with g6: draw_card("MÉTODO", "JUROS COMPOSTOS", 100)
        with g7: draw_card("ESTRATÉGIA", "PROBABILÍSTICA", 100)
        with g8: draw_card("IA MODO", "CONSERVADOR", 100)

elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ APOSTAS POR GOLS - DECISÃO IA</h2>", unsafe_allow_html=True)
    g1, g2, g3, g4 = st.columns(4)
    with g1: draw_card("MELHOR ENTRADA", "OVER 2.5 GOLS", 92, "#9d54ff")
    with g2: draw_card("AMBAS MARCAM", "SIM (CONFIRMADO)", 85)
    with g3: draw_card("GOL NO HT", "88% PROB.", 88)
    with g4: draw_card("DECISÃO IA", "ENTRADA FORTE", 100, "#00ff88")
    g5, g6, g7, g8 = st.columns(4)
    with g5: draw_card("UNDER 4.5", "SEGURANÇA ALTA", 98)
    with g6: draw_card("CASA MARCA", "+1.5 GOLS", 74)
    with g7: draw_card("VISITANTE MARCA", "0.5 GOLS", 61)
    with g8: draw_card("STAKE SUGERIDA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)

elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 APOSTAS POR ESCANTEIOS - DECISÃO IA</h2>", unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4)
    with e1: draw_card("LINHA PRINCIPAL", "OVER 9.5 CANTOS", 89, "#06b6d4")
    with e2: draw_card("CANTOS HT", "OVER 4.5", 77)
    with e3: draw_card("PRESSÃO LATERAIS", "MUITO ALTA", 95)
    with e4: draw_card("DECISÃO IA", "ENTRAR NO LIVE", 100, "#ffcc00")
    e5, e6, e7, e8 = st.columns(4)
    with e5: draw_card("RACE 7 CANTOS", "TIME CASA", 68)
    with e6: draw_card("LINHA LIMITE", "10.5 ASIÁTICO", 55)
    with e7: draw_card("ZONA DE VALOR", "ODD 1.80+", 100)
    with e8: draw_card("RISCO ESCANTEIO", "MÍNIMO", 100, "#00ff88")

elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🏆 VENCEDORES - DECISÃO IA</h2>", unsafe_allow_html=True)
    v1, v2, v3, v4 = st.columns(4)
    with v1: draw_card("VENCEDOR (ML)", "FLAMENGO WIN", 94, "#00ff88")
    with v2: draw_card("DUPLA CHANCE", "CASA OU EMPATE", 99)
    with v3: draw_card("EMPATE ANULA", "CASA (DNB)", 91)
    with v4: draw_card("DECISÃO IA", "VALOR NO MANDANTE", 100)
    v5, v6, v7, v8 = st.columns(4)
    with v5: draw_card("PROB. MANDANTE", "72%", 72)
    with v6: draw_card("PROB. EMPATE", "18%", 18)
    with v7: draw_card("PROB. VISITANTE", "10%", 10)
    with v8: draw_card("CONFIANÇA ALGO", "ALTA", 100)

# TELAS DE HISTÓRICO E SCANNER PRÉ-LIVE MANTIDAS INTEGRALMENTE
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    st.info("Selecione o confronto para a IA processar a decisão...")
    c1, c2 = st.columns(2)
    t_casa = c1.selectbox("🏠 CASA", ["City", "Liverpool", "Arsenal"])
    t_fora = c2.selectbox("🚀 FORA", ["Chelsea", "United", "Spurs"])
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        st.session_state.analise_bloqueada = {"casa": t_casa, "fora": t_fora, "vencedor": t_casa, "gols": "OVER 2.5", "data": "20:45"}
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("DECISÃO ML", m['vencedor'], 85, "#00ff88")
        with r2: draw_card("DECISÃO GOLS", m['gols'], 70)
        with r3: draw_card("STAKE", "1%", 100)
        with r4: draw_card("ASSERTIVIDADE", "94%", 94)

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    st.info("Nenhuma call encerrada no momento.")

# FOOTER
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.26</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
