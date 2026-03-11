import streamlit as st

# 1. Configuração inicial - TRAVA TOTAL DE LAYOUT
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. CSS "BLINDADO" DARK MODE PROFISSIONAL
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap');

    /* TEMA DARK PROFISSIONAL - CORES DE TERMINAL */
    :root {
        --bg-dark: #0b0e11; /* Cinza quase preto (Fundo) */
        --bg-sidebar: #15191d; /* Cinza grafite (Sidebar) */
        --accent-orange: #f64d23; /* Laranja (Marca/Alerta) */
        --accent-green: #00cc66; /* Verde (Lucro/Entrada) */
        --text-main: #e2e8f0; /* Branco acinzentado (Leitura) */
        --text-dim: #94a3b8; /* Cinza (Suporte) */
    }

    /* REMOVER TUDO DO STREAMLIT */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] {
        display: none !important;
        visibility: hidden !important;
    }

    /* FUNDO DA APLICAÇÃO */
    .stApp {
        background-color: var(--bg-dark) !important;
        color: var(--text-main) !important;
        font-family: 'Roboto', sans-serif !important;
    }

    /* --- BARRA SUPERIOR (NAVBAR) --- */
    .pro-navbar {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 50px;
        background-color: var(--bg-sidebar);
        border-bottom: 2px solid var(--accent-orange);
        display: flex; align-items: center;
        padding: 0 20px; z-index: 999999;
    }

    /* LOGO CYBER-HEX NEON */
    .logo-box {
        display: flex; align-items: center; gap: 10px;
    }
    .cyber-hex {
        width: 28px; height: 32px;
        background: var(--accent-orange);
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 0 15px rgba(246, 77, 35, 0.4);
        animation: pulse-glow 3s infinite ease-in-out;
    }
    @keyframes pulse-glow {
        0%, 100% { filter: drop-shadow(0 0 2px var(--accent-orange)); }
        50% { filter: drop-shadow(0 0 8px var(--accent-orange)); }
    }
    .hexagon-inner {
        width: 18px; height: 22px; background-color: var(--bg-sidebar);
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
    }
    .logo-text {
        color: var(--accent-orange); font-weight: 900; font-size: 18px;
        letter-spacing: -0.5px; font-style: italic;
    }

    /* LINKS SUPERIORES */
    .nav-links { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; }
    .nav-links span {
        color: var(--text-main); font-size: 11px; font-weight: 700;
        text-transform: uppercase; cursor: pointer; opacity: 0.8;
    }
    .nav-links span:hover { opacity: 1; color: var(--accent-orange); }

    /* --- SIDEBAR (ALTA DENSIDADE / SEM ROLAGEM) --- */
    [data-testid="stSidebar"] {
        background-color: var(--bg-sidebar) !important;
        margin-top: 50px !important;
        border-right: 1px solid #2d3843 !important;
        width: 240px !important;
    }
    [data-testid="stSidebarContent"] {
        overflow: hidden !important; /* MATA O SCROLL */
        padding-top: 0px !important;
    }

    /* BOTÕES DA SIDEBAR (ESTILO TERMINAL) */
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        color: var(--text-main) !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        font-weight: 500 !important;
        font-size: 11px !important; /* Fonte menor para simetria */
        padding: 8px 15px !important;
        width: 100% !important;
        border-radius: 0px !important;
        display: block !important;
        transition: 0.2s;
        text-transform: uppercase;
    }
    [data-testid="stSidebar"] button:hover {
        background-color: #1e293b !important;
        color: var(--accent-orange) !important;
        border-left: 3px solid var(--accent-orange) !important;
    }

    /* --- ÁREA PRINCIPAL (COCKPIT) --- */
    .main-container {
        margin-top: 70px;
        padding: 0 25px;
    }
    
    /* Customizando Selectbox e inputs para Dark Mode */
    .stSelectbox label { color: var(--text-dim) !important; font-size: 10px !important; text-transform: uppercase; }
    div[data-baseweb="select"] { background-color: #1e293b !important; border-radius: 4px !important; }

    /* --- RODAPÉ (FOOTER) --- */
    .pro-footer {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background-color: var(--bg-sidebar);
        padding: 5px 20px; border-top: 1px solid #2d3843;
        display: flex; justify-content: space-between;
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
            <div style="color:var(--text-dim); font-size:14px;">🔍</div>
            <div style="border:1px solid var(--text-dim); color:white; padding:3px 12px; border-radius:3px; font-size:10px; font-weight:bold; cursor:pointer;">REGISTRAR</div>
            <button style="background:var(--accent-green); color:white; padding:5px 18px; border-radius:3px; font-weight:bold; border:none; font-size:10px; cursor:pointer;">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - OS 8 ITENS DO SEU PAPEL (ENQUADRADOS)
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

# 5. CONTEÚDO PRINCIPAL (DENTRO DA DIV DE MARGEM)
st.markdown('<div class="main-container">', unsafe_allow_html=True)

if st.session_state.view == "home":
    st.markdown("<h2 style='color:white; margin-bottom:5px;'>📊 Dashboard de Análise</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;'>Sistema pronto para processamento. Selecione uma opção na lateral.</p>", unsafe_allow_html=True)

elif st.session_state.view == "processar":
    st.markdown("<h3 style='color:var(--accent-orange);'>🤖 Processar Algoritmo IA</h3>", unsafe_allow_html=True)
    
    # Exemplo de Dashboard Compacto (O que virá depois)
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        st.selectbox("CAMPEONATO", ["BRASIL - SÉRIE A", "INGLATERRA - PREMIER LEAGUE"])
    with col2:
        st.selectbox("CONFRONTO", ["Flamengo vs Palmeiras", "Man City vs Arsenal"])
    with col3:
        st.write("") # Espaçador
        st.button("ANALISAR", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# 6. RODAPÉ FIXO (PADRÃO TRADING)
st.markdown("""
    <div class="pro-footer">
        <div>STATUS: <span style="color:var(--accent-green)">● CONECTADO</span> | DADOS: LIVE API | LATÊNCIA: 24ms</div>
        <div>GESTOR IA v3.0 PRO EDITION © 2023</div>
    </div>
    """, unsafe_allow_html=True)
