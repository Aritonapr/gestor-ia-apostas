import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA (DEVE SER A PRIMEIRA LINHA) ---
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide")

# --- PROTOCOLO OMEGA V22: INJEÇÃO DE INTERFACE BLINDADA ---
st.markdown(
    """
    <style>
        /* 1. Cores da Estrutura */
        header[data-testid="stHeader"] {
            background-color: #002366 !important; /* Azul Royal */
        }
        
        section[data-testid="stSidebar"] {
            background-color: #383838 !important; /* Grafite */
            width: 280px !important;
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* 2. Ajuste da Sidebar (Largura Fixa) */
        [data-testid="stSidebar"][aria-expanded="true"] {
            min-width: 280px !important;
            max-width: 280px !important;
        }

        /* 3. Estilização do Logo Roxo (22px) */
        .logo-text {
            font-size: 22px !important;
            color: #8A2BE2 !important; /* Roxo */
            font-weight: bold;
            padding-left: 10px;
            margin-bottom: 20px;
            display: block;
        }

        /* 4. Menu Lateral (11px) e Correção de Corte de Texto */
        [data-testid="stSidebarNav"] ul {
            padding-top: 20px;
        }

        /* Alvo específico para os links do menu */
        [data-testid="stSidebarNav"] li div span {
            font-size: 11px !important;
            color: #FFFFFF !important;
            white-space: normal !important; /* Permite quebra de linha */
            word-wrap: break-word !important;
            padding-right: 25px !important; /* Margem de segurança da linha vertical */
            line-height: 1.4 !important;
        }

        /* 5. Ajuste Geral de Margens do Menu */
        [data-testid="stSidebarNav"] {
            max-height: none !important;
            padding-bottom: 100px;
        }

        /* Estilização para icones da Sidebar se houver */
        [data-testid="stSidebarNav"] li svg {
            width: 16px !important;
            height: 16px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- ESTRUTURA VISUAL DA SIDEBAR (JARVIS SHIELD) ---
with st.sidebar:
    st.markdown('<div class="logo-text">GESTOR IA</div>', unsafe_allow_html=True)
    
    # Aqui os itens do menu serão gerados automaticamente se você usar arquivos na pasta /pages
    # Ou manualmente como abaixo:
    st.write("---")
    st.markdown("### Navegação")

# --- CONTEÚDO PRINCIPAL (Exemplo de Dashboard) ---
st.title("PROJETO GESTOR IA")
st.subheader("Protocolo de Sincronização Omega V22 Ativo")

col1, col2, col3 = st.columns(3)
with col1:
    st.info("Status: IA OPERACIONAL")
with col2:
    st.success("Chave: GIAE-V17-ELITE-RECOVERY")
with col3:
    st.warning("Interface: Blindada (280px)")

# Mensagem de Log do Sistema
st.write("---")
st.code("LOG: Ajuste de padding-right aplicado ao menu lateral para evitar colisão de borda.")
