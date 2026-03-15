import streamlit as st
import time
import random

# ==============================================================================
# [GIAE KERNEL SHIELD v38.0 - ESTRUTURA BLINDADA]
# FIX: SIMETRIA SIDEBAR | ESPAÇAMENTO HEADER | HIERARQUIA 3 NÍVEIS
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

# --- [LOCK] BLOCO DE SEGURANÇA CSS (AJUSTE DE SIMETRIA E ESPAÇAMENTO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }

    /* [02] SIDEBAR - AJUSTE DE SIMETRIA TOTAL */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { 
        margin-top: -30px !important; 
        gap: 0px !important; 
        padding-left: 0px !important; 
        padding-right: 0px !important; 
    }

    /* [03] NAVBAR SUPERIOR - AJUSTE DE DISTÂNCIA LOGO/MENU */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 40px !important; z-index: 999999; 
    }
    .header-left { display: flex; align-items: center; }
    
    .logo-link { 
        color: #9d54ff !important; font-weight: 900; font-size: 22px !important; 
        text-transform: uppercase; letter-spacing: 1px; 
        margin-right: 80px !important; /* DISTÂNCIA AUMENTADA PARA NÃO ENCOSTAR */
        text-decoration: none !important; 
    }
    
    .nav-items { display: flex; gap: 20px; align-items: center; }
    .nav-items span { color: #ffffff; font-size: 10px !important; text-transform: uppercase; white-space: nowrap; opacity: 0.8; }

    .header-right { display: flex; align-items: center; gap: 20px; }
    .search-icon { color: white; font-size: 16px; opacity: 0.7; }
    .registrar-pill { color: white; font-size: 10px; font-weight: 700; border: 1px solid white; padding: 6px 18px; border-radius: 20px; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 7px 25px; border-radius: 4px; font-weight: 800; font-size: 10px; }

    /* [04] BOTÕES SIDEBAR - SIMETRIA REFORÇADA */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1e293b !important; border-radius: 0px !important;
        text-align: left !important; width: 100% !important; 
        padding: 20px 30px !important; /* PADDING IGUAL PARA SIMETRIA */
        font-size: 11px !important; text-transform: uppercase !important;
        display: flex !important; align-items: center !important;
    }
    [data-testid="stSidebar"] button:hover { 
        color: #ffffff !important; 
        border-left: 5px solid #6d28d9 !important; 
        background: rgba(255, 255, 255, 0.03) !important; 
    }

    /* CARDS DASHBOARD */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 160px; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    /* ESTILO SELECTS */
    div[data-baseweb="select"] > div { background-color: #11151a !important; border: 1px solid #1e293b !important; color: white !important; }
    
    /* FOOTER */
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DADOS HIERÁRQUICA (EXEMPLO MELHORADO) ---
DADOS_IA = {
    "BRASIL": {
        "Estadual": {
            "Paulistão": ["Palmeiras", "São Paulo", "Corinthians", "Santos", "RB Bragantino"],
            "Carioca": ["Flamengo", "Fluminense", "Vasco", "Botafogo"]
        },
        "Nacional": {
            "Brasileirão Série A": ["Flamengo", "Botafogo", "Palmeiras", "Fortaleza", "Cruzeiro"],
            "Copa do Brasil": ["Vasco", "Atlético-MG", "Flamengo", "Corinthians"]
        }
    },
    "INGLATERRA": {
        "Nacional": {
            "Premier League": ["Man City", "Arsenal", "Liverpool", "Chelsea"],
            "FA Cup": ["Man United", "Tottenham", "Newcastle"]
        }
    },
    "INTERNACIONAL": {
        "Seleções": {
            "Copa do Mundo 2026": ["Brasil", "França", "Argentina", "Espanha"],
            "Eurocopa": ["Alemanha", "Portugal", "Inglaterra"]
        }
    }
}

# --- HEADER ---
st.markdown(f"""
    <div class="betano-header">
        <div class="header-left">
            <div class="logo-link">GESTOR IA</div>
            <div class="nav-items">
                <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Apostas Encontradas</span>
                <span>Estatísticas Avançadas</span><span>Mercado Probabilístico</span><span>Assertividade IA</span>
            </div>
        </div>
        <div class="header-right">
            <span class="search-icon">🔍</span>
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (SIMETRIA TOTAL) ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("📊 LOCALIZAR APOSTA"): st.session_state.aba_ativa = "analise"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    st.button("⏰ PRÓXIMOS JOGOS")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("✅ APOSTAS POR ODDS")
    st.button("⚽ APOSTAS POR GOLS")
    st.button("🚩 APOSTAS POR ESCANTEIOS")
    st.button("⚖️ ÁRBITRO DA PARTIDA")

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- HOME / DASHBOARD ---
if st.session_state.aba_ativa == "home":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:10px;">HOME / DASHBOARD</div>', unsafe_allow_html=True)
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">FLAMENGO x PALMEIRAS</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">FLAMENGO x PALMEIRAS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">SUGESTÃO</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">OVER 2.5 GOLS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:88%;"></div></div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">GESTÃO</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">GESTÃO 3%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)

# --- ANÁLISE MÉTRICA (HIERARQUIA SOLICITADA) ---
elif st.session_state.aba_ativa == "analise":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        pais = st.selectbox("🌎 CATEGORIA (PAÍS)", list(DADOS_IA.keys()))
    with col2:
        tipo = st.selectbox("📂 TIPO DE COMPETIÇÃO", list(DADOS_IA[pais].keys()))
    with col3:
        campeonato = st.selectbox("🏆 CAMPEONATO", list(DADOS_IA[pais][tipo].keys()))

    col_t1, col_t2 = st.columns(2)
    with col_t1:
        time_a = st.selectbox("🏠 TIME DA CASA", DADOS_IA[pais][tipo][campeonato])
    with col_t2:
        time_b = st.selectbox("🚀 TIME VISITANTE", [t for t in DADOS_IA[pais][tipo][campeonato] if t != time_a])

    if st.button("🚀 EXECUTAR ALGORITMO GIAE"):
        with st.spinner("CALCULANDO MÉTRICAS..."):
            time.sleep(1.5)
            st.session_state.analise_pronta = True

    if st.session_state.analise_pronta:
        st.markdown(f'<div style="background:#1a202c; border: 1px solid #6d28d9; padding:20px; border-radius:10px; margin-top:20px;">', unsafe_allow_html=True)
        st.markdown(f'<div style="color:#9d54ff; font-weight:900; font-size:18px; margin-bottom:15px;">RELATÓRIO: {time_a} vs {time_b} ({campeonato})</div>', unsafe_allow_html=True)
        r1, r2 = st.columns(2)
        with r1:
            st.markdown(f"✅ **VENCEDOR:** {time_a} (Prob. 76%)")
            st.markdown(f"⚽ **GOLS:** Over 1.5 Real")
            st.markdown(f"🟨 **CARTÕES:** +4.5 total")
            st.markdown(f"🚩 **ESCANTEIOS:** Over 9.5")
        with r2:
            st.markdown(f"🥅 **TIROS DE META:** 14 médios")
            st.markdown(f"🎯 **CHUTES GOL:** +5.5 casa")
            st.markdown(f"🧤 **DEFESAS:** 4+ goleiro visitante")
        st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v38.0 | JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
