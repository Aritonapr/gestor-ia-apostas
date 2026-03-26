import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v59.10 - INTEGRAÇÃO TOTAL E 8 KPI CARDS]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO) - MANTER UI v57.35
# DIRETRIZ 5: PROTOCOLO PIT - INTEGRIDADE TOTAL DE CÓDIGO (SEM ABREVIAÇÕES)
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# Redirecionamento via Query Params para Header Clicável
query_params = st.query_params
if query_params.get("go") == "home":
    st.session_state.aba_ativa = "home"
    st.query_params.clear()
elif query_params.get("go") == "assertividade":
    st.session_state.aba_ativa = "assertividade"
    st.query_params.clear()

# --- CARREGAMENTO DE BANCO DE DADOS ---
def carregar_dados():
    path_diario = "data/database_diario.csv"
    path_perf = "data/performance_ia.csv"
    
    df_d = pd.read_csv(path_diario) if os.path.exists(path_diario) else pd.DataFrame()
    
    if os.path.exists(path_perf):
        df_p = pd.read_csv(path_perf)
    else:
        df_p = pd.DataFrame(columns=['DATA', 'JOGO', 'MERCADO', 'STATUS', 'LUCRO'])
        
    return df_d, df_p

df_diario, df_performance = carregar_dados()

# 2. ESTILIZAÇÃO CSS (MANTER PADRÃO ZERO WHITE)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }

    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
        transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    .nav-links { display: flex; gap: 22px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600; text-decoration: none; transition: 0.3s; }
    .nav-item:hover { color: #06b6d4 !important; }

    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; cursor: pointer; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }

    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: all 0.2s ease !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 140px; margin-bottom: 15px;
        transition: all 0.3s ease;
    }
    .highlight-card:hover { border-color: #6d28d9; transform: translateY(-3px); }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER FIXO
st.markdown(f"""
    <div class="betano-header">
        <div class="header-left" style="display:flex; align-items:center; gap:25px;">
            <a href="?go=home" class="logo-link">GESTOR IA</a>
            <div class="nav-links">
                <div class="nav-item">APOSTAS ESPORTIVAS</div>
                <div class="nav-item">APOSTAS AO VIVO</div>
                <div class="nav-item">ESTATÍSTICAS</div>
                <a href="?go=assertividade" class="nav-item" style="color:#06b6d4 !important;">ASSERTIVIDADE IA</a>
            </div>
        </div>
        <div class="header-right" style="display:flex; align-items:center; gap:15px;">
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    <div style="height:20px;"></div>
""", unsafe_allow_html=True)

# 4. SIDEBAR DE NAVEGAÇÃO
with st.sidebar:
    st.markdown("<div style='height:70px;'></div>", unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "prelive"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🧠 ASSERTIVIDADE & IA"): st.session_state.aba_ativa = "assertividade"
    if st.button("⚽ MERCADO DE GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 MERCADO DE CANTOS"): st.session_state.aba_ativa = "escanteios"
    if st.button("🏆 VENCEDORES"): st.session_state.aba_ativa = "vencedores"

# FUNÇÃO AUXILIAR DE CARD
def draw_card(title, value, perc, color="#6d28d9"):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div>
            <div style="color:white; font-size:18px; font-weight:900; margin-top:10px;">{value}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:15px auto;">
                <div style="background:{color}; height:100%; width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# 5. LÓGICA DAS TELAS (SEM ABREVIAÇÕES)

# --- TELA HOME ---
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with c2: draw_card("ASSERTIVIDADE", "92.4%", 92, "#00ff88")
    with c3: draw_card("SUGESTÃO DIA", "OVER 2.5", 85)
    with c4: draw_card("SISTEMA", "JARVIS v59.10", 100, "#06b6d4")

# --- TELA ASSERTIVIDADE (8 KPI CARDS) ---
elif st.session_state.aba_ativa == "assertividade":
    st.markdown("<h2 style='color:white;'>🧠 CENTRAL DE ASSERTIVIDADE & IA</h2>", unsafe_allow_html=True)
    
    # Linha 1
    k1, k2, k3, k4 = st.columns(4)
    with k1: draw_card("ACERTOS (GREENS)", "128", 100, "#00ff88")
    with k2: draw_card("ERROS (REDS)", "12", 100, "#ff4b4b")
    with k3: draw_card("ROI GLOBAL", "18.5%", 80, "#9d54ff")
    with k4: draw_card("LUCRO LÍQUIDO", "R$ 1.420,00", 100, "#00ff88")
    
    # Linha 2
    k5, k6, k7, k8 = st.columns(4)
    with k5: draw_card("DRAWDOWN", "2.1%", 15, "#ffcc00")
    with k6: draw_card("MERCADO ELITE", "CANTOS", 90, "#06b6d4")
    with k7: draw_card("STREAK ATUAL", "7 ✅", 100, "#00ff88")
    with k8: draw_card("MEMÓRIA IA", "5.420 JOGOS", 100, "#9d54ff")

# --- TELA SCANNER PRÉ-LIVE ---
elif st.session_state.aba_ativa == "prelive":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    if not df_diario.empty:
        st.dataframe(df_diario, use_container_width=True)
    else:
        st.warning("Aguardando sincronização de dados do database_diario.csv...")

# --- TELA GOLS ---
elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ MERCADO DE GOLS</h2>", unsafe_allow_html=True)
    st.info("IA Analisando tendências de Over/Under baseadas no histórico...")

# --- TELA CANTOS ---
elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 MERCADO DE CANTOS</h2>", unsafe_allow_html=True)
    st.info("IA Analisando volume de escanteios por liga...")

# --- TELA GESTÃO ---
elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL", value=st.session_state.banca_total)
    st.write(f"Sua stake de 1% é: R$ {st.session_state.banca_total * 0.01:.2f}")

# RODAPÉ STATUS
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v59.10</div><div>PROTEÇÃO DE DADOS ATIVA</div></div>""", unsafe_allow_html=True)
