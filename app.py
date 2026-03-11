import streamlit as st

# 1. Configuração inicial
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. CSS PARA DIFERENCIAR O "PROCESSAR ALGORITMO"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap');

    /* ANIMAÇÃO PARA O BOTÃO FERRAMENTA */
    @keyframes pulse-orange {
        0% { box-shadow: 0 0 0 0 rgba(246, 77, 35, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(246, 77, 35, 0); }
        100% { box-shadow: 0 0 0 0 rgba(246, 77, 35, 0); }
    }

    /* ELIMINAR TUDO DO STREAMLIT */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] {
        display: none !important;
    }

    .stApp { 
        background-color: #0b0e11 !important; 
        color: #e2e8f0 !important; 
        font-family: 'Roboto', sans-serif !important;
    }

    /* --- BARRA SUPERIOR FIXA --- */
    .betano-header {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 50px;
        background-color: #1a242d;
        border-bottom: 2px solid #f64d23;
        display: flex; align-items: center;
        padding: 0 20px; z-index: 999999;
    }

    /* LOGO PULSANTE */
    .gestor-logo-container { display: flex; align-items: center; gap: 12px; }
    .pulsing-hex {
        width: 22px; height: 25px; background: #f64d23; 
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
        animation: pulse-hex 2s infinite ease-in-out;
    }
    @keyframes pulse-hex {
        0%, 100% { transform: scale(0.9); filter: drop-shadow(0 0 2px #f64d23); }
        50% { transform: scale(1.1); filter: drop-shadow(0 0 10px #f64d23); }
    }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }

    /* --- SIDEBAR CORRIGIDA --- */
    [data-testid="stSidebar"] {
        background-color: #15191d !important;
        margin-top: 50px !important;
        border-right: 1px solid #2d3843 !important;
        width: 260px !important;
    }
    [data-testid="stSidebarContent"] { padding-top: 0px !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; }

    /* --- ESTILIZAÇÃO DO BOTÃO "FERRAMENTA" (O PRIMEIRO) --- */
    /* Usamos um seletor para pegar o primeiro botão da sidebar */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button {
        background: linear-gradient(90deg, #f64d23 0%, #ff8c00 100%) !important;
        color: white !important;
        border: none !important;
        font-weight: 900 !important;
        font-size: 12px !important;
        height: 50px !important;
        margin-bottom: 15px !important; /* Espaço para separar das categorias */
        box-shadow: 0 4px 15px rgba(246, 77, 35, 0.3) !important;
        animation: pulse-orange 2s infinite;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::before {
        content: '⚡ '; /* Ícone de ferramenta/energia */
    }

    /* ESTILO DOS OUTROS BOTÕES (CATEGORIAS) */
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        color: #e2e8f0 !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        font-weight: 700 !important;
        font-size: 11px !important;
        padding: 10px 15px !important; 
        min-height: 40px !important;
        width: 100% !important;
        border-radius: 0px !important;
        text-transform: uppercase;
    }
    [data-testid="stSidebar"] button:hover {
        color: #f64d23 !important;
        background-color: #1e293b !important;
    }

    /* CONTEÚDO CENTRAL */
    .main .block-container { padding-top: 60px !important; }

    /* RODAPÉ */
    .betano-footer {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843;
        display: flex; justify-content: space-between; align-items: center;
        padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVBAR SUPERIOR
st.markdown("""
    <div class="betano-header">
        <div class="gestor-logo-container">
            <div class="pulsing-hex"></div>
            <div class="logo-text">GESTOR IA</div>
        </div>
        <div style="display:flex; gap:20px; margin-left:30px; flex-grow:1; color:white; font-size:11px; font-weight:700; text-transform:uppercase;">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:12px; align-items:center;">
            <div style="border:1px solid #adb5bd; color:white; padding:4px 12px; border-radius:3px; font-size:11px; font-weight:bold; cursor:pointer;">REGISTRAR</div>
            <button style="background:#00cc66; color:white; padding:6px 20px; border-radius:3px; font-weight:bold; border:none; font-size:11px; cursor:pointer;">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - COM DIFERENCIAÇÃO DA FERRAMENTA
with st.sidebar:
    # O primeiro botão agora herda o estilo "FERRAMENTA"
    st.button("PROCESSAR ALGORITMO")
    
    # Os demais seguem o estilo "CATEGORIA"
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. CONTEÚDO PRINCIPAL
st.markdown("### 📊 Dashboard de Análise Profissional")
st.info("Observe a lateral: O 'PROCESSAR ALGORITMO' agora está destacado como a ferramenta principal do sistema.")

# 6. RODAPÉ
st.markdown("""
    <div class="betano-footer">
        <div>STATUS: ● ONLINE | SISTEMA IA ATIVO</div>
        <div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div>
    </div>
    """, unsafe_allow_html=True)
