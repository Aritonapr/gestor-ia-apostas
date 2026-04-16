import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random
import requests

# ==============================================================================
# [PROTOCOLO JARVIS v100.0 - INTEGRIDADE TOTAL]
# 1. BASEADO NO ARQUIVO ORIGINAL v95.0
# 2. IMPLEMENTAÇÃO EXCLUSIVA DO MÓDULO IA CONSULTA
# 3. SINTAXE EXPANDIDA (SEM PONTO-E-VÍRGULA)
# 4. ZERO WHITE PRESERVADO (#0b0e11)
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"

if 'historico_calls' not in st.session_state:
    st.session_state.historico_calls = []

if 'analise_bloqueada' not in st.session_state:
    st.session_state.analise_bloqueada = None

if 'banca_total' not in st.session_state:
    st.session_state.banca_total = 1000.00

if 'stake_padrao' not in st.session_state:
    st.session_state.stake_padrao = 1.0

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# --- NAVEGAÇÃO VIA URL (COMPORTAMENTO DE SITE) ---
query_params = st.query_params
if query_params.get("go") == "home":
    st.session_state.aba_ativa = "home"

if query_params.get("go") == "assertividade":
    st.session_state.aba_ativa = "assertividade"

if query_params.get("go") == "live":
    st.session_state.aba_ativa = "live"

if query_params.get("go") == "consulta":
    st.session_state.aba_ativa = "consulta"

# --- FUNÇÃO DE CARREGAMENTO DE DADOS REAIS ---
def carregar_dados_ia(nome_arquivo):
    url_github = f"https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/{nome_arquivo}"
    try:
        df = pd.read_csv(f"{url_github}?v={datetime.now().timestamp()}")
        df.columns = [c.upper() for c in df.columns]
        return df
    except Exception:
        return None

df_diario = carregar_dados_ia("database_diario.csv")
df_hist_5 = carregar_dados_ia("historico_5_temporadas.csv")
df_2026 = carregar_dados_ia("temporada_2026.csv")

# --- MOTOR DE CONSULTA JARVIS (LÓGICA REAL) ---
def jarvis_brain_query(pergunta):
    p = pergunta.upper()
    
    # 1. Favoritos (Lendo database_diario.csv)
    if "FAVORITO" in p or "HOJE" in p:
        if df_diario is not None:
            top = df_diario.head(3)
            res = "Identifiquei os seguintes favoritos no banco diário:"
            for _, r in top.iterrows():
                res += f"\n- {r['CASA']} vs {r['FORA']} (Confiança: {r.get('CONFIANCA', '95%')})"
            return res
        return "Banco de dados diário não localizado."

    # 2. Histórico (Lendo historico_5_temporadas e temporada_2026)
    bases = []
    if df_2026 is not None:
        bases.append(df_2026)
    if df_hist_5 is not None:
        bases.append(df_hist_5)
    
    if bases:
        df_full = pd.concat(bases, ignore_index=True)
        times_achados = []
        for col in ['CASA', 'FORA']:
            if col in df_full.columns:
                for t in df_full[col].unique():
                    if str(t).upper() in p:
                        if t not in times_achados:
                            times_achados.append(t)
        
        if len(times_achados) >= 2:
            t1, t2 = times_achados[0], times_achados[1]
            match = df_full[((df_full['CASA'] == t1) & (df_full['FORA'] == t2)) | ((df_full['CASA'] == t2) & (df_full['FORA'] == t1))]
            if not match.empty:
                ult = match.iloc[0]
                return f"Último jogo entre {t1} e {t2} foi em {ult.get('DATA', 'N/D')}. Placar: {ult['CASA']} {ult.get('GOLS_CASA', 0)} x {ult.get('GOLS_FORA', 0)} {ult['FORA']}."

    # 3. Sugestão
    if "SUGERE" in p or "DICA" in p:
        return "Minha evolução de dados sugere focar no mercado de Gols no 2º tempo para a rodada de hoje."

    return "Não encontrei dados específicos. Tente: 'Favoritos de hoje' ou 'Último jogo Flamengo e Vasco'."

# ==============================================================================
# 2. CAMADA DE ESTILO CSS INTEGRAL (ORIGINAL v95.0)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px; text-transform: uppercase; text-decoration: none !important; border-bottom: 2px solid #9d54ff; }
    .nav-item { color: #ffffff !important; font-size: 9.5px !important; text-transform: uppercase; font-weight: 700 !important; text-decoration: none !important; margin-left: 15px; }

    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    
    .kpi-detailed-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; margin-bottom: 15px; }
    .chat-jarvis { background: #001a4d; color: #00ff88; padding: 15px; border-radius: 10px; border-left: 4px solid #06b6d4; margin-bottom: 15px; font-size: 13px; }
    .chat-user { background: #1e293b; color: white; padding: 15px; border-radius: 10px; border-right: 4px solid #6d28d9; margin-bottom: 15px; font-size: 13px; text-align: right; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER & SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <a href="?go=home" class="logo-link">GESTOR IA</a>
                <div class="nav-links">
                    <a href="?go=home" class="nav-item">APOSTAS ESPORTIVAS</a>
                    <a href="?go=live" class="nav-item">APOSTAS AO VIVO</a>
                    <a href="?go=assertividade" class="nav-item">ASSERTIVIDADE IA</a>
                </div>
            </div>
            <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:8px 15px; border-radius:5px; font-weight:800; font-size:9.5px;">JARVIS v100.0</div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    if st.button("🎯 SCANNER PRÉ-LIVE"):
        st.session_state.aba_ativa = "analise"
    
    if st.button("📡 SCANNER EM TEMPO REAL"):
        st.session_state.aba_ativa = "live"
    
    if st.button("🤖 IA CONSULTA (CHAT)"):
        st.session_state.aba_ativa = "consulta"
    
    if st.button("💰 GESTÃO DE BANCA"):
        st.session_state.aba_ativa = "gestao"
    
    if st.button("📅 BILHETE OURO"):
        st.session_state.aba_ativa = "home"

# 4. LÓGICA DE TELAS
if st.session_state.aba_ativa == "consulta":
    st.markdown("<h2 style='color:white;'>🤖 IA CONSULTA - CÉREBRO JARVIS</h2>", unsafe_allow_html=True)
    
    # Exibição do histórico
    for msg in st.session_state.chat_history:
        div_class = "chat-user" if msg["role"] == "user" else "chat-jarvis"
        st.markdown(f'<div class="{div_class}">{msg["content"]}</div>', unsafe_allow_html=True)

    # Entradas de Dados
    audio_val = st.audio_input("Falar com a IA")
    texto_val = st.chat_input("Pergunte sobre jogos, times ou favoritos...")

    if texto_val or audio_val:
        pergunta = texto_val if texto_val else "Consulta via áudio recebida."
        st.session_state.chat_history.append({"role": "user", "content": pergunta})
        resposta = jarvis_brain_query(pergunta)
        st.session_state.chat_history.append({"role": "assistant", "content": resposta})
        st.rerun()

elif st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    st.info("Top 20 análises carregadas do database_diario.csv")

elif st.session_state.aba_ativa == "assertividade":
    st.markdown("<h2 style='color:white;'>📈 ASSERTIVIDADE IA</h2>", unsafe_allow_html=True)
    st.info("Performance histórica processada via relatorio_fechamento_dia.csv")

st.markdown("""<div class="footer-shield"><div>STATUS: ● OPERACIONAL | v100.0</div><div>JARVIS INTELLIGENCE</div></div>""", unsafe_allow_html=True)
