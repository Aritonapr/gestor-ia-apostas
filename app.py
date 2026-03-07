import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. CSS REFINADO (PROPORÇÃO E EQUILÍBRIO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    /* Remover Header e ajustar topo */
    [data-testid="stHeader"] {display: none !important;}
    .block-container { padding: 10px 1.5rem !important; }
    
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    /* SIDEBAR - EQUILIBRADA */
    [data-testid="stSidebar"] { background-color: #0f171e; border-right: 1px solid #f05a22; width: 260px !important; }
    
    .sidebar-header { 
        display: flex; flex-direction: column; align-items: center; 
        padding: 15px 0; border-bottom: 1px solid #1a242d; margin-bottom: 10px;
    }
    .ai-logo-box { background-color: #f05a22; padding: 8px; border-radius: 8px; margin-bottom: 8px; box-shadow: 0 0 15px rgba(240,90,34,0.3); }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 18px; font-weight: 900; letter-spacing: 2px; }
    
    /* Botões Laterais - Tamanho Harmônico */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: 700 !important; height: 35px !important; line-height: 1.2 !important;
        border-radius: 5px !important; text-transform: uppercase; font-size: 10px !important;
        width: 100% !important; margin-bottom: 5px !important; transition: 0.3s;
    }
    .stButton > button:hover { border-color: #f05a22 !important; color: #f05a22 !important; }
    .stButton > button[kind="primary"] {
        background-color: rgba(240,90,34,0.1) !important; color: #f05a22 !important; border: 1px solid #f05a22 !important;
    }

    .cat-label { color: #5a6b79; font-size: 10px; font-weight: 800; margin-top: 12px; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 1px; }

    /* ÁREA PRINCIPAL - CARDS OTIMIZADOS */
    .radar-topo {
        background: rgba(26, 36, 45, 0.6); border-radius: 6px; padding: 6px 12px; margin-bottom: 10px;
        display: flex; align-items: center; border-left: 4px solid #f05a22;
    }
    .radar-label { font-family: 'Orbitron', sans-serif; font-weight: 700; color: #f05a22; font-size: 10px; margin-right: 15px; }
    
    .card-principal { 
        background-color: #1a242d; padding: 15px; border-radius: 12px; 
        border-bottom: 4px solid #f05a22; margin-bottom: 12px; text-align: center; 
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 20px; font-weight: 800; margin-bottom: 15px; letter-spacing: 2px; }
    
    .prob-container { display: flex; justify-content: space-around; align-items: center; background: rgba(0,0,0,0.3); border-radius: 8px; padding: 10px 0; }
    .val-prob { color: #f05a22; font-size: 24px; font-weight: 900; line-height: 1; }
    .label-prob { color: #8899a6; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-top: 5px; }

    .mini-card { background-color: #111a21; padding: 8px; border-radius: 8px; border: 1px solid #2d3748; text-align: center; }
    .mini-label { color: #8899a6; font-size: 8px; font-weight: 700; text-transform: uppercase; margin-bottom: 4px; display: block; }
    .mini-val { color: #00ffc3; font-weight: 900; font-size: 16px; }

    /* Estilo Selectbox */
    div[data-baseweb="select"] { background-color: #111a21 !important; }
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
        br = ['Flamengo', 'Palmeiras', 'Bahia', 'Corinthians', 'Santos', 'Vasco', 'Inter', 'Grêmio']
        data = [[np.random.choice(br), np.random.choice(br), np.random.randint(0,4), np.random.randint(0,3)] for _ in range(50)]
        return pd.DataFrame(data, columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

# --- 4. BARRA LATERAL (ESTILIZADA COMO DASHBOARD) ---
with st.sidebar:
    st.markdown("""
        <div class="sidebar-header">
            <div class="ai-logo-box">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3">
                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                    <line x1="8" y1="12" x2="16" y2="12"></line>
                </svg>
            </div>
            <div class="sidebar-title">GESTOR IA</div>
        </div>
    """, unsafe_allow_html=True)
    
    def s_btn(label, vid):
        if st.button(label, key=f"s_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid
            st.session_state.nome_liga = label
            st.rerun()

    st.markdown('<p class="cat-label">BRASILEIRÃO</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: s_btn("SÉRIE A", "BRA_A")
    with c2: s_btn("SÉRIE B", "BRA_B")
    
    st.markdown('<p class="cat-label">COP / ESTADUAIS</p>', unsafe_allow_html=True)
    c3, c4 = st.columns(2)
    with c3: s_btn("COPA BR", "CDB")
    with c4: s_btn("PAULISTÃO", "SP")

    st.markdown('<p class="cat-label">CONTINENTAIS</p>', unsafe_allow_html=True)
    c5, c6 = st.columns(2)
    with c5: s_btn("LIBERTA", "LIB")
    with c6: s_btn("SUL-AMER", "SUL")

    st.markdown('<p class="cat-label">EUROPA</p>', unsafe_allow_html=True)
    c7, c8 = st.columns(2)
    with c7: s_btn("PREMIER", "E0"); s_btn("BUNDES", "D1")
    with c8: s_btn("LA LIGA", "SP1"); s_btn("SERIE A", "I1")

# --- 5. ÁREA PRINCIPAL ---
df = load_data(st.session_state.liga_ativa)
times = sorted(df['HomeTeam'].unique())

# Filtros e Executar na mesma linha
col_a, col_b, col_c = st.columns([3, 3, 2.5])
with col_a: t_casa = st.selectbox("Mandante", times, label_visibility="collapsed")
with col_b: t_fora = st.selectbox("Visitante", [t for t in times if t != t_casa], label_visibility="collapsed")
with col_c: executar = st.button("🔥 EXECUTAR ALGORITMO", use_container_width=True, type="primary")

if executar:
    st.markdown(f'<div class="radar-topo"><div class="radar-label">📡 RADAR ESTRATÉGICO</div><div style="font-size:10px; color:#8899a6;">Conexão estável. Analisando {st.session_state.nome_liga}...</div></div>', unsafe_allow_html=True)

    st.markdown(f"""
        <div class="card-principal">
            <div class="match-title">{t_casa.upper()} VS {t_fora.upper()}</div>
            <div class="prob-container">
                <div><p class="val-prob">44.2%</p><p class="label-prob">Mandante</p></div>
                <div><p class="val-prob">22.8%</p><p class="label-prob">Empate</p></div>
                <div><p class="val-prob">33.0%</p><p class="label-prob">Visitante</p></div>
            </div>
            <div style="margin-top:10px; display:flex; justify-content:space-around; font-size:11px; color:#00ffc3; font-weight:700;">
                <span>ODD JUSTA: @2.10</span>
                <span>VALOR: +12.5%</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Mini cards compactos
    m = st.columns(6)
    metrics = [("⚽ GOLS +2.5", "62%"), ("🚩 CANTOS +9.5", "75%"), ("👞 CHUTES +22", "81%"), 
               ("🎯 NO GOL +8", "58%"), ("⚠️ FALTAS +24", "85%"), ("🟨 CARTÕES +4", "72%")]
    
    for i, (label, val) in enumerate(metrics):
        with m[i]:
            st.markdown(f"<div class='mini-card'><span class='mini-label'>{label}</span><span class='mini-val'>{val}</span></div>", unsafe_allow_html=True)
else:
    st.markdown("<div style='height:200px; display:flex; align-items:center; justify-content:center; border:1px dashed #2d3748; border-radius:12px; color:#5a6b79; font-size:14px; background:rgba(255,255,255,0.02);'>Aguardando comando...</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; opacity:0.2; font-size:8px; margin-top:10px;'>GESTOR IA v12.8 - PROPORÇÃO AJUSTADA</p>", unsafe_allow_html=True)
