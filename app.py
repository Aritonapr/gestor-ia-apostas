import streamlit as st
import time
import random
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v57.23 - PROTEÇÃO ATIVA]
# DIRETRIZ 1: HEADER DEVE FICAR DENTRO DA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. [CAMADA DE PROTEÇÃO 1] - CSS DE PERSISTÊNCIA ABSOLUTA (ANTI-FLICKER + DARK MODE FIX)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');
    
    /* BLOQUEIO DE FUNDO TOTAL - ELIMINA QUALQUER RASTRO DE BRANCO */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: white !important;
    }

    /* REMOVE ELEMENTOS NATIVOS QUE CAUSAM PISCAR */
    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    [data-testid="stMainBlockContainer"] { padding-top: 65px !important; padding-bottom: 1rem !important; }
    
    /* HEADER BLINDADO (DIRETRIZ 2) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; 
        border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 30px !important; z-index: 1000000; 
        transform: translate3d(0,0,0);
        -webkit-backface-visibility: hidden;
        contain: strict;
    }
    
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; letter-spacing: 1px; text-decoration: none !important; margin-right: 40px; }
    .nav-items { display: flex; gap: 20px; align-items: center; }
    .nav-items span { color: #ffffff; font-size: 9px !important; text-transform: uppercase; opacity: 0.7; font-weight: 600; }
    
    /* SIDEBAR DESIGN */
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        white-space: nowrap !important; border-radius: 0px !important; display: block !important;
    }
    
    /* FIX PARA SCANNER PRÉ-LIVE: REMOVE FUNDO BRANCO DE SELECTBOXES E DROPDOWNS */
    div[data-baseweb="select"] > div {
        background-color: #1a202c !important; 
        color: white !important; 
        border: 1px solid #334155 !important;
    }
    
    /* Altera a cor da lista suspensa (dropdown) que costuma ficar branca */
    div[data-baseweb="popover"] ul {
        background-color: #1a202c !important;
        color: white !important;
        border: 1px solid #334155 !important;
    }
    
    div[role="option"] {
        background-color: #1a202c !important;
        color: white !important;
    }
    
    div[role="option"]:hover {
        background-color: #6d28d9 !important;
    }

    input { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }

    /* UI CARDS */
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px !important; border-radius: 8px; margin-bottom: 10px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. [CAMADA DE PROTEÇÃO 2] - HEADER ANCORADO NA SIDEBAR (DIRETRIZ 1)
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div style="display:flex; align-items:center;">
                <div class="logo-link">GESTOR IA</div>
                <div class="nav-items">
                    <span>APOSTAS ESPORTIVAS</span>
                    <span>APOSTAS AO VIVO</span>
                    <span>OPORTUNIDADES IA</span>
                    <span>ESTATÍSTICAS AVANÇADAS</span>
                </div>
            </div>
            <div style="display: flex; gap: 20px;">
                <div style="color: #ffffff; font-size: 10px; font-weight: 700; border: 1px solid #ffffff; padding: 6px 15px; border-radius: 20px;">REGISTRAR</div>
                <div style="background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 7px 20px; border-radius: 4px; font-weight: 800; font-size: 10px;">ENTRAR</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    # --- [INICIALIZAÇÃO DE MEMÓRIA] ---
    if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
    if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
    if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
    if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
    if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

    # --- [NAVEGAÇÃO] ---
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"

# --- [DADOS INTEGRAIS] ---
DADOS_HIEARARQUIA = {
    "🏆 COPA DO MUNDO 2026": {"Seleções FIFA": {"Principais": ["Brasil", "Argentina", "França", "Alemanha", "Espanha", "Portugal"]}},
    "🇧🇷 BRASIL (LIGAS & COPAS)": {"Campeonato Brasileiro": {"Série A": ["Flamengo", "Palmeiras", "Botafogo", "São Paulo", "Atlético-MG", "Grêmio", "Corinthians", "Fluminense", "Vasco", "Internacional", "Bahia", "Cruzeiro"]}},
    "🇪🇺 EUROPA (PRINCIPAIS LIGAS)": {"Ligas Nacionais": {"Premier League": ["Man. City", "Arsenal", "Liverpool", "Chelsea", "Man. United"], "La Liga": ["Real Madrid", "Barcelona", "Atlético Madrid"]}}
}

# --- [FUNÇÃO GLOBAL DE CARDS] ---
def draw_card(title, value, perc):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div class="conf-bar-bg"><div class="conf-bar-fill" style="width:{perc}%;"></div></div>
        </div>
    """, unsafe_allow_html=True)

# --- [CONTEÚDO DINÂMICO] ---
if st.session_state.aba_ativa == "home":
    st.markdown("""<div class="news-ticker">● LIVE: IA OPERACIONAL ● v57.23</div>""", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("Sugestão", "OVER 2.5 GOLS", 88)
    with h3: draw_card("IA Education", f"STAKE {st.session_state.stake_padrao}%", 100)
    with h4: draw_card("Tendência", "ODDS EM QUEDA", 75)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<div style='color:white; font-weight:900; font-size:26px; margin-bottom:15px;'>🎯 SCANNER PRÉ-LIVE</div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    # Aqui os Selectboxes agora estão blindados pelo CSS para serem escuros
    cat = c1.selectbox("🌎 CATEGORIA", list(DADOS_HIEARARQUIA.keys()))
    tip = c2.selectbox("📂 TIPO", list(DADOS_HIEARARQUIA[cat].keys()))
    cmp = c3.selectbox("🏆 CAMPEONATO", list(DADOS_HIEARARQUIA[cat][tip].keys()))
    
    t1, t2 = st.columns(2)
    lista_times = DADOS_HIEARARQUIA[cat][tip][cmp]
    casa = t1.selectbox("🏠 CASA", lista_times)
    fora = t2.selectbox("🚀 VISITANTE", [x for x in lista_times if x != casa])
    
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        st.session_state.analise_bloqueada = {"casa": casa, "fora": fora, "vencedor": casa, "gols": "OVER 1.5 REAL"}
            
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<div style='color:#9d54ff; font-weight:900; font-size:18px; margin:20px 0;'>RESULTADO: {m['casa']} vs {m['fora']}</div>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['vencedor'], 85)
        with r2: draw_card("MERCADO GOLS", m['gols'], 70)
        with r3: draw_card("STAKE CALC.", "CALCULANDO...", 100)
        with r4: draw_card("ESCANTEIOS", "MAIS DE 9.5", 65)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<div style='color:white; font-weight:900; font-size:26px; margin-bottom:15px;'>💰 GESTÃO DE BANCA</div>", unsafe_allow_html=True)
    nova_banca = st.number_input("VALOR TOTAL DA SUA BANCA (R$)", min_value=0.0, value=st.session_state.banca_total)
    if st.button("SALVAR CONFIGURAÇÃO"):
        st.session_state.banca_total = nova_banca
        st.success("BANCA ATUALIZADA!")

elif st.session_state.aba_ativa == "historico":
    st.markdown("<div style='color:white; font-weight:900; font-size:26px; margin-bottom:15px;'>📜 HISTÓRICO DE CALLS</div>", unsafe_allow_html=True)
    st.info("Histórico de calls processadas pela IA.")

# FOOTER FIXO
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.23</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
