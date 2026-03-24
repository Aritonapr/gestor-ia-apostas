import streamlit as st
import time
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v57.23 - PROTEÇÃO ATIVA]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO)
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# Redirecionamento Home via Query Params
query_params = st.query_params
if query_params.get("go") == "home":
    st.session_state.aba_ativa = "home"
    st.query_params.clear()

# 2. [CAMADA DE PROTEÇÃO 1] - CSS INTEGRAL E BLINDADO
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
    
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; cursor: pointer;}
    .entrar-grad { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: white !important; padding: 8px 22px !important; border-radius: 5px !important; 
        font-weight: 800; font-size: 9.5px; transition: 0.3s ease; cursor: pointer;
    }

    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: all 0.2s ease !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important;
    }

    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important;
        border-radius: 6px !important; width: 100% !important;
    }

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
    }
    
    .banca-title-banner {
        background-color: #003399 !important; padding: 15px 25px; border-radius: 5px;
        color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px;
    }

    .history-card-box { 
        background: #161b22 !important; border: 1px solid #30363d !important; 
        padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; 
    }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER NA SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <a href="?go=home" class="logo-link">GESTOR IA</a>
            </div>
            <div class="header-right">
                <div class="entrar-grad">IA OPERACIONAL</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    # --- NAVEGAÇÃO ---
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

# FUNÇÃO CARD KPI
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

# TELA 1: HOME (8 CARDS)
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
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>""", unsafe_allow_html=True)
    col_input, col_display = st.columns([1.2, 2.5])
    with col_input:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total, step=50.0)
        st.session_state.stake_padrao = st.slider("STAKE POR OPERAÇÃO (%)", 0.1, 10.0, st.session_state.stake_padrao)
        st.session_state.meta_diaria = st.slider("META DIÁRIA (%)", 1.0, 30.0, st.session_state.meta_diaria)
        st.session_state.stop_loss = st.slider("STOP LOSS (%)", 1.0, 30.0, st.session_state.stop_loss)
    with col_display:
        v_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        g1, g2, g3, g4 = st.columns(4)
        with g1: draw_card("VALOR ENTRADA", f"R$ {v_stake:,.2f}", 100)
        with g2: draw_card("STOP GAIN", f"R$ {(st.session_state.banca_total * st.session_state.meta_diaria / 100):,.2f}", 100)
        with g3: draw_card("STOP LOSS", f"R$ {(st.session_state.banca_total * st.session_state.stop_loss / 100):,.2f}", 100)
        with g4: draw_card("ALVO FINAL", f"R$ {(st.session_state.banca_total * (1 + st.session_state.meta_diaria/100)):,.2f}", 100)
        g5, g6, g7, g8 = st.columns(4)
        with g5: draw_card("RISCO", f"{st.session_state.stake_padrao}%", 100)
        with g6: draw_card("ENTRADAS/META", "3", 100)
        with g7: draw_card("ENTRADAS/LOSS", "5", 100)
        with g8: draw_card("SAÚDE", "EXCELENTE", 100)

# TELA 3: SCANNER PRÉ-LIVE (COMPLETO E REVISADO)
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    db_master = {
        "BRASIL": {
            "BRASILEIRÃO": ["Série A", "Série B", "Série C", "Série D"],
            "REGIONAIS": ["Copa do Nordeste", "Copa Verde"],
            "ESTADUAIS": ["Paulistão", "Carioca", "Mineiro", "Gaúcho", "Paranaense"],
            "COPAS": ["Copa do Brasil", "Supercopa do Brasil"],
            "FEMININO / BASE": ["Brasileiro Fem A1", "Copinha Sub-20", "Brasileiro Sub-20"],
            "TIMES": ["Flamengo", "Palmeiras", "Vasco", "São Paulo", "Corinthians", "Fluminense", "Botafogo", "Grêmio", "Inter", "Atlético-MG"]
        },
        "EUROPA (UEFA)": {
            "CONTINENTAL": ["Champions League", "Europa League", "Conference League"],
            "TIMES": ["Real Madrid", "Man City", "Bayern Munchen", "PSG", "Liverpool", "Inter Milan", "Barcelona", "Arsenal"]
        },
        "INGLATERRA": {
            "LIGA NACIONAL": ["Premier League", "Championship"],
            "COPAS": ["FA Cup", "EFL Cup"],
            "TIMES": ["Man City", "Arsenal", "Liverpool", "Chelsea", "Man United", "Tottenham"]
        },
        "ESPANHA": {
            "LIGA NACIONAL": ["La Liga", "La Liga 2"],
            "COPAS": ["Copa del Rey"],
            "TIMES": ["Real Madrid", "Barcelona", "Atlético Madrid", "Sevilla", "Valencia"]
        },
        "FIFA": {
            "GLOBAL": ["Mundial de Clubes", "Copa do Mundo"],
            "TIMES": ["Time Mundial A", "Time Mundial B"]
        }
    }

    row_filtros = st.columns(3)
    with row_filtros[0]:
        cat_pais = st.selectbox("🌎 CATEGORIA", list(db_master.keys()))
    with row_filtros[1]:
        grupo_opcoes = [k for k in db_master[cat_pais].keys() if k != "TIMES"]
        grupo_sel = st.selectbox("📂 GRUPO", grupo_opcoes)
    with row_filtros[2]:
        competicao = st.selectbox("🏆 COMPETIÇÃO", db_master[cat_pais][grupo_sel])

    st.markdown("<h4 style='color:white;'>⚔️ DEFINIR CONFRONTO</h4>", unsafe_allow_html=True)
    lista_times = db_master[cat_pais]["TIMES"]
    c_casa, c_fora = st.columns(2)
    with c_casa:
        t_casa = st.selectbox("🏠 CASA", lista_times)
    with c_fora:
        # Trava: Time de fora não pode ser igual ao de casa
        lista_fora_filtrada = [t for t in lista_times if t != t_casa]
        t_fora = st.selectbox("🚀 FORA", lista_fora_filtrada)

    if st.button("⚡ EXECUTAR ALGORITMO IA"):
        v_calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        st.session_state.analise_bloqueada = {"casa": t_casa, "fora": t_fora, "vencedor": "Indefinido", "gols": "OVER 2.5", "data": datetime.now().strftime("%H:%M"), "stake_val": f"R$ {v_calc:,.2f}"}
    
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<h3 style='color:#9d54ff; text-align:center;'>RESULTADO: {m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['vencedor'], 85)
        with r2: draw_card("GOLS", m['gols'], 70)
        with r3: draw_card("STAKE", m['stake_val'], 100)
        with r4: draw_card("CANTOS", "9.5+", 65)
        r5, r6, r7, r8 = st.columns(4)
        with r5:
            draw_card("IA CONF.", "94%", 94)
        with r6:
            draw_card("PRESSÃO", "ALTA", 88)
        with r7:
            draw_card("TENDÊNCIA", "SUBINDO", 60)
        with r8:
            draw_card("SISTEMA", "v57.23", 100)

# TELA 4: LIVE (8 CARDS)
elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER LIVE</h2>", unsafe_allow_html=True)
    l1, l2, l3, l4 = st.columns(4)
    with l1: draw_card("PRESSÃO CASA", "88%", 88)
    with l2: draw_card("ATAQUES", "14/5m", 70)
    with l3: draw_card("POSSE", "65%", 65)
    with l4: draw_card("GOL PROB", "90%", 90)
    l5, l6, l7, l8 = st.columns(4)
    with l5: draw_card("ODDS ATUAIS", "1.85", 100)
    with l6: draw_card("VARIAÇÃO", "+0.12", 40)
    with l7: draw_card("CANTOS LIVE", "8", 80)
    with l8: draw_card("STAKE LIVE", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)

# TELA 5: VENCEDORES (8 CARDS)
elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🏆 VENCEDORES DA COMPETIÇÃO</h2>", unsafe_allow_html=True)
    v1, v2, v3, v4 = st.columns(4)
    with v1: draw_card("FAVORITO 1", "Flamengo", 45)
    with v2: draw_card("FAVORITO 2", "Palmeiras", 38)
    with v3: draw_card("FAVORITO 3", "Botafogo", 25)
    with v4: draw_card("ZEBRA PROB", "Fortaleza", 12)
    v5, v6, v7, v8 = st.columns(4)
    with v5: draw_card("ROI MÉDIO", "12.4%", 100)
    with v6: draw_card("VOLATILIDADE", "BAIXA", 20)
    with v7: draw_card("TENDÊNCIA", "ESTÁVEL", 50)
    with v8: draw_card("LIQUIDEZ", "ALTA", 90)

# TELA 6: GOLS (8 CARDS)
elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ APOSTAS POR GOLS</h2>", unsafe_allow_html=True)
    g1, g2, g3, g4 = st.columns(4)
    with g1: draw_card("OVER 0.5 HT", "82%", 82)
    with g2: draw_card("OVER 1.5 FT", "75%", 75)
    with g3: draw_card("AMBAS MARCAM", "61%", 61)
    with g4: draw_card("UNDER 3.5", "90%", 90)
    g5, g6, g7, g8 = st.columns(4)
    with g5: draw_card("UNDER 1.5 HT", "65%", 65)
    with g6: draw_card("OVER 2.5 FT", "54%", 54)
    with g7: draw_card("BTTS NO", "39%", 39)
    with g8: draw_card("IA GOLS", "v2.0", 100)

# TELA 7: ESCANTEIOS (8 CARDS)
elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 APOSTAS POR ESCANTEIOS</h2>", unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4)
    with e1: draw_card("OVER 8.5", "88%", 88)
    with e2: draw_card("OVER 10.5", "62%", 62)
    with e3: draw_card("CANTOS HT", "4.5+", 70)
    with e4: draw_card("RACE", "Time A", 55)
    e5, e6, e7, e8 = st.columns(4)
    with e5: draw_card("RACE TO 5", "72%", 72)
    with e6: draw_card("OVER 12.5", "18%", 18)
    with e7: draw_card("UNDER 7.5", "12%", 12)
    with e8: draw_card("ASIÁTICOS", "9.0", 100)

# HISTÓRICO
elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    if not st.session_state.historico_calls:
        st.info("Nenhuma operação registrada.")
    else:
        for i, call in enumerate(reversed(st.session_state.historico_calls)):
            st.markdown(f"""<div class="history-card-box"><div style="color:white; font-weight:800;">{call['casa']} x {call['fora']} | {call['gols']}</div></div>""", unsafe_allow_html=True)

# FOOTER
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.23</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
