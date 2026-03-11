import streamlit as st

# 1. Configuração inicial
st.set_page_config(page_title="GESTOR IA - PRO", layout="wide", initial_sidebar_state="expanded")

# 2. CSS DE ALTA PRECISÃO (ESTILO BETANO UI/UX)
st.markdown("""
    <style>
    /* IMPORTAÇÃO DA FONTE ROBOTO (PADRÃO GOOGLE/BETANO) */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap');

    /* CONFIGURAÇÃO GLOBAL: Redução de escala para simetria */
    html, body, [class*="st-"] {
        font-family: 'Roboto', sans-serif !important;
        font-size: 13px !important; /* Tamanho base menor para caber tudo */
    }

    /* REMOVER ELEMENTOS NATIVOS */
    [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"], header, [data-testid="stHeader"] {
        display: none !important;
    }

    .stApp { background-color: #f0f2f5 !important; }

    /* --- NAVBAR SUPERIOR (MAIS FINA E COMPACTA) --- */
    .custom-navbar {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 55px;
        background-color: #1a242d;
        border-bottom: 3px solid #f64d23;
        display: flex; align-items: center;
        padding: 0 20px; z-index: 999999;
    }

    /* --- LOGO FUTURISTA COM GLOW --- */
    @keyframes neon-glow {
        0% { filter: drop-shadow(0 0 2px #f64d23); transform: scale(1); }
        50% { filter: drop-shadow(0 0 8px #f64d23); transform: scale(1.02); }
        100% { filter: drop-shadow(0 0 2px #f64d23); transform: scale(1); }
    }
    .logo-container {
        display: flex; align-items: center; gap: 10px; margin-right: 30px;
        animation: neon-glow 4s infinite ease-in-out;
    }
    .hexagon {
        width: 28px; height: 32px;
        background: linear-gradient(135deg, #f64d23, #ff8c00);
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
        display: flex; align-items: center; justify-content: center;
    }
    .hexagon-inner {
        width: 20px; height: 24px; background-color: #1a242d;
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
    }
    .gestor-ia-text {
        color: #f64d23; font-weight: 900; font-size: 20px;
        letter-spacing: -0.8px; font-style: italic;
    }

    /* --- MENU SUPERIOR (FONTE PEQUENA E NEGRI TO) --- */
    .nav-links { display: flex; gap: 18px; flex-grow: 1; }
    .nav-links span {
        color: #ffffff; font-size: 11px; font-weight: 700;
        text-transform: uppercase; cursor: pointer; letter-spacing: 0.1px;
    }

    /* --- SIDEBAR (EXTREMAMENTE COMPACTA - SIMETRIA BETANO) --- */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important; margin-top: 55px !important;
        border-right: 1px solid #e1e4e8 !important; width: 250px !important;
    }
    /* Estilo da lista de botões lateral */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #1a242d !important;
        border: none !important; border-bottom: 1px solid #f3f4f6 !important;
        text-align: left !important; font-weight: 500 !important;
        font-size: 12px !important; /* Fonte menor */
        padding: 8px 15px !important; /* Padding reduzido para não rolar */
        min-height: 40px !important;
        width: 100% !important; border-radius: 0px !important;
        display: block !important; transition: 0.2s;
    }
    [data-testid="stSidebar"] button:hover {
        background-color: #f9fafb !important; color: #f64d23 !important;
    }

    /* --- CONTEÚDO PRINCIPAL --- */
    .main-content { margin-top: 75px; padding: 20px; min-height: 70vh; }

    /* --- RODAPÉ (MINIMALISTA E ENQUADRADO) --- */
    .custom-footer {
        background-color: #1a242d; color: #6b7280;
        padding: 20px; text-align: center; 
        font-size: 10px; /* Fonte bem pequena profissional */
        border-top: 1px solid #2d3843; margin-top: 30px;
    }
    .footer-links { margin-bottom: 10px; display: flex; justify-content: center; gap: 15px; text-transform: uppercase; font-weight: bold; }
    .footer-links span:hover { color: white; cursor: pointer; }

    /* Ajuste para o conteúdo central não ficar muito largo */
    .stSelectbox label { font-size: 12px !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA NAVBAR (TOPO)
st.markdown("""
    <div class="custom-navbar">
        <div class="logo-container">
            <div class="hexagon"><div class="hexagon-inner"></div></div>
            <div class="gestor-ia-text">GESTOR IA</div>
        </div>
        <div class="nav-links">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:12px; align-items:center;">
            <span style="color:#adb5bd; font-size:16px;">🔍</span>
            <div style="border:1px solid #adb5bd; color:white; padding:4px 12px; border-radius:3px; font-size:11px; font-weight:bold; cursor:pointer;">REGISTRAR</div>
            <button style="background:#00cc66; color:white; padding:5px 18px; border-radius:3px; font-weight:bold; border:none; font-size:11px; cursor:pointer;">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - COM AS PALAVRAS DO SEU PAPEL (ENQUADRADAS)
with st.sidebar:
    if 'page' not in st.session_state: st.session_state.page = "home"
    
    st.button("PROCESSAR ALGORITMO") # Sem comando de page para simplificar o visual
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. CONTEÚDO PRINCIPAL (REDUZIDO PARA SIMETRIA)
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.markdown("### 🏟️ Bem-vindo ao GESTOR IA")
st.write("Layout otimizado para visualização completa sem barra de rolagem lateral.")

# Exemplo de enquadramento de seleção
col1, col2 = st.columns(2)
with col1:
    st.selectbox("Campeonato", ["BRASIL - SÉRIE A", "ESPANHA - LA LIGA"], label_visibility="collapsed")
with col2:
    st.button("BUSCAR CONFRONTOS", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# 6. RODAPÉ (TEXTO PEQUENO E PROFISSIONAL)
st.markdown("""
    <div class="custom-footer">
        <div class="footer-links">
            <span>Sobre Nós</span>
            <span>Regras</span>
            <span>Privacidade</span>
            <span>Suporte IA</span>
        </div>
        <p>© 2023 GESTOR IA. PERFORMANCE E INTELIGÊNCIA ESPORTIVA PROFISSIONAL.</p>
        <p style="margin-top:5px; color:#4b5563;">18+ Jogue com responsabilidade.</p>
    </div>
    """, unsafe_allow_html=True)
