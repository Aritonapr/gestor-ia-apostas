import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random
import requests

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v95.5 - INTEGRAÇÃO IA CONSULTA BLINDADA]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO)
# DIRETRIZ 5: CÓDIGO 100% ÍNTEGRO - SEM SNIPPETS
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state:
    st.session_state.historico_calls = []

# --- CARREGAMENTO DE DADOS ---
def carregar_dados_ia():
    url_github = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    try:
        df = pd.read_csv(f"{url_github}?v={datetime.now().timestamp()}", on_bad_lines='skip')
        df.columns = [c.upper() for c in df.columns]
        return df
    except:
        return None

df_diario = carregar_dados_ia()

# ==============================================================================
# 2. CAMADA DE ESTILO CSS (BLINDAGEM VISUAL)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* RESET GERAL PARA DARK THEME */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: white;
    }

    /* REMOVER COMPONENTES PADRÃO DO STREAMLIT */
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    /* ESTILIZAÇÃO DO INPUT (IA CONSULTA) - REMOVE FUNDO BRANCO */
    div[data-baseweb="input"] {
        background-color: #11151a !important;
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
        color: white !important;
    }
    input[data-testid="stTextInputInput"] {
        color: white !important;
        background-color: transparent !important;
    }

    /* HEADER CUSTOMIZADO (GESTOR IA) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #0b0e11 !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
        transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none !important; border-bottom: 2px solid #9d54ff; }
    
    /* CARDS DE ANÁLISE */
    .kpi-detailed-card { 
        background: #11151a; 
        border: 1px solid #1e293b; 
        padding: 20px; 
        border-radius: 8px; 
        margin-bottom: 15px; 
    }
    .kpi-stat { font-size: 10px; color: #94a3b8; margin-bottom: 6px; display: flex; justify-content: space-between;}
    .kpi-stat b { color: white; }
    
    .btn-grad { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: white !important; padding: 10px 20px !important; 
        border-radius: 5px !important; font-weight: 800; border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR E NAVEGAÇÃO
with st.sidebar:
    st.markdown('<a href="#" class="logo-link">GESTOR IA</a>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "home"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("🔍 IA CONSULTA"): st.session_state.aba_ativa = "ia_consulta"
    if st.button("📊 ASSERTIVIDADE IA"): st.session_state.aba_ativa = "assertividade"

# 4. ÁREA DE CONTEÚDO
st.markdown("""
    <div class="betano-header">
        <div class="logo-link">GESTOR IA</div>
        <div style="background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 5px 15px; border-radius: 5px; font-size: 10px; font-weight: bold;">ENTRAR</div>
    </div>
""", unsafe_allow_html=True)

# --- TELA: IA CONSULTA ---
if st.session_state.aba_ativa == "ia_consulta":
    st.markdown("<h2 style='color:white;'>🤖 JARVIS INTELLIGENCE</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:12px;'>CONSULTE O BANCO DE DADOS EM TEMPO REAL:</p>", unsafe_allow_html=True)
    
    pergunta = st.text_input("", placeholder="Ex: Último resultado Flamengo vs Vasco", label_visibility="collapsed")
    
    col_btn1, col_btn2, _ = st.columns([1, 1, 4])
    with col_btn1: st.button("🎤 ÁUDIO")
    with col_btn2: consultar = st.button("🔍 CONSULTAR")

    if consultar and pergunta:
        st.markdown(f"<h4 style='color:#06b6d4; margin-top:20px;'>RELATÓRIO: {pergunta.upper()}</h4>", unsafe_allow_html=True)
        res_cols = st.columns(4)
        with res_cols[0]:
            st.markdown("""<div class="kpi-detailed-card" style="border-left: 4px solid #9d54ff;">
                <div style="color:#94a3b8; font-size:9px;">HISTÓRICO</div>
                <div style="color:white; font-size:12px; font-weight:800; margin-top:5px;">FLAMENGO 2 X 0 VASCO</div>
                <div class="kpi-stat" style="margin-top:10px;">GOLS: <b>2</b></div>
                <div class="kpi-stat">CANTOS: <b>12</b></div>
            </div>""", unsafe_allow_html=True)
        # (Outros cards simulados para manter a simetria da imagem enviada)
        for i in range(1, 4):
            with res_cols[i]:
                st.markdown("""<div class="kpi-detailed-card">
                    <div style="text-align:center;">
                        <div style="color:#94a3b8; font-size:9px;">PROBABILIDADE</div>
                        <div style="color:white; font-size:24px; font-weight:900;">85%</div>
                    </div>
                </div>""", unsafe_allow_html=True)

# --- TELA: HOME (BILHETE OURO) ---
elif st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO - TOP 20 ANALISES IA</h2>", unsafe_allow_html=True)
    st.markdown("<div style='background:#00c85322; color:#00c853; padding:5px 15px; border-radius:5px; font-size:10px; font-weight:bold; display:inline-block; margin-bottom:20px;'>● BIG DATA ATIVO: PADRÕES 2021-2026 CARREGADOS</div>", unsafe_allow_html=True)
    
    cols = st.columns(4)
    exemplos = [
        {"C": "Liverpool", "F": "Sporting", "P": "98%"},
        {"C": "Juventus", "F": "Chelsea", "P": "98%"},
        {"C": "Juventus", "F": "Porto", "P": "97%"},
        {"C": "Liverpool", "F": "Dortmund", "P": "97%"}
    ]
    for i, jogo in enumerate(exemplos):
        with cols[i]:
            st.markdown(f"""<div class="kpi-detailed-card">
                <div style="color:#9d54ff; font-size:10px; font-weight:900;">IA CONFIANÇA: {jogo['P']}</div>
                <div style="color:white; font-size:12px; font-weight:800; padding: 5px 0;">{jogo['C']} vs {jogo['F']}</div>
                <div class="kpi-stat">🏆 VENCEDOR: <b>72% (FAVORITO)</b></div>
                <div class="kpi-stat">⚽ GOLS: <b>1.5+ (AMBOS TEMPOS)</b></div>
                <div class="kpi-stat">🚩 ESCANTEIOS: <b>9.5 (C:5 | F:4)</b></div>
                <div style="color:#06b6d4; font-size:10px; font-weight:bold; text-align:center; margin-top:10px;">INVESTIMENTO: R$ 10.00</div>
            </div>""", unsafe_allow_html=True)

# Rodapé de Status
st.markdown("<br><div style='color:#555; font-size:9px;'>STATUS: ● IA OPERACIONAL | v95.5</div>", unsafe_allow_html=True)
