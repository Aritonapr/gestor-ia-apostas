import streamlit as st

# 1. Configuração Inicial
st.set_page_config(page_title="GESTOR IA", layout="wide", initial_sidebar_state="expanded")

# 2. CSS "BLINDADO" COM TRAVA DE SETA
st.markdown("""
    <style>
    /* 1. REMOVE O CABEÇALHO PADRÃO E A SETA DE VOLTAR (COLLAPSE) */
    [data-testid="stHeader"], 
    header, 
    [data-testid="collapsedControl"] {
        display: none !important;
        visibility: hidden !important;
    }

    /* 2. FORÇA O FUNDO DO SITE */
    .stApp {
        background-color: #f0f2f5 !important;
    }

    /* 3. BARRA SUPERIOR (NAVBAR) - ESTILO BETANO */
    .custom-top-bar {
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
        font-family: 'Arial', sans-serif;
    }

    .logo-box {
        color: white !important;
        font-size: 26px;
        font-weight: 900;
        font-style: italic;
        margin-right: 40px;
        white-space: nowrap;
    }

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
        padding: 8px 20px;
        border-radius: 4px;
        font-weight: bold;
        border: none;
        font-size: 12px;
    }

    /* 4. SIDEBAR (MENU DA ESQUERDA) - TRAVADO E SEM SETA */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        margin-top: 65px !important;
        border-right: 1px solid #ddd !important;
        min-width: 300px !important;
        max-width: 300px !important;
    }

    /* BOTÕES DA SIDEBAR */
    [data-testid="stSidebar"] button {
        background-color: white !important;
        color: #1a242d !important;
        border: none !important;
        border-bottom: 1px solid #f0f2f5 !important;
        text-align: left !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        font-size: 12px !important;
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

    /* 5. ÁREA DO CONTEÚDO PRINCIPAL */
    .main-container {
        margin-top: 85px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA NAVBAR
st.markdown("""
    <div class="custom-top-bar">
        <div class="logo-box">GESTOR IA</div>
        <div class="nav-links">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div class="nav-right">
            <span style="color: white; font-size: 18px;">🔍</span>
            <div class="btn-registrar">REGISTRAR</div>
            <button class="btn-entrar">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - COM AS PALAVRAS DO SEU PAPEL
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
st.markdown('<div class="main-container">', unsafe_allow_html=True)

if st.session_state.view == "home":
    st.title("Bem-vindo ao Gestor IA")
    st.write("Selecione **PROCESSAR ALGORITMO** na lateral para iniciar a análise.")

elif st.session_state.view == "processar":
    st.header("⚙️ Processar Algoritmo")
    
    # Seleção de Campeonato
    campeonato = st.selectbox(
        "Selecione o Campeonato:",
        ["Selecione...", "BRASIL (Todos)", "LA LIGA (Espanha)", "PREMIER (Inglaterra)"]
    )

    if campeonato != "Selecione...":
        st.write("---")
        st.subheader("⚽ Seleção de Confronto")
        
        if "BRASIL" in campeonato:
            lista_times = ["Flamengo", "Palmeiras", "Botafogo", "Amazonas", "América-MG", "Santos"]
        elif "LA LIGA" in campeonato:
            lista_times = ["Real Madrid", "Barcelona", "Atlético Madrid"]
        else:
            lista_times = ["Man City", "Arsenal", "Liverpool"]

        col1, col2 = st.columns(2)
        with col1:
            time_a = st.selectbox("Mandante", ["Escolha o time..."] + lista_times)
        with col2:
            time_b = st.selectbox("Visitante", ["Escolha o time..."] + lista_times)

        if time_a != "Escolha o time..." and time_b != "Escolha o time...":
            if st.button("🚀 INICIAR BUSCA E ANÁLISE PROFUNDA"):
                st.info(f"O Algoritmo está cruzando dados de {time_a} vs {time_b}...")

st.markdown('</div>', unsafe_allow_html=True)
