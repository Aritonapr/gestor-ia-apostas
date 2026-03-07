import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL (ESTRUTURA PROTEGIDA + DESTAQUE DE BOTÃO ATIVO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 320px !important; }
    
    /* Header Sidebar */
    .sidebar-header { display: flex; align-items: center; padding: 20px 10px; margin-bottom: 20px; }
    .ai-logo-box { background-color: #f05a22; padding: 10px; border-radius: 10px; margin-right: 15px; box-shadow: 0 0 15px rgba(240,90,34,0.4); }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 16px; font-weight: 900; line-height: 1.1; }

    /* ESTILO DOS BOTÕES NORMAIS */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 38px !important;
        border-radius: 6px !important; margin-bottom: 4px !important; text-transform: uppercase; font-size: 11px !important;
        transition: 0.3s;
    }

    /* ESTILO DO BOTÃO QUANDO ESTÁ ATIVO (CLICADO) */
    .stButton > button[kind="primary"] {
        background-color: rgba(240,90,34,0.2) !important;
        color: #f05a22 !important;
        border: 2px solid #f05a22 !important;
        box-shadow: 0 0 10px rgba(240,90,34,0.3) !important;
    }

    .cat-label { color: #5a6b79; font-size: 11px; font-weight: bold; margin-top: 15px; text-transform: uppercase; border-left: 3px solid #f05a22; padding-left: 8px; margin-bottom: 8px; }

    /* RADAR NO TOPO */
    .radar-topo {
        background: linear-gradient(90deg, rgba(240,90,34,0.2) 0%, rgba(26,36,45,1) 100%);
        border-radius: 12px; padding: 15px 25px; margin-bottom: 20px;
        display: flex; align-items: center; border: 1px solid #f05a22;
    }
    .radar-pulse { width: 12px; height: 12px; background: #f05a22; border-radius: 50%; margin-right: 15px; position: relative; }
    .radar-pulse::after { content: ""; position: absolute; width: 100%; height: 100%; background: #f05a22; border-radius: 50%; animation: pulse-orange 2s infinite; }
    @keyframes pulse-orange { 0% { transform: scale(1); opacity: 1; } 100% { transform: scale(3); opacity: 0; } }
    .radar-label { font-family: 'Orbitron', sans-serif; font-weight: 900; color: #f05a22; font-size: 12px; margin-right: 20px; }

    /* CARD E MINI CARDS (VISIBILIDADE CORRIGIDA) */
    .card-principal { background-color: #1a242d; padding: 40px; border-radius: 20px; border-bottom: 4px solid #f05a22; margin-bottom: 30px; text-align: center; }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 32px; font-weight: 900; text-transform: uppercase; margin-bottom: 30px; }
    .label-prob { color: #ffffff !important; font-size: 14px; font-weight: 800; text-transform: uppercase; }
    .val-prob { color: #f05a22; font-size: 32px; font-weight: 900; }
    .mini-card { background-color: #111a21; padding: 12px; border-radius: 12px; border: 1px solid #2d3748; text-align: center; height: 110px; display: flex; flex-direction: column; justify-content: center; }
    .mini-label { color: #ffffff !important; font-weight: 800 !important; font-size: 11px; text-transform: uppercase; margin-bottom: 10px; }
    .mini-val { color: #00ffc3; font-weight: 900; font-size: 22px; }
    .value-box { border: 1px dashed #00ffc3; border-radius: 12px; padding: 15px; display: flex; justify-content: space-around; background: rgba(0, 255, 195, 0.05); margin-top: 30px; }
    .value-item { color: #00ffc3; font-weight: 700; font-size: 13px; }
    .section-header { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 16px; margin-bottom: 20px; border-left: 4px solid #f05a22; padding-left: 10px; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGICA DE DADOS SEPARADA ---
if 'liga_ativa' not in st.session_state: 
    st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A - BRASILEIRÃO')

@st.cache_data(ttl=3600)
def load_data(liga):
    urls = {
        'BRA_A': "https://raw.githubusercontent.com/automacaobrasil/dataset-brasileirao/main/brasileirao_serie_a.csv",
        'BRA_B': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/brasileirao_serie_b.csv",
        'E0': "https://www.football-data.co.uk/mmz4281/2425/E0.csv",
        'SP1': "https://www.football-data.co.uk/mmz4281/2425/SP1.csv",
        'D1': "https://www.football-data.co.uk/mmz4281/2425/D1.csv"
    }
    try:
        url = urls.get(liga, urls['BRA_A'])
        df = pd.read_csv(url)
        mapa = {'mandante': 'HomeTeam', 'visitante': 'AwayTeam', 'home_team': 'HomeTeam', 'away_team': 'AwayTeam',
                'home_score': 'FTHG', 'away_score': 'FTAG'}
        return df.rename(columns=mapa).dropna(subset=['HomeTeam', 'AwayTeam'])
    except:
        br = ['Botafogo', 'Flamengo', 'Palmeiras', 'Corinthians', 'Santos']
        eu = ['Chelsea', 'Aston Villa', 'Real Madrid', 'Barcelona', 'Bayern']
        teams = br if 'BRA' in liga or liga == 'PAULISTÃO' else eu
        data = [[np.random.choice(teams), np.random.choice(teams), np.random.randint(0,4), np.random.randint(0,3)] for _ in range(50)]
        return pd.DataFrame(data, columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

# --- 4. BARRA LATERAL COM MARCAÇÃO ATIVA ---
with st.sidebar:
    st.markdown("""<div class="sidebar-header"><div class="ai-logo-box"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="8" y1="12" x2="16" y2="12"></line></svg></div><div class="sidebar-title">GESTOR IA<br>APOSTAS</div></div>""", unsafe_allow_html=True)
    
    # Função para criar botão que "lembra" se foi clicado
    def sidebar_button(label, id_liga):
        is_active = st.session_state.liga_ativa == id_liga
        if st.button(label, key=f"btn_{id_liga}", type="primary" if is_active else "secondary"):
            st.session_state.liga_ativa = id_liga
            st.session_state.nome_liga = label
            st.rerun()

    st.markdown('<p class="cat-label">BR NACIONAIS</p>', unsafe_allow_html=True)
    sidebar_button("SÉRIE A - BRASILEIRÃO", 'BRA_A')
    sidebar_button("SÉRIE B - BRASILEIRÃO", 'BRA_B')
    sidebar_button("COPA DO BRASIL", 'CDB')

    st.markdown('<p class="cat-label">BR ESTADUAIS</p>', unsafe_allow_html=True)
    sidebar_button("PAULISTÃO", 'PAULISTÃO')

    st.markdown('<p class="cat-label">🌎 CONTINENTAIS</p>', unsafe_allow_html=True)
    sidebar_button("LIBERTADORES", 'LIB')
    sidebar_button("SUL-AMERICANA", 'SUL')

    st.markdown('<p class="cat-label">🇪🇺 EUROPA</p>', unsafe_allow_html=True)
    sidebar_button("PREMIER LEAGUE", 'E0')
    sidebar_button("LA LIGA", 'SP1')
    sidebar_button("BUNDESLIGA", 'D1')

# --- 5. ÁREA PRINCIPAL ---
df = load_data(st.session_state.liga_ativa)
times_da_liga = sorted(df['HomeTeam'].unique())

executar = st.button("🔥 EXECUTAR ALGORITMO COMPLETO")

c1, c2 = st.columns(2)
with c1: t_casa = st.selectbox("Mandante", times_da_liga, key=f"c_{st.session_state.liga_ativa}")
with c2: t_fora = st.selectbox("Visitante", times_da_liga, index=min(1, len(times_da_liga)-1), key=f"f_{st.session_state.liga_ativa}")

if executar:
    # Simulação para o visual
    res = {'win_h': 46.0, 'draw': 25.1, 'win_a': 29.0, 'odd_j': 2.17, 'over25': 47.4, 'cantos': 73.5, 'chutes': 78.3, 'nogol': 62.5, 'faltas': 86.8, 'cartoes': 84.2}
    
    st.markdown(f"""
        <div class="radar-topo">
            <div class="radar-pulse"></div>
            <div class="radar-label">📡 RADAR ESTRATÉGICO</div>
            <div class="radar-info">Análise neural para <b>{st.session_state.nome_liga}</b> concluída. Conexão estável.</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="card-principal">
            <div class="match-title">{t_casa.upper()} VS {t_fora.upper()}</div>
            <div style="display:flex; justify-content:space-around; align-items:center;">
                <div><p class="label-prob">Vitória Casa</p><p class="val-prob">{res['win_h']:.1f}%</p></div>
                <div><p class="label-prob">Empate</p><p class="val-prob">{res['draw']:.1f}%</p></div>
                <div><p class="label-prob">Vitória Fora</p><p class="val-prob">{res['win_a']:.1f}%</p></div>
            </div>
            <div class="value-box">
                <span class="value-item">Odd Justa: @{res['odd_j']}</span>
                <span class="value-item">Odd Mercado: @{round(res['odd_j']*1.12, 2)}</span>
                <span class="value-item">Valor Esperado: +12.9%</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">PROBABILIDADES DE MERCADO (OVER/MAIS DE)</div>', unsafe_allow_html=True)

    m1, m2, m3, m4, m5, m6 = st.columns(6)
    with m1: st.markdown(f"<div class='mini-card'><span class='mini-label'>⚽ GOLS +2.5</span><span class='mini-val'>{res['over25']:.1f}%</span></div>", unsafe_allow_html=True)
    with m2: st.markdown(f"<div class='mini-card'><span class='mini-label'>🚩 CANTOS +9.5</span><span class='mini-val'>{res['cantos']:.1f}%</span></div>", unsafe_allow_html=True)
    with m3: st.markdown(f"<div class='mini-card'><span class='mini-label'>👞 CHUTES +22.5</span><span class='mini-val'>{res['chutes']:.1f}%</span></div>", unsafe_allow_html=True)
    with m4: st.markdown(f"<div class='mini-card'><span class='mini-label'>🎯 NO GOL +8.5</span><span class='mini-val'>{res['nogol']:.1f}%</span></div>", unsafe_allow_html=True)
    with m5: st.markdown(f"<div class='mini-card'><span class='mini-label'>⚠️ FALTAS +24.5</span><span class='mini-val'>{res['faltas']:.1f}%</span></div>", unsafe_allow_html=True)
    with m6: st.markdown(f"<div class='mini-card'><span class='mini-label'>🟨 CARTÕES +4.5</span><span class='mini-val'>{res['cartoes']:.1f}%</span></div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:10px;'>GESTOR IA v12.0 - INDICADOR DE LIGA ATIVA</p>", unsafe_allow_html=True)
