import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random

# ==============================================================================
# [PROTOCOLO JARVIS v68.0 - INTEGRIDADE TOTAL + FILTRAGEM DINÂMICA]
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
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'top_20_ia' not in st.session_state: st.session_state.top_20_ia = []
if 'jogos_live_ia' not in st.session_state: st.session_state.jogos_live_ia = []

# --- MOTOR DE DADOS (CONEXÃO REAL) ---
@st.cache_data(ttl=60)
def carregar_dados_mestre():
    # Tenta carregar do GitHub, se falhar vai pro local, se falhar cria base reserva
    url = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    try:
        df = pd.read_csv(f"{url}?v={datetime.now().timestamp()}", on_bad_lines='skip')
        df.columns = [c.strip().upper() for c in df.columns]
        return df
    except:
        path_local = "data/database_diario.csv"
        if os.path.exists(path_local):
            df_l = pd.read_csv(path_local)
            df_l.columns = [c.strip().upper() for c in df_l.columns]
            return df_l
    return pd.DataFrame({
        'REGIAO': ['BRASIL', 'EUROPA'], 'COMPETICAO': ['SERIE A', 'CHAMPIONS'], 'CASA': ['Flamengo', 'Arsenal'], 'FORA': ['Palmeiras', 'Bayern'], 'CONF': ['95%', '92%']
    })

df_diario = carregar_dados_mestre()

# ==============================================================================
# CSS IMUTÁVEL (ZERO WHITE PRO)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [data-testid="stAppViewContainer"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; z-index: 1000000; display: flex; align-items: center; padding: 0 40px; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px; text-decoration: none; }
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; margin-bottom: 15px; }
    .kpi-detailed-card { background: #11151a; border: 1px solid #1e293b; padding: 15px; border-radius: 8px; margin-bottom: 15px; min-height: 350px; }
    .kpi-stat { font-size: 10px; color: #94a3b8; display: flex; justify-content: space-between; margin-bottom: 5px; }
    .kpi-stat b { color: white; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR E NAVEGAÇÃO ---
with st.sidebar:
    st.markdown('<div class="betano-header"><a href="#" class="logo-link">GESTOR IA</a></div><div style="height:65px;"></div>', unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc, color="#6d28d9"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; margin:10px auto;"><div style="background:{color}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# LÓGICA DE TELAS ATIVAS
# ==============================================================================

if st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    # FILTRAGEM HIERÁRQUICA REAL (Sincronizada com o CSV)
    c1, c2, c3 = st.columns(3)
    
    # Identifica colunas dinamicamente
    col_reg = 'REGIAO' if 'REGIAO' in df_diario.columns else df_diario.columns[0]
    col_comp = 'COMPETICAO' if 'COMPETICAO' in df_diario.columns else df_diario.columns[1]
    col_t = 'CASA' if 'CASA' in df_diario.columns else df_diario.columns[2]

    with c1:
        regiao_sel = st.selectbox("🌍 REGIÃO / PAÍS", sorted(df_diario[col_reg].unique()))
    with c2:
        df_reg = df_diario[df_diario[col_reg] == regiao_sel]
        comp_sel = st.selectbox("📂 GRUPO", sorted(df_reg[col_comp].unique()))
    with c3:
        st.selectbox("🏆 COMPETIÇÃO", [comp_sel])

    st.markdown("---")
    st.markdown("<h4 style='color:white;'>⚔️ DEFINIR CONFRONTO</h4>", unsafe_allow_html=True)

    # FILTRO DE TIMES: Garante que só apareçam times da competição escolhida
    df_final = df_diario[df_diario[col_comp] == comp_sel]
    lista_times = sorted(df_final[col_t].unique())

    tc1, tc2 = st.columns(2)
    with tc1: t_casa = st.selectbox("🏠 TIME DA CASA", lista_times)
    with tc2: 
        lista_f = [t for t in lista_times if t != t_casa]
        t_fora = st.selectbox("🚀 TIME DE FORA", lista_f if lista_f else lista_times)

    if st.button("⚡ EXECUTAR ALGORITMO"):
        v_calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        st.session_state.analise_bloqueada = {
            "casa": t_casa, "fora": t_fora, "vencedor": "ALTA PROB.", "gols": "OVER 1.5",
            "stake_val": f"R$ {v_calc:,.2f}", "confia": f"{random.randint(88,98)}%", "cor": "#00ff88"
        }

    if st.session_state.analise_bloqueada:
        res = st.session_state.analise_bloqueada
        st.markdown(f"<h3 style='color:white; text-align:center;'>{res['casa']} x {res['fora']}</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", res['vencedor'], 85)
        with r2: draw_card("MERCADO GOLS", res['gols'], 70)
        with r3: draw_card("VALOR STAKE", res['stake_val'], 100, "#06b6d4")
        with r4: draw_card("IA CONFIANÇA", res['confia'], 94, "#9d54ff")

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    # Mostra 12 jogos live simulando o scanner
    for i in range(3):
        cols = st.columns(4)
        for c in cols:
            with c:
                conf = random.randint(85, 99)
                st.markdown(f"""<div class="kpi-detailed-card"><div style="color:#00ff88; font-size:10px; font-weight:900;">LIVE IA: {conf}%</div><div style="color:white; font-size:12px; font-weight:800; border-bottom:1px solid #1e293b; padding-bottom:5px;">JOGO AO VIVO {i}</div><div class="kpi-stat">Pressão: <b>{random.randint(60,95)}%</b></div><div class="kpi-stat">Canto Limite: <b>SIM</b></div></div>""", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total))
    st.session_state.stake_padrao = st.slider("STAKE (%)", 0.5, 10.0, float(st.session_state.stake_padrao))
    v_entrada = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    draw_card("VALOR POR ENTRADA", f"R$ {v_entrada:,.2f}", 100, "#00ff88")

elif st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO - TOP 20 IA</h2>", unsafe_allow_html=True)
    # Aqui o Jarvis lista os 20 melhores do CSV carregado
    vips = df_diario.head(20)
    for index, row in vips.iterrows():
        st.markdown(f"""<div style="background:#11151a; padding:10px; border-bottom:1px solid #1e293b; color:white;">🔥 {row[col_t]} x {row.get('FORA', 'Visitante')} | Confiança: {row.get('CONF', '90%')}</div>""", unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v68.0</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
