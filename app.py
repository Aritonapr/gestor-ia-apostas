import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random
import requests

# ==============================================================================
# [PROTOCOLO JARVIS v100.0 - ESTABILIDADE MÁXIMA]
# DIRETRIZ: LAYOUT ZERO WHITE PRO (IMUTÁVEL) - ANTI-CRASH
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CONFIGURAÇÃO DA CHAVE DE API ---
API_KEY_JARVIS = "AIzaSyC83QqObkFM5QaJfVrivAmdqIp1ruWHo-4"

# --- TENTA CONFIGURAR O GEMINI ---
try:
    import google.generativeai as genai
    genai.configure(api_key=API_KEY_JARVIS)
    GEMINI_OK = True
except:
    GEMINI_OK = False

# --- MOTOR DE BUSCA (COM PLANO B PARA EVITAR O ERRO DA SUA IMAGEM) ---
def realizar_ia_consulta(pergunta):
    contexto = ""
    try:
        # Tenta usar o DuckDuckGo, se não existir, ele pula para o Gemini direto
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            busca = list(ddgs.text(f"{pergunta} futebol", max_results=2))
            contexto = "\n".join([r['body'] for r in busca])
    except:
        contexto = "Nota: Pesquisa em tempo real indisponível. Usando base histórica."

    if GEMINI_OK:
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"Você é o Jarvis. Responda de forma curta sobre: {pergunta}. Contexto: {contexto}"
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Jarvis: Erro ao processar IA. {str(e)}"
    return "Jarvis: Sistema de Inteligência Offline. Verifique a chave API."

# --- INICIALIZAÇÃO DE SESSÃO (BLINDAGEM CONTRA TELA BRANCA) ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'resultado_ia_consulta' not in st.session_state:
    st.session_state.resultado_ia_consulta = ""
if 'top_20_ia' not in st.session_state:
    # Cria dados falsos iniciais para o layout nunca carregar vazio
    st.session_state.top_20_ia = [{"C": "Carregando...", "F": "Dados...", "P": "90%", "V": "Analise", "G": "1.5+"} for _ in range(20)]

# ==============================================================================
# 2. ESTILO CSS ZERO WHITE (PROTEÇÃO CONTRA DESMONTE)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    ::-webkit-scrollbar { display: none !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: white;
    }
    
    [data-testid="stMainBlockContainer"] { padding: 80px 40px !important; }
    
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        border-right: 1px solid #1e293b !important;
    }
    
    section[data-testid="stSidebar"] div.stButton > button {
        background-color: transparent !important;
        color: #94a3b8 !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        width: 100% !important;
        padding: 18px 25px !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        font-weight: 700 !important;
    }
    
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important;
        color: #06b6d4 !important;
        border-left: 4px solid #6d28d9 !important;
    }

    .kpi-card {
        background: #11151a;
        border: 1px solid #1e293b;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
    }

    .stTextInput>div>div>input {
        background-color: #1a202c !important;
        color: white !important;
        border: 1px solid #334155 !important;
        padding: 15px !important;
    }

    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05); 
        display: flex; align-items: center; padding: 0 40px !important; z-index: 1000000;
    }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown('<div class="betano-header"><b style="color:#9d54ff; font-size:20px;">GESTOR IA</b></div>', unsafe_allow_html=True)
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True)
    
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🔍 IA CONSULTA"): st.session_state.aba_ativa = "vencedores"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"

# 4. CONTEÚDO
if st.session_state.aba_ativa == "home":
    st.markdown("<h2>📅 BILHETE OURO - TOP 20</h2>", unsafe_allow_html=True)
    cols = st.columns(4)
    for idx, jogo in enumerate(st.session_state.top_20_ia):
        with cols[idx % 4]:
            st.markdown(f"""<div class="kpi-card">
                <div style="color:#06b6d4; font-size:10px; font-weight:900;">CONFIANÇA: {jogo['P']}</div>
                <div style="font-size:13px; font-weight:700; margin:10px 0;">{jogo['C']} x {jogo['F']}</div>
                <div style="color:#94a3b8; font-size:11px;">Palpite: {jogo['V']}</div>
            </div>""", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2>🔍 IA CONSULTA - AGENTE JARVIS</h2>", unsafe_allow_html=True)
    
    pergunta_input = st.text_input("DIGITE SUA PERGUNTA:", placeholder="Ex: Quem vence hoje entre City e Arsenal?")
    
    if st.button("EXECUTAR CONSULTA"):
        if pergunta_input:
            with st.spinner("O Agente está processando..."):
                st.session_state.resultado_ia_consulta = realizar_ia_consulta(pergunta_input)
        else:
            st.warning("Digite sua pergunta.")

    if st.session_state.resultado_ia_consulta:
        st.markdown(f"""<div class="kpi-card" style="border-left: 5px solid #06b6d4; margin-top:20px;">
            <div style="color:#06b6d4; font-size:10px; font-weight:900; margin-bottom:15px;">JARVIS RESPONDE:</div>
            <div style="color:white; font-size:14px; line-height:1.6;">{st.session_state.resultado_ia_consulta}</div>
        </div>""", unsafe_allow_html=True)

# RODAPÉ
st.markdown("""<div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #0b0e11; text-align:center; font-size:10px; color:#475569; padding:5px; border-top:1px solid #1e293b; z-index:1000;">PROTOCOLO JARVIS v100.0 - OPERACIONAL</div>""", unsafe_allow_html=True)
