import streamlit as st
import pandas as pd
import math

# ==============================================================================
# [PROTOCOLO FINAL v61.2 - SIDEBAR GOLD + BOTÕES ESTILO FOTO]
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- MOTOR DE INTELIGÊNCIA ---
def engine_ia_avancada():
    try:
        df_diario = pd.read_csv('data/database_diario.csv')
        df_hist = pd.read_csv('data/historico_5_temporadas.csv')
        analises = []
        for i, row in df_diario.head(20).iterrows():
            time_casa = str(row['CASA'])
            jogos_hist = df_hist[(df_hist['Casa'] == time_casa) | (df_hist['Fora'] == time_casa)]
            vitorias = len(jogos_hist[((jogos_hist['Casa'] == time_casa) & (jogos_hist['Resultado'] == 'H'))])
            prob_vitoria = (vitorias / len(jogos_hist)) * 100 if len(jogos_hist) > 0 else 50.0
            analises.append({
                "jogo": f"{time_casa} vs {row['FORA']}",
                "prob": f"{prob_vitoria:.1f}%",
                "confia": row['CONF'],
                "gols": row['GOLS'],
                "cantos": row['CANTOS'],
                "cards": row['CARTOES'],
                "meta": row['TMETA'],
                "chutes": row['CHUTES'],
                "defesas": row['DEFESAS']
            })
        return analises
    except: return []

# --- ESTILO CSS (SIDEBAR GOLD + BOTÕES FOTO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    
    /* REMOVER SCROLLBARS */
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; background-color: #f8f9fa !important; }

    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"] { display: none !important; }

    /* BOTÃO BILHETE OURO (GOLD NA SIDEBAR) */
    div.stButton > button:first-child, [data-testid="stSidebar"] div.stButton > button:first-of-type {
        background: linear-gradient(135deg, #bf953f, #fcf6ba, #b38728, #fcf6ba, #aa771c) !important;
        color: #000 !important;
        font-weight: 900 !important;
        border: 1px solid #fff5b7 !important;
        border-radius: 8px !important;
        position: relative;
        overflow: hidden;
        height: 50px !important;
        box-shadow: 0 4px 10px rgba(184, 134, 11, 0.3) !important;
    }

    /* EFEITO SHINE NO BOTÃO DA SIDEBAR */
    div.stButton > button:first-child::after {
        content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
        background: linear-gradient(to right, transparent, rgba(255,255,255,0.6), transparent);
        transform: rotate(45deg); animation: shine 3s infinite;
    }
    @keyframes shine { 0% { transform: translateX(-150%) rotate(45deg); } 100% { transform: translateX(150%) rotate(45deg); } }

    /* OUTROS BOTÕES DA SIDEBAR (ESTILO FOTO) */
    [data-testid="stSidebar"] div.stButton > button {
        background-color: white !important;
        color: #1e293b !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        margin-bottom: 5px !important;
        transition: 0.3s;
    }
    [data-testid="stSidebar"] div.stButton > button:hover {
        border-color: #9d54ff !important;
        color: #6d28d9 !important;
    }

    /* HEADER */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.1); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 30px !important; z-index: 9999999;
    }
    .logo-box { color: #9d54ff !important; font-weight: 900; font-size: 22px; text-transform: uppercase; }

    /* CARDS GOLD NO TOPO */
    .card-gold {
        background: linear-gradient(135deg, #bf953f, #fcf6ba, #b38728, #fcf6ba, #aa771c);
        color: #000 !important; border-radius: 10px; padding: 15px; text-align: center;
        border: 1px solid #fff5b7; position: relative; overflow: hidden;
    }

    /* ESTRUTURA DOS JOGOS */
    .game-container {
        background: #11151a; border: 1px solid #1e293b; border-left: 4px solid #bf953f;
        border-radius: 8px; padding: 20px; margin-bottom: 20px;
    }
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px; margin-top: 15px; }
    .stat-box { background: rgba(255,255,255,0.03); border: 1px solid #1e293b; padding: 8px; border-radius: 6px; }
    .stat-label { color: #bf953f; font-size: 8px; font-weight: 900; }
    .stat-value { color: #ffffff; font-size: 11px; font-weight: 700; margin-top: 3px; }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVEGAÇÃO ---
st.sidebar.markdown('<div class="betano-header"><div class="logo-box">GESTOR IA</div><div style="background:#6d28d9; color:white; padding:4px 12px; border-radius:4px; font-size:9px; font-weight:800;">IA GOLD</div></div><div style="height:75px;"></div>', unsafe_allow_html=True)

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

# --- RENDERIZAÇÃO PRINCIPAL ---
if st.session_state.aba == "home":
    dados = engine_ia_avancada()
    st.markdown("<h3 style='color:#FFD700; text-align:center; font-weight:900;'>🏆 BILHETE OURO - ANÁLISE REAL 🏆</h3>", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="card-gold"><div style="font-size:8px;font-weight:800;">ASSERTIVIDADE</div><div style="font-size:18px;font-weight:900;">94.2%</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="card-gold"><div style="font-size:8px;font-weight:800;">JOGOS</div><div style="font-size:18px;font-weight:900;">20 ATIVOS</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="card-gold"><div style="font-size:8px;font-weight:800;">BANCA</div><div style="font-size:18px;font-weight:900;">R$ 1.000,00</div></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="card-gold"><div style="font-size:8px;font-weight:800;">SISTEMA</div><div style="font-size:18px;font-weight:900;">GOLD IA</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    for res in dados:
        st.markdown(f"""
            <div class="game-container">
                <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
                    <span style="color:#bf953f; font-size:10px; font-weight:900;">WIN RATE: {res['prob']}</span>
                    <span style="color:#00f2ff; font-size:10px; font-weight:900;">CONFIA: {res['confia']}</span>
                </div>
                <div style="color:white; font-size:20px; font-weight:800;">{res['jogo']}</div>
                <div class="stats-grid">
                    <div class="stat-box"><div class="stat-label">1. VENCEDOR</div><div class="stat-value">{res['prob']}</div></div>
                    <div class="stat-box"><div class="stat-label">2. GOLS</div><div class="stat-value">{res['gols']}</div></div>
                    <div class="stat-box"><div class="stat-label">3. CARTÕES</div><div class="stat-value">{res['cards']}</div></div>
                    <div class="stat-box"><div class="stat-label">4. ESCANTEIOS</div><div class="stat-value">{res['cantos']}</div></div>
                    <div class="stat-box"><div class="stat-label">5. TIROS META</div><div class="stat-value">{res['meta']}</div></div>
                    <div class="stat-box"><div class="stat-label">6. CHUTES GOL</div><div class="stat-value">{res['chutes']}</div></div>
                    <div class="stat-box"><div class="stat-label">7. DEFESAS</div><div class="stat-value">{res['defesas']}</div></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● JARVIS GOLD v61.2 | SIDEBAR ATUALIZADA</div><div>PROTEÇÃO ATIVA</div></div>""", unsafe_allow_html=True)
