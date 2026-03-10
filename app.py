import streamlit as st

# 1. Configuração da página (deve ser a primeira linha)
st.set_page_config(page_title="GESTOR IA - PRO", layout="wide")

# 2. CSS Avançado para Forçar o Layout Betano e as palavras no topo
st.markdown("""
    <style>
    /* Esconder o cabeçalho padrão do Streamlit */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Fundo do site */
    .stApp {
        background-color: #f0f2f5;
    }

    /* BARRA SUPERIOR CUSTOMIZADA (IGUAL AO SEU ESBOÇO) */
    .custom-header {
        background-color: #1a242d;
        height: 60px;
        width: 100%;
        position: fixed;
        top: 0;
        left: 0;
        display: flex;
        align-items: center;
        padding: 0 20px;
        z-index: 9999;
        border-bottom: 3px solid #f64d23;
        color: white;
        font-family: 'Arial', sans-serif;
    }

    .logo-text {
        font-weight: 900;
        font-size: 22px;
        margin-right: 40px;
        white-space: nowrap;
    }

    .nav-menu {
        display: flex;
        gap: 20px;
        flex-grow: 1;
    }

    .nav-item {
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
        color: #adb5bd;
        cursor: pointer;
        white-space: nowrap;
    }

    .nav-item:hover {
        color: white;
    }

    .header-right {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .search-icon {
        font-size: 18px;
        cursor: pointer;
    }

    .btn-registrar {
        border: 1px solid #adb5bd;
        background: transparent;
        color: white;
        padding: 5px 15px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 12px;
        cursor: pointer;
    }

    .btn-entrar {
        background-color: #00cc66;
        color: white;
        border: none;
        padding: 6px 20px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 12px;
        cursor: pointer;
    }

    /* AJUSTE DA SIDEBAR PARA FICAR ABAIXO DO HEADER */
    [data-testid="stSidebar"] {
        padding-top: 40px;
        background-color: white !important;
    }

    /* BOTÕES DA SIDEBAR (ESTILO LISTA) */
    .stButton > button {
        width: 100%;
        text-align: left;
        background: none;
        border: none;
        border-bottom: 1px solid #f0f2f5;
        color: #1a242d;
        padding: 15px 10px;
        font-weight: bold;
        font-size: 13px;
        text-transform: uppercase;
        border-radius: 0;
    }

    .stButton > button:hover {
        background-color: #f6f7f9;
        color: #f64d23;
        border-left: 4px solid #f64d23;
    }

    /* Espaçamento do conteúdo para não ficar sob o header fixo */
    .block-container {
        padding-top: 80px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA NAVBAR (IGUAL AO SEU PAPEL)
st.markdown("""
    <div class="custom-header">
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-menu">
            <div class="nav-item">Apostas Esportivas</div>
            <div class="nav-item">Apostas ao Vivo</div>
            <div class="nav-item">Apostas Encontradas</div>
            <div class="nav-item">Assertividade IA</div>
        </div>
        <div class="header-right">
            <div class="search-icon">🔍</div>
            <button class="btn-registrar">REGISTRAR</button>
            <button class="btn-entrar">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR (ITENS DO SEU PAPEL)
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
if st.session_state.page == "home":
    st.subheader("Bem-vindo ao Gestor IA")
    st.info("Selecione 'PROCESSAR ALGORITMO' para iniciar.")

elif st.session_state.page == "processar":
    st.markdown("### 🏟️ Configuração do Algoritmo")
    
    # Seleção de Campeonato
    camp = st.selectbox(
        "Selecione o Campeonato:",
        ["Selecione...", "BRASIL (Série A, B, C, D)", "LA LIGA (Espanha)", "PREMIER (Inglaterra)"]
    )

    if camp != "Selecione...":
        col1, col_vs, col2 = st.columns([2, 0.5, 2])
        
        # Simulação de times por campeonato
        if "BRASIL" in camp:
            times = ["Amazonas", "América-MG", "Flamengo", "Palmeiras", "Santos"]
        elif "LA LIGA" in camp:
            times = ["Real Madrid", "Barcelona", "Atlético Madrid"]
        else:
            times = ["Man City", "Arsenal", "Liverpool"]

        with col1:
            time_a = st.selectbox("Mandante", ["Selecione..."] + times)
        with col_vs:
            st.markdown("<h2 style='text-align:center; padding-top:20px;'>VS</h2>", unsafe_allow_html=True)
        with col2:
            time_b = st.selectbox("Visitante", ["Selecione..."] + times)

        if time_a != "Selecione..." and time_b != "Selecione...":
            st.write("")
            if st.button("🔍 EXECUTAR ANÁLISE IA"):
                st.success(f"Algoritmo processando: {time_a} vs {time_b}...")
