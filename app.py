import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random
import requests

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v106.0 - BUSCA POR PALAVRA-CHAVE (SISTEMA JARVIS)]
# DIRETRIZ 1: LAYOUT ORIGINAL v95.0 PRESERVADO
# DIRETRIZ 2: MOTOR DE BUSCA FLEXÍVEL (PROCURA PARTE DO NOME DO TIME)
# DIRETRIZ 3: ASSERTIVIDADE IA COMO ABA DE SITE (QUERY PARAMS)
# DIRETRIZ 4: ZERO WHITE REFORÇADO (#0b0e11)
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
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'banca_total' not in st.session_state:
    st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state:
    st.session_state.stake_padrao = 1.0

# Navegação via URL
query_params = st.query_params
if query_params.get("go") == "home":
    st.session_state.aba_ativa = "home"
if query_params.get("go") == "assertividade":
    st.session_state.aba_ativa = "assertividade"

# --- CARREGAMENTO DE DADOS (CONEXÃO GITHUB REAL) ---
def carregar_csv(arquivo):
    url = f"https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/{arquivo}"
    try:
        df = pd.read_csv(f"{url}?v={datetime.now().timestamp()}")
        df.columns = [c.upper() for c in df.columns]
        return df
    except:
        return None

df_diario = carregar_csv("database_diario.csv")
df_hist_5 = carregar_csv("historico_5_temporadas.csv")
df_2026 = carregar_csv("temporada_2026.csv")

# --- MOTOR DE BUSCA JARVIS (MÉTODO DE FRAGMENTO DE TEXTO) ---
def motor_de_busca_jarvis(pergunta):
    p = pergunta.upper().strip()
    
    # Busca Favoritos
    if "FAVORITO" in p or "HOJE" in p:
        if df_diario is not None:
            top = df_diario.head(3)
            res = "Analisando database_diario.csv... Favoritos de hoje:"
            for _, r in top.iterrows():
                res += f"\n- {r['CASA']} vs {r['FORA']} (Confiança: {r.get('CONFIANCA', '95%')})"
            return res
        return "Arquivo database_diario.csv não carregado."

    # Busca em Histórico (Lógica de Fragmento)
    bases = [df_2026, df_hist_5]
    for db in bases:
        if db is not None:
            # Filtra linhas onde CASA ou FORA contém qualquer palavra da pergunta
            palavras = p.split()
            # Pega a última palavra (geralmente o nome do time) para ser mais preciso
            time_alvo = palavras[-1] if len(palavras) > 0 else p
            
            filtro = db[(db['CASA'].astype(str).str.upper().str.contains(time_alvo)) | 
                        (db['FORA'].astype(str).str.upper().str.contains(time_alvo))]
            
            if not filtro.empty:
                ult = filtro.iloc[0] # Pega o mais recente
                g_c = ult.get('GOLS_CASA', 0)
                g_f = ult.get('GOLS_FORA', 0)
                data_j = ult.get('DATA', 'N/D')
                return f"🔍 Big Data: Achei o último registro de {time_alvo}. Placar: {ult['CASA']} {int(g_c)} x {int(g_f)} {ult['FORA']} em {data_j}."
    
    return "Jarvis não encontrou esse time no Big Data. Tente apenas o nome (Ex: 'Palmeiras')."

# ==============================================================================
# 2. CAMADA DE ESTILO CSS (ORIGINAL v95.0)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px; text-transform: uppercase; text-decoration: none !important; border-bottom: 2px solid #9d54ff; }
    .nav-item { color: #ffffff !important; font-size: 9.5px !important; text-transform: uppercase; font-weight: 700; text-decoration: none !important; margin-left: 15px; }

    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    
    .chat-jarvis { background: #001a4d; color: #00ff88; padding: 15px; border-radius: 10px; border-left: 4px solid #06b6d4; margin-bottom: 15px; font-size: 13px; }
    .chat-user { background: #1e293b; color: white; padding: 15px; border-radius: 10px; border-right: 4px solid #6d28d9; margin-bottom: 15px; font-size: 13px; text-align: right; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR
with st.sidebar:
    st.markdown(f"""
        <div class="betano-header">
            <div class="header-left">
                <a href="?go=home" class="logo-link">GESTOR IA</a>
                <div class="nav-links">
                    <a href="?go=home" class="nav-item">APOSTAS ESPORTIVAS</a>
                    <a href="?go=live" class="nav-item">APOSTAS AO VIVO</a>
                    <a href="?go=assertividade" class="nav-item">ASSERTIVIDADE IA</a>
                </div>
            </div>
            <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:8px 15px; border-radius:5px; font-weight:800; font-size:9.5px;">JARVIS v106.0</div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🤖 IA CONSULTA (CHAT)"): st.session_state.aba_ativa = "consulta"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

# 4. LÓGICA DE TELAS
if st.session_state.aba_ativa == "consulta":
    st.markdown("<h2 style='color:white;'>🤖 IA CONSULTA - CÉREBRO JARVIS</h2>", unsafe_allow_html=True)
    
    # Renderização simples do chat
    for m in st.session_state.chat_history:
        div_class = "chat-user" if m["role"] == "user" else "chat-jarvis"
        st.markdown(f'<div class="{div_class}">{m["content"]}</div>', unsafe_allow_html=True)

    # Inputs
    c1, c2 = st.columns([1, 4])
    with c1: aud = st.audio_input("Voz")
    with c2: prompt = st.chat_input("Pergunte ao Jarvis (Ex: Flamengo)")
    
    if prompt or aud:
        texto = prompt if prompt else "Áudio recebido."
        st.session_state.chat_history.append({"role": "user", "content": texto})
        st.session_state.chat_history.append({"role": "jarvis", "content": motor_de_busca_jarvis(texto)})
        st.rerun()

elif st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    st.info("Interface original preservada.")

elif st.session_state.aba_ativa == "assertividade":
    st.markdown("<h2 style='color:white;'>📈 ASSERTIVIDADE IA</h2>", unsafe_allow_html=True)
    st.info("Modo Aba de Site ativo.")

st.markdown("""<div class="footer-shield"><div>STATUS: ● OPERACIONAL | v106.0</div><div>JARVIS INTELLIGENCE</div></div>""", unsafe_allow_html=True)
