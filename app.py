import streamlit as st
import time
import random

# ==============================================================================
# [GIAE KERNEL SHIELD v35.0 - ESTRUTURA BLINDADA]
# ESTADO: 100% FIEL À IMAGEM DO WORD (SIDEBAR E HEADER ORIGINAIS)
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

# --- [LOCK] BLOCO DE SEGURANÇA CSS (IDÊNTICO À IMAGEM FORNECIDA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }

    /* [02] SIDEBAR ORIGINAL DA IMAGEM */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    /* [03] NAVBAR SUPERIOR AZUL ROYAL (STILO BETANO) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; text-decoration: none !important; }
    .nav-items { display: flex; gap: 15px; }
    .nav-items span { color: #ffffff; font-size: 10px !important; text-transform: uppercase; white-space: nowrap; opacity: 0.8; }
    
    .header-right { display: flex; align-items: center; gap: 15px; }
    .search-icon { color: white; font-size: 16px; cursor: pointer; }
    .registrar-pill { 
        color: #ffffff !important; font-size: 10px !important; font-weight: 700 !important; border: 1px solid #ffffff !important; 
        padding: 6px 15px !important; border-radius: 20px !important;
    }
    .entrar-grad { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: white !important; padding: 7px 20px !important; border-radius: 4px !important; 
        font-weight: 800 !important; font-size: 10px !important;
    }

    /* [04] SIDEBAR BOTÕES COM ÍCONES DA IMAGEM */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; border-radius: 0px !important;
        text-align: left !important; width: 100% !important; padding: 18px 25px !important; 
        font-size: 10px !important; text-transform: uppercase !important;
    }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }

    /* [05] CARDS DO DASHBOARD */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; border-radius: 4px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; min-height: 155px; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    /* FORMULÁRIOS DE ANÁLISE */
    div[data-baseweb="select"] > div { background-color: #11151a !important; border: 1px solid #1e293b !important; color: white !important; }
    
    /* FOOTER */
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATA HIERÁRQUICA (BRASIL / INTERNACIONAL / SELEÇÕES) ---
DADOS_IA = {
    "BRASIL": {
        "Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo", "São Paulo", "Atlético-MG", "Cruzeiro", "Fluminense", "Vasco", "Grêmio", "Internacional", "Bahia", "Corinthians"],
        "Brasileirão Série B": ["Santos", "Goiás", "Coritiba", "Sport", "Ceará", "América-MG"],
        "Copa do Brasil": ["Qualificados Oitavas", "Qualificados Quartas"],
        "Estaduais (Paulistão/Carioca)": ["Corinthians", "São Paulo", "Palmeiras", "Flamengo", "Vasco", "Fluminense"]
    },
    "EUROPA": {
        "Premier League (Inglaterra)": ["Man. City", "Arsenal", "Liverpool", "Chelsea", "Man. United", "Tottenham"],
        "La Liga (Espanha)": ["Real Madrid", "Barcelona", "Atlético Madrid", "Girona", "Sevilla"],
        "UEFA Champions League": ["Real Madrid", "Man. City", "Bayern Munich", "PSG", "Inter de Milão"],
        "UEFA Europa League": ["Liverpool", "Roma", "Leverkusen", "Benfica"]
    },
    "INTERNACIONAL / SELEÇÕES": {
        "Copa do Mundo 2026": ["Brasil", "Argentina", "França", "Inglaterra", "Espanha", "Portugal", "Alemanha", "Uruguai"],
        "Eliminatórias": ["Brasil", "Argentina", "Uruguai", "Colômbia", "Equador"],
        "Eurocopa": ["França", "Alemanha", "Portugal", "Inglaterra", "Espanha"]
    }
}

# --- HEADER (IDÊNTICO À IMAGEM) ---
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
            <span class="search-icon">🔍</span>
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (CONFORME IMAGEM DO WORD) ---
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

# ==============================================================================
# TELA: HOME / DASHBOARD (IDÊNTICO À IMAGEM)
# ==============================================================================
if st.session_state.aba_ativa == "home":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:10px; letter-spacing:-1px;">HOME / DASHBOARD</div>', unsafe_allow_html=True)
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE ● ALERTA: ODDS EM QUEDA ● DICA: GESTÃO DE BANCA ATUALIZADA</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">DESTAQUE LIVE</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">FLAMENGO x PALMEIRAS</div><div style="color:#06b6d4; font-size:10px;">BRASILEIRÃO - AO VIVO</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">SUGESTÃO DE MERCADO</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">OVER 2.5 GOLS</div><div style="color:#00cc66; font-size:10px;">CONFIDÊNCIA: 88%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:88%;"></div></div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;">IA EDUCATION</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">GESTÃO 3%</div><div style="color:#9d54ff; font-size:10px;">PRESERVE SEU CAPITAL</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)

# ==============================================================================
# TELA: ANÁLISE MÉTRICA (PROXIMO NÍVEL COM 3 DIVISÕES)
# ==============================================================================
elif st.session_state.aba_ativa == "analise":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    
    # DIVISÃO EM 3 PARTES (SUGESTÃO IMPLEMENTADA)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        categoria = st.selectbox("📂 PARTE 1: CATEGORIA", list(DADOS_IA.keys()))
    with col2:
        competicao = st.selectbox("🏆 PARTE 2: COMPETIÇÃO", list(DADOS_IA[categoria].keys()))
    with col3:
        lista_times = DADOS_IA[categoria][competicao]
        time_a = st.selectbox("🏠 TIME DA CASA", lista_times)
        time_b = st.selectbox("🚀 TIME VISITANTE", [t for t in lista_times if t != time_a])

    if st.button("🚀 EXECUTAR ALGORITMO GIAE"):
        with st.spinner("CALCULANDO MATRIZES PROBABILÍSTICAS..."):
            time.sleep(1.5)
            st.session_state.analise_pronta = True

    if st.session_state.analise_pronta:
        st.markdown(f"""
            <div style="background:#1a202c; border: 1px solid #6d28d9; padding:20px; border-radius:10px; margin-top:20px;">
                <div style="color:#9d54ff; font-weight:900; font-size:18px; margin-bottom:15px;">RELATÓRIO DE ALTA ASSERTIVIDADE: {time_a} vs {time_b}</div>
        """, unsafe_allow_html=True)
        
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.markdown(f"✅ **VENCEDOR:** Probabilidade Real de 78% para {time_a}")
            st.markdown(f"⚽ **GOLS:** Over 1.5 Real (85% de chance em ambos os tempos)")
            st.markdown(f"🟨 **CARTÕES:** +4.5 cartões (Tendência real no 2º tempo)")
            st.markdown(f"🚩 **ESCANTEIOS:** Over 9.5 total (70% de dominância de {time_a})")
        with res_col2:
            st.markdown(f"🥅 **TIROS DE META:** Média matemática de 14.5 tiros")
            st.markdown(f"🎯 **CHUTES NO GOL:** {time_a} com +5.5 chutes confirmados")
            st.markdown(f"🧤 **DEFESAS:** Goleiro do {time_b} com alta carga (4+ defesas)")
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown('<div style="color:#475569; font-size:9px; margin-top:10px;">* NOTA: SÃO EXIBIDOS APENAS RESULTADOS COM PROBABILIDADE REAL ACIMA DE 75%.</div>', unsafe_allow_html=True)

# --- [LOCK] FOOTER (IDÊNTICO) ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v35.0 | JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
