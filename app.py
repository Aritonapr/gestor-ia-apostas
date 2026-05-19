import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random
import requests
from bs4 import BeautifulSoup

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v95.0 - MOTOR DE RESPOSTA DIRETA / BUSCA IA]
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA (ORIGINAL)
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA (ORIGINAL) ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'top_20_ia' not in st.session_state: st.session_state.top_20_ia = []
if 'jogos_live_ia' not in st.session_state: st.session_state.jogos_live_ia = []

# Roteamento via URL
query_params = st.query_params
if query_params.get("go") == "busca_ia": st.session_state.aba_ativa = "busca_ia"
if query_params.get("go") == "home": st.session_state.aba_ativa = "home"

# --- NOVO MOTOR DE BUSCA IA (FOCO EM RESPOSTA DIRETA) ---
def realizar_busca_ia_direta(pergunta):
    resultados = []
    try:
        # Headers para simular navegador real e evitar bloqueios
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        
        # Busca Geral (não apenas News) para pegar resultados de placares e tabelas
        search_url = f"https://www.google.com/search?q={pergunta.replace(' ', '+')}"
        response = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Lógica para capturar "Snippets" de resposta (blocos de texto informativo)
        # Procuramos por classes comuns de descrição de resultados do Google
        for result in soup.select('.tF2Cxc')[:4]: 
            titulo = result.select_one('h3').text if result.select_one('h3') else "Informação Encontrada"
            # O 'snippet' é onde mora a resposta real (Ex: "Flamengo venceu por 2x0...")
            snippet = result.select_one('.VwiC3b').text if result.select_one('.VwiC3b') else ""
            
            if snippet:
                # Limpeza básica para remover datas soltas no início do texto
                if " — " in snippet: snippet = snippet.split(" — ")[1]
                
                resultados.append({
                    "T": titulo[:45] + "...", 
                    "D": snippet[:160] + "...", 
                    "H": datetime.now().strftime("%H:%M")
                })
        
        # Caso o Google falhe, fallback para DuckDuckGo (estilo texto direto)
        if not resultados:
            ddg_url = f"https://html.duckduckgo.com/html/?q={pergunta}"
            res_ddg = requests.get(ddg_url, headers=headers, timeout=10)
            soup_ddg = BeautifulSoup(res_ddg.text, 'html.parser')
            for item in soup_ddg.select('.result__body')[:4]:
                t = item.select_one('.result__title').text.strip()
                d = item.select_one('.result__snippet').text.strip()
                resultados.append({"T": t[:45], "D": d[:160], "H": datetime.now().strftime("%H:%M")})
                
    except Exception as e:
        resultados = [{"T": "Erro de Conexão", "D": "A IA não conseguiu acessar a rede mundial agora.", "H": "--:--"}]
    
    return resultados

# ==============================================================================
# 2. CAMADA DE ESTILO CSS (ORIGINAL INTEGRAL - SEM ALTERAÇÕES)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; display: flex; align-items: center; justify-content: space-between; padding: 0 40px !important; z-index: 1000000; }
    .header-left { display: flex; align-items: center; gap: 20px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none !important; border-bottom: 2px solid #9d54ff; }
    .nav-item { color: #ffffff !important; font-size: 9.5px !important; text-transform: uppercase; font-weight: 700 !important; text-decoration: none !important; }
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important; }
    div.stButton > button:not([data-testid="stSidebar"] *) { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: #ffffff !important; border: none !important; padding: 15px 20px !important; font-weight: 900 !important; text-transform: uppercase !important; border-radius: 6px !important; width: 100% !important; }
    .kpi-detailed-card { background: #11151a; border: 1px solid #1e293b; padding: 20px 18px; border-radius: 8px; margin-bottom: 15px; min-height: 180px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR (MANTENDO "BUSCA IA")
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <a href="?go=home" class="logo-link">GESTOR IA</a>
                <div class="nav-links" style="display:flex; gap:15px;">
                    <a href="?go=home" class="nav-item">APOSTAS ESPORTIVAS</a>
                    <a href="?go=busca_ia" class="nav-item" style="color:#06b6d4 !important;">BUSCA IA</a>
                </div>
            </div>
            <div class="header-right" style="display:flex; gap:10px;"><div style="color:white; font-size:9px; border:1px solid white; padding:5px 10px; border-radius:20px;">REGISTRAR</div><div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; font-size:9px; padding:6px 15px; border-radius:5px; font-weight:800;">ENTRAR</div></div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 
    if st.button("🔍 BUSCA IA"): st.session_state.aba_ativa = "busca_ia"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"

# ==============================================================================
# 4. LÓGICA DE TELAS
# ==============================================================================

if st.session_state.aba_ativa == "busca_ia":
    st.markdown("<h2 style='color:white; margin-bottom:10px;'>🔍 BUSCA IA - RESPOSTA DIRETA</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:12px;'>A IA vasculha os dados mais recentes para te dar a resposta correta.</p>", unsafe_allow_html=True)
    
    pergunta_usuario = st.text_input("QUAL SUA DÚVIDA?", placeholder="Ex: Quanto foi o último jogo do Flamengo?")
    
    if pergunta_usuario:
        with st.spinner("PROCESSANDO DADOS REAIS..."):
            infos = realizar_busca_ia_direta(pergunta_usuario)
            if infos:
                st.markdown("<h4 style='color:white; margin:25px 0;'>📡 RESULTADOS PROCESSADOS:</h4>", unsafe_allow_html=True)
                cols = st.columns(4)
                for idx, item in enumerate(infos):
                    with cols[idx]:
                        st.markdown(f"""
                            <div class="kpi-detailed-card">
                                <div style="color:#06b6d4; font-size:10px; font-weight:900; margin-bottom:5px;">SISTEMA JARVIS | {item['H']}</div>
                                <div style="color:white; font-size:12px; font-weight:800; margin-bottom:10px; border-bottom:1px solid #1e293b; padding-bottom:5px;">{item['T']}</div>
                                <div style="color:#e2e8f0; font-size:10.5px; line-height:1.5;">{item['D']}</div>
                                <div style="margin-top:15px; color:#00ff88; font-size:9px; font-weight:900; text-align:center;">DADO ANALISADO ✓</div>
                            </div>
                        """, unsafe_allow_html=True)
            else:
                st.info("A IA não encontrou uma resposta direta. Tente perguntar de forma mais simples (Ex: 'Resultado Flamengo ontem').")

elif st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO - TOP 20 ANALISES IA</h2>", unsafe_allow_html=True)
    st.info("Módulo principal ativo.")

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v95.0</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
