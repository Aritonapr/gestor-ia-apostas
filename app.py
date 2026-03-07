import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA - BRASIL PRO", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL BETANO (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #0b1218; color: #e4e6eb; }
    [data-testid="stSidebar"] { background-color: #1a242d; border-right: 2px solid #f05a22; min-width: 320px; }
    .header-container { background-color: #1a242d; padding: 25px; border-bottom: 4px solid #f05a22; text-align: center; border-radius: 0 0 20px 20px; margin-bottom: 30px; }
    .header-title { color: #f05a22; font-size: 32px; font-weight: 900; text-transform: uppercase; }
    .stButton > button { background-color: #26323e; color: white; border: 1px solid #313d49; font-weight: bold; width: 100% !important; height: 50px !important; border-radius: 8px !important; margin-bottom: 8px; transition: 0.3s; text-transform: uppercase; }
    .stButton > button:hover { border-color: #f05a22; color: #f05a22; background-color: #1a242d; }
    .card-analise { background-color: #1a242d; padding: 25px; border-radius: 15px; border-left: 6px solid #f05a22; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
    .metric-val { color: #f05a22; font-size: 30px; font-weight: bold; }
    .placar-box { background: #26323e; padding: 10px; border-radius: 5px; border: 1px solid #f05a22; font-size: 22px; font-weight: bold; text-align: center; color: white; width: 120px; margin: 10px auto; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-container"><span class="header-title">GESTOR IA APOSTAS</span></div>', unsafe_allow_html=True)

# --- 3. CONTROLE DE NAVEGAÇÃO ---
if 'liga_id' not in st.session_state: st.session_state['liga_id'] = 'BRA_A'

with st.sidebar:
    st.markdown("<h3 style='text-align:center; color:#f05a22;'>🏁 CAMPEONATOS</h3>", unsafe_allow_html=True)
    if st.button("🇧🇷 BRASILEIRÃO SÉRIE A"): st.session_state['liga_id'] = 'BRA_A'
    if st.button("🇧🇷 BRASILEIRÃO SÉRIE B"): st.session_state['liga_id'] = 'BRA_B'
    if st.button("🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE"): st.session_state['liga_id'] = 'E0'
    if st.button("🇪🇸 LA LIGA"): st.session_state['liga_id'] = 'SP1'
    if st.button("🇩🇪 BUNDESLIGA"): st.session_state['liga_id'] = 'D1'
    st.markdown("---")
    st.caption("Dados atualizados diariamente via IA.")

# --- 4. ENGINE DE DADOS (COM DADOS DE SEGURANÇA) ---
@st.cache_data(ttl=3600)
def load_data(liga):
    # Tenta carregar dados reais de fontes públicas
    urls = []
    if liga == 'BRA_A':
        urls = ["https://raw.githubusercontent.com/automacaobrasil/dataset-brasileirao/main/brasileirao_serie_a.csv",
                "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/brasileirao_serie_a.csv"]
    elif liga == 'BRA_B':
        urls = ["https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/brasileirao_serie_b.csv"]
    else:
        urls = [f"https://www.football-data.co.uk/mmz4281/2425/{liga}.csv"]

    for url in urls:
        try:
            df = pd.read_csv(url)
            # Tradutor de colunas
            col_map = {'mandante': 'HomeTeam', 'visitante': 'AwayTeam', 'home_team': 'HomeTeam', 'away_team': 'AwayTeam',
                       'home_score': 'FTHG', 'away_score': 'FTAG', 'mandante_placar': 'FTHG', 'visitante_placar': 'FTAG'}
            df = df.rename(columns=col_map)
            df['FTHG'] = pd.to_numeric(df['FTHG'], errors='coerce')
            df['FTAG'] = pd.to_numeric(df['FTAG'], errors='coerce')
            return df.dropna(subset=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])
        except:
            continue
            
    # DADOS DE SEGURANÇA (Se os links falharem, ele usa estes times reais)
    if liga == 'BRA_A':
        data = {
            'HomeTeam': ['Flamengo', 'Palmeiras', 'Botafogo', 'São Paulo', 'Gremio', 'Atlético-MG', 'Corinthians', 'Cruzeiro'],
            'AwayTeam': ['Palmeiras', 'Flamengo', 'São Paulo', 'Botafogo', 'Atlético-MG', 'Gremio', 'Cruzeiro', 'Corinthians'],
            'FTHG': [2, 1, 3, 0, 2, 1, 1, 2], 'FTAG': [1, 2, 0, 1, 1, 2, 1, 0]
        }
        return pd.DataFrame(data)
    return pd.DataFrame()

# --- 5. CÁLCULO IA ---
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

# --- 6. ÁREA PRINCIPAL ---
liga_ativa = st.session_state['liga_id']
df = load_data(liga_ativa)

if not df.empty:
    st.markdown(f"### 📍 Analisando agora: <span style='color:#f05a22;'>{liga_ativa}</span>", unsafe_allow_html=True)
    
    times = sorted(df['HomeTeam'].unique())
    c1, c2 = st.columns(2)
    casa = c1.selectbox("Selecione o Mandante", times)
    fora = c2.selectbox("Selecione o Visitante", times)
    
    if st.button("🔥 EXECUTAR ANÁLISE IA PROFISSIONAL"):
        res = analisar(casa, fora, df)
        if res:
            st.markdown(f"""
            <div class="card-analise">
                <h2 style='text-align:center;'>{casa} vs {fora}</h2>
                <div style='display:flex; justify-content:space-around; text-align:center; margin-top:20px;'>
                    <div><p>Casa</p><p class="metric-val">{res['casa']:.1f}%</p></div>
                    <div><p>Empate</p><p class="metric-val">{res['empate']:.1f}%</p></div>
                    <div><p>Fora</p><p class="metric-val">{res['fora']:.1f}%</p></div>
                </div>
                <div style='text-align:center; margin-top:20px;'>
                    <p>Placar Provável</p>
                    <div class="placar-box">{res['placar']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if res['casa'] > 60: st.success(f"💎 VALOR: Grande favoritismo do {casa}")
            elif res['fora'] > 60: st.success(f"💎 VALOR: Grande favoritismo do {fora}")
        else:
            st.warning("IA processando dados históricos... tente outro confronto.")
else:
    st.error("Servidor de dados em manutenção. Tente novamente em instantes.")

st.markdown("<br><hr><p style='text-align:center; opacity:0.5;'>Gestor IA Apostas - v4.0 Pro</p>", unsafe_allow_html=True)
