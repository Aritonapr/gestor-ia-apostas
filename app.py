import streamlit as st
import time
import random
from datetime import datetime

# ==============================================================================
# [GIAE KERNEL SHIELD v57.23 - INTEGRATED OPERATIONAL SYSTEM]
# MODS: BANKROLL MGMT | LIVE SCANNER REFINEMENT | DATA PERSISTENCE
# INTEGRITY: NO ABBREVIATIONS | FULL CODE RESTORED | INTERFACE LOCKED
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- [INICIALIZAÇÃO DE MEMÓRIA CRÍTICA] ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0 # 1% inicial

# --- [FUNÇÃO GLOBAL DE RENDERIZAÇÃO DE CARDS] ---
def draw_card(title, value, perc):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div class="conf-bar-bg">
                <div class="conf-bar-fill" style="width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- [LOCK] BLOCO DE SEGURANÇA CSS (NÃO ALTERAR ESTRUTURA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }
    
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; display: block !important; cursor: pointer !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { 
        color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; 
    }
    
    [data-testid="stMainBlockContainer"] div.stButton > button {
        background: linear-gradient(90deg, #6d28d9 0%, #4c1d95 100%) !important;
        color: white !important; font-weight: 700 !important; text-transform: uppercase !important;
        font-size: 11px !important; border-radius: 4px !important; padding: 12px 20px !important; border: none !important;
    }

    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #002366; border-bottom: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: space-between; padding: 0 30px; z-index: 999999; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px; text-transform: uppercase; text-decoration: none; cursor: pointer; }
    .nav-items { display: flex; gap: 20px; }
    .nav-items span { color: #ffffff; font-size: 9px; text-transform: uppercase; opacity: 0.7; cursor: pointer; font-weight: 600; }
    .header-right { display: flex; align-items: center; gap: 20px; }
    
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }
    
    .history-card-box { background: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 8px; margin-bottom: 10px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    
    input { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- [BASE DE DADOS INTEGRAL] ---
DADOS_HIEARARQUIA = {
    "🏆 COPA DO MUNDO 2026": {"Seleções FIFA": {"Principais": ["Brasil", "Argentina", "França", "Alemanha", "Portugal"]}},
    "🇧🇷 BRASIL (LIGAS)": {"Brasileirão": {"Série A": ["Flamengo", "Palmeiras", "Botafogo", "Vasco"], "Série B": ["Santos", "Sport"], "Série C": ["Remo", "Náutico"], "Série D": ["Santa Cruz", "Treze"]}},
    "🇪🇺 EUROPA ELITE": {"Premier League": {"Inglaterra": ["Man. City", "Arsenal", "Liverpool"]}, "La Liga": {"Espanha": ["Real Madrid", "Barcelona"]}},
    "🇸🇦 ORIENTE MÉDIO": {"Saudi Pro League": {"Liga": ["Al-Hilal", "Al-Nassr"]}},
    "🇺🇸 MLS": {"Major League": {"USA": ["Inter Miami", "LA Galaxy"]}}
}

# --- [CABECALHO] ---
st.markdown("""<div class="betano-header"><div style="display:flex; align-items:center;"><a class="logo-link">GESTOR IA</a><div class="nav-items"><span>AO VIVO</span><span>ESTATÍSTICAS</span><span>MERCADO PRO</span></div></div><div class="header-right"><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div></div>""", unsafe_allow_html=True)

# --- [SIDEBAR] ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- [ABA: HOME] ---
if st.session_state.aba_ativa == "home":
    st.markdown("""<div class="news-ticker">● STATUS: IA OPERACIONAL ● AGUARDANDO COMANDO DE ANÁLISE ● v57.23</div>""", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("PERFORMANCE", "89.4%", 89)
    with h3: draw_card("STAKE ATUAL", f"{st.session_state.stake_padrao}%", 100)
    with h4: draw_card("SISTEMA", "PROTEGIDO", 100)

# --- [PARTE 1: GESTÃO DE BANCA FUNCIONAL] ---
elif st.session_state.aba_ativa == "gestao":
    st.markdown("<div style='color:white; font-weight:900; font-size:26px;'>💰 GESTÃO DE BANCA PRO</div>", unsafe_allow_html=True)
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        nova_banca = st.number_input("VALOR TOTAL DA BANCA (R$)", min_value=0.0, value=st.session_state.banca_total)
        if st.button("ATUALIZAR BANCA"):
            st.session_state.banca_total = nova_banca
            st.success(f"BANCA ATUALIZADA: R$ {nova_banca}")
    with col_b2:
        st.session_state.stake_padrao = st.select_slider("DEFINIR RISCO POR ENTRADA (%)", options=[0.5, 1.0, 2.0, 3.0, 5.0], value=st.session_state.stake_padrao)
        st.info(f"CÁLCULO AUTOMÁTICO: R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f} POR CALL")

# --- [PARTE 2: REFINO SCANNER LIVE (SIMULAÇÃO)] ---
elif st.session_state.aba_ativa == "live":
    st.markdown("<div style='color:white; font-weight:900; font-size:26px;'>📡 MONITORAMENTO EM TEMPO REAL</div>", unsafe_allow_html=True)
    st.markdown("<div class='news-ticker'>VARREDURA GLOBAL ATIVA: CAPTURANDO PRESSÃO DE JOGO...</div>", unsafe_allow_html=True)
    
    # Simulação de Grids dinâmicos
    l1, l2, l3, l4 = st.columns(4)
    with l1: draw_card("LIVE: FLAMENGO", "1 x 0 (72')", 72)
    with l2: draw_card("ATAQUES PERIGOSOS", "14 - 3", 85)
    with l3: draw_card("POSSE DE BOLA", "62%", 62)
    with l4: draw_card("PRESSÃO IA", "ALTA", 90)

# --- [ABA: SCANNER PRÉ-LIVE + INTEGRAÇÃO BANCA] ---
elif st.session_state.aba_ativa == "analise":
    st.markdown("<div style='color:white; font-weight:900; font-size:26px;'>🎯 SCANNER PRÉ-LIVE</div>", unsafe_allow_html=True)
    cat = st.selectbox("🌎 CATEGORIA", list(DADOS_HIEARARQUIA.keys()))
    tip = st.selectbox("📂 TIPO", list(DADOS_HIEARARQUIA[cat].keys()))
    cmp = st.selectbox("🏆 CAMPEONATO", list(DADOS_HIEARARQUIA[cat][tip].keys()))
    
    t1, t2 = st.columns(2)
    lista_times = DADOS_HIEARARQUIA[cat][tip][cmp]
    casa = t1.selectbox("🏠 CASA", lista_times)
    fora = t2.selectbox("🚀 VISITANTE", [x for x in lista_times if x != casa])
    
    if st.button("⚡ EXECUTAR ALGORITIMO"):
        valor_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        st.session_state.analise_bloqueada = {
            "casa": casa, "fora": fora, "vencedor": casa, 
            "gols": "OVER 1.5", "data": datetime.now().strftime("%H:%M"),
            "stake_calc": f"R$ {valor_stake:,.2f}"
        }
    
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['vencedor'], 85)
        with r2: draw_card("STAKE SUGERIDA", m['stake_calc'], 100)
        with r3: draw_card("MERCADO", m['gols'], 70)
        with r4: draw_card("CONFIANÇA", "ALTA", 92)
        
        # PARTE 3: CONEXÃO DO HISTÓRICO
        if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True):
            st.session_state.historico_calls.append(m)
            st.toast("✅ CALL ENVIADA PARA O HISTÓRICO!")

# --- [ABA: HISTÓRICO] ---
elif st.session_state.aba_ativa == "historico":
    st.markdown("<div style='color:white; font-weight:900; font-size:26px;'>📜 HISTÓRICO DE CALLS</div>", unsafe_allow_html=True)
    if not st.session_state.historico_calls: st.info("Histórico vazio.")
    else:
        for i, call in enumerate(reversed(st.session_state.historico_calls)):
            st.markdown(f"""<div class="history-card-box"><span style="color:#9d54ff; font-weight:900;">[{call['data']}]</span> <span style="color:white; margin-left:15px;">{call['casa']} x {call['fora']}</span><span style="color:#06b6d4; float:right;">STAKE: {call['stake_calc']} | {call['gols']}</span></div>""", unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.23</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
