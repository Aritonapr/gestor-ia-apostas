import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- BLOCO DE CSS (PRESERVADO E INTEGRADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
        background-color: #000000 !important;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    /* Header Estilizado */
    .main-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 20px;
        background-color: #050505;
        border-bottom: 1px solid #1e1e1e;
        margin-bottom: 25px;
    }

    /* Cards de KPI - Padrão Zero White */
    .kpi-card {
        background: #0a0a0a;
        border: 1px solid #1e1e1e;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
    }
    .kpi-title { color: #888; font-size: 12px; text-transform: uppercase; margin-bottom: 8px; }
    .kpi-value { color: #00ff00; font-size: 22px; font-weight: 700; }

    /* Tabela de Jogos ao Vivo */
    .live-container {
        background: #0a0a0a;
        border-radius: 8px;
        border: 1px solid #1e1e1e;
        margin-top: 20px;
    }
    .live-row {
        display: grid;
        grid-template-columns: 80px 1fr 100px 120px 100px;
        padding: 15px;
        border-bottom: 1px solid #151515;
        align-items: center;
    }
    .time-badge { color: #ff4b4b; font-weight: bold; }
    .score-badge { background: #1e1e1e; padding: 4px 10px; border-radius: 4px; }
    
    /* Sidebar Custom */
    [data-testid="stSidebar"] { border-right: 1px solid #1e1e1e; }
    </style>
""", unsafe_allow_html=True)

# --- INICIALIZAÇÃO DO ESTADO (BACK-END INVISÍVEL) ---
if 'banca_total' not in st.session_state:
    st.session_state.banca_total = 1250.00
if 'stake_padrao' not in st.session_state:
    st.session_state.stake_padrao = 1.0
if 'aba_atual' not in st.session_state:
    st.session_state.aba_atual = "DASHBOARD PRINCIPAL"

# Lógica de cálculo corrigida (Removido erro de sintaxe da imagem)
valor_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)

# Dados simulados para a tabela
jogos_data = [
    {"tempo": "23'", "jogo": "Raith Rvs vs Ayr", "placar": "1 - 0", "mercado": "Over 1.5 Gols", "conf": "57%"},
    {"tempo": "12'", "jogo": "Annan Athletic vs Stranraer", "placar": "0 - 0", "mercado": "Over 1.5 Gols", "conf": "57%"},
    {"tempo": "85'", "jogo": "Morton vs Arbroath", "placar": "2 - 2", "mercado": "Over 1.5 Gols", "conf": "57%"}
]

# --- HEADER FIXO ---
st.markdown(f"""
    <div class="main-header">
        <div style="font-size: 20px; font-weight: 700; color: #fff;">GESTOR IA <span style="color: #00ff00;">v60.00</span></div>
        <div style="color: #00ff00; font-size: 13px;">● SISTEMA JARVIS OPERACIONAL</div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR (ESTRUTURA FIXA) ---
with st.sidebar:
    st.markdown("<h3 style='color: #00ff00;'>NAVEGAÇÃO</h3>", unsafe_allow_html=True)
    
    # Botões de navegação que controlam o estado
    if st.button("🎯 SCANNER EM TEMPO REAL", use_container_width=True):
        st.session_state.aba_atual = "SCANNER EM TEMPO REAL"
    if st.button("📊 DASHBOARD PRINCIPAL", use_container_width=True):
        st.session_state.aba_atual = "DASHBOARD PRINCIPAL"
    if st.button("💰 GESTÃO DE BANCA", use_container_width=True):
        st.session_state.aba_atual = "GESTÃO DE BANCA"
    if st.button("⚙️ CONFIGURAÇÕES", use_container_width=True):
        st.session_state.aba_atual = "CONFIGURAÇÕES"
    
    st.markdown("---")
    st.write(f"Stake Atual: R$ {valor_stake:.2f}")
    st.info("Bot Operando em Segundo Plano")

# --- LÓGICA DE EXIBIÇÃO POR BOTÃO ---

if st.session_state.aba_atual == "DASHBOARD PRINCIPAL":
    # 8 KPI CARDS (Exibição padrão da Home)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="kpi-card"><div class="kpi-title">Assertividade</div><div class="kpi-value">84.5%</div></div>', unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="kpi-card"><div class="kpi-title">Banca</div><div class="kpi-value">R$ {st.session_state.banca_total}</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="kpi-card"><div class="kpi-title">Lucro</div><div class="kpi-value">R$ 412,10</div></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="kpi-card"><div class="kpi-title">Entradas</div><div class="kpi-value">12</div></div>', unsafe_allow_html=True)
    
    c5, c6, c7, c8 = st.columns(4)
    with c5: st.markdown('<div class="kpi-card"><div class="kpi-title">Gols</div><div class="kpi-value">78%</div></div>', unsafe_allow_html=True)
    with c6: st.markdown('<div class="kpi-card"><div class="kpi-title">Cantos</div><div class="kpi-value">82%</div></div>', unsafe_allow_html=True)
    with c7: st.markdown('<div class="kpi-card"><div class="kpi-title">ROI</div><div class="kpi-value">+15.4%</div></div>', unsafe_allow_html=True)
    with c8: st.markdown('<div class="kpi-card"><div class="kpi-title">Stop Loss</div><div class="kpi-value">R$ 150,00</div></div>', unsafe_allow_html=True)

elif st.session_state.aba_atual == "SCANNER EM TEMPO REAL":
    st.markdown("<h3 style='color: #00ff00;'>⚽ SCANNER DE JOGOS AO VIVO</h3>", unsafe_allow_html=True)
    
    # Injeção da Tabela dentro deste botão específico
    st.markdown('<div class="live-container">', unsafe_allow_html=True)
    st.markdown('<div class="live-row" style="color: #888; font-weight: bold; border-bottom: 1px solid #333;"><div>TEMPO</div><div>PARTIDA</div><div>PLACAR</div><div>MERCADO</div><div>CONF.</div></div>', unsafe_allow_html=True)
    
    for jogo in jogos_data:
        st.markdown(f"""
            <div class="live-row">
                <div class="time-badge">{jogo['tempo']}</div>
                <div style="font-weight: 600;">{jogo['jogo']}</div>
                <div><span class="score-badge">{jogo['placar']}</span></div>
                <div style="color: #aaa;">{jogo['mercado']}</div>
                <div style="color: #00ff00; font-weight: bold;">{jogo['conf']}</div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.aba_atual == "GESTÃO DE BANCA":
    st.markdown("### 🏦 Módulo de Gestão de Banca")
    st.write("Configurações de banca e stake...")

elif st.session_state.aba_atual == "CONFIGURAÇÕES":
    st.markdown("### ⚙️ Configurações do Sistema")
    st.session_state.stake_padrao = st.slider("Definir Stake (%)", 0.1, 5.0, st.session_state.stake_padrao)
