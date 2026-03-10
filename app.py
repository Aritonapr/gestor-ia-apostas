import streamlit as st

# 1. CONFIGURAÇÃO - DEVE SER A PRIMEIRA LINHA
st.set_page_config(page_title="GESTOR IA", layout="wide", initial_sidebar_state="expanded")

# 2. CSS "BLINDADO" (Força visibilidade total)
st.markdown("""
    <style>
    /* 1. ELIMINAR O TOPO DO STREAMLIT (Seta, Menu, Barra Cinza) */
    header[data-testid="stHeader"], [data-testid="stHeader"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* 2. FUNDO DO SITE */
    .stApp {
        background-color: #f0f2f5 !important;
    }

    /* 3. BARRA SUPERIOR CUSTOMIZADA (ESTILO BETANO) */
    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 65px;
        background-color: #1a242d;
        border-bottom: 4px solid #f64d23;
        display: flex;
        align-items: center;
        padding: 0 20px;
        z-index: 10000;
        color: white !important;
    }
    .logo-gestor {
        font-weight: 900;
        font-size: 26px;
        font-style: italic;
        margin-right: 30px;
        color: white !important;
        font-family: 'Arial Black', sans-serif;
    }
    .top-menu {
        display: flex;
        gap: 20px;
        flex-grow: 1;
    }
    .top-menu-item {
        color: #adb5bd !important;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
        text-decoration: none;
    }
    .top-menu-item:hover { color: white !important; }

    .top-right {
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
        padding: 7px 20px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 12px;
        border: none;
    }

    /* 4. SIDEBAR (MENU DA ESQUERDA) - FORÇAR VISIBILIDADE */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        margin-top: 65px !important; /* Ajuste para ficar abaixo da barra azul */
        border-right: 1px solid #ddd !important;
        width: 320px !important;
    }
    
    /* Forçar cor dos botões da sidebar para aparecerem */
    [data-testid="stSidebar"] button {
        background-color: white !important;
        color: #1a242d !important; /* Texto Escuro */
        border: none !important;
        border-bottom: 1px solid #eee !important;
        text-align: left !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        font-size: 13px !important;
        padding: 20px 10px !important;
        width: 100% !important;
        display: block !important;
        border-radius: 0px !important;
    }
    [data-testid="stSidebar"] button:hover {
        color: #f64d23 !important;
        background-color: #f8f9fa !important;
    }

    /* 5. ÁREA DE CONTEÚDO PRINCIPAL */
    .main-body {
        margin-top: 85px; /* Não deixar o conteúdo sumir sob a barra */
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA BARRA SUPERIOR (NAVBAR)
st.markdown("""
    <div class="fixed-header">
        <div class="logo-gestor">GESTOR IA</div>
        <div class="top-menu">
            <span class="top-menu-item">Apostas Esportivas</span>
            <span class="top-menu-item">Apostas ao Vivo</span>
            <span class="top-menu-item">Apostas Encontradas</span>
            <span class="top-menu-item">Assertividade IA</span>
        </div>
        <div class="top-right">
            <span style="font-size: 20px;">🔍</span>
            <div class="btn-registrar">REGISTRAR</div>
            <button class="btn-entrar">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR (ITENS DO SEU PAPEL)
with st.sidebar:
    # Controle de navegação
    if 'opcao' not in st.session_state:
        st.session_state.opcao = "home"

    if st.button("PROCESSAR ALGORITMO"):
        st.session_state.opcao = "processar"
    
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. CONTEÚDO DA TELA
st.markdown('<div class="main-body">', unsafe_allow_html=True)

if st.session_state.opcao == "home":
    st.title("Bem-vindo ao Gestor IA")
    st.info("👈 Selecione 'PROCESSAR ALGORITMO' para configurar sua análise.")

elif st.session_state.opcao == "processar":
    st.header("⚙️ Processar Algoritmo")
    
    # Campo de Seleção conforme seu pedido
    camp = st.selectbox(
        "Selecione o Campeonato:",
        ["Selecione...", "BRASIL (Todos)", "LA LIGA (Espanha)", "PREMIER (Inglaterra)"],
        key="camp_select"
    )

    if camp != "Selecione...":
        col1, col2 = st.columns(2)
        
        # Simulação de times
        if "BRASIL" in camp:
            times = ["Amazonas", "América-MG", "Flamengo", "Palmeiras", "Santos", "Corinthians"]
        elif "LA LIGA" in camp:
            times = ["Real Madrid", "Barcelona", "Atlético Madrid", "Sevilla"]
        else:
            times = ["Man City", "Arsenal", "Liverpool", "Chelsea"]

        with col1:
            time_a = st.selectbox("Time Mandante", ["Escolha um time..."] + times)
        with col2:
            time_b = st.selectbox("Time Visitante", ["Escolha um time..."] + times)
            
        if time_a != "Escolha um time..." and time_b != "Escolha um time...":
            st.write("---")
            if st.button("🚀 INICIAR BUSCA E ANÁLISE IA"):
                st.warning(f"Analisando dados históricos de {time_a} vs {time_b}...")

st.markdown('</div>', unsafe_allow_html=True)
