import streamlit as st

# 1. Configuração inicial (Travando a lateral aberta)
st.set_page_config(page_title="GESTOR IA", layout="wide", initial_sidebar_state="expanded")

# 2. O CSS "NUCLEAR" - Para apagar a seta de vez
st.markdown("""
    <style>
    /* 1. APAGAR O CABEÇALHO E QUALQUER BOTÃO DE SETA OU MENU DO STREAMLIT */
    header[data-testid="stHeader"], 
    [data-testid="stHeader"],
    .st-emotion-cache-18ni7ap,
    button[data-testid="stSidebarCollapseButton"],
    [data-testid="collapsedControl"] {
        display: none !important;
        visibility: hidden !important;
        height: 0px !important;
    }

    /* 2. RECONSTRUIR O FUNDO */
    .stApp {
        background-color: #f0f2f5 !important;
    }

    /* 3. BARRA SUPERIOR (NAVBAR) FIXA */
    .betano-top-bar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 65px;
        background-color: #1a242d;
        border-bottom: 4px solid #f64d23;
        display: flex;
        align-items: center;
        padding: 0 30px;
        z-index: 999999;
    }

    .logo {
        color: white !important;
        font-weight: 900;
        font-size: 26px;
        font-style: italic;
        margin-right: 40px;
        font-family: 'Arial Black', sans-serif;
    }

    .nav-text {
        color: #adb5bd !important;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
        margin-right: 25px;
    }

    .auth-right {
        margin-left: auto;
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .reg-btn {
        border: 1px solid #adb5bd;
        color: white !important;
        padding: 5px 15px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: bold;
    }

    .ent-btn {
        background-color: #00cc66;
        color: white !important;
        padding: 7px 20px;
        border-radius: 4px;
        border: none;
        font-weight: bold;
        font-size: 12px;
    }

    /* 4. MENU LATERAL (SIDEBAR) TRAVADO E VISÍVEL */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        margin-top: 65px !important; /* Começa abaixo da barra */
        border-right: 1px solid #ddd !important;
        min-width: 320px !important;
    }

    /* Botões da Sidebar - Cor escura para não sumir */
    [data-testid="stSidebar"] button {
        background-color: white !important;
        color: #1a242d !important;
        border: none !important;
        border-bottom: 1px solid #eee !important;
        text-align: left !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        font-size: 13px !important;
        padding: 20px 15px !important;
        width: 100% !important;
        border-radius: 0px !important;
        display: block !important;
    }

    [data-testid="stSidebar"] button:hover {
        color: #f64d23 !important;
        background-color: #f8f9fa !important;
        border-left: 5px solid #f64d23 !important;
    }

    /* Ajuste do conteúdo principal */
    .main-body {
        margin-top: 80px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA BARRA SUPERIOR (EXATO AO PAPEL)
st.markdown("""
    <div class="betano-top-bar">
        <div class="logo">GESTOR IA</div>
        <div class="nav-text">Apostas Esportivas</div>
        <div class="nav-text">Apostas ao Vivo</div>
        <div class="nav-text">Apostas Encontradas</div>
        <div class="nav-text">Assertividade IA</div>
        <div class="auth-right">
            <span style="color:white; font-size:20px;">🔍</span>
            <div class="reg-btn">REGISTRAR</div>
            <button class="ent-btn">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - COM TODAS AS PALAVRAS DO SEU ESBOÇO
with st.sidebar:
    # Usando state para navegar
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    if st.button("PROCESSAR ALGORITMO"):
        st.session_state.page = "processar"
    
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. ÁREA DE CONTEÚDO
st.markdown('<div class="main-body">', unsafe_allow_html=True)

if st.session_state.page == "home":
    st.title("Bem-vindo ao Gestor IA")
    st.info("👈 Selecione uma opção no menu lateral.")

elif st.session_state.page == "processar":
    st.header("⚙️ Processar Algoritmo")
    
    camp = st.selectbox(
        "Selecione o Campeonato:",
        ["Selecione...", "BRASIL (Todos)", "LA LIGA (Espanha)", "PREMIER (Inglaterra)"]
    )

    if camp != "Selecione...":
        col1, col2 = st.columns(2)
        
        # Times
        if "BRASIL" in camp:
            times = ["Amazonas", "América-MG", "Flamengo", "Palmeiras", "Santos"]
        elif "LA LIGA" in camp:
            times = ["Real Madrid", "Barcelona", "Sevilla"]
        else:
            times = ["Man City", "Arsenal", "Liverpool"]

        with col1:
            time_a = st.selectbox("Time Mandante", ["Escolha..."] + times)
        with col2:
            time_b = st.selectbox("Time Visitante", ["Escolha..."] + times)

        if time_a != "Escolha..." and time_b != "Escolha...":
            if st.button("🔥 INICIAR ANÁLISE IA"):
                st.success(f"Buscando estatísticas para {time_a} vs {time_b}...")

st.markdown('</div>', unsafe_allow_html=True)
