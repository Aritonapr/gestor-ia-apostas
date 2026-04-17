import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random
import requests
import google.generativeai as genai

# ==============================================================================
# [SISTEMA JARVIS - COM BOTÃO DE EXECUÇÃO E LAYOUT ORIGINAL]
# ==============================================================================

# CONFIGURAÇÃO DA IA (CHAVE INTEGRADA)
CHAVE_GOOGLE = "AQ.Ab8RN6LMEbr5B86ihr0Ij6uGYrD8y4xxOjDFzmaT3mxV3BJVuA" 
genai.configure(api_key=CHAVE_GOOGLE)

def pesquisar_oraculo(pergunta):
    try:
        # Modelo 1.5 Flash para resposta instantânea
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        Você é o Oráculo Jarvis. Um especialista em futebol e trading.
        Responda de forma curta, objetiva e com dados reais sobre: {pergunta}
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro na conexão com o cérebro da IA. Verifique sua chave ou tente novamente."

# 1. CONFIGURAÇÃO DE PÁGINA (ESTILO ORIGINAL)
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'top_20_ia' not in st.session_state:
    st.session_state.top_20_ia = [{"C": "Flamengo", "F": "Vasco", "P": "94%", "V": "FAVORITO"}] * 20

# ==============================================================================
# 2. ESTILO CSS (SEU LAYOUT ORIGINAL PRESERVADO)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none !important; border-bottom: 2px solid #9d54ff; padding-bottom: 2px; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }

    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    
    .kpi-detailed-card { background: #11151a; border: 1px solid #1e293b; padding: 20px 18px; border-radius: 8px; margin-bottom: 15px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    .big-data-badge { background: rgba(0, 255, 136, 0.1); color: #00ff88; padding: 5px 12px; border-radius: 4px; font-size: 10px; font-weight: 800; border: 1px solid #00ff88; margin-bottom: 20px; display: inline-block; }
    
    /* Estilo do Botão de Execução */
    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: white !important;
        font-weight: 900 !important;
        border: none !important;
        padding: 10px 25px !important;
        text-transform: uppercase !important;
        border-radius: 5px !important;
        cursor: pointer !important;
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left"><a href="#" class="logo-link">GESTOR IA</a></div>
            <div class="header-right"><div class="entrar-grad">ENTRAR</div></div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🔮 ORÁCULO JARVIS"): st.session_state.aba_ativa = "oraculo"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"

# ==============================================================================
# 4. LÓGICA DE TELAS
# ==============================================================================

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white; margin-bottom:10px;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    cols = st.columns(4)
    for idx, j in enumerate(st.session_state.top_20_ia[:4]):
        with cols[idx]:
            st.markdown(f"""<div class="kpi-detailed-card"><div style="color:#9d54ff; font-size:10px; font-weight:900;">CONF: {j['P']}</div><div style="color:white; font-size:12px;">{j['C']} vs {j['F']}</div></div>""", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "oraculo":
    st.markdown("<h2 style='color:white; margin-bottom:10px;'>🔮 ORÁCULO JARVIS - INTELIGÊNCIA REAL</h2>", unsafe_allow_html=True)
    st.markdown('<div class="big-data-badge">🌐 CONSULTA INSTANTÂNEA ATIVA</div>', unsafe_allow_html=True)
    
    # Pergunta e Botão
    pergunta = st.text_input("QUAL A SUA DÚVIDA?", placeholder="Digite aqui sua pergunta...")
    botao_executar = st.button("🔮 EXECUTAR CONSULTA AO ORÁCULO")
    
    if botao_executar and pergunta:
        with st.spinner("O Oráculo está processando..."):
            resposta = pesquisar_oraculo(pergunta)
            st.markdown(f"""
                <div class="kpi-detailed-card" style="border-left: 5px solid #9d54ff; margin-top: 20px;">
                    <div style="color:#9d54ff; font-size:12px; font-weight:900; margin-bottom:10px;">RESPOSTA DO ORÁCULO:</div>
                    <div style="color:white; font-size:14px; line-height:1.6; text-align: justify;">
                        {resposta}
                    </div>
                </div>
            """, unsafe_allow_html=True)
    elif botao_executar and not pergunta:
        st.warning("Por favor, digite uma pergunta antes de executar.")

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
