import streamlit as st
import pandas as pd
import os

# ==============================================================================
# [PROTOCOLO JARVIS v67.0 - ESTABILIDADE MÁXIMA]
# DIRETRIZ: CORREÇÃO DE DEPENDÊNCIA ALTAIR E BOOT 2026
# ==============================================================================

# 1. BOOT PRIORITÁRIO (LINHA OBRIGATÓRIA)
st.set_page_config(page_title="GESTOR IA 2026", layout="wide")

# 2. INICIALIZAÇÃO DE MEMÓRIA (BLINDADA)
if 'aba' not in st.session_state: st.session_state['aba'] = "home"
if 'banca' not in st.session_state: st.session_state['banca'] = 1000.0

# 3. ESTILO CSS (ZERO WHITE PRO - MODO SEGURO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: white !important;
    }
    header, [data-testid="stHeader"] { display: none !important; }
    
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        border-right: 1px solid #1e293b !important; 
    }
    
    .card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; margin-bottom: 10px;
    }
    
    .logo-text { color: #9d54ff; font-weight: 900; font-size: 24px; text-align: center; margin-bottom: 20px; }
    
    .footer { 
        position: fixed; bottom: 0; left: 0; width: 100%; 
        background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 0 20px; font-size: 9px; color: #475569; 
    }
    </style>
""", unsafe_allow_html=True)

#
