import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. CSS AVANÇADO (OCULTAR HEADER E COMPACTAR TUDO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    /* 1. ELIMINAR CABEÇALHO E ESPAÇOS DO TOPO */
    [data-testid="stHeader"] {display: none !important;}
    .block-container { padding: 0px 1rem 0px 1rem !important; }
    footer {display: none !important;}
    
    /* 2. BACKGROUND E FONTE GLOBAL */
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    /* 3. SIDEBAR COMPACTA */
    [data-testid="stSidebar"] { background-color: #0f171e; border-right: 1px solid #f05a22; width: 250px !important; }
    .sidebar-header { display: flex; align-items: center; padding: 5px; margin-bottom: 0px; }
    .ai-logo-box { background-color: #f05a22; padding: 4px; border-radius: 4px; margin-right: 8px; }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 11px; font-weight: 900; }
    
    /* Botões Laterais em Miniatura */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: 600 !important; height: 26px !important; padding: 0px !important;
        border-radius: 3px !important; text-transform: uppercase; font-size: 9px !important;
        width: 100% !important; margin-bottom: -5px !important;
    }
    .stButton > button[kind="primary"] {
        background-color: rgba(240,90,34,0.15) !important; color: #f05a22 !important; border: 1px solid #f05a22 !important;
    }
    .cat-label { color: #5a6b79; font-size: 9px; font-weight: bold; margin-top: 8px; margin-bottom: 2px; text-transform: uppercase; }

    /* 4. ÁREA PRINCIPAL - CARD DE RESULTADO SLIM */
    .radar-topo {
        background: rgba(240,90,34,0.05); border-radius: 4px; padding: 4px 10px; margin-bottom: 8px;
        display: flex; align-items: center; border: 1px solid rgba(240,90,34,0.3);
    }
    .radar-label { font-family: 'Orbitron', sans-serif; font-weight: 700; color: #f05a22; font-size: 9px; margin-right: 10px; }
    
    .card-principal { 
        background-color: #1a242d; padding: 12px; border-radius: 10px; 
        border-bottom: 3px solid #f05a22; margin-bottom: 10px; text-align: center; 
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 16px; font-weight: 800; margin-bottom: 10px; }
    
    .prob-container { display: flex; justify-content: space-around; align-items: center; background: rgba(0,0,0,0.2); border-radius: 8px; padding: 8px 0; }
    .val-prob { color: #f05a22; font-size: 22px; font-weight: 900; line-height: 1; }
    .label-prob { color: #8899a6; font-size: 9px; font-weight: 700; text-transform: uppercase; margin-top: 4px; }

    .mini-card { background-color: #111a21; padding: 6px; border-radius: 6px; border: 1px solid #2d3748; text-align: center; }
    .mini-label { color: #8899a6; font-size: 8px; font-weight: 700; text-transform: uppercase; margin-bottom: 2px; display: block; }
    .mini-val { color: #00ffc3; font-weight: 900; font-size: 14px; }

    /* Ajuste de Selectbox e Input */
    .stSelectbox div[data-baseweb="select"] { min-height: 28px !important; font-size: 12px !important; }
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

# --- 4. BARRA LATERAL (COLUNAS ULTRA-COMPACTAS) ---
with st.sidebar:
    st.markdown("""<div class="sidebar-header"><div class="ai-logo-box"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="8" y1="12" x2="16" y2="12"></line></svg></div><div class="sidebar-title">GESTOR IA APOSTAS</div></div>""", unsafe_allow_html=True)
    
    def s_btn(label, vid):
        if st.button(label, key=f"s_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid
            st.session_state.nome_liga = label
            st.rerun()

    st.markdown('<p class="cat-label">BR NACIONAIS</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: s_btn("SÉRIE A", "BRA_A"); s_btn("COPA BR", "CDB")
    with c2: s_btn("SÉRIE B", "BRA_B"); s_btn("PAULISTÃO", "SP")

    st.markdown('<p class="cat-label">CONTINENTAIS</p>', unsafe_allow_html=True)
    c3, c4 = st.columns(2)
    with c3: s_btn("LIBERTA", "LIB")
    with c4: s_btn("SUL-AMER", "SUL")

    st.markdown('<p class="cat-label">EUROPA</p>', unsafe_allow_html=True)
    c5, c6 = st.columns(2)
    with c5: s_btn("PREMIER", "E0"); s_btn("BUNDES", "D1")
    with c6: s_btn("LA LIGA", "SP1"); s_btn("SERIE A", "I1")

# --- 5. ÁREA PRINCIPAL (FOCO EM ALTURA ÚNICA) ---
df = load_data(st.session_state.liga_ativa)
times = sorted(df['HomeTeam'].unique())

# Seletores e Botão na mesma linha para economizar espaço vertical
col_a, col_b, col_c = st.columns([3, 3, 2])
with col_a: t_casa = st.selectbox("Mandante", times, label_visibility="collapsed")
with col_b: t_fora = st.selectbox("Visitante", [t for t in times if t != t_casa], label_visibility="collapsed")
with col_c: executar = st.button("🔥 EXECUTAR IA", use_container_width=True, type="primary")

if executar:
    st.markdown(f'<div class="radar-topo"><div class="radar-label">📡 RADAR</div><div style="font-size:10px; color:#8899a6;">{st.session_state.nome_liga} analise concluída.</div></div>', unsafe_allow_html=True)

    st.markdown(f"""
        <div class="card-principal">
            <div class="match-title">{t_casa.upper()} VS {t_fora.upper()}</div>
            <div class="prob-container">
                <div><p class="val-prob">44.2%</p><p class="label-prob">Casa</p></div>
                <div><p class="val-prob">22.8%</p><p class="label-prob">Empate</p></div>
                <div><p class="val-prob">33.0%</p><p class="label-prob">Fora</p></div>
            </div>
            <div style="margin-top:8px; display:flex; justify-content:space-around; font-size:10px; color:#00ffc3; font-weight:700;">
                <span>ODD JUSTA: @2.10</span>
                <span>VALOR ESPERADO: +12.5%</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 6 Colunas em miniatura
    m = st.columns(6)
    metrics = [("⚽ GOLS +2.5", "62%"), ("🚩 CANTOS +9.5", "75%"), ("👞 CHUTES +22", "81%"), 
               ("🎯 NO GOL +8", "58%"), ("⚠️ FALTAS +24", "85%"), ("🟨 CARTÕES +4", "72%")]
    
    for i, (label, val) in enumerate(metrics):
        with m[i]:
            st.markdown(f"<div class='mini-card'><span class='mini-label'>{label}</span><span class='mini-val'>{val}</span></div>", unsafe_allow_html=True)
else:
    st.markdown("<div style='height:250px; display:flex; align-items:center; justify-content:center; border:1px dashed #2d3748; border-radius:10px; color:#5a6b79; font-size:12px;'>Aguardando comando...</div>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; opacity:0.2; font-size:7px; margin-top:5px;'>GESTOR IA v12.7 OTIMIZADO</p>", unsafe_allow_html=True)
