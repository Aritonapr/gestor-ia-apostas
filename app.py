import streamlit as st

# ==============================================================================
# [PROTOCOLO v61.5 - RESTAURAÇÃO TOTAL IMAGEM v58 - ESTABILIDADE VISUAL]
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- ESTILO CSS EXATO DA IMAGEM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
    
    /* RESET DE SCROLLBAR */
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; background-color: #0b0e11 !important; }

    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 80px 30px 20px 30px !important; }

    /* HEADER SUPERIOR (BARRA AZUL) */
    .top-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 65px; 
        background-color: #000c29 !important; border-bottom: 1px solid rgba(255,255,255,0.05); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 9999999;
    }
    .logo { color: #9d54ff; font-weight: 900; font-size: 24px; text-transform: uppercase; letter-spacing: -1px; }
    .nav-items { display: flex; gap: 20px; color: #cbd5e1; font-size: 9.5px; font-weight: 700; text-transform: uppercase; }
    .btn-reg { color: white; border: 1.5px solid white; border-radius: 20px; padding: 6px 20px; font-size: 9px; font-weight: 800; }
    .btn-ent { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 8px 25px; border-radius: 5px; font-weight: 800; font-size: 10px; }

    /* SIDEBAR (LISTA DE BOTÕES) */
    [data-testid="stSidebar"] { min-width: 300px !important; background-color: #0b0e11 !important; border-right: 1px solid #1e293b !important; }
    
    /* BOTÃO 1 - GOLD */
    [data-testid="stSidebar"] div.stButton > button:first-of-type {
        background: linear-gradient(135deg, #bf953f, #fcf6ba, #b38728, #fcf6ba, #aa771c) !important;
        color: #000 !important; font-weight: 900 !important; border: 1px solid #fff5b7 !important;
        border-radius: 6px !important; height: 45px !important; margin-bottom: 15px !important;
        position: relative; overflow: hidden; box-shadow: 0 4px 12px rgba(184, 134, 11, 0.3) !important;
    }
    [data-testid="stSidebar"] div.stButton > button:first-of-type::after {
        content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
        background: linear-gradient(to right, transparent, rgba(255,255,255,0.5), transparent);
        transform: rotate(45deg); animation: shine 3s infinite;
    }
    @keyframes shine { 0% { transform: translateX(-150%) rotate(45deg); } 100% { transform: translateX(150%) rotate(45deg); } }

    /* OUTROS 7 BOTÕES SIDEBAR */
    [data-testid="stSidebar"] div.stButton > button:not(:first-of-type) {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        text-align: left !important; width: 100% !important; padding: 12px 0px !important;
        font-size: 11px !important; font-weight: 600 !important; text-transform: uppercase !important;
        border-bottom: 1px solid rgba(255,255,255,0.03) !important; border-radius: 0 !important;
    }
    [data-testid="stSidebar"] div.stButton > button:not(:first-of-type):hover { color: white !important; }

    /* GRID DE CARDS (v58) */
    .v58-card {
        background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px;
        text-align: center; height: 125px; display: flex; flex-direction: column; justify-content: center;
    }
    .v58-card-highlight { border: 1px solid #6d28d9 !important; box-shadow: 0 0 15px rgba(109, 40, 217, 0.15); }
    .v58-label { color: #64748b; font-size: 8.5px; font-weight: 800; text-transform: uppercase; margin-bottom: 12px; }
    .v58-value { color: white; font-size: 18px; font-weight: 900; }
    .v58-bar-bg { background: #1e293b; height: 3px; width: 80%; border-radius: 10px; margin: 15px auto 0 auto; }
    .v58-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; border-radius: 10px; }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0b0e11; height: 30px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SUPERIOR ---
st.sidebar.markdown("""
    <div class="top-header">
        <div class="logo">GESTOR IA</div>
        <div class="nav-items">
            <span>APOSTAS ESPORTIVAS</span><span>APOSTAS AO VIVO</span><span>APOSTAS ENCONTRADAS</span>
            <span>ESTATÍSTICAS AVANÇADAS</span><span>MERCADO PROBABILÍSTICO</span><span>ASSERTIVIDADE IA</span>
        </div>
        <div style="display:flex; gap:12px; align-items:center;">
            <div class="btn-reg">REGISTRAR</div>
            <div class="btn-ent">ENTRAR</div>
        </div>
    </div>
    <div style="height:80px;"></div>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVEGAÇÃO (8 BOTÕES) ---
with st.sidebar:
    st.button("📅 BILHETE OURO")
    st.button("🎯 SCANNER PRÉ-LIVE")
    st.button("📡 SCANNER EM TEMPO REAL")
    st.button("💰 GESTÃO DE BANCA")
    st.button("📜 HISTÓRICO DE CALLS")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("⚽ APOSTAS POR GOLS")
    st.button("🚩 APOSTAS POR ESCANTEIOS")

# --- CONTEÚDO PRINCIPAL ---
st.markdown("<h2 style='color:white; font-weight:900; margin-bottom:30px;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)

# GRID DE 8 CARDS EXATOS DA IMAGEM
r1_c1, r1_c2, r1_c3, r1_c4 = st.columns(4)
with r1_c1:
    st.markdown('<div class="v58-card"><div class="v58-label">BANCA ATUAL</div><div class="v58-value">R$ 1.000,00</div><div class="v58-bar-bg"><div class="v58-bar-fill" style="width:45%;"></div></div></div>', unsafe_allow_html=True)
with r1_c2:
    st.markdown('<div class="v58-card"><div class="v58-label">ASSERTIVIDADE</div><div class="v58-value">92.4%</div><div class="v58-bar-bg"><div class="v58-bar-fill" style="width:92%;"></div></div></div>', unsafe_allow_html=True)
with r1_c3:
    st.markdown('<div class="v58-card v58-card-highlight"><div class="v58-label">SUGESTÃO</div><div class="v58-value">OVER 2.5</div><div class="v58-bar-bg"><div class="v58-bar-fill" style="width:65%;"></div></div></div>', unsafe_allow_html=True)
with r1_c4:
    st.markdown('<div class="v58-card"><div class="v58-label">IA STATUS</div><div class="v58-value">ONLINE</div><div class="v58-bar-bg"><div class="v58-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)

st.write("") # Espaço entre linhas

r2_c1, r2_c2, r2_c3, r2_c4 = st.columns(4)
with r2_c1:
    st.markdown('<div class="v58-card"><div class="v58-label">VOL. GLOBAL</div><div class="v58-value">ALTO</div><div class="v58-bar-bg"><div class="v58-bar-fill" style="width:85%;"></div></div></div>', unsafe_allow_html=True)
with r2_c2:
    st.markdown('<div class="v58-card"><div class="v58-label">STAKE PADRÃO</div><div class="v58-value">1.0%</div><div class="v58-bar-bg"><div class="v58-bar-fill" style="width:25%;"></div></div></div>', unsafe_allow_html=True)
with r2_c3:
    st.markdown('<div class="v58-card"><div class="v58-label">VALOR ENTRADA</div><div class="v58-value">R$ 10,00</div><div class="v58-bar-bg"><div class="v58-bar-fill" style="width:50%;"></div></div></div>', unsafe_allow_html=True)
with r2_c4:
    st.markdown('<div class="v58-card"><div class="v58-label">SISTEMA</div><div class="v58-value">JARVIS v58.00</div><div class="v58-bar-bg"><div class="v58-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v58.00</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
