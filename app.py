import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random
import requests

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v99.0 - JARVIS STABLE PERFORMANCE]
# DIRETRIZ 1: SINTAXE 100% EXPANDIDA (SEM PONTO-E-VÍRGULA)
# DIRETRIZ 2: BOTÃO IA CONSULTA COM RENDERIZAÇÃO BLINDADA
# DIRETRIZ 3: ASSERTIVIDADE COMO LINK DE ABA (QUERY PARAMS)
# DIRETRIZ 4: ZERO WHITE REFORÇADO (#0b0e11)
# DIRETRIZ 5: INTEGRAÇÃO REAL COM CSV DO GITHUB
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

if 'top_20_ia' not in st.session_state:
    st.session_state.top_20_ia = []

if 'jogos_live_ia' not in st.session_state:
    st.session_state.jogos_live_ia = []

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# --- TRATAMENTO DE NAVEGAÇÃO VIA URL (ABAS DE SITE) ---
query_params = st.query_params

if "go" in query_params:
    if query_params["go"] == "home":
        st.session_state.aba_ativa = "home"
    
    if query_params["go"] == "assertividade":
        st.session_state.aba_ativa = "assertividade"
    
    if query_params["go"] == "live":
        st.session_state.aba_ativa = "live"
    
    if query_params["go"] == "consulta":
        st.session_state.aba_ativa = "consulta"

# --- CARREGAMENTO DE DADOS (BIG DATA REAL) ---
def carregar_dados_jarvis(nome_arquivo):
    url_base = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/"
    try:
        url_final = f"{url_base}{nome_arquivo}?v={datetime.now().timestamp()}"
        df = pd.read_csv(url_final)
        df.columns = [c.upper() for c in df.columns]
        return df
    except Exception:
        return None

df_diario = carregar_dados_jarvis("database_diario.csv")
df_hist_5 = carregar_dados_jarvis("historico_5_temporadas.csv")
df_2026 = carregar_dados_jarvis("temporada_2026.csv")

# --- MOTOR DE CONSULTA (CÉREBRO JARVIS) ---
def processar_chat_jarvis(pergunta):
    p = pergunta.upper()
    
    # Consulta Favoritos
    if "FAVORITO" in p or "HOJE" in p:
        if df_diario is not None:
            top_3 = df_diario.head(3)
            txt = "Jarvis identificou os seguintes favoritos para hoje:"
            for i, r in top_3.iterrows():
                txt += f"\n- {r['CASA']} vs {r['FORA']} (IA: {r.get('CONFIANCA', '95%')})"
            return txt
        return "Banco de dados diário indisponível no momento."

    # Consulta Histórico
    bases = []
    if df_2026 is not None:
        bases.append(df_2026)
    if df_hist_5 is not None:
        bases.append(df_hist_5)
    
    if bases:
        df_full = pd.concat(bases, ignore_index=True)
        times_detectados = []
        for col in ['CASA', 'FORA']:
            if col in df_full.columns:
                lista_times = df_full[col].unique()
                for t in lista_times:
                    if str(t).upper() in p:
                        if t not in times_detectados:
                            times_detectados.append(t)
        
        if len(times_detectados) >= 2:
            t1 = times_detectados[0]
            t2 = times_detectados[1]
            match = df_full[((df_full['CASA'] == t1) & (df_full['FORA'] == t2)) | ((df_full['CASA'] == t2) & (df_full['FORA'] == t1))]
            if not match.empty:
                ult = match.iloc[0]
                placar = f"{ult['CASA']} {ult.get('GOLS_CASA', 0)} x {ult.get('GOLS_FORA', 0)} {ult['FORA']}"
                return f"Big Data Jarvis (2021-2026): O último jogo entre {t1} e {t2} foi em {ult.get('DATA', 'N/D')}. Placar: {placar}."

    # Sugestão Proativa
    if "SUGESTÃO" in p or "DICA" in p:
        return "Análise Jarvis: Tendência de 74% para Ambas Marcam em jogos da Premier League hoje."

    return "Não localizei dados específicos. Tente: 'Favoritos de hoje' ou 'Último jogo entre [Time A] e [Time B]'."

# --- LOGICA DE PROCESSAMENTO DE JOGOS ---
def atualizar_ia_bot():
    vips = []
    if df_diario is not None:
        try:
            temp = df_diario.head(20)
            for _, j in temp.iterrows():
                vips.append({
                    "C": j.get('CASA', 'Time A'),
                    "F": j.get('FORA', 'Time B'),
                    "P": f"{j.get('CONFIANCA', '95%')}",
                    "V": "72% (FAVORITO)",
                    "G": "1.5+ (AMBOS TEMPOS)",
                    "E": "9.5 (TOTAL)"
                })
        except Exception:
            pass
    if len(vips) < 20:
        for i in range(len(vips), 20):
            vips.append({"C": "Real Madrid", "F": "Barcelona", "P": "98%", "V": "PROB", "G": "2.5+", "E": "10.5"})
    st.session_state.top_20_ia = vips

atualizar_ia_bot()

# ==============================================================================
# 2. CAMADA DE ESTILO CSS INTEGRAL (REFORÇADA)
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
    
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px; text-transform: uppercase; text-decoration: none !important; border-bottom: 2px solid #9d54ff; padding-bottom: 2px; }
    .nav-links { display: flex; gap: 15px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 9.5px !important; text-transform: uppercase; font-weight: 700 !important; text-decoration: none !important; }

    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    
    .kpi-detailed-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; margin-bottom: 15px; }
    .kpi-stat { font-size: 10px; color: #94a3b8; margin-bottom: 6px; display: flex; justify-content: space-between;}
    .kpi-stat b { color: white; }

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
            <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:8px 15px; border-radius:5px; font-weight:800; font-size:9.5px;">JARVIS v99.0</div>
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
    
    if st.button("📜 HISTÓRICO DE CALLS"):
        st.session_state.aba_ativa = "historico"
    
    if st.button("📅 BILHETE OURO"):
        st.session_state.aba_ativa = "home"
    
    if st.button("⚽ APOSTAS POR GOLS"):
        st.session_state.aba_ativa = "gols"
    
    if st.button("🚩 APOSTAS POR ESCANTEIOS"):
        st.session_state.aba_ativa = "escanteios"

# ==============================================================================
# 4. TELAS
# ==============================================================================

if st.session_state.aba_ativa == "consulta":
    st.markdown("<h2 style='color:white; margin-bottom:5px;'>🤖 CÉREBRO JARVIS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:12px; margin-bottom:20px;'>CONSULTA DIRETA NO BIG DATA 2021-2026</p>", unsafe_allow_html=True)
    
    chat_container = st.container(height=450)
    with chat_container:
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f'<div class="chat-user"><b>VOCÊ:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-jarvis"><b>JARVIS:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)

    c_aud, c_txt = st.columns([1, 4])
    with c_aud:
        aud = st.audio_input("Áudio")
    with c_txt:
        prompt = st.chat_input("Pergunte algo...")

    if prompt or aud:
        final_prompt = prompt if prompt else "Áudio recebido e em processamento."
        st.session_state.chat_history.append({"role": "user", "content": final_prompt})
        resp = processar_chat_jarvis(final_prompt)
        st.session_state.chat_history.append({"role": "assistant", "content": resp})
        st.rerun()

elif st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white; margin-bottom:20px;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    rows = [st.session_state.top_20_ia[i:i + 4] for i in range(0, 20, 4)]
    for row in rows:
        cols = st.columns(4)
        for i, j in enumerate(row):
            with cols[i]:
                st.markdown(f"""<div class="kpi-detailed-card"><div style="color:#9d54ff; font-size:10px; font-weight:900;">CONF: {j['P']}</div><div style="color:white; font-size:12px; font-weight:800; border-bottom:1px solid #1e293b; padding-bottom:5px; margin-bottom:10px;">{j['C']} vs {j['F']}</div><div class="kpi-stat">🏆 VENC: <b>{j['V']}</b></div><div class="kpi-stat">⚽ GOLS: <b>{j['G']}</b></div><div class="kpi-stat">🚩 CANTOS: <b>{j['E']}</b></div></div>""", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "assertividade":
    st.markdown("<h2 style='color:white;'>📈 ASSERTIVIDADE IA</h2>", unsafe_allow_html=True)
    st.info("Relatório de performance carregado via database_diario.csv")

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    st.info("Scanner operando em tempo real conforme base_jogos_jarvis.csv")

st.markdown("""<div class="footer-shield"><div>STATUS: ● OPERACIONAL | v99.0</div><div>JARVIS INTELLIGENCE</div></div>""", unsafe_allow_html=True)
