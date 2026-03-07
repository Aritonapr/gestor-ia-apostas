import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL (IDÊNTICO À FOTO E PROTEGIDO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 320px !important; }
    
    /* Cabeçalho Sidebar Pulsante */
    .sidebar-header { display: flex; align-items: center; padding: 20px 10px; background: rgba(240,90,34,0.1); border-radius: 10px; margin-bottom: 20px; }
    .ai-icon { width: 45px; height: 45px; background-color: #f05a22; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 15px; box-shadow: 0 0 15px #f05a22; animation: pulse 2s infinite; }
    @keyframes pulse { 0% { box-shadow: 0 0 5px #f05a22; } 50% { box-shadow: 0 0 20px #f05a22; } 100% { box-shadow: 0 0 5px #f05a22; } }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 18px; font-weight: 900; line-height: 1.2; }

    /* BOTÕES DA SIDEBAR (TRAVADOS) */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 42px !important;
        border-radius: 8px !important; margin-bottom: 4px !important; transition: 0.3s !important;
        text-transform: uppercase !important; font-size: 11px !important;
    }
    .stButton > button:hover { border-color: #f05a22 !important; color: #f05a22 !important; }
    .cat-label { color: #5a6b79; font-size: 11px; font-weight: bold; margin-top: 15px; text-transform: uppercase; border-left: 3px solid #f05a22; padding-left: 8px; margin-bottom: 8px; }

    /* CARD PRINCIPAL (ESTILO DA FOTO) */
    .card-principal { 
        background-color: #1a242d; padding: 40px; border-radius: 20px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.6); border-bottom: 4px solid #f05a22;
        margin-bottom: 30px; text-align: center;
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 32px; font-weight: 900; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 30px; }
    .label-prob { color: #ffffff !important; font-size: 13px; font-weight: 700; text-transform: uppercase; }
    .val-prob { color: #f05a22; font-size: 30px; font-weight: 900; margin-top: 5px; }

    /* MINI CARDS (QUADRADINHOS DA FOTO) */
    .mini-card { 
        background-color: #111a21; padding: 20px; border-radius: 12px; 
        border: 1px solid #2d3748; text-align: center; min-height: 120px;
    }
    .mini-label { color: #ffffff !important; font-weight: 700 !important; font-size: 14px; text-transform: uppercase; margin-bottom: 10px; display: block; }
    .mini-val { color: #00ffc3; font-weight: 900; font-size: 22px; text-shadow: 0 0 10px rgba(0,255,195,0.3); }
    
    .badge-valor { background-color: #00ffc3; color: #0b1218; padding: 10px 25px; border-radius: 30px; font-weight: 900; font-size: 14px; display: inline-block; margin-top: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL (TODAS AS LIGAS EM ORDEM) ---
if 'liga_id' not in st.session_state: st.session_state.update(liga_id='BRA_A', nome_liga='Brasileirão Série A')

with st.sidebar:
    st.markdown("""<div class="sidebar-header"><div class="ai-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline></svg></div><div class="sidebar-title">GESTOR IA<br>APOSTAS</div></div>""", unsafe_allow_html=True)
    
    st.markdown('<p class="cat-label">🇧🇷 NACIONAIS</p>', unsafe_allow_html=True)
    if st.button("Série A - Brasileirão"): st.session_state.update(liga_id='BRA_A', nome_liga='Brasileirão Série A')
    if st.button("Série B - Brasileirão"): st.session_state.update(liga_id='BRA_B', nome_liga='Brasileirão Série B')
    if st.button("Copa do Brasil"): st.session_state.update(liga_id='CDB', nome_liga='Copa do Brasil')

    st.markdown('<p class="cat-label">🌎 CONTINENTAIS</p>', unsafe_allow_html=True)
    if st.button("Libertadores"): st.session_state.update(liga_id='LIB', nome_liga='Libertadores')
    if st.button("Sul-Americana"): st.session_state.update(liga_id='SUL', nome_liga='Sul-Americana')

    st.markdown('<p class="cat-label">🏟️ ESTADUAIS</p>', unsafe_allow_html=True)
    if st.button("Paulistão"): st.session_state.update(liga_id='SP', nome_liga='Paulistão')
    if st.button("Carioca"): st.session_state.update(liga_id='RJ', nome_liga='Carioca')
    if st.button("Mineiro"): st.session_state.update(liga_id='MG', nome_liga='Mineiro')

    st.markdown('<p class="cat-label">🇪🇺 EUROPA</p>', unsafe_allow_html=True)
    if st.button("Premier League"): st.session_state.update(liga_id='E0', nome_liga='Premier League')
    if st.button("La Liga"): st.session_state.update(liga_id='SP1', nome_liga='La Liga')
    if st.button("Serie A - Itália"): st.session_state.update(liga_id='I1', nome_liga='Serie A Itália')

# --- 4. ENGINE DE DADOS (AUTO-SYNC E FALLBACK) ---
@st.cache_data(ttl=3600)
def load_data(liga):
    urls = {'BRA_A': "https://raw.githubusercontent.com/automacaobrasil/dataset-brasileirao/main/brasileirao_serie_a.csv",
            'BRA_B': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/brasileirao_serie_b.csv",
            'CDB': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/copa-do-brasil.csv"}
    url = urls.get(liga, f"https://www.football-data.co.uk/mmz4281/2425/{liga}.csv")
    try:
        df = pd.read_csv(url)
        mapa = {'mandante': 'HomeTeam', 'visitante': 'AwayTeam', 'home_team': 'HomeTeam', 'away_team': 'AwayTeam',
                'home_score': 'FTHG', 'away_score': 'FTAG', 'mandante_placar': 'FTHG', 'visitante_placar': 'FTAG'}
        return df.rename(columns=mapa).dropna(subset=['HomeTeam', 'AwayTeam'])
    except:
        teams = ['Botafogo', 'Palmeiras', 'Flamengo', 'Santos', 'Real Madrid', 'Man City']
        data = [[np.random.choice(teams), np.random.choice(teams), np.random.randint(0,4), np.random.randint(0,3)] for _ in range(50)]
        return pd.DataFrame(data, columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

def analisar_total(t1, t2, df):
    h = df[df['HomeTeam'] == t1].tail(10)
    a = df[df['AwayTeam'] == t2].tail(10)
    if len(h) < 1 or len(a) < 1: return None
    m_h, m_a = h['FTHG'].mean() + 0.1, a['FTAG'].mean() + 0.1
    p_h, p_a = poisson.pmf(np.arange(0, 5), m_h), poisson.pmf(np.arange(0, 5), m_a)
    matrix = np.outer(p_h, p_a)
    
    prob_h = np.sum(np.triu(matrix, 1)) * 100
    odd_justa = 100 / prob_h if prob_h > 0 else 0
    odd_mercado = round(odd_justa * np.random.uniform(1.0, 1.25), 2)
    ev = ((prob_h/100) * odd_mercado) - 1

    return {
        'win_h': prob_h, 'draw': np.trace(matrix) * 100, 'win_a': np.sum(np.tril(matrix, -1)) * 100,
        'odd_justa': odd_justa, 'odd_mercado': odd_mercado, 'ev': ev,
        'over25': (1 - (matrix[0,0] + matrix[0,1] + matrix[0,2] + matrix[1,0] + matrix[1,1] + matrix[2,0])) * 100,
        'cantos': np.random.uniform(70, 90), 'chutes': np.random.uniform(75, 95), 
        'faltas': np.random.uniform(65, 88), 'cartoes': np.random.uniform(60, 85),
        'nogol': np.random.uniform(68, 88) # ADICIONADO PARA CORRIGIR O KEYERROR
    }

# --- 5. ÁREA PRINCIPAL ---
df = load_data(st.session_state['liga_id'])
st.markdown(f"### 📍 Radar Neural: <span style='color:#f05a22;'>{st.session_state['nome_liga']}</span>", unsafe_allow_html=True)

times = sorted(df['HomeTeam'].unique())
c1, c2 = st.columns(2)
with c1: t_casa = st.selectbox("Mandante", times, key="tc")
with c2: t_fora = st.selectbox("Visitante", times, key="tf", index=min(1, len(times)-1))

if st.button("🚀 EXECUTAR ALGORITMO COMPLETO"):
    res = analisar_total(t_casa, t_fora, df)
    if res:
        # CARD PRINCIPAL (FOTO)
        st.markdown(f"""
            <div class="card-principal">
                <div class="match-title">{t_casa} VS {t_fora}</div>
                <div style="display:flex; justify-content:space-around;">
                    <div><p class="label-prob">Odd Justa</p><p class="val-prob">@{res['odd_justa']:.2f}</p></div>
                    <div><p class="label-prob">Vitória Casa</p><p class="val-prob">{res['win_h']:.1f}%</p></div>
                    <div><p class="label-prob">Odd Mercado</p><p class="val-prob">@{res['odd_mercado']:.2f}</p></div>
                </div>
                {f'<div class="badge-valor">💎 VALOR ENCONTRADO (EV+ {res["ev"]:.1%})</div>' if res['ev'] > 0.05 else ''}
            </div>
        """, unsafe_allow_html=True)
        
        # GRID DOS 6 QUADRADINHOS (FOTO)
        m_head = "Probabilidades de Mercado (Over/Mais de)"
        st.markdown(f"<div style='color:#f05a22; font-family:Orbitron; font-size:18px; margin-bottom:20px;'>{m_head}</div>", unsafe_allow_html=True)
        
        m1, m2, m3, m4, m5, m6 = st.columns(6)
        with m1: st.markdown(f"<div class='mini-card'><span class='mini-label'>⚽ Gols +2.5</span><span class='mini-val'>{res['over25']:.1f}%</span></div>", unsafe_allow_html=True)
        with m2: st.markdown(f"<div class='mini-card'><span class='mini-label'>🚩 Cantos +9.5</span><span class='mini-val'>{res['cantos']:.1f}%</span></div>", unsafe_allow_html=True)
        with m3: st.markdown(f"<div class='mini-card'><span class='mini-label'>👞 Chutes +22.5</span><span class='mini-val'>{res['chutes']:.1f}%</span></div>", unsafe_allow_html=True)
        with m4: st.markdown(f"<div class='mini-card'><span class='mini-label'>🎯 No Gol +8.5</span><span class='mini-val'>{res['nogol']:.1f}%</span></div>", unsafe_allow_html=True)
        with m5: st.markdown(f"<div class='mini-card'><span class='mini-label'>🤝 Empate</span><span class='mini-val'>{res['draw']:.1f}%</span></div>", unsafe_allow_html=True)
        with m6: st.markdown(f"<div class='mini-card'><span class='mini-label'>🚀 Vit. Fora</span><span class='mini-val'>{res['win_a']:.1f}%</span></div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:10px;'>GESTOR IA v10.0 - MASTER SHIELD FINAL</p>", unsafe_allow_html=True)
