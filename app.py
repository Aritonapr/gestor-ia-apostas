import streamlit as st
import time

# ==============================================================================
# [GIAE KERNEL SHIELD v18.0 - PROTOCOLO JARVIS REFINED]
# ESTADO: ATIVO (ESTRUTURA TRAVADA E PROTEGIDA)
# ALTERAÇÕES: LOGO SPACED / RENOMEAR SIDEBAR / FONT-WEIGHT ADJUST
# CHAVE DE SEGURANÇA: GIAE-V17-ELITE-RECOVERY
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE ESTADO ---
if 'aba_navegacao' not in st.session_state:
    st.session_state.aba_navegacao = "home"

# --- BLOCO DE SEGURANÇA CSS (PROTEÇÃO JARVIS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET TOTAL ANTI-QUEBRA */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { 
        display: none !important; visibility: hidden !important; 
    }
    .stApp { background-color: #0b0e11 !important; overflow: hidden !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; padding-top: 0px !important; }

    /* [02] NAVBAR SUPERIOR (AZUL ROYAL) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 55px; 
        background-color: #002366 !important; 
        border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between;
        padding: 0 25px !important; z-index: 999999; 
    }
    
    /* AJUSTE 1: LOGO COM MAIOR ESPAÇAMENTO */
    .logo-text { 
        color: #9d54ff !important; font-weight: 900; font-size: 17px; 
        text-transform: uppercase; letter-spacing: 2px !important; /* ESPAÇO ADICIONADO */
        margin-right: 25px; 
    }

    .nav-items { display: flex; gap: 18px; align-items: center; }
    
    /* AJUSTE 3: REMOÇÃO DE NEGRITO DOS ITENS ESPECÍFICOS */
    .nav-items span { 
        color: #ffffff; font-size: 9px; 
        font-weight: 400 !important; /* SUAVIZAÇÃO DA FONTE (SEM NEGRITO) */
        text-transform: uppercase; 
        cursor: pointer; white-space: nowrap !important; transition: 0.2s;
    }
    .nav-items span:hover { color: #9d54ff; }

    .header-right { display: flex; align-items: center; gap: 12px; }
    .registrar-pill { 
        color: #ffffff; font-size: 9px; font-weight: 700; text-transform: uppercase; 
        border: 1px solid #ffffff; padding: 5px 15px; border-radius: 20px; cursor: pointer;
    }
    .entrar-grad {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%);
        color: white; padding: 6px 18px; border-radius: 4px;
        font-weight: 800; font-size: 10px; cursor: pointer; text-transform: uppercase;
    }

    /* [03] SIDEBAR (GRAFITE - ANTI-QUEBRA) */
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
        min-width: 260px !important;
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { 
        margin-top: -45px !important; gap: 0px !important; 
    }
    
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; border-radius: 0px !important;
        text-align: left !important; justify-content: flex-start !important;
        width: 100% !important; padding: 14px 25px 14px 20px !important; 
        font-size: 10px !important; text-transform: uppercase !important; 
        white-space: nowrap !important;
    }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: #1a242d !important; }

    /* [04] DASHBOARD CENTRAL */
    .dashboard-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; }
    
    section.main div.stButton > button {
        background: #ffffff !important; color: #000000 !important; border-radius: 4px !important;
        height: 40px !important; width: 220px !important; font-weight: 800 !important;
        font-size: 11px !important; text-transform: uppercase !important; border: none !important;
    }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO (AZUL ROYAL - AJUSTES JARVIS) ---
st.markdown(f"""
    <div class="betano-header">
        <div style="display:flex; align-items:center;">
            <div class="logo-text">GESTOR &nbsp; IA</div>
            <div class="nav-items">
                <span>Apostas Esportivas</span>
                <span>Apostas ao Vivo</span>
                <span>Apostas Encontradas</span>
                <span>Estatísticas Avançadas</span>
                <span>Mercado Probabilístico</span>
                <span>Assertividade IA</span>
            </div>
        </div>
        <div class="header-right">
            <div style="color:white; cursor:pointer; font-size:12px; margin-right:5px;">🔍</div>
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (AJUSTE 2: RENOMEAR LOCALIZAR APOSTA) ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("📊 LOCALIZAR APOSTA"): # NOME ATUALIZADO
        st.session_state.aba_navegacao = "analise"
    if st.button("🏠 HOME / DASHBOARD"):
        st.session_state.aba_navegacao = "home"
    
    st.button("📅 JOGOS DO DIA")
    st.button("⏰ PRÓXIMOS JOGOS")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("📈 APOSTAS POR ODDS")
    st.button("⚽ APOSTAS POR GOLS")
    st.button("🚩 APOSTAS POR ESCANTEIOS")
    st.button("⚖️ ÁRBITRO DA PARTIDA")

# --- CONTEÚDO ---
st.markdown('<div style="height: 70px;"></div>', unsafe_allow_html=True)

if st.session_state.aba_navegacao == "home":
    st.markdown('<div style="color:white; font-weight:900; font-size:24px; margin-bottom:15px;">DASHBOARD DE TENDÊNCIAS IA</div>', unsafe_allow_html=True)
    st.markdown('<div style="background: rgba(0, 35, 102, 0.1); border: 1px solid #1e293b; padding: 8px; color: #06b6d4; font-size: 9px; font-weight: 700; margin-bottom: 20px;">● NEWS: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="dashboard-card"><div style="color:#64748b; font-size:8px; text-transform:uppercase;">Destaque</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">FLAMENGO x PALMEIRAS</div><div style="color:#06b6d4; font-size:10px; margin-top:5px;">SÉRIE A - 21:30h</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="dashboard-card"><div style="color:#64748b; font-size:8px; text-transform:uppercase;">Sugestão</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">OVER 2.5 GOLS</div><div style="color:#00cc66; font-size:10px; margin-top:5px;">CONFIDÊNCIA: 88%</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="dashboard-card"><div style="color:#64748b; font-size:8px; text-transform:uppercase;">IA Education</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">GESTÃO 3%</div><div style="color:#9d54ff; font-size:10px; margin-top:5px;">PRESERVE SEU CAPITAL</div></div>', unsafe_allow_html=True)

elif st.session_state.aba_navegacao == "analise":
    st.markdown('<div style="color:white; font-weight:900; font-size:24px; margin-bottom:5px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:#ffffff; font-size:10px; font-weight:700; margin-bottom:25px; text-transform:uppercase;">Protocolo de Análise Crizal Active</div>', unsafe_allow_html=True)
    # Filtros e botão "Executar" protegidos aqui
    st.button("EXECUTAR ALGORITMO GIAE")

# --- FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v18.0 | JARVIS OPTIMIZED</div></div>""", unsafe_allow_html=True)
