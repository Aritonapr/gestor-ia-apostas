import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO FINAL v60.7 - VISIBILIDADE MÁXIMA + ZERO SCROLLBAR SIDEBAR]
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- FUNÇÃO DE INTELIGÊNCIA ---
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
            else:
                win_rate, media_gols = 50.0, 0.0
            analises.append({
                "jogo": f"{time_casa} vs {row['FORA']}",
                "win": f"{win_rate:.1f}%",
                "gols_txt": "OVER 2.5" if media_gols > 2.2 else "OVER 1.5",
                "media_hist": f"{media_gols:.2f}",
                "cantos": f"{row['CANTOS']}+",
                "ia": row['CONF'],
                "meta": row['TMETA'],
                "chutes": f"{row['CHUTES']}+",
                "defesas": f"{row['DEFESAS']}+",
                "cards": f"{row['CARTOES']}+"
            })
        return analises
    except: return []

# --- ESTILO CSS REFINADO (ALTA VISIBILIDADE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap');
    
    /* REMOVER SCROLLBARS DE TUDO */
    ::-webkit-scrollbar { display: none !important; width: 0 !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    
    /* TRAVA ESPECÍFICA PARA SIDEBAR */
    [data-testid="stSidebarContent"] { overflow: hidden !important; }

    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 80px 30px 20px 30px !important; }

    /* HEADER */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.1); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 30px !important; z-index: 9999999;
    }
    .logo-box { color: #9d54ff !important; font-weight: 900; font-size: 22px; text-transform: uppercase; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 8px 22px; border-radius: 5px; font-weight: 800; font-size: 10px; }

    /* BOTÕES DA SIDEBAR */
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #cbd5e1 !important; border: none !important; 
        border-bottom: 1px solid #1e293b !important; text-align: left !important; width: 100% !important; 
        padding: 15px 25px !important; font-size: 11px !important; text-transform: uppercase !important;
        font-weight: 600;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { color: #06b6d4 !important; background: #1e293b !important; }

    /* CARDS DE JOGO (VISIBILIDADE MELHORADA) */
    .bilhete-item-box { 
        background: #1a1f26 !important; /* Fundo levemente mais claro para contraste */
        border-left: 5px solid #9d54ff; 
        padding: 18px; 
        border-radius: 10px; 
        margin-bottom: 15px; 
        border-right: 1px solid #2d3748;
        border-top: 1px solid #2d3748;
        border-bottom: 1px solid #2d3748;
    }
    .text-main { color: #ffffff !important; font-size: 16px; font-weight: 800; margin-bottom: 8px; }
    .text-sub { color: #00f2ff !important; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    .stat-row { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 10px; }
    .stat-item { color: #e2e8f0 !important; font-size: 11px; }
    .stat-val { color: #ffffff !important; font-weight: 800; }

    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO ---
st.sidebar.markdown('<div class="betano-header"><div class="logo-box">GESTOR IA</div><div class="header-right"><div class="entrar-grad">AO VIVO</div></div></div><div style="height:70px;"></div>', unsafe_allow_html=True)

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

if st.session_state.aba in ["home", "gols", "cantos"]:
    st.markdown(f"<h2 style='color:white;'>📋 {st.session_state.aba.upper()} (DADOS REAIS)</h2>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    for i, res in enumerate(dados_reais):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""
                <div class="bilhete-item-box">
                    <div class="text-sub">IA ANALYST | CONFIA: {res['ia']}</div>
                    <div class="text-main">{res['jogo']}</div>
                    <div class="stat-row">
                        <div class="stat-item">WIN RATE: <span class="stat-val">{res['win']}</span></div>
                        <div class="stat-item">PALPITE: <span class="stat-val">{res['gols_txt']}</span></div>
                        <div class="stat-item">MÉDIA GOLS: <span class="stat-val">{res['media_hist']}</span></div>
                        <div class="stat-item">CANTOS: <span class="stat-val">{res['cantos']}</span></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
else:
    st.info(f"Painel {st.session_state.aba} carregado. Aguardando processamento de novos sinais.")

st.markdown(f"""<div class="footer-shield"><div>STATUS: ● JARVIS v60.7 | CONECTADO | {len(dados_reais)} JOGOS</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
