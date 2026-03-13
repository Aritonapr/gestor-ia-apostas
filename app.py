import streamlit as st
import time

# ==============================================================================
# [GIAE KERNEL SHIELD v18.0 - PROTOCOLO DE NAVEGAÇÃO E ESTADOS]
# ESTADO: ATIVO (ESTRUTURA BLINDADA | CABEÇALHO INTERATIVO)
# LÓGICA: HOME (CARDS) -> APOSTAS (MÉTRICAS)
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DO ESTADO DE NAVEGAÇÃO ---
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = "home"

# --- BLOCO DE SEGURANÇA CSS (MODIFICADO APENAS PARA EFEITOS DE BOTÃO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');

    /* [01] RESET E FUNDO GERAL */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { 
        display: none !important; visibility: hidden !important; 
    }
    .stApp { background-color: #0b0e11 !important; }
    [data-testid="stSidebarContent"] { padding-top: 0px !important; }

    /* [02] NAVBAR SUPERIOR (AZUL ROYAL - PRESERVADO) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 55px; 
        background-color: #002366 !important; 
        border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; 
        padding: 0 40px !important; 
        z-index: 999999; 
    }
    .logo-text { 
        color: #9d54ff !important; 
        font-weight: 900; font-size: 20px; 
        text-transform: uppercase; margin-right: 40px; 
        letter-spacing: -1px; 
    }
    
    /* EFEITO NOS TEXTOS DO MENU */
    .nav-items span { 
        color: #ffffff; font-size: 10px; font-weight: 700; 
        text-transform: uppercase; letter-spacing: 0.8px; 
        margin-right: 20px; cursor: pointer; transition: 0.3s;
    }
    .nav-items span:hover { color: #9d54ff !important; text-shadow: 0 0 10px rgba(157, 84, 255, 0.5); }

    .header-right { display: flex; align-items: center; gap: 15px; }
    
    /* EFEITO BOTÃO REGISTRAR (CIRCULAR) */
    .registrar-btn { 
        color: #ffffff; font-size: 10px; font-weight: 700; 
        text-transform: uppercase; cursor: pointer;
        border: 1px solid #ffffff; padding: 6px 15px; 
        border-radius: 20px; transition: 0.3s;
    }
    .registrar-btn:hover { background: white; color: #002366; }

    /* EFEITO BOTÃO ENTRAR */
    .entrar-btn {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%);
        color: white; padding: 7px 20px; border-radius: 4px;
        font-weight: 800; font-size: 11px; cursor: pointer;
        text-transform: uppercase; transition: 0.3s;
    }
    .entrar-btn:hover { opacity: 0.8; transform: scale(1.05); }

    /* [03] SIDEBAR (GRAFITE - PRESERVADO) */
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        border-right: 1px solid #1e293b !important;
        margin-top: 50px !important;
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { 
        margin-top: -65px !important; gap: 0px !important; 
    }
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important;
        border-radius: 0px !important; text-align: left !important;
        justify-content: flex-start !important; width: 100% !important;
        padding: 15px 25px !important; font-size: 11px !important;
        text-transform: uppercase !important;
    }
    [data-testid="stSidebar"] button:hover { 
        color: #ffffff !important; background-color: #1a242d !important;
        border-left: 4px solid #6d28d9 !important; 
    }

    /* [04] BOTÃO EXECUTAR (BRANCO IDENTICO À FOTO) */
    section.main div.stButton > button {
        background: #ffffff !important; color: #000000 !important;
        border-radius: 4px !important; height: 40px !important; 
        width: 220px !important; font-weight: 800 !important;
        font-size: 12px !important; text-transform: uppercase !important;
        border: none !important; margin-top: 15px !important;
    }

    /* CARDS DASHBOARD */
    .highlight-card {
        background: #11151a; border: 1px solid #1e293b;
        padding: 20px; border-radius: 8px; text-align: center;
        height: 160px;
    }

    /* FOOTER */
    .betano-footer { 
        position: fixed; bottom: 0; left: 0; width: 100%; 
        background-color: #0d0d12 !important; height: 25px; 
        border-top: 1px solid #1e293b; display: flex; 
        justify-content: space-between; align-items: center; 
        padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO FIXO ---
st.markdown(f"""
    <div class="betano-header">
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-items">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Estatísticas Avançadas</span>
        </div>
        <div class="header-right">
            <div class="registrar-btn">REGISTRAR</div>
            <div class="entrar-btn">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (COM GATILHO DE NAVEGAÇÃO) ---
with st.sidebar:
    if st.button("📊 APOSTAS ESPORTIVAS"):
        st.session_state.pagina_ativa = "apostas"
    if st.button("🏠 HOME / DASHBOARD"):
        st.session_state.pagina_ativa = "home"
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("ÁRBITRO DA PARTIDA")

# --- CONTEÚDO DINÂMICO ---
st.markdown('<div style="height: 60px;"></div>', unsafe_allow_html=True)

# [CENÁRIO A] - APENAS DASHBOARD (HOME)
if st.session_state.pagina_ativa == "home":
    st.markdown('<div style="color:white; font-weight:900; font-size:24px; margin-bottom:20px;">DASHBOARD DE TENDÊNCIAS IA</div>', unsafe_allow_html=True)
    st.markdown('<div style="background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; margin-bottom: 20px;">● NEWS: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Destaque</div><div style="color:white; font-size:18px; font-weight:900; margin-top:15px;">FLAMENGO x PALMEIRAS</div><div style="color:#06b6d4; font-size:11px; margin-top:5px;">SERIE A - 21:30h</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Sugestão</div><div style="color:white; font-size:18px; font-weight:900; margin-top:15px;">OVER 2.5 GOLS</div><div style="color:#00cc66; font-size:11px; margin-top:5px;">CONFIDÊNCIA: 88%</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">IA Education</div><div style="color:white; font-size:18px; font-weight:900; margin-top:15px;">GESTÃO 3%</div><div style="color:#9d54ff; font-size:11px; margin-top:5px;">PRESERVE SEU CAPITAL</div></div>""", unsafe_allow_html=True)

# [CENÁRIO B] - ANÁLISE MÉTRICA (LIBERADO AO CLICAR)
elif st.session_state.pagina_ativa == "apostas":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:5px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:#ffffff; font-size:10px; font-weight:700; margin-bottom:25px; text-transform:uppercase;">Protocolo de Análise Crizal Active</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1: st.selectbox("REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
    with c2: st.selectbox("CATEGORIA", ["Brasileirão", "Copa do Brasil"])
    with c3: st.selectbox("CAMPEONATO", ["Série A", "Série B"])

    st.markdown("<hr style='border: 0.1px solid #1e293b; margin: 20px 0;'>", unsafe_allow_html=True)

    t1, t2 = st.columns(2)
    with t1: st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "Botafogo"])
    with t2: st.selectbox("TIME FORA", ["Flamengo", "Vasco", "Palmeiras"])

    if st.button("EXECUTAR ALGORITMO GIAE"):
        with st.status("🤖 Processando Métricas...", expanded=False):
            time.sleep(1)
        st.success("Análise Metrics Concluída!")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v18.0 | DYNAMIC NAVIGATION ACTIVE</div></div>""", unsafe_allow_html=True)
