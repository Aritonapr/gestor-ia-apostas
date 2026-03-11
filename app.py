import streamlit as st

# 1. Configuração inicial
st.set_page_config(page_title="GESTOR IA - PRO", layout="wide", initial_sidebar_state="expanded")

# 2. CSS "BLINDADO" COM ESTILO BETANO E LOGO FUTURISTA
st.markdown("""
    <style>
    /* IMPORTAÇÃO DE FONTE SIMILAR À DA BETANO */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700;900&display=swap');

    /* CONFIGURAÇÃO GLOBAL DE FONTE */
    html, body, [class*="st-"] {
        font-family: 'Roboto', sans-serif !important;
    }

    /* REMOVER ELEMENTOS STREAMLIT */
    [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"], header, [data-testid="stHeader"] {
        display: none !important;
    }

    .stApp { background-color: #f0f2f5 !important; }

    /* --- NAVBAR SUPERIOR --- */
    .custom-navbar {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 65px;
        background-color: #1a242d;
        border-bottom: 3px solid #f64d23;
        display: flex; align-items: center;
        padding: 0 20px; z-index: 999999;
    }

    /* --- LOGO FUTURISTA --- */
    @keyframes logo-glow {
        0% { filter: drop-shadow(0 0 2px #f64d23); }
        50% { filter: drop-shadow(0 0 10px #f64d23); }
        100% { filter: drop-shadow(0 0 2px #f64d23); }
    }
    .logo-container {
        display: flex; align-items: center; gap: 15px; margin-right: 40px;
        animation: logo-glow 3s infinite ease-in-out;
    }
    .hexagon-logo {
        width: 35px; height: 38px;
        background: linear-gradient(135deg, #f64d23, #ff8c00);
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
        display: flex; align-items: center; justify-content: center;
    }
    .hexagon-inner {
        width: 25px; height: 28px; background-color: #1a242d;
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
    }
    .gestor-ia-text {
        color: #f64d23; font-weight: 900; font-size: 24px;
        letter-spacing: -0.5px; text-transform: uppercase; font-style: italic;
    }

    /* --- LINKS SUPERIORES (FONTE BETANO) --- */
    .nav-links { display: flex; gap: 20px; flex-grow: 1; }
    .nav-links span {
        color: #ffffff !important; font-size: 13px; font-weight: 700;
        text-transform: uppercase; cursor: pointer; letter-spacing: 0.2px;
    }

    /* --- SIDEBAR (PADRÃO DE ESPAÇAMENTO BETANO) --- */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important; margin-top: 65px !important;
        border-right: 1px solid #e1e4e8 !important; min-width: 280px !important;
    }
    /* Estilo dos Botões da Sidebar */
    [data-testid="stSidebar"] button {
        background-color: white !important; color: #1a242d !important;
        border: none !important; border-bottom: 1px solid #f0f2f5 !important;
        text-align: left !important; font-weight: 500 !important;
        font-size: 13.5px !important; padding: 12px 20px !important; /* Espaçamento idêntico Betano */
        width: 100% !important; border-radius: 0px !important; display: block !important;
        transition: 0.2s;
    }
    [data-testid="stSidebar"] button:hover {
        background-color: #f6f7f9 !important; color: #f64d23 !important;
    }

    /* --- CONTEÚDO PRINCIPAL --- */
    .main-content { margin-top: 85px; padding: 25px; min-height: 80vh; }

    /* --- RODAPÉ --- */
    .custom-footer {
        background-color: #1a242d; color: #adb5bd;
        padding: 40px 20px; text-align: center; font-size: 12px;
        border-top: 1px solid #2d3843; margin-top: 50px;
    }
    .footer-links { margin-bottom: 15px; display: flex; justify-content: center; gap: 20px; }
    .footer-links span { cursor: pointer; }
    .footer-links span:hover { color: white; }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA NAVBAR
st.markdown("""
    <div class="custom-navbar">
        <div class="logo-container">
            <div class="hexagon-logo"><div class="hexagon-inner"></div></div>
            <div class="gestor-ia-text">GESTOR IA</div>
        </div>
        <div class="nav-links">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:15px; align-items:center;">
            <span style="color:white; font-size:18px;">🔍</span>
            <div style="border:1px solid #adb5bd; color:white; padding:5px 15px; border-radius:4px; font-size:12px; font-weight:bold;">REGISTRAR</div>
            <button style="background:#00cc66; color:white; padding:7px 20px; border-radius:4px; font-weight:bold; border:none; font-size:12px;">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - COM AS PALAVRAS DO SEU PAPEL
with st.sidebar:
    if 'page' not in st.session_state: st.session_state.page = "home"
    
    if st.button("PROCESSAR ALGORITMO"): st.session_state.page = "processar"
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. CONTEÚDO PRINCIPAL
st.markdown('<div class="main-content">', unsafe_allow_html=True)

if st.session_state.page == "home":
    st.subheader("Bem-vindo ao GESTOR IA")
    st.write("Selecione uma opção na lateral para iniciar a análise.")

elif st.session_state.page == "processar":
    st.markdown("### 🏟️ Configuração do Algoritmo")
    camp = st.selectbox("Selecione o Campeonato:", ["Selecione...", "BRASIL", "ESPANHA", "INGLATERRA"])
    if camp != "Selecione...":
        col1, col2 = st.columns(2)
        with col1: st.selectbox("Mandante", ["Time A", "Time B"])
        with col2: st.selectbox("Visitante", ["Time C", "Time D"])
        st.button("🚀 EXECUTAR ANÁLISE")

st.markdown('</div>', unsafe_allow_html=True)

# 6. RODAPÉ (FOOTER)
st.markdown("""
    <div class="custom-footer">
        <div class="footer-links">
            <span>Sobre Nós</span>
            <span>Regras de Apostas</span>
            <span>Política de Privacidade</span>
            <span>IA Responsável</span>
        </div>
        <div style="margin-bottom:10px;">
            <span style="font-size:18px; margin: 0 10px;">⚽</span>
            <span style="font-size:18px; margin: 0 10px;">🏀</span>
            <span style="font-size:18px; margin: 0 10px;">🎾</span>
        </div>
        <p>© 2023 GESTOR IA. Todos os direitos reservados. Inteligência Artificial aplicada ao Esporte.</p>
    </div>
    """, unsafe_allow_html=True)
