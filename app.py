import streamlit as st

# 1. Configuração de Página (Obrigatório ser a primeira linha)
st.set_page_config(page_title="GESTOR IA - PROFISSIONAL", layout="wide", initial_sidebar_state="expanded")

# 2. O "SUPER CSS" - Redesenhando a estrutura do Streamlit
st.markdown("""
    <style>
    /* 1. ELIMINAÇÃO TOTAL DOS ELEMENTOS PADRÃO DO STREAMLIT */
    [data-testid="stHeader"], 
    header, 
    .st-emotion-cache-18ni7ap, 
    .st-emotion-cache-v08dbt {
        display: none !important;
        visibility: hidden !important;
    }

    /* 2. RECONSTRUÇÃO DO CORPO DA PÁGINA */
    .stApp {
        background-color: #f0f2f5 !important; /* Fundo Betano */
    }

    .main .block-container {
        padding-top: 0px !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
    }

    /* 3. BARRA SUPERIOR (HEADER) - EXATAMENTE SEU ESBOÇO */
    .betano-navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 70px;
        background-color: #1a242d;
        border-bottom: 4px solid #f64d23;
        display: flex;
        align-items: center;
        padding: 0 30px;
        z-index: 999999;
        font-family: 'Segoe UI', Arial, sans-serif;
    }

    .betano-logo {
        color: white !important;
        font-size: 28px;
        font-weight: 900;
        font-style: italic;
        margin-right: 40px;
        text-decoration: none;
    }

    .betano-menu {
        display: flex;
        gap: 30px;
        flex-grow: 1;
    }

    .betano-menu-item {
        color: #adb5bd !important;
        font-size: 13px;
        font-weight: bold;
        text-transform: uppercase;
        cursor: pointer;
    }
    .betano-menu-item:hover { color: white !important; }

    .betano-auth {
        display: flex;
        align-items: center;
        gap: 20px;
    }

    .btn-registrar {
        border: 1px solid #adb5bd;
        color: white !important;
        padding: 8px 18px;
        border-radius: 4px;
        font-size: 13px;
        font-weight: bold;
        background: transparent;
    }

    .btn-entrar {
        background-color: #00cc66;
        color: white !important;
        padding: 9px 25px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 13px;
        border: none;
    }

    /* 4. MENU LATERAL (SIDEBAR) - ITENS DO SEU PAPEL */
    [data-testid="stSidebar"] {
        top: 70px !important; /* Começa exatamente abaixo da barra */
        background-color: white !important;
        border-right: 1px solid #ddd !important;
        z-index: 99999;
    }

    /* Estilo dos Botões da Esquerda */
    [data-testid="stSidebar"] button {
        background-color: white !important;
        color: #1a242d !important;
        border: none !important;
        border-bottom: 1px solid #eee !important;
        text-align: left !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        font-size: 13px !important;
        padding: 20px 15px !important;
        width: 100% !important;
        display: block !important;
        border-radius: 0px !important;
    }
    [data-testid="stSidebar"] button:hover {
        color: #f64d23 !important;
        background-color: #f8f9fa !important;
    }

    /* 5. ÁREA DE CONTEÚDO (PARA NÃO FICAR ATRÁS DO HEADER) */
    .content-wrapper {
        margin-top: 100px;
        padding: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DA NAVBAR (TOPO)
st.markdown("""
    <div class="betano-navbar">
        <div class="betano-logo">GESTOR IA</div>
        <div class="betano-menu">
            <div class="betano-menu-item">Apostas Esportivas</div>
            <div class="betano-menu-item">Apostas ao Vivo</div>
            <div class="betano-menu-item">Apostas Encontradas</div>
            <div class="betano-menu-item">Assertividade IA</div>
        </div>
        <div class="betano-auth">
            <span style="color: white; font-size: 20px; cursor: pointer;">🔍</span>
            <div class="btn-registrar">REGISTRAR</div>
            <button class="btn-entrar">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - COM TODAS AS PALAVRAS DO SEU ESBOÇO
with st.sidebar:
    # Estado para troca de páginas
    if 'view' not in st.session_state:
        st.session_state.view = 'home'

    if st.button("PROCESSAR ALGORITMO"):
        st.session_state.view = 'processar'
    
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. CONTEÚDO PRINCIPAL (DENTRO DO WRAPPER)
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

if st.session_state.view == 'home':
    st.title("Bem-vindo ao Gestor IA")
    st.write("Clique em **PROCESSAR ALGORITMO** na esquerda para começar a análise dos times.")

elif st.session_state.view == 'processar':
    st.header("⚙️ Configuração do Algoritmo IA")
    
    # Seleção de Campeonato
    campeonato = st.selectbox(
        "Selecione o Campeonato:",
        ["Selecione...", "BRASIL (Série A, B, C, D)", "LA LIGA (Espanha)", "PREMIER (Inglaterra)"]
    )

    if campeonato != "Selecione...":
        col1, col2 = st.columns(2)
        
        # Times Mockados
        times = {
            "BRASIL (Série A, B, C, D)": ["Flamengo", "Palmeiras", "Botafogo", "Amazonas", "América-MG"],
            "LA LIGA (Espanha)": ["Real Madrid", "Barcelona", "Sevilla"],
            "PREMIER (Inglaterra)": ["Man City", "Arsenal", "Liverpool"]
        }
        
        lista = times.get(campeonato, [])

        with col1:
            time_a = st.selectbox("Escolha o Time Mandante", ["Selecione..."] + lista)
        with col2:
            time_b = st.selectbox("Escolha o Time Visitante", ["Selecione..."] + lista)

        if time_a != "Selecione..." and time_b != "Selecione...":
            st.markdown("---")
            if st.button("🚀 INICIAR BUSCA E ANÁLISE"):
                st.success(f"Buscando dados históricos de {time_a} vs {time_b}...")

st.markdown('</div>', unsafe_allow_html=True)
