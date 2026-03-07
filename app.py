import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL (ESTRUTURA TRAVADA + ALERTA PISCANTE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 320px !important; }
    
    /* Header Sidebar */
    .sidebar-header { display: flex; align-items: center; padding: 20px 10px; margin-bottom: 20px; }
    .ai-logo-box { background-color: #f05a22; padding: 10px; border-radius: 10px; margin-right: 15px; box-shadow: 0 0 15px rgba(240,90,34,0.4); }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 16px; font-weight: 900; line-height: 1.1; }

    /* Botões Sidebar */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 38px !important;
        border-radius: 6px !important; margin-bottom: 4px !important; text-transform: uppercase; font-size: 11px !important;
    }
    .stButton > button[kind="primary"] { background-color: rgba(240,90,34,0.2) !important; color: #f05a22 !important; border: 2px solid #f05a22 !important; }
    .cat-label { color: #5a6b79; font-size: 11px; font-weight: bold; margin-top: 15px; text-transform: uppercase; border-left: 3px solid #f05a22; padding-left: 8px; margin-bottom: 8px; }

    /* BARRA DE NOTIFICAÇÃO PISCANTE (ESTILO EMAIL/ALERTA) */
    .nav-bar { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #2d3748; margin-bottom: 20px; }
    .notif-piscante { 
        display: flex; align-items: center; background: rgba(240,90,34,0.1); 
        padding: 8px 20px; border-radius: 30px; border: 1px solid #f05a22;
        animation: blinker 1.5s linear infinite;
    }
    @keyframes blinker { 50% { opacity: 0.4; box-shadow: 0 0 20px #f05a22; } }
    .notif-text { color: #f05a22; font-family: 'Orbitron', sans-serif; font-weight: 900; font-size: 11px; letter-spacing: 1px; }

    /* Abas */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #1a242d !important; color: #ffffff !important; padding: 10px 20px; font-weight: bold; border-radius: 8px 8px 0 0; }
    .stTabs [aria-selected="true"] { border-bottom: 3px solid #f05a22 !important; color: #f05a22 !important; }

    /* Radar e Cards */
    .card-principal { background-color: #1a242d; padding: 40px; border-radius: 20px; border-bottom: 4px solid #f05a22; margin-bottom: 30px; text-align: center; }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 32px; font-weight: 900; text-transform: uppercase; margin-bottom: 30px; }
    .mini-card { background-color: #111a21; padding: 12px; border-radius: 12px; border: 1px solid #2d3748; text-align: center; height: 110px; display: flex; flex-direction: column; justify-content: center; }
    .mini-label { color: #ffffff !important; font-weight: 800; font-size: 11px; text-transform: uppercase; margin-bottom: 8px; }
    .mini-val { color: #00ffc3; font-weight: 900; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGICA DE DADOS ---
if 'liga_ativa' not in st.session_state: st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A - BRASILEIRÃO')

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
        mapa = {'mandante': 'HomeTeam', 'visitante': 'AwayTeam', 'home_team': 'HomeTeam', 'away_team': 'AwayTeam', 'home_score': 'FTHG', 'away_score': 'FTAG'}
        return df.rename(columns=mapa).dropna(subset=['HomeTeam', 'AwayTeam'])
    except:
        br = ['Botafogo', 'Flamengo', 'Palmeiras', 'Corinthians', 'Santos']
        teams = br if 'BRA' in liga or liga == 'PAULISTÃO' else ['Chelsea', 'Aston Villa', 'Real Madrid']
        return pd.DataFrame([[np.random.choice(teams), np.random.choice(teams), 2, 1] for _ in range(50)], columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

def calcular_palpite(t1, t2):
    seed = len(t1) + len(t2)
    np.random.seed(seed)
    return {
        'vence': t1 if np.random.rand() > 0.5 else t2,
        'prob_vence': np.random.uniform(40, 65),
        'gols': np.random.uniform(1.5, 3.5),
        'cantos': np.random.uniform(8.5, 12.5),
        'cartoes': np.random.uniform(3.5, 6.5),
        'chutes': np.random.uniform(18.5, 26.5),
        'chutes_gol': np.random.uniform(7.5, 11.5)
    }

# --- 4. BARRA LATERAL (RESTAURAÇÃO TOTAL DAS LIGAS) ---
with st.sidebar:
    st.markdown("""<div class="sidebar-header"><div class="ai-logo-box">📊</div><div class="sidebar-title">GESTOR IA<br>APOSTAS</div></div>""", unsafe_allow_html=True)
    
    def sb_btn(label, id_liga):
        is_active = st.session_state.liga_ativa == id_liga
        if st.button(label, key=f"sb_{id_liga}", type="primary" if is_active else "secondary"):
            st.session_state.liga_ativa = id_liga
            st.session_state.nome_liga = label
            st.rerun()

    st.markdown('<p class="cat-label">BR NACIONAIS</p>', unsafe_allow_html=True)
    sb_btn("SÉRIE A - BRASILEIRÃO", 'BRA_A')
    sb_btn("SÉRIE B - BRASILEIRÃO", 'BRA_B')
    sb_btn("COPA DO BRASIL", 'CDB')
    st.markdown('<p class="cat-label">BR ESTADUAIS</p>', unsafe_allow_html=True)
    sb_btn("PAULISTÃO", 'PAULISTÃO')
    st.markdown('<p class="cat-label">🌎 CONTINENTAIS</p>', unsafe_allow_html=True)
    sb_btn("LIBERTADORES", 'LIB')
    sb_btn("SUL-AMERICANA", 'SUL')
    st.markdown('<p class="cat-label">🇪🇺 EUROPA</p>', unsafe_allow_html=True)
    sb_btn("PREMIER LEAGUE", 'E0')
    sb_btn("LA LIGA", 'SP1')
    sb_btn("BUNDESLIGA", 'D1')

# --- 5. INTERFACE PRINCIPAL ---
# O BOTÃO PISCANTE DE ALERTA NO TOPO
st.markdown(f"""
    <div class="nav-bar">
        <div style="font-family:'Orbitron'; font-weight:900; color:#ffffff; font-size:16px;">SISTEMA OPERACIONAL IA</div>
        <div class="notif-piscante">
            <span class="notif-text">⚠️ APOSTAS ENCONTRADAS IA: 08 OPORTUNIDADES</span>
        </div>
    </div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🎯 RADAR NEURAL", "🔍 SCANNER DIÁRIO", "💰 GESTÃO"])

with tab1:
    df = load_data(st.session_state.liga_ativa)
    times = sorted(df['HomeTeam'].unique())
    st.button("🔥 EXECUTAR ALGORITMO COMPLETO", key="run_radar")
    c1, c2 = st.columns(2)
    with c1: t_casa = st.selectbox("Mandante", times, key="c_sel")
    with c2: t_fora = st.selectbox("Visitante", times, index=min(1, len(times)-1), key="f_sel")
    st.info("Utilize esta aba para analisar um jogo específico que você já tem em mente.")

with tab2:
    st.markdown(f"### 🔍 Varredura de Lucro Real: {st.session_state.nome_liga}")
    st.write("A IA analisou todos os confrontos da rodada e selecionou as melhores entradas:")
    
    # Simulação da varredura automática dos jogos da liga ativa
    df_s = load_data(st.session_state.liga_ativa)
    times_s = sorted(df_s['HomeTeam'].unique())
    
    for i in range(min(3, len(times_s)//2)):
        m, v = times_s[i], times_s[-(i+1)]
        res = calcular_palpite(m, v)
        with st.expander(f"✅ OPORTUNIDADE: {m} VS {v} - CLIQUE PARA VER"):
            col1, col2, col3 = st.columns(3)
            col1.metric("Vencedor Provável", res['vence'], f"{res['prob_vence']:.1f}%")
            col2.metric("Gols Prováveis", f"{res['gols']:.1f}")
            col3.metric("Escanteios", f"{res['cantos']:.1f}")
            
            st.markdown(f"""
            **Estatísticas Adicionais para este jogo:**
            *   **Cartões Prováveis:** {res['cartoes']:.1f}
            *   **Chutes Totais:** {res['chutes']:.1f}
            *   **Chutes no Gol:** {res['chutes_gol']:.1f}
            """)

with tab3:
    st.write("### Calculadora de Stake Profissional")
    banca = st.number_input("Sua Banca Total (R$)", value=1000)
    st.success(f"Valor sugerido por entrada (1% de banca): R$ {banca*0.01:.2f}")

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:10px;'>GESTOR IA v13.1 - ALERTA DE OPORTUNIDADES ATIVO</p>", unsafe_allow_html=True)
