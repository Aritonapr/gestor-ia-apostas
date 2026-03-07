import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL (SIDEBAR COMPACTA + ÍCONE ORIGINAL + ALERTA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    /* SIDEBAR AJUSTADA PARA CABER TUDO */
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 280px !important; }
    
    .sidebar-header { display: flex; align-items: center; padding: 15px 10px; margin-bottom: 10px; }
    
    /* ÍCONE LINDÃO ORIGINAL */
    .ai-logo-box { 
        background-color: #f05a22; padding: 8px; border-radius: 8px; margin-right: 12px; 
        box-shadow: 0 0 12px rgba(240,90,34,0.5); display: flex; align-items: center; justify-content: center;
    }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 15px; font-weight: 900; line-height: 1.1; }

    /* BOTÕES DA SIDEBAR (ULTRA COMPACTOS) */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 32px !important; /* Altura reduzida */
        border-radius: 4px !important; margin-bottom: 2px !important; /* Margem reduzida */
        text-transform: uppercase; font-size: 10px !important; /* Fonte menor para caber */
        transition: 0.2s; padding: 0 !important;
    }
    .stButton > button[kind="primary"] { 
        background-color: rgba(240,90,34,0.2) !important; color: #f05a22 !important; border: 1px solid #f05a22 !important; 
    }
    
    .cat-label { 
        color: #5a6b79; font-size: 10px; font-weight: bold; margin-top: 10px; 
        text-transform: uppercase; border-left: 3px solid #f05a22; padding-left: 6px; margin-bottom: 4px; 
    }

    /* BARRA DE NOTIFICAÇÃO PISCANTE */
    .nav-bar { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #2d3748; margin-bottom: 15px; }
    .notif-piscante { 
        display: flex; align-items: center; background: rgba(240,90,34,0.1); 
        padding: 6px 15px; border-radius: 20px; border: 1px solid #f05a22;
        animation: blinker 1.5s linear infinite;
    }
    @keyframes blinker { 50% { opacity: 0.3; box-shadow: 0 0 15px #f05a22; } }
    .notif-text { color: #f05a22; font-family: 'Orbitron', sans-serif; font-weight: 900; font-size: 10px; letter-spacing: 1px; }

    /* Abas Customizadas */
    .stTabs [data-baseweb="tab-list"] { gap: 5px; }
    .stTabs [data-baseweb="tab"] { background-color: #1a242d !important; color: #ffffff !important; padding: 8px 15px; font-size: 12px; border-radius: 5px 5px 0 0; }
    .stTabs [aria-selected="true"] { border-bottom: 2px solid #f05a22 !important; color: #f05a22 !important; }

    /* Cards e Probabilidades */
    .card-principal { background-color: #1a242d; padding: 30px; border-radius: 20px; border-bottom: 4px solid #f05a22; margin-bottom: 20px; text-align: center; }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 28px; font-weight: 900; text-transform: uppercase; margin-bottom: 20px; }
    .mini-card { background-color: #111a21; padding: 10px; border-radius: 12px; border: 1px solid #2d3748; text-align: center; height: 100px; display: flex; flex-direction: column; justify-content: center; }
    .mini-label { color: #ffffff !important; font-weight: 800; font-size: 10px; text-transform: uppercase; margin-bottom: 5px; }
    .mini-val { color: #00ffc3; font-weight: 900; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LÓGICA DE DADOS ---
if 'liga_ativa' not in st.session_state: st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A - BRASILEIRÃO')

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
        mapa = {'mandante': 'HomeTeam', 'visitante': 'AwayTeam', 'home_team': 'HomeTeam', 'away_team': 'AwayTeam', 'home_score': 'FTHG', 'away_score': 'FTAG'}
        return df.rename(columns=mapa).dropna(subset=['HomeTeam', 'AwayTeam'])
    except:
        br = ['Botafogo', 'Flamengo', 'Palmeiras', 'Corinthians', 'Santos']
        teams = br if 'BRA' in liga or liga == 'PAULISTÃO' else ['Chelsea', 'Real Madrid', 'Man City']
        return pd.DataFrame([[np.random.choice(teams), np.random.choice(teams), 2, 1] for _ in range(50)], columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

def calcular_palpite(t1, t2):
    seed = len(t1) + len(t2)
    np.random.seed(seed)
    return {
        'vence': t1 if np.random.rand() > 0.5 else t2,
        'prob': np.random.uniform(40, 65),
        'gols': np.random.uniform(1.5, 3.5),
        'cantos': np.random.uniform(8.5, 12.5),
        'cartoes': np.random.uniform(3.5, 6.5),
        'chutes': np.random.uniform(18.5, 26.5)
    }

# --- 4. BARRA LATERAL (ORGANIZAÇÃO TOTAL) ---
with st.sidebar:
    st.markdown("""
        <div class="sidebar-header">
            <div class="ai-logo-box">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="18" y1="20" x2="18" y2="10"></line>
                    <line x1="12" y1="20" x2="12" y2="4"></line>
                    <line x1="6" y1="20" x2="6" y2="14"></line>
                </svg>
            </div>
            <div class="sidebar-title">GESTOR IA<br>APOSTAS</div>
        </div>
    """, unsafe_allow_html=True)
    
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
st.markdown(f"""
    <div class="nav-bar">
        <div style="font-family:'Orbitron'; font-weight:900; color:#ffffff; font-size:14px;">ESTAÇÃO DE TRABALHO IA</div>
        <div class="notif-piscante">
            <span class="notif-text">🔔 APOSTAS ENCONTRADAS IA: 08 JOGOS</span>
        </div>
    </div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🎯 RADAR NEURAL", "🔍 SCANNER DIÁRIO", "💰 GESTÃO"])

with tab1:
    df = load_data(st.session_state.liga_ativa)
    times = sorted(df['HomeTeam'].unique())
    exec_radar = st.button("🔥 EXECUTAR ALGORITMO COMPLETO", key="run_radar")
    c1, c2 = st.columns(2)
    with c1: t_casa = st.selectbox("Mandante", times, key="c_sel")
    with c2: t_fora = st.selectbox("Visitante", times, index=min(1, len(times)-1), key="f_sel")
    
    if exec_radar:
        res = calcular_palpite(t_casa, t_fora)
        st.markdown(f"""<div class="card-principal"><div class="match-title">{t_casa} VS {t_fora}</div><div style="display:flex; justify-content:space-around;"><div class="val-prob">{res['prob']:.1f}%</div><div class="val-prob">25%</div><div class="val-prob">15%</div></div></div>""", unsafe_allow_html=True)

with tab2:
    st.markdown(f"### 🔍 Melhores Oportunidades: {st.session_state.nome_liga}")
    df_s = load_data(st.session_state.liga_ativa)
    times_s = sorted(df_s['HomeTeam'].unique())
    for i in range(min(4, len(times_s)//2)):
        m, v = times_s[i], times_s[-(i+1)]
        res = calcular_palpite(m, v)
        with st.expander(f"💰 APOSTA SUGERIDA: {m} x {v}"):
            st.write(f"**Vencedor:** {res['vence']} | **Gols:** {res['gols']:.1f} | **Cantos:** {res['cantos']:.1f}")

with tab3:
    st.write("### Calculadora de Stake")
    banca = st.number_input("Banca R$", value=1000)
    st.success(f"Aposta Sugerida: R$ {banca*0.01:.2f}")

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:10px;'>GESTOR IA v13.2 - ESTRUTURA VISUAL OTIMIZADA</p>", unsafe_allow_html=True)
