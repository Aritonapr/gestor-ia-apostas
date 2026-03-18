import streamlit as st
import time
import random
from datetime import datetime

# ==============================================================================
# [GIAE KERNEL SHIELD v57.8 - BUGFIX NAME_ERROR & STABILITY LOCK]
# FIX: GLOBAL SCOPE FOR draw_card | FRAGMENT RECOVERY | UI INTEGRITY
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- [FUNÇÕES GLOBAIS - NÃO MOVER DAQUI] ---

def draw_card(title, value, perc):
    """Renderiza os cards de alta performance do Anderson."""
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div class="conf-bar-bg">
                <div class="conf-bar-fill" style="width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- [LOCK] BLOCO DE SEGURANÇA CSS (IDENTIDADE VISUAL COMPLETA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; letter-spacing: 1px; text-decoration: none !important; margin-right: 40px; }
    .nav-items { display: flex; gap: 15px; }
    .nav-items span { color: #ffffff; font-size: 10px !important; text-transform: uppercase; opacity: 0.8; }
    .header-right { display: flex; align-items: center; gap: 15px; min-width: 280px; justify-content: flex-end; }
    .registrar-pill { color: #ffffff !important; font-size: 10px !important; font-weight: 700; border: 1px solid #ffffff !important; padding: 6px 15px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 7px 20px !important; border-radius: 4px !important; font-weight: 800 !important; font-size: 10px !important; }
    
    [data-testid="stSidebar"] button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }
    
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; transition: 0.3s; }
    .highlight-card:hover { border-color: #6d28d9; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px !important; border-radius: 8px; margin-bottom: 10px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- [INICIALIZAÇÃO DE MEMÓRIA] ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_atual' not in st.session_state: st.session_state.banca_atual = 1000.0
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None

# --- [DADOS] ---
DADOS_HIEARARQUIA = {
    "BRASIL": {"Nacional": {"Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo", "São Paulo"], "Brasileirão Série B": ["Santos", "Sport"]}},
    "EUROPA": {"Competições UEFA": {"UEFA Champions League": ["Real Madrid", "Man. City", "Bayern Munique"]}}
}

# --- [CABECALHO] ---
st.markdown("""<div class="betano-header"><div style="display:flex; align-items:center;"><a class="logo-link">GESTOR IA</a><div class="nav-items"><span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Oportunidades IA</span><span>Estatísticas Avançadas</span><span>Probabilidades Reais</span></div></div><div class="header-right"><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div></div>""", unsafe_allow_html=True)

# --- [SIDEBAR] ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "scanner_live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    st.button("📅 JOGOS DO DIA")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("⚽ APOSTAS POR GOLS")

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- [ABA: HOME] ---
if st.session_state.aba_ativa == "home":
    st.markdown("""<div class="news-ticker">● LIVE: IA OPERACIONAL ● HIERARQUIA v57.8 ATIVA</div>""", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("Destaque Live", "FLAMENGO x PALMEIRAS", 90)
    with h2: draw_card("Sugestão", "OVER 2.5 GOLS", 88)
    with h3: draw_card("IA Education", "GESTÃO 3%", 100)
    with h4: draw_card("Tendência", "ODDS EM QUEDA", 75)
    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("Scanner", "ALTA PRESSÃO (HT)", 60)
    with h6: draw_card("Performance", "ASSERTIVIDADE 92%", 92)
    with h7: draw_card("Volume", "MERCADO EM ALTA", 80)
    with h8: draw_card("Proteção", "JARVIS SUPREME", 100)

# --- [ABA: SCANNER - CORREÇÃO DO ERRO DE NOME] ---
elif st.session_state.aba_ativa == "analise":
    st.markdown("""<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">🎯 SCANNER PRÉ-LIVE</div>""", unsafe_allow_html=True)
    
    @st.fragment
    def area_scanner():
        c1, c2, c3 = st.columns(3)
        cat = c1.selectbox("🌎 CATEGORIA", list(DADOS_HIEARARQUIA.keys()))
        tip = c2.selectbox("📂 TIPO", list(DADOS_HIEARARQUIA[cat].keys()))
        cmp = c3.selectbox("🏆 CAMPEONATO", list(DADOS_HIEARARQUIA[cat][tip].keys()))
        
        t1, t2 = st.columns(2)
        casa = t1.selectbox("🏠 CASA", DADOS_HIEARARQUIA[cat][tip][cmp])
        fora = t2.selectbox("🚀 VISITANTE", [x for x in DADOS_HIEARARQUIA[cat][tip][cmp] if x != casa])

        if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
            st.session_state.analise_bloqueada = {"casa": casa, "fora": fora, "vencedor": casa, "gols": "OVER 1.5 REAL", "data": datetime.now().strftime("%H:%M")}
            st.rerun()

        if st.session_state.analise_bloqueada:
            m = st.session_state.analise_bloqueada
            st.markdown(f"<div style='color:#9d54ff; font-weight:900; font-size:18px; margin:20px 0;'>RESULTADO: {m['casa']} vs {m['fora']}</div>", unsafe_allow_html=True)
            r1, r2, r3, r4 = st.columns(4)
            with r1: draw_card("VENCEDOR", m['vencedor'], 85)
            with r2: draw_card("MERCADO GOLS", m['gols'], 70)
            with r3: draw_card("STAKE RECOMENDADA", "R$ 10.00", 100)
            with r4: draw_card("ESCANTEIOS", "MAIS DE 9.5", 65)
            st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
            r5, r6, r7, r8 = st.columns(4)
            with r5: draw_card("TIROS DE META", "14-16 TOTAIS", 40)
            with r6: draw_card("CHUTES AO GOL", "CASA +5.5", 50)
            with r7: draw_card("DEFESAS GOLEIRO", "VISITANTE 4+", 30)
            with r8: draw_card("ÍNDICE PRESSÃO", "GOL MADURO 68%", 68)

            if st.button("📥 ENVIAR PARA HISTÓRICO", use_container_width=True):
                st.session_state.historico_calls.append(m)
                st.toast("✅ ADICIONADO AO HISTÓRICO!")
    
    area_scanner()

# --- [ABA: HISTÓRICO] ---
elif st.session_state.aba_ativa == "historico":
    st.markdown("""<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">📜 HISTÓRICO DE CALLS</div>""", unsafe_allow_html=True)
    @st.fragment
    def render_history_list():
        if not st.session_state.historico_calls: st.info("Histórico vazio.")
        else:
            for i, call in enumerate(reversed(st.session_state.historico_calls)):
                idx_real = len(st.session_state.historico_calls) - 1 - i
                col_info, col_del = st.columns([0.9, 0.1])
                with col_info: st.markdown(f"""<div class="history-card-box"><span style="color:#9d54ff; font-weight:900;">[{call['data']}]</span> <span style="color:white; margin-left:15px;">{call['casa']} x {call['fora']}</span><span style="color:#06b6d4; float:right;">{call['gols']}</span></div>""", unsafe_allow_html=True)
                with col_del: 
                    if st.button("🗑️", key=f"del_v578_{idx_real}"):
                        st.session_state.historico_calls.pop(idx_real)
                        st.rerun(scope="fragment")
    render_history_list()

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.8 LOCKED</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
