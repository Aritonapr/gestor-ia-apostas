import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random
import requests
import google.generativeai as genai
from duckduckgo_search import DDGS

# ==============================================================================
# [SISTEMA JARVIS - FOCO TOTAL NO FUNCIONAMENTO DO ORÁCULO]
# ==============================================================================

# CONFIGURAÇÃO DA IA
CHAVE_GOOGLE = "AQ.Ab8RN6LMEbr5B86ihr0Ij6uGYrD8y4xxOjDFzmaT3mxV3BJVuA" 
genai.configure(api_key=CHAVE_GOOGLE)

def pesquisar_oraculo(pergunta):
    # Tenta buscar na internet, se falhar, a IA responde direto
    try:
        contexto = ""
        try:
            with DDGS() as ddgs:
                # Busca rápida de 2 resultados
                buscas = list(ddgs.text(f"{pergunta} esportes hoje", max_results=2))
                contexto = " ".join([b['body'] for b in buscas])
        except:
            contexto = "Use seu conhecimento geral para responder."

        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Você é o Oráculo Jarvis. Responda de forma curta para um apostador: {pergunta}. Contexto atual: {contexto}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "O Oráculo está processando. Por favor, tente enviar a pergunta novamente."

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide")

# --- MEMÓRIA DO SISTEMA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'top_20_ia' not in st.session_state:
    st.session_state.top_20_ia = [{"C": "Real Madrid", "F": "Barcelona", "P": "92%", "V": "FAV"}] * 20

# ==============================================================================
# 2. ESTILO CSS ORIGINAL (ZERO WHITE)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; color: white; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; display: flex; align-items: center; justify-content: space-between; padding: 0 40 paradox 40px !important; z-index: 1000000; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-decoration: none !important; border-bottom: 2px solid #9d54ff; }
    .nav-item { color: #ffffff !important; font-size: 9.5px !important; text-transform: uppercase; font-weight: 700 !important; text-decoration: none !important; margin-left: 15px;}
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    .kpi-detailed-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; margin-bottom: 15px; }
    .big-data-badge { background: rgba(0, 255, 136, 0.1); color: #00ff88; padding: 5px 12px; border-radius: 4px; font-size: 10px; font-weight: 800; border: 1px solid #00ff88; margin-bottom: 20px; display: inline-block; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; padding: 0 20px; font-size: 9px; color: #475569; display: flex; align-items: center; justify-content: space-between; }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR MENU
with st.sidebar:
    st.markdown('<div class="betano-header"><div class="header-left"><a href="#" class="logo-link">GESTOR IA</a><span class="nav-item">TRADING PRO</span></div></div><div style="height:65px;"></div>', unsafe_allow_html=True)
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🔮 ORÁCULO JARVIS"): st.session_state.aba_ativa = "oraculo"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"

# 4. TELAS
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    cols = st.columns(4)
    for idx, j in enumerate(st.session_state.top_20_ia[:4]):
        with cols[idx]:
            st.markdown(f'<div class="kpi-detailed-card"><div style="color:#9d54ff; font-size:10px;">CONF: {j["P"]}</div><div style="color:white; font-size:14px; font-weight:800;">{j["C"]} vs {j["F"]}</div></div>', unsafe_allow_html=True)

elif st.session_state.aba_ativa == "oraculo":
    st.markdown("<h2 style='color:white;'>🔮 ORÁCULO JARVIS</h2>", unsafe_allow_html=True)
    st.markdown('<div class="big-data-badge">🌐 PESQUISA AO VIVO</div>', unsafe_allow_html=True)
    
    # Campo de texto para pergunta
    pergunta = st.text_input("QUAL A SUA DÚVIDA?", key="input_oraculo")
    
    if pergunta:
        with st.spinner("Buscando resposta..."):
            resposta = pesquisar_oraculo(pergunta)
            st.markdown(f"""
                <div class="kpi-detailed-card" style="border-left: 5px solid #9d54ff;">
                    <div style="color:#9d54ff; font-size:11px; font-weight:900; margin-bottom:10px;">RESPOSTA:</div>
                    <div style="color:white; font-size:14px; line-height:1.6;">{resposta}</div>
                </div>
            """, unsafe_allow_html=True)

st.markdown('<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL</div><div>JARVIS v95.0</div></div>', unsafe_allow_html=True)
