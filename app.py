import streamlit as st

# 1. Configuração de Página (Sempre no topo)
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# 2. Injeção de CSS Blindado (Protocolo Omega V22)
st.markdown(
    """
    <style>
        /* Fundo da Sidebar (Grafite) e Largura Fixa (280px) */
        [data-testid="stSidebar"] {
            background-color: #383838 !important;
            min-width: 280px !important;
            max-width: 280px !important;
        }

        /* Topo da Sidebar (Onde fica o logo) */
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
            padding-top: 20px;
        }

        /* Header (Azul Royal) */
        header[data-testid="stHeader"] {
            background-color: #002366 !important;
            color: white !important;
        }

        /* Estilização do Logo Roxo (22px) */
        .logo-custom {
            font-size: 22px !important;
            color: #8A2BE2 !important;
            font-weight: 800;
            text-transform: uppercase;
            margin-bottom: 30px;
            padding-left: 10px;
        }

        /* Ajuste dos Itens do Menu (11px) e Correção do Corte de Texto */
        /* Alvo: Botões e Textos na Sidebar */
        .stButton button, .menu-item {
            font-size: 11px !important;
            text-transform: uppercase;
            background-color: transparent !important;
            color: #E0E0E0 !important;
            border: none !important;
            width: 100% !important;
            text-align: left !important;
            padding: 10px 15px 10px 10px !important; /* Padding direito para não cortar */
            white-space: normal !important; /* Permite quebra de linha */
            line-height: 1.3 !important;
            display: flex;
            align-items: center;
        }

        /* Efeito de Hover no Menu */
        .stButton button:hover {
            color: #8A2BE2 !important;
            background-color: rgba(255, 255, 255, 0.05) !important;
        }

        /* Linha Vertical Divisora - Ajuste de Margem */
        [data-testid="stSidebar"] > div:first-child {
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Esconder ícones padrão de navegação se necessário */
        [data-testid="stSidebarNav"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Estrutura de Conteúdo da Sidebar
with st.sidebar:
    # Logo Roxo
    st.markdown('<div class="logo-custom">GESTOR IA</div>', unsafe_allow_html=True)
    
    # Itens do Menu (Simulando sua estrutura da imagem 1)
    # Adicionamos um ícone básico para cada
    st.button("📊 LOCALIZAR APOSTA")
    st.button("📅 JOGOS DO DIA")
    st.button("🎯 PRÓXIMOS JOGOS")
    
    # O ITEM COM PROBLEMA: Agora com segurança de espaço
    st.button("🏆 VENCEDORES DA COMPETIÇÃO") 
    
    st.button("📈 APOSTAS POR ODDS")
    st.button("⚽ APOSTAS POR GOLS")
    st.button("🚩 APOSTAS POR ESCANTEIOS")
    st.button("⚖️ ÁRBITRO DA PARTIDA")

# 4. Área Principal (Main Content)
st.title("PROJETO GESTOR IA")
st.subheader("Protocolo de Sincronização Omega V22 Ativo")

# Exemplo de Dashboard
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Status", "IA OPERACIONAL")
with col2:
    st.metric("Chave", "GIAE-V17-ELITE")
with col3:
    st.metric("Sidebar", "280px FIXED")

st.info("Log: Correção de padding aplicada. O texto 'Vencedores da Competição' agora possui margem interna de segurança.")
