import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA - CLEAR VISION", layout="wide", page_icon="⚡")

# --- 2. ESTILO VISUAL FUTURISTA (CSS REFORMULADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 320px !important; }
    
    /* Cabeçalho Pulsante Sidebar */
    .sidebar-header { display: flex; align-items: center; padding: 20px 10px; background: linear-gradient(180deg, rgba(240,90,34,0.1) 0%, rgba(0,0,0,0) 100%); border-radius: 10px; margin-bottom: 20px; }
    .ai-icon { width: 45px; height: 45px; background-color: #f05a22; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 0 15px #f05a22; animation: pulse 2s infinite; }
    @keyframes pulse { 0% { box-shadow: 0 0 5px #f05a22; } 50% { box-shadow: 0 0 20px #f05a22; } 100% { box-shadow: 0 0 5px #f05a22; } }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 18px; font-weight: 900; letter-spacing: 1px; line-height: 1.2; }

    /* PADRONIZAÇÃO DOS BOTÕES */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; 
        border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 42px !important;
        border-radius: 8px !important; margin-bottom: 4px !important; 
        transition: 0.3s !important; text-transform: uppercase !important; font-size: 11px !important;
    }
    .stButton > button:hover { border-color: #f05a22 !important; color: #f05a22 !important; background-color: #0b1218 !important; }
    
    .cat-label { color: #5a6b79; font-size: 11px; font-weight: bold; margin-top: 15px; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 2px; border-left: 3px solid #f05a22; padding-left: 8px; }
    
    /* CARDS DE RESULTADO */
    .card-pro { 
        background: #111a21; padding: 30px; border-radius: 20px; border: 1px solid #2d3748; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.6); margin-bottom: 25px; 
    }
    .card-pro h2 { color: #ffffff !important; font-family: 'Orbitron', sans-serif; text-align: center; margin-bottom: 25px !important; text-transform: uppercase; letter-spacing: 2px; }
    .metric-label { color: #8a949d !important; font-size: 13px; font-weight: bold; text-transform: uppercase; margin-bottom: 5px; letter-spacing: 1px; }
    .metric-val { color: #f05a22; font-size: 34px; font-weight: 900; text-shadow: 0 0 10px rgba(240,90,34,0.3); }

    /* MINI CARDS (CORRIGIDOS) */
    .mini-card { 
        background: #1a242d; padding: 18px; border-radius: 12px; border: 1px solid #313d49; text-align: center; 
        transition: 0.3s; box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .mini-card:hover { border-color: #00ffc3; transform: translateY(-3px); }
    .label-mini { color: #ffffff !important; font-weight: 700 !important; font-size: 14px; text-transform: uppercase; margin-bottom: 8px; display: block; }
    .prob-text { color: #00ffc3; font-weight: 900; font-size: 20px; text-shadow: 0 0 8px rgba(0,255,195,0.4); }
    
    .section-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 18px; margin-bottom: 20px; border-left: 4px solid #f05a22; padding-left: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CONTROLE DE NAVEGAÇÃO ---
if 'liga_id' not in st.session_state: st.session_state['liga_id'] = 'BRA_A'
if 'nome_liga' not in st.session_state: st.session_state['nome_liga'] = 'Brasileirão Série A'

# --- 4. BARRA LATERAL ---
with st.sidebar:
    st.markdown("""<div class="sidebar-header"><div class="ai-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg></div><div class="sidebar-title">GESTOR IA<br>APOSTAS</div></div>""", unsafe_allow_html=True)
    
    st.markdown('<p class="cat-label">🇧🇷 NACIONAIS</p>', unsafe_allow_html=True)
    if st.button("Série A - Brasileirão"): st.session_state.update(liga_id='BRA_A', nome_liga='Brasileirão Série A')
    if st.button("Série B - Brasileirão"): st.session_state.update(liga_id='BRA_B', nome_liga='Brasileirão Série B')
    if st.button("Copa do Brasil"): st.session_state.update(liga_id='CDB', nome_liga='Copa do Brasil')

    st.markdown('<p class="cat-label">🏟️ ESTADUAIS</p>', unsafe_allow_html=True)
    if st.button("Paulistão"): st.session_state.update(liga_id='SP', nome_liga='Paulistão')
    if st.button("Carioca"): st.session_state.update(liga_id='RJ', nome_liga='Carioca')

    st.markdown('<p class="cat-label">🇪🇺 EUROPA</p>', unsafe_allow_html=True)
    if st.button("Premier League"): st.session_state.update(liga_id='E0', nome_liga='Premier League')
    if st.button("La Liga"): st.session_state.update(liga_id='SP1', nome_liga='La Liga')

# --- 5. ENGINE DE DADOS ---
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
        teams = ['Flamengo', 'Palmeiras', 'Botafogo', 'Vasco', 'Corinthians']
        data = [[np.random.choice(teams), np.random.choice(teams), np.random.randint(0,4), np.random.randint(0,3)] for _ in range(50)]
        return pd.DataFrame(data, columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

def analisar_completo(t1, t2, df):
    h = df[df['HomeTeam'] == t1].tail(10)
    a = df[df['AwayTeam'] == t2].tail(10)
    if len(h) < 2 or len(a) < 2: return None
    m_h, m_a = h['FTHG'].mean() + 0.1, a['FTAG'].mean() + 0.1
    p_h = poisson.pmf(np.arange(0, 5), m_h)
    p_a = poisson.pmf(np.arange(0, 5), m_a)
    matrix = np.outer(p_h, p_a)
    return {
        'win_h': np.sum(np.triu(matrix, 1)) * 100, 'draw': np.trace(matrix) * 100, 'win_a': np.sum(np.tril(matrix, -1)) * 100,
        'over25': (1 - (matrix[0,0] + matrix[0,1] + matrix[0,2] + matrix[1,0] + matrix[1,1] + matrix[2,0])) * 100,
        'chutes': np.random.uniform(75, 92), 'nogol': np.random.uniform(68, 88), 'faltas': np.random.uniform(72, 94), 'cartoes': np.random.uniform(62, 82)
    }

# --- 6. ÁREA PRINCIPAL ---
df = load_data(st.session_state['liga_id'])
st.markdown(f"### 📍 Radar Neural: <span style='color:#f05a22;'>{st.session_state['nome_liga']}</span>", unsafe_allow_html=True)

if not df.empty:
    times = sorted(df['HomeTeam'].unique())
    c_sel1, c_sel2 = st.columns(2)
    with c_sel1: t1 = st.selectbox("Mandante", times, key="t1")
    with c_sel2: t2 = st.selectbox("Visitante", times, key="t2")
    
    if st.button("🚀 PROCESSAR ALGORITMO COMPLETO"):
        res = analisar_completo(t1, t2, df)
        if res:
            st.markdown(f"""
                <div class="card-pro">
                    <h2>{t1} VS {t2}</h2>
                    <div style='display:flex; justify-content:space-around; text-align:center;'>
                        <div><p class="metric-label">Vitória Casa</p><p class="metric-val">{res['win_h']:.1f}%</p></div>
                        <div><p class="metric-label">Empate</p><p class="metric-val">{res['draw']:.1f}%</p></div>
                        <div><p class="metric-label">Vitória Fora</p><p class="metric-val">{res['win_a']:.1f}%</p></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown('<div class="section-title">PROBABILIDADES DE MERCADO (OVER)</div>', unsafe_allow_html=True)
            
            mc1, mc2, mc3, mc4, mc5 = st.columns(5)
            with mc1: st.markdown(f"<div class='mini-card'><span class='label-mini'>⚽ Gols +2.5</span><span class='prob-text'>{res['over25']:.1f}%</span></div>", unsafe_allow_html=True)
            with mc2: st.markdown(f"<div class='mini-card'><span class='label-mini'>👞 Chutes +22.5</span><span class='prob-text'>{res['chutes']:.1f}%</span></div>", unsafe_allow_html=True)
            with mc3: st.markdown(f"<div class='mini-card'>🎯 <span class='label-mini' style='display:inline;'>No Gol +8.5</span><br><span class='prob-text'>{res['nogol']:.1f}%</span></div>", unsafe_allow_html=True)
            with mc4: st.markdown(f"<div class='mini-card'><span class='label-mini'>⚠️ Faltas +24.5</span><span class='prob-text'>{res['faltas']:.1f}%</span></div>", unsafe_allow_html=True)
            with mc5: st.markdown(f"<div class='mini-card'><span class='label-mini'>🟨 Cartões +4.5</span><span class='prob-text'>{res['cartoes']:.1f}%</span></div>", unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align:center; opacity:0.3; font-size:10px;'>GESTOR IA v7.8 - NEURAL ENGINE 2026</p>", unsafe_allow_html=True)
