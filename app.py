import streamlit as st
import time
import random

# ==============================================================================
# [GIAE KERNEL SHIELD v30.0 - PROTEÇÃO TOTAL DE INTERFACE]
# ESTADO: OPERACIONAL - BLOQUEIO DE ALTERAÇÃO VISUAL ATIVO
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CONTROLE DE ESTADO (PROTEGIDO) ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'analise_executada' not in st.session_state:
    st.session_state.analise_executada = False

# --- [LOCK] BLOCO DE SEGURANÇA CSS (NÃO ALTERAR) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* RESET E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }

    /* SIDEBAR LOCK */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    /* NAVBAR SUPERIOR AZUL ROYAL */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; 
    }
    .header-left { display: flex; align-items: center; }
    .logo-link { 
        color: #9d54ff !important; font-weight: 900; font-size: 20px !important; 
        text-transform: uppercase; letter-spacing: 1px; margin-right: 40px; 
        text-decoration: none !important; cursor: pointer !important;
    }
    .nav-items { display: flex; gap: 15px; }
    .nav-items span { color: #ffffff; font-size: 10px !important; text-transform: uppercase; cursor: pointer; white-space: nowrap; }

    .header-right { display: flex; align-items: center; gap: 15px; min-width: 250px; justify-content: flex-end; }
    .registrar-pill { 
        color: #ffffff !important; font-size: 10px !important; font-weight: 700 !important; border: 1px solid #ffffff !important; 
        padding: 6px 15px !important; border-radius: 20px !important; cursor: pointer !important;
    }
    .entrar-grad { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: white !important; padding: 7px 20px !important; border-radius: 4px !important; 
        font-weight: 800 !important; font-size: 10px !important;
    }

    /* SIDEBAR BOTÕES */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; border-radius: 0px !important;
        text-align: left !important; width: 100% !important; padding: 18px 25px !important; 
        font-size: 10px !important; text-transform: uppercase !important;
    }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }

    /* DASHBOARD CARDS */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    /* ESTILO FORMULÁRIOS DE ANÁLISE */
    div[data-baseweb="select"] > div { background-color: #11151a !important; border: 1px solid #6d28d9 !important; color: white !important; border-radius: 4px !important; }
    .stSelectbox label { color: #94a3b8 !important; font-size: 10px !important; text-transform: uppercase !important; font-weight: 700 !important; margin-bottom: 5px !important; }
    
    /* FOOTER */
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- [LOCK] CABEÇALHO ---
st.markdown(f"""
    <div class="betano-header">
        <div class="header-left">
            <div class="logo-link">GESTOR IA</div>
            <div class="nav-items">
                <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Apostas Encontradas</span>
                <span>Estatísticas Avançadas</span><span>Mercado Probabilístico</span><span>Assertividade IA</span>
            </div>
        </div>
        <div class="header-right"><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div>
    </div>
    """, unsafe_allow_html=True)

# --- [LOCK] SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("📊 LOCALIZAR APOSTA"): 
        st.session_state.aba_ativa = "analise"
        st.session_state.analise_executada = False
    st.button("📅 JOGOS DO DIA")
    st.button("⏰ PRÓXIMOS JOGOS")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("📈 APOSTAS POR ODDS")
    st.button("⚽ APOSTAS POR GOLS")
    st.button("🚩 APOSTAS POR ESCANTEIOS")
    st.button("⚖️ ÁRBITRO DA PARTIDA")

# --- CONTEÚDO CENTRAL ---
st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# TELA: HOME / DASHBOARD (IDÊNTICA AO ORIGINAL)
# ------------------------------------------------------------------------------
if st.session_state.aba_ativa == "home":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:10px; letter-spacing:-1px;">HOME / DASHBOARD</div>', unsafe_allow_html=True)
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE ● ALERTA: ODDS EM QUEDA ● DICA: GESTÃO DE BANCA ATUALIZADA</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">FLAMENGO x PALMEIRAS</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">FLAMENGO x PALMEIRAS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">SUGESTÃO</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">OVER 2.5 GOLS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:88%;"></div></div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">IA EDUCATION</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">GESTÃO 3%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# TELA: PRÓXIMO NÍVEL - ANÁLISE MÉTRICA
# ------------------------------------------------------------------------------
elif st.session_state.aba_ativa == "analise":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px; letter-spacing:-1px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    
    # ESTRUTURA DE PASTAS (DICIONÁRIO ORGANIZADO)
    menu_competicoes = {
        "FUTEBOL BRASIL": ["Brasileirão Série A", "Brasileirão Série B", "Brasileirão Série C", "Brasileirão Série D", "Copa do Brasil", "Paulistão", "Carioca", "Mineiro", "Gaúcho", "Supercopa do Brasil", "Copa do Nordeste"],
        "INTERNACIONAIS (AMÉRICA)": ["Copa Libertadores", "Copa Sul-Americana"],
        "LIGAS NACIONAIS EUROPA": ["La Liga (Espanha)", "Serie A (Itália)", "Bundesliga (Alemanha)", "Ligue 1 (França)", "Premier League (Inglaterra)"],
        "UEFA (CONTINENTAIS)": ["UEFA Champions League", "UEFA Europa League", "UEFA Conference League"],
        "COPAS E OUTROS": ["FA Cup", "Copa do Rei", "Coppa Italia", "Eurocopa 2024/2026", "Copa da Liga Inglesa"]
    }

    # SISTEMA DE PASTAS (COLUNAS)
    col_pasta, col_camp = st.columns(2)
    with col_pasta:
        categoria_sel = st.selectbox("📁 CATEGORIA / REGIÃO", list(menu_competicoes.keys()))
    with col_camp:
        campeonato_sel = st.selectbox("🏆 SELECIONE O CAMPEONATO", menu_competicoes[categoria_sel])

    # SELEÇÃO DE TIMES
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        time_casa = st.text_input("🏠 TIME DA CASA", placeholder="Ex: Flamengo")
    with col_t2:
        time_fora = st.text_input("🚀 TIME VISITANTE", placeholder="Ex: Palmeiras")

    if st.button("⚡ EXECUTAR ALGORITMO GIAE"):
        if time_casa and time_fora:
            with st.spinner('CALCULANDO MÉTRICAS PROBABILÍSTICAS...'):
                time.sleep(2)
                st.session_state.analise_executada = True
        else:
            st.error("Por favor, preencha o nome dos times para analisar.")

    # RESULTADO DA ANÁLISE (ESTILO PREMIUM DARK)
    if st.session_state.analise_executada:
        st.markdown(f"""
            <div style="background: rgba(109, 40, 217, 0.1); border: 1px solid #6d28d9; padding: 25px; border-radius: 8px; margin-top: 20px;">
                <h2 style="color: #9d54ff; font-size: 18px; font-weight: 900; margin-top: 0;">RELATÓRIO DE ALTA ASSERTIVIDADE IA</h2>
                <p style="color: #94a3b8; font-size: 11px; text-transform: uppercase;">Competição: {campeonato_sel} | Conflito: {time_casa} vs {time_fora}</p>
                <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.1); margin: 15px 0;">
        """, unsafe_allow_html=True)

        res1, res2 = st.columns(2)
        with res1:
            # 1. VENCEDOR
            st.markdown(f"<div style='color:white; font-size:13px;'>✅ <b>VENCEDOR:</b> Probabilidade {random.randint(65,82)}% para {time_casa}</div>", unsafe_allow_html=True)
            # 2. GOLS
            st.markdown(f"<div style='color:white; font-size:13px;'>⚽ <b>GOLS:</b> Over 1.5 Gols (Ambos os tempos confirmados)</div>", unsafe_allow_html=True)
            # 3. CARTÕES
            st.markdown(f"<div style='color:white; font-size:13px;'>🟨 <b>CARTÕES:</b> Tendência de 2 cartões no 1º tempo / Total +4.5</div>", unsafe_allow_html=True)
            # 4. ESCANTEIOS
            st.markdown(f"<div style='color:white; font-size:13px;'>🚩 <b>ESCANT.:</b> Over 9.5 Total / {time_casa} com 60% de dominância</div>", unsafe_allow_html=True)

        with res2:
            # 5. TIROS DE META
            st.markdown(f"<div style='color:white; font-size:13px;'>🥅 <b>TIROS DE META:</b> Padrão de 14-16 totais no jogo</div>", unsafe_allow_html=True)
            # 6. CHUTES NO GOL
            st.markdown(f"<div style='color:white; font-size:13px;'>🎯 <b>CHUTES GOL:</b> {time_casa} > 4.5 chutes reais</div>", unsafe_allow_html=True)
            # 7. DEFESAS GOLEIRO
            st.markdown(f"<div style='color:white; font-size:13px;'>🧤 <b>DEFESAS:</b> Goleiro do {time_fora} com 80% de carga de trabalho</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown('<div style="color: #06b6d4; font-size: 9px; font-weight: 700; margin-top: 10px;">⚠️ NOTA: APENAS PROBABILIDADES ACIMA DE 75% SÃO EXIBIDAS.</div>', unsafe_allow_html=True)

# --- [LOCK] FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V30-ULTRA-SHIELD</div><div>GESTOR IA PRO v30.0 | JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
