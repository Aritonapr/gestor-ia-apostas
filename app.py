import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="GESTOR IA", layout="wide")

# 2. CSS Ultra-Focado (Para não sumir nada)
st.markdown("""
    <style>
    /* Esconde a barra original e a seta de voltar */
    [data-testid="stHeader"] {
        display: none;
    }
    
    /* Cria a Barra do Topo (Igual seu esboço) */
    .top-bar {
        background-color: #1a242d;
        height: 65px;
        width: 100%;
        position: fixed;
        top: 0; left: 0;
        display: flex;
        align-items: center;
        padding: 0 20px;
        z-index: 9999;
        border-bottom: 3px solid #f64d23;
        color: white;
    }
    .logo {
        font-weight: 900;
        font-size: 24px;
        font-style: italic;
        margin-right: 30px;
    }
    .links {
        display: flex;
        gap: 20px;
        flex-grow: 1;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
    }
    .right-side {
        display: flex;
        gap: 15px;
    }
    .btn-green {
        background-color: #00cc66;
        color: white;
        padding: 5px 15px;
        border-radius: 4px;
        border: none;
        font-weight: bold;
    }

    /* Ajusta a Sidebar para aparecer abaixo da barra */
    [data-testid="stSidebar"] {
        padding-top: 70px !important;
        background-color: #ffffff !important;
    }

    /* Estilo dos Botões da Esquerda - FORÇANDO COR ESCURA */
    .stButton > button {
        width: 100% !important;
        background-color: #f8f9fa !important;
        color: #1a242d !important; /* Texto Azul Escuro para aparecer */
        border: 1px solid #ddd !important;
        padding: 12px !important;
        text-align: left !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        margin-bottom: 5px !important;
    }
    .stButton > button:hover {
        border-color: #f64d23 !important;
        color: #f64d23 !important;
    }

    /* Área de conteúdo principal */
    .main-content {
        margin-top: 80px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA BARRA SUPERIOR
st.markdown("""
    <div class="top-bar">
        <div class="logo">GESTOR IA</div>
        <div class="links">
            <div>Apostas Esportivas</div>
            <div>Apostas ao Vivo</div>
            <div>Apostas Encontradas</div>
            <div>Assertividade IA</div>
        </div>
        <div class="right-side">
            <span style="font-size: 20px;">🔍</span>
            <div style="border: 1px solid white; padding: 5px 10px; border-radius: 4px; font-size: 12px; font-weight: bold;">REGISTRAR</div>
            <button class="btn-green">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. MENU LATERAL (SIDEBAR)
with st.sidebar:
    st.write("### MENU") # Título para confirmar que a sidebar está aqui
    
    if st.button("PROCESSAR ALGORITMO"):
        st.session_state.page = "processar"
    
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. CONTEÚDO DA PÁGINA
st.markdown('<div class="main-content">', unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    st.header("Bem-vindo ao Gestor IA")
    st.write("Clique em **PROCESSAR ALGORITMO** no menu à esquerda para selecionar os campeonatos.")

elif st.session_state.page == "processar":
    st.header("⚙️ Processar Algoritmo")
    
    camp = st.selectbox(
        "Selecione o Campeonato:",
        ["Selecione...", "BRASIL (Série A, B, C, D)", "LA LIGA (Espanha)", "PREMIER (Inglaterra)"]
    )
    
    if camp != "Selecione...":
        st.write(f"Você selecionou: {camp}")
        col1, col2 = st.columns(2)
        with col1:
            st.selectbox("Time A (Mandante)", ["Time 1", "Time 2", "Time 3"])
        with col2:
            st.selectbox("Time B (Visitante)", ["Time 4", "Time 5", "Time 6"])
            
        if st.button("EXECUTAR ANÁLISE"):
            st.success("Analisando dados...")

st.markdown('</div>', unsafe_allow_html=True)
