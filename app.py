import streamlit as st

# 1. Configuração inicial - TRAVA A LATERAL ABERTA
st.set_page_config(page_title="GESTOR IA", layout="wide", initial_sidebar_state="expanded")

# 2. CSS "EXTERMINADOR DE SETA"
st.markdown("""
    <style>
    /* 1. APAGA COMPLETAMENTE A SETA DE VOLTAR E O CABEÇALHO */
    [data-testid="stSidebarCollapseButton"],
    [data-testid="collapsedControl"],
    button[kind="header"],
    header,
    [data-testid="stHeader"] {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        height: 0 !important;
    }

    /* 2. REMOVE QUALQUER MARGEM NO TOPO DO STREAMLIT */
    .st-emotion-cache-z5fcl4 {
        padding-top: 0px !important;
    }
    
    /* FUNDO DO SITE */
    .stApp {
        background-color: #f0f2f5 !important;
    }

    /* 3. BARRA SUPERIOR (NAVBAR) - IGUAL SEU ESBOÇO */
    .betano-navbar {
        position: fixed;
        top: 0; left: 0;
        width: 100%;
        height: 65px;
        background-color: #1a242d;
        border-bottom: 4px solid #f64d23;
        display: flex;
        align-items: center;
        padding: 0 30px;
        z-index: 999999;
        font-family: 'Arial', sans-serif;
    }

    .logo-gestor {
        color: white !important;
        font-weight: 900;
        font-size: 26px;
        font-style: italic;
        margin-right: 40px;
        letter-spacing: -1px;
    }

    .menu-text {
        color: #adb5bd !important;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
        margin-right: 25px;
        white-space: nowrap;
    }

    .auth-section {
        margin-left: auto;
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .btn-reg {
        border: 1px solid #adb5bd;
        color: white !important;
        padding: 6px 15px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: bold;
    }

    .btn-ent {
        background-color: #00cc66;
        color: white !important;
        padding: 8px 22px;
        border-radius: 4px;
        font-weight: bold;
        border: none;
        font-size: 12px;
    }

    /* 4. MENU LATERAL (SIDEBAR) - FIXO E SEM OPÇÃO DE FECHAR */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        margin-top: 65px !important;
        border-right: 1px solid #ddd !important;
        min-width: 320px !important;
    }

    /* Botões da Sidebar (Seu Esboço) */
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
    .content-box {
        margin-top: 100px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA NAVBAR SUPERIOR
st.markdown("""
    <div class="betano-navbar">
        <div class="logo-gestor">GESTOR IA</div>
        <div class="menu-text">Apostas Esportivas</div>
        <div class="menu-text">Apostas ao Vivo</div>
        <div class="menu-text">Apostas Encontradas</div>
        <div class="menu-text">Assertividade IA</div>
        <div class="auth-section">
            <span style="color:white; font-size:20px; cursor:pointer;">🔍</span>
            <div class="btn-reg">REGISTRAR</div>
            <button class="btn-ent">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - COM OS ITENS DO SEU PAPEL
with st.sidebar:
    if 'view' not in st.session_state:
        st.session_state.view = "home"

    if st.button("PROCESSAR ALGORITMO"):
        st.session_state.view = "processar"
    
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. CONTEÚDO PRINCIPAL
st.markdown('<div class="content-box">', unsafe_allow_html=True)

if st.session_state.view == "home":
    st.title("Bem-vindo ao Gestor IA")
    st.write("Clique em **PROCESSAR ALGORITMO** no menu lateral para selecionar o campeonato e os times.")

elif st.session_state.view == "processar":
    st.subheader("🤖 Algoritmo de Processamento")
    
    campeonato = st.selectbox(
        "Selecione o Campeonato:",
        ["Selecione...", "BRASIL (Todos)", "LA LIGA (Espanha)", "PREMIER (Inglaterra)"]
    )

    if campeonato != "Selecione...":
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        # Simulação de times
        if "BRASIL" in campeonato:
            lista = ["Amazonas", "América-MG", "Flamengo", "Palmeiras", "Santos"]
        elif "LA LIGA" in campeonato:
            lista = ["Real Madrid", "Barcelona", "Atlético Madrid"]
        else:
            lista = ["Man City", "Arsenal", "Liverpool"]

        with col1:
            t1 = st.selectbox("Mandante", ["Selecione o time..."] + lista)
        with col2:
            t2 = st.selectbox("Visitante", ["Selecione o time..."] + lista)

        if t1 != "Selecione o time..." and t2 != "Selecione o time...":
            if st.button("🚀 EXECUTAR ANÁLISE IA"):
                st.info(f"O GIAE está analisando agora: {t1} vs {t2}")

st.markdown('</div>', unsafe_allow_html=True)
