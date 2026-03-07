import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL (FOCO: ALINHAMENTO DA SIDEBAR) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    /* 1. SUBIR O LOGO (REMOVER ESPAÇO DO TOPO) */
    [data-testid="stSidebar"] { background-color: #111a21 !important; border-right: 2px solid #f05a22 !important; min-width: 250px !important; }
    [data-testid="stSidebar"] > div:first-child { padding-top: 15px !important; } /* Sobe o conteúdo */

    /* HEADER DA SIDEBAR COMPACTO */
    .sidebar-header { display: flex; align-items: center; padding: 5px 10px; margin-bottom: 10px; }
    .ai-logo-box { background-color: #f05a22; padding: 8px; border-radius: 8px; margin-right: 12px; box-shadow: 0 0 10px #f05a22; }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 15px; font-weight: 900; line-height: 1.1; }

    /* 2. AJUSTE DOS BOTÕES (MAIS FINOS PARA CABER TUDO) */
    .stButton > button {
        background-color: #1a242d !important; color: #ffffff !important; border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 32px !important; /* Altura controlada */
        border-radius: 4px !important; margin-bottom: 4px !important; 
        text-transform: uppercase; font-size: 10px !important;
        transition: 0.3s;
    }
    .stButton > button:hover { border-color: #f05a22 !important; color: #f05a22 !important; }
    
    /* ESTILO PARA O BOTÃO SELECIONADO */
    .stButton > button[kind="primary"] {
        background-color: rgba(240,90,34,0.15) !important;
        color: #f05a22 !important;
        border: 1px solid #f05a22 !important;
    }

    /* RÓTULOS DE CATEGORIA COMPACTOS */
    .cat-label { color: #5a6b79; font-size: 10px; font-weight: bold; margin-top: 12px; text-transform: uppercase; border-left: 3px solid #f05a22; padding-left: 8px; margin-bottom: 5px; }

    /* CARD PRINCIPAL (DESIGN v12.0) */
    .card-principal { 
        background-color: #1a242d; padding: 40px; border-radius: 20px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.6); border-bottom: 4px solid #f05a22;
        margin-bottom: 30px; text-align: center;
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 32px; font-weight: 900; text-transform: uppercase; margin-bottom: 30px; }
    .label-prob { color: #ffffff !important; font-size: 14px; font-weight: 800; text-transform: uppercase; }
    .val-prob { color: #f05a22; font-size: 32px; font-weight: 900; }

    /* CAIXA VERDE TRACEJADA */
    .value-box { 
        border: 1px dashed #00ffc3; border-radius: 12px; padding: 15px; 
        display: flex; justify-content: space-around; background: rgba(0, 255, 195, 0.05); margin-top: 30px; 
    }
    .value-item { color: #00ffc3; font-weight: 700; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LÓGICA DE ESTADO ---
if 'liga_ativa' not in st.session_state: 
    st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A - BRASILEIRÃO')

# --- 4. SIDEBAR REORGANIZADA E COMPACTA ---
with st.sidebar:
    # Cabeçalho com o ícone "lindão"
    st.markdown("""
        <div class="sidebar-header">
            <div class="ai-logo-box">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3">
                    <line x1="18" y1="20" x2="18" y2="10"></line>
                    <line x1="12" y1="20" x2="12" y2="4"></line>
                    <line x1="6" y1="20" x2="6" y2="14"></line>
                </svg>
            </div>
            <div class="sidebar-title">GESTOR IA<br>APOSTAS</div>
        </div>
    """, unsafe_allow_html=True)
    
    def sidebar_button(label, id_liga):
        is_active = st.session_state.liga_ativa == id_liga
        if st.button(label, key=f"btn_{id_liga}", type="primary" if is_active else "secondary"):
            st.session_state.liga_ativa = id_liga
            st.rerun()

    st.markdown('<p class="cat-label">🇧🇷 BR NACIONAIS</p>', unsafe_allow_html=True)
    sidebar_button("SÉRIE A - BRASILEIRÃO", 'BRA_A')
    sidebar_button("SÉRIE B - BRASILEIRÃO", 'BRA_B')
    sidebar_button("COPA DO BRASIL", 'CDB')

    st.markdown('<p class="cat-label">🇧🇷 BR ESTADUAIS</p>', unsafe_allow_html=True)
    sidebar_button("PAULISTÃO", 'PAULISTÃO')

    st.markdown('<p class="cat-label">🌎 CONTINENTAIS</p>', unsafe_allow_html=True)
    sidebar_button("LIBERTADORES", 'LIB')
    sidebar_button("SUL-AMERICANA", 'SUL')

    st.markdown('<p class="cat-label">🇪🇺 EUROPA</p>', unsafe_allow_html=True)
    sidebar_button("PREMIER LEAGUE", 'E0')
    sidebar_button("LA LIGA", 'SP1')
    sidebar_button("BUNDESLIGA", 'D1')

# --- 5. ÁREA PRINCIPAL ---
st.markdown(f"### 📍 Liga Selecionada: <span style='color:#f05a22;'>{st.session_state.nome_liga}</span>", unsafe_allow_html=True)

# Botão Executar e Seletores
st.button("🔥 EXECUTAR ALGORITMO COMPLETO")

c1, c2 = st.columns(2)
with c1: t_casa = st.selectbox("Mandante", ["Botafogo", "Flamengo", "Palmeiras", "Chelsea", "Real Madrid"])
with c2: t_fora = st.selectbox("Visitante", ["Corinthians", "Santos", "Vasco", "Arsenal", "Barcelona"], index=1)

# CARD PRINCIPAL (Exemplo fixo para validar o visual)
st.markdown(f"""
    <div class="card-principal">
        <div class="match-title">{t_casa.upper()} VS {t_fora.upper()}</div>
        <div style="display:flex; justify-content:space-around; align-items:center;">
            <div><p class="label-prob">Vitória Casa</p><p class="val-prob">46.0%</p></div>
            <div><p class="label-prob">Empate</p><p class="val-prob">25.1%</p></div>
            <div><p class="label-prob">Vitória Fora</p><p class="val-prob">29.0%</p></div>
        </div>
        <div class="value-box">
            <span class="value-item">Odd Justa: @2.17</span>
            <span class="value-item">Odd Mercado: @2.43</span>
            <span class="value-item">Valor Esperado: +12.9%</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:10px;'>GESTOR IA v12.1 - AJUSTE DE SIDEBAR</p>", unsafe_allow_html=True)
