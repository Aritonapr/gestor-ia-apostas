import streamlit as st
import time

# ==============================================================================
# [GIAE KERNEL SHIELD v25.0 - PROTOCOLO JARVIS SUPREME]
# ESTADO: EXPANSÃO DASHBOARD (6 CARDS / GRID 3x2)
# FIX: ALINHAMENTO PROPORCIONAL E SIMETRIA VISUAL
# CHAVE DE SEGURANÇA: GIAE-V17-ELITE-RECOVERY
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CONTROLE DE NAVEGAÇÃO INTERNO ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"

# --- [LOCK] BLOCO DE SEGURANÇA CSS (NÃO ALTERAR) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET E BLINDAGEM DE FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; }
    
    [data-testid="stMainBlockContainer"] {
        padding-top: 0rem !important;
        padding-bottom: 1rem !important;
    }

    /* SIDEBAR LOCK (320PX E SEM SCROLLBAR) */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; padding-top: 0px !important; }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }
    [data-testid="stSidebarContent"] { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    [data-testid="stSidebarResizer"] { display: none !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    /* [02] NAVBAR SUPERIOR (AZUL ROYAL) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; 
        border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between;
        padding: 0 40px !important; z-index: 999999; 
    }
    
    .logo-text { 
        color: #9d54ff !important; font-weight: 900; font-size: 22px !important;
        text-transform: uppercase; letter-spacing: 1.5px !important; 
        margin-right: 60px !important; white-space: nowrap; cursor: pointer;
    }

    .nav-items { display: flex; gap: 25px; align-items: center; }
    .nav-items span { 
        color: #ffffff; font-size: 11px !important; text-transform: uppercase; 
        letter-spacing: 0.5px !important; cursor: pointer; transition: 0.2s;
    }
    .nav-items span:hover { color: #9d54ff; text-shadow: 0 0 10px #9d54ff; }

    /* HEADER INTERATIVO */
    .header-right { display: flex; align-items: center; gap: 20px; }
    .search-icon { color: #ffffff !important; cursor: pointer !important; font-size: 18px !important; transition: 0.3s !important; }
    .search-icon:hover { color: #9d54ff !important; transform: scale(1.2) !important; }
    
    .registrar-pill { 
        color: #ffffff !important; font-size: 10px !important; font-weight: 700 !important; text-transform: uppercase !important; 
        border: 1px solid #ffffff !important; padding: 7px 20px !important; border-radius: 20px !important; cursor: pointer !important; transition: 0.3s !important;
    }
    .registrar-pill:hover { background: #ffffff !important; color: #002366 !important; transform: translateY(-1px); }

    .entrar-grad {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: white !important; padding: 8px 25px !important; border-radius: 4px !important;
        font-weight: 800 !important; font-size: 11px !important; cursor: pointer !important; text-transform: uppercase !important;
        transition: 0.3s !important; box-shadow:
