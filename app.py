import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO FINAL v60.9 - GOLD EDITION + EFEITOS ESPECIAIS]
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CÉREBRO REAL (CSVs) ---
def engine_ia_avancada():
    try:
        df_diario = pd.read_csv('data/database_diario.csv')
        df_hist = pd.read_csv('data/historico_5_temporadas.csv')
        analises = []
        for _, row in df_diario.iterrows():
            time_casa = str(row['CASA'])
            jogos_casa = df_hist[df_hist['Casa'] == time_casa]
            if not jogos_casa.empty:
                win_rate = (len(jogos_casa[jogos_casa['Resultado'] == 'H']) / len(jogos_casa)) * 100
                media_gols = jogos_casa['GolsCasa'].mean() + jogos_casa['GolsFora'].mean()
            else: win_rate, media_gols = 50.0, 0.0
            analises.append({
                "jogo": f"{time_casa} vs {row['FORA']}",
                "win": f"{win_rate:.1f}%",
                "gols_txt": "OVER 2.5" if media_gols > 2.2 else "OVER 1.5",
                "media_hist": f"{media_gols:.2f}",
                "ia": row['CONF']
            })
        return analises
    except: return []

# --- ESTILO CSS GOLD EDITION ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    /* REMOVER SCROLLBARS */
    ::-webkit-scrollbar { display: none !important; width: 0 !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }

    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 70px 30px 20px 30px !important; }

    /* HEADER */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.1); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 30px !important; z-index: 9999999;
    }
    .logo-box { color: #9d54ff !important; font-weight: 900; font-size: 22px; text-transform: uppercase; }
    .btn-entrar { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 6px 20px; border-radius: 5px; font-weight: 800; font-size: 10px; }

    /* SIDEBAR */
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #cbd5e1 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 12px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }

    /* CARD GOLD COM EFEITO SHINE */
    .card-gold {
        background: linear-gradient(135deg, #bf953f, #fcf6ba, #b38728, #fcf6ba, #aa771c);
        color: #000 !important;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 15px rgba(184, 134, 11, 0.4);
        border: 1px solid #fff5b7;
        margin-bottom: 15px;
    }

    .card-gold::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(to right, transparent, rgba(255,255,255,0.4), transparent);
        transform: rotate(45deg);
        animation: shine 4s infinite;
    }

    @keyframes shine {
        0% { transform: translateX(-150%) rotate(45deg); }
        100% { transform: translateX(150%) rotate(45deg); }
    }

    .gold-title { font-weight: 900; text-transform: uppercase; font-size: 12px; margin-bottom: 5px; color: #4b3a08; }
    .gold-value { font-size: 20px; font-weight: 900; color: #000; }

    /* GRID v58 CARDS NORMAIS */
    .card-v58 {
        background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 6px;
        text-align: center; height: 100px;
    }
    .card-v58 .title { color: #64748b; font-size: 8px; font-weight: 800; text-transform: uppercase; margin-bottom: 10px; }
    .card-v58 .value { color: white; font-size: 16px; font-weight: 900; }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR & HEADER ---
st.sidebar.markdown('<div class="betano-header"><div class="logo-box">GESTOR IA</div><div class="btn-entrar">AO VIVO</div></div><div style="height:70px;"></div>', unsafe_allow_html=True)

if 'aba' not in st.session_state: st.session_state.aba = "home"
with st.sidebar:
    if st.button("📅 BILHETE OURO"): st.session_state.aba = "home"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba = "scanner"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba = "historico"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba = "cantos"

# --- RENDERIZAÇÃO ---
dados_reais = engine_ia_avancada()

if st.session_state.aba == "home":
    # 1ª LINHA: BILHETE OURO EM DESTAQUE (EFEITO GOLD)
    st.markdown("<h3 style='color:#FFD700; text-align:center; font-weight:900;'>🏆 BILHETE OURO - TOP ANALYST 🏆</h3>", unsafe_allow_html=True)
    
    g1, g2, g3, g4 = st.columns(4)
    with g1: st.markdown('<div class="card-gold"><div class="gold-title">BILHETE 01</div><div class="gold-value">OVER 2.5</div></div>', unsafe_allow_html=True)
    with g2: st.markdown('<div class="card-gold"><div class="gold-title">BILHETE 02</div><div class="gold-value">AMBAS SIM</div></div>', unsafe_allow_html=True)
    with g3: st.markdown('<div class="card-gold"><div class="gold-title">ASSERTIVIDADE</div><div class="gold-value">94.8%</div></div>', unsafe_allow_html=True)
    with g4: st.markdown('<div class="card-gold"><div class="gold-title">IA STATUS</div><div class="gold-value">OPERAÇÕES</div></div>', unsafe_allow_html=True)

    # 2ª LINHA: CARDS DE GESTÃO (ESTILO v58)
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="card-v58"><div class="title">BANCA ATUAL</div><div class="value">R$ 1,000.00</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="card-v58"><div class="title">VOL. GLOBAL</div><div class="value">ALTO</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="card-v58"><div class="title">STAKE PADRÃO</div><div class="value">1.0%</div></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="card-v58"><div class="title">SISTEMA</div><div class="value">JARVIS v60.9</div></div>', unsafe_allow_html=True)

    # DETALHES DOS JOGOS
    st.markdown("<br><h4 style='color:white;'>📋 DETALHES DAS OPERAÇÕES</h4>", unsafe_allow_html=True)
    for res in dados_reais[:10]: # Mostra os primeiros 10
        st.markdown(f"""
            <div style="background:#1a1f26; border-left:4px solid #bf953f; padding:15px; border-radius:8px; margin-bottom:10px; border:1px solid #1e293b;">
                <div style="color:#bf953f; font-size:10px; font-weight:800;">JOGO ANALISADO</div>
                <div style="color:white; font-size:16px; font-weight:800;">{res['jogo']}</div>
                <div style="color:#94a3b8; font-size:11px;">Média Histórica: {res['media_hist']} gols | Win Rate: {res['win']}</div>
            </div>
        """, unsafe_allow_html=True)

else:
    st.info(f"Painel {st.session_state.aba} em operação.")

st.markdown("""<div class="footer-shield"><div>STATUS: ● JARVIS GOLD EDITION ATIVO</div><div>PROTEÇÃO ATIVA</div></div>""", unsafe_allow_html=True)
