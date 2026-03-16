import streamlit as st
import time

# ==============================================================================
# [SISTEMA DE DADOS - ADICIONE SEUS TIMES AQUI]
# ==============================================================================
DADOS_HIEARARQUIA = {
    "BRASIL": {
        "Nacional": {
            "Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo", "Fortaleza", "São Paulo"],
            "Brasileirão Série B": ["Santos", "Sport", "Ceará"]
        },
        "Estadual": {
            "Paulistão": ["Palmeiras", "São Paulo", "Corinthians", "Santos"],
            "Carioca": ["Flamengo", "Fluminense", "Vasco", "Botafogo"]
        }
    },
    "INGLATERRA": {
        "Nacional": { "Premier League": ["Man City", "Arsenal", "Liverpool", "Chelsea"] }
    }
}

# ==============================================================================
# [CONFIGURAÇÃO E ESTILO CSS] - RESTAURANDO OS CARDS DA IMAGEM 2
# ==============================================================================
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'analise_pronta' not in st.session_state: st.session_state.analise_pronta = False

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');
    header, [data-testid="stHeader"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; }
    
    /* NAVBAR SUPERIOR */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #002366; display: flex; align-items: center; justify-content: space-between; padding: 0 30px; z-index: 999999; border-bottom: 1px solid rgba(255,255,255,0.1); }
    .logo-link { color: #9d54ff; font-weight: 900; font-size: 20px; text-transform: uppercase; text-decoration: none; }
    .nav-items { display: flex; gap: 15px; }
    .nav-items span { color: #ffffff; font-size: 10px; text-transform: uppercase; cursor: pointer; }
    .registrar-pill { color: #ffffff; font-size: 10px; font-weight: 700; border: 1px solid #ffffff; padding: 6px 15px; border-radius: 20px; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 7px 20px; border-radius: 4px; font-weight: 800; font-size: 10px; }

    /* SIDEBAR */
    [data-testid="stSidebar"] { min-width: 320px; background-color: #11151a !important; border-right: 1px solid #1e293b; }
    [data-testid="stSidebar"] button { background: transparent; color: #94a3b8; border: none; border-bottom: 1px solid #1a202c; text-align: left; width: 100%; padding: 18px 25px; font-size: 10px; text-transform: uppercase; }
    [data-testid="stSidebar"] button:hover { color: #ffffff; border-left: 4px solid #6d28d9; background: rgba(26, 36, 45, 0.8); }

    /* CARDS DO DASHBOARD E RESULTADOS */
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; transition: 0.3s; margin-bottom: 10px; }
    .result-box { background: #11151a; border: 1px solid #6d28d9; border-radius: 10px; padding: 20px; margin-top: 20px; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }
    
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown(f"""<div class="betano-header"><div class="header-left"><a href="#" class="logo-link">GESTOR IA</a><div class="nav-items"><span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Estatísticas Avançadas</span></div></div><div class="header-right"><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div></div>""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True)
    if st.button("📊 LOCALIZAR APOSTA"): st.session_state.aba_ativa = "analise"; st.session_state.analise_pronta = False
    if st.button("🏠 HOME / DASHBOARD"): st.session_state.aba_ativa = "home"
    st.button("📅 JOGOS DO DIA")
    st.button("⏰ PRÓXIMOS JOGOS")

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- PAGINA HOME ---
if st.session_state.aba_ativa == "home":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:10px;">HOME / DASHBOARD</div>', unsafe_allow_html=True)
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE ● ALERTA: ODDS EM QUEDA</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    for c in [c1, c2, c3]:
        with c: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">DESTAQUE</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">FLAMENGO x PALMEIRAS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)

# --- PAGINA ANALISE (AQUI ESTÁ A CORREÇÃO DOS CARDS) ---
elif st.session_state.aba_ativa == "analise":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1: p = st.selectbox("🌎 CATEGORIA", list(DADOS_HIEARARQUIA.keys()))
    with col2: t = st.selectbox("📂 TIPO", list(DADOS_HIEARARQUIA[p].keys()))
    with col3: c = st.selectbox("🏆 CAMPEONATO", list(DADOS_HIEARARQUIA[p][t].keys()))
    
    t1, t2 = st.columns(2)
    with t1: casa = st.selectbox("🏠 CASA", DADOS_HIEARARQUIA[p][t][c])
    with t2: fora = st.selectbox("🚀 VISITANTE", [x for x in DADOS_HIEARARQUIA[p][t][c] if x != casa])

    if st.button("⚡ RESULTADO ALGORITIMO"):
        with st.spinner("PROCESSANDO..."):
            time.sleep(1)
            st.session_state.analise_pronta = True

    if st.session_state.analise_pronta:
        st.markdown(f'<div style="color:#9d54ff; font-weight:900; font-size:18px; margin-top:20px;">RESULTADO ALGORITIMO: {casa} VS {fora}</div>', unsafe_allow_html=True)
        
        # GRID DE CARDS IGUAL À IMAGEM 2
        r1, r2, r3, r4 = st.columns(4)
        with r1: st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:8px;">VENCEDOR</div><div style="color:white; font-weight:900;">{casa}</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:78%;"></div></div></div>', unsafe_allow_html=True)
        with r2: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:8px;">MERCADO GOLS</div><div style="color:white; font-weight:900;">OVER 1.5 REAL</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:85%;"></div></div></div>', unsafe_allow_html=True)
        with r3: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:8px;">CARTÕES</div><div style="color:white; font-weight:900;">MAIS DE 4.5</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:60%;"></div></div></div>', unsafe_allow_html=True)
        with r4: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:8px;">ESCANTEIOS</div><div style="color:white; font-weight:900;">MAIS DE 9.5</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:70%;"></div></div></div>', unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL</div><div>GESTOR IA PRO v18.0</div></div>""", unsafe_allow_html=True)
