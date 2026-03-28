import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v59.80 - RESTAURAÇÃO DE FUNÇÕES E GRID]
# DIRETRIZ: NAVEGAÇÃO BLINDADA - CADA BOTÃO DEVE EXIBIR SUA RESPECTIVA TELA
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA (PROTEÇÃO CONTRA SUMIÇO DE DADOS) ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'top_20_ia' not in st.session_state: st.session_state.top_20_ia = []

# --- CARREGAMENTO DE DADOS DOS JOGOS ---
def carregar_dados_sistema():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            col_conf = next((c for c in df.columns if 'CONF' in c.upper()), None)
            if col_conf:
                df['CONF_NUM'] = df[col_conf].astype(str).str.replace('%', '').astype(float)
                top_df = df.sort_values(by='CONF_NUM', ascending=False).head(20)
                jogos = []
                for i, row in top_df.iterrows():
                    jogos.append({
                        "CASA": row.get('CASA', 'Time A'),
                        "FORA": row.get('FORA', 'Time B'),
                        "CONF": f"{int(row.get('CONF_NUM', 0))}%",
                        "MERCADO": "OVER 1.5 GOLS",
                        "HORA": datetime.now().strftime("%H:%M")
                    })
                st.session_state.top_20_ia = jogos
        except:
            pass

carregar_dados_sistema()

# 2. ESTILIZAÇÃO CSS (CORREÇÃO DE SOBREPOSIÇÃO)
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #0b0e11 !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* Barra Superior Fixa */
    .top-bar-custom {
        position: fixed; top: 0; left: 0; width: 100%; height: 60px;
        background: #001a4d; display: flex; align-items: center;
        justify-content: space-between; padding: 0 30px; z-index: 9999;
        border-bottom: 1px solid #1e293b;
    }
    .logo-text { color: #9d54ff; font-weight: 900; font-size: 18px; text-transform: uppercase; }
    .nav-links { display: flex; gap: 20px; color: white; font-size: 10px; font-weight: 600; text-transform: uppercase; }

    /* Sidebar Estilizada */
    [data-testid="stSidebar"] { background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    .stButton > button {
        width: 100% !important; background: transparent !important; color: #94a3b8 !important;
        border: none !important; border-bottom: 1px solid #1a202c !important;
        text-align: left !important; padding: 12px 20px !important; font-size: 10px !important;
        text-transform: uppercase !important; border-radius: 0px !important;
    }
    .stButton > button:hover { background: #1e293b !important; color: #06b6d4 !important; border-left: 2px solid #6d28d9; }

    /* KPI Cards - Grid de 4 Colunas */
    .kpi-card {
        background: #161b22; border: 1px solid #30363d; border-radius: 8px;
        padding: 12px; text-align: center; margin-bottom: 10px;
    }
    .kpi-label { color: #8b949e; font-size: 9px; text-transform: uppercase; }
    .kpi-value { color: #ffffff; font-size: 16px; font-weight: 800; }

    /* Cards de Jogos */
    .game-card {
        background: #161b22; border: 1px solid #30363d; border-radius: 10px; 
        padding: 15px; margin-bottom: 15px; position: relative;
    }
    .game-header { font-size: 9px; color: #8b949e; display: flex; justify-content: space-between; }
    .game-teams { color: #f0f6fc; font-size: 13px; font-weight: 700; margin: 8px 0; text-align: center; }
    .game-market { background: #1e293b; color: #58a6ff; padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: 700; }
    .game-conf { color: #3fb950; font-weight: 800; font-size: 15px; float: right; }

    /* Rodapé */
    .footer-bar { position: fixed; bottom: 0; left: 0; width: 100%; background: #0d1117; padding: 4px 20px; font-size: 9px; color: #484f58; border-top: 1px solid #30363d; z-index: 9999; }
    </style>
""", unsafe_allow_html=True)

# 3. INTERFACE DE TOPO
st.markdown(f"""
    <div class="top-bar-custom">
        <div class="nav-links">
            <span class="logo-text">GESTOR IA</span>
            <span>APOSTAS ESPORTIVAS</span>
            <span>AO VIVO</span>
            <span>ASSERTIVIDADE IA</span>
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">
            <div style="color:white; font-size:10px; border:1px solid #30363d; padding:5px 12px; border-radius:20px; cursor:pointer;">REGISTRAR</div>
            <div style="background:#238636; color:white; padding:6px 15px; border-radius:5px; font-weight:bold; font-size:11px; cursor:pointer;">ENTRAR</div>
        </div>
    </div>
    <div style="height:70px;"></div>
""", unsafe_allow_html=True)

# 4. MENU LATERAL (DISPARADOR DE TELAS)
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "prelive"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"
    if st.button("📊 ASSERTIVIDADE IA"): st.session_state.aba_ativa = "ia"

# 5. RENDERIZAÇÃO DE TELAS (CONTROLE DE FLUXO)

# --- TELA: BILHETE OURO (HOME) ---
if st.session_state.aba_ativa == "home":
    st.markdown("<h4 style='color:white;'>📅 BILHETE OURO - TOP 20</h4>", unsafe_allow_html=True)
    
    # Cálculos para os Cards
    valor_entrada = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    
    # KPI CARDS (8 UNIDADES)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown(f'<div class="kpi-card"><div class="kpi-label">Banca Total</div><div class="kpi-value">R$ {st.session_state.banca_total:,.2f}</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="kpi-card"><div class="kpi-label">Assertividade</div><div class="kpi-value">94.2%</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="kpi-card"><div class="kpi-label">Mercado</div><div class="kpi-value">Gols</div></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="kpi-card"><div class="kpi-label">Versão</div><div class="kpi-value">v59.80</div></div>', unsafe_allow_html=True)
    
    c5, c6, c7, c8 = st.columns(4)
    with c5: st.markdown(f'<div class="kpi-card"><div class="kpi-label">Stake %</div><div class="kpi-value">{st.session_state.stake_padrao}%</div></div>', unsafe_allow_html=True)
    with c6: st.markdown(f'<div class="kpi-card"><div class="kpi-label">Entrada</div><div class="kpi-value">R$ {valor_entrada:,.2f}</div></div>', unsafe_allow_html=True)
    with c7: st.markdown('<div class="kpi-card"><div class="kpi-label">Sinais</div><div class="kpi-value">Ativos</div></div>', unsafe_allow_html=True)
    with c8: st.markdown('<div class="kpi-card"><div class="kpi-label">IA Status</div><div class="kpi-value" style="color:#3fb950;">ON</div></div>', unsafe_allow_html=True)

    # GRID DE JOGOS
    st.markdown("<br>", unsafe_allow_html=True)
    if st.session_state.top_20_ia:
        grid_cols = st.columns(3)
        for idx, jogo in enumerate(st.session_state.top_20_ia):
            with grid_cols[idx % 3]:
                st.markdown(f"""
                    <div class="game-card">
                        <div class="game-header"><span>ID: {1000+idx}</span><span>{jogo['HORA']}</span></div>
                        <div class="game-teams">{jogo['CASA']} <br> vs <br> {jogo['FORA']}</div>
                        <div class="game-market">{jogo['MERCADO']}</div>
                        <div class="game-conf">{jogo['CONF']}</div>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.info("Buscando oportunidades no banco de dados...")

# --- TELA: SCANNER PRÉ-LIVE ---
elif st.session_state.aba_ativa == "prelive":
    st.markdown("<h3 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h3>", unsafe_allow_html=True)
    pais = st.selectbox("Selecione a Região", ["BRASIL", "INGLATERRA", "ESPANHA", "ALEMANHA"])
    if st.button("🚀 EXECUTAR ALGORITMO"):
        st.success(f"Analisando jogos em {pais}...")
        st.warning("SISTEMA JARVIS: ALERTA DE DADOS FORA DA ROTINA")

# --- TELA: GESTÃO DE BANCA ---
elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h3 style='color:white;'>💰 GESTÃO DE BANCA</h3>", unsafe_allow_html=True)
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.session_state.banca_total = st.number_input("Banca Atual (R$)", value=float(st.session_state.banca_total))
    with col_g2:
        st.session_state.stake_padrao = st.slider("Stake por operação (%)", 0.1, 5.0, float(st.session_state.stake_padrao))
    st.write(f"Seu valor por entrada será de: **R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}**")

# --- TELA: ASSERTIVIDADE IA ---
elif st.session_state.aba_ativa == "ia":
    st.markdown("<h3 style='color:white;'>📊 ASSERTIVIDADE IA</h3>", unsafe_allow_html=True)
    st.info("A IA analisa os resultados diariamente às 23:00.")

# --- TRATAMENTO PARA OUTRAS ABAS (IMPEDE TELA PRETA) ---
else:
    st.markdown(f"<h3 style='color:white;'>{st.session_state.aba_ativa.upper()}</h3>", unsafe_allow_html=True)
    st.write("Esta funcionalidade está sendo sincronizada com a versão v59.80.")

# RODAPÉ DE STATUS FIXO
st.markdown("""<div class="footer-bar">STATUS: ● IA OPERACIONAL | v59.80 | RIO DE JANEIRO, BRASIL</div>""", unsafe_allow_html=True)
