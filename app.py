import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL BETANO (CSS MELHORADO) ---
st.markdown("""
    <style>
    /* Fundo principal */
    .main { background-color: #0b1218; color: #e4e6eb; }
    
    /* Barra Lateral */
    [data-testid="stSidebar"] { 
        background-color: #1a242d; 
        border-right: 2px solid #f05a22; 
        min-width: 300px !important;
    }

    /* Título do Cabeçalho */
    .header-container {
        background-color: #1a242d;
        padding: 25px;
        border-bottom: 4px solid #f05a22;
        text-align: center;
        border-radius: 0 0 20px 20px;
        margin-bottom: 30px;
    }
    .header-title { color: #f05a22; font-size: 32px; font-weight: 900; letter-spacing: 2px; text-transform: uppercase; }

    /* PADRONIZAÇÃO DOS BOTÕES (O QUE VOCÊ PEDIU) */
    .stButton > button {
        background-color: #26323e;
        color: #ffffff;
        border: 1px solid #313d49;
        font-weight: bold;
        text-transform: uppercase;
        
        /* Força todos os botões a serem iguais */
        width: 100% !important;
        height: 55px !important;
        display: block;
        margin-bottom: 12px !important;
        border-radius: 8px !important;
        font-size: 14px !important;
        transition: all 0.3s ease-in-out;
    }

    /* Efeito ao passar o mouse */
    .stButton > button:hover {
        border-color: #f05a22 !important;
        color: #f05a22 !important;
        background-color: #1a242d !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(240, 90, 34, 0.3);
    }

    /* Estilo dos Cards de Resultado */
    .card-resultado {
        background-color: #1a242d;
        padding: 25px;
        border-radius: 15px;
        border-left: 6px solid #f05a22;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        margin-top: 20px;
    }
    .metric-title { color: #8a949d; font-size: 14px; font-weight: bold; text-transform: uppercase; }
    .metric-value { color: #f05a22; font-size: 32px; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CABEÇALHO ---
st.markdown('<div class="header-container"><span class="header-title">GESTOR IA APOSTAS</span></div>', unsafe_allow_html=True)

# --- 4. LOGICA DE NAVEGAÇÃO ---
if 'liga_selecionada' not in st.session_state:
    st.session_state['liga_selecionada'] = 'BRA'

# --- 5. BARRA LATERAL (BOTÕES PADRONIZADOS) ---
with st.sidebar:
    st.markdown("<h3 style='text-align: center; color: #f05a22;'>🏆 CAMPEONATOS</h3>", unsafe_allow_html=True)
    
    # Criamos os botões. Como definimos width 100% no CSS, eles ficarão todos iguais.
    if st.button("🇧🇷 BRASILEIRAO SERIE A"): st.session_state['liga_selecionada'] = 'BRA'
    if st.button("🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE"): st.session_state['liga_selecionada'] = 'E0'
    if st.button("🇪🇸 LA LIGA ESPANHA"): st.session_state['liga_selecionada'] = 'SP1'
    if st.button("🇮🇹 SERIE A ITALIA"): st.session_state['liga_selecionada'] = 'I1'
    if st.button("🇩🇪 BUNDESLIGA"): st.session_state['liga_selecionada'] = 'D1'
    if st.button("🇫🇷 LIGUE 1 FRANCA"): st.session_state['liga_selecionada'] = 'F1'
    
    st.markdown("---")
    st.caption("Selecione a liga para carregar os times reais.")

# --- 6. FUNÇÃO DE DADOS ---
@st.cache_data(ttl=3600)
def load_liga(liga_id):
    try:
        if liga_id == 'BRA':
            url = "https://raw.githubusercontent.com/automacaobrasil/dataset-brasileirao/main/brasileirao_serie_a.csv"
            df = pd.read_csv(url)
            df = df.rename(columns={'mandante': 'HomeTeam', 'visitante': 'AwayTeam', 'mandante_placar': 'FTHG', 'visitante_placar': 'FTAG'})
        else:
            url = f"https://www.football-data.co.uk/mmz4281/2425/{liga_id}.csv"
            df = pd.read_csv(url)
        
        df['FTHG'] = pd.to_numeric(df['FTHG'], errors='coerce')
        df['FTAG'] = pd.to_numeric(df['FTAG'], errors='coerce')
        return df.dropna(subset=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])
    except:
        return pd.DataFrame()

# --- 7. PROCESSAMENTO IA ---
def calcular_probabilidades(t1, t2, df_liga):
    # Pega os últimos 8 jogos para ver a forma atual
    h_data = df_liga[df_liga['HomeTeam'] == t1].tail(8)
    a_data = df_liga[df_liga['AwayTeam'] == t2].tail(8)
    
    if len(h_data) < 2 or len(a_data) < 2: return None
    
    m_h, m_a = h_data['FTHG'].mean(), a_data['FTAG'].mean()
    p_h = poisson.pmf(np.arange(0, 6), m_h)
    p_a = poisson.pmf(np.arange(0, 6), m_a)
    m = np.outer(p_h, p_a)
    
    return {
        'casa': np.sum(np.triu(m, 1)) * 100,
        'empate': np.trace(m) * 100,
        'fora': np.sum(np.tril(m, -1)) * 100,
        'xg_h': m_h, 'xg_a': m_a
    }

# --- 8. ÁREA PRINCIPAL ---
liga_ativa = st.session_state['liga_selecionada']
df = load_liga(liga_ativa)

if not df.empty:
    st.markdown(f"### 📍 Analisando agora: <span style='color:#f05a22;'>{liga_ativa}</span>", unsafe_allow_html=True)
    
    times = sorted(df['HomeTeam'].unique())
    col_1, col_2 = st.columns(2)
    casa = col_1.selectbox("Time Mandante", times)
    fora = col_2.selectbox("Time Visitante", times)
    
    if st.button("🔥 CALCULAR ODDS DA IA"):
        res = calcular_probabilidades(casa, fora, df)
        if res:
            st.markdown(f"""
            <div class="card-resultado">
                <h2 style='text-align:center;'>{casa} vs {fora}</h2>
                <div style='display: flex; justify-content: space-around; text-align: center; margin-top: 20px;'>
                    <div><p class="metric-title">Vitória Casa</p><p class="metric-value">{res['casa']:.1f}%</p></div>
                    <div><p class="metric-title">Empate</p><p class="metric-value">{res['empate']:.1f}%</p></div>
                    <div><p class="metric-title">Vitória Fora</p><p class="metric-value">{res['fora']:.1f}%</p></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Barras Visuais
            st.write("")
            st.write(f"Força do Mandante ({casa}):")
            st.progress(res['casa'] / 100)
            
            if res['casa'] > 65:
                st.balloons()
                st.success(f"🚀 ENTRADA DE VALOR: A probabilidade de vitória do {casa} é muito alta!")
        else:
            st.warning("Dados insuficientes para gerar a probabilidade destes times.")
else:
    st.error("Erro ao carregar dados. Por favor, clique em um campeonato na esquerda.")

# --- 9. RODAPÉ ---
st.markdown("<br><hr><p style='text-align:center; color:#8a949d;'>GESTOR IA APOSTAS - Desenvolvido com Inteligência de Dados v2.0</p>", unsafe_allow_html=True)
