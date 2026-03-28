import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO FINAL v60.5 - CÉREBRO CONECTADO AOS CSVs]
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- FUNÇÃO DE INTELIGÊNCIA REAL (PROCESSA SEUS CSVs) ---
def engine_ia_real():
    try:
        # Carrega seus arquivos das pastas corretas
        df_diario = pd.read_csv('data/database_diario.csv')
        df_hist = pd.read_csv('data/historico_5_temporadas.csv')
        
        analises = []
        
        for _, row in df_diario.iterrows():
            time_casa = str(row['CASA'])
            time_fora = str(row['FORA'])
            
            # --- CÁLCULO DE ASSERTIVIDADE REAL (BASEADO NAS 5 TEMPORADAS) ---
            # Filtra no histórico os jogos do time da casa
            jogos_passados = df_hist[df_hist['Casa'] == time_casa]
            if len(jogos_passados) > 0:
                vitorias = len(jogos_passados[jogos_passados['Resultado'] == 'H'])
                win_rate_real = (vitorias / len(jogos_passados)) * 100
            else:
                win_rate_real = 50.0 # Caso o time seja novo no histórico
            
            # --- COLETA DE DADOS DO SEU CSV DIÁRIO ---
            analises.append({
                "jogo": f"{time_casa} vs {time_fora}",
                "win": f"{win_rate_real:.1f}%",
                "gols": row['GOLS'],
                "cantos": f"{row['CANTOS']}+",
                "ia": row['CONF'], # Usa a confiança que já vem no seu CSV
                "meta": row['TMETA'],
                "chutes": f"{row['CHUTES']}+",
                "defesas": f"{row['DEFESAS']}+",
                "cards": f"{row['CARTOES']}+"
            })
        return analises
    except Exception as e:
        return [{"jogo": "Erro ao ler CSV", "win": "0%", "gols": "Erro", "cantos": "Erro", "ia": str(e), "meta": "0", "chutes": "0", "defesas": "0", "cards": "0"}]

# --- ESTILO CSS (PRESERVADO v60.3) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; width: 0 !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 90px 40px 20px 40px !important; }
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.1); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 30px !important; z-index: 9999999;
    }
    .logo-box { color: #9d54ff !important; font-weight: 900; font-size: 20px; text-transform: uppercase; }
    .header-right { display: flex; align-items: center; gap: 15px; }
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

# --- SIDEBAR ---
st.sidebar.markdown('<div class="betano-header"><div class="logo-box">GESTOR IA</div><div class="header-right"><div class="entrar-grad">AO VIVO</div></div></div><div style="height:70px;"></div>', unsafe_allow_html=True)

if 'aba' not in st.session_state: st.session_state.aba = "home"

with st.sidebar:
    if st.button("📅 BILHETE OURO"): st.session_state.aba = "home"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba = "gestao"
    if st.button("⚽ GOLS DO DIA"): st.session_state.aba = "gols"
    if st.button("🚩 ESCANTEIOS"): st.session_state.aba = "cantos"

# --- CONTEÚDO ---
def draw_card(title, value, bar_color="#06b6d4"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{bar_color}; height:100%; width:70%;"></div></div></div>""", unsafe_allow_html=True)

if st.session_state.aba == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO (DADOS REAIS)</h2>", unsafe_allow_html=True)
    
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("SISTEMA", "AUTÔNOMO")
    with h2: draw_card("FONTE", "CSV GITHUB")
    with h3: draw_card("STATUS", "PROCESSANDO")
    with h4: draw_card("IA", "CONECTADA")

    # EXECUTA A ANALISE REAL
    resultados = engine_ia_real()
    
    c1, c2 = st.columns(2)
    for i, res in enumerate(resultados):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""
                <div class="bilhete-item-box">
                    <div style="color:#06b6d4; font-size:9px; font-weight:900;">SUGESTÃO | CONFIA: {res['ia']}</div>
                    <div style="color:white; font-size:15px; font-weight:800; margin:5px 0;">{res['jogo']}</div>
                    <div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px; font-size:10px; color:#94a3b8;">
                        <div>WIN RATE HISTÓRICO: <b style="color:white;">{res['win']}</b></div>
                        <div>PALPITE GOLS: <b style="color:white;">{res['gols']}</b></div>
                        <div>CANTOS: <b style="color:white;">{res['cantos']}</b></div>
                        <div>CHUTES: <b style="color:white;">{res['chutes']}</b></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

st.markdown(f"""<div class="footer-shield"><div>STATUS: ● IA LENDO {len(engine_ia_real())} JOGOS HOJE</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
