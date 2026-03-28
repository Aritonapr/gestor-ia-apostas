import streamlit as st
import pandas as pd
import time
from datetime import datetime

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="GESTOR IA - DASHBOARD", layout="wide", initial_sidebar_state="expanded")

# --- BLOCO DE CSS E ESTILIZAÇÃO (IMUTÁVEL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }

    /* Estilização dos KPI Cards */
    .card-container {
        background: linear-gradient(145deg, #1a1a1a, #0d0d0d);
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #333;
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .card-container:hover {
        border-color: #00ff00;
        transform: translateY(-5px);
    }

    .card-title {
        font-size: 14px;
        color: #888;
        margin-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .card-value {
        font-size: 24px;
        font-weight: 700;
        color: #00ff00;
    }

    /* Estilização da Tabela de Jogos ao Vivo */
    .live-table-container {
        margin-top: 30px;
        background: #0d0d0d;
        border-radius: 12px;
        border: 1px solid #333;
        overflow: hidden;
    }

    .live-table-header {
        background: #1a1a1a;
        padding: 15px;
        border-bottom: 1px solid #333;
        font-weight: 700;
        color: #00ff00;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .live-row {
        display: grid;
        grid-template-columns: 1fr 2fr 1fr 1fr 1fr;
        padding: 12px 15px;
        border-bottom: 1px solid #222;
        align-items: center;
        font-size: 14px;
    }

    .live-row:hover {
        background: #151515;
    }

    .status-live {
        color: #ff4b4b;
        font-weight: bold;
        animation: blinker 1.5s linear infinite;
    }

    @keyframes blinker {
        50% { opacity: 0; }
    }

    .score-box {
        background: #333;
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: 700;
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# --- LÓGICA DE BACK-END (BOT INVISÍVEL) ---
if 'jogos_ao_vivo' not in st.session_state:
    # Simulando entrada de dados do Scanner
    st.session_state.jogos_ao_vivo = [
        {"minuto": "23'", "partida": "Flamengo vs Palmeiras", "placar": "1 - 0", "mercado": "Gols", "ia_confianca": "88%"},
        {"minuto": "12'", "partida": "Real Madrid vs Barcelona", "placar": "0 - 0", "mercado": "Cantos", "ia_confianca": "75%"},
        {"minuto": "85'", "partida": "Man. City vs Arsenal", "placar": "2 - 2", "mercado": "Gols", "ia_confianca": "92%"},
        {"minuto": "41'", "partida": "Bayern vs Dortmund", "placar": "1 - 0", "mercado": "Cantos", "ia_confianca": "81%"}
    ]

def draw_kpi_card(title, value):
    st.markdown(f"""
        <div class="card-container">
            <div class="card-title">{title}</div>
            <div class="card-value">{value}</div>
        </div>
    """, unsafe_allow_html=True)

# --- HEADER (IMUTÁVEL) ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0px; border-bottom: 2px solid #333; margin-bottom: 20px;">
        <h1 style="margin: 0; color: #ffffff; font-size: 28px;">GESTOR IA <span style="color: #00ff00;">v60.00</span></h1>
        <div style="text-align: right;">
            <span style="color: #888;">STATUS DO SISTEMA:</span> <span style="color: #00ff00;">● ONLINE</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://via.placeholder.com/150x50/000000/00FF00?text=LOGO+SCANNER", use_container_width=True)
    st.markdown("---")
    menu = st.radio("NAVEGAÇÃO", ["DASHBOARD PRINCIPAL", "GESTÃO DE BANCA", "SCANNER PRÉ-LIVE", "CONFIGURAÇÕES"])
    st.markdown("---")
    st.info("Bot Operando em Segundo Plano")

# --- CONTEÚDO PRINCIPAL ---

# 8 KPI CARDS (Conforme solicitado na Versão 59.00 e mantido aqui)
col1, col2, col3, col4 = st.columns(4)
col5, col6, col7, col8 = st.columns(4)

with col1: draw_kpi_card("ASSERTIVIDADE HOJE", "84.5%")
with col2: draw_kpi_card("BANCA ATUAL", "R$ 1.250,00")
with col3: draw_kpi_card("LUCRO LÍQUIDO", "R$ 412,10")
with col4: draw_kpi_card("ENTRADAS REALIZADAS", "12")
with col5: draw_kpi_card("MERCADO DE GOLS", "78%")
with col6: draw_kpi_card("MERCADO DE CANTOS", "82%")
with col7: draw_kpi_card("ROI MENSAL", "+15.4%")
with col8: draw_kpi_card("STOP LOSS", "R$ 150,00")

st.markdown("<br>", unsafe_allow_html=True)

# --- TABELA DE JOGOS AO VIVO (IMPLEMENTAÇÃO SOLICITADA) ---
st.markdown("""
    <div class="live-table-container">
        <div class="live-table-header">
            <span>⚽ JOGOS AO VIVO AGORA</span>
            <span style="font-size: 12px; color: #888;">Sincronizado via IA</span>
        </div>
""", unsafe_allow_html=True)

# Cabeçalho da Tabela
st.markdown("""
    <div class="live-row" style="background: #111; font-weight: bold; color: #888; border-bottom: 1px solid #333;">
        <div>TEMPO</div>
        <div>PARTIDA</div>
        <div>PLACAR</div>
        <div>MERCADO</div>
        <div>CONFIANÇA</div>
    </div>
""", unsafe_allow_html=True)

# Loop para injetar os dados do session_state na tabela
for jogo in st.session_state.jogos_ao_vivo:
    st.markdown(f"""
        <div class="live-row">
            <div class="status-live">{jogo['minuto']}</div>
            <div style="font-weight: 600;">{jogo['partida']}</div>
            <div><span class="score-box">{jogo['placar']}</span></div>
            <div style="color: #aaa;">{jogo['mercado']}</div>
            <div style="color: #00ff00; font-weight: bold;">{jogo['ia_confianca']}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- LOG DE ATIVIDADES (RODAPÉ) ---
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("LOG DE PROCESSAMENTO IA (BACK-END)", expanded=False):
    st.code(f"[{datetime.now().strftime('%H:%M:%S')}] Scanner iniciado...\n[{datetime.now().strftime('%H:%M:%S')}] Analisando 4 partidas ao vivo...\n[{datetime.now().strftime('%H:%M:%S')}] Assertividade recalculada com sucesso.")
