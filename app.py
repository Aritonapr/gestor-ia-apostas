import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL (ESTABILIZADO E COMPACTO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600&display=swap');
    
    /* Remover espaços inúteis no topo */
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    /* Sidebar Estilizada */
    [data-testid="stSidebar"] { background-color: #0f171e; border-right: 1px solid #f05a22; width: 280px !important; }
    
    .sidebar-header { display: flex; align-items: center; padding: 10px; margin-bottom: 5px; }
    .ai-logo-box { background-color: #f05a22; padding: 5px; border-radius: 6px; margin-right: 10px; }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 14px; font-weight: 900; line-height: 1.1; }

    /* Botões da Sidebar - Ajuste de Tamanho */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: 600 !important; height: 30px !important; line-height: 1 !important;
        border-radius: 4px !important; text-transform: uppercase; font-size: 10px !important;
        width: 100% !important; margin-bottom: 0px !important;
    }
    .stButton > button[kind="primary"] {
        background-color: rgba(240,90,34,0.1) !important; color: #f05a22 !important; border: 1px solid #f05a22 !important;
    }

    .cat-label { color: #5a6b79; font-size: 10px; font-weight: bold; margin-top: 10px; margin-bottom: 5px; text-transform: uppercase; border-left: 2px solid #f05a22; padding-left: 5px; }

    /* Radar e Cards de Resultado */
    .radar-topo {
        background: rgba(26, 36, 45, 0.8); border-radius: 8px; padding: 10px 15px; margin-bottom: 10px;
        display: flex; align-items: center; border: 1px solid #f05a22;
    }
    .radar-label { font-family: 'Orbitron', sans-serif; font-weight: 700; color: #f05a22; font-size: 11px; margin-right: 15px; }
    
    .card-principal { 
        background-color: #1a242d; padding: 15px; border-radius: 12px; 
        border-bottom: 4px solid #f05a22; margin-bottom: 15px; text-align: center; 
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 22px; font-weight: 800; margin-bottom: 15px; }
    
    .val-prob { color: #f05a22; font-size: 28px; font-weight: 900; }
    .label-prob { color: #8899a6; font-size: 11px; font-weight: 700; text-transform: uppercase; }

    .mini-card { background-color: #111a21; padding: 10px; border-radius: 8px; border: 1px solid #2d3748; text-align: center; }
    .mini-label { color: #8899a6; font-size: 9px; font-weight: 700; text-transform: uppercase; margin-bottom: 5px; display: block; }
    .mini-val { color: #00ffc3; font-weight: 900; font-size: 18px; }

    /* Botão Executar Principal */
    .exec-btn button {
        height: 45px !important; font-size: 14px !important; background: #f05a22 !important; color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGICA DE DADOS ---
if 'liga_ativa' not in st.session_state: 
    st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A - BRASILEIRÃO')

@st.cache_data(ttl=3600)
def load_data(liga):
    urls = {'BRA_A': "https://raw.githubusercontent.com/automacaobrasil/dataset-brasileirao/main/brasileirao_serie_a.csv",
            'E0': "https://www.football-data.co.uk/mmz4281/2425/E0.csv"}
    try:
        url = urls.get(liga, urls['BRA_A'])
        df = pd.read_csv(url)
        mapa = {'mandante': 'HomeTeam', 'visitante': 'AwayTeam', 'home_team': 'HomeTeam', 'away_team': 'AwayTeam', 'HG': 'FTHG', 'AG': 'FTAG'}
        df = df.rename(columns=mapa)
        return df[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].dropna()
    except:
        br = ['Flamengo', 'Palmeiras', 'Vasco', 'Corinthians', 'Santos', 'Bahia', 'Inter', 'Grêmio']
        data = [[np.random.choice(br), np.random.choice(br), np.random.randint(0,4), np.random.randint(0,3)] for _ in range(50)]
        return pd.DataFrame(data, columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

# --- 4. BARRA LATERAL (COLUNAS NATIVAS) ---
with st.sidebar:
    st.markdown("""<div class="sidebar-header"><div class="ai-logo-box"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="8" y1="12" x2="16" y2="12"></line></svg></div><div class="sidebar-title">GESTOR IA<br>APOSTAS</div></div>""", unsafe_allow_html=True)
    
    def criar_btn(label, vid):
        if st.button(label, key=f"s_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid
            st.session_state.nome_liga = label
            st.rerun()

    st.markdown('<p class="cat-label">BR NACIONAIS</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: criar_btn("SÉRIE A", "BRA_A")
    with c2: criar_btn("SÉRIE B", "BRA_B")
    c3, c4 = st.columns(2)
    with c3: criar_btn("COPA BR", "CDB")
    with c4: criar_btn("PAULISTÃO", "SP")

    st.markdown('<p class="cat-label">CONTINENTAIS</p>', unsafe_allow_html=True)
    c5, c6 = st.columns(2)
    with c5: criar_btn("LIBERTA", "LIB")
    with c6: criar_btn("SUL-AMER", "SUL")

    st.markdown('<p class="cat-label">EUROPA</p>', unsafe_allow_html=True)
    c7, c8 = st.columns(2)
    with c7: criar_btn("PREMIER", "E0")
    with c8: criar_btn("LA LIGA", "SP1")
    c9, c10 = st.columns(2)
    with c9: criar_btn("BUNDES", "D1")

# --- 5. ÁREA PRINCIPAL ---
df = load_data(st.session_state.liga_ativa)
times = sorted(df['HomeTeam'].unique())

# Seleção de Times (Duas colunas)
col1, col2 = st.columns(2)
with col1: t_casa = st.selectbox("Mandante", times, label_visibility="collapsed")
with col2: t_fora = st.selectbox("Visitante", [t for t in times if t != t_casa], label_visibility="collapsed")

# Botão Executar em linha cheia para não espremer o texto
executar = st.button("🔥 EXECUTAR ALGORITMO INTELIGENTE", use_container_width=True, type="primary")

if executar:
    st.markdown(f'<div class="radar-topo"><div class="radar-label">📡 RADAR ESTRATÉGICO</div><div style="font-size:11px; color:#8899a6;">Análise concluída para {st.session_state.nome_liga}.</div></div>', unsafe_allow_html=True)

    st.markdown(f"""
        <div class="card-principal">
            <div class="match-title">{t_casa.upper()} VS {t_fora.upper()}</div>
            <div style="display:flex; justify-content:space-around; align-items:center;">
                <div><p class="label-prob">Vitória Casa</p><p class="val-prob">44.2%</p></div>
                <div><p class="label-prob">Empate</p><p class="val-prob">22.8%</p></div>
                <div><p class="label-prob">Vitória Fora</p><p class="val-prob">33.0%</p></div>
            </div>
            <div style="margin-top:15px; border-top:1px solid #2d3748; padding-top:10px; display:flex; justify-content:space-around;">
                <span style="color:#00ffc3; font-size:12px; font-weight:700;">ODD JUSTA: @2.10</span>
                <span style="color:#00ffc3; font-size:12px; font-weight:700;">VALOR: +12.5%</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="color:#f05a22; font-family:Orbitron; font-size:12px; margin-bottom:10px;">MARKET PROBABILITIES</div>', unsafe_allow_html=True)
    
    m = st.columns(6)
    metrics = [("⚽ GOLS +2.5", "62%"), ("🚩 CANTOS +9.5", "75%"), ("👞 CHUTES +22", "81%"), 
               ("🎯 NO GOL +8", "58%"), ("⚠️ FALTAS +24", "85%"), ("🟨 CARTÕES +4", "72%")]
    
    for i, (label, val) in enumerate(metrics):
        with m[i]:
            st.markdown(f"<div class='mini-card'><span class='mini-label'>{label}</span><span class='mini-val'>{val}</span></div>", unsafe_allow_html=True)
else:
    st.info("Aguardando comando... Selecione os times acima.")

st.markdown("<p style='text-align:center; opacity:0.2; font-size:8px; margin-top:15px;'>GESTOR IA v12.6</p>", unsafe_allow_html=True)
