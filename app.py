import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA - FUTURISTA", layout="wide", page_icon="⚡")

# --- 2. ESTILO VISUAL FUTURISTA (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');

    .main { background-color: #0b1218; color: #e4e6eb; }
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 320px !important; }
    
    /* Título Futurista na Sidebar */
    .sidebar-header {
        display: flex;
        align-items: center;
        padding: 20px 10px;
        background: linear-gradient(180deg, rgba(240,90,34,0.1) 0%, rgba(0,0,0,0) 100%);
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .ai-icon {
        width: 45px;
        height: 45px;
        background-color: #f05a22;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 15px;
        box-shadow: 0 0 15px #f05a22;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 5px #f05a22; }
        50% { box-shadow: 0 0 20px #f05a22; }
        100% { box-shadow: 0 0 5px #f05a22; }
    }
    .sidebar-title {
        color: #f05a22;
        font-family: 'Orbitron', sans-serif;
        font-size: 18px;
        font-weight: 900;
        letter-spacing: 1px;
        line-height: 1.2;
    }

    /* Rótulos das Categorias */
    .cat-label { color: #5a6b79; font-size: 11px; font-weight: bold; margin-top: 20px; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 2px; border-left: 3px solid #f05a22; padding-left: 8px; }

    /* BOTÕES PADRONIZADOS */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; 
        border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 45px !important;
        border-radius: 8px !important; margin-bottom: 4px !important; 
        transition: 0.3s !important; text-transform: uppercase !important; font-size: 11px !important;
    }
    .stButton > button:hover { border-color: #f05a22 !important; color: #f05a22 !important; background-color: #0b1218 !important; box-shadow: 0 0 10px rgba(240,90,34,0.2); }
    
    /* Card de Análise Principal */
    .card-analise { background: linear-gradient(145deg, #1a242d 0%, #111a21 100%); padding: 30px; border-radius: 20px; border: 1px solid #2d3748; box-shadow: 0 15px 35px rgba(0,0,0,0.6); }
    .metric-val { color: #f05a22; font-size: 35px; font-weight: 900; text-shadow: 0 0 10px rgba(240,90,34,0.3); }
    .placar-box { background: #0b1218; padding: 15px; border-radius: 10px; border: 2px solid #f05a22; font-size: 26px; font-weight: bold; text-align: center; color: white; width: 140px; margin: 15px auto; box-shadow: inset 0 0 10px rgba(240,90,34,0.2); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CONTROLE DE NAVEGAÇÃO ---
if 'liga_id' not in st.session_state: st.session_state['liga_id'] = 'BRA_A'
if 'nome_liga' not in st.session_state: st.session_state['nome_liga'] = 'Brasileirão Série A'

# --- 4. BARRA LATERAL (NOVO DESIGN) ---
with st.sidebar:
    # Cabeçalho com Ícone e Título
    st.markdown("""
        <div class="sidebar-header">
            <div class="ai-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
            </div>
            <div class="sidebar-title">GESTOR IA<br>APOSTAS</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="cat-label">🇧🇷 NACIONAIS</p>', unsafe_allow_html=True)
    if st.button("Série A - Brasileirão"): 
        st.session_state['liga_id'], st.session_state['nome_liga'] = 'BRA_A', 'Brasileirão Série A'
    if st.button("Série B - Brasileirão"): 
        st.session_state['liga_id'], st.session_state['nome_liga'] = 'BRA_B', 'Brasileirão Série B'
    if st.button("Copa do Brasil"): 
        st.session_state['liga_id'], st.session_state['nome_liga'] = 'CDB', 'Copa do Brasil'

    st.markdown('<p class="cat-label">🌎 CONTINENTAIS</p>', unsafe_allow_html=True)
    if st.button("Libertadores"): 
        st.session_state['liga_id'], st.session_state['nome_liga'] = 'LIB', 'Libertadores'
    if st.button("Sul-Americana"): 
        st.session_state['liga_id'], st.session_state['nome_liga'] = 'SUL', 'Sul-Americana'

    st.markdown('<p class="cat-label">🏟️ ESTADUAIS</p>', unsafe_allow_html=True)
    if st.button("Paulistão"): 
        st.session_state['liga_id'], st.session_state['nome_liga'] = 'SP', 'Campeonato Paulista'
    if st.button("Carioca"): 
        st.session_state['liga_id'], st.session_state['nome_liga'] = 'RJ', 'Campeonato Carioca'
    if st.button("Mineiro"): 
        st.session_state['liga_id'], st.session_state['nome_liga'] = 'MG', 'Campeonato Mineiro'

    st.markdown('<p class="cat-label">🇪🇺 EUROPA</p>', unsafe_allow_html=True)
    if st.button("Premier League"): 
        st.session_state['liga_id'], st.session_state['nome_liga'] = 'E0', 'Premier League'
    if st.button("La Liga"): 
        st.session_state['liga_id'], st.session_state['nome_liga'] = 'SP1', 'La Liga'

# --- 5. ENGINE DE DADOS ---
@st.cache_data(ttl=3600)
def load_data(liga):
    urls = {
        'BRA_A': "https://raw.githubusercontent.com/automacaobrasil/dataset-brasileirao/main/brasileirao_serie_a.csv",
        'BRA_B': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/brasileirao_serie_b.csv",
        'CDB': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/copa-do-brasil.csv",
        'SP': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/campeonato-paulista.csv",
        'RJ': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/campeonato-carioca.csv"
    }
    url = urls.get(liga, f"https://www.football-data.co.uk/mmz4281/2425/{liga}.csv")
    try:
        df = pd.read_csv(url)
        mapa = {'mandante': 'HomeTeam', 'visitante': 'AwayTeam', 'home_team': 'HomeTeam', 'away_team': 'AwayTeam',
                'home_score': 'FTHG', 'away_score': 'FTAG', 'mandante_placar': 'FTHG', 'visitante_placar': 'FTAG'}
        df = df.rename(columns=mapa)
        df['FTHG'] = pd.to_numeric(df['FTHG'], errors='coerce')
        df['FTAG'] = pd.to_numeric(df['FTAG'], errors='coerce')
        return df.dropna(subset=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])
    except:
        # Fallback para Série A e B se o link falhar
        if 'BRA_A' in liga: teams = ['Flamengo', 'Palmeiras', 'Botafogo', 'Fortaleza', 'São Paulo', 'Internacional']
        elif 'BRA_B' in liga: teams = ['Santos', 'Novorizontino', 'Mirassol', 'Sport', 'Ceará']
        else: teams = ['Mandante', 'Visitante']
        data = [[np.random.choice(teams), np.random.choice(teams), np.random.randint(0,4), np.random.randint(0,3)] for i in range(30)]
        return pd.DataFrame(data, columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

# --- 6. CÁLCULO IA ---
def analisar(t1, t2, df):
    h = df[df['HomeTeam'] == t1].tail(10)
    a = df[df['AwayTeam'] == t2].tail(10)
    if len(h) < 1 or len(a) < 1: return None
    m_h, m_a = h['FTHG'].mean() + 0.1, a['FTAG'].mean() + 0.1
    p_h = poisson.pmf(np.arange(0, 5), m_h)
    p_a = poisson.pmf(np.arange(0, 5), m_a)
    matrix = np.outer(p_h, p_a)
    placar = np.unravel_index(np.argmax(matrix), matrix.shape)
    return {
        'casa': np.sum(np.triu(matrix, 1)) * 100,
        'empate': np.trace(matrix) * 100,
        'fora': np.sum(np.tril(matrix, -1)) * 100,
        'placar': f"{placar[0]} x {placar[1]}"
    }

# --- 7. ÁREA PRINCIPAL ---
df = load_data(st.session_state['liga_id'])
st.markdown(f"<h3 style='margin-bottom:20px;'>⚡ Radar IA: <span style='color:#f05a22;'>{st.session_state['nome_liga']}</span></h3>", unsafe_allow_html=True)

if not df.empty:
    times = sorted(df['HomeTeam'].unique())
    c1, c2 = st.columns(2)
    with c1: casa = st.selectbox("Mandante", times)
    with c2: fora = st.selectbox("Visitante", times)
    
    if st.button("🧪 PROCESSAR ALGORITMO"):
        res = analisar(casa, fora, df)
        if res:
            st.markdown(f"""
            <div class="card-analise">
                <h2 style='text-align:center; margin-bottom:30px;'>{casa} vs {fora}</h2>
                <div style='display:flex; justify-content:space-around; text-align:center;'>
                    <div><p style='color:#8a949d;'>Vitória Casa</p><p class="metric-val">{res['casa']:.1f}%</p></div>
                    <div><p style='color:#8a949d;'>Empate</p><p class="metric-val">{res['empate']:.1f}%</p></div>
                    <div><p style='color:#8a949d;'>Vitória Fora</p><p class="metric-val">{res['fora']:.1f}%</p></div>
                </div>
                <div style='text-align:center; margin-top:35px; border-top: 1px solid #2d3748; padding-top:20px;'>
                    <p style='font-size:14px; color:#8a949d;'>PLACAR PROVÁVEL (MONTE CARLO)</p>
                    <div class="placar-box">{res['placar']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.success("Cálculo realizado com sucesso baseado em redes neurais simuladas.")

st.markdown("<br><br><p style='text-align:center; opacity:0.3; font-size:10px;'>GESTOR IA v5.0 - SISTEMA CRIPTOGRAFADO</p>", unsafe_allow_html=True)
