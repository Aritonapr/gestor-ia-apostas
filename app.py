import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# ==============================================================================
# [PROTOCOLO JARVIS v62.3 - PROTEÇÃO VISUAL + EXPANSÃO 20 JOGOS]
# ==============================================================================

# 1. CONFIGURAÇÃO DA PÁGINA (Mantendo Layout Wide para os 20 jogos)
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# 2. MEMÓRIA DO SISTEMA (Garante que o bot não perca dados ao navegar)
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state:
    st.session_state.banca_total = 1000.00

# 3. ESTILO CSS "ZERO WHITE PRO" (PRESERVANDO SEU DESIGN)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    /* Fundo Dark e Fontes */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: white;
    }

    /* Esconder Header Original do Streamlit */
    header {visibility: hidden;}
    
    /* Seu Header Personalizado */
    .custom-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 65px;
        background-color: #001a4d;
        display: flex;
        align-items: center;
        padding: 0 40px;
        z-index: 9999;
        border-bottom: 1px solid #1e293b;
    }

    /* Sidebar Estilizada */
    [data-testid="stSidebar"] {
        background-color: #11151a !important;
        border-right: 1px solid #1e293b !important;
    }

    /* Estilo dos Cards de Jogo no Live */
    .live-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        transition: 0.3s;
    }
    .live-card:hover {
        border-color: #06b6d4;
        background: #1c222a;
    }
    
    .status-live {
        color: #ff4b4b;
        font-size: 11px;
        font-weight: bold;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# 4. COMPONENTES VISUAIS FIXOS
st.markdown('<div class="custom-header"><h2 style="color: #9d54ff; margin:0; font-weight:900;">GESTOR IA</h2></div>', unsafe_allow_html=True)

# 5. MENU LATERAL (SIDEBAR)
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size:12px; color:#475569;'>🎯 MENU DE COMANDOS</h3>", unsafe_allow_html=True)
    
    if st.button("🎯 SCANNER PRÉ-LIVE"):
        st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"):
        st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"):
        st.session_state.aba_ativa = "gestao"
    if st.button("📅 BILHETE OURO"):
        st.session_state.aba_ativa = "home"
    
    st.markdown("<br>"*10, unsafe_allow_html=True)
    st.info(f"STATUS: IA OPERACIONAL | v62.3")

# 6. LÓGICA DAS ABAS

# --- ABA: BILHETE OURO (HOME) ---
if st.session_state.aba_ativa == "home":
    st.markdown("<h1>📅 BILHETE OURO</h1>", unsafe_allow_html=True)
    st.write("Exibindo as melhores oportunidades do dia...")
    # Aqui entraria sua tabela de jogos do dia

# --- ABA: SCANNER PRÉ-LIVE ---
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h1>🎯 SCANNER PRÉ-LIVE - ANÁLISE MANUAL</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("Selecione a Liga:", ["PREMIER LEAGUE", "BRASILEIRÃO", "LA LIGA"])
    with col2:
        st.selectbox("Selecione a Partida:", ["Arsenal x Chelsea", "Flamengo x Palmeiras"])
    st.button("GERAR LEITURA JARVIS")

# --- ABA: SCANNER EM TEMPO REAL (AQUI ESTÃO OS 20 JOGOS) ---
elif st.session_state.aba_ativa == "live":
    st.markdown("<h1 style='color:white;'>📡 SCANNER EM TEMPO REAL (20 JOGOS)</h1>", unsafe_allow_html=True)
    
    # Simulação de 20 Jogos (Para o bot ler em tempo real)
    jogos = [
        {"time": "Flamengo vs Corinthians", "placar": "1-1", "ap1": 82, "tempo": "74'"},
        {"time": "Arsenal vs Chelsea", "placar": "0-0", "ap1": 51, "tempo": "10'"},
        {"time": "Real Madrid vs Barcelona", "placar": "2-1", "ap1": 70, "tempo": "80'"},
        {"time": "Man City vs United", "placar": "3-0", "ap1": 91, "tempo": "65'"},
        {"time": "Palmeiras vs Santos", "placar": "1-0", "ap1": 65, "tempo": "40'"},
        {"time": "Bayern vs Dortmund", "placar": "2-2", "ap1": 88, "tempo": "88'"},
        {"time": "Inter vs Milan", "placar": "0-1", "ap1": 45, "tempo": "22'"},
        {"time": "Liverpool vs Spurs", "placar": "1-1", "ap1": 77, "tempo": "55'"},
        {"time": "PSG vs Marseille", "placar": "4-0", "ap1": 95, "tempo": "70'"},
        {"time": "Juventus vs Roma", "placar": "0-0", "ap1": 30, "tempo": "15'"},
        {"time": "Porto vs Benfica", "placar": "1-2", "ap1": 68, "tempo": "60'"},
        {"time": "Ajax vs PSV", "placar": "2-0", "ap1": 72, "tempo": "35'"},
        {"time": "Galo vs Cruzeiro", "placar": "1-0", "ap1": 80, "tempo": "50'"},
        {"time": "Grêmio vs Inter", "placar": "0-0", "ap1": 55, "tempo": "28'"},
        {"time": "Boca vs River", "placar": "1-1", "ap1": 89, "tempo": "82'"},
        {"time": "Napoli vs Lazio", "placar": "2-1", "ap1": 63, "tempo": "44'"},
        {"time": "Benfica vs Sporting", "placar": "0-1", "ap1": 40, "tempo": "12'"},
        {"time": "Sevilla vs Betis", "placar": "3-2", "ap1": 85, "tempo": "90'"},
        {"time": "Vasco vs São Paulo", "placar": "0-0", "ap1": 48, "tempo": "20'"},
        {"time": "Leipzig vs Leverkusen", "placar": "1-1", "ap1": 74, "tempo": "58'"}
    ]

    # Criando a Grade de 20 jogos (4 colunas)
    col_grid = st.columns(4)
    
    for i, jogo in enumerate(jogos):
        with col_grid[i % 4]:
            # Cor da pressão dinâmica
            cor_pressao = "#00ff88" if jogo['ap1'] > 80 else "#06b6d4"
            
            st.markdown(f"""
                <div class="live-card">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span class="status-live">● AO VIVO</span>
                        <span style="color:#8b949e; font-size:10px;">{jogo['tempo']}</span>
                    </div>
                    <div style="margin:10px 0; font-weight:bold; font-size:13px;">{jogo['time']}</div>
                    <div style="font-size:18px; font-weight:900; color:#06b6d4;">{jogo['placar']}</div>
                    <div style="margin-top:10px; font-size:10px; color:#94a3b8;">PRESSÃO IA: <b>{jogo['ap1']}%</b></div>
                    <div style="background:#30363d; height:4px; width:100%; border-radius:2px; margin-top:5px;">
                        <div style="background:{cor_pressao}; height:100%; width:{jogo['ap1']}%; border-radius:2px;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"DETALHES JOGO {i+1}", key=f"btn_{i}"):
                st.toast(f"Carregando dados profundos de {jogo['time']}...")

# --- ABA: GESTÃO DE BANCA ---
elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h1>💰 GESTÃO DE BANCA</h1>", unsafe_allow_html=True)
    st.metric("Banca Atual", f"R$ {st.session_state.banca_total:.2f}")
    st.number_input("Nova Stake (%)", min_value=0.5, max_value=10.0, value=1.0)
