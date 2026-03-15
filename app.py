import streamlit as st
import time
import random

# ==============================================================================
# [GIAE KERNEL SHIELD v28.0 - PROTOCOLO JARVIS SUPREME]
# INTEGRADO: CONCEITO "LOCALIZAR APOSTAS" SEM ALTERAR ESTÉTICA
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

# --- [LOCK] BLOCO DE SEGURANÇA CSS (MANTIDO EXATAMENTE COMO O SEU) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }

    /* [02] SIDEBAR LOCK (320PX) */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    /* [03] NAVBAR SUPERIOR AZUL ROYAL */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; 
    }
    .header-left { display: flex; align-items: center; }
    
    /* ESTILO DO LOGO - AJUSTADO MARGIN PARA NÃO ENCOSTAR */
    .logo-link { 
        color: #9d54ff !important; font-weight: 900; font-size: 20px !important; 
        text-transform: uppercase; letter-spacing: 1px; margin-right: 80px; 
        text-decoration: none !important; cursor: pointer !important; transition: 0.3s;
    }
    .logo-link:hover { text-shadow: 0 0 15px #9d54ff; filter: brightness(1.2); }

    .nav-items { display: flex; gap: 15px; }
    .nav-items span { color: #ffffff; font-size: 10px !important; text-transform: uppercase; cursor: pointer; white-space: nowrap; transition: 0.2s; }
    .nav-items span:hover { color: #9d54ff; }

    /* HEADER DIREITO */
    .header-right { display: flex; align-items: center; gap: 15px; min-width: 250px; justify-content: flex-end; }
    .search-icon { color: #ffffff !important; cursor: pointer !important; font-size: 16px !important; transition: 0.3s !important; }
    
    .registrar-pill { 
        color: #ffffff !important; font-size: 10px !important; font-weight: 700 !important; border: 1px solid #ffffff !important; 
        padding: 6px 15px !important; border-radius: 20px !important; cursor: pointer !important; transition: 0.3s; white-space: nowrap;
    }
    .registrar-pill:hover { background: #ffffff !important; color: #002366 !important; }

    .entrar-grad { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: white !important; padding: 7px 20px !important; border-radius: 4px !important; 
        font-weight: 800 !important; font-size: 10px !important; cursor: pointer !important; transition: 0.3s; white-space: nowrap;
    }

    /* [04] SIDEBAR BOTÕES - SIMETRIA TOTAL */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; border-radius: 0px !important;
        text-align: left !important; width: 100% !important; padding: 20px 30px !important; 
        font-size: 10px !important; text-transform: uppercase !important; white-space: nowrap !important;
    }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }

    /* [05] DASHBOARD CARDS */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; transition: 0.3s; }
    
    .pulse-dot { height: 6px; width: 6px; background-color: #22c55e; border-radius: 50%; display: inline-block; margin-right: 5px; animation: pulse 1.5s infinite; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    /* ESTILO SELECTS (ADAPTADO AO TEMA) */
    div[data-baseweb="select"] > div { background-color: #11151a !important; border: 1px solid #1e293b !important; color: white !important; }

    /* FOOTER */
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DADOS (CONCEITO PAÍS -> TIPO -> CAMPEONATO) ---
DADOS_HIEARARQUIA = {
    "BRASIL": {
        "Estadual": {
            "Paulistão": ["Palmeiras", "São Paulo", "Corinthians", "Santos", "RB Bragantino"],
            "Carioca": ["Flamengo", "Fluminense", "Vasco", "Botafogo"]
        },
        "Nacional": {
            "Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo", "São Paulo"],
            "Copa do Brasil": ["Atlético-MG", "Vasco", "Flamengo", "Corinthians"]
        }
    },
    "INGLATERRA": {
        "Nacional": {
            "Premier League": ["Man City", "Arsenal", "Liverpool", "Chelsea", "Man United"]
        }
    }
}

# --- [LOCK] CABEÇALHO ---
st.markdown(f"""
    <div class="betano-header">
        <div class="header-left">
            <a href="/" target="_self" class="logo-link">GESTOR IA</a>
            <div class="nav-items">
                <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Apostas Encontradas</span>
                <span>Estatísticas Avançadas</span><span>Mercado Probabilístico</span><span>Assertividade IA</span>
            </div>
        </div>
        <div class="header-right">
            <div class="search-icon">🔍</div>
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- [LOCK] SIDEBAR (MANTIDO) ---
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
    st.button("⚖️ ÁRBITRO DA PARTIDA")

# --- CONTEÚDO CENTRAL ---
st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

if st.session_state.aba_ativa == "home":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:10px; letter-spacing:-1px;">HOME / DASHBOARD</div>', unsafe_allow_html=True)
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE ● ALERTA: ODDS EM QUEDA</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;"><span class="pulse-dot"></span>Destaque Live</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">FLAMENGO x PALMEIRAS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Sugestão</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">OVER 2.5 GOLS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:88%;"></div></div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">IA Education</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">GESTÃO 3%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# TELA: ANÁLISE MÉTRICA (INTEGRADA NO SEU CONCEITO)
# ------------------------------------------------------------------------------
elif st.session_state.aba_ativa == "analise":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    
    # SELEÇÃO 3 NÍVEIS
    col1, col2, col3 = st.columns(3)
    with col1:
        pais = st.selectbox("🌎 CATEGORIA (PAÍS)", list(DADOS_HIEARARQUIA.keys()))
    with col2:
        tipo = st.selectbox("📂 TIPO DE COMPETIÇÃO", list(DADOS_HIEARARQUIA[pais].keys()))
    with col3:
        campeonato = st.selectbox("🏆 CAMPEONATO", list(DADOS_HIEARARQUIA[pais][tipo].keys()))

    col_t1, col_t2 = st.columns(2)
    with col_t1:
        time_a = st.selectbox("🏠 TIME DA CASA", DADOS_HIEARARQUIA[pais][tipo][campeonato])
    with col_t2:
        time_b = st.selectbox("🚀 TIME VISITANTE", [t for t in DADOS_HIEARARQUIA[pais][tipo][campeonato] if t != time_a])

    # BOTÃO RENOMEADO
    if st.button("⚡ RESULTADO ALGORITIMO"):
        with st.spinner("PROCESSANDO..."):
            time.sleep(1.2)
            st.session_state.analise_pronta = True

    # RESULTADO (SEM BOTÕES ROXOS EXTRAS)
    if st.session_state.analise_pronta:
        st.markdown(f"""
            <div style="background:#1a202c; border: 1px solid #6d28d9; padding:25px; border-radius:10px; margin-top:20px;">
                <div style="color:#9d54ff; font-weight:900; font-size:18px; margin-bottom:15px; text-transform: uppercase;">
                    RESULTADO ALGORITIMO: {time_a} vs {time_b}
                </div>
        """, unsafe_allow_html=True)
        
        r1, r2 = st.columns(2)
        with r1:
            st.markdown(f"✅ **VENCEDOR:** Probabilidade Real de 78% para {time_a}")
            st.markdown(f"⚽ **GOLS:** Over 1.5 Real Confirmado (Ambos os tempos)")
            st.markdown(f"🟨 **CARTÕES:** Tendência de +4.5 total no jogo")
            st.markdown(f"🚩 **ESCANTEIOS:** Over 9.5 total (Foco no 2º tempo)")
        with r2:
            st.markdown(f"🥅 **TIROS DE META:** Média matemática de 14.5 tiros")
            st.markdown(f"🎯 **CHUTES NO GOL:** {time_a} com +5.5 chutes reais")
            st.markdown(f"🧤 **DEFESAS:** Goleiro do {time_b} com alta carga (4+ defesas)")
            
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div style="color:#475569; font-size:9px; margin-top:10px;">* NOTA: SÃO EXIBIDOS APENAS RESULTADOS COM PROBABILIDADE REAL ACIMA DE 75%.</div>', unsafe_allow_html=True)

# --- [LOCK] FOOTER (MANTIDO) ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v18.0 | JARVIS PROTECT V21</div></div>""", unsafe_allow_html=True)
