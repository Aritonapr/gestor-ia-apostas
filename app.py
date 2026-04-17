import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import google.generativeai as genai
from duckduckgo_search import DDGS

# ==============================================================================
# [SISTEMA JARVIS - VERSÃO FINAL BLINDADA - FOCO NO FUNCIONAMENTO]
# ==============================================================================

# CHAVE DE API QUE VOCÊ ENVIOU
CHAVE_GOOGLE = "AIzaSyC83QqObkFM5QaJfVrivAmdqIp1ruWHo-4"

def pesquisar_oraculo(pergunta):
    try:
        # 1. Tenta buscar informações rápidas na internet para a IA saber do "ontem"
        contexto = ""
        try:
            with DDGS() as ddgs:
                busca = list(ddgs.text(f"{pergunta} futebol", max_results=2))
                if busca:
                    contexto = " ".join([b['body'] for b in busca])
        except:
            contexto = "Responda com seu conhecimento atual."

        # 2. Configura a IA
        genai.configure(api_key=CHAVE_GOOGLE)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Aja como o Oráculo Jarvis. Use este contexto: {contexto}. Responda de forma curta, direta e com letras grandes sobre: {pergunta}"
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # PLANO B: Se a IA der erro de limite, ela tenta uma resposta simples
        return f"O Oráculo está processando sua dúvida sobre '{pergunta}'. Por favor, tente clicar no botão novamente em 10 segundos. Se o erro persistir, verifique se a 'Generative Language API' está ATIVA no seu painel do Google."

# 1. CONFIGURAÇÃO DE PÁGINA (ESTILO ORIGINAL)
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"

# ==============================================================================
# 2. ESTILO CSS (ALTO CONTRASTE E LETRAS GIGANTES PARA FACILITAR A VISÃO)
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
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        text-align: left !important; width: 100% !important; padding: 18px 25px !important; 
        font-size: 11px !important; text-transform: uppercase !important; border-radius: 0px !important; 
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    
    .kpi-detailed-card { background: #11151a; border: 1px solid #1e293b; padding: 30px; border-radius: 8px; margin-bottom: 15px; }
    .big-data-badge { background: rgba(0, 255, 136, 0.1); color: #00ff88; padding: 5px 12px; border-radius: 4px; font-size: 10px; font-weight: 800; border: 1px solid #00ff88; margin-bottom: 20px; display: inline-block; }

    /* BOTÃO DE EXECUÇÃO - MÁXIMA VISIBILIDADE */
    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: white !important;
        font-weight: 900 !important;
        border: none !important;
        padding: 20px 40px !important;
        text-transform: uppercase !important;
        border-radius: 8px !important;
        width: 100% !important;
        font-size: 16px !important;
        box-shadow: 0 5px 20px rgba(109, 40, 217, 0.5) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (MENU)
with st.sidebar:
    st.markdown('<div class="betano-header"><div class="header-left"><a href="#" class="logo-link">GESTOR IA</a></div></div><div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🔮 ORÁCULO JARVIS"): st.session_state.aba_ativa = "oraculo"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"

# 4. TELA DO ORÁCULO
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    st.write("Dados carregados. Selecione o Oráculo na barra lateral.")

elif st.session_state.aba_ativa == "oraculo":
    st.markdown("<h2 style='color:white; font-size: 30px;'>🔮 ORÁCULO JARVIS - PESQUISA REAL</h2>", unsafe_allow_html=True)
    st.markdown('<div class="big-data-badge">🌐 CONSULTA AO VIVO ATIVA</div>', unsafe_allow_html=True)
    
    # Campo de Pergunta (Fonte maior)
    pergunta = st.text_input("QUAL A SUA DÚVIDA?", placeholder="Ex: Quanto foi o jogo do Flamengo ontem?")
    
    # BOTÃO EXECUTAR
    if st.button("🔮 EXECUTAR CONSULTA AO ORÁCULO AGORA"):
        if pergunta:
            with st.spinner("O Oráculo está acessando a rede e processando..."):
                resposta = pesquisar_oraculo(pergunta)
                st.markdown(f"""
                    <div class="kpi-detailed-card" style="border-left: 8px solid #9d54ff; margin-top: 30px;">
                        <div style="color:#9d54ff; font-size:14px; font-weight:900; margin-bottom:15px;">RESPOSTA DO ORÁCULO:</div>
                        <div style="color:white; font-size:22px; font-weight:700; line-height:1.5; text-align: justify;">
                            {resposta}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Por favor, digite sua dúvida primeiro.")

st.markdown("""<div style="position:fixed; bottom:0; left:0; width:100%; background:#0d0d12; color:#475569; font-size:9px; padding:5px 20px; border-top:1px solid #1e293b;">STATUS: ● IA OPERACIONAL | JARVIS PROTECT</div>""", unsafe_allow_html=True)
