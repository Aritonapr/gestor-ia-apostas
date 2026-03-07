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
    
    .header-container {
        background-color: #1a242d; padding: 25px; border-bottom: 4px solid #f05a22;
        text-align: center; border-radius: 0 0 20px 20px; margin-bottom: 30px;
    }
    .header-title { color: #f05a22; font-size: 32px; font-weight: 900; text-transform: uppercase; }

    /* BOTÕES PADRONIZADOS */
    .stButton > button {
        background-color: #26323e; color: white; border: 1px solid #313d49;
        font-weight: bold; width: 100% !important; height: 50px !important;
        border-radius: 8px !important; margin-bottom: 8px; transition: 0.3s;
        text-transform: uppercase; font-size: 13px;
    }
    .stButton > button:hover { border-color: #f05a22; color: #f05a22; background-color: #1a242d; }
    
    .card-analise {
        background-color: #1a242d; padding: 25px; border-radius: 15px;
        border-left: 6px solid #f05a22; box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }
    .metric-val { color: #f05a22; font-size: 30px; font-weight: bold; }
    .placar-box { background: #26323e; padding: 10px; border-radius: 5px; border: 1px solid #f05a22; font-size: 20px; font-weight: bold; text-align: center; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CABEÇALHO ---
st.markdown('<div class="header-container"><span class="header-title">GESTOR IA APOSTAS</span></div>', unsafe_allow_html=True)

# --- 4. CONTROLE DE NAVEGAÇÃO ---
if 'categoria' not in st.session_state: st.session_state['categoria'] = None
if 'liga_id' not in st.session_state: st.session_state['liga_id'] = None

# --- 5. BARRA LATERAL (MENU ESTRUTURADO) ---
with st.sidebar:
    st.markdown("<h3 style='text-align:center; color:#f05a22;'>🏁 CATEGORIAS</h3>", unsafe_allow_html=True)
    
    # Botões de Categoria
    if st.button("🇧🇷 CAMPEONATOS BRASILEIROS"): st.session_state['categoria'] = 'BRA'
    if st.button("🇪🇺 LIGAS EUROPEIAS"): st.session_state['categoria'] = 'EUR'
    if st.button("🏆 COPAS E OUTROS"): st.session_state['categoria'] = 'COP'

    st.markdown("---")

    # SUBMENU BRASIL
    if st.session_state['categoria'] == 'BRA':
        st.markdown("<p style='text-align:center; color:#8a949d;'>Selecione a Liga Brasileira</p>", unsafe_allow_html=True)
        if st.button("BRASILEIRÃO SÉRIE A"): st.session_state['liga_id'] = 'BRA_A'
        if st.button("BRASILEIRÃO SÉRIE B"): st.session_state['liga_id'] = 'BRA_B'
        if st.button("CAMPEONATO PAULISTA"): st.session_state['liga_id'] = 'PAULISTA'
        if st.button("CAMPEONATO CARIOCA"): st.session_state['liga_id'] = 'CARIOCA'

    # SUBMENU EUROPA
    elif st.session_state['categoria'] == 'EUR':
        st.markdown("<p style='text-align:center; color:#8a949d;'>Selecione a Liga Europeia</p>", unsafe_allow_html=True)
        if st.button("PREMIER LEAGUE"): st.session_state['liga_id'] = 'E0'
        if st.button("LA LIGA"): st.session_state['liga_id'] = 'SP1'
        if st.button("BUNDESLIGA"): st.session_state['liga_id'] = 'D1'

    # SUBMENU COPAS
    elif st.session_state['categoria'] == 'COP':
        st.markdown("<p style='text-align:center; color:#8a949d;'>Torneios Eliminatórios</p>", unsafe_allow_html=True)
        if st.button("COPA DO BRASIL"): st.session_state['liga_id'] = 'CDB'

# --- 6. SUPER ENGINE DE DADOS (COM TRADUTOR) ---
@st.cache_data(ttl=3600)
def load_data(liga):
    # Dicionário de URLs estáveis
    urls = {
        'BRA_A': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/brasileirao_serie_a.csv",
        'BRA_B': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/brasileirao_serie_b.csv",
        'PAULISTA': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/campeonato-paulista.csv",
        'CARIOCA': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/campeonato-carioca.csv",
        'CDB': "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/copa-do-brasil.csv"
    }
    
    try:
        if liga in urls:
            url = urls[liga]
        else:
            url = f"https://www.football-data.co.uk/mmz4281/2425/{liga}.csv"
        
        df = pd.read_csv(url)
        
        # --- TRADUTOR DE COLUNAS (O SEGREDO PARA NÃO DAR ERRO) ---
        col_map = {
            'mandante': 'HomeTeam', 'visitante': 'AwayTeam', 
            'home_team': 'HomeTeam', 'away_team': 'AwayTeam',
            'home_score': 'FTHG', 'away_score': 'FTAG',
            'mandante_placar': 'FTHG', 'visitante_placar': 'FTAG',
            'vencedor': 'FTR', 'result': 'FTR'
        }
        df = df.rename(columns=col_map)
        
        # Garante que as colunas essenciais existem e são numéricas
        df['FTHG'] = pd.to_numeric(df['FTHG'], errors='coerce')
        df['FTAG'] = pd.to_numeric(df['FTAG'], errors='coerce')
        return df.dropna(subset=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])
    except:
        return pd.DataFrame()

# --- 7. CÁLCULO IA AVANÇADO ---
def analisar_partida(t1, t2, df_liga):
    h_matches = df_liga[df_liga['HomeTeam'] == t1].tail(10)
    a_matches = df_liga[df_liga['AwayTeam'] == t2].tail(10)
    
    if len(h_matches) < 2 or len(a_matches) < 2: return None
    
    # Médias de Gols
    m_h, m_a = h_matches['FTHG'].mean(), a_matches['FTAG'].mean()
    
    # Distribuição de Poisson
    prob_h = poisson.pmf(np.arange(0, 5), m_h)
    prob_a = poisson.pmf(np.arange(0, 5), m_a)
    matrix = np.outer(prob_h, prob_a)
    
    # Placar Provável (Maior valor na matriz)
    placar = np.unravel_index(np.argmax(matrix), matrix.shape)
    
    return {
        'casa': np.sum(np.triu(matrix, 1)) * 100,
        'empate': np.trace(matrix) * 100,
        'fora': np.sum(np.tril(matrix, -1)) * 100,
        'placar': f"{placar[0]} x {placar[1]}",
        'xg_h': m_h, 'xg_a': m_a
    }

# --- 8. ÁREA DE ANÁLISE ---
if st.session_state['liga_id']:
    liga_sel = st.session_state['liga_id']
    df = load_data(liga_sel)
    
    if not df.empty:
        st.markdown(f"### 📍 Analisando agora: <span style='color:#f05a22;'>{liga_sel}</span>", unsafe_allow_html=True)
        
        times = sorted(df['HomeTeam'].unique())
        c1, c2 = st.columns(2)
        casa = c1.selectbox("Selecione o Mandante", times)
        fora = c2.selectbox("Selecione o Visitante", times)
        
        if st.button("🚀 EXECUTAR ANÁLISE DA IA"):
            res = analisar_partida(casa, fora, df)
            if res:
                st.markdown(f"""
                <div class="card-analise">
                    <h2 style='text-align:center;'>{casa} vs {fora}</h2>
                    <div style='display:flex; justify-content:space-around; text-align:center; margin-top:20px;'>
                        <div><p>Vitória Casa</p><p class="metric-val">{res['casa']:.1f}%</p></div>
                        <div><p>Empate</p><p class="metric-val">{res['empate']:.1f}%</p></div>
                        <div><p>Vitória Fora</p><p class="metric-val">{res['fora']:.1f}%</p></div>
                    </div>
                    <div style='margin-top:20px; display:flex; flex-direction:column; align-items:center;'>
                        <p>Placar mais Provável</p>
                        <div class="placar-box">{res['placar']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Barra de Probabilidade
                st.write("")
                st.write(f"Força ofensiva estimada: {res['xg_h']:.2f} (Casa) vs {res['xg_a']:.2f} (Fora)")
                st.progress(res['casa'] / 100)
            else:
                st.warning("A IA precisa de pelo menos 2 jogos históricos de cada time para analisar.")
    else:
        st.error("Dados deste campeonato ainda não disponíveis ou em atualização.")
else:
    st.info("👋 Bem-vindo! Selecione uma CATEGORIA na barra lateral para começar suas análises.")

# --- 9. RODAPÉ ---
st.markdown("<br><hr><p style='text-align:center; opacity:0.5;'>Gestor IA Apostas - Módulo Brasil Atualizado 2024</p>", unsafe_allow_html=True)
