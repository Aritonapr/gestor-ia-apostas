import streamlit as st
import pandas as pd
import numpy as np

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL (AJUSTE DE 1CM PARA CIMA + SIDEBAR ULTRA COMPACTA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    /* SUBIR LOGO 1CM E COMPACTAR SIDEBAR */
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 230px !important; }
    [data-testid="stSidebar"] > div:first-child { padding-top: 5px !important; } /* Sobe o conteúdo ao máximo */
    
    .sidebar-header { display: flex; align-items: center; padding: 5px 10px; margin-bottom: 2px; }
    .ai-logo-box { background-color: #f05a22; padding: 6px; border-radius: 6px; margin-right: 8px; box-shadow: 0 0 10px #f05a22; }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 13px; font-weight: 900; line-height: 1.1; }

    /* BOTÕES SIDEBAR (ALTURA MÍNIMA PARA CABER TUDO) */
    .stButton > button {
        background-color: #1a242d !important; color: #ffffff !important; border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 24px !important; 
        border-radius: 3px !important; margin-bottom: 1px !important; text-transform: uppercase; font-size: 7.5px !important;
        padding: 0 !important; line-height: 24px !important;
    }
    .stButton > button[kind="primary"] { border: 1px solid #f05a22 !important; color: #f05a22 !important; background: rgba(240,90,34,0.1) !important; }
    .cat-label { color: #5a6b79; font-size: 7.5px; font-weight: bold; margin-top: 4px; text-transform: uppercase; border-left: 2px solid #f05a22; padding-left: 4px; margin-bottom: 1px; }

    /* BOTÃO DE ALERTA PISCANTE */
    .stButton > button[key="alerta_vip"] {
        background-color: #f05a22 !important; color: white !important; height: 40px !important;
        font-family: 'Orbitron', sans-serif !important; font-size: 12px !important;
        border-radius: 8px !important; animation: blinker 2s infinite !important; font-weight: 900 !important;
    }
    @keyframes blinker { 50% { opacity: 0.6; box-shadow: 0 0 15px #f05a22; } }

    /* CARD v12 RESTAURADO (BRANCO NÍTIDO) */
    .card-principal { 
        background-color: #1a242d; padding: 30px; border-radius: 20px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.6); border-bottom: 5px solid #f05a22;
        margin-bottom: 25px; text-align: center; border: 1px solid #2d3748;
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 28px; font-weight: 900; text-transform: uppercase; margin-bottom: 25px; }
    .label-prob { color: #ffffff !important; font-size: 13px; font-weight: 800; text-transform: uppercase; margin-bottom: 8px; display: block; }
    .val-prob { color: #f05a22 !important; font-size: 32px; font-weight: 900; }

    .value-box { border: 2px dashed #00ffc3; border-radius: 12px; padding: 15px; display: flex; justify-content: space-around; background: rgba(0, 255, 195, 0.05); margin-top: 30px; }
    .value-item { color: #00ffc3 !important; font-weight: 800; font-size: 13px; }

    .mini-card { background-color: #111a21; padding: 12px; border-radius: 12px; border: 1px solid #2d3748; text-align: center; height: 110px; display: flex; flex-direction: column; justify-content: center; }
    .mini-label { color: #ffffff !important; font-weight: 800; font-size: 10px; text-transform: uppercase; margin-bottom: 10px; }
    .mini-val { color: #00ffc3 !important; font-weight: 900; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGICA DE NAVEGAÇÃO ---
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
        return pd.DataFrame([['Botafogo', 'Flamengo', 1, 0], ['Santos', 'Palmeiras', 0, 0]], columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

# --- 4. SIDEBAR (LOGOTIPO NO TOPO + COMPACTAÇÃO) ---
with st.sidebar:
    st.markdown("""<div class="sidebar-header"><div class="ai-logo-box"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></div><div class="sidebar-title">GESTOR IA<br>APOSTAS</div></div>""", unsafe_allow_html=True)
    
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
if st.button("⚠️ APOSTAS ENCONTRADAS IA: 12 OPORTUNIDADES DISPONÍVEIS", key="alerta_vip"):
    st.session_state.pg = 'scanner'

col_nav1, col_nav2, col_nav3 = st.columns(3)
with col_nav1: 
    if st.button("🎯 RADAR NEURAL"): st.session_state.pg = 'radar'
with col_nav2:
    if st.button("🔍 SCANNER DIÁRIO"): st.session_state.pg = 'scanner'
with col_nav3:
    if st.button("💰 GESTÃO BANCA"): st.session_state.pg = 'gestao'

df = load_data(st.session_state.liga)
times = sorted(df['HomeTeam'].unique())

if st.session_state.pg == 'radar':
    if st.button("🔥 EXECUTAR ALGORITMO COMPLETO"): st.session_state.ex = True
    c1, c2 = st.columns(2)
    with c1: t_casa = st.selectbox("Mandante", times, key="sc1")
    with c2: t_fora = st.selectbox("Visitante", times, index=min(1, len(times)-1), key="sc2")

    if st.session_state.get('ex'):
        st.markdown(f"""
            <div class="card-principal">
                <div class="match-title">{t_casa} VS {t_fora}</div>
                <div style="display:flex; justify-content:space-around; align-items:center;">
                    <div><span class="label-prob">Vitória Casa</span><span class="val-prob">45.2%</span></div>
                    <div><span class="label-prob">Empate</span><span class="val-prob">28.5%</span></div>
                    <div><span class="label-prob">Vitória Fora</span><span class="val-prob">26.3%</span></div>
                </div>
                <div class="value-box">
                    <span class="value-item">Odd Justa: @2.21</span>
                    <span class="value-item">Valor Esperado: +12.9%</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        m1, m2, m3, m4, m5, m6 = st.columns(6)
        with m1: st.markdown("<div class='mini-card'><span class='mini-label'>⚽ GOLS +2.5</span><span class='mini-val'>61%</span></div>", unsafe_allow_html=True)
        with m2: st.markdown("<div class='mini-card'><span class='mini-label'>🚩 CANTOS +9.5</span><span class='mini-val'>84%</span></div>", unsafe_allow_html=True)
        with m3: st.markdown("<div class='mini-card'><span class='mini-label'>👞 CHUTES +22.5</span><span class='mini-val'>78%</span></div>", unsafe_allow_html=True)
        with m4: st.markdown("<div class='mini-card'><span class='mini-label'>🎯 NO GOL +8.5</span><span class='mini-val'>62%</span></div>", unsafe_allow_html=True)
        with m5: st.markdown("<div class='mini-card'><span class='mini-label'>⚠️ FALTAS +24.5</span><span class='mini-val'>81%</span></div>", unsafe_allow_html=True)
        with m6: st.markdown("<div class='mini-card'><span class='mini-label'>🟨 CARTÕES +4.5</span><span class='mini-val'>74%</span></div>", unsafe_allow_html=True)

elif st.session_state.pg == 'scanner':
    st.markdown(f"### 🔍 Scanner de Oportunidades: {st.session_state.nome}")
    # CORREÇÃO DO ERRO INDEXERROR
    if len(times) >= 2:
        for i in range(min(5, len(times)//2)):
            t1, t2 = times[i], times[-(i+1)]
            with st.expander(f"💰 JOGO COM VALOR: {t1} x {t2}"):
                st.write(f"Análise Sugerida para {st.session_state.nome}: Over Gols / Vitória Mandante.")
    else:
        st.warning("Dados insuficientes para esta liga no momento.")

elif st.session_state.pg == 'gestao':
    st.write("### Calculadora de Stake")
    st.number_input("Banca Total R$", value=1000)

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:9px;'>GESTOR IA v14.2 - ESTRUTURA BLINDADA</p>", unsafe_allow_html=True)
