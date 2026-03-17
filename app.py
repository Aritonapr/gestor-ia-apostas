import streamlit as st
import time
import random
import os
import pandas as pd

# ==============================================================================
# [GIAE KERNEL SHIELD v47.0 - THE ULTIMATE RESTORATION]
# FOCO: FIDELIDADE TOTAL ÀS IMAGENS | RESTAURAÇÃO DOS 8 CARDS | PROTEÇÃO DE DADOS
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- [01] ESTABILIZAÇÃO DE SESSÃO ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'analise_pronta' not in st.session_state: st.session_state.analise_pronta = False
if 'banca_atual' not in st.session_state: st.session_state.banca_atual = 1000.0

# --- [02] DIRETÓRIOS ---
DATA_DIR = "giae_core_data"
if not os.path.exists(DATA_DIR): os.makedirs(DATA_DIR)
DB_PATH = os.path.join(DATA_DIR, "historico_estatistico.csv")

# --- [03] BLOCO DE SEGURANÇA CSS (ESTILO JARVIS - CÓPIA FIEL DAS IMAGENS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* RESET E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }

    /* SIDEBAR LOCK */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    /* NAVBAR SUPERIOR AZUL ROYAL */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; 
    }
    .header-left { display: flex; align-items: center; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; text-decoration: none !important; margin-right: 40px; }
    .nav-items { display: flex; gap: 15px; }
    .nav-items span { color: #ffffff; font-size: 9px !important; text-transform: uppercase; opacity: 0.7; white-space: nowrap; }

    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { color: #ffffff !important; font-size: 10px !important; font-weight: 700; border: 1px solid #ffffff !important; padding: 6px 15px !important; border-radius: 20px !important; text-decoration: none !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 7px 20px !important; border-radius: 4px !important; font-weight: 800; font-size: 10px !important; }

    /* BOTÕES DA SIDEBAR */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; 
        font-size: 10px !important; text-transform: uppercase !important;
    }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }

    /* NEWS TICKER */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 12px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 20px; border-radius: 4px; }

    /* CARDS DE RESULTADO (FIEL ÀS IMAGENS) */
    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 25px 15px; border-radius: 8px; 
        text-align: center; height: 160px; transition: 0.3s; margin-bottom: 15px;
    }
    .highlight-card:hover { border-color: #6d28d9; transform: translateY(-3px); }
    
    .card-label { color: #64748b; font-size: 9px; text-transform: uppercase; font-weight: 600; margin-bottom: 10px; }
    .card-value { color: white; font-size: 16px; font-weight: 900; margin-top: 10px; }
    
    .pulse-dot { height: 6px; width: 6px; background-color: #22c55e; border-radius: 50%; display: inline-block; margin-right: 5px; animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
    
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 15px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    /* BOTÃO EXECUTAR ROXO */
    [data-testid="stMainBlockContainer"] .stButton > button {
        background: linear-gradient(90deg, #6d28d9 0%, #4f46e5 100%) !important;
        color: white !important; border: none !important; font-weight: 900 !important;
        padding: 12px 30px !important; border-radius: 6px !important;
        text-transform: uppercase; letter-spacing: 1px;
        animation: pulse-glow 2s infinite !important;
    }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- [04] HIERARQUIA DE DADOS (RECUPERADA) ---
DADOS_HIEARARQUIA = {
    "BRASIL": {
        "Nacional": {
            "Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo", "São Paulo", "Grêmio", "Atlético-MG", "Fluminense", "Internacional", "Corinthians", "Bahia"]
        }
    },
    "EUROPA": {
        "Internacional": {
            "UEFA Champions League": ["Real Madrid", "Man. City", "Bayern Munique", "Arsenal", "Barcelona", "Inter de Milão"]
        }
    }
}

# --- [05] CABEÇALHO ---
st.markdown("""
    <div class="betano-header">
        <div class="header-left">
            <a class="logo-link">GESTOR IA</a>
            <div class="nav-items">
                <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Oportunidades IA</span>
                <span>Estatísticas Avançadas</span><span>Probabilidades Reais</span><span>Assertividade IA</span>
            </div>
        </div>
        <div class="header-right">
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- [06] SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE"): 
        st.session_state.aba_ativa = "analise"
        st.session_state.analise_pronta = False
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "scanner_live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    st.button("📅 JOGOS DO DIA")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("⚽ APOSTAS POR GOLS")

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- [07] TELA: HOME (CONFORME IMAGEM 1) ---
if st.session_state.aba_ativa == "home":
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE ● ALERTA: ODDS EM QUEDA</div>', unsafe_allow_html=True)
    
    h1, h2, h3, h4 = st.columns(4)
    with h1: st.markdown('<div class="highlight-card"><div class="card-label"><span class="pulse-dot"></span>Destaque Live</div><div class="card-value">FLAMENGO x PALMEIRAS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)
    with h2: st.markdown('<div class="highlight-card"><div class="card-label">Sugestão</div><div class="card-value">OVER 2.5 GOLS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:88%;"></div></div></div>', unsafe_allow_html=True)
    with h3: st.markdown('<div class="highlight-card"><div class="card-label">IA Education</div><div class="card-value">GESTÃO 3%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)
    with h4: st.markdown('<div class="highlight-card"><div class="card-label">Tendência</div><div class="card-value">ODDS EM QUEDA</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:75%;"></div></div></div>', unsafe_allow_html=True)

    h5, h6, h7, h8 = st.columns(4)
    with h5: st.markdown('<div class="highlight-card"><div class="card-label">Scanner</div><div class="card-value">ALTA PRESSÃO (HT)</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:60%;"></div></div></div>', unsafe_allow_html=True)
    with h6: st.markdown('<div class="highlight-card"><div class="card-label">Performance</div><div class="card-value">ASSERTIVIDADE 92%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:92%;"></div></div></div>', unsafe_allow_html=True)
    with h7: st.markdown('<div class="highlight-card"><div class="card-label">Volume</div><div class="card-value" style="border: 1px solid #6d28d9; border-radius:4px; padding:5px;">MERCADO EM ALTA</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:80%;"></div></div></div>', unsafe_allow_html=True)
    with h8: st.markdown('<div class="highlight-card"><div class="card-label">Proteção</div><div class="card-value">JARVIS SUPREME</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)

# --- [08] TELA: SCANNER (CONFORME IMAGEM 2) ---
elif st.session_state.aba_ativa == "analise":
    c1, c2 = st.columns(2)
    with c1: casa = st.selectbox("🏠 CASA", DADOS_HIEARARQUIA["BRASIL"]["Nacional"]["Brasileirão Série A"])
    with c2: fora = st.selectbox("🚀 VISITANTE", [t for t in DADOS_HIEARARQUIA["BRASIL"]["Nacional"]["Brasileirão Série A"] if t != casa])

    with st.expander("💰 CONFIGURAR GESTÃO DE BANCA"):
        st.session_state.banca_atual = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_atual)

    if st.button("⚡ EXECUTAR ALGORITIMO"):
        with st.spinner("PROCESSANDO..."):
            time.sleep(1)
            st.session_state.analise_pronta = True

    if st.session_state.analise_pronta:
        stake = st.session_state.banca_atual * 0.01
        st.markdown(f'<div style="color:#9d54ff; font-weight:900; font-size:16px; margin: 20px 0; text-transform: uppercase;">RESULTADO ALGORITIMO: {casa} vs {fora}</div>', unsafe_allow_html=True)
        
        # LINHA 1 (4 CARDS)
        r1, r2, r3, r4 = st.columns(4)
        with r1: st.markdown(f'<div class="highlight-card"><div class="card-label">VENCEDOR</div><div class="card-value">{casa}</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:76%;"></div></div></div>', unsafe_allow_html=True)
        with r2: st.markdown(f'<div class="highlight-card"><div class="card-label">MERCADO GOLS</div><div class="card-value">OVER 1.5 REAL</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:85%;"></div></div></div>', unsafe_allow_html=True)
        with r3: st.markdown(f'<div class="highlight-card"><div class="card-label">STAKE RECOMENDADA</div><div style="color:#22c55e; font-size:18px; font-weight:900; margin-top:10px;">R$ {stake:,.2f}</div><div style="color:#475569; font-size:9px;">(Gestão 1%)</div></div>', unsafe_allow_html=True)
        with r4: st.markdown(f'<div class="highlight-card" style="border: 1px solid #6d28d9;"><div class="card-label">ESCANTEIOS</div><div class="card-value">MAIS DE 9.5</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:82%;"></div></div></div>', unsafe_allow_html=True)
        
        # LINHA 2 (MAIS 4 CARDS = 8 TOTAL)
        r5, r6, r7, r8 = st.columns(4)
        with r5: st.markdown(f'<div class="highlight-card"><div class="card-label">TIROS DE META</div><div class="card-value">14-16 TOTAIS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)
        with r6: st.markdown(f'<div class="highlight-card"><div class="card-label">CHUTES AO GOL</div><div class="card-value">CASA +5.5</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:78%;"></div></div></div>', unsafe_allow_html=True)
        with r7: st.markdown(f'<div class="highlight-card"><div class="card-label">DEFESAS GOLEIRO</div><div class="card-value">VISITANTE 4+</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:80%;"></div></div></div>', unsafe_allow_html=True)
        with r8: st.markdown(f'<div class="highlight-card"><div class="card-label">ÍNDICE PRESSÃO</div><div class="card-value">GOL MADURO 68%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:68%;"></div></div></div>', unsafe_allow_html=True)

# --- [09] FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v47.0 | JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
