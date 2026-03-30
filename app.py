import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# Tenta carregar a ferramenta de busca, se não conseguir, avisa o usuário
try:
    from bs4 import BeautifulSoup
except:
    st.error("Erro: Adicione 'beautifulsoup4' no seu arquivo requirements.txt do GitHub.")

# ==============================================================================
# PROTOCOLO JARVIS v69.0 - SCANNER AO VIVO + BILHETE OURO (ESTÁVEL)
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- DESIGN ZERO WHITE PRO (RESTAURAÇÃO TOTAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: white !important;
    }

    /* Remove barras de rolagem desnecessárias */
    ::-webkit-scrollbar { width: 0px; background: transparent; }
    [data-testid="stSidebar"] > div:first-child { overflow: hidden !important; }

    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 90px 45px 20px 45px !important; }

    /* Cabeçalho Profissional */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 70px; 
        background-color: #001133 !important; border-bottom: 1px solid rgba(255,255,255,0.08); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 50px; z-index: 10000; 
    }
    .logo-area { color: #9d54ff !important; font-weight: 900; font-size: 26px; letter-spacing: -1.5px; }
    .btn-entrar { background: linear-gradient(90deg, #6d28d9, #06b6d4); color: white; padding: 9px 28px; border-radius: 6px; font-weight: 900; font-size: 11px; cursor: pointer; }

    /* Menu Lateral */
    [data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 1px solid #1e293b !important; }
    .stButton > button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        text-align: left !important; width: 100% !important; padding: 15px 25px !important; 
        font-size: 13px !important; font-weight: 600 !important; border-bottom: 1px solid #161b22 !important; border-radius: 0px !important;
    }
    .stButton > button:hover { color: #06b6d4 !important; background-color: #161b22 !important; border-left: 4px solid #6d28d9 !important; }

    /* Cards de Impacto */
    .kpi-box { background: #11151c; border: 1px solid #1c2533; padding: 30px 20px; border-radius: 12px; text-align: center; margin-bottom: 20px; }
    .kpi-label { color: #64748b; font-size: 10px; font-weight: 800; text-transform: uppercase; margin-bottom: 15px; }
    .kpi-val { color: #ffffff; font-size: 22px; font-weight: 900; margin-bottom: 15px; }
    .neon-line { height: 4px; width: 80%; margin: 0 auto; background: #1c2533; border-radius: 10px; overflow: hidden; position: relative; }
    .neon-fill { position: absolute; left: 0; top: 0; height: 100%; background: linear-gradient(90deg, #6d28d9, #06b6d4); }
    </style>
""", unsafe_allow_html=True)

# --- MOTOR DE BUSCA AO VIVO ---
def capturar_live():
    jogos_live = []
    try:
        header = {'User-Agent': 'Mozilla/5.0'}
        # Busca no placar de futebol os jogos que estão rolando agora
        res = requests.get("https://www.placardefutebol.com.br/", headers=header, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        for card in soup.select('.match-card'):
            try:
                status = card.select_one('.status').text.strip()
                casa = card.select_one('.team-home').text.strip()
                fora = card.select_one('.team-away').text.strip()
                placar = card.select_one('.match-score').text.strip().replace('\n', ' ')
                # Só adiciona se o jogo estiver em andamento (com minutos ou 'Intervalo')
                if any(char.isdigit() for char in status) or "Intervalo" in status:
                    jogos_live.append({"HORA/MIN": status, "CONFRONTO": f"{casa} x {fora}", "PLACAR": placar})
            except: continue
    except: pass
    return pd.DataFrame(jogos_live) if jogos_live else None

# --- NAVEGAÇÃO E INTERFACE ---
if 'menu' not in st.session_state: st.session_state.menu = "bilhete"

# BARRA SUPERIOR
st.markdown('<div class="betano-header"><div class="logo-area">GESTOR IA</div><div class="btn-entrar">ENTRAR</div></div>', unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown('<div style="height:80px;"></div>', unsafe_allow_html=True)
    if st.button("📅 BILHETE OURO"): st.session_state.menu = "bilhete"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.menu = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.menu = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.menu = "calls"

def render_kpi(label, val, pct):
    st.markdown(f'<div class="kpi-box"><div class="kpi-label">{label}</div><div class="kpi-val">{val}</div><div class="neon-line"><div class="neon-fill" style="width:{pct}%"></div></div></div>', unsafe_allow_html=True)

# LÓGICA DAS TELAS
if st.session_state.menu == "bilhete":
    st.markdown("<h2 style='font-weight:900;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: render_kpi("BANCA ATUAL", "R$ 1.000,00", 100)
    with c2: render_kpi("ASSERTIVIDADE", "92.4%", 92)
    with c3: render_kpi("SUGESTÃO", "OVER 2.5", 75)
    with c4: render_kpi("IA STATUS", "ONLINE", 100)
    
    # Busca os jogos que o seu robô salvou no GitHub
    try:
        df_db = pd.read_csv("https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv")
        st.write("### 📝 Jogos Analisados para Hoje")
        st.dataframe(df_db, use_container_width=True)
    except:
        st.info("Aguardando sincronização de dados...")

elif st.session_state.menu == "live":
    st.markdown("<h2 style='font-weight:900;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    with st.spinner("Buscando jogos nos estádios..."):
        df_live = capturar_live()
        if df_live is not None:
            st.write("### ⚽ Partidas em Andamento")
            st.table(df_live) # Usando table para ficar mais limpo no mobile/web
        else:
            st.warning("Nenhum jogo em andamento no momento. Verifique mais tarde!")

# RODAPÉ
st.markdown('<div style="position:fixed; bottom:0; left:0; width:100%; background:#0b0e11; height:28px; border-top:1px solid #1e293b; display:flex; justify-content:space-between; align-items:center; padding:0 25px; font-size:9px; color:#475569; z-index:10000;"><div>STATUS: ● JARVIS v69.0 OPERACIONAL</div><div>30/03/2026</div></div>', unsafe_allow_html=True)
