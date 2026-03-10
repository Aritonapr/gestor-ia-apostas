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
        top: 70px !important; /* Começa ex
