import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# Tenta carregar a ferramenta de busca para o Live
try:
    from bs4 import BeautifulSoup
except:
    pass

# ==============================================================================
# PROTOCOLO JARVIS v70.0 - RESTAURAÇÃO TOTAL DESIGN ZERO WHITE PRO
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- BLOCO DE ESTILO (RESTAURAÇÃO DO VISUAL DAS FOTOS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800;900&display=swap');
    
    /* Fundo Escuro Total */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: white !important;
    }

    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 100px 45px 20px 45px !important; }

    /* REMOVER BARRA DE ROLAGEM DA ESQUERDA */
    [data-testid="stSidebar"] > div:first-child { overflow: hidden !important; }
    [data-testid="stSidebarNav"] { overflow: hidden !important; }

    /* Barra Superior Azul (Fiel à sua foto v60) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 75px; 
        background-color: #001133 !important; border-bottom: 1px solid rgba(255,255,255,0.08); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px; z-index: 10000; 
    }
    .logo-area { color: #9d54ff !important; font-weight: 900; font-size: 28px; letter-spacing: -1.5px; }
    .nav-links-container { display: flex; gap: 20px; align-items: center; margin-left: 30px; }
    .nav-link-item { color: #ffffff; font-size: 10px; font-weight: 800; text-transform: uppercase; opacity: 0.8; }
    .btn-registrar { border: 1px solid #ffffff; color: white; padding: 8px 20px; border-radius: 20px; font-size: 10px; font-weight: 800; margin-right: 10px;}
    .btn-entrar-neon { background: linear-gradient(90deg, #6d28d9, #06b6d4); color: white; padding: 10px 30px; border-radius: 6px; font-weight: 900; font-size: 11px; }

    /* Menu Lateral Customizado */
    [data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 1px solid #1e293b !important; width: 320px !important; }
    .stButton > button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        text-align: left !important; width: 100% !important; padding: 16px 25px !important; 
        font-size: 13px !important; font-weight: 600 !important; text-transform: uppercase !important;
        border-bottom: 1px solid #161b22 !important; border-radius: 0px !important;
    }
    .stButton > button:hover { color: #06b6d4 !important; background-color: #161b22 !important; border-left: 4px solid #6d28d9 !important; }

    /* Cards KPI (Restauração das fotos v60/v63) */
    .kpi-box {
        background: #11151c; border: 1px solid #1c2533; padding: 30px 15px;
        border-radius: 12px; text-align: center; margin-bottom: 20px; min-height: 180px;
    }
    .kpi-label { color: #64748b; font-size: 9px; font-weight: 800; text-transform: uppercase; margin-bottom: 20px; letter-spacing: 1px; }
    .kpi-hero-text { color: #ffffff; font-size: 22px; font-weight: 900; margin-bottom: 25px; }
    .neon-bar-container { background: #1c2533; height: 4px; width: 80%; margin: 0 auto; border-radius: 10px; overflow: hidden; position: relative;}
    .neon-bar-fill { position: absolute; left: 0; top: 0; height: 100%; background: linear-gradient(90deg, #6d28d9, #06b6d4); }
    </style>
""", unsafe_allow_html=True)

# --- FUNÇÕES DE BUSCA ---
def buscar_live_agora():
    lista = []
    try:
        header = {'User-Agent': 'Mozilla/5.0'}
        res = requests.get("https://www.placardefutebol.com.br/", headers=header, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        for jogo in soup.select('.match-card'):
            stt = jogo.select_one('.status').text.strip()
            csa = jogo.select_one('.team-home').text.strip()
            fra = jogo.select_one('.team-away').text.strip()
            plc = jogo.select_one('.match-score').text.strip().replace('\n', ' ')
            lista.append({"STATUS": stt, "CASA": csa, "PLACAR": plc, "FORA": fra})
    except: pass
    return pd.DataFrame(lista) if lista else None

# --- NAVEGAÇÃO ---
if 'pagina_atual' not in st.session_state: st.session_state.pagina_atual = "bilhete"

# HEADER SUPERIOR FIXO
st.markdown(f"""
    <div class="betano-header">
        <div style="display: flex; align-items: center;">
            <div class="logo-area">GESTOR IA</div>
            <div class="nav-links-container">
                <div class="nav-link-item">APOSTAS ESPORTIVAS</div>
                <div class="nav-link-item">APOSTAS AO VIVO</div>
                <div class="nav-link-item">ESTATÍSTICAS</div>
            </div>
        </div>
        <div style="display: flex; align-items: center;">
            <div class="btn-registrar">REGISTRAR</div>
            <div class="btn-entrar-neon">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# SIDEBAR (MENU)
with st.sidebar:
    st.markdown('<div style="height:80px;"></div>', unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.pagina_atual = "scanner"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.pagina_atual = "live"
    if st.button("📅 BILHETE OURO"): st.session_state.pagina_atual = "bilhete"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.pagina_atual = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.pagina_atual = "calls"

# FUNÇÃO PARA DESENHAR OS CARDS IGUAIS À FOTO
def draw_card(label, valor, pct):
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-label">{label}</div>
            <div class="kpi-hero-text">{valor}</div>
            <div class="neon-bar-container">
                <div class="neon-bar-fill" style="width: {pct}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- CONTEÚDO DAS TELAS ---
if st.session_state.pagina_atual == "bilhete":
    st.markdown("<h2 style='font-size:30px; font-weight:900; margin-bottom:30px;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    
    # Primeira Linha de 4 Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1: draw_card("BANCA ATUAL", "R$ 1.000,00", 100)
    with col2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with col3: draw_card("SUGESTÃO", "OVER 2.5", 75)
    with col4: draw_card("IA STATUS", "ONLINE", 100)
    
    # Segunda Linha de 4 Cards
    col5, col6, col7, col8 = st.columns(4)
    with col5: draw_card("VOL. GLOBAL", "ALTO", 85)
    with col6: draw_card("STAKE PADRÃO", "1.0%", 10)
    with col7: draw_card("VALOR ENTRADA", "R$ 10,00", 100)
    with col8: draw_card("SISTEMA", "JARVIS v70.0", 100)

    st.markdown("<br>### 📋 ANÁLISE COMPLETA DO DIA", unsafe_allow_html=True)
    try:
        df = pd.read_csv("https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv")
        st.dataframe(df, use_container_width=True)
    except:
        st.info("Carregando jogos do banco de dados...")

elif st.session_state.pagina_atual == "live":
    st.markdown("<h2 style='font-size:30px; font-weight:900; margin-bottom:30px;'>📡 AO VIVO AGORA</h2>", unsafe_allow_html=True)
    with st.spinner("Conectando aos estádios..."):
        df_live = buscar_live_agora()
        if df_live is not None:
            st.table(df_live)
        else:
            st.warning("Sem jogos ao vivo no radar da IA agora.")

# RODAPÉ
st.markdown('<div style="position:fixed; bottom:0; left:0; width:100%; background:#0b0e11; height:28px; border-top:1px solid #1e293b; display:flex; justify-content:space-between; align-items:center; padding:0 25px; font-size:9.5px; color:#475569; z-index:10000;"><div>STATUS: ● IA OPERACIONAL | v70.0</div><div>JARVIS © 2026</div></div>', unsafe_allow_html=True)
