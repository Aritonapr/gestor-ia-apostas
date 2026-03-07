import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA - ELITE", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL BETANO (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #0b1218; color: #e4e6eb; }
    [data-testid="stSidebar"] { background-color: #1a242d; border-right: 2px solid #f05a22; min-width: 300px; }
    
    .header-container {
        background-color: #1a242d; padding: 25px; border-bottom: 4px solid #f05a22;
        text-align: center; border-radius: 0 0 20px 20px; margin-bottom: 30px;
    }
    .header-title { color: #f05a22; font-size: 32px; font-weight: 900; text-transform: uppercase; }

    /* BOTÕES PADRONIZADOS */
    .stButton > button {
        background-color: #26323e; color: white; border: 1px solid #313d49;
        font-weight: bold; width: 100% !important; height: 50px !important;
        border-radius: 8px !important; margin-bottom: 10px; transition: 0.3s;
    }
    .stButton > button:hover { border-color: #f05a22; color: #f05a22; background-color: #1a242d; }
    
    .card-analise {
        background-color: #1a242d; padding: 25px; border-radius: 15px;
        border-left: 6px solid #f05a22; box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }
    .metric-val { color: #f05a22; font-size: 30px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CABEÇALHO ---
st.markdown('<div class="header-container"><span class="header-title">GESTOR IA APOSTAS</span></div>', unsafe_allow_html=True)

# --- 4. GERENCIAMENTO DE NAVEGAÇÃO ---
if 'categoria' not in st.session_state:
    st.session_state['categoria'] = None
if 'liga_id' not in st.session_state:
    st.session_state['liga_id'] = None

# --- 5. BARRA LATERAL (MENU POR CATEGORIAS) ---
with st.sidebar:
    st.markdown("<h3 style='text-align:center; color:#f05a22;'>🏁 CATEGORIAS</h3>", unsafe_allow_html=True)
    
    col_br, col_eu = st.columns(2)
    if col_br.button("🇧🇷 BRASIL"):
        st.session_state['categoria'] = 'BRA'
    if col_eu.button("🇪🇺 EUROPA"):
        st.session_state['categoria'] = 'EUR'

    st.markdown("---")

    # SUBMENU BRASIL
    if st.session_state['categoria'] == 'BRA':
        st.markdown("<p style='text-align:center;'>Ligas Brasileiras</p>", unsafe_allow_html=True)
        if st.button("SERIE A"): st.session_state['liga_id'] = 'BRA_A'
        if st.button("SERIE B"): st.session_state['liga_id'] = 'BRA_B'

    # SUBMENU EUROPA
    elif st.session_state['categoria'] == 'EUR':
        st.markdown("<p style='text-align:center;'>Ligas Europeias</p>", unsafe_allow_html=True)
        if st.button("PREMIER LEAGUE"): st.session_state['liga_id'] = 'E0'
        if st.button("LA LIGA"): st.session_state['liga_id'] = 'SP1'
        if st.button("SERIE A (ITÁLIA)"): st.session_state['liga_id'] = 'I1'
        if st.button("BUNDESLIGA"): st.session_state['liga_id'] = 'D1'

# --- 6. ENGINE DE DADOS ---
@st.cache_data(ttl=3600)
def load_data(liga):
    try:
        if liga == 'BRA_A':
            # Nova fonte estável para Brasileirão Série A
            url = "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/brasileirao_serie_a.csv"
            df = pd.read_csv(url)
            # Mapeamento específico para este arquivo
            df = df.rename(columns={'home_team': 'HomeTeam', 'away_team': 'AwayTeam', 'home_score': 'FTHG', 'away_score': 'FTAG'})
        elif liga == 'BRA_B':
            # Exemplo Série B (pode ser ajustado se tiver o link direto)
            st.warning("Dados da Série B em fase de carregamento...")
            return pd.DataFrame()
        else:
            url = f"https://www.football-data.co.uk/mmz4281/2425/{liga}.csv"
            df = pd.read_csv(url)
        
        df['FTHG'] = pd.to_numeric(df['FTHG'], errors='coerce')
        df['FTAG'] = pd.to_numeric(df['FTAG'], errors='coerce')
        return df.dropna(subset=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])
    except:
        return pd.DataFrame()

# --- 7. CÁLCULO IA ---
def calcular_odds(t1, t2, df_liga):
    # Analisa o histórico recente dos times
    h_data = df_liga[df_liga['HomeTeam'] == t1].tail(10)
    a_data = df_liga[df_liga['AwayTeam'] == t2].tail(10)
    if len(h_data) < 2 or len(a_data) < 2: return None
    
    m_h, m_a = h_data['FTHG'].mean(), a_data['FTAG'].mean()
    p_h = poisson.pmf(np.arange(0, 6), m_h)
    p_a = poisson.pmf(np.arange(0, 6), m_a)
    matrix = np.outer(p_h, p_a)
    
    return {
        'casa': np.sum(np.triu(matrix, 1)) * 100,
        'empate': np.trace(matrix) * 100,
        'fora': np.sum(np.tril(matrix, -1)) * 100
    }

# --- 8. ÁREA PRINCIPAL ---
if st.session_state['liga_id']:
    df = load_data(st.session_state['liga_id'])
    
    if not df.empty:
        st.markdown(f"### 📍 Campeonato Selecionado: <span style='color:#f05a22;'>{st.session_state['liga_id']}</span>", unsafe_allow_html=True)
        
        times = sorted(df['HomeTeam'].unique())
        c1, c2 = st.columns(2)
        casa = c1.selectbox("Time Mandante", times)
        fora = c2.selectbox("Time Visitante", times)
        
        if st.button("🔥 ANALISAR PARTIDA"):
            res = calcular_odds(casa, fora, df)
            if res:
                st.markdown(f"""
                <div class="card-analise">
                    <h2 style='text-align:center;'>{casa} vs {fora}</h2>
                    <div style='display:flex; justify-content:space-around; text-align:center; margin-top:20px;'>
                        <div><p>Vitoria Casa</p><p class="metric-val">{res['casa']:.1f}%</p></div>
                        <div><p>Empate</p><p class="metric-val">{res['empate']:.1f}%</p></div>
                        <div><p>Vitoria Fora</p><p class="metric-val">{res['fora']:.1f}%</p></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if res['casa'] > 60:
                    st.success(f"💎 DICA: O {casa} possui grande vantagem estatística!")
            else:
                st.info("Dados insuficientes para calcular a probabilidade deste confronto.")
    else:
        st.error("Erro ao carregar os dados desta liga. Tente outra opção.")
else:
    st.info("👋 Bem-vindo! Selecione uma CATEGORIA na barra lateral (Brasil ou Europa) para começar.")

# --- 9. RODAPÉ ---
st.markdown("<br><hr><p style='text-align:center; opacity:0.6;'>Gestor IA Aposta - Sistema de Elite v3.0</p>", unsafe_allow_html=True)
