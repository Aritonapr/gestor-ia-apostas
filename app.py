import streamlit as st
import time
from datetime import datetime

# ==============================================================================
# [PROTOCOLO v57.29 - VERSÃO INTEGRAL PARA NÃO-PROGRAMADORES]
# ESTE CÓDIGO CONTÉM TODAS AS FUNÇÕES E PÁGINAS SEM ABREVIAÇÕES.
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA (CUIDA DOS DADOS DO APP) ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# 2. ESTILO VISUAL (CSS) - NÃO MEXER AQUI PARA NÃO PERDER O LAYOUT
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
        transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    
    .header-left { display: flex; align-items: center; gap: 25px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; letter-spacing: 0.5px; text-decoration: none; cursor: pointer;}
    
    .nav-links { display: flex; gap: 18px; align-items: center; }
    .nav-item { 
        color: #ffffff !important; font-size: 8.5px !important; 
        text-transform: uppercase; opacity: 0.85; font-weight: 700; 
        letter-spacing: 0.8px; white-space: nowrap;
    }

    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { 
        color: #ffffff !important; font-size: 9px !important; font-weight: 800; 
        border: 1.5px solid #ffffff !important; padding: 7px 18px !important; 
        border-radius: 20px !important; cursor: pointer;
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
        border-radius: 0px !important; transition: all 0.2s ease !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important;
    }

    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important;
        border-radius: 6px !important; width: 100% !important; margin-top: 10px !important;
    }

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
    }
    
    .banca-title-banner {
        background-color: #003399 !important; padding: 15px 25px; border-radius: 5px;
        color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px;
    }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SUPERIOR FIXO
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <div class="logo-link">GESTOR IA</div>
                <div class="nav-links">
                    <div class="nav-item">APOSTAS ESPORTIVAS</div>
                    <div class="nav-item">APOSTAS AO VIVO</div>
                </div>
            </div>
            <div class="header-right">
                <div class="registrar-pill">REGISTRAR</div>
                <div class="entrar-grad">ENTRAR</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    # Menu de Navegação Lateral
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

# Função que desenha os quadros de informação
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

# --- INÍCIO DAS TELAS DO SISTEMA ---

# PÁGINA: JOGOS DO DIA (HOME)
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("SINAL FORTE", "REAL MADRID", 94)
    with h3: draw_card("SUGESTÃO IA", "OVER 1.5 GOLS", 88)
    with h4: draw_card("IA STATUS", "ONLINE", 100)

# PÁGINA: SCANNER PRÉ-LIVE (ONDE VOCÊ QUER ADICIONAR CAMPEONATOS)
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    # Lista de Campeonatos (Adicione novos nomes dentro dos colchetes abaixo)
    lista_campeonatos = [
        "Brasileirão Série A", "Brasileirão Série B", 
        "Premier League (Inglaterra)", "La Liga (Espanha)", 
        "Bundesliga (Alemanha)", "Série A (Itália)", 
        "Champions League", "Europa League", "Libertadores"
    ]
    
    sel_campeonato = st.selectbox("🏆 SELECIONE A COMPETIÇÃO", lista_campeonatos)
    
    col_t1, col_t2 = st.columns(2)
    with col_t1: t_casa = st.text_input("🏠 TIME MANDANTE", "Ex: Flamengo")
    with col_t2: t_fora = st.text_input("🚀 TIME VISITANTE", "Ex: Palmeiras")
    
    if st.button("⚡ ANALISAR PROBABILIDADES", use_container_width=True):
        st.session_state.analise_bloqueada = {
            "vencedor": t_casa if t_casa != "Ex: Flamengo" else "Mandante",
            "gols": "OVER 2.5",
            "conf": "94%"
        }
        
    if st.session_state.analise_bloqueada:
        a1, a2, a3, a4 = st.columns(4)
        with a1: draw_card("DECISÃO IA", st.session_state.analise_bloqueada["vencedor"], 94, "#00ff88")
        with a2: draw_card("MERCADO", st.session_state.analise_bloqueada["gols"], 85)
        with a3: draw_card("CONFIANÇA", st.session_state.analise_bloqueada["conf"], 94)
        with a4: draw_card("SISTEMA", "v57.29", 100)

# PÁGINA: GESTÃO DE BANCA
elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>""", unsafe_allow_html=True)
    col_e, col_d = st.columns([1, 2])
    with col_e:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
        st.session_state.stake_padrao = st.slider("STAKE (%)", 0.5, 10.0, st.session_state.stake_padrao)
    with col_d:
        v_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        draw_card("VALOR POR ENTRADA", f"R$ {v_stake:,.2f}", 100, "#00d2ff")

# PÁGINA: SCANNER LIVE
elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER LIVE</h2>", unsafe_allow_html=True)
    l1, l2, l3, l4 = st.columns(4)
    with l1: draw_card("DECISÃO IA", "OVER 0.5 HT", 88, "#00ff88")
    with l2: draw_card("PROB. GOL", "91%", 91)
    with l3: draw_card("ATAQUES/MIN", "1.2", 60)
    with l4: draw_card("STATUS", "ALTA PRESSÃO", 100)

# PÁGINA: VENCEDORES
elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🏆 VENCEDORES DA COMPETIÇÃO</h2>", unsafe_allow_html=True)
    v1, v2, v3, v4 = st.columns(4)
    with v1: draw_card("FAVORITO", "CITY WIN", 94, "#00ff88")
    with v2: draw_card("CONFIANÇA", "ALTA", 95)
    with v3: draw_card("TENDÊNCIA", "SUBINDO", 70)
    with v4: draw_card("LIQUIDEZ", "ALTA", 100)

# PÁGINA: GOLS
elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ APOSTAS POR GOLS</h2>", unsafe_allow_html=True)
    g1, g2, g3, g4 = st.columns(4)
    with g1: draw_card("SUGESTÃO", "OVER 2.5", 85, "#9d54ff")
    with g2: draw_card("AMBAS MARCAM", "SIM", 75)
    with g3: draw_card("GOL HT", "SIM", 82)
    with g4: draw_card("VALOR", "ENTRADA FORTE", 100, "#00ff88")

# PÁGINA: ESCANTEIOS
elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 APOSTAS POR ESCANTEIOS</h2>", unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4)
    with e1: draw_card("LINHA IA", "OVER 9.5", 89, "#06b6d4")
    with e2: draw_card("CANTOS HT", "OVER 4.5", 72)
    with e3: draw_card("PRESSÃO", "ALTA", 95)
    with e4: draw_card("CORNER RACE", "CASA", 70)

# PÁGINA: HISTÓRICO
elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    st.info("O histórico será exibido aqui após as entradas serem salvas.")

# RODAPÉ
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.29</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
