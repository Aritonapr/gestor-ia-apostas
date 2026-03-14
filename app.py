import streamlit as st
import time

# ==============================================================================
# [GIAE KERNEL SHIELD v18.0 - PROTOCOLO JARVIS SÉRIE GOLD]
# ESTADO: TOTALMENTE BLINDADO (LARGURA FIXA / BOTÃO INTERATIVO)
# AJUSTES: SIDEBAR LOCK 260PX / ENTRAR CLICK EFFECT
# CHAVE DE SEGURANÇA: GIAE-V17-ELITE-RECOVERY
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DO ESTADO DE NAVEGAÇÃO ---
if 'navegacao_jarvis' not in st.session_state:
    st.session_state.navegacao_jarvis = "home"

# --- [LOCK] BLOCO DE SEGURANÇA CSS (NÃO ALTERAR) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET E FUNDO GERAL */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; overflow: hidden !important; }
    
    /* BLOQUEIO DO ARRASTE DA SIDEBAR (TRAVA DE LARGURA) */
    [data-testid="stSidebar"] { 
        min-width: 260px !important; 
        max-width: 260px !important; 
        width: 260px !important;
        background-color: #11151a !important; 
        border-right: 1px solid #1e293b !important; 
    }
    /* REMOVER O CONTROLE DE REDIMENSIONAMENTO MANUAL */
    [data-testid="stSidebarResizer"] { display: none !important; }

    [data-testid="stSidebarContent"] { overflow: hidden !important; padding-top: 0px !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    /* [02] NAVBAR SUPERIOR AZUL ROYAL (TRAVADA) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; 
        border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between;
        padding: 0 30px !important; z-index: 999999; 
    }
    
    /* LOGO ROXO 22PX */
    .logo-text { 
        color: #9d54ff !important; font-weight: 900; font-size: 22px !important;
        text-transform: uppercase; letter-spacing: 1px !important; margin-right: 30px; white-space: nowrap;
    }

    /* MENU SUPERIOR 11PX CLEAN */
    .nav-items { display: flex; gap: 20px; align-items: center; }
    .nav-items span { 
        color: #ffffff; font-size: 11px !important; font-weight: 400 !important; 
        text-transform: uppercase; letter-spacing: 0.5px !important; cursor: pointer; 
        white-space: nowrap !important; transition: 0.2s;
    }
    .nav-items span:hover { color: #9d54ff; }

    /* BOTÕES DA DIREITA */
    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { 
        color: #ffffff; font-size: 10px; font-weight: 700; text-transform: uppercase; 
        border: 1px solid #ffffff; padding: 6px 18px; border-radius: 20px; cursor: pointer; transition: 0.2s;
    }
    .registrar-pill:active { transform: scale(0.95); background: rgba(255,255,255,0.1); }

    /* BOTÃO ENTRAR COM EFEITO DE CLIQUE ATIVO */
    .entrar-grad {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%);
        color: white; padding: 7px 22px; border-radius: 4px;
        font-weight: 800; font-size: 11px; cursor: pointer; text-transform: uppercase;
        transition: 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        user-select: none;
    }
    .entrar-grad:hover { opacity: 0.9; transform: translateY(-1px); box-shadow: 0 4px 12px rgba(109, 40, 217, 0.3); }
    .entrar-grad:active { 
        transform: scale(0.94); /* EFEITO DE PRESSIONAR */
        filter: brightness(0.8); 
    }

    /* BOTÕES SIDEBAR */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; border-radius: 0px !important;
        text-align: left !important; justify-content: flex-start !important;
        width: 100% !important; padding: 15px 25px !important; font-size: 10px !important; 
        text-transform: uppercase !important; white-space: nowrap !important;
    }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: #1a242d !important; }

    /* CARDS HOME */
    .news-ticker {
        background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px;
        color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 25px;
    }
    .highlight-card {
        background: #11151a; border: 1px solid #1e293b; padding: 25px; border-radius: 8px;
        text-align: center; height: 170px;
    }

    /* BOTÃO EXECUTAR (BRANCO) */
    section.main div.stButton > button {
        background: #ffffff !important; color: #000000 !important; border-radius: 4px !important;
        height: 40px !important; width: 220px !important; font-weight: 800 !important;
        font-size: 11px !important; text-transform: uppercase !important; border: none !important;
    }
    section.main div.stButton > button:active { transform: scale(0.97); }

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
            <div style="color:white; cursor:pointer; font-size:14px; margin-right:5px;">🔍</div>
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- [LOCK] SIDEBAR FIXA EM 260PX ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("📊 LOCALIZAR APOSTA"):
        st.session_state.navegacao_jarvis = "analise"
    if st.button("🏠 HOME / DASHBOARD"):
        st.session_state.navegacao_jarvis = "home"
    
    st.button("📅 JOGOS DO DIA")
    st.button("⏰ PRÓXIMOS JOGOS")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("📈 APOSTAS POR ODDS")
    st.button("⚽ APOSTAS POR GOLS")
    st.button("🚩 APOSTAS POR ESCANTEIOS")
    st.button("⚖️ ÁRBITRO DA PARTIDA")

# --- CONTEÚDO CENTRAL DINÂMICO ---
st.markdown('<div style="height: 85px;"></div>', unsafe_allow_html=True)

if st.session_state.navegacao_jarvis == "home":
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE ● ALERTA: ODDS EM QUEDA ● DICA: GESTÃO DE BANCA ATUALIZADA</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Destaque do Dia</div><div style="color:white; font-size:18px; font-weight:900; margin-top:15px;">FLAMENGO x PALMEIRAS</div><div style="color:#06b6d4; font-size:11px; margin-top:8px;">BRASILEIRÃO - 21:30h</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Sugestão de Mercado</div><div style="color:white; font-size:18px; font-weight:900; margin-top:15px;">OVER 2.5 GOLS</div><div style="color:#00cc66; font-size:11px; margin-top:8px;">CONFIDÊNCIA: 88%</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">IA Education</div><div style="color:white; font-size:18px; font-weight:900; margin-top:15px;">GESTÃO 3%</div><div style="color:#9d54ff; font-size:11px; margin-top:8px;">PRESERVE SEU CAPITAL</div></div>', unsafe_allow_html=True)

elif st.session_state.navegacao_jarvis == "analise":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:5px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:#ffffff; font-size:10px; font-weight:700; margin-bottom:25px; text-transform:uppercase;">Protocolo de Análise Crizal Active</div>', unsafe_allow_html=True)
    # [Filtros Protegidos]
    st.button("EXECUTAR ALGORITMO GIAE")

# --- FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v18.0 | FIXED SIDEBAR & CLICK EFFECT</div></div>""", unsafe_allow_html=True)
