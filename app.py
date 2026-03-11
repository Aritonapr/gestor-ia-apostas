import streamlit as st

# 1. Configuração inicial
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. CSS DE ALTA PRECISÃO (Ajuste de Simetria e Verticalidade)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap');

    /* TEMA DARK PROFISSIONAL */
    :root {
        --bg-dark: #0b0e11;
        --bg-sidebar: #15191d;
        --accent-orange: #f64d23;
        --accent-green: #00cc66;
        --text-main: #e2e8f0;
        --text-dim: #94a3b8;
        --nav-height: 50px;
        --footer-height: 25px;
    }

    /* REMOVER TUDO DO STREAMLIT */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] {
        display: none !important;
    }

    .stApp { 
        background-color: var(--bg-dark) !important; 
        color: var(--text-main) !important; 
        font-family: 'Roboto', sans-serif !important; 
    }

    /* --- NAVBAR SUPERIOR --- */
    .pro-navbar {
        position: fixed;
        top: 0; left: 0; width: 100%; height: var(--nav-height);
        background-color: var(--bg-sidebar);
        border-bottom: 2px solid var(--accent-orange);
        display: flex; align-items: center;
        padding: 0 20px; z-index: 999999;
    }

    .logo-box { display: flex; align-items: center; gap: 10px; }
    .cyber-hex {
        width: 28px; height: 32px;
        background: var(--accent-orange);
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 0 15px rgba(246, 77, 35, 0.4);
    }
    .hexagon-inner {
        width: 18px; height: 22px; background-color: var(--bg-sidebar);
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
    }
    .logo-text { color: var(--accent-orange); font-weight: 900; font-size: 18px; font-style: italic; }

    .nav-links { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; }
    .nav-links span { color: var(--text-main); font-size: 11px; font-weight: 700; text-transform: uppercase; cursor: pointer; opacity: 0.8; }

    /* --- SIDEBAR CORRIGIDA --- */
    [data-testid="stSidebar"] {
        background-color: var(--bg-sidebar) !important;
        margin-top: var(--nav-height) !important;
        border-right: 1px solid #2d3843 !important;
        width: 260px !important;
    }
    [data-testid="stSidebarContent"] { padding-top: 0px !important; overflow: hidden !important; }

    /* BOTÕES DA LATERAL */
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        color: var(--text-main) !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        font-weight: 700 !important;
        font-size: 11px !important;
        padding: 6px 15px !important; 
        min-height: 35px !important; 
        width: 100% !important;
        border-radius: 0px !important;
        display: block !important;
        text-transform: uppercase;
    }
    [data-testid="stSidebar"] button:hover {
        background-color: #1e293b !important;
        color: var(--accent-orange) !important;
        border-left: 3px solid var(--accent-orange) !important;
    }

    /* --- CONTEÚDO PRINCIPAL (AJUSTE DE DISTÂNCIA E SIMETRIA) --- */
    .main-container { 
        margin-top: 55px; /* Quase encostado na barra superior */
        padding: 20px 25px;
        min-height: calc(100vh - 110px); /* Ocupa o espaço até o rodapé */
        display: flex;
        flex-direction: column;
    }

    /* Estilização do Dashboard Title */
    .dashboard-header {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 5px;
        border-bottom: 1px solid #1e293b;
        padding-bottom: 10px;
    }

    /* --- RODAPÉ FIXO --- */
    .pro-footer {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background-color: var(--bg-sidebar);
        height: var(--footer-height);
        padding: 0 20px; border-top: 1px solid #2d3843;
        display: flex; justify-content: space-between; align-items: center;
        font-size: 9px; color: var(--text-dim);
        z-index: 9999;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA NAVBAR SUPERIOR
st.markdown("""
    <div class="pro-navbar">
        <div class="logo-box">
            <div class="cyber-hex"><div class="hexagon-inner"></div></div>
            <div class="logo-text">GESTOR IA</div>
        </div>
        <div class="nav-links">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:15px; align-items:center;">
            <div style="color:white; font-size:14px; cursor:pointer;">🔍</div>
            <div style="border:1px solid var(--text-dim); color:white; padding:3px 12px; border-radius:3px; font-size:10px; font-weight:bold; cursor:pointer;">REGISTRAR</div>
            <button style="background:var(--accent-green); color:white; padding:5px 18px; border-radius:3px; font-weight:bold; border:none; font-size:10px; cursor:pointer;">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - OS 8 ITENS DO SEU PAPEL
with st.sidebar:
    if 'view' not in st.session_state: st.session_state.view = "home"
    
    if st.button("PROCESSAR ALGORITMO"): st.session_state.view = "processar"
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. CONTEÚDO PRINCIPAL (COM AJUSTE DE POSICIONAMENTO)
st.markdown('<div class="main-container">', unsafe_allow_html=True)

if st.session_state.view == "home":
    # Cabeçalho do Dashboard mais alto e limpo
    st.markdown("""
        <div class="dashboard-header">
            <span style="font-size: 24px;">📊</span>
            <h2 style="margin: 0; color: white; font-size: 22px;">Dashboard de Análise Profissional</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='color:#94a3b8; font-size:13px; margin-top: 10px;'>Sistema configurado. Interface simétrica enquadrada entre o cabeçalho e o rodapé.</p>", unsafe_allow_html=True)
    
    # Criando uma área vazia que "empurra" o rodapé, mantendo o enquadramento
    st.write("") 
    st.write("")

elif st.session_state.view == "processar":
    st.markdown("<h3 style='color:var(--accent-orange); margin-top:0;'>🤖 Processar Algoritmo IA</h3>", unsafe_allow_html=True)
    # Conteúdo de processamento aqui

st.markdown('</div>', unsafe_allow_html=True)

# 6. RODAPÉ FIXO (ALINHADO AO FUNDO)
st.markdown("""
    <div class="pro-footer">
        <div>STATUS: <span style="color:var(--accent-green)">● ONLINE</span> | SERVIDOR: PRINCIPAL | DADOS: LIVE</div>
        <div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div>
    </div>
    """, unsafe_allow_html=True)
