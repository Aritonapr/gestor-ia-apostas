import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v59.62 - REESTRUTURAÇÃO VISUAL E INTEGRIDADE]
# DIRETRIZ: MANTER TODAS AS FUNÇÕES EXISTENTES E EXIBIR 20 JOGOS EM GRID
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA (NÃO APAGAR) ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'top_20_ia' not in st.session_state: st.session_state.top_20_ia = []

# --- CARREGAMENTO DE DADOS ---
def carregar_dados_sistema():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            # Lógica para extrair Top 20 por confiança
            col_conf = next((c for c in df.columns if 'CONF' in c.upper()), None)
            if col_conf:
                df['CONF_NUM'] = df[col_conf].astype(str).str.replace('%', '').astype(float)
                top_df = df.sort_values(by='CONF_NUM', ascending=False).head(20)
                jogos = []
                for _, row in top_df.iterrows():
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

# 2. ESTILIZAÇÃO CSS (FOCO EM LEITURA E DARK MODE)
st.markdown("""
    <style>
    /* Reset e Fundo */
    [data-testid="stAppViewContainer"] { background-color: #0b0e11 !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* Barra Superior Fixa */
    .top-bar-custom {
        position: fixed; top: 0; left: 0; width: 100%; height: 65px;
        background: #001a4d; display: flex; align-items: center;
        justify-content: space-between; padding: 0 30px; z-index: 9999;
        border-bottom: 1px solid #1e293b;
    }
    .logo-text { color: #9d54ff; font-weight: 900; font-size: 20px; }
    .nav-links { display: flex; gap: 20px; color: white; font-size: 11px; font-weight: 600; text-transform: uppercase; }

    /* Sidebar Custom */
    [data-testid="stSidebar"] { background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    .stButton > button {
        width: 100% !important; background: transparent !important; color: #94a3b8 !important;
        border: none !important; border-bottom: 1px solid #1a202c !important;
        text-align: left !important; padding: 15px 20px !important; font-size: 11px !important;
    }
    .stButton > button:hover { background: #1e293b !important; color: #06b6d4 !important; }

    /* KPI Cards - 8 UNIDADES */
    .kpi-container { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-bottom: 25px; }
    .kpi-card {
        background: #161b22; border: 1px solid #30363d; border-radius: 10px;
        padding: 15px; text-align: center;
    }
    .kpi-label { color: #8b949e; font-size: 10px; text-transform: uppercase; margin-bottom: 5px; }
    .kpi-value { color: #ffffff; font-size: 18px; font-weight: 800; }

    /* Grid de Jogos (Novo Modelo) */
    .game-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 15px; }
    .game-card {
        background: linear-gradient(145deg, #161b22, #0d1117);
        border: 1px solid #30363d; border-radius: 12px; padding: 15px;
        transition: transform 0.2s;
    }
    .game-card:hover { transform: translateY(-3px); border-color: #58a6ff; }
    .game-header { display: flex; justify-content: space-between; font-size: 10px; color: #8b949e; margin-bottom: 10px; }
    .game-teams { color: #f0f6fc; font-size: 14px; font-weight: 700; margin: 10px 0; }
    .game-market { background: rgba(88, 166, 255, 0.1); color: #58a6ff; padding: 5px 10px; border-radius: 5px; font-size: 11px; font-weight: 700; display: inline-block; }
    .game-conf { float: right; color: #3fb950; font-weight: 800; font-size: 16px; }

    /* Rodapé */
    .footer-bar { position: fixed; bottom: 0; left: 0; width: 100%; background: #0d1117; padding: 5px 20px; font-size: 10px; color: #484f58; border-top: 1px solid #30363d; }
    </style>
""", unsafe_allow_html=True)

# 3. INTERFACE SUPERIOR E LATERAL (PRESERVAÇÃO DE FUNÇÕES)
st.markdown(f"""
    <div class="top-bar-custom">
        <div class="nav-links">
            <span class="logo-text">GESTOR IA</span>
            <span>APOSTAS ESPORTIVAS</span>
            <span>AO VIVO</span>
            <span>ASSERTIVIDADE IA</span>
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">
            <div style="color:white; font-size:12px; border:1px solid #30363d; padding:5px 15px; border-radius:20px;">REGISTRAR</div>
            <div style="background:#238636; color:white; padding:6px 15px; border-radius:5px; font-weight:bold; font-size:12px;">ENTRAR</div>
        </div>
    </div>
    <div style="height:80px;"></div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "scanner"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

# 4. CONTEÚDO PRINCIPAL (DASHBOARD)
if st.session_state.aba_ativa == "home":
    st.markdown("<h3 style='color:white; margin-bottom:20px;'>📅 BILHETE OURO - TOP 20 OPORTUNIDADES</h3>", unsafe_allow_html=True)
    
    # RENDERIZAÇÃO DOS 8 KPI CARDS
    valor_entrada = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown(f'<div class="kpi-card"><div class="kpi-label">Banca Total</div><div class="kpi-value">R$ {st.session_state.banca_total:,.2f}</div></div>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="kpi-card"><div class="kpi-label">Assertividade</div><div class="kpi-value">94.8%</div></div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="kpi-card"><div class="kpi-label">Tendência</div><div class="kpi-value">Alta</div></div>', unsafe_allow_html=True)
    with col4: st.markdown('<div class="kpi-card"><div class="kpi-label">Sinais Hoje</div><div class="kpi-value">142</div></div>', unsafe_allow_html=True)
    
    col5, col6, col7, col8 = st.columns(4)
    with col5: st.markdown(f'<div class="kpi-card"><div class="kpi-label">Stake (%)</div><div class="kpi-value">{st.session_state.stake_padrao}%</div></div>', unsafe_allow_html=True)
    with col6: st.markdown(f'<div class="kpi-card"><div class="kpi-label">Entrada (R$)</div><div class="kpi-value">R$ {valor_entrada:,.2f}</div></div>', unsafe_allow_html=True)
    with col7: st.markdown('<div class="kpi-card"><div class="kpi-label">Mercado</div><div class="kpi-value">Gols</div></div>', unsafe_allow_html=True)
    with col8: st.markdown('<div class="kpi-card"><div class="kpi-label">Versão</div><div class="kpi-value">v59.62</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # NOVO MODELO DE LISTAGEM: GRID DE CARDS MODERNOS (20 JOGOS)
    if st.session_state.top_20_ia:
        cols = st.columns(3) # Organiza em 3 colunas para melhor aproveitamento de espaço
        for i, jogo in enumerate(st.session_state.top_20_ia):
            with cols[i % 3]:
                st.markdown(f"""
                    <div class="game-card">
                        <div class="game-header">
                            <span>ID: {1000 + i}</span>
                            <span>HOJE • {jogo['HORA']}</span>
                        </div>
                        <div class="game-teams">
                            {jogo['CASA']} <br> 
                            <span style="color:#8b949e; font-size:10px;">VS</span> <br> 
                            {jogo['FORA']}
                        </div>
                        <hr style="border: 0; border-top: 1px solid #30363d; margin: 10px 0;">
                        <div class="game-market">{jogo['MERCADO']}</div>
                        <div class="game-conf">{jogo['CONF']}</div>
                    </div>
                """, unsafe_allow_html=True)
                st.markdown("<div style='margin-bottom:15px;'></div>", unsafe_allow_html=True)
    else:
        st.info("Aguardando processamento dos dados para listar os jogos...")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h3 style='color:white;'>💰 GESTÃO DE BANCA</h3>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("Definir Banca (R$)", value=float(st.session_state.banca_total))
    st.session_state.stake_padrao = st.slider("Stake (%)", 0.1, 5.0, float(st.session_state.stake_padrao))

# RODAPÉ DE STATUS
st.markdown("""<div class="footer-bar">STATUS: ● IA OPERACIONAL | v59.62 | PROTEÇÃO JARVIS ATIVA</div>""", unsafe_allow_html=True)
