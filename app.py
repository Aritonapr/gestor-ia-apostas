import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO FINAL v60.8 - LOOK v58 + CÉREBRO REAL + BILHETE OURO]
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- FUNÇÃO DE INTELIGÊNCIA (CONECTADA AOS SEUS CSVs) ---
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
        return analises, len(df_diario)
    except: return [], 0

# --- ESTILO CSS v58 REFINADO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap');
    
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

    /* HEADER SUPERIOR ESTILO v58 */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.1); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 30px !important; z-index: 9999999;
    }
    .logo-box { color: #9d54ff !important; font-weight: 900; font-size: 22px; text-transform: uppercase; }
    .header-nav { display: flex; gap: 15px; color: white; font-size: 9px; font-weight: 700; }
    .btn-registrar { border: 1px solid white; border-radius: 20px; padding: 5px 15px; font-size: 9px; }
    .btn-entrar { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 6px 20px; border-radius: 5px; font-weight: 800; font-size: 10px; }

    /* SIDEBAR v58 */
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #cbd5e1 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 12px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        font-weight: 600;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    /* GRID DE CARDS v58 */
    .card-v58 {
        background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 6px;
        text-align: center; height: 110px; position: relative;
    }
    .card-v58:hover { border-color: #6d28d9; }
    .card-title { color: #64748b; font-size: 8px; font-weight: 800; text-transform: uppercase; margin-bottom: 10px; }
    .card-value { color: white; font-size: 16px; font-weight: 900; }
    .card-bar-bg { background: #1e293b; height: 3px; width: 70%; border-radius: 10px; margin: 12px auto; }
    .card-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; border-radius: 10px; }

    /* BILHETES */
    .bilhete-box { 
        background: rgba(109, 40, 217, 0.05); border-left: 4px solid #9d54ff; 
        padding: 15px; border-radius: 8px; margin-bottom: 12px; border: 1px solid #1e293b;
    }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER v58 ---
st.sidebar.markdown("""
    <div class="betano-header">
        <div class="logo-box">GESTOR IA</div>
        <div class="header-nav">
            <span>APOSTAS ESPORTIVAS</span><span>APOSTAS AO VIVO</span><span>APOSTAS ENCONTRADAS</span>
        </div>
        <div style="display:flex; gap:10px; align-items:center;">
            <div class="btn-registrar">REGISTRAR</div>
            <div class="btn-entrar">ENTRAR</div>
        </div>
    </div>
    <div style="height:70px;"></div>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO ---
if 'aba' not in st.session_state: st.session_state.aba = "home"
with st.sidebar:
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba = "scanner"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba = "cantos"

# --- PROCESSAMENTO ---
dados_reais, total_jogos = engine_ia_avancada()

def draw_v58_card(title, value, bar_w="70%"):
    st.markdown(f"""
        <div class="card-v58">
            <div class="card-title">{title}</div>
            <div class="card-value">{value}</div>
            <div class="card-bar-bg"><div class="card-bar-fill" style="width:{bar_w};"></div></div>
        </div>
    """, unsafe_allow_html=True)

if st.session_state.aba == "home":
    st.markdown("<h3 style='color:white; margin-bottom:20px;'>📅 BILHETE OURO</h3>", unsafe_allow_html=True)
    
    # GRID 4x2 DE CARDS IGUAL À IMAGEM v58
    r1c1, r1c2, r1c3, r1c4 = st.columns(4)
    with r1c1: draw_v58_card("BANCA ATUAL", "R$ 1,000.00", "40%")
    with r1c2: draw_v58_card("ASSERTIVIDADE", "92.4%", "90%")
    with r1c3: draw_v58_card("SUGESTÃO", "OVER 2.5", "60%")
    with r1c4: draw_v58_card("IA STATUS", "ONLINE", "100%")
    
    st.write("") # Espaçamento entre linhas
    
    r2c1, r2c2, r2c3, r2c4 = st.columns(4)
    with r2c1: draw_v58_card("VOL. GLOBAL", "ALTO", "85%")
    with r2c2: draw_v58_card("STAKE PADRÃO", "1.0%", "30%")
    with r2c3: draw_v58_card("VALOR ENTRADA", "R$ 10.00", "50%")
    with r2c4: draw_v58_card("SISTEMA", "JARVIS v60.8", "100%")

    st.markdown("<br><h4 style='color:white;'>📋 ANÁLISE DETALHADA</h4>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    for i, res in enumerate(dados_reais):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""
                <div class="bilhete-box">
                    <div style="color:#00f2ff; font-size:10px; font-weight:800;">CONFIA: {res['ia']}</div>
                    <div style="color:white; font-size:16px; font-weight:800; margin:5px 0;">{res['jogo']}</div>
                    <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px; font-size:11px; color:#94a3b8;">
                        <div>WIN RATE: <b style="color:white;">{res['win']}</b></div>
                        <div>PALPITE: <b style="color:white;">{res['gols_txt']}</b></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

else:
    st.info(f"Painel {st.session_state.aba} carregado com sucesso.")

st.markdown(f"""<div class="footer-shield"><div>STATUS: ● JARVIS OPERACIONAL | {total_jogos} JOGOS HOJE</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
