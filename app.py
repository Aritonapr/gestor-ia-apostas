import streamlit as st
import time
import random
from datetime import datetime

# ==============================================================================
# [GIAE KERNEL SHIELD v57.24 - ANTI-FLICKER STABILIZATION]
# FIX: FRAGMENTED EXECUTION FOR SCANNER | ZERO HEADER JITTER
# INTEGRITY: FULL STRUCTURE PRESERVED | NO ABBREVIATIONS | VISUAL LOCK
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
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# --- [FUNÇÃO GLOBAL DE RENDERIZAÇÃO DE CARDS] ---
def draw_card(title, value, perc):
    """Renderiza os cards de alta performance conforme padrão visual Anderson."""
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
    
    /* RESET DE INTERFACE STREAMLIT */
    header, [data-testid="stHeader"], [data-testid="stHeader"]::before { display: none !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }
    
    /* SIDEBAR: DESIGN TRANSPARENTE */
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        white-space: nowrap !important; border-radius: 0px !important; display: block !important; cursor: pointer !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { 
        color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; 
    }
    
    /* BOTÕES DA ÁREA PRINCIPAL */
    [data-testid="stMainBlockContainer"] div.stButton > button {
        background: linear-gradient(90deg, #6d28d9 0%, #4c1d95 100%) !important;
        color: white !important; border: 1px solid rgba(255,255,255,0.1) !important; font-weight: 700 !important;
        text-transform: uppercase !important; font-size: 11px !important; border-radius: 4px !important;
        padding: 12px 20px !important; transition: 0.3s !important; cursor: pointer !important;
    }

    /* CABEÇALHO (HEADER) FIXO - SEM OSCILAÇÃO */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; letter-spacing: 1px; text-decoration: none !important; margin-right: 40px; cursor: pointer !important; }
    .nav-items { display: flex; gap: 20px; align-items: center; }
    .nav-items span { color: #ffffff; font-size: 9px !important; text-transform: uppercase; opacity: 0.7; white-space: nowrap; cursor: pointer !important; transition: 0.3s ease; font-weight: 600; }
    .header-right { display: flex; align-items: center; gap: 20px; }
    .registrar-pill { color: #ffffff !important; font-size: 10px !important; font-weight: 700; border: 1px solid #ffffff !important; padding: 6px 15px !important; border-radius: 20px !important; cursor: pointer !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 7px 20px !important; border-radius: 4px !important; font-weight: 800 !important; font-size: 10px !important; cursor: pointer !important; }
    
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }
    
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px !important; border-radius: 8px; margin-bottom: 10px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    
    div[data-baseweb="select"] > div { background-color: #1a202c !important; color: white !important; border-color: #334155 !important; }
    input { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- [BASE DE DADOS EXPANDIDA] ---
DADOS_HIEARARQUIA = {
    "🏆 COPA DO MUNDO 2026": {"Seleções FIFA": {"Principais": ["Brasil", "Argentina", "França", "Alemanha", "Portugal", "Espanha"]}},
    "🇧🇷 BRASIL (LIGAS & COPAS)": {"Campeonato Brasileiro": {"Série A": ["Flamengo", "Palmeiras", "Botafogo", "Vasco", "São Paulo"], "Série B": ["Santos", "Sport", "Goiás"], "Série C": ["Remo", "Náutico"], "Série D": ["Santa Cruz", "Treze"]}},
    "🇪🇺 EUROPA (ELITE)": {"Premier League (Ing)": {"Clubes": ["Man. City", "Arsenal", "Liverpool", "Chelsea"]}, "La Liga (Esp)": {"Clubes": ["Real Madrid", "Barcelona", "Atlético Madrid"]}},
    "🇸🇦 ORIENTE MÉDIO": {"Saudi Pro League": {"Liga": ["Al-Hilal", "Al-Nassr", "Al-Ittihad"]}},
    "🇺🇸 MLS": {"Major League": {"Liga": ["Inter Miami", "LA Galaxy"]}}
}

# --- [CABEÇALHO ESTÁTICO] ---
st.markdown("""
    <div class="betano-header">
        <div style="display:flex; align-items:center;">
            <a class="logo-link">GESTOR IA</a>
            <div class="nav-items">
                <span>APOSTAS ESPORTIVAS</span>
                <span>APOSTAS AO VIVO</span>
                <span>OPORTUNIDADES IA</span>
                <span>ESTATÍSTICAS AVANÇADAS</span>
            </div>
        </div>
        <div class="header-right">
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

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
    st.markdown("""<div class="news-ticker">● LIVE: IA OPERACIONAL ● v57.24 LOCKED ● GESTÃO ATIVA</div>""", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("PERFORMANCE", "89.4%", 89)
    with h3: draw_card("STAKE ATUAL", f"{st.session_state.stake_padrao}%", 100)
    with h4: draw_card("JARVIS", "PROTECT ON", 100)
    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("VOLATILIDADE", "BAIXA", 20)
    with h6: draw_card("SUGESTÃO", "OVER 1.5 HT", 75)
    with h7: draw_card("MERCADO", "ABERTO", 100)
    with h8: draw_card("STATUS", "V57.24", 100)

# --- [ABA: SCANNER PRÉ-LIVE COM ANTI-FLICKER] ---
elif st.session_state.aba_ativa == "analise":
    st.markdown("<div style='color:white; font-weight:900; font-size:26px; margin-bottom:15px;'>🎯 SCANNER PRÉ-LIVE</div>", unsafe_allow_html=True)
    
    @st.fragment
    def area_scanner_estabilizada():
        c1, c2, c3 = st.columns(3)
        cat = c1.selectbox("🌎 CATEGORIA", list(DADOS_HIEARARQUIA.keys()))
        tip = c2.selectbox("📂 TIPO", list(DADOS_HIEARARQUIA[cat].keys()))
        cmp = c3.selectbox("🏆 CAMPEONATO", list(DADOS_HIEARARQUIA[cat][tip].keys()))
        
        t1, t2 = st.columns(2)
        lista_times = DADOS_HIEARARQUIA[cat][tip][cmp]
        casa = t1.selectbox("🏠 CASA", lista_times)
        fora = t2.selectbox("🚀 VISITANTE", [x for x in lista_times if x != casa])
        
        if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
            valor_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
            st.session_state.analise_bloqueada = {
                "casa": casa, "fora": fora, "vencedor": casa, 
                "gols": "OVER 1.5 REAL", "data": datetime.now().strftime("%H:%M"),
                "stake_val": f"R$ {valor_stake:,.2f}"
            }
            st.rerun(scope="fragment")
            
        if st.session_state.analise_bloqueada:
            m = st.session_state.analise_bloqueada
            st.markdown(f"<div style='color:#9d54ff; font-weight:900; font-size:18px; margin:20px 0;'>RESULTADO: {m['casa']} vs {m['fora']}</div>", unsafe_allow_html=True)
            r1, r2, r3, r4 = st.columns(4)
            with r1: draw_card("VENCEDOR", m['vencedor'], 85)
            with r2: draw_card("STAKE CALC.", m['stake_val'], 100)
            with r3: draw_card("MERCADO", m['gols'], 70)
            with r4: draw_card("CONFIANÇA", "ALTA", 92)
            st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
            r5, r6, r7, r8 = st.columns(4)
            with r5: draw_card("ESCANT.", "9.5+", 60)
            with r6: draw_card("CHUTES", "5.5+", 50)
            with r7: draw_card("DEFESAS", "3+", 30)
            with r8: draw_card("PRESSÃO", "68%", 68)
            
            if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True):
                st.session_state.historico_calls.append(m)
                st.toast("✅ CALL REGISTRADA!")

    area_scanner_estabilizada()

# --- [ABA: SCANNER LIVE] ---
elif st.session_state.aba_ativa == "live":
    st.markdown("<div style='color:white; font-weight:900; font-size:26px; margin-bottom:15px;'>📡 SCANNER EM TEMPO REAL</div>", unsafe_allow_html=True)
    l1, l2, l3, l4 = st.columns(4)
    with l1: draw_card("LIVE: FLAMENGO", "1 x 0 (72')", 72)
    with l2: draw_card("ATAQUES", "14 - 3", 85)
    with l3: draw_card("POSSE", "62%", 62)
    with l4: draw_card("TENDÊNCIA", "GOL 88%", 88)
    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
    l5, l6, l7, l8 = st.columns(4)
    with l5: draw_card("CANTOS", "8", 40)
    with l6: draw_card("CHUTES", "12", 50)
    with l7: draw_card("DEFESAS", "4", 30)
    with l8: draw_card("PRESSÃO IA", "MÁXIMA", 100)

# --- [ABA: GESTÃO DE BANCA] ---
elif st.session_state.aba_ativa == "gestao":
    st.markdown("<div style='color:white; font-weight:900; font-size:26px; margin-bottom:15px;'>💰 GESTÃO DE BANCA</div>", unsafe_allow_html=True)
    g1, g2 = st.columns(2)
    with g1:
        nova_banca = st.number_input("BANCA TOTAL (R$)", min_value=0.0, value=st.session_state.banca_total)
        if st.button("SALVAR BANCA", use_container_width=True):
            st.session_state.banca_total = nova_banca
            st.success("BANCA ATUALIZADA!")
    with g2:
        st.session_state.stake_padrao = st.select_slider("RISCO (%)", options=[0.5, 1.0, 2.0, 3.0, 5.0], value=st.session_state.stake_padrao)
        calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        st.info(f"VALOR POR ENTRADA: R$ {calc:,.2f}")

# --- [ABA: HISTÓRICO] ---
elif st.session_state.aba_ativa == "historico":
    st.markdown("<div style='color:white; font-weight:900; font-size:26px; margin-bottom:15px;'>📜 HISTÓRICO DE CALLS</div>", unsafe_allow_html=True)
    if not st.session_state.historico_calls: st.info("Histórico vazio.")
    else:
        for call in reversed(st.session_state.historico_calls):
            st.markdown(f"""<div class="history-card-box"><span style="color:#9d54ff; font-weight:900;">[{call['data']}]</span> <span style="color:white; margin-left:15px;">{call['casa']} x {call['fora']}</span><span style="color:#06b6d4; float:right;">{call['stake_val']} | {call['gols']}</span></div>""", unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.24 LOCKED</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
