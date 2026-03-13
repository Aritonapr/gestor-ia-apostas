import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v6.3]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS DE ALTA ESPECIFICIDADE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* 1. RESET E TIPOGRAFIA GLOBAL */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { 
        background-color: #0b0e11 !important; 
        color: #e2e8f0 !important; 
        font-family: 'Inter', sans-serif !important; 
    }
    
    /* Ajuste de margem para o conteúdo não ser coberto pela Navbar */
    .main .block-container { padding-top: 60px !important; }

    /* Ajuste da Sidebar para a altura do Header */
    [data-testid="stSidebar"] { 
        background-color: #15191d !important; 
        margin-top: 50px !important; 
        border-right: 1px solid #2d3843 !important;
    }

    /* 2. NAVBAR SUPERIOR (FUNDO LARANJA) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 50px; 
        background-color: #f64d23; 
        display: flex; align-items: center; padding: 0 25px; z-index: 999999; 
    }
    
    .logo-text { 
        color: #ffffff !important; 
        font-weight: 900 !important; 
        font-size: 22px !important; 
        letter-spacing: -1px !important;
        text-transform: uppercase;
        margin-right: 35px;
    }

    /* MENU DE NAVEGAÇÃO */
    .nav-items { 
        display: flex; gap: 20px; flex-grow: 1; 
        color: white; font-size: 11px; font-weight: 700; 
        text-transform: uppercase; 
        letter-spacing: 0.3px;
    }

    /* 3. BOTÕES DA NAVBAR */
    .btn-registrar { 
        border: 1px solid rgba(255,255,255,0.7); 
        color: white; padding: 6px 15px; border-radius: 4px; 
        font-size: 11px; font-weight: 800; cursor: pointer;
        text-transform: uppercase;
    }
    /* BOTÃO ENTRAR VERDE */
    .btn-entrar { 
        background: #00cc66; color: white; padding: 8px 22px; 
        border-radius: 4px; font-weight: 800; border: none; 
        font-size: 11px; cursor: pointer;
        text-transform: uppercase;
    }

    /* 4. SELECTBOXES DARK */
    div[data-baseweb="select"] > div {
        background-color: #1a242d !important;
        border: 1px solid #2d3843 !important;
        border-radius: 4px !important;
    }
    div[data-baseweb="select"] div { color: white !important; font-size: 14px !important; }
    div[data-testid="stSelectbox"] label p {
        color: #94a3b8 !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
    }

    /* 5. BOTÕES CÁPSULA GIAE */
    div[data-testid="stVerticalBlock"] button, .stButton button {
        background-color: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        border: none !important;
    }

    /* FOOTER */
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR ATUALIZADA ---
st.markdown(f"""
    <div class="betano-header">
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-items">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Estatísticas Avançadas</span>
            <span>Mercado Probabilístico</span>
            <span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:12px; align-items:center;">
            <div class="btn-registrar">Registrar</div>
            <div class="btn-entrar">Entrar</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    if st.button("🔥 FERRAMENTA IA"): st.session_state.app_state = "processar"
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL ---
if "app_state" not in st.session_state: st.session_state.app_state = "processar"

if st.session_state.app_state == "processar":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:25px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    
    # Grid de Seleção
    c1, c2, c3 = st.columns(3)
    with c1: st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
    with c2: st.selectbox("CATEGORIA", ["Brasileirão", "Copa do Brasil"])
    with c3: st.selectbox("CAMPEONATO", ["Série A", "Série B"])

    st.markdown("<hr style='border: 0.5px solid #2d3843; opacity: 0.5;'>", unsafe_allow_html=True)
    st.markdown('<div style="color:white; font-weight:700; font-size:18px; margin-top:10px;">Confronto: Série A</div>', unsafe_allow_html=True)
    
    t1, t2 = st.columns(2)
    with t1: st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "Botafogo"])
    with t2: st.selectbox("TIME FORA", ["Flamengo", "Vasco", "Palmeiras"])

    if st.button("PROCESSAR ALGORITMO"):
        with st.status("GIAE IA: Processando...", expanded=False):
            time.sleep(1)
        st.success("🤖 Análise Concluída!")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN V6.3</div><div>GESTOR IA PRO v6.3 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
