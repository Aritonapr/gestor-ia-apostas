import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="GESTOR IA", layout="wide", initial_sidebar_state="expanded")

# 2. CSS Corrigido para manter o Menu Lateral visível e sem a seta
st.markdown("""
    <style>
    /* Remove a seta e o cabeçalho original sem quebrar a lateral */
    header[data-testid="stHeader"] {
        visibility: hidden;
        height: 0px;
    }
    
    /* Ajusta o espaçamento do corpo da página */
    .block-container {
        padding-top: 5rem !important;
    }

    /* BARRA SUPERIOR FIXA (NAVBAR) */
    .betano-header {
        background-color: #1a242d;
        height: 60px;
        width: 100%;
        position: fixed;
        top: 0;
        left: 0;
        display: flex;
        align-items: center;
        padding: 0 30px;
        z-index: 10000;
        border-bottom: 3px solid #f64d23;
        font-family: 'Arial', sans-serif;
    }

    .logo-gestor {
        color: white;
        font-weight: 900;
        font-size: 24px;
        font-style: italic;
        margin-right: 40px;
        letter-spacing: -1px;
    }

    .menu-items {
        display: flex;
        gap: 25px;
        flex-grow: 1;
    }

    .menu-link {
        color: #ffffff;
        text-decoration: none;
        font-size: 13px;
        font-weight: bold;
        text-transform: uppercase;
        white-space: nowrap;
    }

    .header-right {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .btn-reg {
        border: 1px solid #adb5bd;
        color: white;
        padding: 5px 12px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 12px;
        background: transparent;
    }

    .btn-ent {
        background-color: #00cc66;
        color: white;
        padding: 6px 18px;
        border-radius: 4px;
        font-weight: bold;
        border: none;
        font-size: 12px;
    }

    /* MENU LATERAL (SIDEBAR) - CORREÇÃO DE VISIBILIDADE */
    section[data-testid="stSidebar"] {
        top: 60px !important; /* Coloca o menu exatamente abaixo da barra azul */
        background-color: white !important;
        width: 300px !important;
    }

    /* Estilização dos Botões da Esquerda (Seu Esboço) */
    section[data-testid="stSidebar"] .stButton > button {
        width: 100%;
        text-align: left;
        background: none;
        border: none;
        border-bottom: 1px solid #f0f2f5;
        color: #1a242d !important;
        padding: 15px 10px;
        font-weight: bold;
        font-size: 13px;
        text-transform: uppercase;
        border-radius: 0;
    }

    section[data-testid="stSidebar"] .stButton > button:hover {
        color: #f64d23 !important;
        background-color: #f8f9fa;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA BARRA SUPERIOR (Mantendo todos os nomes do esboço)
st.markdown("""
    <div class="betano-header">
        <div class="logo-gestor">GESTOR IA</div>
        <div class="menu-items">
            <div class="menu-link">Apostas Esportivas</div>
            <div class="menu-link">Apostas ao Vivo</div>
            <div class="menu-link">Apostas Encontradas</div>
            <div class="menu-link">Assertividade IA</div>
        </div>
        <div class="header-right">
            <span style="color:white; font-size:18px;">🔍</span>
            <button class="btn-reg">REGISTRAR</button>
            <button class="btn-ent">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. MENU LATERAL (Exatamente as palavras do seu papel)
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
    st.title("Bem-vindo ao Gestor IA")
    st.write("Selecione 'PROCESSAR ALGORITMO' na lateral para iniciar a análise dos campeonatos.")

elif st.session_state.page == "processar":
    st.subheader("⚙️ Processar Algoritmo")
    
    # Seleção de Campeonato conforme seu pedido
    campeonato = st.selectbox(
        "Selecione o Campeonato:",
        ["Selecione...", "BRASIL (Série A, B, C, D)", "LA LIGA (Espanha)", "PREMIER (Inglaterra)"]
    )

    if campeonato != "Selecione...":
        st.markdown(f"#### Analisando: {campeonato}")
        
        col1, col2 = st.columns(2)
        
        # Lista de times fictícia para teste
        times = {
            "BRASIL (Série A, B, C, D)": ["Amazonas", "América-MG", "Flamengo", "Palmeiras", "Santos"],
            "LA LIGA (Espanha)": ["Real Madrid", "Barcelona", "Atlético Madrid"],
            "PREMIER (Inglaterra)": ["Man City", "Arsenal", "Liverpool"]
        }
        
        lista_times = times.get(campeonato, [])

        with col1:
            time_a = st.selectbox("Escolha o Time Mandante", ["Selecione..."] + lista_times)
        with col2:
            time_b = st.selectbox("Escolha o Time Visitante", ["Selecione..."] + lista_times)

        if time_a != "Selecione..." and time_b != "Selecione...":
            if st.button("INICIAR BUSCA DE DADOS IA"):
                st.success(f"Buscando estatísticas para {time_a} vs {time_b}...")
