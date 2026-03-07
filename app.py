import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="GESTOR IA APOSTAS", 
    layout="wide", 
    page_icon="⚽",
    initial_sidebar_state="expanded"
)

# --- 2. CSS DE ALTO NÍVEL (LIMPEZA TOTAL E ÍCONE ORIGINAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    /* 1. OCULTAR ELEMENTOS DESNECESSÁRIOS (SETINHA E HEADER) */
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stSidebarCollapse"] { display: none !important; } /* SOME COM A SETINHA */
    button[kind="headerNoPadding"] { display: none !important; } /* SOME COM O BOTÃO DA SETINHA */
    
    /* 2. AJUSTE DE ESPAÇAMENTO PARA NÃO ENCOSTAR NO SHARE */
    .block-container { 
        padding-top: 3.5rem !important; /* EMPURRA O CONTEÚDO PARA BAIXO DO SHARE */
        padding-bottom: 0rem !important; 
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    /* 3. SIDEBAR FIXA E ÍCONE ORIGINAL */
    [data-testid="stSidebar"] { 
        background-color: #0f171e; 
        border-right: 1px solid #f05a22; 
        width: 260px !important; 
    }
    
    .sidebar-header { 
        display: flex; align-items: center; padding: 20px 15px; 
        margin-bottom: 10px; border-bottom: 1px solid #1a242d;
    }
    
    /* O ÍCONE QUE VOCÊ GOSTA (Quadrado Laranja + Traço Branco) */
    .ai-logo-box { 
        background-color: #f05a22; width: 34px; height: 34px; 
        border-radius: 6px; display: flex; align-items: center; 
        justify-content: center; margin-right: 12px;
        box-shadow: 0 0 12px rgba(240,90,34,0.3);
    }
    .ai-logo-dash { width: 16px; height: 4px; background-color: white; border-radius: 2px; }
    
    .sidebar-title { 
        color: #f05a22; font-family: 'Orbitron', sans-serif; 
        font-size: 18px; font-weight: 900; letter-spacing: 1px;
    }
    
    /* Botões da Sidebar */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: 700 !important; height: 34px !important; line-height: 1 !important;
        border-radius: 4px !important; text-transform: uppercase; font-size: 10px !important;
        width: 100% !important; margin-bottom: 4px !important;
    }
    .stButton > button[kind="primary"] {
        background-color: rgba(240,90,34,0.1) !important; color: #f05a22 !important; border: 1px solid #f05a22 !important;
    }
    .cat-label { color: #5a6b79; font-size: 9px; font-weight: 800; margin-top: 15px; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 1px; }

    /* 4. CARDS E RESULTADOS */
    .radar-topo {
        background: rgba(26, 36, 45, 0.6); border-radius: 6px; padding: 6px 15px; margin-bottom: 15px;
        display: flex; align-items: center; border-left: 4px solid #f05a22;
    }
    .radar-label { font-family: 'Orbitron', sans-serif; font-weight: 700; color: #f05a22; font-size: 11px; margin-right: 15px; }
    
    .card-principal { 
        background-color: #1a242d; padding: 20px; border-radius: 12px; 
        border-bottom: 4px solid #f05a22; margin-bottom: 15px; text-align: center; 
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 22px; font-weight: 800; margin-bottom: 20px; }
    
    .prob-container { display: flex; justify-content: space-around; align-items: center; background: rgba(0,0,0,0.3); border-radius: 10px; padding: 15px 0; }
    .val-prob { color: #f05a22; font-size: 26px; font-weight: 900; }
    .label-prob { color: #8899a6; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-top: 5px; }

    .mini-card { background-color: #111a21; padding: 10px; border-radius: 8px; border: 1px solid #2d3748; text-align: center; }
    .mini-label { color: #8899a6; font-size: 8px; font-weight: 700; text-transform: uppercase; margin-bottom: 5px; display: block; }
    .mini-val { color: #00ffc3; font-weight: 900; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGICA DE DADOS
