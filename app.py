import streamlit as st

# 1. Configuração inicial
st.set_page_config(page_title="GESTOR IA - PRO", layout="wide", initial_sidebar_state="expanded")

# 2. CSS "BLINDADO" COM LOGO REESTILIZADO
st.markdown("""
    <style>
    /* 1. APAGAR COMPLETAMENTE ELEMENTOS DO STREAMLIT (Seta, Header, etc) */
    [data-testid="stSidebarCollapseButton"],
    [data-testid="collapsedControl"],
    header,
    [data-testid="stHeader"] {
        display: none !important;
        visibility: hidden !important;
    }

    /* 2. FUNDO DO SITE */
    .stApp {
        background-color: #f0f2f5 !important;
    }

    /* 3. BARRA SUPERIOR (NAVBAR) - ESTILO BETANO COM SUA LOGO */
    .custom-navbar {
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        height: 70px;
        background-color: #1a242d;
        border-bottom: 3px solid #f64d23;
        display: flex;
        align-items: center;
        padding: 0 25px;
        z-index: 999999;
    }

    /* CONTAINER DA LOGO (LOGO + TEXTO) */
    .logo-container {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-right: 40px;
    }

    /* O HEXÁGONO DO LOGO */
    .hexagon-logo {
        width: 38px;
        height: 42px;
        background: linear-gradient(135deg, #a44d1d 0%, #f64d23 100%);
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
    }
    .hexagon-inner {
        width: 28px;
        height: 32px;
        background-color: #1a242d;
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .hexagon-center {
        width: 16px;
        height: 18px;
        background: #a44d1d;
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
    }

    /* O TEXTO "GESTOR IA" EM BLOCO */
    .gestor-ia-text {
        color: #f64d23;
        font-family: 'Arial Black', 'Arial Bold', sans-serif;
        font-size: 28px;
        font-weight: 900;
        letter-spacing: 1px;
        text-transform: uppercase;
        line-height: 1;
        margin-top: 4px;
    }

    /* LINKS DO MENU SUPERIOR */
    .nav-links {
        display: flex;
        gap: 25px;
        flex-grow: 1;
    }
    .nav-links span {
        color: #adb5bd !important;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
        cursor: pointer;
    }
    .nav-links span:hover { color: white !important; }

    /* BOTÕES DA DIREITA */
    .nav-right {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .btn-registrar {
        border: 1px solid #adb5bd;
        color: white !important;
        padding: 6px 15px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: bold;
    }
    .btn-entrar {
        background-color: #00cc66;
        color: white !important;
        padding: 8px 22px;
        border-radius: 4px;
        font-weight: bold;
        border: none;
        font-size: 12px;
    }

    /* 4. SIDEBAR (MENU LATERAL) */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        margin-top: 70px !important;
        border-right: 1px solid #ddd !important;
        min-width: 320px !important;
    }

    /* BOTÕES DA SIDEBAR */
    [data-testid="stSidebar"] button {
        background-color: white !important;
        color: #1a242d !important;
        border: none !important;
        border-bottom: 1px solid #f0f2f5 !important;
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

    /* 5. ÁREA CENTRAL */
    .content-area {
        margin-top: 100px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA NAVBAR (TOPO) COM SEU LOGO REFEITO
st.markdown("""
    <div class="custom-navbar">
        <div class="logo-container">
            <div class="hexagon-logo">
                <div class="hexagon-inner">
                    <div class="hexagon-center"></div>
                </div>
            </div>
            <div class="gestor-ia-text">GESTOR IA</div>
        </div>
        <div class="nav-links">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div class="nav-right">
            <span style="color:white; font-size:20px; cursor:pointer;">🔍</span>
            <div class="btn-registrar">REGISTRAR</div>
            <button class="btn-entrar">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - COM AS PALAVRAS DO SEU PAPEL
with st.sidebar:
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

# 5. CONTEÚDO PRINCIPAL
st.markdown('<div class="content-area">', unsafe_allow_html=True)

if st.session_state.page == "home":
    st.title("Bem-vindo ao Gestor IA")
    st.write("Abra o menu lateral para configurar seu algoritmo.")

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
            t1 = st.selectbox("Mandante", ["Escolha..."] + times)
        with col2:
            t2 = st.selectbox("Visitante", ["Escolha..."] + times)

        if t1 != "Escolha..." and t2 != "Escolha...":
            if st.button("🔥 INICIAR ANÁLISE IA"):
                st.success(f"GIAE analisando estatísticas para {t1} vs {t2}...")

st.markdown('</div>', unsafe_allow_html=True)
