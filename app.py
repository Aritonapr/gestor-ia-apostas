import streamlit as st

# 1. Configuração inicial
st.set_page_config(page_title="GESTOR IA - PRO", layout="wide", initial_sidebar_state="expanded")

# 2. CSS DE ALTA PERFORMANCE E DESIGN FUTURISTA
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap');

    /* CONFIGURAÇÃO GLOBAL - REMOVER SCROLLBARS ONDE POSSÍVEL */
    html, body, [class*="st-"] {
        font-family: 'Roboto', sans-serif !important;
        font-size: 13px !important;
    }
    
    /* ESCONDER SCROLLBAR DA SIDEBAR */
    [data-testid="stSidebarContent"] {
        overflow: hidden !important; /* Mata a barra de rolagem lateral */
        padding-top: 0rem !important; /* Sobe o texto ao limite */
    }

    /* REMOVER HEADER NATIVO */
    [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"], header, [data-testid="stHeader"] {
        display: none !important;
    }

    .stApp { background-color: #f0f2f5 !important; }

    /* --- NAVBAR SUPERIOR --- */
    .custom-navbar {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 50px;
        background-color: #1a242d;
        border-bottom: 2px solid #f64d23;
        display: flex; align-items: center;
        padding: 0 15px; z-index: 999999;
    }

    /* --- LOGO CYBER-HEXAGON (Efeito Futurista Avançado) --- */
    .logo-container {
        display: flex; align-items: center; gap: 12px;
    }
    .cyber-hex {
        position: relative;
        width: 32px; height: 32px;
        background: #f64d23;
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 0 15px rgba(246, 77, 35, 0.6);
    }
    .cyber-hex::before {
        content: '';
        position: absolute;
        width: 110%; height: 110%;
        border: 2px solid #f64d23;
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
        animation: rotate-hex 4s linear infinite;
    }
    @keyframes rotate-hex {
        0% { transform: rotate(0deg); opacity: 0.5; }
        50% { transform: rotate(180deg); opacity: 1; }
        100% { transform: rotate(360deg); opacity: 0.5; }
    }
    .hexagon-inner {
        width: 22px; height: 26px;
        background-color: #1a242d;
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
        display: flex; align-items: center; justify-content: center;
    }
    .gestor-ia-text {
        color: #f64d23; font-weight: 900; font-size: 19px;
        letter-spacing: -0.5px; font-style: italic;
        text-shadow: 0 0 5px rgba(246, 77, 35, 0.3);
    }

    /* --- MENU SUPERIOR COMPACTO --- */
    .nav-links { display: flex; gap: 15px; flex-grow: 1; margin-left: 20px; }
    .nav-links span {
        color: #ffffff; font-size: 10.5px; font-weight: 700;
        text-transform: uppercase; cursor: pointer;
    }

    /* --- SIDEBAR ULTRA COMPACTA (Symmetry Fix) --- */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important; margin-top: 50px !important;
        border-right: 1px solid #e1e4e8 !important; width: 240px !important;
    }
    /* Estilo dos Botões - Redução drástica de padding para subir o texto */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #1a242d !important;
        border: none !important; border-bottom: 1px solid #f8f9fa !important;
        text-align: left !important; font-weight: 500 !important;
        font-size: 11.5px !important;
        padding: 6px 15px !important; /* Reduzi de 8px para 6px */
        min-height: 38px !important; /* Altura compacta */
        width: 100% !important; border-radius: 0px !important;
        display: block !important;
    }
    [data-testid="stSidebar"] button:hover {
        background-color: #f6f7f9 !important; color: #f64d23 !important;
        border-left: 3px solid #f64d23 !important;
    }

    /* --- CONTEÚDO --- */
    .main-content { margin-top: 65px; padding: 15px; }

    /* --- FOOTER FIXO NO FUNDO --- */
    .custom-footer {
        background-color: #1a242d; color: #6b7280;
        padding: 15px; text-align: center; font-size: 9px;
        border-top: 1px solid #2d3843;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA NAVBAR SUPERIOR
st.markdown("""
    <div class="custom-navbar">
        <div class="logo-container">
            <div class="cyber-hex"><div class="hexagon-inner"><div style="width:10px; height:12px; background:#f64d23; clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);"></div></div></div>
            <div class="gestor-ia-text">GESTOR IA</div>
        </div>
        <div class="nav-links">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:10px; align-items:center;">
            <div style="border:1px solid #adb5bd; color:white; padding:3px 10px; border-radius:3px; font-size:10px; font-weight:bold; cursor:pointer;">REGISTRAR</div>
            <button style="background:#00cc66; color:white; padding:4px 15px; border-radius:3px; font-weight:bold; border:none; font-size:10px; cursor:pointer;">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - PALAVRAS DO PAPEL SUBIDAS E ENQUADRADAS
with st.sidebar:
    # A ordem exata do seu papel, com espaçamento reduzido
    st.button("PROCESSAR ALGORITMO")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. CONTEÚDO PRINCIPAL
st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.markdown("### 💠 Interface de Alta Performance Ativada")
st.info("O conteúdo acima foi comprimido para garantir visibilidade total sem rolagem.")

col1, col2 = st.columns(2)
with col1:
    st.selectbox("Mercado de Análise", ["Escanteios HT", "Gols FT", "Vencedor IA"], label_visibility="collapsed")
with col2:
    st.button("INICIAR SCANNER", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 6. RODAPÉ COMPACTO
st.markdown("""
    <div class="custom-footer">
        <p>© 2023 GESTOR IA. PERFORMANCE ANALYTICS. 18+ JOGUE COM RESPONSABILIDADE.</p>
    </div>
    """, unsafe_allow_html=True)
