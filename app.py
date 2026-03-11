import streamlit as st

# 1. Configuração inicial
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. CSS FOCO TOTAL EM SUBIR O TEXTO DA ESQUERDA
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap');

    /* ESCONDER ELEMENTOS NATIVOS */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] {
        display: none !important;
    }

    /* FUNDO DARK */
    .stApp { 
        background-color: #0b0e11 !important; 
        color: #e2e8f0 !important; 
        font-family: 'Roboto', sans-serif !important; 
    }

    /* --- BARRA SUPERIOR (FIXA) --- */
    .top-bar {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 50px;
        background-color: #15191d;
        border-bottom: 2px solid #f64d23;
        display: flex; align-items: center;
        padding: 0 20px; z-index: 999999;
    }
    .logo-gestor { color: #f64d23; font-weight: 900; font-size: 18px; font-style: italic; display: flex; align-items: center; gap: 10px; }
    .nav-links { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; color: #e2e8f0; font-size: 11px; font-weight: 700; text-transform: uppercase; }

    /* --- SIDEBAR: SUBIR O TEXTO AO MÁXIMO --- */
    [data-testid="stSidebar"] {
        background-color: #15191d !important;
        margin-top: 50px !important; /* Começa logo abaixo da linha laranja */
        border-right: 1px solid #2d3843 !important;
        width: 260px !important;
    }

    /* ESSA É A PARTE QUE SOBE O TEXTO DA ESQUERDA */
    [data-testid="stSidebarContent"] {
        padding-top: 0px !important; /* Zera o espaço no topo */
        margin-top: -15px !important; /* Puxa os botões para cima para encostar na barra */
        overflow: hidden !important; 
    }

    /* BOTÕES DA LATERAL (ESTILO LISTA) */
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        color: #e2e8f0 !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        font-weight: 700 !important;
        font-size: 11px !important;
        padding: 8px 15px !important; 
        min-height: 38px !important; 
        width: 100% !important;
        border-radius: 0px !important;
        display: block !important;
        text-transform: uppercase;
    }
    [data-testid="stSidebar"] button:hover {
        color: #f64d23 !important;
        background-color: #1e293b !important;
        border-left: 3px solid #f64d23 !important;
    }

    /* ÁREA CENTRAL */
    .main-container {
        margin-top: 70px;
        padding: 0 30px;
    }

    /* RODAPÉ */
    .footer {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background-color: #15191d;
        height: 25px; border-top: 1px solid #2d3843;
        display: flex; justify-content: space-between; align-items: center;
        padding: 0 20px; font-size: 9px; color: #94a3b8;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA BARRA SUPERIOR
st.markdown("""
    <div class="top-bar">
        <div class="logo-gestor">
            <div style="width:25px; height:28px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); box-shadow: 0 0 10px #f64d23;"></div>
            GESTOR IA
        </div>
        <div class="nav-links">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:15px; align-items:center;">
            <div style="color:white; font-size:12px; border:1px solid #94a3b8; padding:3px 10px; border-radius:3px;">REGISTRAR</div>
            <div style="background:#00cc66; color:white; padding:4px 15px; border-radius:3px; font-weight:bold; font-size:12px;">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - OS 8 ITENS DO SEU PAPEL (SUBIDOS)
with st.sidebar:
    st.button("PROCESSAR ALGORITMO")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. CONTEÚDO PRINCIPAL
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown("### 📊 Dashboard Profissional")
st.write("Os itens da lateral esquerda foram subidos para eliminar o espaço vazio no topo.")
st.markdown('</div>', unsafe_allow_html=True)

# 6. RODAPÉ
st.markdown("""
    <div class="footer">
        <div>STATUS: ● ONLINE</div>
        <div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div>
    </div>
    """, unsafe_allow_html=True)
