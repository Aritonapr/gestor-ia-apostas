import streamlit as st
import pandas as pd
import numpy as np

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL BLINDADO (RESTAURAÇÃO TOTAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    /* SIDEBAR: SUBIR LOGO E COMPACTAR SEM TREPAR */
    [data-testid="stSidebar"] { background-color: #111a21 !important; border-right: 2px solid #f05a22 !important; min-width: 250px !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { padding-top: 10px !important; gap: 0px !important; }
    
    .sidebar-header { display: flex; align-items: center; padding: 5px 10px; margin-top: -30px; margin-bottom: 10px; }
    .ai-logo-box { background-color: #f05a22; padding: 8px; border-radius: 8px; margin-right: 12px; box-shadow: 0 0 15px #f05a22; }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 14px; font-weight: 900; line-height: 1.1; }

    /* BOTÕES DA SIDEBAR (FINOS E ALINHADOS) */
    [data-testid="stSidebar"] .stButton > button {
        background-color: #1a242d !important; color: #ffffff !important; border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 28px !important; 
        border-radius: 4px !important; margin-bottom: 2px !important; text-transform: uppercase; font-size: 8px !important;
        padding: 0 !important; display: flex; align-items: center; justify-content: center;
    }
    [data-testid="stSidebar"] .stButton > button[kind="primary"] { border: 1px solid #f05a22 !important; color: #f05a22 !important; background: rgba(240,90,34,0.1) !important; }
    .cat-label { color: #5a6b79; font-size: 8px; font-weight: bold; margin-top: 8px; text-transform: uppercase; border-left: 2px solid #f05a22; padding-left: 5px; margin-bottom: 4px; }

    /* BOTÃO DE ALERTA (LARANJA SÓLIDO E PISCANTE) */
    .stButton > button[key="alerta_final"] {
        background-color: #f05a22 !important; 
        color: white !important; 
        height: 50px !important; 
        font-family: 'Orbitron', sans-serif !important; 
        font-weight: 900 !important;
        font-size: 14px !important;
        border-radius: 10px !important;
        border: none !important;
        box-shadow: 0 0 20px rgba(240,90,34,0.5) !important;
        animation: pulse-orange 1.5s infinite !important;
    }
    @keyframes pulse-orange { 0% { opacity: 1; } 50% { opacity: 0.7; } 100% { opacity: 1; } }

    /* BOTÕES DE NAVEGAÇÃO */
    .nav-buttons button { background-color: #1a242d !important; color: white !important; border: 1px solid #2d3748 !important; height: 40px !important; font-size: 11px !important; }

    /* CARD PRINCIPAL v12.0 (LETRAS BRANCAS NÍTIDAS) */
    .card-principal { 
        background-color: #1a242d; padding: 40px; border-radius: 20px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.6); border-bottom: 5px solid #f05a22;
        margin-bottom: 30px; text-align: center; border: 1px solid #2d3748;
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 32px; font-weight: 900; text-transform: uppercase; margin-bottom: 35px; letter-spacing: 2px; }
    .label-prob { color: #ffffff !important; font-size: 14px; font-weight: 800; text-transform: uppercase; margin-bottom: 10px; display: block; }
    .val-prob { color: #f05a22 !important; font-size: 36px; font-weight: 900; }

    /* CAIXA VERDE TRACEJADA */
    .value-box { border: 2px dashed #00ffc3; border-radius: 12px; padding: 20px; display: flex; justify-content: space-around; background: rgba(0, 255, 195, 0.05); margin-top: 40px; }
    .value-item { color: #00ffc3 !important; font-weight: 800; font-size: 14px; }

    /* MINI CARDS */
    .mini-card { background-color: #111a21; padding: 15px; border-radius: 12px; border: 1px solid #2d3748; text-align: center; height: 110px; display: flex; flex-direction: column; justify-content: center; }
    .mini-label { color: #ffffff !important; font-weight: 800; font-size: 11px; text-transform: uppercase; margin-bottom: 12px; }
    .mini-val { color: #00ffc3 !important; font-weight: 900; font-size: 24px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGICA DE ESTADO ---
if 'pg' not in st.session_state: st.session_state.update(pg='radar', liga='BRA_A', nome='SÉRIE A')

# --- 4. SIDEBAR (LOGO NO TOPO + COMPACTAÇÃO) ---
with st.sidebar:
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
    
    def sb_btn(label, id_liga):
        if st.button(label, key=f"sb_{id_liga}", type="primary" if st.session_state.liga == id_liga else "secondary"):
            st.session_state.liga = id_liga
            st.session_state.nome = label
            st.rerun()

    st.markdown('<p class="cat-label">🇧🇷 BRASIL</p>', unsafe_allow_html=True)
    sb_btn("SÉRIE A - BRASILEIRÃO", 'BRA_A')
    sb_btn("SÉRIE B - BRASILEIRÃO", 'BRA_B')
    sb_btn("COPA DO BRASIL", 'CDB')
    sb_btn("PAULISTÃO", 'PAULISTÃO')
    
    st.markdown('<p class="cat-label">🌎 CONTINENTAIS</p>', unsafe_allow_html=True)
    sb_btn("LIBERTADORES", 'LIB')
    sb_btn("SUL-AMERICANA", 'SUL')
    
    st.markdown('<p class="cat-label">🇪🇺 EUROPA</p>', unsafe_allow_html=True)
    sb_btn("PREMIER LEAGUE", 'E0')
    sb_btn("LA LIGA", 'SP1')
    sb_btn("BUNDESLIGA", 'D1')

# --- 5. ÁREA PRINCIPAL ---
# BOTÃO DE ALERTA VIP REAL (LARANJA SÓLIDO)
if st.button("⚠️ APOSTAS ENCONTRADAS IA: 12 OPORTUNIDADES DISPONÍVEIS", key="alerta_final"):
    st.session_state.pg = 'scanner'

st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
c_nav1, c_nav2, c_nav3 = st.columns(3)
with c_nav1: 
    if st.button("🎯 RADAR NEURAL", key="n1"): st.session_state.pg = 'radar'
with c_nav2:
    if st.button("🔍 SCANNER DIÁRIO", key="n2"): st.session_state.pg = 'scanner'
with c_nav3:
    if st.button("💰 GESTÃO BANCA", key="n3"): st.session_state.pg = 'gestao'
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.pg == 'radar':
    if st.button("🚀 EXECUTAR ALGORITMO COMPLETO", key="run"): st.session_state.run = True
    c1, c2 = st.columns(2)
    with c1: t_casa = st.selectbox("Mandante", ["Botafogo", "Flamengo", "Palmeiras", "Chelsea", "Real Madrid"], key="s1")
    with c2: t_fora = st.selectbox("Visitante", ["Corinthians", "Santos", "Arsenal", "Barcelona", "Bayern"], index=1, key="s2")

    if st.session_state.get('run'):
        st.markdown(f"""
            <div class="card-principal">
                <div class="match-title">{t_casa} VS {t_fora}</div>
                <div style="display:flex; justify-content:space-around;">
                    <div><span class="label-prob">Vitória Casa</span><span class="val-prob">48.2%</span></div>
                    <div><span class="label-prob">Empate</span><span class="val-prob">24.5%</span></div>
                    <div><span class="label-prob">Vitória Fora</span><span class="val-prob">27.3%</span></div>
                </div>
                <div class="value-box">
                    <span class="value-item">Odd Justa: @2.07</span>
                    <span class="value-item">Odd Mercado: @2.35</span>
                    <span class="value-item">Valor Esperado: +12.9%</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        m = st.columns(6)
        with m[0]: st.markdown("<div class='mini-card'><span class='mini-label'>⚽ GOLS +2.5</span><span class='mini-val'>62%</span></div>", unsafe_allow_html=True)
        with m[1]: st.markdown("<div class='mini-card'><span class='mini-label'>🚩 CANTOS +9.5</span><span class='mini-val'>81%</span></div>", unsafe_allow_html=True)
        with m[2]: st.markdown("<div class='mini-card'><span class='mini-label'>👞 CHUTES +22.5</span><span class='mini-val'>77%</span></div>", unsafe_allow_html=True)
        with m[3]: st.markdown("<div class='mini-card'><span class='mini-label'>🎯 NO GOL +8.5</span><span class='mini-val'>65%</span></div>", unsafe_allow_html=True)
        with m[4]: st.markdown("<div class='mini-card'><span class='mini-label'>⚠️ FALTAS +24.5</span><span class='mini-val'>88%</span></div>", unsafe_allow_html=True)
        with m[5]: st.markdown("<div class='mini-card'><span class='mini-label'>🟨 CARTÕES +4.5</span><span class='mini-val'>72%</span></div>", unsafe_allow_html=True)

elif st.session_state.pg == 'scanner':
    st.markdown(f"### 🔍 Scanner de Oportunidades: {st.session_state.nome}")
    st.expander("💰 JOGO COM VALOR: Botafogo x Santos").write("Análise Sugerida: Over Gols / Vitória Mandante.")
    st.expander("💰 JOGO COM VALOR: Real Madrid x Barcelona").write("Análise Sugerida: Ambas Marcam.")

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:9px;'>GESTOR IA v15.1 - ESTABILIDADE VISUAL ALCANÇADA</p>", unsafe_allow_html=True)
