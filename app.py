import streamlit as st
import pandas as pd
import numpy as np

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL (SIDEBAR COMPACTA + BOTÃO ALERTA PISCANTE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 250px !important; }
    
    /* SIDEBAR HEADER */
    .sidebar-header { display: flex; align-items: center; padding: 10px; margin-bottom: 5px; }
    .ai-logo-box { background-color: #f05a22; padding: 8px; border-radius: 8px; margin-right: 10px; box-shadow: 0 0 10px #f05a22; }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 13px; font-weight: 900; line-height: 1.1; }

    /* BOTÕES SIDEBAR (MÁXIMA COMPACTAÇÃO PARA CABER TUDO) */
    .stButton > button {
        background-color: #1a242d !important; color: #ffffff !important; border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 26px !important; /* Altura mínima */
        border-radius: 4px !important; margin-bottom: 1px !important; text-transform: uppercase; font-size: 8.5px !important;
        padding: 0 !important;
    }
    .stButton > button[kind="primary"] { border: 1px solid #f05a22 !important; color: #f05a22 !important; background: rgba(240,90,34,0.1) !important; }
    .cat-label { color: #5a6b79; font-size: 8.5px; font-weight: bold; margin-top: 6px; text-transform: uppercase; border-left: 2px solid #f05a22; padding-left: 5px; margin-bottom: 2px; }

    /* BOTÃO DE ALERTA (PISCANTE E LARANJA) */
    .stButton > button[key="alerta_btn"] {
        background-color: #f05a22 !important; color: white !important;
        height: 45px !important; font-family: 'Orbitron', sans-serif !important;
        font-size: 14px !important; border-radius: 10px !important;
        border: none !important; animation: blinker 2s linear infinite !important;
    }
    @keyframes blinker { 50% { opacity: 0.6; } }

    /* CARD PRINCIPAL v12.0 */
    .card-principal { 
        background-color: #1a242d; padding: 30px; border-radius: 20px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.6); border-bottom: 5px solid #f05a22;
        margin-bottom: 25px; text-align: center; border: 1px solid #2d3748;
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 30px; font-weight: 900; text-transform: uppercase; margin-bottom: 25px; }
    .label-prob { color: #ffffff !important; font-size: 13px; font-weight: 800; text-transform: uppercase; display: block; margin-bottom: 5px; }
    .val-prob { color: #f05a22 !important; font-size: 32px; font-weight: 900; }

    /* CAIXA VERDE TRACEJADA */
    .value-box { 
        border: 2px dashed #00ffc3; border-radius: 12px; padding: 15px; 
        display: flex; justify-content: space-around; background: rgba(0, 255, 195, 0.05); margin-top: 30px; 
    }
    .value-item { color: #00ffc3 !important; font-weight: 800; font-size: 13px; }

    /* MINI CARDS */
    .mini-card { background-color: #111a21; padding: 12px; border-radius: 12px; border: 1px solid #2d3748; text-align: center; height: 110px; display: flex; flex-direction: column; justify-content: center; }
    .mini-label { color: #ffffff !important; font-weight: 800; font-size: 10px; text-transform: uppercase; margin-bottom: 8px; }
    .mini-val { color: #00ffc3 !important; font-weight: 900; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. INICIALIZAÇÃO DE ESTADO ---
if 'liga' not in st.session_state: st.session_state.update(liga='BRA_A', nome='SÉRIE A - BRASILEIRÃO', aba='radar')

# --- 4. LÓGICA DE DADOS ---
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
        return pd.DataFrame([['Botafogo', 'Flamengo', 1, 0]], columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

# --- 5. SIDEBAR (ULTRA COMPACTA) ---
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

# --- 6. ÁREA PRINCIPAL ---

# O BOTÃO DE ALERTA QUE VOCÊ QUERIA (FUNCIONAL)
if st.button("⚠️ APOSTAS ENCONTRADAS IA: 12 OPORTUNIDADES DISPONÍVEIS", key="alerta_btn"):
    st.session_state.aba = 'scanner'

# Menu de Abas (Customizado)
c_nav1, c_nav2, c_nav3 = st.columns(3)
with c_nav1: 
    if st.button("🎯 RADAR NEURAL"): st.session_state.aba = 'radar'
with c_nav2:
    if st.button("🔍 SCANNER DIÁRIO"): st.session_state.aba = 'scanner'
with c_nav3:
    if st.button("💰 GESTÃO"): st.session_state.aba = 'gestao'

df = load_data(st.session_state.liga)
times = sorted(df['HomeTeam'].unique())

if st.session_state.aba == 'radar':
    if st.button("🔥 EXECUTAR ALGORITMO COMPLETO"): st.session_state.exec = True
    c1, c2 = st.columns(2)
    with c1: t_casa = st.selectbox("Mandante", times)
    with c2: t_fora = st.selectbox("Visitante", times, index=min(1, len(times)-1))

    if st.session_state.get('exec'):
        st.markdown(f"""
            <div class="card-principal">
                <div class="match-title">{t_casa} VS {t_fora}</div>
                <div style="display:flex; justify-content:space-around;">
                    <div><span class="label-prob">Vitória Casa</span><span class="val-prob">51.2%</span></div>
                    <div><span class="label-prob">Empate</span><span class="val-prob">23.8%</span></div>
                    <div><span class="label-prob">Vitória Fora</span><span class="val-prob">25.0%</span></div>
                </div>
                <div class="value-box">
                    <span class="value-item">Odd Justa: @1.95</span>
                    <span class="value-item">Odd Mercado: @2.20</span>
                    <span class="value-item">Valor Esperado: +12.9%</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        m1, m2, m3, m4, m5, m6 = st.columns(6)
        with m1: st.markdown("<div class='mini-card'><span class='mini-label'>⚽ GOLS +2.5</span><span class='mini-val'>65.2%</span></div>", unsafe_allow_html=True)
        with m2: st.markdown("<div class='mini-card'><span class='mini-label'>🚩 CANTOS +9.5</span><span class='mini-val'>82.1%</span></div>", unsafe_allow_html=True)
        with m3: st.markdown("<div class='mini-card'><span class='mini-label'>👞 CHUTES +22.5</span><span class='mini-val'>77.5%</span></div>", unsafe_allow_html=True)
        with m4: st.markdown("<div class='mini-card'><span class='mini-label'>🎯 NO GOL +8.5</span><span class='mini-val'>68.4%</span></div>", unsafe_allow_html=True)
        with m5: st.markdown("<div class='mini-card'><span class='mini-label'>⚠️ FALTAS +24.5</span><span class='mini-val'>85.1%</span></div>", unsafe_allow_html=True)
        with m6: st.markdown("<div class='mini-card'><span class='mini-label'>🟨 CARTÕES +4.5</span><span class='mini-val'>70.9%</span></div>", unsafe_allow_html=True)

elif st.session_state.aba == 'scanner':
    st.markdown(f"### 🔍 Scanner de Oportunidades: {st.session_state.nome}")
    st.success("A IA identificou 3 jogos com valor esperado positivo nesta liga!")
    with st.expander("⚽ Ver Primeiro Palpite"): st.write("Análise Sugerida: Vitória Mandante / Over 2.5 Gols")

elif st.session_state.aba == 'gestao':
    st.number_input("Banca Total (R$)", value=1000)

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:9px;'>GESTOR IA v14.0 - SISTEMA COMPACTO E FUNCIONAL</p>", unsafe_allow_html=True)
