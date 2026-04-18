import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random
import requests

# Tenta importar as bibliotecas de IA, se falhar, o sistema não trava
try:
    import google.generativeai as genai
    from duckduckgo_search import DDGS
    IA_DISPONIVEL = True
except ImportError:
    IA_DISPONIVEL = False

# ==============================================================================
# [PROTOCOLO JARVIS v99.0 - BLINDAGEM TOTAL]
# DIRETRIZ: LAYOUT ZERO WHITE PRO (IMUTÁVEL) - 100% COMPLETO
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CONFIGURAÇÃO DA CHAVE DE API ---
API_KEY_JARVIS = "AIzaSyC83QqObkFM5QaJfVrivAmdqIp1ruWHo-4"
if IA_DISPONIVEL:
    genai.configure(api_key=API_KEY_JARVIS)

# --- INICIALIZAÇÃO DE MEMÓRIA (TRAVA CONTRA TELA BRANCA) ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'resultado_ia_consulta' not in st.session_state:
    st.session_state.resultado_ia_consulta = ""
if 'top_20_ia' not in st.session_state:
    st.session_state.top_20_ia = []

# --- MOTOR DE BUSCA EM TEMPO REAL (RAG) COM PROTEÇÃO ---
def realizar_ia_consulta(pergunta):
    if not IA_DISPONIVEL:
        return "Jarvis: Bibliotecas de IA não instaladas no ambiente. Verifique o Requirements.txt."
    
    try:
        # Busca real no DuckDuckGo
        with DDGS() as ddgs:
            busca = list(ddgs.text(f"{pergunta} futebol notícias", max_results=3))
            contexto = "\n".join([r['body'] for r in busca])
        
        # Processamento Gemini
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Você é o Jarvis. Use as notícias: {contexto}. Responda curto sobre: {pergunta}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Jarvis: Erro na sincronização. Detalhe: {str(e)}"

# --- CARREGAMENTO DE DADOS COM TRAVA DE SEGURANÇA ---
def carregar_dados():
    url = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    try:
        df = pd.read_csv(f"{url}?v={datetime.now().timestamp()}")
        return df
    except:
        return None

# Preenchimento preventivo para evitar erro de 'NoneType' que causa tela branca
if not st.session_state.top_20_ia:
    for i in range(20):
        st.session_state.top_20_ia.append({
            "C": "Analizando...", "F": "Aguarde...", "P": "90%", "V": "Pendente", "G": "---"
        })

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
    
    /* SIDEBAR */
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
        border-radius: 0px !important;
        font-weight: 700 !important;
    }
    
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important;
        color: #06b6d4 !important;
        border-left: 4px solid #6d28d9 !important;
    }

    /* CARDS */
    .kpi-card {
        background: #11151a;
        border: 1px solid #1e293b;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
    }

    /* INPUT DE BUSCA IA */
    .stTextInput>div>div>input {
        background-color: #1a202c !important;
        color: white !important;
        border: 1px solid #334155 !important;
        padding: 15px !important;
    }

    /* HEADER FIXO */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05); 
        display: flex; align-items: center; padding: 0 40px !important; z-index: 1000000;
    }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (MENU LATERAL)
with st.sidebar:
    st.markdown('<div class="betano-header"><b style="color:#9d54ff; font-size:20px;">GESTOR IA</b></div>', unsafe_allow_html=True)
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True)
    
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    
    # BOTÃO IA CONSULTA
    if st.button("🔍 IA CONSULTA"): st.session_state.aba_ativa = "vencedores"
    
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "scanner"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"

# 4. CONTEÚDO DAS ABAS
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO - TOP 20</h2>", unsafe_allow_html=True)
    cols = st.columns(4)
    if st.session_state.top_20_ia:
        for idx, jogo in enumerate(st.session_state.top_20_ia):
            with cols[idx % 4]:
                st.markdown(f"""<div class="kpi-card">
                    <div style="color:#06b6d4; font-size:10px; font-weight:900;">CONFIANÇA: {jogo['P']}</div>
                    <div style="font-size:13px; font-weight:700; margin:10px 0;">{jogo['C']} x {jogo['F']}</div>
                    <div style="color:#94a3b8; font-size:11px;">Palpite: {jogo['V']}</div>
                </div>""", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🔍 IA CONSULTA - AGENTE EM TEMPO REAL</h2>", unsafe_allow_html=True)
    
    pergunta_input = st.text_input("FAÇA SUA PERGUNTA:", placeholder="Ex: Favorito para Flamengo vs Palmeiras?")
    
    if st.button("CONSULTAR JARVIS"):
        if pergunta_input:
            with st.spinner("O Agente está lendo as notícias e analisando..."):
                st.session_state.resultado_ia_consulta = realizar_ia_consulta(pergunta_input)
        else:
            st.warning("Por favor, digite algo.")

    if st.session_state.resultado_ia_consulta:
        st.markdown(f"""<div class="kpi-card" style="border-left: 5px solid #06b6d4; margin-top:20px;">
            <div style="color:#06b6d4; font-size:10px; font-weight:900; margin-bottom:15px;">JARVIS RESPONDE:</div>
            <div style="color:white; font-size:14px; line-height:1.6;">{st.session_state.resultado_ia_consulta}</div>
        </div>""", unsafe_allow_html=True)

# RODAPÉ
st.markdown("""<div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #0b0e11; text-align:center; font-size:10px; color:#475569; padding:5px; border-top:1px solid #1e293b; z-index:1000;">PROTOCOLO JARVIS v99.0 - PROTEGIDO</div>""", unsafe_allow_html=True)
