import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v89.00 - FULL STATS & FIX LAYOUT]
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"

def carregar_dados():
    if os.path.exists("data/database_diario.csv"): return pd.read_csv("data/database_diario.csv")
    return None

df_diario = carregar_dados()

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, .stApp { background-color: #0b0e11 !important; color: white; font-family: 'Inter', sans-serif; }
    header { display: none !important; }
    .fixed-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: center; justify-content: space-between; padding: 0 40px; z-index: 1000000; }
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; }
    /* AJUSTE PARA NÃO CORTAR TEXTO */
    .stCodeBlock { background: #161b22 !important; border: 1px solid #1e293b !important; border-radius: 8px !important; }
    .stCodeBlock code { white-space: pre-wrap !important; word-break: break-all !important; color: #00ff88 !important; }
    
    .bilhete-master { background: #ffffff !important; color: #111 !important; padding: 20px; border-radius: 8px; max-width: 500px; margin: 0 auto; border-top: 10px solid #9d54ff; }
    .ticket-row { display: flex; justify-content: space-between; font-size: 11px; border-bottom: 1px solid #f0f0f0; padding: 8px 0; }
    .market-badge { background: #f1f5f9; padding: 2px 6px; border-radius: 4px; font-weight: 800; color: #6d28d9; font-size: 9px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""<div class="fixed-header"><div style="color:#9d54ff; font-weight:900; font-size:20px;">GESTOR IA</div><div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:7px 20px; border-radius:5px; font-size:9px; font-weight:800;">ENTRAR</div></div>""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("🎟️ GERAR BILHETE DO DIA"): st.session_state.aba_ativa = "bilhete"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='margin-top:30px;'>📅 RESUMO DO DIA</h2>", unsafe_allow_html=True)
    if df_diario is not None: st.dataframe(df_diario, use_container_width=True)

elif st.session_state.aba_ativa == "bilhete":
    st.markdown("<h2 style='text-align:center; margin-top:30px;'>🎟️ BILHETE MESTRE IA</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        bilhete_html = f'<div class="bilhete-master"><div style="text-align:center; border-bottom:1px solid #eee; padding-bottom:10px; margin-bottom:15px;"><b style="font-size:16px;">GESTOR IA PRO - ANÁLISE 7 NÍVEIS</b></div>'
        texto_copia = "🔥 *SINAIS JARVIS - 7 CATEGORIAS*\n\n"
        
        for i, row in df_diario.iterrows():
            bilhete_html += f'<div class="ticket-row"><span><b>{row["TIME_CASA"]}</b> x <b>{row["TIME_FORA"]}</b></span><span class="market-badge">{row["MERCADO"]}</span></div>'
            
            # Texto detalhado para cópia
            texto_copia += f"✅ *{row['TIME_CASA']} x {row['TIME_FORA']}*\n"
            texto_copia += f"💰 Win: {row['CONFIDANÇA']} | ⚽ Gols: {row['MERCADO']}\n"
            texto_copia += f"🚩 Cantos: {row['CANTOS']} | 🟨 Cards: {row['CARTOES']}\n"
            texto_copia += f"👟 Chutes: {row['CHUTES']} | 🧤 Defesas: {row['DEFESAS']}\n"
            texto_copia += f"🥅 T.Meta: {row['TMETA']}\n"
            texto_copia += "--------------------------\n"
        
        bilhete_html += '</div>'
        col_x1, col_x2, col_x3 = st.columns([1, 2, 1])
        with col_x2: 
            st.markdown(bilhete_html, unsafe_allow_html=True)
            st.markdown("### 📋 COPIAR SINAIS COMPLETOS")
            st.code(texto_copia, language="text") # Corrigido para não cortar
    else: st.error("Rode o robô no Actions primeiro!")

st.markdown("""<div style="position:fixed; bottom:0; width:100%; background:#0d0d12; color:#475569; font-size:9px; padding:5px 20px; border-top:1px solid #1e293b;">STATUS: ● IA OPERACIONAL | v89.00 | 7 CATEGORIAS ATIVAS</div>""", unsafe_allow_html=True)
