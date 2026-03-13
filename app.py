import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v5.6]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS REFINADO (FOCO NO VISUAL DA IMAGEM) ---
st.markdown("""
    <style>
    /* 1. RESET E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    /* Padding para não cobrir o conteúdo com a Navbar */
    .main .block-container { padding-top: 60px !important; }

    /* 2. NAVBAR SUPERIOR (ESTILO BETANO) */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; margin-right: 30px; }
    .nav-items { display: flex; gap: 20px; flex-grow: 1; color: white; font-size: 10px; font-weight: 700; text-transform: uppercase; }
    .logo-hex { width:18px; height:22px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:8px; }

    /* 3. SIDEBAR (ESTILO MENU LISTA) */
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        width: 260px !important; 
        border-right: 1px solid #2d3843 !important;
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; }

    /* Botão Principal da Sidebar (Laranja) */
    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button {
        background-color: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        height: 55px !important;
        width: 90% !important;
        margin: 20px auto !important;
        font-weight: 900 !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(246, 77, 35, 0.3) !important;
    }

    /* Outros Botões da Sidebar (Links de Menu) */
    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:not(:first-child) button {
        background-color: transparent !important;
        color: #adb5bd !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        justify-content: flex-start !important;
        font-weight: 700 !important;
        font-size: 12px !important;
        padding: 15px 20px !important;
        width: 100% !important;
        border-radius: 0px !important;
    }
    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:not(:first-child) button:hover {
        color: #f64d23 !important;
        background-color: #1a242d !important;
    }

    /* 4. SELECTBOXES DARK (IMPORTANTE PARA O VISUAL) */
    div[data-baseweb="select"] > div {
        background-color: #1a242d !important;
        border: 1px solid #2d3843 !important;
        border-radius: 6px !important;
    }
    div[data-baseweb="select"] div { color: white !important; font-size: 14px !important; }
    div[data-testid="stSelectbox"] label { 
        color: #64748b !important; 
        font-size: 11px !important; 
        text-transform: uppercase; 
        font-weight: 700;
    }

    /* 5. ÁREA CENTRAL */
    .white-title { color: white !important; font-weight: 900; font-size: 28px !important; margin-bottom: 30px !important; }
    .standard-text { color: white !important; font-weight: 700; font-size: 18px !important; margin: 20px 0 !important; }
    
    /* Botão Processar */
    .main .stButton button {
        background-color: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        height: 50px !important;
        width: 280px !important;
        font-weight: 900 !important;
        font-size: 14px !important;
        border: none !important;
        margin-top: 20px !important;
    }

    /* FOOTER */
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown(f"""
    <div class="betano-header">
        <div class="logo-hex"></div>
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-items">
            <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Apostas Encontradas</span><span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:12px; align-items:center;">
            <div style="border:1px solid #adb5bd; color:white; padding:4px 12px; border-radius:3px; font-size:11px; font-weight:bold; cursor:pointer;">REGISTRAR</div>
            <div style="background:#f64d23; color:white; padding:6px 20px; border-radius:3px; font-weight:bold; border:none; font-size:11px; cursor:pointer;">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Mantendo como estava) ---
with st.sidebar:
    if st.button("FERRAMENTA IA"): st.session_state.app_state = "processar"
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL (Configurada para parecer a imagem) ---
if "app_state" not in st.session_state: st.session_state.app_state = "processar"

if st.session_state.app_state == "processar":
    st.markdown('<div class="white-title">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    
    # Grid Superior (3 colunas)
    c1, c2, c3 = st.columns(3)
    with c1: st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
    with c2: st.selectbox("CATEGORIA", ["Brasileirão", "Estaduais"])
    with c3: st.selectbox("CAMPEONATO", ["Série A", "Série B"])

    st.markdown("<div style='margin: 20px 0; border-bottom: 1px solid #2d3843;'></div>", unsafe_allow_html=True)
    
    # Seção Confronto
    st.markdown('<div class="standard-text">Confronto: Série A</div>', unsafe_allow_html=True)
    
    t1, t2 = st.columns(2)
    with t1: st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "São Paulo"])
    with t2: st.selectbox("TIME FORA", ["Flamengo", "Palmeiras", "Corinthians"])

    if st.button("PROCESSAR ALGORITMO"):
        with st.status("GIAE IA: Processando...", expanded=False):
            time.sleep(1)
        st.success("🤖 Análise pronta.")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN V5.6 BLINDADO</div><div>GESTOR IA PRO v5.6 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
