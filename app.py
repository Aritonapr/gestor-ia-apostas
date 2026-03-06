import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA - ELITE", layout="wide", page_icon="⚽")

# --- ESTILO VISUAL BETANO DARK ---
st.markdown("""
    <style>
    .main { background-color: #0b1218; color: #e4e6eb; }
    div[data-testid="stSidebar"] { background-color: #1a242d; }
    .stButton>button { background: linear-gradient(90deg, #f05a22 0%, #ff8235 100%); color: white; border: none; padding: 12px 30px; border-radius: 25px; font-weight: bold; width: 100%; transition: 0.3s; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 4px 15px rgba(240,90,34,0.4); }
    .card-jogo { background-color: #1a242d; padding: 25px; border-radius: 15px; border-top: 4px solid #f05a22; margin-bottom: 20px; box-shadow: 0 8px 16px rgba(0,0,0,0.4); }
    .label-valor { background-color: #28a745; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; }
    .metric-title { color: #8a949d; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }
    .metric-value { color: #f05a22; font-size: 24px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- ENGINE DE DADOS ---
@st.cache_data(ttl=3600)
def get_data(league_code):
    url = f"https://www.football-data.co.uk/mmz4281/2425/{league_code}.csv"
    try:
        df = pd.read_csv(url)
        return df
    except:
        return pd.DataFrame()

def calcular_probabilidades(home, away, df):
    h_matches = df[df['HomeTeam'] == home]
    a_matches = df[df['AwayTeam'] == away]
    
    if len(h_matches) == 0 or len(a_matches) == 0: return None
    
    # Médias avançadas
    xg_h = h_matches['FTHG'].mean()
    xg_a = a_matches['FTAG'].mean()
    chutes_h = h_matches['HS'].mean() if 'HS' in h_matches else 0
    chutes_a = a_matches['AS'].mean() if 'AS' in a_matches else 0
    corners_h = h_matches['HC'].mean() if 'HC' in h_matches else 0
    corners_a = a_matches['AC'].mean() if 'AC' in a_matches else 0
    cartoes = (h_matches['HY'].mean() if 'HY' in h_matches else 0) + (a_matches['AY'].mean() if 'AY' in a_matches else 0)
    
    # Poisson para Probabilidades
    prob_h_list = poisson.pmf(np.arange(0, 5), xg_h)
    prob_a_list = poisson.pmf(np.arange(0, 5), xg_a)
    matrix = np.outer(prob_h_list, prob_a_list)
    
    win_h = np.sum(np.triu(matrix, 1)) * 100
    draw = np.trace(matrix) * 100
    win_a = np.sum(np.tril(matrix, -1)) * 100
    over25 = (1 - (matrix[0,0] + matrix[0,1] + matrix[0,2] + matrix[1,0] + matrix[1,1] + matrix[2,0])) * 100
    
    return {
        'win_h': win_h, 'draw': draw, 'win_a': win_a, 'over25': over25,
        'corners': corners_h + corners_a, 'chutes': chutes_h + chutes_a,
        'cartoes': cartoes, 'xg_h': xg_h, 'xg_a': xg_a,
        'odd_justa_h': 100/win_h if win_h > 0 else 0
    }

# --- SIDEBAR E FILTROS ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Betano_logo.svg/1200px-Betano_logo.svg.png", width=180)
st.sidebar.markdown("---")
liga_nome = st.sidebar.selectbox("🏆 SELECIONE A LIGA", 
    ['Premier League', 'La Liga', 'Serie A', 'Bundesliga', 'Ligue 1'])
ligas_map = {'Premier League':'E0', 'La Liga':'SP1', 'Serie A':'I1', 'Bundesliga':'D1', 'Ligue 1':'F1'}

# --- CARREGAMENTO ---
df = get_data(ligas_map[liga_nome])

if not df.empty:
    tab1, tab2, tab3 = st.tabs(["🎯 ANALISADOR", "🔍 SCANNER DE VALOR", "📋 RELATÓRIO"])

    with tab1:
        col_t1, col_t2 = st.columns(2)
        teams = sorted(df['HomeTeam'].unique())
        t_home = col_t1.selectbox("Casa", teams, index=0)
        t_away = col_t2.selectbox("Fora", teams, index=1)
        
        if st.button("GERAR ANÁLISE COMPLETA"):
            res = calcular_probabilidades(t_home, t_away, df)
            if res:
                st.markdown(f"""
                <div class="card-jogo">
                    <div style="display: flex; justify-con
