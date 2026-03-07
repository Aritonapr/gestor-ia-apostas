import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson
import requests

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA - APOSTAS", layout="wide", page_icon="⚽")

# --- ESTILO BETANO DARK (CSS CUSTOMIZADO) ---
st.markdown("""
    <style>
    .main { background-color: #0b1218; color: #e4e6eb; }
    div[data-testid="stSidebar"] { background-color: #1a242d; border-right: 1px solid #f05a22; }
    
    /* Cabeçalho Estilo Betano */
    .header-betano {
        background-color: #1a242d;
        padding: 20px;
        border-bottom: 3px solid #f05a22;
        text-align: center;
        margin-bottom: 20px;
        border-radius: 0 0 15px 15px;
    }
    .header-title { color: #f05a22; font-size: 32px; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; }
    
    /* Botões de Liga */
    .stButton>button {
        background-color: #26323e;
        color: white;
        border: 1px solid #313d49;
        padding: 10px 20px;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover { border-color: #f05a22; color: #f05a22; background-color: #1a242d; }
    .active-btn { background: #f05a22 !important; color: white !important; }

    /* Cards de Jogo */
    .card-jogo {
        background-color: #1a242d;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #f05a22;
        margin-bottom: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO DO SITE ---
st.markdown("""
    <div class="header-betano">
        <span class="header-title">🧡 GESTOR IA APOSTAS</span>
    </div>
    """, unsafe_allow_html=True)

# --- SISTEMA DE ESTADO (PARA OS BOTOES FUNCIONAREM) ---
if 'liga_selecionada' not in st.session_state:
    st.session_state['liga_selecionada'] = 'BRA'

# --- BARRA LATERAL (BOTÕES DE LIGA) ---
st.sidebar.markdown("### 🏆 CAMPEONATOS")
if st.sidebar.button("🇧🇷 Brasileirão Série A"):
    st.session_state['liga_selecionada'] = 'BRA'
if st.sidebar.button("🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League"):
    st.session_state['liga_selecionada'] = 'E0'
if st.sidebar.button("🇪🇸 La Liga"):
    st.session_state['liga_selecionada'] = 'SP1'
if st.sidebar.button("🇮🇹 Serie A (Itália)"):
    st.session_state['liga_selecionada'] = 'I1'
if st.sidebar.button("🇩🇪 Bundesliga"):
    st.session_state['liga_selecionada'] = 'D1'

st.sidebar.markdown("---")
st.sidebar.header("🤖 ALERTA TELEGRAM")
tg_token = st.sidebar.text_input("Token do Bot", type="password")
tg_id = st.sidebar.text_input("Seu ID")

# --- ENGINE DE DADOS ---
@st.cache_data(ttl=3600)
def get_data(liga):
    if liga == 'BRA':
        url = "https://raw.githubusercontent.com/automacaobrasil/dataset-brasileirao/main/brasileirao_serie_a.csv"
    else:
        url = f"https://www.football-data.co.uk/mmz4281/2425/{liga}.csv"
    
    try:
        df = pd.read_csv(url)
        if liga == 'BRA':
            df = df.rename(columns={'mandante': 'HomeTeam', 'visitante': 'AwayTeam', 'mandante_placar': 'FTHG', 'visitante_placar': 'FTAG', 'vencedor': 'FTR'})
        df['FTHG'] = pd.to_numeric(df['FTHG'], errors='coerce')
        df['FTAG'] = pd.to_numeric(df['FTAG'], errors='coerce')
        return df.dropna(subset=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])
    except:
        return pd.DataFrame()

def calcular_ia(home, away, df):
    h_m = df[df['HomeTeam'] == home].tail(8)
    a_m = df[df['AwayTeam'] == away].tail(8)
    if len(h_m) < 2 or len(a_m) < 2: return None
    
    xg_h, xg_a = h_m['FTHG'].mean(), a_m['FTAG'].mean()
    prob_h = poisson.pmf(np.arange(0, 5), xg_h)
    prob_a = poisson.pmf(np.arange(0, 5), xg_a)
    matrix = np.outer(prob_h, prob_a)
    
    win_h = np.sum(np.triu(matrix, 1)) * 100
    draw = np.trace(matrix) * 100
    win_a = np.sum(np.tril(matrix, -1)) * 100
    
    return {'v_casa': win_h, 'empate': draw, 'v_fora': win_a, 'xg_h': xg_h, 'xg_a': xg_a}

# --- CARREGAR LIGA ATUAL ---
liga_atual = st.session_state['liga_selecionada']
df = get_data(liga_atual)

if not df.empty:
    st.subheader(f"Analisando: {liga_atual} ⚽")
    
    teams = sorted(df['HomeTeam'].unique())
    col1, col2 = st.columns(2)
    t1 = col1.selectbox("Time da Casa", teams)
    t2 = col2.selectbox("Time de Fora", teams)
    
    if st.button("🔥 CALCULAR PROBABILIDADES"):
        res = calcular_ia(t1, t2, df)
        if res:
            st.markdown(f"""
            <div class="card-jogo">
                <h2 style='text-align:center;'>{t1} vs {t2}</h2>
                <p style='text-align:center;'>Expectativa de Gols: {res['xg_h']:.1f} x {res['xg_a']:.1f}</p>
            </div>
            """, unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Vitória Casa", f"{res['v_casa']:.1f}%")
            c2.metric("Empate", f"{res['empate']:.1f}%")
            c3.metric("Vitória Fora", f"{res['v_fora']:.1f}%")
            
            # Barras de Progresso Visuais
            st.write("Confiança da IA no Mandante:")
            st.progress(res['v_casa']/100)
            
            if res['v_casa'] > 60:
                st.success(f"💎 VALOR ENCONTRADO: Forte tendência de vitória para o {t1}")
            
    # --- SCANNER AUTOMÁTICO ---
    with st.expander("🔍 SCANNER DE HOJE (TOP 5)"):
        oportunidades = []
        for i in range(min(len(teams), 8)):
            r = calcular_ia(teams[i], teams[-i-1], df)
            if r and r['v_casa'] > 65:
                oportunidades.append([teams[i], teams[-i-1], f"{r['v_casa']:.1f}%"])
        
        if oportunidades:
            st.table(pd.DataFrame(oportunidades, columns=['Casa', 'Fora', 'Prob. Vitória']))
        else:
            st.info("Nenhuma aposta de alta confiança encontrada agora.")

else:
    st.error("Selecione uma liga nos botões laterais para carregar os dados.")

# --- RODAPÉ ---
st.markdown("---")
st.caption("Gestor IA Apostas © 2024 - Otimizado para Brasileirão e Ligas Europeias")
