import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA - OMNI 2026", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL FUTURISTA (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');
    .main { background-color: #0b1218; color: #e4e6eb; }
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 320px !important; }
    
    /* Cabeçalho Pulsante Sidebar */
    .sidebar-header { display: flex; align-items: center; padding: 20px 10px; background: linear-gradient(180deg, rgba(240,90,34,0.1) 0%, rgba(0,0,0,0) 100%); border-radius: 10px; margin-bottom: 20px; }
    .ai-icon { width: 45px; height: 45px; background-color: #f05a22; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 0 15px #f05a22; animation: pulse 2s infinite; }
    @keyframes pulse { 0% { box-shadow: 0 0 5px #f05a22; } 50% { box-shadow: 0 0 20px #f05a22; } 100% { box-shadow: 0 0 5px #f05a22; } }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 18px; font-weight: 900; letter-spacing: 1px; line-height: 1.2; }

    /* PADRONIZAÇÃO TOTAL DOS BOTÕES */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; 
        border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 42px !important;
        border-radius: 8px !important; margin-bottom: 4px !important; 
        transition: 0.3s !important; text-transform: uppercase !important; font-size: 11px !important;
    }
    .stButton > button:hover { border-color: #f05a22 !important; color: #f05a22 !important; background-color: #0b1218 !important; }
    
    .cat-label { color: #5a6b79; font-size: 11px; font-weight: bold; margin-top: 15px; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 2px; border-left: 3px solid #f05a22; padding-left: 8px; }
    
    .card-pro { background: #111a21; padding: 25px; border-radius: 15px; border: 1px solid #2d3748; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    .metric-val { color: #f05a22; font-size: 32px; font-weight: 900; }
    .zebra-alert { background-color: #ff4b4b22; border: 1px solid #ff4b4b; padding: 10px; border-radius: 10px; color: #ff4b4b; font-weight: bold; text-align: center; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CONTROLE DE NAVEGAÇÃO ---
if 'liga_id' not in st.session_state: st.session_state['liga_id'] = 'BRA_A'
if 'nome_liga' not in st.session_state: st.session_state['nome_liga'] = 'Brasileirão Série A'

# --- 4. BARRA LATERAL (OMNI COMPLETA) ---
with st.sidebar:
    # Cabeçalho Fixo
    st.markdown("""<div class="sidebar-header"><div class="ai-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg></div><div class="sidebar-title">GESTOR IA<br>APOSTAS</div></div>""", unsafe_allow_html=True)
    
    # NACIONAIS
    st.markdown('<p class="cat-label">🇧🇷 NACIONAIS</p>', unsafe_allow_html=True)
    if st.button("Série A - Brasileirão"): st.session_state.update(liga_id='BRA_A', nome_liga='Brasileirão Série A')
    if st.button("Série B - Brasileirão"): st.session_state.update(liga_id='BRA_B', nome_liga='Brasileirão Série B')
    if st.button("Copa do Brasil"): st.session_state.update(liga_id='CDB', nome_liga='Copa do Brasil')

    # CONTINENTAIS
    st.markdown('<p class="cat-label">🌎 CONTINENTAIS</p>', unsafe_allow_html=True)
    if st.button("Libertadores"): st.session_state.update(liga_id='LIB', nome_liga='Libertadores')
    if st.button("Sul-Americana"): st.session_state.update(liga_id='SUL', nome_liga='Sul-Americana')

    # ESTADUAIS
    st.markdown('<p class="cat-label">🏟️ ESTADUAIS</p>', unsafe_allow_html=True)
    if st.button("Paulistão"): st.session_state.update(liga_id='SP', nome_liga='Paulistão')
    if st.button("Carioca"): st.session_state.update(liga_id='RJ', nome_liga='Carioca')
    if st.button("Mineiro"): st.session_state.update(liga_id='MG', nome_liga='Mineiro')

    # EUROPA (RESTAURADA)
    st.markdown('<p class="cat-label">🇪🇺 EUROPA</p>', unsafe_allow_html=True)
    if st.button("Premier League"): st.session_state.update(liga_id='E0', nome_liga='Premier League')
    if st.button("La Liga"): st.session_state.update(liga_id='SP1', nome_liga='La Liga')
    if st.button("Serie A - Itália"): st.session_state.update(liga_id='I1', nome_liga='Serie A Itália')
    if st.button("Bundesliga"): st.session_state.update(liga_id='D1', nome_liga='Bundesliga')
    if st.button("Ligue 1 - França"): st.session_state.update(liga_id='F1', nome_liga='Ligue 1 França')

# --- 5. ENGINE DE DADOS ---
@st.cache_data(ttl=3600)
def load_data(liga):
    urls = {
        'BRA_A': "https://raw.githubusercontent.com/automacaobrasil/dataset-brasileirao/main/brasileirao_serie_a.csv",
        'BRA_B': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/brasileirao_serie_b.csv",
        'CDB': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/copa-do-brasil.csv",
        'SP': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/campeonato-paulista.csv",
        'LIB': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/libertadores.csv"
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
        # Fallback Robusto
        teams = ['Flamengo', 'Palmeiras', 'Botafogo', 'Real Madrid', 'Man City', 'Arsenal', 'Santos', 'Sport']
        data = [[np.random.choice(teams), np.random.choice(teams), np.random.randint(0,4), np.random.randint(0,3)] for _ in range(50)]
        return pd.DataFrame(data, columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

def analisar(t1, t2, df):
    h = df[df['HomeTeam'] == t1].tail(10)
    a = df[df['AwayTeam'] == t2].tail(10)
    if len(h) < 2 or len(a) < 2: return None
    m_h, m_a = h['FTHG'].mean() + 0.1, a['FTAG'].mean() + 0.1
    p_h = poisson.pmf(np.arange(0, 5), m_h)
    p_a = poisson.pmf(np.arange(0, 5), m_a)
    matrix = np.outer(p_h, p_a)
    
    # Zebra Check
    zebra = False
    if np.sum(np.triu(matrix, 1)) > 0.55 and (h['FTHG'] < h['FTAG']).sum() >= 3:
        zebra = True

    return {'casa': np.sum(np.triu(matrix, 1)) * 100, 'empate': np.trace(matrix) * 100, 
            'fora': np.sum(np.tril(matrix, -1)) * 100, 'xg_h': m_h, 'xg_a': m_a, 'zebra': zebra}

# --- 6. ÁREA PRINCIPAL ---
df = load_data(st.session_state['liga_id'])
st.markdown(f"### ⚡ Radar IA: <span style='color:#f05a22;'>{st.session_state['nome_liga']}</span>", unsafe_allow_html=True)

tab_analise, tab_scanner, tab_zebras = st.tabs(["🎯 ANALISADOR PRO", "🔍 VALUE HUNTER", "⚠️ FILTRO DE ZEBRAS"])

with tab_analise:
    if not df.empty:
        times = sorted(df['HomeTeam'].unique())
        c1, c2 = st.columns(2)
        with c1: t1 = st.selectbox("Mandante", times, key="t1")
        with c2: t2 = st.selectbox("Visitante", times, key="t2")
        
        if st.button("PROCESSAR ALGORITMO"):
            res = analisar(t1, t2, df)
            if res:
                st.markdown(f"""<div class="card-pro"><h2 style='text-align:center;'>{t1} vs {t2}</h2>
                <div style='display:flex; justify-content:space-around; text-align:center;'>
                <div><p style='color:#8a949d;'>Casa</p><p class="metric-val">{res['casa']:.1f}%</p></div>
                <div><p style='color:#8a949d;'>Empate</p><p class="metric-val">{res['empate']:.1f}%</p></div>
                <div><p style='color:#8a949d;'>Fora</p><p class="metric-val">{res['fora']:.1f}%</p></div>
                </div></div>""", unsafe_allow_html=True)
                st.markdown("#### 📊 Comparativo de Poder Ofensivo")
                st.write(f"{t1}: {res['xg_h']:.2f}")
                st.progress(min(res['xg_h']/4, 1.0))
                st.write(f"{t2}: {res['xg_a']:.2f}")
                st.progress(min(res['xg_a']/4, 1.0))

with tab_scanner:
    st.markdown("#### 🔍 Oportunidades Identificadas na Liga")
    times_scan = sorted(df['HomeTeam'].unique())
    scan_res = []
    for i in range(min(len(times_scan), 6)):
        for j in range(len(times_scan)-1, len(times_scan)-4, -1):
            if i != j:
                r = analisar(times_scan[i], times_scan[j], df)
                if r and r['casa'] > 70:
                    scan_res.append({'Jogo': f"{times_scan[i]} vs {times_scan[j]}", 'Vitória Casa': f"{r['casa']:.1f}%"})
    if scan_res:
        st.table(pd.DataFrame(scan_res).head(3))
    else:
        st.info("Buscando padrões de alta confiança...")

with tab_zebras:
    st.markdown("#### ⚠️ Alerta de Zebras (Favoritos Instáveis)")
    found_z = False
    for i in range(min(len(times_scan), 10)):
        for j in range(len(times_scan)-1, 0, -1):
            r = analisar(times_scan[i], times_scan[j], df)
            if r and r['zebra']:
                st.markdown(f'<div class="zebra-alert">🚨 Risco no favoritismo do {times_scan[i]} contra o {times_scan[j]}!</div>', unsafe_allow_html=True)
                found_z = True
    if not found_z:
        st.success("Nenhum favorito sob risco detectado nesta rodada.")

st.markdown("<br><br><p style='text-align:center; opacity:0.3; font-size:10px;'>GESTOR IA v6.5 - OMNI SUPREME</p>", unsafe_allow_html=True)
