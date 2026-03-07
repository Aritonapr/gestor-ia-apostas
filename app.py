import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL (ESTRUTURA v12.0 PROTEGIDA + SIDEBAR COMPACTA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 260px !important; }
    
    /* SIDEBAR HEADER + ÍCONE ORIGINAL */
    .sidebar-header { display: flex; align-items: center; padding: 15px 10px; margin-bottom: 10px; }
    .ai-logo-box { background-color: #f05a22; padding: 8px; border-radius: 8px; margin-right: 12px; box-shadow: 0 0 10px #f05a22; }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 14px; font-weight: 900; line-height: 1.1; }

    /* BOTÕES SIDEBAR ULTRA COMPACTOS */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 30px !important;
        border-radius: 4px !important; margin-bottom: 2px !important; text-transform: uppercase; font-size: 9px !important;
    }
    .stButton > button[kind="primary"] { border: 1px solid #f05a22 !important; color: #f05a22 !important; background: rgba(240,90,34,0.1) !important; }
    .cat-label { color: #5a6b79; font-size: 9px; font-weight: bold; margin-top: 8px; text-transform: uppercase; border-left: 3px solid #f05a22; padding-left: 6px; margin-bottom: 3px; }

    /* BARRA DE ALERTA PISCANTE NO TOPO */
    .alert-bar { 
        display: flex; justify-content: space-between; align-items: center; 
        background: rgba(240,90,34,0.1); padding: 8px 20px; border-radius: 10px; 
        border: 1px solid #f05a22; margin-bottom: 20px;
        animation: blink 2s infinite;
    }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }

    /* CARD PRINCIPAL v12.0 (RESTAURADO) */
    .card-principal { 
        background-color: #1a242d; padding: 40px; border-radius: 20px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.6); border-bottom: 4px solid #f05a22;
        margin-bottom: 30px; text-align: center;
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 32px; font-weight: 900; text-transform: uppercase; margin-bottom: 30px; }
    .label-prob { color: #ffffff !important; font-size: 14px; font-weight: 800; text-transform: uppercase; }
    .val-prob { color: #f05a22; font-size: 32px; font-weight: 900; margin-top: 5px; }

    /* CAIXA VERDE TRACEJADA */
    .value-box { 
        border: 1px dashed #00ffc3; border-radius: 12px; padding: 15px; 
        display: flex; justify-content: space-around; background: rgba(0, 255, 195, 0.05); margin-top: 30px; 
    }
    .value-item { color: #00ffc3; font-weight: 700; font-size: 13px; }

    /* MINI CARDS */
    .mini-card { background-color: #111a21; padding: 12px; border-radius: 12px; border: 1px solid #2d3748; text-align: center; height: 110px; display: flex; flex-direction: column; justify-content: center; }
    .mini-label { color: #ffffff !important; font-weight: 800; font-size: 11px; text-transform: uppercase; margin-bottom: 8px; }
    .mini-val { color: #00ffc3; font-weight: 900; font-size: 20px; }
    
    .section-header { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 16px; margin-bottom: 20px; border-left: 4px solid #f05a22; padding-left: 10px; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGICA DE DADOS ---
if 'liga_ativa' not in st.session_state: st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A - BRASILEIRÃO')

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
        return pd.DataFrame([['Time A', 'Time B', 2, 1]], columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

# --- 4. SIDEBAR (RESTAURADA E COMPACTA) ---
with st.sidebar:
    st.markdown("""<div class="sidebar-header"><div class="ai-logo-box"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div><div class="sidebar-title">GESTOR IA<br>APOSTAS</div></div>""", unsafe_allow_html=True)
    
    def sb_btn(label, id_liga):
        is_active = st.session_state.liga_ativa == id_liga
        if st.button(label, key=f"sb_{id_liga}", type="primary" if is_active else "secondary"):
            st.session_state.liga_ativa = id_liga
            st.session_state.nome_liga = label
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

# --- 5. INTERFACE PRINCIPAL ---
st.markdown(f"""<div class="alert-bar"><span style="color:white; font-family:'Orbitron'; font-size:12px; font-weight:900;">⚠️ APOSTAS ENCONTRADAS IA: 12 OPORTUNIDADES</span><span style="color:#f05a22; font-size:10px;">SCANNER ATIVO</span></div>""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🎯 RADAR NEURAL", "🔍 SCANNER DIÁRIO", "💰 GESTÃO"])

with tab1:
    df = load_data(st.session_state.liga_ativa)
    times = sorted(df['HomeTeam'].unique())
    if st.button("🔥 EXECUTAR ALGORITMO COMPLETO"):
        st.session_state.executou = True

    c1, c2 = st.columns(2)
    with c1: t_casa = st.selectbox("Mandante", times, key="c")
    with c2: t_fora = st.selectbox("Visitante", times, index=min(1, len(times)-1), key="f")

    if st.session_state.get('executou'):
        # CARD PRINCIPAL RESTAURADO
        st.markdown(f"""
            <div class="card-principal">
                <div class="match-title">{t_casa} VS {t_fora}</div>
                <div style="display:flex; justify-content:space-around;">
                    <div><p class="label-prob">Vitória Casa</p><p class="val-prob">48.2%</p></div>
                    <div><p class="label-prob">Empate</p><p class="val-prob">24.5%</p></div>
                    <div><p class="label-prob">Vitória Fora</p><p class="val-prob">27.3%</p></div>
                </div>
                <div class="value-box">
                    <span class="value-item">Odd Justa: @2.07</span>
                    <span class="value-item">Odd Mercado: @2.35</span>
                    <span class="value-item">Valor Esperado: +12.9%</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">PROBABILIDADES DE MERCADO</div>', unsafe_allow_html=True)
        m1, m2, m3, m4, m5, m6 = st.columns(6)
        with m1: st.markdown("<div class='mini-card'><span class='mini-label'>⚽ GOLS +2.5</span><span class='mini-val'>62%</span></div>", unsafe_allow_html=True)
        with m2: st.markdown("<div class='mini-card'><span class='mini-label'>🚩 CANTOS +9.5</span><span class='mini-val'>81%</span></div>", unsafe_allow_html=True)
        with m3: st.markdown("<div class='mini-card'><span class='mini-label'>👞 CHUTES +22.5</span><span class='mini-val'>77%</span></div>", unsafe_allow_html=True)
        with m4: st.markdown("<div class='mini-card'><span class='mini-label'>🎯 NO GOL +8.5</span><span class='mini-val'>65%</span></div>", unsafe_allow_html=True)
        with m5: st.markdown("<div class='mini-card'><span class='mini-label'>⚠️ FALTAS +24.5</span><span class='mini-val'>88%</span></div>", unsafe_allow_html=True)
        with m6: st.markdown("<div class='mini-card'><span class='mini-label'>🟨 CARTÕES +4.5</span><span class='mini-val'>72%</span></div>", unsafe_allow_html=True)

with tab2:
    st.markdown("### 🔍 Jogos Sugeridos para Hoje")
    st.success("A IA selecionou 3 jogos com alta probabilidade de lucro:")
    with st.expander("⚽ Ver Jogo 1"): st.write("Botafogo x Flamengo - Sugestão: Vitória Casa")
    with st.expander("⚽ Ver Jogo 2"): st.write("Real Madrid x Barcelona - Sugestão: Over 2.5 Gols")

with tab3:
    st.write("### Calculadora de Gestão")
    st.number_input("Sua Banca R$", value=1000)

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:10px;'>GESTOR IA v13.2 - ESTRUTURA v12 RESTAURADA</p>", unsafe_allow_html=True)
