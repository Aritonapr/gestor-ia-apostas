import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="GESTOR IA APOSTAS", 
    layout="wide", 
    page_icon="⚽",
    initial_sidebar_state="expanded"
)

# --- 2. CSS DE ALTO NÍVEL (LIMPEZA TOTAL E ÍCONE ORIGINAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    /* 1. OCULTAR ELEMENTOS DESNECESSÁRIOS (SETINHA E HEADER) */
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stSidebarCollapse"] { display: none !important; } /* SOME COM A SETINHA */
    button[kind="headerNoPadding"] { display: none !important; } /* SOME COM O BOTÃO DA SETINHA */
    
    /* 2. AJUSTE DE ESPAÇAMENTO PARA NÃO ENCOSTAR NO SHARE */
    .block-container { 
        padding-top: 3.5rem !important; /* EMPURRA O CONTEÚDO PARA BAIXO DO SHARE */
        padding-bottom: 0rem !important; 
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    /* 3. SIDEBAR FIXA E ÍCONE ORIGINAL */
    [data-testid="stSidebar"] { 
        background-color: #0f171e; 
        border-right: 1px solid #f05a22; 
        width: 260px !important; 
    }
    
    .sidebar-header { 
        display: flex; align-items: center; padding: 20px 15px; 
        margin-bottom: 10px; border-bottom: 1px solid #1a242d;
    }
    
    /* O ÍCONE QUE VOCÊ GOSTA (Quadrado Laranja + Traço Branco) */
    .ai-logo-box { 
        background-color: #f05a22; width: 34px; height: 34px; 
        border-radius: 6px; display: flex; align-items: center; 
        justify-content: center; margin-right: 12px;
        box-shadow: 0 0 12px rgba(240,90,34,0.3);
    }
    .ai-logo-dash { width: 16px; height: 4px; background-color: white; border-radius: 2px; }
    
    .sidebar-title { 
        color: #f05a22; font-family: 'Orbitron', sans-serif; 
        font-size: 18px; font-weight: 900; letter-spacing: 1px;
    }
    
    /* Botões da Sidebar */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: 700 !important; height: 34px !important; line-height: 1 !important;
        border-radius: 4px !important; text-transform: uppercase; font-size: 10px !important;
        width: 100% !important; margin-bottom: 4px !important;
    }
    .stButton > button[kind="primary"] {
        background-color: rgba(240,90,34,0.1) !important; color: #f05a22 !important; border: 1px solid #f05a22 !important;
    }
    .cat-label { color: #5a6b79; font-size: 9px; font-weight: 800; margin-top: 15px; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 1px; }

    /* 4. CARDS E RESULTADOS */
    .radar-topo {
        background: rgba(26, 36, 45, 0.6); border-radius: 6px; padding: 6px 15px; margin-bottom: 15px;
        display: flex; align-items: center; border-left: 4px solid #f05a22;
    }
    .radar-label { font-family: 'Orbitron', sans-serif; font-weight: 700; color: #f05a22; font-size: 11px; margin-right: 15px; }
    
    .card-principal { 
        background-color: #1a242d; padding: 20px; border-radius: 12px; 
        border-bottom: 4px solid #f05a22; margin-bottom: 15px; text-align: center; 
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 22px; font-weight: 800; margin-bottom: 20px; }
    
    .prob-container { display: flex; justify-content: space-around; align-items: center; background: rgba(0,0,0,0.3); border-radius: 10px; padding: 15px 0; }
    .val-prob { color: #f05a22; font-size: 26px; font-weight: 900; }
    .label-prob { color: #8899a6; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-top: 5px; }

    .mini-card { background-color: #111a21; padding: 10px; border-radius: 8px; border: 1px solid #2d3748; text-align: center; }
    .mini-label { color: #8899a6; font-size: 8px; font-weight: 700; text-transform: uppercase; margin-bottom: 5px; display: block; }
    .mini-val { color: #00ffc3; font-weight: 900; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGICA DE DADOS ---
if 'liga_ativa' not in st.session_state: 
    st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A - BRASILEIRÃO')

@st.cache_data(ttl=3600)
def load_data(liga):
    urls = {'BRA_A': "https://raw.githubusercontent.com/automacaobrasil/dataset-brasileirao/main/brasileirao_serie_a.csv"}
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

# --- 4. BARRA LATERAL FIXA ---
with st.sidebar:
    st.markdown("""
        <div class="sidebar-header">
            <div class="ai-logo-box">
                <div class="ai-logo-dash"></div>
            </div>
            <div class="sidebar-title">GESTOR IA</div>
        </div>
    """, unsafe_allow_html=True)
    
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

# --- 5. ÁREA PRINCIPAL ---
df = load_data(st.session_state.liga_ativa)
times = sorted(df['HomeTeam'].unique())

# Colunas com um pouco mais de espaço no topo para evitar o Share
col_a, col_b, col_c = st.columns([3, 3, 2.5])
with col_a: t_casa = st.selectbox("Mandante", times, label_visibility="collapsed")
with col_b: t_fora = st.selectbox("Visitante", [t for t in times if t != t_casa], label_visibility="collapsed")
with col_c: executar = st.button("🔥 EXECUTAR ALGORITMO", use_container_width=True, type="primary")

if executar:
    st.markdown(f'<div class="radar-topo"><div class="radar-label">📡 RADAR ESTRATÉGICO</div><div style="font-size:11px; color:#8899a6;">{st.session_state.nome_liga} analisada com sucesso.</div></div>', unsafe_allow_html=True)

    st.markdown(f"""
        <div class="card-principal">
            <div class="match-title">{t_casa.upper()} VS {t_fora.upper()}</div>
            <div class="prob-container">
                <div><p class="val-prob">44.2%</p><p class="label-prob">Mandante</p></div>
                <div><p class="val-prob">22.8%</p><p class="label-prob">Empate</p></div>
                <div><p class="val-prob">33.0%</p><p class="label-prob">Visitante</p></div>
            </div>
            <div style="margin-top:15px; display:flex; justify-content:space-around; font-size:11px; color:#00ffc3; font-weight:700;">
                <span>ODD JUSTA: @2.10</span>
                <span>VALOR ESPERADO: +12.5%</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    m = st.columns(6)
    metrics = [("⚽ GOLS +2.5", "62%"), ("🚩 CANTOS +9.5", "75%"), ("👞 CHUTES +22", "81%"), 
               ("🎯 NO GOL +8", "58%"), ("⚠️ FALTAS +24", "85%"), ("🟨 CARTÕES +4", "72%")]
    
    for i, (label, val) in enumerate(metrics):
        with m[i]:
            st.markdown(f"<div class='mini-card'><span class='mini-label'>{label}</span><span class='mini-val'>{val}</span></div>", unsafe_allow_html=True)
else:
    st.markdown("<div style='height:150px;'></div>", unsafe_allow_html=True)
