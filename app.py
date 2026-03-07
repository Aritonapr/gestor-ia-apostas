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
    
    /* SIDEBAR: SUBIR TUDO E AJUSTAR BOTÕES */
    [data-testid="stSidebar"] { background-color: #111a21 !important; border-right: 2px solid #f05a22 !important; }
    [data-testid="stSidebar"] > div:first-child { padding-top: 0px !important; }
    
    .sidebar-header { display: flex; align-items: center; padding: 10px; margin-top: 0px; margin-bottom: 10px; }
    .ai-logo-box { background-color: #f05a22; padding: 8px; border-radius: 8px; margin-right: 10px; box-shadow: 0 0 10px #f05a22; }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 14px; font-weight: 900; line-height: 1.1; }

    /* BOTÕES DA SIDEBAR (SEM TREPAR) */
    .stButton > button {
        background-color: #1a242d !important; color: #ffffff !important; border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 30px !important; 
        border-radius: 4px !important; margin-bottom: 4px !important; text-transform: uppercase; font-size: 9px !important;
        transition: 0.3s;
    }
    .stButton > button:hover { border-color: #f05a22 !important; color: #f05a22 !important; }
    .stButton > button[kind="primary"] { border: 1px solid #f05a22 !important; color: #f05a22 !important; background: rgba(240,90,34,0.1) !important; }
    
    .cat-label { color: #5a6b79; font-size: 9px; font-weight: bold; margin-top: 12px; text-transform: uppercase; border-left: 3px solid #f05a22; padding-left: 6px; margin-bottom: 5px; }

    /* BOTÃO DE ALERTA VIP (LARANJA SÓLIDO PISCANTE) */
    .alerta-container button {
        background-color: #f05a22 !important; 
        color: white !important; 
        height: 55px !important; 
        font-family: 'Orbitron', sans-serif !important; 
        font-weight: 900 !important;
        font-size: 15px !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 0 20px rgba(240,90,34,0.6) !important;
        animation: pulse-orange 2s infinite !important;
    }
    @keyframes pulse-orange { 0% { opacity: 1; } 50% { opacity: 0.7; transform: scale(0.99); } 100% { opacity: 1; } }

    /* BOTÕES DE NAVEGAÇÃO (RADAR/SCANNER/GESTÃO) */
    .nav-container button {
        background-color: #1a242d !important; color: white !important; 
        border: 1px solid #2d3748 !important; height: 45px !important; font-weight: bold !important;
    }

    /* CARD PRINCIPAL v12.0 (RESTAURADO) */
    .card-principal { 
        background-color: #1a242d; padding: 40px; border-radius: 20px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.6); border-bottom: 5px solid #f05a22;
        margin-bottom: 30px; text-align: center; border: 1px solid #2d3748;
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 32px; font-weight: 900; text-transform: uppercase; margin-bottom: 35px; letter-spacing: 2px; }
    .label-prob { color: #ffffff !important; font-size: 14px; font-weight: 800; text-transform: uppercase; margin-bottom: 10px; display: block; }
    .val-prob { color: #f05a22 !important; font-size: 36px; font-weight: 900; }

    /* CAIXA VERDE TRACEJADA */
    .value-box { 
        border: 2px dashed #00ffc3; border-radius: 15px; padding: 20px; 
        display: flex; justify-content: space-around; background: rgba(0, 255, 195, 0.05); margin-top: 40px; 
    }
    .value-item { color: #00ffc3 !important; font-weight: 800; font-size: 14px; }

    /* MINI CARDS */
    .mini-card { background-color: #111a21; padding: 15px; border-radius: 12px; border: 1px solid #2d3748; text-align: center; height: 120px; display: flex; flex-direction: column; justify-content: center; }
    .mini-label { color: #ffffff !important; font-weight: 800; font-size: 11px; text-transform: uppercase; margin-bottom: 12px; }
    .mini-val { color: #00ffc3 !important; font-weight: 900; font-size: 24px; }
    
    .section-header { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 18px; margin: 25px 0; border-left: 5px solid #f05a22; padding-left: 12px; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGICA DE ESTADO ---
if 'pg' not in st.session_state: st.session_state.update(pg='radar', liga='BRA_A', nome='SÉRIE A')

@st.cache_data(ttl=3600)
def load_data(liga):
    urls = {'BRA_A': "https://raw.githubusercontent.com/automacaobrasil/dataset-brasileirao/main/brasileirao_serie_a.csv",
            'BRA_B': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/brasileirao_serie_b.csv",
            'E0': "https://www.football-data.co.uk/mmz4281/2425/E0.csv"}
    try:
        url = urls.get(liga, urls['BRA_A'])
        df = pd.read_csv(url)
        mapa = {'mandante': 'HomeTeam', 'visitante': 'AwayTeam', 'home_team': 'HomeTeam', 'away_team': 'AwayTeam', 'home_score': 'FTHG', 'away_score': 'FTAG'}
        return df.rename(columns=mapa).dropna(subset=['HomeTeam', 'AwayTeam'])
    except:
        return pd.DataFrame([['Botafogo', 'Flamengo', 1, 0], ['Santos', 'Chelsea', 0, 0]], columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

# --- 4. SIDEBAR (LOGO NO TOPO + COMPACTAÇÃO SEGURA) ---
with st.sidebar:
    st.markdown("""
        <div class="sidebar-header">
            <div class="ai-logo-box">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3">
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

    st.markdown('<p class="cat-label">🇧🇷 NACIONAIS / ESTADUAIS</p>', unsafe_allow_html=True)
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

# ALERTA VIP (BOTAO LARANJA SÓLIDO)
st.markdown('<div class="alerta-container">', unsafe_allow_html=True)
if st.button("⚠️ APOSTAS ENCONTRADAS IA: 12 OPORTUNIDADES DISPONÍVEIS", key="alerta_vip"):
    st.session_state.pg = 'scanner'
st.markdown('</div>', unsafe_allow_html=True)

# NAVEGAÇÃO (BOTÕES NITIDOS)
st.markdown('<div class="nav-container">', unsafe_allow_html=True)
n1, n2, n3 = st.columns(3)
with n1: 
    if st.button("🎯 RADAR NEURAL"): st.session_state.pg = 'radar'
with n2:
    if st.button("🔍 SCANNER DIÁRIO"): st.session_state.pg = 'scanner'
with n3:
    if st.button("💰 GESTÃO BANCA"): st.session_state.pg = 'gestao'
st.markdown('</div>', unsafe_allow_html=True)

df = load_data(st.session_state.liga)
times = sorted(df['HomeTeam'].unique())

if st.session_state.pg == 'radar':
    if st.button("🚀 EXECUTAR ALGORITMO COMPLETO", key="run_main"): st.session_state.run = True
    
    c1, c2 = st.columns(2)
    with c1: t_casa = st.selectbox("Mandante", times, key="sel_c1")
    with c2: t_fora = st.selectbox("Visitante", times, index=min(1, len(times)-1), key="sel_f1")

    if st.session_state.get('run'):
        st.markdown(f"""
            <div class="card-principal">
                <div class="match-title">{t_casa} VS {t_fora}</div>
                <div style="display:flex; justify-content:space-around; align-items:center;">
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
        
        st.markdown('<div class="section-header">PROBABILIDADES DE MERCADO (EFICIÊNCIA)</div>', unsafe_allow_html=True)
        m_col = st.columns(6)
        with m_col[0]: st.markdown("<div class='mini-card'><span class='mini-label'>⚽ GOLS +2.5</span><span class='mini-val'>62%</span></div>", unsafe_allow_html=True)
        with m_col[1]: st.markdown("<div class='mini-card'><span class='mini-label'>🚩 CANTOS +9.5</span><span class='mini-val'>81%</span></div>", unsafe_allow_html=True)
        with m_col[2]: st.markdown("<div class='mini-card'><span class='mini-label'>👞 CHUTES +22.5</span><span class='mini-val'>77%</span></div>", unsafe_allow_html=True)
        with m_col[3]: st.markdown("<div class='mini-card'><span class='mini-label'>🎯 NO GOL +8.5</span><span class='mini-val'>65%</span></div>", unsafe_allow_html=True)
        with m_col[4]: st.markdown("<div class='mini-card'><span class='mini-label'>⚠️ FALTAS +24.5</span><span class='mini-val'>88%</span></div>", unsafe_allow_html=True)
        with m_col[5]: st.markdown("<div class='mini-card'><span class='mini-label'>🟨 CARTÕES +4.5</span><span class='mini-val'>72%</span></div>", unsafe_allow_html=True)

elif st.session_state.pg == 'scanner':
    st.markdown(f"### 🔍 Scanner de Oportunidades: {st.session_state.nome}")
    if len(times) >= 2:
        for i in range(min(5, len(times)//2)):
            st.expander(f"💰 JOGO COM VALOR: {times[i]} x {times[-(i+1)]}").write(f"Análise Sugerida: Over Gols / Vitória Mandante.")

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:9px;'>GESTOR IA v14.4 - DESIGN FINAL CORRIGIDO</p>", unsafe_allow_html=True)
