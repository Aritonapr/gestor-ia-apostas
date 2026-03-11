import streamlit as st

# 1. Configuração inicial
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. CSS DE ALTA PRECISÃO - FOCO EM ALINHAMENTO SUPERIOR
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap');

    /* 1. ELIMINAÇÃO DE ESPAÇOS NATIVOS DO STREAMLIT */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] {
        display: none !important;
    }

    /* 2. ZERAR PADDING DA PÁGINA INTEIRA */
    .stApp { 
        background-color: #0b0e11 !important; 
        color: #e2e8f0 !important; 
    }

    /* SUBIR O CONTEÚDO CENTRAL */
    [data-testid="stAppViewBlockContainer"] {
        padding-top: 0px !important;
        margin-top: -45px !important; /* Puxa o título central para cima */
    }

    /* --- BARRA SUPERIOR (HEADER FIXO) --- */
    .top-bar {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 60px;
        background-color: #15191d;
        border-bottom: 3px solid #f64d23;
        display: flex; align-items: center;
        padding: 0 25px; z-index: 999999;
    }
    .gestor-logo {
        display: flex; align-items: center; gap: 12px;
        animation: neon-pulse 3s infinite ease-in-out;
    }
    @keyframes neon-pulse {
        0%, 100% { filter: drop-shadow(0 0 2px #f64d23); }
        50% { filter: drop-shadow(0 0 10px #f64d23); }
    }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 22px; font-style: italic; font-family: 'Roboto', sans-serif; }

    /* LINKS DO TOPO */
    .nav-links { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; }
    .nav-links span { color: #ffffff; font-size: 11px; font-weight: 700; text-transform: uppercase; cursor: pointer; opacity: 0.8; }
    .nav-links span:hover { opacity: 1; color: #f64d23; }

    /* --- SIDEBAR: SUBIR O TEXTO PARA O TOPO ABSOLUTO --- */
    [data-testid="stSidebar"] {
        background-color: #15191d !important;
        margin-top: 60px !important; /* Ajustado à altura da barra superior */
        border-right: 1px solid #2d3843 !important;
        width: 260px !important;
    }

    /* REMOVE O VAZIO DO TOPO DA SIDEBAR */
    [data-testid="stSidebarContent"] {
        padding-top: 0px !important; 
        margin-top: -20px !important; /* PUXA OS BOTÕES PARA CIMA */
        overflow-y: hidden !important; 
    }

    /* BOTÕES DA SIDEBAR (TEXTO ENQUADRADO) */
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        color: #e2e8f0 !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        font-weight: 700 !important;
        font-size: 11px !important;
        padding: 8px 15px !important; 
        min-height: 40px !important; 
        width: 100% !important;
        border-radius: 0px !important;
        display: block !important;
        text-transform: uppercase;
        transition: 0.2s;
    }
    [data-testid="stSidebar"] button:hover {
        background-color: #1e293b !important;
        color: #f64d23 !important;
        border-left: 4px solid #f64d23 !important;
    }

    /* --- RODAPÉ FIXO --- */
    .pro-footer {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background-color: #15191d;
        height: 25px; border-top: 1px solid #2d3843;
        display: flex; justify-content: space-between; align-items: center;
        padding: 0 25px; font-size: 9px; color: #94a3b8;
        z-index: 999999;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA BARRA SUPERIOR (HEADER)
st.markdown("""
    <div class="top-bar">
        <div class="gestor-logo">
            <div style="width:28px; height:32px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); box-shadow: 0 0 15px #f64d23;"></div>
            <div class="logo-text">GESTOR IA</div>
        </div>
        <div class="nav-links">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:15px; align-items:center;">
            <div style="color:white; font-size:16px; cursor:pointer;">🔍</div>
            <div style="border:1px solid #adb5bd; color:white; padding:4px 12px; border-radius:4px; font-size:11px; font-weight:bold; cursor:pointer;">REGISTRAR</div>
            <button style="background:#00cc66; color:white; padding:6px 20px; border-radius:4px; font-weight:bold; border:none; font-size:11px; cursor:pointer;">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - OS 8 ITENS DO SEU PAPEL (SUBIDOS)
with st.sidebar:
    # Espaço mínimo apenas para evitar colisão absoluta
    st.button("PROCESSAR ALGORITMO")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. CONTEÚDO PRINCIPAL (ENQUADRADO NO TOPO)
# Usando um container para garantir que o texto central suba junto com a lateral
st.markdown("""
    <div style="margin-top: 20px;">
        <h3 style="color:white; margin:0;">📊 Dashboard de Análise Profissional</h3>
        <p style="color:#94a3b8; font-size:13px;">Interface alinhada: O texto da esquerda subiu para o topo da sidebar.</p>
    </div>
    """, unsafe_allow_html=True)

# 6. RODAPÉ FIXO (TOTALMENTE ALINHADO)
st.markdown("""
    <div class="pro-footer">
        <div>STATUS: <span style="color:#00cc66">● ONLINE</span> | SERVIDOR: CLOUD-IA | LATÊNCIA: 18ms</div>
        <div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div>
    </div>
    """, unsafe_allow_html=True)
