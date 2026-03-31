import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np

# ==============================================================================
# [PROTOCOLO v62.2 - EXPANSÃO LIVE 20 JOGOS + INTEGRIDADE ZERO WHITE]
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- MEMÓRIA DO SISTEMA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "live" # Iniciando na Live para teste
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# --- ESTILO CSS IMUTÁVEL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px; text-transform: uppercase; text-decoration: none; }
    
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    .live-card {
        background: #161b22; border: 1px solid #30363d; border-radius: 6px;
        padding: 12px; margin-bottom: 10px; transition: 0.3s;
    }
    .live-card:hover { border-color: #06b6d4; background: #1c222a; }
    .status-live { color: #ff4b4b; font-size: 10px; font-weight: bold; animation: blinker 1.5s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR & HEADER ---
with st.sidebar:
    st.markdown('<div class="betano-header"><div class="logo-link">GESTOR IA</div><div style="color:white; font-size:9.5px; font-weight:800; background:linear-gradient(90deg, #6d28d9, #06b6d4); padding:8px 20px; border-radius:5px;">LIVE PRO</div></div><div style="height:65px;"></div>', unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"

# --- LOGICA DA ABA LIVE (20 JOGOS) ---
if st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL (20 JOGOS)</h2>", unsafe_allow_html=True)
    
    # Criando 20 jogos fictícios para demonstração do Scanner
    jogos_simulados = []
    times_casa = ["Flamengo", "Arsenal", "Real Madrid", "Palmeiras", "Man City", "Inter", "Bayern", "PSG", "Chelsea", "Liverpool", "Juventus", "Ajax", "Porto", "Benfica", "Dortmund", "Napoli", "Galo", "Grêmio", "São Paulo", "Boca"]
    times_fora = ["Corinthians", "Chelsea", "Barcelona", "Santos", "United", "Milan", "Leverkusen", "Marseille", "Spurs", "Everton", "Roma", "PSV", "Sporting", "Braga", "Leipzig", "Lazio", "Cruzeiro", "Inter-RS", "Vasco", "River"]

    for i in range(20):
        ap1 = np.random.randint(30, 95)
        ap2 = np.random.randint(20, 80)
        jogos_simulados.append({
            "TIME": f"{times_casa[i]} vs {times_fora[i]}",
            "PLACAR": f"{np.random.randint(0,3)} - {np.random.randint(0,2)}",
            "TEMPO": f"{np.random.randint(10,85)}'",
            "AP1": ap1,
            "AP2": ap2,
            "CANTOS": np.random.randint(0,14),
            "TENDÊNCIA": "🔥 GOL PRÓXIMO" if ap1 > 80 else "🎯 OVER CANTO" if ap1 > 65 else "📉 ESTÁVEL"
        })

    # Renderização em Grid (4 colunas x 5 linhas = 20 jogos)
    cols = st.columns(4)
    for idx, jogo in enumerate(jogos_simulados):
        with cols[idx % 4]:
            cor_ap = "#00ff88" if jogo['AP1'] > 75 else "#06b6d4"
            st.markdown(f"""
                <div class="live-card">
                    <div style="display:flex; justify-content:space-between;">
                        <span class="status-live">● AO VIVO</span>
                        <span style="color:#8b949e; font-size:10px;">{jogo['TEMPO']}</span>
                    </div>
                    <div style="color:white; font-weight:800; font-size:12px; margin:8px 0;">{jogo['TIME']}</div>
                    <div style="color:#06b6d4; font-size:16px; font-weight:900; margin-bottom:5px;">{jogo['PLACAR']}</div>
                    <div style="display:flex; justify-content:space-between; font-size:10px; color:#94a3b8;">
                        <span>PRESSÃO (AP1): <b style="color:{cor_ap};">{jogo['AP1']}</b></span>
                        <span>CANTOS: <b style="color:white;">{jogo['CANTOS']}</b></span>
                    </div>
                    <div style="background:#30363d; height:3px; width:100%; border-radius:2px; margin-top:8px;">
                        <div style="background:{cor_ap}; height:100%; width:{jogo['AP1']}%; border-radius:2px;"></div>
                    </div>
                    <div style="margin-top:8px; font-size:9px; font-weight:bold; color:{cor_ap}; text-align:center;">
                        {jogo['TENDÊNCIA']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"ANALISAR {idx+1}", key=f"btn_{idx}"):
                st.toast(f"Analisando {jogo['TIME']}...")

# --- RODAPÉ ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v62.2</div><div>20 JOGOS MONITORADOS SIMULTANEAMENTE</div></div>""", unsafe_allow_html=True)
