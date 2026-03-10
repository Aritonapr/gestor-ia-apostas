import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="GIAE - PRO EDITION", layout="wide")

# 2. CSS para visual Betano + Sua Identidade
st.markdown("""
    <style>
    /* Fundo Escuro Betano */
    .stApp {
        background-color: #0b1218;
        color: white;
    }

    /* BARRA SUPERIOR (NAVBAR) */
    .navbar {
        background-color: #1a242d;
        padding: 10px 30px;
        display: flex;
        align-items: center;
        border-bottom: 2px solid #f64d23;
        position: fixed;
        top: 0; left: 0; right: 0; z-index: 1000;
        height: 70px;
    }
    .logo-giae {
        background: linear-gradient(45deg, #f64d23, #ff8c00);
        color: white;
        font-family: 'Arial Black', sans-serif;
        font-size: 24px;
        padding: 5px 15px;
        border-radius: 8px;
        margin-right: 30px;
        font-style: italic;
    }
    .nav-link {
        color: #adb5bd;
        margin-right: 25px;
        font-weight: 600;
        font-size: 13px;
        text-transform: uppercase;
        text-decoration: none;
    }
    .nav-link:hover { color: white; }

    /* SIDEBAR CUSTOMIZADA */
    [data-testid="stSidebar"] {
        background-color: #1a242d;
        padding-top: 20px;
    }
    .sidebar-item {
        color: #ffffff;
        padding: 10px;
        border-bottom: 1px solid #2d3843;
        font-size: 14px;
        font-weight: 500;
        text-transform: uppercase;
    }

    /* BOTÕES DA SIDEBAR */
    div.stButton > button {
        width: 100%;
        text-align: left;
        background-color: transparent;
        color: white;
        border: none;
        border-bottom: 1px solid #2d3843;
        border-radius: 0;
        padding: 15px 5px;
        transition: 0.3s;
        text-transform: uppercase;
        font-size: 13px;
    }
    div.stButton > button:hover {
        background-color: #2d3843;
        color: #f64d23;
        border-left: 4px solid #f64d23;
    }

    /* BOTÃO DE PROCESSAR (LARANJA) */
    .btn-processar {
        background-color: #f64d23 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        margin-top: 10px;
    }

    /* Ajuste de espaço para a Navbar */
    .main-content { margin-top: 80px; }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVBAR (TOPO)
st.markdown(f"""
    <div class="navbar">
        <div class="logo-giae">GIAE</div>
        <a class="nav-link" href="#">Apostas Esportivas</a>
        <a class="nav-link" href="#">Apostas ao Vivo</a>
        <a class="nav-link" href="#">Apostas Encontradas</a>
        <a class="nav-link" href="#">Assertividade IA</a>
        <div style="flex-grow: 1;"></div>
        <button style="background:transparent; border:1px solid #adb5bd; color:white; padding:5px 15px; border-radius:4px; margin-right:10px;">REGISTRAR</button>
        <button style="background:#f64d23; border:none; color:white; padding:5px 15px; border-radius:4px;">ENTRAR</button>
    </div>
    """, unsafe_allow_html=True)

# Espaçador para o conteúdo não ficar embaixo da navbar
st.markdown('<div class="main-content"></div>', unsafe_allow_html=True)

# 4. SIDEBAR (CONFORME SEU PAPEL)
with st.sidebar:
    st.write("") # Espaço
    # Iniciamos o estado do sistema
    if 'menu_ativo' not in st.session_state:
        st.session_state.menu_ativo = "home"

    if st.button("🚀 PROCESSAR ALGORITMO"):
        st.session_state.menu_ativo = "processar"
    
    st.button("📅 Próximos Jogos")
    st.button("🏆 Vencedores da Competição")
    st.button("📊 Apostas por Odds")
    st.button("⚽ Apostas por Gols")
    st.button("⛳ Apostas por Escanteios")
    st.button("🟨 Apostas por Cartões")
    st.button("⚖️ Árbitro da Partida")

# 5. CONTEÚDO PRINCIPAL DINÂMICO
if st.session_state.menu_ativo == "home":
    st.title("Bem-vindo ao GIAE")
    st.write("Selecione 'Processar Algoritmo' na lateral para iniciar a análise.")

elif st.session_state.menu_ativo == "processar":
    st.subheader("🤖 Configuração de Análise IA")
    
    col1, col2 = st.columns(2)
    
    with col1:
        campeonato = st.selectbox(
            "Selecione o Campeonato",
            ["Selecione...", "BRASIL (Todos)", "LA LIGA (Espanha)", "PREMIER (Inglaterra)"]
        )

    # Lógica de seleção de times baseada no campeonato
    if campeonato != "Selecione...":
        with col2:
            if "BRASIL" in campeonato:
                times = ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Galo", "Grêmio"]
            elif "LA LIGA" in campeonato:
                times = ["Real Madrid", "Barcelona", "Atlético de Madrid", "Sevilla"]
            else:
                times = ["Man City", "Arsenal", "Liverpool", "Man United", "Chelsea"]
            
            time_selecionado = st.selectbox("Escolha o Confronto / Time", times)
        
        # Área de resultados (vazia por enquanto)
        st.markdown("---")
        st.markdown(f"### Analisando: **{time_selecionado}**")
        st.info("Aguardando definição dos algoritmos de busca e análise...")
        
        # Botão final de execução
        if st.button("🔥 INICIAR ANÁLISE PROFUNDA"):
            st.warning("IA em desenvolvimento para este mercado.")

# Rodapé de Status
st.markdown("""
    <div style="position: fixed; bottom: 10px; right: 20px; color: #666; font-size: 10px;">
        GIAE PRO v2.0 | Layout Baseado em Betano Interface
    </div>
    """, unsafe_allow_html=True)
