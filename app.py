import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO v90.00 - RESULTADOS DIRETOS E AUTÔNOMOS]
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

if 'aba' not in st.session_state: st.session_state.aba = "bilhete"

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
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: center; justify-content: space-between; padding: 0 40px; z-index: 1000000; }
    .nav-item { color: #ffffff; font-size: 10px; text-transform: uppercase; font-weight: 600; opacity: 0.8; margin-right: 15px; }
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 16px 25px !important; font-size: 10px !important; text-transform: uppercase !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    .bilhete-master { background: #ffffff !important; color: #111 !important; padding: 25px; border-radius: 8px; max-width: 480px; margin: 0 auto; border-top: 10px solid #9d54ff; box-shadow: 0 10px 40px rgba(0,0,0,0.8); }
    .ticket-row { display: flex; justify-content: space-between; font-size: 12px; border-bottom: 1px solid #f0f0f0; padding: 10px 0; color: #111 !important; }
    .badge-m { background: #f1f5f9; padding: 3px 8px; border-radius: 4px; font-weight: 800; color: #6d28d9; font-size: 10px; }
    </style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""<div class="betano-header"><div style="color:#9d54ff; font-weight:900; font-size:20px;">GESTOR IA</div><div style="display:flex;"><span class="nav-item">ESPORTIVAS</span><span class="nav-item">AO VIVO</span><span class="nav-item">ESTATÍSTICAS</span></div><div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:7px 20px; border-radius:5px; font-size:9px; font-weight:800;">ENTRAR</div></div>""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown('<div style="height:70px;"></div>', unsafe_allow_html=True) 
    if st.button("🎟️ GERAR BILHETE DO DIA"): st.session_state.aba = "bilhete"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba = "scanner"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba = "banca"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba = "jogos"
    if st.button("🏆 VENCEDORES"): st.session_state.aba = "vence"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba = "gols"
    if st.button("🚩 ESCANTEIOS"): st.session_state.aba = "cantos"

# CONTEÚDO
st.markdown('<div style="height:40px;"></div>', unsafe_allow_html=True)

if st.session_state.aba == "bilhete":
    st.markdown("<h2 style='text-align:center;'>🎟️ BILHETE MESTRE IA</h2>", unsafe_allow_html=True)
    if df is not None:
        # BILHETE VISUAL
        b_html = f'<div class="bilhete-master"><div style="text-align:center; border-bottom:1px solid #eee; padding-bottom:10px; margin-bottom:15px;"><b style="font-size:18px;">GESTOR IA PRO</b><br><span style="font-size:10px; color:#666;">ANÁLISE COMPLETA 7 NÍVEIS</span></div>'
        sinal_txt = "🔥 *SINAIS JARVIS IA*\n\n"
        
        for i, r in df.iterrows():
            b_html += f'<div class="ticket-row"><span><b>{r["CASA"]}</b> x <b>{r["FORA"]}</b></span><span class="badge-m">{r["GOLS"]}</span></div>'
            sinal_txt += f"✅ *{r['CASA']} x {r['FORA']}*\n💰 Confiança: {r['CONF']} | ⚽ Gols: {r['GOLS']}\n🚩 Cantos: {r['CANTOS']} | 🟨 Cards: {r['CARTOES']}\n👟 Chutes: {r['CHUTES']} | 🧤 Defesas: {r['DEFESAS']}\n🥅 T.Meta: {r['TMETA']}\n----------\n"
        
        b_html += '</div>'
        
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            st.markdown(b_html, unsafe_allow_html=True)
            st.markdown("### 📋 COPIAR RESULTADOS")
            st.code(sinal_txt, language="text")
    else: st.info("Rode a Automação no GitHub Actions primeiro.")

else:
    st.markdown(f"## {st.session_state.aba.upper()}")
    st.info("Módulo operando em segundo plano. Resultados disponíveis no Bilhete.")

st.markdown("""<div style="position:fixed; bottom:0; width:100%; background:#0d0d12; color:#475569; font-size:9px; padding:5px 20px; border-top:1px solid #1e293b;">STATUS: ● IA OPERACIONAL | v90.00 | 7 CATEGORIAS</div>""", unsafe_allow_html=True)
