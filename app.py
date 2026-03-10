import streamlit as st

# 1. Configuração da página (Deve ser a primeira linha)
st.set_page_config(page_title="GESTOR IA", layout="wide", initial_sidebar_state="expanded")

# 2. CSS Avançado para remover a "seta", o cabeçalho padrão e formatar como a Betano
st.markdown("""
    <style>
    /* Remove o cabeçalho padrão, a seta de voltar e o menu de opções do Streamlit */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    /* Remove o preenchimento superior padrão */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 5rem !important;
        padding-right: 5rem !important;
    }

    /* BARRA SUPERIOR FIXA (NAVBAR) - ESTILO BETANO TOTAL */
    .betano-header {
        background-color: #1a242d;
        height: 60px;
        width: 100%;
        position: fixed;
        top: 0;
        left: 0;
        display: flex;
        align-items: center;
        padding: 0 40px;
        z-index: 999999;
        border-bottom: 3px solid #f64d23;
        font-family: 'Arial', sans-serif;
    }

    .logo-gestor {
        color: white;
        font-weight: 900;
        font-size: 26px;
        font-style: italic;
        margin-right: 40px;
        letter-spacing: -1px;
    }

    .menu-items {
        display: flex;
        gap: 30px;
        flex-grow: 1;
    }

    .menu-link {
        color: white;
        text-decoration: none;
        font-size: 13px;
        font-weight: bold;
        text-transform: uppercase;
        cursor: pointer;
    }

    .header-right {
        display: flex;
        align-items: center;
        gap: 20px;
    }

    .icon { color: white; font-size: 20px; cursor: pointer; }

    .btn-reg {
        border: 1px solid #adb5bd;
        color: white;
        padding: 6px 15px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 13px;
        background: transparent;
    }

    .btn-ent {
        background-color: #00cc66;
        color: white;
        padding: 7px 20px;
        border-radius: 4px;
        font-weight: bold;
        border: none;
        font-size: 13px;
    }

    /* AJUSTE DA SIDEBAR PARA FICAR EMBAIXO DA BARRA */
    [data-testid="stSidebar"] {
        margin-top: 60px;
        background-color: white !important;
        border-right: 1px solid #ddd;
    }

    /* BOTÕES DA SIDEBAR */
    .stButton > button {
        width: 100%;
        text-align: left;
        background: none;
        border: none;
        border-bottom: 1px solid #f0f2f5;
        color: #1a242d;
        padding: 18px 15px;
        font-weight: bold;
        font-size: 13px;
        text-transform: uppercase;
        border-radius: 0;
    }

    .stButton > button:hover {
        color: #f64d23;
        background-color: #f8f9fa;
    }

    /* Espaço para o conteúdo não sumir atrás da barra */
    .content-area {
        margin-top: 100px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HTML DO CABEÇALHO (Ocupando 100% da largura, sem setas)
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
            <div class="icon">🔍</div>
            <button class="btn-reg">REGISTRAR</button>
            <button class="btn-ent">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. MENU LATERAL (SIDEBAR) - ITENS DO PAPEL
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

# 5. ÁREA DE CONTEÚDO (Abaixo do menu)
st.markdown('<div class="content-area">', unsafe_allow_html=True)

if st.session_state.page == "home":
    st.title("Bem-vindo ao Gestor IA")
    st.write("Selecione uma opção no menu lateral para começar.")

elif st.session_state.page == "processar":
    st.subheader("🛠️ PROCESSAR ALGORITMO")
    
    # Seleção de Campeonato
    campeonato = st.selectbox(
        "Selecione o Campeonato:",
        ["Selecione...", "BRASIL (Série A, B, C, D)", "LA LIGA (Espanha)", "PREMIER (Inglaterra)"]
    )

    if campeonato != "Selecione...":
        col1, col_vs, col2 = st.columns([2, 0.5, 2])
        
        # Mock de times
        times = {
            "BRASIL (Série A, B, C, D)": ["Flamengo", "Palmeiras", "São Paulo", "Amazonas", "América-MG"],
            "LA LIGA (Espanha)": ["Real Madrid", "Barcelona", "Atlético Madrid"],
            "PREMIER (Inglaterra)": ["Man City", "Arsenal", "Liverpool"]
        }
        
        lista_times = times.get(campeonato, [])

        with col1:
            time_a = st.selectbox("Time Mandante", ["Selecione..."] + lista_times)
        with col_vs:
            st.markdown("<h2 style='text-align:center; padding-top:20px;'>VS</h2>", unsafe_allow_html=True)
        with col2:
            time_b = st.selectbox("Time Visitante", ["Selecione..."] + lista_times)

        if time_a != "Selecione..." and time_b != "Selecione...":
            if st.button("🚀 EXECUTAR ANÁLISE"):
                st.success(f"Analisando: {time_a} vs {time_b}...")

st.markdown('</div>', unsafe_allow_html=True)
