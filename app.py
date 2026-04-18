import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np

# ==============================================================================
# [PROTOCOLO JARVIS v108.0 - ESTABILIDADE FINAL]
# DIRETRIZ: LAYOUT ZERO WHITE PRO (IMUTÁVEL) - ANTI-CRASH
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CHAVE DE API JARVIS ---
API_KEY_JARVIS = "AIzaSyC83QqObkFM5QaJfVrivAmdqIp1ruWHo-4"

# --- MOTOR DE CONSULTA JARVIS (IMPORTAÇÃO PROTEGIDA) ---
def realizar_ia_consulta(pergunta):
    try:
        # Só importa as bibliotecas quando o usuário clica no botão
        # Isso evita que o site dê erro ao abrir
        import google.generativeai as genai
        from duckduckgo_search import DDGS
        
        genai.configure(api_key=API_KEY_JARVIS)
        
        with DDGS() as ddgs:
            busca = list(ddgs.text(f"{pergunta} futebol notícias", max_results=2))
            contexto = "\n".join([r['body'] for r in busca])
        
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Analise curta para Jarvis: {pergunta}. Contexto: {contexto}"
        response = model.generate_content(prompt)
        return response.text

    except (ImportError, ModuleNotFoundError):
        return "⚙️ **ESTADO DE INSTALAÇÃO:** O servidor do GitHub ainda está configurando as ferramentas de IA. Aguarde 2 minutos e tente novamente. O layout está preservado."
    except Exception as e:
        return f"⚠️ **JARVIS OFFLINE:** {str(e)}"

# --- GERENCIAMENTO DE ABAS ---
if 'aba_active' not in st.session_state:
    st.session_state.aba_active = "home"
if 'resultado_ia_consulta' not in st.session_state:
    st.session_state.resultado_ia_consulta = ""
if 'top_20_ia' not in st.session_state:
    st.session_state.top_20_ia = [{"C": "Carregando", "F": "Dados", "P": "90%", "V": "Analise", "G": "1.5+"} for _ in range(20)]

# ==============================================================================
# 2. ESTILO CSS ZERO WHITE (IMUTÁVEL)
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
    
    if st.button("📅 BILHETE OURO"): st.session_state.aba_active = "home"
    if st.button("🔍 IA CONSULTA"): st.session_state.aba_active = "vencedores"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_active = "gestao"

# 4. CONTEÚDO
aba = st.session_state.aba_active

if aba == "home":
    st.markdown("<h2>📅 BILHETE OURO - TOP 20</h2>", unsafe_allow_html=True)
    cols = st.columns(4)
    for idx, jogo in enumerate(st.session_state.top_20_ia):
        with cols[idx % 4]:
            st.markdown(f"""<div class="kpi-card">
                <div style="color:#06b6d4; font-size:10px; font-weight:900;">PROBABILIDADE: {jogo['P']}</div>
                <div style="font-size:13px; font-weight:700; margin:8px 0;">{jogo['C']} x {jogo['F']}</div>
                <div style="color:#94a3b8; font-size:10px;">TIP: {jogo['V']}</div>
            </div>""", unsafe_allow_html=True)

elif aba == "vencedores":
    st.markdown("<h2>🔍 IA CONSULTA - AGENTE JARVIS</h2>", unsafe_allow_html=True)
    pergunta = st.text_input("QUAL A SUA DÚVIDA?", placeholder="Ex: Notícias do jogo do Flamengo?")
    
    if st.button("EXECUTAR CONSULTA"):
        if pergunta:
            with st.spinner("O Agente está acessando as notícias..."):
                st.session_state.resultado_ia_consulta = realizar_ia_consulta(pergunta)
        else:
            st.warning("Por favor, digite uma pergunta.")

    if st.session_state.resultado_ia_consulta:
        st.markdown(f"""<div class="kpi-card" style="border-left: 5px solid #06b6d4; margin-top:20px;">
            <div style="color:white; font-size:14px; line-height:1.6;">{st.session_state.resultado_ia_consulta}</div>
        </div>""", unsafe_allow_html=True)

# RODAPÉ
st.markdown("""<div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #0b0e11; text-align:center; font-size:10px; color:#475569; padding:5px; border-top:1px solid #1e293b; z-index:1000;">PROTOCOLO JARVIS v108.0 - OPERACIONAL</div>""", unsafe_allow_html=True)
