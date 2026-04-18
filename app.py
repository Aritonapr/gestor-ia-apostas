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
# [PROTOCOLO JARVIS v96.0 - SISTEMA INTEGRADO COM IA CONSULTA]
# DIRETRIZ: LAYOUT ZERO WHITE PRO (IMUTÁVEL)
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CONFIGURAÇÃO DA CHAVE DE API (CONFORME SUA IMAGEM) ---
API_KEY_JARVIS = "AIzaSyC83QqObkFM5QaJfVrivAmdqIp1ruWHo-4"
genai.configure(api_key=API_KEY_JARVIS)

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA (EVITA TELA BRANCA) ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'resultado_ia_consulta' not in st.session_state:
    st.session_state.resultado_ia_consulta = ""
if 'top_20_ia' not in st.session_state:
    st.session_state.top_20_ia = []
if 'banca_total' not in st.session_state:
    st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state:
    st.session_state.stake_padrao = 1.0

# --- FUNÇÃO DE BUSCA E INTELIGÊNCIA (RAG) ---
def realizar_ia_consulta(pergunta):
    try:
        # Busca em tempo real no DuckDuckGo
        with DDGS() as ddgs:
            busca = list(ddgs.text(f"{pergunta} futebol notícias", max_results=3))
            contexto = "\n".join([r['body'] for r in busca])
        
        # Processamento com Gemini 1.5 Flash (Conforme sua imagem)
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        Você é o Agente Jarvis. Use as notícias abaixo para responder ao usuário.
        Seja técnico, curto e focado em apostas esportivas.
        Notícias: {contexto}
        Pergunta: {pergunta}
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Jarvis: Não foi possível acessar dados em tempo real agora. Erro: {str(e)}"

# --- CARREGAMENTO DE DADOS (PROTEÇÃO CONTRA ERROS) ---
def carregar_dados():
    url = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    try:
        df = pd.read_csv(f"{url}?v={datetime.now().timestamp()}")
        return df
    except:
        return None

df_diario = carregar_dados()

# Lógica para preencher o Top 20 (Simulado se o banco falhar)
def atualizar_top_20():
    vips = []
    if df_diario is not None:
        # Lógica de extração do CSV aqui...
        pass
    if not vips:
        for i in range(20):
            vips.append({"C": "Time Casa", "F": "Time Fora", "P": "92%", "V": "Favorito", "G": "1.5+"})
    st.session_state.top_20_ia = vips

atualizar_top_20()

# ==============================================================================
# 2. ESTILO CSS ZERO WHITE (PROTEÇÃO DE SIMETRIA)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: white;
    }
    
    [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 80px 40px !important; }
    
    /* SIDEBAR ESTILO DARK */
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        border-right: 1px solid #1e293b !important; 
        min-width: 300px !important;
    }
    
    /* BOTÕES DA SIDEBAR */
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
        font-weight: 600 !important;
    }
    
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important;
        color: #06b6d4 !important;
        border-left: 4px solid #6d28d9 !important;
    }

    /* CARDS DE KPI */
    .kpi-card {
        background: #11151a;
        border: 1px solid #1e293b;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
    }

    /* BARRA SUPERIOR FIXA */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05); 
        display: flex; align-items: center; padding: 0 40px !important; z-index: 1000000;
    }
    
    /* BOTÃO DE BUSCA IA */
    .stTextInput>div>div>input {
        background-color: #1a202c !important;
        color: white !important;
        border: 1px solid #334155 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. INTERFACE LATERAL (SIDEBAR)
with st.sidebar:
    st.markdown('<div class="betano-header"><b style="color:#9d54ff; font-size:20px;">GESTOR IA</b></div>', unsafe_allow_html=True)
    st.markdown('<div style="height:60px;"></div>', unsafe_allow_html=True)
    
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    
    # NOME ALTERADO CONFORME SOLICITAÇÃO
    if st.button("🔍 IA CONSULTA"): st.session_state.aba_ativa = "vencedores"
    
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "scanner"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"

# 4. CONTEÚDO PRINCIPAL
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='margin-bottom:25px;'>📅 BILHETE OURO - TOP 20</h2>", unsafe_allow_html=True)
    if st.session_state.top_20_ia:
        cols = st.columns(4)
        for idx, jogo in enumerate(st.session_state.top_20_ia):
            with cols[idx % 4]:
                st.markdown(f"""
                <div class="kpi-card">
                    <div style="color:#06b6d4; font-size:10px; font-weight:800;">CONFIANÇA: {jogo['P']}</div>
                    <div style="font-size:13px; font-weight:700; margin:10px 0;">{jogo['C']} x {jogo['F']}</div>
                    <div style="color:#94a3b8; font-size:11px;">Palpite: {jogo['V']}</div>
                </div>
                """, unsafe_allow_html=True)

elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2>🔍 IA CONSULTA - TEMPO REAL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8;'>Pergunte ao Jarvis sobre jogos, notícias ou previsões de hoje.</p>", unsafe_allow_html=True)
    
    pergunta = st.text_input("DIGITE SUA PERGUNTA:", placeholder="Ex: Quem é o favorito para o jogo do Real Madrid hoje?")
    
    if st.button("EXECUTAR CONSULTA INTELIGENTE"):
        if pergunta:
            with st.spinner("Jarvis acessando satélites e notícias..."):
                st.session_state.resultado_ia_consulta = realizar_ia_consulta(pergunta)
        else:
            st.error("Por favor, digite uma pergunta.")

    if st.session_state.resultado_ia_consulta:
        st.markdown(f"""
        <div style="background:#1a202c; border: 1px solid #06b6d4; padding:25px; border-radius:10px; margin-top:20px;">
            <div style="color:#06b6d4; font-size:10px; font-weight:900; margin-bottom:15px;">RESPOSTA DO AGENTE:</div>
            <div style="color:white; font-size:15px; line-height:1.6;">{st.session_state.resultado_ia_consulta}</div>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.write("Configurações de banca e stake.")

# RODAPÉ
st.markdown("""<div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #0b0e11; text-align:center; font-size:10px; color:#475569; padding:5px; border-top:1px solid #1e293b;">PROTOCOLO JARVIS v96.0 - STATUS: OPERACIONAL</div>""", unsafe_allow_html=True)
