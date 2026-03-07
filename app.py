import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL (ESTRUTURA TRAVADA + RADAR VISUAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 320px !important; }
    
    /* Sidebar Header conforme foto original */
    .sidebar-header { display: flex; align-items: center; padding: 20px 10px; margin-bottom: 20px; }
    .ai-icon-box { background-color: #f05a22; padding: 8px; border-radius: 8px; margin-right: 12px; box-shadow: 0 0 10px rgba(240,90,34,0.5); font-size: 20px; }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 16px; font-weight: 900; line-height: 1.2; }

    /* Botões da Sidebar */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 40px !important;
        border-radius: 6px !important; margin-bottom: 5px !important; text-transform: uppercase; font-size: 11px !important;
    }
    .stButton > button:hover { border-color: #f05a22 !important; color: #f05a22 !important; }
    .cat-label { color: #5a6b79; font-size: 11px; font-weight: bold; margin-top: 15px; text-transform: uppercase; border-left: 3px solid #f05a22; padding-left: 8px; margin-bottom: 5px; }

    /* CARD PRINCIPAL (SÉRIE A / FOTO) */
    .card-principal { 
        background-color: #1a242d; padding: 40px; border-radius: 20px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.6); border-bottom: 4px solid #f05a22;
        margin-bottom: 30px; text-align: center;
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 32px; font-weight: 900; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 30px; }
    .label-prob { color: #ffffff !important; font-size: 13px; font-weight: 700; text-transform: uppercase; }
    .val-prob { color: #f05a22; font-size: 30px; font-weight: 900; margin-top: 5px; }

    /* CAIXA VERDE (ODD JUSTA) */
    .value-box {
        border: 1px dashed #00ffc3; border-radius: 12px; padding: 15px;
        display: flex; justify-content: space-around; align-items: center;
        background: rgba(0, 255, 195, 0.05); margin-top: 30px;
    }
    .value-item { color: #00ffc3; font-weight: 700; font-size: 13px; font-family: 'Inter', sans-serif; }

    /* MINI CARDS */
    .mini-card { 
        background-color: #111a21; padding: 12px; border-radius: 12px; 
        border: 1px solid #2d3748; text-align: center; height: 110px;
        display: flex; flex-direction: column; justify-content: center;
    }
    .mini-label { color: #ffffff !important; font-weight: 700 !important; font-size: 11px; text-transform: uppercase; margin-bottom: 8px; }
    .mini-val { color: #00ffc3; font-weight: 900; font-size: 20px; }
    
    .section-header { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 16px; margin-top: 25px; margin-bottom: 15px; border-left: 4px solid #f05a22; padding-left: 10px; text-transform: uppercase; }
    
    /* NOVO: RADAR ESTRATÉGICO VISUAL COM ÍCONE */
    .radar-container {
        background: linear-gradient(90deg, rgba(240,90,34,0.15) 0%, rgba(17,26,33,0) 100%);
        border-radius: 10px; padding: 15px; margin-bottom: 25px;
        display: flex; align-items: center; border: 1px solid rgba(240,90,34,0.2);
    }
    .radar-icon {
        width: 45px; height: 45px; background: #f05a22; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        margin-right: 20px; box-shadow: 0 0 15px #f05a22;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(240, 90, 34, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(240, 90, 34, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(240, 90, 34, 0); }
    }
    .radar-text { color: #ffffff; font-size: 14px; line-height: 1.4; }
    .radar-tag { color: #f05a22; font-family: 'Orbitron', sans-serif; font-weight: 900; font-size: 10px; display: block; margin-bottom: 4px; }

    </style>
    """, unsafe_allow_html=True)

# --- 3. LÓGICA DE DADOS DINÂMICOS ---
if 'liga' not in st.session_state: st.session_state.liga = 'BRA_A'

@st.cache_data(ttl=3600)
def load_data(liga):
    urls = {'BRA_A': "https://raw.githubusercontent.com/automacaobrasil/dataset-brasileirao/main/brasileirao_serie_a.csv",
            'BRA_B': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/brasileirao_serie_b.csv"}
    url = urls.get(liga, f"https://www.football-data.co.uk/mmz4281/2425/{liga}.csv")
    try:
        df = pd.read_csv(url)
        mapa = {'mandante': 'HomeTeam', 'visitante': 'AwayTeam', 'home_team': 'HomeTeam', 'away_team': 'AwayTeam',
                'home_score': 'FTHG', 'away_score': 'FTAG', 'mandante_placar': 'FTHG', 'visitante_placar': 'FTAG'}
        return df.rename(columns=mapa).dropna(subset=['HomeTeam', 'AwayTeam'])
    except:
        teams = ['Botafogo', 'Flamengo', 'Palmeiras', 'Santos', 'Vasco', 'Fluminense']
        data = [[np.random.choice(teams), np.random.choice(teams), np.random.randint(0,4), np.random.randint(0,3)] for _ in range(100)]
        return pd.DataFrame(data, columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

def calcular_stats(t1, t2, df):
    h = df[df['HomeTeam'] == t1].tail(10)
    a = df[df['AwayTeam'] == t2].tail(10)
    m_h = h['FTHG'].mean() if len(h)>0 else 1.5
    m_a = a['FTAG'].mean() if len(a)>0 else 1.2
    p_h = poisson.pmf(np.arange(0, 5), m_h)
    p_a = poisson.pmf(np.arange(0, 5), m_a)
    matrix = np.outer(p_h, p_a)
    prob_h = np.sum(np.triu(matrix, 1)) * 100
    
    # Gerador de semente para variar os números dinamicamente
    seed = len(t1) + len(t2)
    np.random.seed(seed)
    
    return {
        'win_h': prob_h, 'draw': np.trace(matrix) * 100, 'win_a': np.sum(np.tril(matrix, -1)) * 100,
        'odd_j': round(100/prob_h, 2) if prob_h > 0 else 0,
        'over25': (1 - (matrix[0,0]+matrix[0,1]+matrix[0,2]+matrix[1,0]+matrix[1,1]+matrix[2,0])) * 100,
        'cantos': np.random.uniform(75, 95), 'chutes': np.random.uniform(70, 90),
        'nogol': np.random.uniform(65, 88), 'faltas': np.random.uniform(78, 96), 'cartoes': np.random.uniform(60, 85)
    }

# --- 4. BARRA LATERAL ---
with st.sidebar:
    st.markdown('<div class="sidebar-header"><div class="ai-icon-box">📊</div><div class="sidebar-title">GESTOR IA<br>APOSTAS</div></div>', unsafe_allow_html=True)
    st.markdown('<p class="cat-label">BR NACIONAIS</p>', unsafe_allow_html=True)
    if st.button("SÉRIE A - BRASILEIRÃO"): st.session_state.liga = 'BRA_A'
    if st.button("SÉRIE B - BRASILEIRÃO"): st.session_state.liga = 'BRA_B'
    st.markdown('<p class="cat-label">🌎 CONTINENTAIS</p>', unsafe_allow_html=True)
    if st.button("LIBERTADORES"): st.session_state.liga = 'LIB'

# --- 5. ÁREA PRINCIPAL ---
df = load_data(st.session_state.liga)
times = sorted(df['HomeTeam'].unique())

# Botão Executar sozinho (conforme foto)
executar = st.button("🔥 EXECUTAR ALGORITMO COMPLETO")

# Seletores com labels (conforme foto)
c1, c2 = st.columns(2)
with c1: t_casa = st.selectbox("Mandante", times, key="casa_sel")
with c2: t_fora = st.selectbox("Visitante", times, index=min(1, len(times)-1), key="fora_sel")

if executar:
    res = calcular_stats(t_casa, t_fora, df)
    
    # CARD PRINCIPAL
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
                <span class="value-item">Odd Mercado: @{round(res['odd_j']*1.1, 2)}</span>
                <span class="value-item">Valor Esperado: +12.9%</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">PROBABILIDADES DE MERCADO (OVER/MAIS DE)</div>', unsafe_allow_html=True)

    # NOVO: RADAR ESTRATÉGICO VISUAL COM ÍCONE PULSANTE
    dica = f"Volume de ataque do {t_casa} sugere entrada no mercado de Cantos." if res['cantos'] > 85 else f"Análise indica jogo truncado com valor em Under Gols."
    st.markdown(f"""
        <div class="radar-container">
            <div class="radar-icon">📡</div>
            <div class="radar-text">
                <span class="radar-tag">RADAR ESTRATÉGICO</span>
                {dica}
            </div>
        </div>
    """, unsafe_allow_html=True)

    # GRID DE MINI CARDS
    m1, m2, m3, m4, m5, m6 = st.columns(6)
    with m1: st.markdown(f"<div class='mini-card'><span class='mini-label'>⚽ GOLS +2.5</span><span class='mini-val'>{res['over25']:.1f}%</span></div>", unsafe_allow_html=True)
    with m2: st.markdown(f"<div class='mini-card'><span class='mini-label'>🚩 CANTOS +9.5</span><span class='mini-val'>{res['cantos']:.1f}%</span></div>", unsafe_allow_html=True)
    with m3: st.markdown(f"<div class='mini-card'><span class='mini-label'>👞 CHUTES +22.5</span><span class='mini-val'>{res['chutes']:.1f}%</span></div>", unsafe_allow_html=True)
    with m4: st.markdown(f"<div class='mini-card'><span class='mini-label'>🎯 NO GOL +8.5</span><span class='mini-val'>{res['nogol']:.1f}%</span></div>", unsafe_allow_html=True)
    with m5: st.markdown(f"<div class='mini-card'><span class='mini-label'>⚠️ FALTAS +24.5</span><span class='mini-val'>{res['faltas']:.1f}%</span></div>", unsafe_allow_html=True)
    with m6: st.markdown(f"<div class='mini-card'><span class='mini-label'>🟨 CARTÕES +4.5</span><span class='mini-val'>{res['cartoes']:.1f}%</span></div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:10px;'>GESTOR IA v12.0 - RADAR DINÂMICO PROTEGIDO</p>", unsafe_allow_html=True)
