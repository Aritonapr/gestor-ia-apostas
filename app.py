import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v59.20 - RESTAURAÇÃO VISUAL E KPI EXPANDIDO]
# DIRETRIZ: RESTAURAR DESIGN DA IMAGEM 1 (BANCA) E IMAGEM 2 (SCANNER)
# DIRETRIZ: MANTER 8 KPIS NA HOME E 8 KPIS NA ASSERTIVIDADE
# DIRETRIZ: PROTOCOLO PIT - INTEGRIDADE TOTAL SEM ABREVIAÇÕES
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# Redirecionamento URL
qp = st.query_params
if qp.get("go") == "home": st.session_state.aba_ativa = "home"
elif qp.get("go") == "assertividade": st.session_state.aba_ativa = "assertividade"

# --- CARREGAMENTO DE DADOS ---
def carregar_dados():
    path_d = "data/database_diario.csv"
    df_d = pd.read_csv(path_d) if os.path.exists(path_d) else pd.DataFrame()
    return df_d
df_diario = carregar_dados()

# --- CSS ZERO WHITE (RESTAURAÇÃO COMPLETA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stAppViewContainer"] { background-color: #0b0e11 !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    /* HEADER RESTAURADO */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; display: flex; align-items: center; 
        justify-content: space-between; padding: 0 40px !important; z-index: 1000000; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-decoration: none; text-transform: uppercase; }
    .nav-links { display: flex; gap: 20px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 10px !important; text-transform: uppercase; font-weight: 700; text-decoration: none; opacity: 0.8; }
    .nav-item:hover { opacity: 1; color: #06b6d4 !important; }
    
    /* SIDEBAR */
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    /* CARDS */
    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 145px; margin-bottom: 15px;
    }
    .progress-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 15px auto; }
    .progress-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; border-radius: 10px; }

    /* TITULOS */
    .section-title { color: white; font-size: 28px; font-weight: 800; margin-bottom: 30px; display: flex; align-items: center; gap: 15px; }
    .banca-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px; }
    
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# --- FUNÇÃO AUXILIAR CARD ---
def draw_card(title, value, perc):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div>
            <div style="color:white; font-size:18px; font-weight:900; margin-top:10px;">{value}</div>
            <div class="progress-bg"><div class="progress-fill" style="width:{perc}%;"></div></div>
        </div>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown(f"""
    <div class="betano-header">
        <div style="display:flex; align-items:center; gap:25px;">
            <a href="?go=home" class="logo-link">GESTOR IA</a>
            <div class="nav-links">
                <div class="nav-item">ESPORTES</div><div class="nav-item">AO VIVO</div>
                <div class="nav-item">VIRTUAIS</div><div class="nav-item">E-SPORTS</div>
                <div class="nav-item">OPORTUNIDADES IA</div><div class="nav-item">RESULTADOS</div>
                <a href="?go=assertividade" class="nav-item">ASSERTIVIDADE IA</a>
            </div>
        </div>
        <div style="display:flex; align-items:center; gap:15px;">
            <div style="color:white; font-size:16px; cursor:pointer;">🔍</div>
            <div style="color:white; border:1px solid white; padding:7px 15px; border-radius:20px; font-size:10px; font-weight:800;">REGISTRAR</div>
            <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:8px 20px; border-radius:5px; font-size:10px; font-weight:800;">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
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
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"

# --- TELAS ---

if st.session_state.aba_ativa == "home":
    st.markdown('<div class="section-title">📅 JOGOS DO DIA</div>', unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with h3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with h4: draw_card("IA STATUS", "ONLINE", 100)
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("VOL. GLOBAL", "ALTO", 75)
    with h6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with h7: draw_card("VALOR ENTRADA", f"R$ {st.session_state.banca_total*st.session_state.stake_padrao/100:,.2f}", 100)
    with h8: draw_card("SISTEMA", "JARVIS v59.20", 100)

elif st.session_state.aba_ativa == "gestao":
    st.markdown('<div class="banca-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>', unsafe_allow_html=True)
    col_in, col_out = st.columns([1.2, 2.5])
    with col_in:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
        st.session_state.stake_padrao = st.slider("STAKE POR OPERAÇÃO (%)", 0.1, 10.0, st.session_state.stake_padrao)
        st.session_state.meta_diaria = st.slider("META DIÁRIA (%)", 1.0, 30.0, st.session_state.meta_diaria)
        st.session_state.stop_loss = st.slider("LIMITE DE PERDA (%)", 1.0, 30.0, st.session_state.stop_loss)
    
    with col_out:
        v_stake = st.session_state.banca_total * st.session_state.stake_padrao / 100
        g1, g2, g3, g4 = st.columns(4)
        with g1: draw_card("VALOR ENTRADA", f"R$ {v_stake:,.2f}", 100)
        with g2: draw_card("STOP GAIN (R$)", f"R$ {st.session_state.banca_total*st.session_state.meta_diaria/100:,.2f}", 100)
        with g3: draw_card("STOP LOSS (R$)", f"R$ {st.session_state.banca_total*st.session_state.stop_loss/100:,.2f}", 100)
        with g4: draw_card("ALVO FINAL", f"R$ {st.session_state.banca_total*(1+st.session_state.meta_diaria/100):,.2f}", 100)
        g5, g6, g7, g8 = st.columns(4)
        with g5: draw_card("RISCO TOTAL", f"{st.session_state.stake_padrao}%", 100)
        with g6: draw_card("ENTRADAS/META", "3", 100)
        with g7: draw_card("ENTRADAS/LOSS", "5", 100)
        with g8: draw_card("SAÚDE BANCA", "EXCELENTE", 100)

elif st.session_state.aba_ativa == "prelive":
    st.markdown('<div class="section-title">🎯 SCANNER PRÉ-LIVE</div>', unsafe_allow_html=True)
    if not df_diario.empty: st.dataframe(df_diario, use_container_width=True)
    else: st.info("Sincronize o database_diario.csv para ver a lista de jogos.")

elif st.session_state.aba_ativa == "assertividade":
    st.markdown('<div class="section-title">🧠 ASSERTIVIDADE & IA</div>', unsafe_allow_html=True)
    k1, k2, k3, k4 = st.columns(4)
    with k1: draw_card("ACERTOS", "128", 100)
    with k2: draw_card("ERROS", "12", 100)
    with k3: draw_card("ROI %", "14.5%", 100)
    with k4: draw_card("LUCRO", "R$ 420", 100)
    k5, k6, k7, k8 = st.columns(4)
    with k5: draw_card("DRAWDOWN", "2.1%", 100)
    with k6: draw_card("MEMÓRIA IA", "5.4k", 100)
    with k7: draw_card("MERCADO ELITE", "CANTOS", 100)
    with k8: draw_card("STATUS", "EVOLUINDO", 100)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v59.20</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
