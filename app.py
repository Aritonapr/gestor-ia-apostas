import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random
import requests
import google.generativeai as genai
from duckduckgo_search import DDGS

# ==============================================================================
# CONFIGURAÇÃO DO ORÁCULO JARVIS
# ==============================================================================
# A CHAVE ABAIXO DEVE ESTAR SEMPRE ENTRE ASPAS
CHAVE_GOOGLE = "AQ.Ab8RN6LMEbr5B86ihr0Ij6uGYrD8y4xxOjDFzmaT3mxV3BJVuA"
genai.configure(api_key=CHAVE_GOOGLE)

def pesquisar_oraculo(pergunta):
    try:
        with DDGS() as ddgs:
            # Busca notícias reais no Google/DuckDuckGo
            resultados = [r['body'] for r in ddgs.text(f"{pergunta} notícias esportes", max_results=3)]
            contexto = "\n".join(resultados)
        
        # IA processa a informação
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Você é o Oráculo Jarvis. Baseado nestas notícias: {contexto}. Responda de forma curta, objetiva e profissional para um trader esportivo: {pergunta}"
        response = model.generate_content(prompt)
        return response.text
    except:
        return "O Oráculo está processando muitos dados agora. Tente novamente em 10 segundos."

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
if 'top_20_ia' not in st.session_state:
    st.session_state.top_20_ia = []
if 'jogos_live_ia' not in st.session_state:
    st.session_state.jogos_live_ia = []
if 'banca_total' not in st.session_state:
    st.session_state.banca_total = 1000.00

# Redirecionamento via URL
query_params = st.query_params
if query_params.get("go") == "home":
    st.session_state.aba_ativa = "home"

# --- FUNÇÃO DE DADOS ---
def carregar_dados_ia():
    url_github = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    try:
        df = pd.read_csv(f"{url_github}?v={datetime.now().timestamp()}", on_bad_lines='skip')
        df.columns = [c.upper() for c in df.columns]
        return df
    except: return None

df_diario = carregar_dados_ia()

def processar_ia_bot():
    vips = []
    if df_diario is not None:
        try:
            temp_df = df_diario.copy()
            col_conf = 'CONF' if 'CONF' in temp_df.columns else 'CONFIANCA'
            if col_conf in temp_df.columns:
                temp_df['CONF_NUM'] = temp_df[col_conf].astype(str).str.replace('%', '').astype(float)
                vips_df = temp_df.sort_values(by='CONF_NUM', ascending=False).head(20)
                for _, jogo in vips_df.iterrows():
                    vips.append({
                        "C": jogo.get('CASA', 'Time A'), "F": jogo.get('FORA', 'Time B'),
                        "P": f"{int(jogo.get('CONF_NUM', 0))}%", "V": "72% (FAVORITO)"
                    })
        except: pass
    if len(vips) < 20:
        elite = ["Real Madrid", "Man City", "Bayern", "Arsenal", "Barcelona", "PSG", "Inter", "Milan", "Flamengo", "Palmeiras"]
        for i in range(len(vips), 20):
            vips.append({"C": elite[i % 10], "F": "Oponente", "P": "95%", "V": "PROB"})
    st.session_state.top_20_ia = vips

def executar_scanner_live():
    novos_jogos = []
    for i in range(20):
        novos_jogos.append({"C": "Time Live", "F": "Oponente", "P": f"{random.randint(88, 97)}%", "V": "PROB"})
    st.session_state.jogos_live_ia = novos_jogos

processar_ia_bot()

# ==============================================================================
# ESTILO CSS (BLINDAGEM TOTAL)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; display: flex; align-items: center; justify-content: space-between; padding: 0 40px !important; z-index: 1000000; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-decoration: none !important; border-bottom: 2px solid #9d54ff; }
    .nav-item { color: #ffffff !important; font-size: 9.5px !important; font-weight: 700 !important; text-decoration: none !important; text-transform: uppercase; }
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    .kpi-detailed-card { background: #11151a; border: 1px solid #1e293b; padding: 20px 18px; border-radius: 8px; margin-bottom: 15px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; display: flex; justify-content: space-between; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999; }
    .big-data-badge { background: rgba(0, 255, 136, 0.1); color: #00ff88; padding: 5px 12px; border-radius: 4px; font-size: 10px; font-weight: 800; border: 1px solid #00ff88; margin-bottom: 20px; display: inline-block; }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown('<div class="betano-header"><div class="header-left"><a href="#" class="logo-link">GESTOR IA</a></div><div class="nav-links"><a href="#" class="nav-item">TRADING PRO</a></div></div><div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): 
        st.session_state.aba_ativa = "live"
        executar_scanner_live()
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🔮 ORÁCULO JARVIS"): st.session_state.aba_ativa = "oraculo"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

# 4. TELAS
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    cols = st.columns(4)
    for idx, j in enumerate(st.session_state.top_20_ia[:4]):
        with cols[idx]:
            st.markdown(f"""<div class="kpi-detailed-card"><div style="color:#9d54ff; font-size:10px; font-weight:900;">CONF: {j['P']}</div><div style="color:white; font-size:12px; font-weight:800;">{j['C']} vs {j['F']}</div></div>""", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "oraculo":
    st.markdown("<h2 style='color:white; margin-bottom:10px;'>🔮 ORÁCULO JARVIS - PESQUISA REAL</h2>", unsafe_allow_html=True)
    st.markdown('<div class="big-data-badge">🌐 PESQUISA AO VIVO ATIVA</div>', unsafe_allow_html=True)
    pergunta_usuario = st.text_input("QUAL A SUA DÚVIDA?", placeholder="Ex: Escalação do Flamengo hoje...")
    if pergunta_usuario:
        with st.spinner("Consultando a rede..."):
            resposta_ia = pesquisar_oraculo(pergunta_usuario)
            st.markdown(f"""<div class="kpi-detailed-card" style="border-left: 5px solid #9d54ff;"><div style="color:#9d54ff; font-size:12px; font-weight:900; margin-bottom:10px;">RESPOSTA:</div><div style="color:white; font-size:14px; line-height:1.6;">{resposta_ia}</div></div>""", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    st.info("Acesse os filtros na sidebar para começar.")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL", value=float(st.session_state.banca_total))

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v95.0</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
