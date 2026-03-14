import streamlit as st
import time

# ==============================================================================
# [GIAE KERNEL SHIELD v25.0 - PROTOCOLO JARVIS SUPREME]
# ESTADO: EXPANSÃO DASHBOARD (GRID 3x2) - CORREÇÃO DE SINTAXE
# FIX: RESTAURAÇÃO TOTAL DE EFEITOS E ALINHAMENTO SUPERIOR
# CHAVE DE SEGURANÇA: GIAE-V17-ELITE-RECOVERY
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CONTROLE DE NAVEGAÇÃO INTERNO ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"

# --- [LOCK] BLOCO DE SEGURANÇA CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; }
    
    [data-testid="stMainBlockContainer"] {
        padding-top: 0rem !important;
        padding-bottom: 1rem !important;
    }

    /* SIDEBAR LOCK (320PX E SEM SCROLLBAR) */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; padding-top: 0px !important; }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }
    [data-testid="stSidebarContent"] { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    [data-testid="stSidebarResizer"] { display: none !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    /* [02] NAVBAR SUPERIOR */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; 
        border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between;
        padding: 0 40px !important; z-index: 999999; 
    }
    
    .logo-text { 
        color: #9d54ff !important; font-weight: 900; font-size: 22px !important;
        text-transform: uppercase; letter-spacing: 1.5px !important; 
        margin-right: 60px !important; white-space: nowrap; cursor: pointer;
    }

    .nav-items { display: flex; gap: 25px; align-items: center; }
    .nav-items span { 
        color: #ffffff; font-size: 11px !important; text-transform: uppercase; 
        letter-spacing: 0.5px !important; cursor: pointer; transition: 0.2s;
    }
    .nav-items span:hover { color: #9d54ff; text-shadow: 0 0 10px #9d54ff; }

    /* HEADER EFEITOS */
    .header-right { display: flex; align-items: center; gap: 20px; }
    .search-icon { color: #ffffff !important; cursor: pointer !important; font-size: 18px !important; transition: 0.3s !important; }
    .search-icon:hover { color: #9d54ff !important; transform: scale(1.2) !important; }
    
    .registrar-pill { 
        color: #ffffff !important; font-size: 10px !important; font-weight: 700 !important; text-transform: uppercase !important; 
        border: 1px solid #ffffff !important; padding: 7px 20px !important; border-radius: 20px !important; cursor: pointer !important; transition: 0.3s !important;
    }
    .registrar-pill:hover { background: #ffffff !important; color: #002366 !important; transform: translateY(-1px); }

    .entrar-grad {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: white !important; padding: 8px 25px !important; border-radius: 4px !important;
        font-weight: 800 !important; font-size: 11px !important; cursor: pointer !important; text-transform: uppercase !important;
        transition: 0.3s !important; box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
    }
    .entrar-grad:hover { filter: brightness(1.2) !important; box-shadow: 0 0 15px rgba(109, 40, 217, 0.4) !important; transform: translateY(-1px); }

    /* [03] SIDEBAR BOTÕES */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; border-radius: 0px !important;
        text-align: left !important; justify-content: flex-start !important;
        width: 100% !important; padding: 18px 25px !important; 
        font-size: 10px !important; text-transform: uppercase !important; 
        white-space: nowrap !important; transition: 0.3s !important;
    }
    [data-testid="stSidebar"] button:hover { 
        color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important;
    }

    /* [04] DASHBOARD CARDS (GRID) */
    .news-ticker {
        background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px;
        color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px;
    }
    .highlight-card {
        background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px;
        text-align: center; height: 140px; transition: 0.3s;
    }
    .highlight-card:hover { border-color: #6d28d9; transform: translateY(-3px); background: #161b22; }

    /* FOOTER */
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- [LOCK] CABEÇALHO ---
st.markdown(f"""
    <div class="betano-header">
        <div style="display:flex; align-items:center;">
            <div class="logo-text">GESTOR IA</div>
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
            <div class="search-icon">🔍</div>
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- [LOCK] SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("📊 LOCALIZAR APOSTA"): st.session_state.aba_ativa = "analise"
    if st.button("🏠 IR PARA O INÍCIO"): st.session_state.aba_ativa = "home"
    st.button("📅 JOGOS DO DIA")
    st.button("⏰ PRÓXIMOS JOGOS")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("📈 APOSTAS POR ODDS")
    st.button("⚽ APOSTAS POR GOLS")
    st.button("🚩 APOSTAS POR ESCANTEIOS")
    st.button("⚖️ ÁRBITRO DA PARTIDA")

# --- CONTEÚDO CENTRAL (6 QUADROS) ---
st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

if st.session_state.aba_ativa == "home":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:10px; letter-spacing:-1px;">HOME / DASHBOARD</div>', unsafe_allow_html=True)
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE ● ALERTA: ODDS EM QUEDA ● DICA: GESTÃO DE BANCA ATUALIZADA</div>', unsafe_allow_html=True)
    
    # LINHA 1
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Destaque do Dia</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">FLAMENGO x PALMEIRAS</div><div style="color:#06b6d4; font-size:10px; margin-top:5px;">BRASILEIRÃO - 21:30h</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Sugestão de Mercado</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">OVER 2.5 GOLS</div><div style="color:#00cc66; font-size:10px; margin-top:5px;">CONFIDÊNCIA: 88%</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">IA Education</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">GESTÃO 3%</div><div style="color:#9d54ff; font-size:10px; margin-top:5px;">PRESERVE SEU CAPITAL</div></div>', unsafe_allow_html=True)

    st.markdown('<div style="height:15px;"></div>', unsafe_allow_html=True) # Espaçador entre linhas

    # LINHA 2
    c4, c5, c6 = st.columns(3)
    with c4: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Tendência de Valor</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">ODDS DESAJUSTADAS</div><div style="color:#facc15; font-size:10px; margin-top:5px;">PREMIER LEAGUE - LIVE</div></div>', unsafe_allow_html=True)
    with c5: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Scanner de Cantos</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">ALTA PRESSÃO (HT)</div><div style="color:#fb7185; font-size:10px; margin-top:5px;">7 PARTIDAS ENCONTRADAS</div></div>', unsafe_allow_html=True)
    with c6: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Performance Semanal</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">ASSERTIVIDADE 92%</div><div style="color:#22c55e; font-size:10px; margin-top:5px;">PROTOCOLO CRIZAL ACTIVE</div></div>', unsafe_allow_html=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:5px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    st.button("EXECUTAR ALGORITMO GIAE")

# --- [LOCK] FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v18.0 | JARVIS PROTECT V21</div></div>""", unsafe_allow_html=True)
