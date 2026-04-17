import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import google.generativeai as genai

# ==============================================================================
# [SISTEMA JARVIS - BOTÃO DE EXECUÇÃO TOTAL]
# ==============================================================================

# CHAVE DE CONFIGURAÇÃO (Procure a que começa com AIza...)
CHAVE_GOOGLE = "AQ.Ab8RN6LMEbr5B86ihr0Ij6uGYrD8y4xxOjDFzmaT3mxV3BJVuA" 

def pesquisar_oraculo(pergunta):
    # Se a chave não começar com AIza, avisamos o usuário de forma amigável
    if not CHAVE_GOOGLE.startswith("AIza"):
        return f"Sua chave de API parece estar incorreta. Ela deve começar com 'AIza'. Mas aqui está uma resposta de teste: O jogo do {pergunta} está sendo analisado pelo sistema!"
    
    try:
        genai.configure(api_key=CHAVE_GOOGLE)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Responda de forma curta e profissional para um apostador: {pergunta}")
        return response.text
    except:
        return "Erro técnico: Verifique se sua chave do Google AI Studio está ativa e correta."

# 1. CONFIGURAÇÃO DE PÁGINA (VISUAL ORIGINAL)
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"

# ==============================================================================
# 2. ESTILO CSS (SEU LAYOUT ORIGINAL 'ZERO WHITE' PRESERVADO)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none !important; border-bottom: 2px solid #9d54ff; }
    
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    
    .kpi-detailed-card { background: #11151a; border: 1px solid #1e293b; padding: 20px 18px; border-radius: 8px; margin-bottom: 15px; }
    .big-data-badge { background: rgba(0, 255, 136, 0.1); color: #00ff88; padding: 5px 12px; border-radius: 4px; font-size: 10px; font-weight: 800; border: 1px solid #00ff88; margin-bottom: 20px; display: inline-block; }
    
    /* BOTÃO DE EXECUÇÃO - DESTAQUE TOTAL */
    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: white !important;
        font-weight: 900 !important;
        border: none !important;
        padding: 15px 30px !important;
        text-transform: uppercase !important;
        border-radius: 6px !important;
        width: 100% !important;
        font-size: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown('<div class="betano-header"><div class="header-left"><a href="#" class="logo-link">GESTOR IA</a></div></div><div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🔮 ORÁCULO JARVIS"): st.session_state.aba_ativa = "oraculo"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"

# 4. TELAS
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    st.write("Dados da IA carregados com sucesso.")

elif st.session_state.aba_ativa == "oraculo":
    st.markdown("<h2 style='color:white;'>🔮 ORÁCULO JARVIS</h2>", unsafe_allow_html=True)
    st.markdown('<div class="big-data-badge">🌐 CONSULTA AO VIVO ATIVA</div>', unsafe_allow_html=True)
    
    pergunta = st.text_input("DIGITE SUA DÚVIDA:", placeholder="Ex: Quanto foi o jogo do Flamengo?")
    executar = st.button("🔮 EXECUTAR CONSULTA AGORA")
    
    if executar and pergunta:
        with st.spinner("O Oráculo está pensando..."):
            resposta = pesquisar_oraculo(pergunta)
            st.markdown(f"""
                <div class="kpi-detailed-card" style="border-left: 5px solid #9d54ff; margin-top:20px;">
                    <div style="color:#9d54ff; font-size:11px; font-weight:900; margin-bottom:10px;">RESPOSTA:</div>
                    <div style="color:white; font-size:14px; line-height:1.6;">{resposta}</div>
                </div>
            """, unsafe_allow_html=True)

st.markdown("""<div style="position:fixed; bottom:0; width:100%; background:#0d0d12; color:#475569; font-size:9px; padding:5px 20px;">STATUS: ● IA OPERACIONAL | JARVIS PROTECT</div>""", unsafe_allow_html=True)
