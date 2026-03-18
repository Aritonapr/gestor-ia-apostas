import streamlit as st
import time
import random
from datetime import datetime

# ==============================================================================
# [GIAE KERNEL SHIELD v57.12 - HEADER RESTORATION & INTEGRITY]
# FIX: HEADER LABELS | SIDEBAR NOWRAP | ANTI-FLASH | DESIGN BETANO
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- [FUNÇÃO GLOBAL DE CARDS] ---
def draw_card(title, value, perc):
    """Renderiza os cards de alta performance conforme layout do Anderson."""
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div class="conf-bar-bg">
                <div class="conf-bar-fill" style="width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- [LOCK] BLOCO DE SEGURANÇA CSS (NÃO ALTERAR) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');
    
    /* RESET GERAL */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }
    
    /* BARRA DE MENU SUPERIOR (HEADER) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; 
        border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 30px !important; z-index: 999999; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; letter-spacing: 1px; text-decoration: none !important; margin-right: 40px; }
    
    .nav-items { display: flex; gap: 20px; align-items: center; }
    .nav-items span { color: #ffffff; font-size: 10px !important; text-transform: uppercase; opacity: 0.8; font-weight: 500; cursor: pointer; white-space: nowrap; }
    .nav-items span:hover { opacity: 1; color: #9d54ff; }
    
    .header-right { display: flex; align-items: center; gap: 20px; }
    .search-icon { color: #94a3b8; font-size: 16px; cursor: pointer; }
    .registrar-pill { color: #ffffff !important; font-size: 10px !important; font-weight: 700; border: 1px solid #ffffff !important; padding: 6px 20px !important; border-radius: 20px !important; cursor: pointer; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 7px 25px !important; border-radius: 4px !important; font-weight: 800 !important; font-size: 10px !important; cursor: pointer; }
    
    /* SIDEBAR CONFIGURAÇÃO */
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    
    /* BOTÕES DA SIDEBAR (TEXTO EM UMA LINHA SÓ) */
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; 
        color: #94a3b8 !important; 
        border: none !important; 
        border-bottom: 1px solid #1a202c !important; 
        text-align: left !important; 
        width: 100% !important; 
        padding: 18px 25px !important; 
        font-size: 10px !important; 
        text-transform: uppercase !important;
        white-space: nowrap !important; 
        border-radius: 0px !important;
        display: block !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }
    
    /* BOTÕES DA ÁREA PRINCIPAL (REMOÇÃO DO BRANCO) */
    [data-testid="stMainBlockContainer"] div.stButton > button {
        background: linear-gradient(90deg, #6d28d9 0%, #4c1d95 100%) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        font-size: 11px !important;
        border-radius: 4px !important;
        padding: 12px 20px !important;
    }

    /* CARDS E GRÁFICOS */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; transition: 0.3s; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }
    
    /* HISTÓRICO */
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px !important; border-radius: 8px; margin-bottom: 10px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- [INICIALIZAÇÃO DE MEMÓRIA] ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None

# --- [BASE DE DADOS] ---
DADOS_HIEARARQUIA = {
    "BRASIL": {"Nacional": {"Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo", "São Paulo"], "Brasileirão Série B": ["Santos", "Sport"]}},
    "EUROPA": {"Competições UEFA": {"UEFA Champions League": ["Real Madrid", "Man. City", "Bayern"]}}
}

# --- [CABECALHO RESTAURADO] ---
st.markdown("""
    <div class="betano-header">
        <div style="display:flex; align-items:center;">
            <a class="logo-link">GESTOR IA</a>
            <div class="nav-items">
                <span>APOSTAS ESPORTIVAS</span>
                <span>APOSTAS AO VIVO</span>
                <span>APOSTAS ENCONTRADAS</span>
                <span>ESTATÍSTICAS AVANÇADAS</span>
                <span>MERCADO PROBABILÍSTICO</span>
                <span>ASSERTIVIDADE IA</span>
            </div>
        </div>
        <div class="header-right">
            <span class="search-icon">🔍</span>
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- [SIDEBAR] ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("🔍 LOCALIZAR APOSTA"): st.session_state.aba_ativa = "home"
    if st.button("📅 JOGOS DO DIA"): pass
    if st.button("⏰ PRÓXIMOS JOGOS"): pass
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): pass
    if st.button("📈 APOSTAS POR ODDS"): pass
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "analise"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "analise"
    if st.button("⚖️ ÁRBITRO DA PARTIDA"): pass
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- [ABA: HOME / DASHBOARD] ---
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white; margin-bottom:20px;'>HOME / DASHBOARD</h2>", unsafe_allow_html=True)
    st.markdown("""<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE ● ALERTA: ODDS EM QUEDA ● DICA: GESTÃO DE BANCA ATUALIZADA</div>""", unsafe_allow_html=True)
    
    h1, h2, h3 = st.columns(3)
    with h1: draw_card("Destaque Live", "FLAMENGO x PALMEIRAS", 90)
    with h2: draw_card("Sugestão de Mercado", "OVER 2.5 GOLS", 88)
    with h3: draw_card("IA Education", "GESTÃO 3%", 100)
    
    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
    
    h4, h5, h6 = st.columns(3)
    with h4: draw_card("Tendência de Valor", "ODDS DESAJUSTADAS", 75)
    with h5: draw_card("Scanner de Cantos", "ALTA PRESSÃO (HT)", 60)
    with h6: draw_card("Performance Semanal", "ASSERTIVIDADE 92%", 92)

# --- [ABA: SCANNER] ---
elif st.session_state.aba_ativa == "analise":
    @st.fragment
    def area_scanner():
        st.markdown("<h2 style='color:white;'>🎯 SCANNER DE ANÁLISE</h2>", unsafe_allow_html=True)
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
            r1, r2, r3, r4 = st.columns(4)
            with r1: draw_card("VENCEDOR", m['vencedor'], 85)
            with r2: draw_card("MERCADO GOLS", m['gols'], 70)
            with r3: draw_card("STAKE", "R$ 10.00", 100)
            with r4: draw_card("ESCANTEIOS", "9.5+", 65)
            
            if st.button("📥 SALVAR NO HISTÓRICO", use_container_width=True):
                st.session_state.historico_calls.append(m)
                st.toast("✅ SALVO!")
    area_scanner()

# --- [ABA: HISTÓRICO] ---
elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    @st.fragment
    def render_history_list():
        if not st.session_state.historico_calls: st.info("Histórico vazio.")
        else:
            for i, call in enumerate(reversed(st.session_state.historico_calls)):
                idx_real = len(st.session_state.historico_calls) - 1 - i
                col_info, col_del = st.columns([0.9, 0.1])
                with col_info: st.markdown(f"""<div class="history-card-box"><span style="color:#9d54ff; font-weight:900;">[{call['data']}]</span> <span style="color:white; margin-left:15px;">{call['casa']} x {call['fora']}</span><span style="color:#06b6d4; float:right;">{call['gols']}</span></div>""", unsafe_allow_html=True)
                with col_del: 
                    if st.button("🗑️", key=f"del_v12_{idx_real}"):
                        st.session_state.historico_calls.pop(idx_real)
                        st.rerun(scope="fragment")
    render_history_list()

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.12 LOCKED</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
