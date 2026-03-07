import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="GESTOR IA APOSTAS", 
    layout="wide", 
    page_icon="⚽",
    initial_sidebar_state="expanded"
)

# --- 2. CSS DE ALTO NÍVEL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stSidebarCollapse"] { display: none !important; }
    button[kind="headerNoPadding"] { display: none !important; }
    .block-container { padding-top: 1rem !important; }
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    [data-testid="stSidebar"] { 
        background-color: #0b1218; 
        border-right: 1px solid rgba(240, 90, 34, 0.2); 
        width: 300px !important; 
    }
    
    /* ESTILO DOS BOTÕES */
    .stButton > button {
        background-color: rgba(26, 36, 45, 0.4) !important; color: #cbd5e0 !important; 
        border: none !important; border-left: 2px solid transparent !important;
        font-weight: 700 !important; height: 32px !important; text-transform: uppercase; 
        font-size: 7.5pt !important;
        width: 100% !important; text-align: center !important; 
        white-space: nowrap !important; border-radius: 4px !important;
        margin-bottom: 2px !important;
    }

    /* BOTÃO DE CATEGORIA (MESTRE) */
    .cat-button > div > button {
        background-color: rgba(240, 90, 34, 0.05) !important;
        color: #ffffff !important;
        border-bottom: 1px solid rgba(240, 90, 34, 0.2) !important;
        font-size: 8.5pt !important;
        height: 40px !important;
        letter-spacing: 1px;
    }

    /* BOTÃO ATIVO */
    .stButton > button[kind="primary"] { 
        background-color: rgba(240, 90, 34, 0.1) !important; 
        color: #f05a22 !important; 
        border-left: 3px solid #f05a22 !important; 
    }

    .card-principal { 
        background-color: #1a242d; padding: 15px 20px; border-radius: 12px; 
        border-bottom: 4px solid #f05a22; text-align: center; 
        margin-top: 25px !important; margin-bottom: 15px !important;
    }

    [data-testid="stHorizontalBlock"] { gap: 10px !important; display: flex !important; flex-wrap: nowrap !important; }

    .mini-card { 
        background-color: #111a21; padding: 10px 5px; border-radius: 8px; 
        border: 1px solid #2d3748; text-align: center; width: 100%; height: 100px;
        display: flex; flex-direction: column; justify-content: center;
    }
    .mini-label { color: #ffffff !important; font-size: 8.5px !important; font-weight: 800 !important; text-transform: uppercase; margin-bottom: 8px !important; }
    .mini-val { color: #00ffc3 !important; font-weight: 900 !important; font-size: 19px !important; text-shadow: 0 0 10px rgba(0, 255, 195, 0.2); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LÓGICA DE ESTADO (MENUS E LIGAS) ---
if 'liga_ativa' not in st.session_state: 
    st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A')
if 'menu_aberto' not in st.session_state:
    st.session_state.menu_aberto = 'BRASIL' # Começa com Brasil aberto

# --- 4. BARRA LATERAL (SISTEMA DE MENUS DROPDOWN) ---
with st.sidebar:
    # Função para o botão da liga (filho)
    def s_btn(display, full, vid):
        is_active = st.session_state.liga_ativa == vid
        if st.button(display, key=f"s_{vid}", type="primary" if is_active else "secondary"):
            st.session_state.liga_ativa = vid
            st.session_state.nome_liga = full
            st.rerun()

    # Função para o botão da categoria (mestre)
    def cat_btn(label, menu_id):
        # Container especial para estilizar o botão mestre via CSS
        st.markdown('<div class="cat-button">', unsafe_allow_html=True)
        if st.button(f" {label}", key=f"cat_{menu_id}"):
            # Se clicar no que já está aberto, ele fecha, senão abre o novo
            st.session_state.menu_aberto = menu_id if st.session_state.menu_aberto != menu_id else None
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # --- CATEGORIA: BRASILEIRÃO ---
    cat_btn("📂 BRASILEIRÃO", "BRASIL")
    if st.session_state.menu_aberto == "BRASIL":
        c1, c2 = st.columns(2)
        with c1: s_btn("SÉRIE A", "BRASILEIRÃO SÉRIE A", "BRA_A"); s_btn("SÉRIE C", "BRASILEIRÃO SÉRIE C", "BRA_C")
        with c2: s_btn("SÉRIE B", "BRASILEIRÃO SÉRIE B", "BRA_B"); s_btn("SÉRIE D", "BRASILEIRÃO SÉRIE D", "BRA_D")

    # --- CATEGORIA: COPAS ---
    cat_btn("🏆 COPAS", "COPAS")
    if st.session_state.menu_aberto == "COPAS":
        c1, c2 = st.columns(2)
        with c1: s_btn("BRASIL", "COPA DO BRASIL", "CDB"); s_btn("SUPERCOPA", "SUPERCOPA", "SUPER")
        with c2: s_btn("NORDESTE", "COPA DO NORDESTE", "CNE")

    # --- CATEGORIA: ESTADUAIS ---
    cat_btn("📍 ESTADUAIS", "ESTADUAIS")
    if st.session_state.menu_aberto == "ESTADUAIS":
        c1, c2 = st.columns(2)
        with c1: s_btn("PAULISTÃO", "PAULISTÃO", "SP"); s_btn("MINEIRO", "MINEIRO", "MG")
        with c2: s_btn("CARIOCA", "CARIOCA", "RJ"); s_btn("GAÚCHO", "GAÚCHO", "RS")

    # --- CATEGORIA: CONTINENTAIS ---
    cat_btn("🌎 CONTINENTAIS", "CONTINENTAIS")
    if st.session_state.menu_aberto == "CONTINENTAIS":
        s_btn("LIBERTADORES", "LIBERTADORES", "LIB")
        s_btn("SUL-AMERICANA", "SUL-AMERICANA", "SUL")

# --- 5. ÁREA PRINCIPAL ---
st.markdown("""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
        <div style="position: relative; width: 38px; height: 38px; display: flex; align-items: center; justify-content: center;">
            <svg style="position: absolute; width: 100%; height: 100%; fill: none; stroke: #f05a22; stroke-width: 3;" viewBox="0 0 100 100">
                <path d="M50 5 L90 25 L90 75 L50 95 L10 75 L10 25 Z" />
            </svg>
            <div style="width: 12px; height: 12px; background-color: #f05a22; clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);"></div>
        </div>
        <div style="color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 20px; font-weight: 900; letter-spacing: 2px;">GESTOR IA</div>
    </div>
""", unsafe_allow_html=True)

times = ['Flamengo', 'Palmeiras', 'Bahia', 'Botafogo', 'Vasco', 'Corinthians', 'Santos', 'Inter']
col_a, col_b, col_btn = st.columns([3, 3, 2.5])
with col_a: t_casa = st.selectbox("Mandante", sorted(times), label_visibility="collapsed")
with col_b: t_fora = st.selectbox("Visitante", sorted([t for t in times if t != t_casa]), label_visibility="collapsed")
with col_btn: executar = st.button("🔥 EXECUTAR ALGORITMO", use_container_width=True, type="primary")

if executar:
    st.markdown(f'<div style="font-size:10px; color:#f05a22; font-family:Orbitron; margin-bottom:10px; border-left:4px solid #f05a22; padding-left:10px;">📡 ANALISANDO: {st.session_state.nome_liga}</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="card-principal">
            <div style="color: #ffffff; font-family: 'Orbitron', sans-serif; font-size: 22px; font-weight: 800; margin-bottom: 20px;">{t_casa.upper()} VS {t_fora.upper()}</div>
            <div style="display: flex; justify-content: space-around; background: rgba(0,0,0,0.3); border-radius: 10px; padding: 15px 0;">
                <div><p style="color: #f05a22; font-size: 26px; font-weight: 900; margin:0;">44.2%</p><p style="color:#cbd5e0; font-size:10px; font-weight:700; text-transform:uppercase; margin-top:5px;">Mandante</p></div>
                <div><p style="color: #f05a22; font-size: 26px; font-weight: 900; margin:0;">22.8%</p><p style="color:#cbd5e0; font-size:10px; font-weight:700; text-transform:uppercase; margin-top:5px;">Empate</p></div>
                <div><p style="color: #f05a22; font-size: 26px; font-weight: 900; margin:0;">33.0%</p><p style="color:#cbd5e0; font-size:10px; font-weight:700; text-transform:uppercase; margin-top:5px;">Visitante</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    m1, m2, m3, m4, m5, m6 = st.columns(6)
    metrics = [
        ("⚽ GOLS +2.5", "62%"), ("🚩 ESCANTEIOS +9.5", "75%"), ("👞 CHUTES +22", "81%"), 
        ("🎯 NO GOL +8", "58%"), ("⚠️ FALTAS +24", "85%"), ("🟨 CARTÕES +4", "72%")
    ]
    
    cols = [m1, m2, m3, m4, m5, m6]
    for i, (label, val) in enumerate(metrics):
        with cols[i]:
            st.markdown(f"""
                <div class="mini-card">
                    <span class="mini-label">{label}</span>
                    <p class="mini-val">{val}</p>
                </div>
            """, unsafe_allow_html=True)
else:
    st.markdown("<div style='height:150px;'></div>", unsafe_allow_html=True)
