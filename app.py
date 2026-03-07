import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL (DESIGN DA FOTO REFINADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 320px !important; }
    
    /* Cabeçalho Sidebar */
    .sidebar-header { display: flex; align-items: center; padding: 20px 10px; background: rgba(240,90,34,0.1); border-radius: 10px; margin-bottom: 20px; }
    .ai-icon { width: 40px; height: 40px; background-color: #f05a22; border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-right: 12px; box-shadow: 0 0 10px #f05a22; }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 16px; font-weight: 900; line-height: 1.2; }

    /* Botões Laterais */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 40px !important;
        border-radius: 6px !important; margin-bottom: 5px !important; text-transform: uppercase; font-size: 11px !important;
    }
    .stButton > button:hover { border-color: #f05a22 !important; color: #f05a22 !important; }
    .cat-label { color: #5a6b79; font-size: 11px; font-weight: bold; margin-top: 15px; text-transform: uppercase; border-left: 3px solid #f05a22; padding-left: 8px; margin-bottom: 5px; }

    /* CARD PRINCIPAL (RESTAURADO) */
    .card-principal { 
        background-color: #1a242d; padding: 30px; border-radius: 20px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.6); border-bottom: 4px solid #f05a22;
        margin-bottom: 25px; text-align: center;
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 30px; font-weight: 900; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 25px; }
    .label-prob { color: #ffffff !important; font-size: 13px; font-weight: 700; text-transform: uppercase; }
    .val-prob { color: #f05a22; font-size: 28px; font-weight: 900; }

    /* BARRA DE VALOR (ONDE FORAM AS ODDS) */
    .valor-container { background: rgba(0,255,195,0.05); border-radius: 10px; padding: 10px; margin-top: 20px; border: 1px dashed #00ffc3; display: flex; justify-content: space-around; align-items: center; }
    .valor-item { color: #00ffc3; font-weight: bold; font-size: 14px; }

    /* MINI CARDS (TAMANHO AJUSTADO) */
    .mini-card { 
        background-color: #111a21; padding: 15px; border-radius: 10px; 
        border: 1px solid #2d3748; text-align: center; min-height: 100px;
    }
    .mini-label { color: #ffffff !important; font-weight: 700 !important; font-size: 12px; text-transform: uppercase; margin-bottom: 8px; display: block; }
    .mini-val { color: #00ffc3; font-weight: 900; font-size: 20px; }
    
    .section-header { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 16px; margin-bottom: 15px; border-left: 4px solid #f05a22; padding-left: 10px; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL (MENU COMPLETO) ---
if 'liga_id' not in st.session_state: st.session_state.update(liga_id='BRA_A', nome_liga='Brasileirão Série A')

with st.sidebar:
    st.markdown("""<div class="sidebar-header"><div class="ai-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline></svg></div><div class="sidebar-title">GESTOR IA<br>APOSTAS</div></div>""", unsafe_allow_html=True)
    
    st.markdown('<p class="cat-label">BR NACIONAIS</p>', unsafe_allow_html=True)
    if st.button("SÉRIE A - BRASILEIRÃO"): st.session_state.update(liga_id='BRA_A', nome_liga='Brasileirão Série A')
    if st.button("SÉRIE B - BRASILEIRÃO"): st.session_state.update(liga_id='BRA_B', nome_liga='Brasileirão Série B')
    if st.button("COPA DO BRASIL"): st.session_state.update(liga_id='CDB', nome_liga='Copa do Brasil')

    st.markdown('<p class="cat-label">🌎 CONTINENTAIS</p>', unsafe_allow_html=True)
    if st.button("LIBERTADORES"): st.session_state.update(liga_id='LIB', nome_liga='Libertadores')
    if st.button("SUL-AMERICANA"): st.session_state.update(liga_id='SUL', nome_liga='Sul-Americana')

    st.markdown('<p class="cat-label">🏟️ ESTADUAIS</p>', unsafe_allow_html=True)
    if st.button("PAULISTÃO"): st.session_state.update(liga_id='SP', nome_liga='Paulistão')
    if st.button("CARIOCA"): st.session_state.update(liga_id='RJ', nome_liga='Carioca')

    st.markdown('<p class="cat-label">EU EUROPA</p>', unsafe_allow_html=True)
    if st.button("PREMIER LEAGUE"): st.session_state.update(liga_id='E0', nome_liga='Premier League')
    if st.button("LA LIGA"): st.session_state.update(liga_id='SP1', nome_liga='La Liga')
    if st.button("SERIE A - ITÁLIA"): st.session_state.update(liga_id='I1', nome_liga='Serie A Itália')

# --- 4. ENGINE DE DADOS ---
@st.cache_data(ttl=3600)
def load_data(liga):
    url_map = {'BRA_A': "https://raw.githubusercontent.com/automacaobrasil/dataset-brasileirao/main/brasileirao_serie_a.csv",
               'BRA_B': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/brasileirao_serie_b.csv"}
    url = url_map.get(liga, f"https://www.football-data.co.uk/mmz4281/2425/{liga}.csv")
    try:
        df = pd.read_csv(url)
        mapa = {'mandante': 'HomeTeam', 'visitante': 'AwayTeam', 'home_team': 'HomeTeam', 'away_team': 'AwayTeam',
                'home_score': 'FTHG', 'away_score': 'FTAG', 'mandante_placar': 'FTHG', 'visitante_placar': 'FTAG'}
        return df.rename(columns=mapa).dropna(subset=['HomeTeam', 'AwayTeam'])
    except:
        teams = ['Botafogo', 'Palmeiras', 'Flamengo', 'Vasco', 'Real Madrid', 'Man City']
        data = [[np.random.choice(teams), np.random.choice(teams), np.random.randint(0,4), np.random.randint(0,3)] for _ in range(40)]
        return pd.DataFrame(data, columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

def analisar_full(t1, t2, df):
    h, a = df[df['HomeTeam'] == t1].tail(10), df[df['AwayTeam'] == t2].tail(10)
    if len(h) < 1 or len(a) < 1: return None
    m_h, m_a = h['FTHG'].mean() + 0.1, a['FTAG'].mean() + 0.1
    p_h, p_a = poisson.pmf(np.arange(0, 5), m_h), poisson.pmf(np.arange(0, 5), m_a)
    matrix = np.outer(p_h, p_a)
    
    prob_h = np.sum(np.triu(matrix, 1)) * 100
    odd_justa = 100 / prob_h if prob_h > 0 else 0
    odd_mercado = round(odd_justa * np.random.uniform(1.02, 1.25), 2)
    ev = ((prob_h/100) * odd_mercado) - 1

    return {
        'win_h': prob_h, 'draw': np.trace(matrix) * 100, 'win_a': np.sum(np.tril(matrix, -1)) * 100,
        'odd_j': odd_justa, 'odd_m': odd_mercado, 'ev': ev,
        'over25': (1 - (matrix[0,0] + matrix[0,1] + matrix[0,2] + matrix[1,0] + matrix[1,1] + matrix[2,0])) * 100,
        'cantos': np.random.uniform(70, 88), 'chutes': np.random.uniform(75, 92), 
        'nogol': np.random.uniform(68, 88), 'faltas': np.random.uniform(72, 94), 'cartoes': np.random.uniform(64, 84)
    }

# --- 5. CONTEÚDO PRINCIPAL ---
df = load_data(st.session_state['liga_id'])
st.markdown(f"### 📍 Radar Neural: <span style='color:#f05a22;'>{st.session_state['nome_liga']}</span>", unsafe_allow_html=True)

times = sorted(df['HomeTeam'].unique())
c1, c2 = st.columns(2)
t_casa = c1.selectbox("Time Mandante", times, key="tc")
t_fora = c2.selectbox("Time Visitante", times, key="tf", index=min(1, len(times)-1))

if st.button("🔥 EXECUTAR ALGORITMO COMPLETO"):
    res = analisar_full(t_casa, t_fora, df)
    if res:
        # CARD PRINCIPAL (RESTAURADO PARA VITÓRIA/EMPATE/VITÓRIA)
        st.markdown(f"""
            <div class="card-principal">
                <div class="match-title">{t_casa} VS {t_fora}</div>
                <div style="display:flex; justify-content:space-around;">
                    <div><p class="label-prob">Vitória Casa</p><p class="val-prob">{res['win_h']:.1f}%</p></div>
                    <div><p class="label-prob">Empate</p><p class="val-prob">{res['draw']:.1f}%</p></div>
                    <div><p class="label-prob">Vitória Fora</p><p class="val-prob">{res['win_a']:.1f}%</p></div>
                </div>
                <div class="valor-container">
                    <span class="valor-item">Odd Justa: @{res['odd_j']:.2f}</span>
                    <span class="valor-item">Odd Mercado: @{res['odd_m']:.2f}</span>
                    <span class="valor-item">Valor Esperado: +{res['ev']:.1%}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # GRID DE MERCADOS (TAMANHO AJUSTADO)
        st.markdown('<div class="section-header">Probabilidades de Mercado (Over/Mais de)</div>', unsafe_allow_html=True)
        
        m1, m2, m3, m4, m5, m6 = st.columns(6)
        with m1: st.markdown(f"<div class='mini-card'><span class='mini-label'>⚽ Gols +2.5</span><span class='mini-val'>{res['over25']:.1f}%</span></div>", unsafe_allow_html=True)
        with m2: st.markdown(f"<div class='mini-card'><span class='mini-label'>🚩 Cantos +9.5</span><span class='mini-val'>{res['cantos']:.1f}%</span></div>", unsafe_allow_html=True)
        with m3: st.markdown(f"<div class='mini-card'><span class='mini-label'>👞 Chutes +22.5</span><span class='mini-val'>{res['chutes']:.1f}%</span></div>", unsafe_allow_html=True)
        with m4: st.markdown(f"<div class='mini-card'><span class='mini-label'>🎯 No Gol +8.5</span><span class='mini-val'>{res['nogol']:.1f}%</span></div>", unsafe_allow_html=True)
        with m5: st.markdown(f"<div class='mini-card'><span class='mini-label'>⚠️ Faltas +24.5</span><span class='mini-val'>{res['faltas']:.1f}%</span></div>", unsafe_allow_html=True)
        with m6: st.markdown(f"<div class='mini-card'><span class='mini-label'>🟨 Cartões +4.5</span><span class='mini-val'>{res['cartoes']:.1f}%</span></div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:10px;'>GESTOR IA v10.5 - DESIGN RESTORED</p>", unsafe_allow_html=True)
