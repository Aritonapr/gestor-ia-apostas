import streamlit as st
import pandas as pd
import hashlib

# --- 1. CONFIGURAÇÃO DA PÁGINA (Sidebar um pouco mais larga para caber os nomes) ---
st.set_page_config(
    page_title="GESTOR IA - PRO EDITION", 
    layout="wide", 
    page_icon="⚽",
    initial_sidebar_state="expanded"
)

# --- 2. CSS AJUSTADO E PRECISO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    /* Forçar largura da Sidebar para não esmagar os botões */
    [data-testid="stSidebar"] {
        min-width: 300px !important;
        max-width: 300px !important;
        background-color: #0b1218 !important;
        border-right: 2px solid #f05a22 !important;
    }

    /* Ajuste global de fontes */
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }

    /* ESTILO DOS BOTÕES DE LIGA (Série A, Premier, etc) */
    .stButton > button {
        width: 100% !important;
        height: 38px !important;
        background: linear-gradient(90deg, rgba(240, 90, 34, 0.1) 0%, rgba(26, 36, 45, 0.8) 100%) !important;
        color: #cbd5e0 !important;
        font-size: 10px !important; /* Tamanho otimizado */
        font-weight: 700 !important;
        text-transform: uppercase;
        border-radius: 8px !important;
        border: 1px solid rgba(240, 90, 34, 0.2) !important;
        transition: all 0.2s ease;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: clip !important;
        padding: 0px 5px !important; /* Padding mínimo para caber o texto */
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* Efeito ao passar o mouse */
    .stButton > button:hover {
        border-color: #f05a22 !important;
        color: #fff !important;
        background: #f05a22 !important;
        transform: scale(1.02);
    }

    /* Botão da Liga Ativa */
    .stButton > button[kind="primary"] {
        background: #f05a22 !important;
        color: white !important;
        border: 1px solid #fff !important;
        box-shadow: 0 0 10px rgba(240, 90, 34, 0.5) !important;
    }

    /* BOTÕES MÃE (Categorias: FUTEBOL BRASIL, etc) */
    .cat-button > div > button {
        background: rgba(240, 90, 34, 0.05) !important;
        border-bottom: 2px solid #f05a22 !important;
        border-top: none !important;
        border-left: none !important;
        border-right: none !important;
        border-radius: 0px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 12px !important;
        color: #f05a22 !important;
        justify-content: flex-start !important;
        padding-left: 10px !important;
        height: 45px !important;
        margin-top: 15px !important;
    }

    /* Ajuste de colunas na sidebar para não apertar */
    [data-testid="column"] {
        padding: 0 2px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DE NAVEGAÇÃO ---
if 'liga_ativa' not in st.session_state: st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A')
if 'menu_aberto' not in st.session_state: st.session_state.menu_aberto = 'BR'

with st.sidebar:
    st.markdown(f"<h1 style='color:#f05a22; font-family:Orbitron; font-size:20px; text-align:center;'>⚽ GESTOR IA</h1>", unsafe_allow_html=True)
    st.write("---")

    def s_btn(icon, display, vid):
        # Botão de liga individual
        label = f"{icon} {display}"
        if st.button(label, key=f"s_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid; st.rerun()

    # Categoria Brasil
    st.markdown('<div class="cat-button">', unsafe_allow_html=True)
    if st.button("📁 FUTEBOL BRASIL", key="cat_br"):
        st.session_state.menu_aberto = "BR" if st.session_state.menu_aberto != "BR" else None; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.menu_aberto == "BR":
        c1, c2 = st.columns(2)
        with c1: 
            s_btn("🔘", "SÉRIE A", "BRA_A")
            s_btn("🏆", "COPA BR", "CDB")
        with c2: 
            s_btn("🔘", "SÉRIE B", "BRA_B")
            s_btn("☀️", "NORDESTE", "CNE")

    # Categoria Europa
    st.markdown('<div class="cat-button">', unsafe_allow_html=True)
    if st.button("🌍 ELITE EUROPA", key="cat_eu"):
        st.session_state.menu_aberto = "EU" if st.session_state.menu_aberto != "EU" else None; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.menu_aberto == "EU":
        c1, c2 = st.columns(2)
        with c1: 
            s_btn("🏴󠁧󠁢󠁥󠁮󠁧󠁿", "PREMIER", "ENG_P")
            s_btn("🇮🇹", "SERIE A", "ITA_A")
        with c2: 
            s_btn("🇪🇸", "LA LIGA", "ESP_L")
            s_btn("🇩🇪", "BUNDES", "GER_B")

# --- CONTEÚDO PRINCIPAL ---
st.markdown(f"<h2 style='font-family:Orbitron; color:#f05a22; font-size:18px;'>📊 {st.session_state.liga_ativa.replace('_', ' ')}</h2>", unsafe_allow_html=True)

# O restante do seu código (selectbox, engine, processar) continua aqui...
