import streamlit as st

# 1. Configuração inicial
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. CSS DE ALTA PRECISÃO (Compactação Máxima da Sidebar)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap');

    /* TEMA DARK PROFISSIONAL */
    :root {
        --bg-dark: #0b0e11;
        --bg-sidebar: #15191d;
        --accent-orange: #f64d23;
        --accent-green: #00cc66;
        --text-main: #e2e8f0;
        --text-dim: #94a3b8;
    }

    /* REMOVER TUDO DO STREAMLIT */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] {
        display: none !important;
    }

    .stApp { background-color: var(--bg-dark) !important; color: var(--text-main) !important; font-family: 'Roboto', sans-serif !important; }

    /* --- NAVBAR SUPERIOR --- */
    .pro-navbar {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 50px;
        background-color: var(--bg-sidebar);
        border-bottom: 2px solid var(--accent-orange);
        display: flex; align-items: center;
        padding: 0 20px; z-index: 999999;
    }

    /* LOGO CYBER-HEX NEON */
    .logo-box { display: flex; align-items: center; gap: 10px; }
    .cyber-hex {
        width: 28px; height: 32px;
        background: var(--accent-orange);
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 0 15px rgba(246, 77, 35, 0.4);
    }
    .hexagon-inner {
        width: 18px; height: 22px; background-color: var(--bg-sidebar);
        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
    }
    .logo-text { color: var(--accent-orange); font-weight: 900; font-size: 18px; font-style: italic; }

    .nav-links { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; }
    .nav-links span { color: var(--text-main); font-size: 11px; font-weight: 700; text-transform: uppercase; cursor: pointer; opacity: 0.8; }

    /* --- SIDEBAR CORRIGIDA (SUBIR TEXTO AO MÁXIMO) --- */
    [data-testid="stSidebar"] {
        background-color: var(--bg-sidebar) !important;
        margin-top: 50px !important;
        border-right: 1px solid #2d3843 !important;
        width: 260px !important;
    }
    
    /* ZERAR O PADDING DO CONTEÚDO PARA SUBIR OS BOTÕES */
    [data-testid="stSidebarContent"] {
        padding-top: 0px !important; 
        overflow-y: hidden !important; /* MATA O SCROLL */
        overflow-x: hidden !important;
    }

    /* ESTILO DOS BOTÕES DA LATERAL (MAIS COMPACTOS) */
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        color: var(--text-main) !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        font-weight: 700 !important;
        font-size: 11px !important;
        padding: 6px 15px !important; /* Padding reduzido para caber tudo */
        min-height: 35px !importa
