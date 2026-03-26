import streamlit as st
import pandas as pd
import os
from datetime import datetime
import random

# ==============================================================================
# 🔒 [DIRETRIZ DE PROTEÇÃO JARVIS v91.00 - NÃO ALTERAR ESTRUTURA]
# 1. MANTER BACKGROUND #0b0e11 E HEADER #001a4d FIXO.
# 2. NAVEGAÇÃO EXCLUSIVA VIA st.session_state.aba.
# 3. PROIBIDO REMOVER CSS DE ACELERAÇÃO DE GPU (TRANSLATE3D).
# 4. TODAS AS FUNÇÕES DA SIDEBAR DEVEM EXIBIR CONTEÚDO DINÂMICO DO CSV.
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

if 'aba' not in st.session_state: st.session_state.aba = "bilhete"
if 'banca' not in st.session_state: st.session_state.banca = 1000.0

def carregar():
    if os.path.exists("data/database_diario.csv"): return pd.read_csv("data/database_diario.csv")
    return None

df = carregar()

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, .stApp { background-color: #0b0e11 !important; color: white; font-family: 'Inter', sans-serif; }
    header { display: none !important; }
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: space-between; padding: 0 40px; z-index: 1000000; transform: translate3d(0,0,0); }
    .logo-ia { color: #9d54ff !important; font-weight: 900; font-size: 22px; text-transform: uppercase; text-decoration: none; }
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 16px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 4px solid #6d28d9 !important; }
    .bilhete-master { background: #ffffff !important; color: #111 !important; padding: 25px; border-radius: 8px; max-width: 500px; margin: 0 auto; border-top: 10px solid #9d54ff; box-shadow: 0 10px 40px rgba(0,0,0,0.8); }
    .ticket-row { display: flex; justify-content: space-between; font-size: 11px; border-bottom: 1px solid #f2f2f2; padding: 8px 0; color: #111 !important; }
    .badge-m { background: #f1f5f9; padding: 2px 8px; border-radius: 4px; font-weight: 900; color: #6d28d9; font-size: 9px; }
    .card-full { background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 8px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# HEADER FIXO
st.markdown("""<div class="betano-header"><div class="logo-ia">GESTOR IA</div><div style="display:flex; gap:20px;"><span style="color:white; font-size:10px; font-weight:700;">APOSTAS ESPORTIVAS</span><span style="color:white; font-size:10px; font-weight:700;">AO VIVO</span><span style="color:white; font-size:10px; font-weight:700;">ESTATÍSTICAS</span></div><div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:8px 20px; border-radius:5px; font-size:9px; font-weight:900; cursor:pointer;">ENTRAR</div></div>""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown('<div style="height:70px;"></div>', unsafe_allow_html=True) 
    if st.button("🎟️ GERAR BILHETE DO DIA"): st.session_state.aba = "bilhete"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba = "scanner"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba = "banca"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba = "jogos"
    if st.button("🏆 VENCEDORES"): st.session_state.aba = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba = "gols"
    if st.button("🚩 ESCANTEIOS"): st.session_state.aba = "cantos"

st.markdown('<div style="height:40px;"></div>', unsafe_allow_html=True)

# LÓGICA DE TELAS
if st.session_state.aba == "bilhete":
    st.markdown("<h2 style='text-align:center;'>🎟️ BILHETE MESTRE IA (TOP 20)</h2>", unsafe_allow_html=True)
    if df is not None:
        b_html = '<div class="bilhete-master"><div style="text-align:center; border-bottom:1px solid #eee; padding-bottom:10px; margin-bottom:15px;"><b style="font-size:16px;">GESTOR IA PRO</b><br><span style="font-size:10px; color:#666;">ANÁLISE PROFISSIONAL 20 JOGOS</span></div>'
        s_txt = "🔥 *SINAIS JARVIS IA - TOP 20*\n\n"
        for i, r in df.iterrows():
            b_html += f'<div class="ticket-row"><span><b>{r["CASA"]}</b> x <b>{r["FORA"]}</b></span><span class="badge-m">{r["GOLS"]}</span></div>'
            s_txt += f"✅ {r['CASA']} x {r['FORA']} -> {r['GOLS']} ({r['CONF']})\n"
        b_html += '</div>'
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2: 
            st.markdown(b_html, unsafe_allow_html=True)
            st.code(s_txt, language="text")

elif st.session_state.aba == "scanner":
    st.markdown("## 🎯 SCANNER PRÉ-LIVE")
    if df is not None:
        escolha = st.selectbox("SELECIONE O JOGO PARA ANÁLISE DETALHADA", df['CASA'] + " x " + df['FORA'])
        jogo = df[df['CASA'] + " x " + df['FORA'] == escolha].iloc[0]
        st.markdown(f"""<div class="card-full"><h3>{escolha}</h3><p>💰 Probabilidade: {jogo['CONF']}</p><p>🚩 Escanteios Estimados: {jogo['CANTOS']}</p><p>🟨 Cartões Estimados: {jogo['CARTOES']}</p></div>""", unsafe_allow_html=True)

elif st.session_state.aba == "banca":
    st.markdown("## 💰 GESTÃO DE BANCA")
    st.session_state.banca = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca)
    st.write(f"STAKE RECOMENDADA (1%): R$ {st.session_state.banca * 0.01:.2f}")

elif st.session_state.aba == "jogos":
    st.markdown("## 📅 JOGOS ANALISADOS HOJE")
    if df is not None: st.table(df[['PAIS', 'LIGA', 'CASA', 'FORA', 'CONF']])

elif st.session_state.aba == "vencedores":
    st.markdown("## 🏆 PROBABILIDADE DE VENCEDORES")
    if df is not None:
        for i, r in df.head(5).iterrows():
            st.write(f"✅ {r['CASA']} com {r['CONF']} de chance.")

elif st.session_state.aba == "gols":
    st.markdown("## ⚽ ANALISADOR DE GOLS")
    if df is not None:
        for i, r in df.iterrows():
            if "+2.5" in str(r['GOLS']): st.write(f"🔥 ALTA TENDÊNCIA OVER: {r['CASA']} x {r['FORA']}")

elif st.session_state.aba == "cantos":
    st.markdown("## 🚩 ANALISADOR DE ESCANTEIOS")
    if df is not None:
        for i, r in df.iterrows():
            if r['CANTOS'] > 10: st.write(f"🚩 JOGO PARA CANTOS: {r['CASA']} x {r['FORA']} ({r['CANTOS']} avg)")

st.markdown("""<div style="position:fixed; bottom:0; width:100%; background:#0d0d12; color:#475569; font-size:9px; padding:5px 20px; border-top:1px solid #1e293b;">STATUS: ● IA OPERACIONAL | v91.00 | PROTEÇÃO DE CÓDIGO ATIVA</div>""", unsafe_allow_html=True)
