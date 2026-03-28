import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO FINAL v60.6 - CÉREBRO DE GOLS + UI TOTAL PRESERVADA]
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- FUNÇÃO DE INTELIGÊNCIA AVANÇADA ---
def engine_ia_avancada():
    try:
        # Lendo seus arquivos reais do GitHub
        df_diario = pd.read_csv('data/database_diario.csv')
        df_hist = pd.read_csv('data/historico_5_temporadas.csv')
        
        analises = []
        
        for _, row in df_diario.iterrows():
            time_casa = str(row['CASA'])
            time_fora = str(row['FORA'])
            
            # 1. CÁLCULO DE WIN RATE (VITÓRIAS HISTÓRICAS)
            jogos_casa = df_hist[df_hist['Casa'] == time_casa]
            if not jogos_casa.empty:
                win_rate = (len(jogos_casa[jogos_casa['Resultado'] == 'H']) / len(jogos_casa)) * 100
                # 2. MÉDIA DE GOLS (USANDO COLUNAS DO SEU HISTÓRICO)
                media_gols = jogos_casa['GolsCasa'].mean() + jogos_casa['GolsFora'].mean()
            else:
                win_rate = 50.0
                media_gols = 0.0
            
            # Determina a sugestão baseada na média real de 5 anos
            sugestao_gols = "OVER 2.5" if media_gols > 2.2 else "OVER 1.5"
            
            analises.append({
                "jogo": f"{time_casa} vs {time_fora}",
                "win": f"{win_rate:.1f}%",
                "gols_txt": sugestao_gols,
                "media_hist": f"{media_gols:.2f}",
                "cantos": f"{row['CANTOS']}+",
                "ia": row['CONF'],
                "meta": row['TMETA'],
                "chutes": f"{row['CHUTES']}+",
                "defesas": f"{row['DEFESAS']}+",
                "cards": f"{row['CARTOES']}+"
            })
        return analises
    except Exception as e:
        return []

# --- ESTILO CSS (O DESIGN QUE VOCÊ GOSTA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 80px 30px 20px 30px !important; }
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.1); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 30px !important; z-index: 9999999;
    }
    .logo-box { color: #9d54ff !important; font-weight: 900; font-size: 20px; text-transform: uppercase; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 8px 22px; border-radius: 5px; font-weight: 800; font-size: 9.5px; }
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 13px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; margin-bottom: 15px; }
    .bilhete-item-box { background: rgba(109, 40, 217, 0.05); border-left: 4px solid #9d54ff; padding: 15px; border-radius: 8px; margin-bottom: 12px; border: 1px solid #1e293b; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR FIXA ---
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

# --- LÓGICA DE EXIBIÇÃO ---
def draw_card(title, value, color="#06b6d4"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color}; height:100%; width:75%;"></div></div></div>""", unsafe_allow_html=True)

# Processa os dados uma única vez
dados_reais = engine_ia_avancada()

if st.session_state.aba == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("SISTEMA", "JARVIS ATIVO")
    with h2: draw_card("MÉDIA GOLS", "ANALISADA", "#9d54ff")
    with h3: draw_card("HISTÓRICO", "5 TEMPORADAS")
    with h4: draw_card("IA", "REAL DATA", "#10b981")

    c1, c2 = st.columns(2)
    for i, res in enumerate(dados_reais):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""
                <div class="bilhete-item-box">
                    <div style="color:#06b6d4; font-size:9px; font-weight:900;">INTELIGÊNCIA REAL | CONFIA: {res['ia']}</div>
                    <div style="color:white; font-size:15px; font-weight:800; margin:5px 0;">{res['jogo']}</div>
                    <div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px; font-size:10px; color:#94a3b8;">
                        <div>WIN RATE: <b style="color:white;">{res['win']}</b></div>
                        <div>PALPITE GOLS: <b style="color:white;">{res['gols_txt']}</b></div>
                        <div>HIST. GOLS/JOGO: <b style="color:white;">{res['media_hist']}</b></div>
                        <div>CANTOS: <b style="color:white;">{res['cantos']}</b></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

elif st.session_state.aba == "gols":
    st.markdown("<h2 style='color:white;'>⚽ FOCO EM GOLS (HISTÓRICO)</h2>", unsafe_allow_html=True)
    for res in dados_reais:
        st.markdown(f"<div class='bilhete-item-box'><b>{res['jogo']}</b> - Média Histórica: {res['media_hist']} gols/partida</div>", unsafe_allow_html=True)

elif st.session_state.aba == "cantos":
    st.markdown("<h2 style='color:white;'>🚩 FOCO EM ESCANTEIOS</h2>", unsafe_allow_html=True)
    for res in dados_reais:
        st.markdown(f"<div class='bilhete-item-box'><b>{res['jogo']}</b> - Sugestão: {res['cantos']} cantos</div>", unsafe_allow_html=True)

else:
    st.warning(f"A aba '{st.session_state.aba}' está conectada aos dados, mas o visual detalhado será implementado no próximo passo.")

st.markdown(f"""<div class="footer-shield"><div>STATUS: ● JARVIS OPERACIONAL | {len(dados_reais)} JOGOS HOJE</div><div>v60.6 PROTECT</div></div>""", unsafe_allow_html=True)
