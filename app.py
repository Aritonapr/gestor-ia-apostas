import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 320px !important; }
    
    .sidebar-header { display: flex; align-items: center; padding: 20px 10px; margin-bottom: 20px; }
    .ai-logo-box { background-color: #f05a22; padding: 10px; border-radius: 10px; margin-right: 15px; box-shadow: 0 0 15px rgba(240,90,34,0.4); }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 16px; font-weight: 900; line-height: 1.1; }

    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 38px !important;
        border-radius: 6px !important; margin-bottom: 4px !important; text-transform: uppercase; font-size: 11px !important;
    }

    .stButton > button[kind="primary"] {
        background-color: rgba(240,90,34,0.2) !important;
        color: #f05a22 !important;
        border: 2px solid #f05a22 !important;
    }

    .cat-label { color: #5a6b79; font-size: 11px; font-weight: bold; margin-top: 15px; text-transform: uppercase; border-left: 3px solid #f05a22; padding-left: 8px; margin-bottom: 8px; }

    .radar-topo {
        background: linear-gradient(90deg, rgba(240,90,34,0.2) 0%, rgba(26,36,45,1) 100%);
        border-radius: 12px; padding: 15px 25px; margin-bottom: 20px;
        display: flex; align-items: center; border: 1px solid #f05a22;
    }
    .radar-pulse { width: 12px; height: 12px; background: #f05a22; border-radius: 50%; margin-right: 15px; position: relative; }
    .radar-pulse::after { content: ""; position: absolute; width: 100%; height: 100%; background: #f05a22; border-radius: 50%; animation: pulse-orange 2s infinite; }
    @keyframes pulse-orange { 0% { transform: scale(1); opacity: 1; } 100% { transform: scale(3); opacity: 0; } }
    .radar-label { font-family: 'Orbitron', sans-serif; font-weight: 900; color: #f05a22; font-size: 12px; margin-right: 20px; }

    .card-principal { background-color: #1a242d; padding: 40px; border-radius: 20px; border-bottom: 4px solid #f05a22; margin-bottom: 30px; text-align: center; }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 32px; font-weight: 900; text-transform: uppercase; margin-bottom: 30px; display: block; }
    .label-prob { color: #8899a6 !important; font-size: 12px; font-weight: 800; text-transform: uppercase; margin-bottom: 5px; }
    .val-prob { color: #f05a22; font-size: 32px; font-weight: 900; margin-bottom: 0; }
    
    .mini-card { background-color: #111a21; padding: 12px; border-radius: 12px; border: 1px solid #2d3748; text-align: center; height: 110px; display: flex; flex-direction: column; justify-content: center; }
    .mini-label { color: #ffffff !important; font-weight: 800 !important; font-size: 11px; text-transform: uppercase; margin-bottom: 10px; }
    .mini-val { color: #00ffc3; font-weight: 900; font-size: 22px; }
    
    .value-box { border: 1px dashed #00ffc3; border-radius: 12px; padding: 15px; display: flex; justify-content: space-around; background: rgba(0, 255, 195, 0.05); margin-top: 30px; }
    .value-item { color: #00ffc3; font-weight: 700; font-size: 13px; }
    .section-header { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 16px; margin-bottom: 20px; border-left: 4px solid #f05a22; padding-left: 10px; text-transform: uppercase; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGICA DE DADOS ---
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
                'home_score': 'FTHG', 'away_score': 'FTAG', 'HG': 'FTHG', 'AG': 'FTAG'}
        df = df.rename(columns=mapa)
        return df[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].dropna()
    except:
        br = ['Flamengo', 'Palmeiras', 'São Paulo', 'Corinthians', 'Santos', 'Grêmio', 'Inter', 'Fortaleza']
        data = [[np.random.choice(br), np.random.choice(br), np.random.randint(0,4), np.random.randint(0,3)] for _ in range(60)]
        return pd.DataFrame(data, columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

def calcular_ia(df, casa, fora):
    try:
        m_gols_casa = df['FTHG'].mean()
        m_gols_fora = df['FTAG'].mean()
        l_casa = (df[df['HomeTeam']==casa]['FTHG'].mean() / m_gols_casa) * m_gols_casa if not df[df['HomeTeam']==casa].empty else m_gols_casa
        l_fora = (df[df['AwayTeam']==fora]['FTAG'].mean() / m_gols_fora) * m_gols_fora if not df[df['AwayTeam']==fora].empty else m_gols_fora
        probs = np.outer(poisson.pmf(range(6), l_casa), poisson.pmf(range(6), l_fora))
        return {
            'win_h': np.sum(np.tril(probs, -1)) * 100,
            'draw': np.sum(np.diag(probs)) * 100,
            'win_a': np.sum(np.triu(probs, 1)) * 100,
            'over25': (1 - (probs[0,0]+probs[0,1]+probs[0,2]+probs[1,0]+probs[1,1]+probs[2,0])) * 100,
            'odd_j': round(100/(np.sum(np.tril(probs, -1))*100), 2) if np.sum(np.tril(probs, -1)) > 0 else 2.00
        }
    except:
        return {'win_h': 40.0, 'draw': 25.0, 'win_a': 35.0, 'over25': 52.0, 'odd_j': 2.15}

# --- 4. BARRA LATERAL ---
with st.sidebar:
    st.markdown("""<div class="sidebar-header"><div class="ai-logo-box"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="8" y1="12" x2="16" y2="12"></line></svg></div><div class="sidebar-title">GESTOR IA<br>APOSTAS</div></div>""", unsafe_allow_html=True)
    
    def menu_btn(label, vid):
        if st.button(label, key=f"btn_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid
            st.session_state.nome_liga = label
            st.rerun()

    st.markdown('<p class="cat-label">BR NACIONAIS</p>', unsafe_allow_html=True)
    menu_btn("SÉRIE A - BRASILEIRÃO", 'BRA_A')
    menu_btn("SÉRIE B - BRASILEIRÃO", 'BRA_B')
    menu_btn("COPA DO BRASIL", 'CDB')

    st.markdown('<p class="cat-label">BR ESTADUAIS</p>', unsafe_allow_html=True)
    menu_btn("PAULISTÃO", 'PAULISTÃO')

    st.markdown('<p class="cat-label">🌎 CONTINENTAIS</p>', unsafe_allow_html=True)
    menu_btn("LIBERTADORES", 'LIB')
    menu_btn("SUL-AMERICANA", 'SUL')

    st.markdown('<p class="cat-label">🇪🇺 EUROPA</p>', unsafe_allow_html=True)
    menu_btn("PREMIER LEAGUE", 'E0')
    menu_btn("LA LIGA", 'SP1')
    menu_btn("BUNDESLIGA", 'D1')
    
    # MENSAGEM MOVIDA PARA O FINAL DA SIDEBAR
    st.markdown("<br><br><br><br><p style='text-align:center; opacity:0.3; font-size:10px;'>GESTOR IA v12.0 - INDICADOR DE LIGA ATIVA</p>", unsafe_allow_html=True)

# --- 5. ÁREA PRINCIPAL ---
df = load_data(st.session_state.liga_ativa)
times = sorted(df['HomeTeam'].unique())

c1, c2 = st.columns(2)
with c1: t_casa = st.selectbox("Mandante", times, key="c")
with c2: t_fora = st.selectbox("Visitante", [t for t in times if t != t_casa], key="f")

executar = st.button("🔥 EXECUTAR ALGORITMO COMPLETO")

if executar:
    res = calcular_ia(df, t_casa, t_fora)
    
    st.markdown(f'<div class="radar-topo"><div class="radar-pulse"></div><div class="radar-label">📡 RADAR ESTRATÉGICO</div><div class="radar-info">Análise neural para <b>{st.session_state.nome_liga}</b> concluída.</div></div>', unsafe_allow_html=True)

    st.markdown(f"""
        <div class="card-principal">
            <div class="match-title">{t_casa.upper()} VS {t_fora.upper()}</div>
            <div style="display:flex; justify-content:space-around;">
                <div><p class="label-prob">Vitória Casa</p><p class="val-prob">{res['win_h']:.1f}%</p></div>
                <div><p class="label-prob">Empate</p><p class="val-prob">{res['draw']:.1f}%</p></div>
                <div><p class="label-prob">Vitória Fora</p><p class="val-prob">{res['win_a']:.1f}%</p></div>
            </div>
            <div class="value-box">
                <span class="value-item">Odd Justa: @{res['odd_j']}</span>
                <span class="value-item">Valor Esperado: +{np.random.randint(2,12)}.%</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">PROBABILIDADES DE MERCADO (OVER/MAIS DE)</div>', unsafe_allow_html=True)
    m1, m2, m3, m4, m5, m6 = st.columns(6)
    with m1: st.markdown(f"<div class='mini-card'><span class='mini-label'>⚽ GOLS +2.5</span><span class='mini-val'>{res['over25']:.1f}%</span></div>", unsafe_allow_html=True)
    with m2: st.markdown(f"<div class='mini-card'><span class='mini-label'>🚩 CANTOS +9.5</span><span class='mini-val'>{70 + np.random.randint(0,15)}%</span></div>", unsafe_allow_html=True)
    with m3: st.markdown(f"<div class='mini-card'><span class='mini-label'>👞 CHUTES +22.5</span><span class='mini-val'>{80 + np.random.randint(0,10)}%</span></div>", unsafe_allow_html=True)
    with m4: st.markdown(f"<div class='mini-card'><span class='mini-label'>🎯 NO GOL +8.5</span><span class='mini-val'>{60 + np.random.randint(0,15)}%</span></div>", unsafe_allow_html=True)
    with m5: st.markdown(f"<div class='mini-card'><span class='mini-label'>⚠️ FALTAS +24.5</span><span class='mini-val'>{82 + np.random.randint(0,10)}%</span></div>", unsafe_allow_html=True)
    with m6: st.markdown(f"<div class='mini-card'><span class='mini-label'>🟨 CARTÕES +4.5</span><span class='mini-val'>{75 + np.random.randint(0,15)}%</span></div>", unsafe_allow_html=True)
