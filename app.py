import streamlit as st

# 1. Configuração da página - DEVE SER A PRIMEIRA LINHA
st.set_page_config(page_title="GESTOR IA", layout="wide", initial_sidebar_state="expanded")

# 2. CSS COMPLETO E FORÇADO (BETANO STYLE)
st.markdown("""
    <style>
    /* Remove o cabeçalho original e a seta */
    [data-testid="stHeader"] {
        display: none !important;
    }
    
    /* Fundo da tela */
    .stApp {
        background-color: #f0f2f5 !important;
    }

    /* BARRA DO TOPO (GESTOR IA + MENU SUPERIOR) */
    .top-navbar {
        background-color: #1a242d;
        height: 60px;
        width: 100%;
        position: fixed;
        top: 0; left: 0;
        display: flex;
        align-items: center;
        padding: 0 20px;
        z-index: 10000;
        border-bottom: 3px solid #f64d23;
        color: white;
        font-family: Arial, sans-serif;
    }
    .logo {
        font-weight: 900;
        font-size: 24px;
        font-style: italic;
        margin-right: 30px;
        color: white !important;
    }
    .top-links {
        display: flex;
        gap: 20px;
        flex-grow: 1;
        font-size: 11px;
        font-weight: bold;
        text-transform: uppercase;
    }
    .top-right {
        display: flex;
        gap: 15px;
        align-items: center;
    }
    .btn-registrar {
        border: 1px solid #adb5bd;
        padding: 5px 10px;
        border-radius: 4px;
        font-size: 11px;
    }
    .btn-entrar {
        background-color: #00cc66;
        color: white;
        padding: 6px 15px;
        border-radius: 4px;
        border: none;
        font-weight: bold;
        font-size: 11px;
    }

    /* MENU LATERAL (SIDEBAR) */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        margin-top: 60px !important; /* Começa abaixo da barra azul */
        border-right: 1px solid #ddd !important;
    }

    /* BOTÕES DA LATERAL (SEU ESBOÇO) */
    .stButton > button {
        width: 100% !important;
        background-color: white !important;
        color: #1a242d !important; /* Letra escura para aparecer */
        border: none !important;
        border-bottom: 1px solid #f0f2f5 !important;
        text-align: left !important;
        padding: 15px 10px !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        font-size: 12px !important;
        border-radius: 0px !important;
    }
    .stButton > button:hover {
        background-color: #f8f9fa !important;
        color: #f64d23 !important;
        border-left: 4px solid #f64d23 !important;
    }

    /* Espaçamento do conteúdo */
    .main-content {
        margin-top: 80px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA BARRA SUPERIOR (NAVBAR)
st.markdown("""
    <div class="top-navbar">
        <div class="logo">GESTOR IA</div>
        <div class="top-links">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div class="top-right">
            <span>🔍</span>
            <div class="btn-registrar">REGISTRAR</div>
            <button class="btn-entrar">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. MENU LATERAL (Abaixo da Barra)
with st.sidebar:
    # Usando st.session_state para não perder a página ao clicar
    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    if st.button("PROCESSAR ALGORITMO"):
        st.session_state.page = 'processar'
    
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. CONTEÚDO PRINCIPAL
st.markdown('<div class="main-content">', unsafe_allow_html=True)

if st.session_state.page == 'home':
    st.title("Bem-vindo ao Gestor IA")
    st.write("Clique em 'PROCESSAR ALGORITMO' para iniciar a seleção de times.")

elif st.session_state.page == 'processar':
    st.header("⚙️ Configurar Algoritmo")
    
    # Campo de Seleção conforme seu pedido
    campeonato = st.selectbox(
        "Selecione o Campeonato:",
        ["Selecione...", "BRASIL (Todos)", "LA LIGA (Espanha)", "PREMIER (Inglaterra)"]
    )

    if campeonato != "Selecione...":
        col1, col2 = st.columns(2)
        
        # Simulação de times
        if "BRASIL" in campeonato:
            times = ["Amazonas", "América-MG", "Flamengo", "Palmeiras", "Santos", "Corinthians"]
        elif "LA LIGA" in campeonato:
            times = ["Real Madrid", "Barcelona", "Atlético Madrid", "Sevilla"]
        else:
            times = ["Man City", "Arsenal", "Liverpool", "Chelsea"]

        with col1:
            time_a = st.selectbox("Time Mandante", ["Escolha..."] + times)
        with col2:
            time_b = st.selectbox("Time Visitante", ["Escolha..."] + times)
            
        if time_a != "Escolha..." and time_b != "Escolha...":
            st.markdown("---")
            if st.button("🔥 EXECUTAR ANÁLISE IA"):
                st.success(f"Buscando dados de {time_a} vs {time_b}...")

st.markdown('</div>', unsafe_allow_html=True)
