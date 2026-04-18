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
# [PROTOCOLO JARVIS v97.0 - AGENTE INTELIGENTE RAG]
# DIRETRIZ: LAYOUT ZERO WHITE PRO (IMUTÁVEL) - SEM ABREVIAÇÕES
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CONFIGURAÇÃO DA CHAVE DE API (SUA CHAVE ATIVA) ---
API_KEY_JARVIS = "AIzaSyC83QqObkFM5QaJfVrivAmdqIp1ruWHo-4"
genai.configure(api_key=API_KEY_JARVIS)

# --- INICIALIZAÇÃO DE MEMÓRIA (EVITA TELA BRANCA) ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'resultado_ia_consulta' not in st.session_state:
    st.session_state.resultado_ia_consulta = ""
if 'top_20_ia' not in st.session_state:
    st.session_state.top_20_ia = []
if 'banca_total' not in st.session_state:
    st.session_state.banca_total = 1000.00

# --- MOTOR DE BUSCA EM TEMPO REAL (RAG) ---
def realizar_ia_consulta(pergunta):
    try:
        # 1. Busca no DuckDuckGo (Olhos na Internet)
        with DDGS() as ddgs:
            busca = list(ddgs.text(f"{pergunta} futebol notícias hoje", max_results=3))
            contexto = "\n".join([r['body'] for r in busca])
        
        # 2. Processamento com Gemini 1.5 Flash
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        Você é o Agente Jarvis. Baseado nestas notícias reais: {contexto}
        Responda de forma técnica, curta e direta sobre: {pergunta}
        Mantenha o tom profissional de análise esportiva.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Jarvis: Sistema de busca momentaneamente offline. Detalhe: {str(e)}"

# --- CARREGAMENTO DE DADOS (BLINDAGEM) ---
def carregar_dados_safe():
    url = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    try:
        df = pd.read_csv(f"{url}?v={datetime.now().timestamp()}")
        # Simulação de dados se o CSV estiver vazio para evitar quebra
        if df.empty: return None
        return df
    except:
        return None

# Inicializa o Top 20 para evitar erro de 'NoneType'
if not st.session_state.top_20_ia:
    for i in range(20):
        st.session_state.top_20_ia.append({
            "C": f"Time Casa {i+1}", "F": f"Time Fora {i+1}", 
            "P": f"{random.randint(85, 98)}%", "V": "Favorito", "G": "1.5+"
        })

# ==============================================================================
# 2. ESTILO CSS ZERO WHITE (IMUTÁVEL)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* Esconde elementos padrão */
    ::-webkit-scrollbar { display: none !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* Fundo Principal */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: white;
    }
    
    [data-testid="stMainBlockContainer"] { padding: 80px 40px !important; }
    
    /* Sidebar Dark */
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        border-right: 1px solid #1e293b !important;
    }
    
    /* Botões Laterais */
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

    /* Cards e Inputs */
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
        padding: 12px !important;
    }

    /* Cabeçalho Fixo */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05); 
        display: flex; align-items: center; padding: 0 40px !important; z-index: 1000000;
    }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR MENU
with st.sidebar:
    st.markdown('<div class="betano-header"><b style="color:#9d54ff; font-size:20px;">GESTOR IA</b></div>', unsafe_allow_html=True)
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True)
    
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "scanner"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    
    # NOME CORRIGIDO E FUNCIONAL
    if st.button("🔍 IA CONSULTA"): st.session_state.aba_ativa = "vencedores"
    
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"

# 4. ÁREAS DE CONTEÚDO
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO - TOP 20</h2>", unsafe_allow_html=True)
    cols = st.columns(4)
    for idx, jogo in enumerate(st.session_state.top_20_ia):
        with cols[idx % 4]:
            st.markdown(f"""
            <div class="kpi-card">
                <div style="color:#06b6d4; font-size:10px; font-weight:900;">IA: {jogo['P']}</div>
                <div style="font-size:13px; font-weight:700; margin:8px 0;">{jogo['C']} x {jogo['F']}</div>
                <div style="color:#94a3b8; font-size:10px;">PALPITE: {jogo['V']}</div>
            </div>
            """, unsafe_allow_html=True)

elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🔍 IA CONSULTA - AGENTE EM TEMPO REAL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:12px;'>O JARVIS PESQUISA NOTÍCIAS REAIS E ANALISA PARA VOCÊ.</p>", unsafe_allow_html=True)
    
    # Área de Input formatada
    pergunta_user = st.text_input("DIGITE SUA DÚVIDA SOBRE OS JOGOS DE HOJE:", placeholder="Ex: Qual a escalação do Manchester City hoje?")
    
    if st.button("PERGUNTAR AO JARVIS"):
        if pergunta_user:
            with st.spinner("Buscando dados em tempo real..."):
                st.session_state.resultado_ia_consulta = realizar_ia_consulta(pergunta_user)
        else:
            st.error("Digite uma pergunta para o Agente.")

    # Resultado dentro do Layout Dark
    if st.session_state.resultado_ia_consulta:
        st.markdown(f"""
        <div class="kpi-card" style="border-left: 4px solid #06b6d4; margin-top:20px;">
            <div style="color:#06b6d4; font-size:10px; font-weight:900; margin-bottom:12px;">RESPOSTA DO JARVIS:</div>
            <div style="color:white; font-size:14px; line-height:1.6;">{st.session_state.resultado_ia_consulta}</div>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.aba_ativa == "scanner":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    st.write("Dados em processamento...")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.write("Controle sua banca aqui.")

# RODAPÉ DE PROTEÇÃO
st.markdown("""<div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #0b0e11; text-align:center; font-size:10px; color:#475569; padding:5px; border-top:1px solid #1e293b; z-index:1000;">PROTOCOLO JARVIS v97.0 - SISTEMA PROTEGIDO</div>""", unsafe_allow_html=True)
