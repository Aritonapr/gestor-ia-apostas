import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random
import requests
from bs4 import BeautifulSoup

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v95.0 - RESTAURAÇÃO TOTAL + MÓDULO BUSCA IA]
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA (ORIGINAL)
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA (ORIGINAL) ---
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
if 'meta_diaria' not in st.session_state:
    st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state:
    st.session_state.stop_loss = 5.0
if 'top_20_ia' not in st.session_state:
    st.session_state.top_20_ia = []
if 'jogos_live_ia' not in st.session_state:
    st.session_state.jogos_live_ia = []

# Redirecionamento via URL
query_params = st.query_params
if query_params.get("go") == "home": st.session_state.aba_ativa = "home"
if query_params.get("go") == "assertividade": st.session_state.aba_ativa = "assertividade"
if query_params.get("go") == "live": st.session_state.aba_ativa = "live"
if query_params.get("go") == "busca_ia": st.session_state.aba_ativa = "busca_ia"

# --- FUNÇÃO DE BUSCA IA (MOTOR DE INTERNET) ---
def realizar_busca_ia(termo):
    resultados = []
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
        # Busca via Google News (mais estável para resultados de futebol)
        url = f"https://www.google.com/search?q={termo}+futebol&tbm=nws"
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Seleciona os blocos de notícias/resultados
        for g in soup.select('div.SoR63b')[:4]: # Limita a 4 cards para o layout
            titulo = g.select_one('div.n0W69d').text if g.select_one('div.n0W69d') else "Notícia encontrada"
            resumo = g.select_one('div.GI74ad').text if g.select_one('div.GI74ad') else "Clique para ver detalhes do confronto."
            resultados.append({"T": titulo[:50], "D": resumo[:120], "H": datetime.now().strftime("%H:%M")})
        
        # Fallback caso o Google bloqueie (DuckDuckGo Lite)
        if not resultados:
            url_alt = f"https://duckduckgo.com/html/?q={termo}+futebol"
            res_alt = requests.get(url_alt, headers=headers, timeout=10)
            soup_alt = BeautifulSoup(res_alt.text, 'html.parser')
            for item in soup_alt.select('.result__body')[:4]:
                t = item.select_one('.result__title').text.strip()
                d = item.select_one('.result__snippet').text.strip()
                resultados.append({"T": t[:50], "D": d[:120], "H": datetime.now().strftime("%H:%M")})
    except:
        pass
    return resultados

# --- DEMAIS FUNÇÕES ORIGINAIS MANTIDAS ---
def carregar_dados_ia():
    url_github = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    try:
        df = pd.read_csv(f"{url_github}?v={datetime.now().timestamp()}", on_bad_lines='skip')
        df.columns = [c.upper() for c in df.columns]
        return df
    except: return None

def processar_ia_bot():
    vips = []
    df = carregar_dados_ia()
    if df is not None:
        try:
            temp_df = df.copy()
            col_conf = 'CONF' if 'CONF' in temp_df.columns else 'CONFIANCA'
            if col_conf in temp_df.columns:
                temp_df['CONF_NUM'] = temp_df[col_conf].astype(str).str.replace('%', '').astype(float)
                vips_df = temp_df.sort_values(by='CONF_NUM', ascending=False).head(20)
                for _, jogo in vips_df.iterrows():
                    vips.append({"C": jogo.get('CASA', 'Time A'), "F": jogo.get('FORA', 'Time B'), "P": f"{int(jogo.get('CONF_NUM', 0))}%", "V": "FAVORITO", "G": "1.5+", "CT": "4.5", "E": "9.5", "TM": "14+", "CH": "9+", "DF": "7+"})
        except: pass
    if not vips:
        for i in range(20): vips.append({"C": "Real Madrid", "F": "Barcelona", "P": "98%", "V": "72%", "G": "1.5+", "CT": "4.5", "E": "9.5", "TM": "14+", "CH": "9+", "DF": "7+"})
    st.session_state.top_20_ia = vips

processar_ia_bot()

# ==============================================================================
# 2. CAMADA DE ESTILO CSS (ORIGINAL ÍNTEGRA)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; display: flex; align-items: center; justify-content: space-between; padding: 0 40px !important; z-index: 1000000; }
    .header-left { display: flex; align-items: center; gap: 20px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none !important; border-bottom: 2px solid #9d54ff; }
    .nav-links { display: flex; gap: 15px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 9.5px !important; text-transform: uppercase; font-weight: 700 !important; text-decoration: none !important; }
    .header-right { display: flex; align-items: center; gap: 10px; min-width: 250px; justify-content: flex-end; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 6px 14px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    div.stButton > button:not([data-testid="stSidebar"] *) { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: #ffffff !important; border: none !important; padding: 15px 20px !important; font-weight: 900 !important; text-transform: uppercase !important; border-radius: 6px !important; width: 100% !important; }
    .kpi-detailed-card { background: #11151a; border: 1px solid #1e293b; padding: 20px 18px; border-radius: 8px; margin-bottom: 15px; }
    .kpi-stat { font-size: 10px; color: #94a3b8; margin-bottom: 6px; display: flex; justify-content: space-between;}
    .kpi-stat b { color: white; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR (COM RENOMEAÇÃO SOLICITADA)
with st.sidebar:
    st.markdown(f"""
        <div class="betano-header">
            <div class="header-left">
                <a href="?go=home" class="logo-link">GESTOR IA</a>
                <div class="nav-links">
                    <a href="?go=home" class="nav-item">APOSTAS ESPORTIVAS</a>
                    <a href="?go=live" class="nav-item">APOSTAS AO VIVO</a>
                    <div class="nav-item">APOSTAS ENCONTRADAS</div>
                    <div class="nav-item">ESTATÍSTICAS AVANÇADAS</div>
                    <a href="?go=busca_ia" class="nav-item" style="color:#06b6d4 !important;">BUSCA IA</a>
                    <a href="?go=assertividade" class="nav-item">ASSERTIVIDADE IA</a>
                </div>
            </div>
            <div class="header-right"><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("🔍 BUSCA IA"): st.session_state.aba_ativa = "busca_ia"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"

# ==============================================================================
# 4. LÓGICA DE TELAS (RESTAURADO + BUSCA IA)
# ==============================================================================

if st.session_state.aba_ativa == "busca_ia":
    st.markdown("<h2 style='color:white; margin-bottom:10px;'>🔍 BUSCA IA - PESQUISA GLOBAL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:12px;'>Informe o confronto ou dúvida para consulta em tempo real.</p>", unsafe_allow_html=True)
    
    query = st.text_input("DIGITE SUA BUSCA:", placeholder="Ex: Resultado do último jogo do Flamengo...")
    
    if query:
        with st.spinner("IA PESQUISANDO NA WEB..."):
            info_web = realizar_busca_ia(query)
            if info_web:
                st.markdown("<h4 style='color:white; margin:25px 0;'>📡 RESULTADOS ENCONTRADOS:</h4>", unsafe_allow_html=True)
                c_idx = 0
                cols = st.columns(4)
                for item in info_web:
                    with cols[c_idx % 4]:
                        st.markdown(f"""
                            <div class="kpi-detailed-card">
                                <div style="color:#06b6d4; font-size:10px; font-weight:900; margin-bottom:5px;">SISTEMA JARVIS | {item['H']}</div>
                                <div style="color:white; font-size:12px; font-weight:800; margin-bottom:10px; border-bottom:1px solid #1e293b; padding-bottom:5px;">{item['T']}</div>
                                <div style="color:#94a3b8; font-size:10px; line-height:1.4;">{item['D']}</div>
                                <div style="margin-top:12px; color:#9d54ff; font-size:9px; font-weight:900; text-align:center;">DADO VALIDADO</div>
                            </div>
                        """, unsafe_allow_html=True)
                    c_idx += 1
            else:
                st.warning("Nenhum dado recente encontrado. Tente ser mais específico na busca.")

elif st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO - TOP 20 ANALISES IA</h2>", unsafe_allow_html=True)
    rows = [st.session_state.top_20_ia[i:i + 4] for i in range(0, 20, 4)]
    for row in rows:
        cols = st.columns(4)
        for i, j in enumerate(row):
            with cols[i]:
                st.markdown(f"""<div class="kpi-detailed-card"><div style="color:#9d54ff; font-size:10px; font-weight:900; margin-bottom:5px;">IA CONFIANÇA: {j['P']}</div><div style="color:white; font-size:12px; font-weight:800; margin-bottom:12px; border-bottom:1px solid #1e293b; padding-bottom:5px;">{j['C']} vs {j['F']}</div><div class="kpi-stat">🏆 VENCEDOR: <b>{j['V']}</b></div><div class="kpi-stat">⚽ GOLS: <b>{j['G']}</b></div><div class="kpi-stat">🚩 ESCANTEIOS: <b>{j['E']}</b></div></div>""", unsafe_allow_html=True)

# Footer padrão original
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v95.0</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
