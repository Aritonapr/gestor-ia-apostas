import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import google.generativeai as genai
from duckduckgo_search import DDGS

# ==============================================================================
# [SISTEMA JARVIS - VERSÃO FINAL COM BOTÃO DE EXECUÇÃO]
# ==============================================================================

# CHAVE DE API DO PRINT
CHAVE_GOOGLE = "AQ.Ab8RN6LMEbr5B86ihr0Ij6uGYrD8y4xxOjDFzmaT3mxV3BJVuA"

def pesquisar_oraculo(pergunta):
    try:
        # 1. Tenta buscar informações recentes
        contexto = ""
        try:
            with DDGS() as ddgs:
                busca = list(ddgs.text(f"{pergunta} futebol noticias", max_results=2))
                contexto = " ".join([b['body'] for b in busca])
        except:
            pass

        # 2. Configura a IA com a chave do seu print
        genai.configure(api_key=CHAVE_GOOGLE)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Você é o Oráculo Jarvis. Responda de forma curta e objetiva. Notícias atuais: {contexto}. Pergunta: {pergunta}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "O Oráculo recebeu sua pergunta! Se a resposta não aparecer, verifique se a chave de API no seu painel do Google está com as permissões de 'Generative Language API' ativas."

# 1. CONFIGURAÇÃO DE PÁGINA (VISUAL ORIGINAL)
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# MEMÓRIA
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"

# ==============================================================================
# 2. ESTILO CSS (SEU LAYOUT ORIGINAL PRESERVADO - ALTO CONTRASTE)
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
    [data-testid="stMainBlockContainer"] { padding: 85px 40 paradox 40px !important; }
    
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
    
    .kpi-detailed-card { background: #11151a; border: 1px solid #1e293b; padding: 25px; border-radius: 8px; margin-bottom: 15px; }
    .big-data-badge { background: rgba(0, 255, 136, 0.1); color: #00ff88; padding: 5px 12px; border-radius: 4px; font-size: 10px; font-weight: 800; border: 1px solid #00ff88; margin-bottom: 20px; display: inline-block; }
    
    /* BOTÃO DE EXECUÇÃO LARGO E COLORIDO PARA FACILITAR A VISÃO */
    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: white !important;
        font-weight: 900 !important;
        border: none !important;
        padding: 15px 30px !important;
        text-transform: uppercase !important;
        border-radius: 6px !important;
        width: 100% !important;
        font-size: 14px !important;
        margin-top: 10px !important;
        box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important;
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
    st.info("Sistema Jarvis Operacional. Selecione uma opção na barra lateral.")

elif st.session_state.aba_ativa == "oraculo":
    st.markdown("<h2 style='color:white;'>🔮 ORÁCULO JARVIS - INTELIGÊNCIA REAL</h2>", unsafe_allow_html=True)
    st.markdown('<div class="big-data-badge">🌐 CONSULTA AO VIVO ATIVA</div>', unsafe_allow_html=True)
    
    # Campo de Pergunta
    pergunta = st.text_input("DIGITE SUA PERGUNTA ABAIXO:", placeholder="Ex: Quanto foi o último jogo do Flamengo?")
    
    # BOTÃO PARA EXECUTAR
    if st.button("🔮 EXECUTAR CONSULTA AO ORÁCULO AGORA"):
        if pergunta:
            with st.spinner("O Oráculo está consultando a rede..."):
                resposta = pesquisar_oraculo(pergunta)
                st.markdown(f"""
                    <div class="kpi-detailed-card" style="border-left: 5px solid #9d54ff; margin-top: 25px;">
                        <div style="color:#9d54ff; font-size:12px; font-weight:900; margin-bottom:12px;">RESPOSTA DO ORÁCULO:</div>
                        <div style="color:white; font-size:16px; line-height:1.6; text-align: justify;">
                            {resposta}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Por favor, digite sua dúvida antes de clicar no botão.")

st.markdown("""<div style="position:fixed; bottom:0; left:0; width:100%; background:#0d0d12; color:#475569; font-size:9px; padding:5px 20px; border-top:1px solid #1e293b;">STATUS: ● IA OPERACIONAL | JARVIS PROTECT</div>""", unsafe_allow_html=True)
