import streamlit as st
import time
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v57.23 - PROTEÇÃO ATIVA]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE ABSOLUTO)
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
    
    /* [DIRETRIZ 2] HEADER PREMIUM ORIGINAL */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
        transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    
    .header-left { display: flex; align-items: center; gap: 25px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; letter-spacing: 0.5px; }
    
    .nav-links { display: flex; gap: 18px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 8.5px !important; text-transform: uppercase; opacity: 0.85; font-weight: 700; letter-spacing: 0.8px; }

    /* SIDEBAR NAVIGATION */
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: all 0.2s ease !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important;
    }

    /* [DIRETRIZ 4] ZERO WHITE - INPUTS E SELECTS BLINDADOS */
    div[data-baseweb="input"], 
    div[data-baseweb="select"], 
    div[role="listbox"],
    .stSelectbox div,
    .stNumberInput div { 
        background-color: #1a202c !important; 
        color: white !important; 
        border: 1px solid #334155 !important; 
    }
    input, span[data-baseweb="select"] { color: white !important; }

    /* BOTÕES DE AÇÃO */
    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important;
        border: none !important;
        padding: 15px 20px !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        border-radius: 6px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }

    /* TÍTULO INTELIGENTE (HIGHLIGHT BLUE) */
    .smart-title-box {
        background-color: #0044cc;
        color: white;
        padding: 8px 20px;
        display: inline-block;
        font-weight: 800;
        font-size: 24px;
        border-radius: 4px;
        margin-bottom: 25px;
    }

    /* KPI CARDS (8 QUADRADOS) */
    .kpi-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
        transition: all 0.3s ease;
    }
    .kpi-card:hover { transform: translateY(-5px); border-color: #6d28d9; }
    
    .kpi-label { color: #64748b; font-size: 9px; text-transform: uppercase; font-weight: 700; margin-bottom: 10px; }
    .kpi-value { color: white; font-size: 18px; font-weight: 900; }
    .kpi-bar { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 4px; width: 60%; margin: 12px auto; border-radius: 10px; }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. [DIRETRIZ 1] HEADER ANCORADO NA SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <div class="logo-link">GESTOR IA</div>
                <div class="nav-links">
                    <div class="nav-item">ESPORTES</div>
                    <div class="nav-item">AO VIVO</div>
                    <div class="nav-item">VIRTUAIS</div>
                    <div class="nav-item">E-SPORTS</div>
                </div>
            </div>
            <div class="header-right">
                <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:6px 20px; border-radius:5px; font-size:10px; font-weight:800;">ENTRAR</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    # --- MEMÓRIA ---
    if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
    if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
    if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
    if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
    if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0
    if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
    if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None

    # --- NAVEGAÇÃO ---
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

# FUNÇÃO KPI CARD (8 UNIDADES)
def draw_kpi(label, value):
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-bar"></div>
        </div>
    """, unsafe_allow_html=True)

# --- LÓGICA DE TELAS ---

# TELA 1: HOME
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    r1_1, r1_2, r1_3, r1_4 = st.columns(4)
    with r1_1: draw_kpi("BANCA TOTAL", f"R$ {st.session_state.banca_total:,.2f}")
    with r1_2: draw_kpi("ASSERTIVIDADE", "92.4%")
    with r1_3: draw_kpi("SUGESTÃO", "OVER 2.5")
    with r1_4: draw_kpi("IA STATUS", "ONLINE")
    r2_1, r2_2, r2_3, r2_4 = st.columns(4)
    with r2_1: draw_kpi("VOL. GLOBAL", "ALTO")
    with r2_2: draw_kpi("STAKE", f"{st.session_state.stake_padrao}%")
    with r2_3: draw_kpi("ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}")
    with r2_4: draw_kpi("SISTEMA", "v57.23")

# TELA 2: GESTÃO DE BANCA INTELIGENTE
elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div style='display:flex; align-items:center; gap:15px;'>
                    <span style='font-size:35px;'>💰</span> 
                    <div class="smart-title-box">GESTÃO DE BANCA INTELIGENTE</div>
                </div>""", unsafe_allow_html=True)
    
    c_in, c_kp = st.columns([1, 2.2])
    with c_in:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total, step=50.0)
        st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, st.session_state.stake_padrao)
        st.session_state.meta_diaria = st.slider("META (%)", 1.0, 30.0, st.session_state.meta_diaria)
        st.session_state.stop_loss = st.slider("STOP LOSS (%)", 1.0, 30.0, st.session_state.stop_loss)

    with c_kp:
        v_s = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        v_m = (st.session_state.banca_total * st.session_state.meta_diaria / 100)
        v_l = (st.session_state.banca_total * st.session_state.stop_loss / 100)
        
        k1, k2, k3, k4 = st.columns(4)
        with k1: draw_kpi("VALOR ENTRADA", f"R$ {v_s:,.2f}")
        with k2: draw_kpi("STOP GAIN", f"R$ {v_m:,.2f}")
        with k3: draw_kpi("STOP LOSS", f"R$ {v_l:,.2f}")
        with k4: draw_kpi("ALVO FINAL", f"R$ {(st.session_state.banca_total + v_m):,.2f}")
        k5, k6, k7, k8 = st.columns(4)
        with k5: draw_kpi("RISCO TOTAL", f"{st.session_state.stake_padrao}%")
        with k6: draw_kpi("ENTRADAS/META", f"{int(v_m/v_s) if v_s > 0 else 0}")
        with k7: draw_kpi("ENTRADAS/LOSS", f"{int(v_l/v_s) if v_s > 0 else 0}")
        with k8: draw_kpi("SAÚDE BANCA", "EXCELENTE")

# TELA 3: SCANNER PRÉ-LIVE (AJUSTADO)
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    st.selectbox("🏆 VENCEDORES DA COMPETIÇÃO", ["Rodada Atual", "Finais", "Fase de Grupos"])
    cat1, cat2 = st.columns(2)
    with cat1: st.selectbox("🌎 CATEGORIA", ["BRASIL", "EUROPA", "MUNDO"])
    with cat2: st.selectbox("📂 TIPO", ["Série A", "Champions League"])
    
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        st.session_state.analise_bloqueada = {"casa": "Time A", "fora": "Time B", "vencedor": "Casa", "gols": "OVER 2.5", "data": datetime.now().strftime("%H:%M"), "stake_val": f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}"}
    
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<h3 style='color:#9d54ff;'>RESULTADO: {m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_kpi("VENCEDOR", m['vencedor'])
        with r2: draw_kpi("GOLS", m['gols'])
        with r3: draw_kpi("STAKE", m['stake_val'])
        with r4: draw_kpi("CANTOS", "9.5+")
        r5, r6, r7, r8 = st.columns(4)
        with r5: draw_kpi("IA CONF.", "94%")
        with r6: draw_kpi("PRESSÃO", "ALTA")
        with r7: draw_kpi("TENDÊNCIA", "SUBINDO")
        with r8: draw_kpi("STATUS", "ESTÁVEL")
        if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True):
            st.session_state.historico_calls.append(m.copy())
            st.toast("✅ SALVO!")

# OUTRAS TELAS (Sempre com 8 cards para simetria)
elif st.session_state.aba_ativa in ["live", "vencedores", "gols", "escanteios"]:
    st.markdown(f"<h2 style='color:white;'>{st.session_state.aba_ativa.upper()}</h2>", unsafe_allow_html=True)
    l1, l2, l3, l4 = st.columns(4)
    for i in range(4): 
        with [l1,l2,l3,l4][i]: draw_kpi("MÉTRICA ATIVA", "ANÁLISE...")
    l5, l6, l7, l8 = st.columns(4)
    for i in range(4): 
        with [l5,l6,l7,l8][i]: draw_kpi("TENDÊNCIA", "PROCESSANDO...")

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    if not st.session_state.historico_calls: st.info("Vazio.")
    else:
        for idx, call in enumerate(reversed(st.session_state.historico_calls)):
            st.markdown(f"""<div style="background:#161b22; border:1px solid #30363d; padding:15px; border-radius:8px; margin-bottom:10px; color:white;">[{call['data']}] {call['casa']} x {call['fora']} | {call['stake_val']} | {call['gols']}</div>""", unsafe_allow_html=True)

# FOOTER
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.23</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
