import streamlit as st
import time
import random

# ==============================================================================
# [GIAE KERNEL SHIELD v41.0 - SIMETRIA TOTAL 8-CARDS]
# ESTADO: RESULTADOS EM GRID 4x2 (PERFEITO)
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CONTROLE DE NAVEGAÇÃO ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'analise_pronta' not in st.session_state:
    st.session_state.analise_pronta = False

# --- [LOCK] BLOCO DE SEGURANÇA CSS (MANTIDO FIEL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }

    /* [02] SIDEBAR LOCK (320PX) */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    /* [03] NAVBAR SUPERIOR AZUL ROYAL */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; 
    }
    .logo-link { 
        color: #9d54ff !important; font-weight: 900; font-size: 20px !important; 
        text-transform: uppercase; letter-spacing: 1px; margin-right: 80px; 
        text-decoration: none !important; cursor: pointer !important;
    }
    .nav-items span { color: #ffffff; font-size: 10px !important; text-transform: uppercase; cursor: pointer; white-space: nowrap; margin-right: 15px;}

    /* [04] SIDEBAR BOTÕES */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; border-radius: 0px !important;
        text-align: left !important; width: 100% !important; padding: 18px 25px !important; 
        font-size: 10px !important; text-transform: uppercase !important;
    }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }

    /* [05] DASHBOARD CARDS & RESULTADOS */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; transition: 0.3s; }
    .highlight-card:hover { border-color: #6d28d9; transform: translateY(-3px); }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    /* FOOTER */
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DADOS HIERÁRQUICA ---
DADOS_HIEARARQUIA = {
    "BRASIL": {
        "Estadual": {"Paulistão": ["Palmeiras", "São Paulo", "Corinthians", "Santos"], "Carioca": ["Flamengo", "Fluminense", "Vasco"]},
        "Nacional": {"Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo"]}
    }
}

# --- HEADER ---
st.markdown(f"""
    <div class="betano-header">
        <div class="header-left">
            <div class="logo-link">GESTOR IA</div>
            <div class="nav-items">
                <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Apostas Encontradas</span>
                <span>Estatísticas Avançadas</span><span>Mercado Probabilístico</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("📊 LOCALIZAR APOSTA"): 
        st.session_state.aba_ativa = "analise"
        st.session_state.analise_pronta = False
    st.button("📅 JOGOS DO DIA")
    st.button("⏰ PRÓXIMOS JOGOS")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("📈 APOSTAS POR ODDS")
    st.button("⚽ APOSTAS POR GOLS")
    st.button("🚩 APOSTAS POR ESCANTEIOS")

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# TELA: HOME / DASHBOARD (GRID 3x2)
# ------------------------------------------------------------------------------
if st.session_state.aba_ativa == "home":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:10px;">HOME / DASHBOARD</div>', unsafe_allow_html=True)
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">DESTAQUE LIVE</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">FLAMENGO x PALMEIRAS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">SUGESTÃO</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">OVER 2.5 GOLS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:88%;"></div></div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">IA EDUCATION</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">GESTÃO 3%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# TELA: ANÁLISE MÉTRICA (GRID 4x2 - 8 CARDS)
# ------------------------------------------------------------------------------
elif st.session_state.aba_ativa == "analise":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1: pais = st.selectbox("🌎 CATEGORIA", list(DADOS_HIEARARQUIA.keys()))
    with col2: tipo = st.selectbox("📂 TIPO", list(DADOS_HIEARARQUIA[pais].keys()))
    with col3: camp = st.selectbox("🏆 CAMPEONATO", list(DADOS_HIEARARQUIA[pais][tipo].keys()))
    
    t1, t2 = st.columns(2)
    with t1: casa = st.selectbox("🏠 CASA", DADOS_HIEARARQUIA[pais][tipo][camp])
    with t2: fora = st.selectbox("🚀 VISITANTE", [t for t in DADOS_HIEARARQUIA[pais][tipo][camp] if t != casa])

    if st.button("⚡ RESULTADO ALGORITIMO"):
        with st.spinner("CALCULANDO MÉTRICAS..."):
            time.sleep(1.2)
            st.session_state.analise_pronta = True

    if st.session_state.analise_pronta:
        st.markdown(f'<div style="color:#9d54ff; font-weight:900; font-size:18px; margin: 20px 0 10px 0; text-transform: uppercase;">RESULTADO ALGORITIMO: {casa} vs {fora}</div>', unsafe_allow_html=True)
        
        # LINHA 1 (4 CARDS)
        res1, res2, res3, res4 = st.columns(4)
        with res1: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px;">VENCEDOR</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">{casa}</div><div style="color:#00cc66; font-size:10px; margin-top:5px;">CONFIDÊNCIA: 76%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:76%;"></div></div></div>', unsafe_allow_html=True)
        with res2: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px;">MERCADO GOLS</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">OVER 1.5 REAL</div><div style="color:#00cc66; font-size:10px; margin-top:5px;">AMBOS OS TEMPOS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:85%;"></div></div></div>', unsafe_allow_html=True)
        with res3: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px;">CARTÕES</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">MAIS DE 4.5</div><div style="color:#facc15; font-size:10px; margin-top:5px;">FOCO 2º TEMPO</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:70%;"></div></div></div>', unsafe_allow_html=True)
        with res4: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px;">ESCANTEIOS</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">MAIS DE 9.5</div><div style="color:#06b6d4; font-size:10px; margin-top:5px;">DOMINÂNCIA CASA</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:82%;"></div></div></div>', unsafe_allow_html=True)
        
        st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
        
        # LINHA 2 (4 CARDS)
        res5, res6, res7, res8 = st.columns(4)
        with res5: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px;">TIROS DE META</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">14-16 TOTAIS</div><div style="color:#94a3b8; font-size:10px; margin-top:5px;">PADRÃO ESTÁVEL</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)
        with res6: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px;">CHUTES AO GOL</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">CASA +5.5</div><div style="color:#fb7185; font-size:10px; margin-top:5px;">ALTA PRESSÃO</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:78%;"></div></div></div>', unsafe_allow_html=True)
        with res7: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px;">DEFESAS GOLEIRO</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">VISITANTE 4+</div><div style="color:#fb7185; font-size:10px; margin-top:5px;">CARGA ELEVADA</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:80%;"></div></div></div>', unsafe_allow_html=True)
        with res8: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px;">ÍNDICE DE PRESSÃO</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">DOMÍNIO ZONA-X</div><div style="color:#9d54ff; font-size:10px; margin-top:5px;">GOL MADURO: 68%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:68%;"></div></div></div>', unsafe_allow_html=True)

# --- [LOCK] FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v41.0 | JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
