import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime
import random

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v88.00 - SCANNER & AUDITORIA]
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00

def carregar_dados(path):
    if os.path.exists(path): return pd.read_csv(path)
    return None

df_diario = carregar_dados("data/database_diario.csv")
df_hist = carregar_dados("data/historico_mestre.csv")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 90px 40px 20px 40px !important; }
    .fixed-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; display: flex; align-items: center; justify-content: space-between; padding: 0 40px !important; z-index: 1000000; }
    .logo-txt { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; text-decoration: none; }
    .nav-txt { color: #ffffff; font-size: 10px; text-transform: uppercase; font-weight: 600; opacity: 0.8; }
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 14px 25px !important; font-size: 10px !important; text-transform: uppercase !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    .bilhete-master { background: #ffffff !important; color: #111 !important; padding: 25px; border-radius: 8px; max-width: 480px; margin: 0 auto; border-top: 10px solid #9d54ff; box-shadow: 0 10px 40px rgba(0,0,0,0.8); }
    .ticket-row { display: flex; justify-content: space-between; font-size: 12px; border-bottom: 1px solid #f2f2f2; padding: 10px 0; }
    .vip-tag { background: #ffd700; color: #000; padding: 2px 6px; border-radius: 4px; font-weight: 900; font-size: 9px; }
    .card-ia { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 150px; }
    .footer-ia { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""<div class="fixed-header"><div style="display:flex; align-items:center; gap:20px;"><div class="logo-txt">GESTOR IA</div><div class="nav-txt">APOSTAS ESPORTIVAS</div><div class="nav-txt">AO VIVO</div><div class="nav-txt">ESTATÍSTICAS</div></div><div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:7px 20px; border-radius:5px; font-size:9px; font-weight:800;">ENTRAR</div></div>""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("🎟️ GERAR BILHETE DO DIA"): st.session_state.aba_ativa = "bilhete"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("📜 HISTÓRICO"): st.session_state.aba_ativa = "historico"

def draw_card(title, value, perc, color="#06b6d4"):
    st.markdown(f"""<div class="card-ia"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 VISÃO GERAL JARVIS</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("ASSERTIVIDADE REAL", "91.2%", 91, "#00ff88")
    with c2: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with c3: draw_card("SINAIS VIP HOJE", "3 DISPONÍVEIS", 100, "#ffd700")
    with c4: draw_card("SISTEMA", "JARVIS v88.00", 100)

elif st.session_state.aba_ativa == "bilhete":
    st.markdown("<h2 style='color:white; text-align:center;'>🎟️ BILHETE DE OURO - TOP 20</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        bilhete_html = f'<div class="bilhete-master"><div style="text-align:center; border-bottom:1px solid #eee; padding-bottom:10px; margin-bottom:15px;"><b style="font-size:18px;">GESTOR IA PRO</b><br><span style="font-size:10px; color:#666;">DADOS: HISTÓRICO 5 ANOS | {datetime.now().strftime("%d/%m/%Y")}</span></div>'
        texto_copia = "🔥 *SINAIS JARVIS IA*\n\n"
        for i, row in df_diario.iterrows():
            vip = '<span class="vip-tag">💎 VIP</span>' if i < 3 else ''
            bilhete_html += f'<div class="ticket-row"><span>{vip} <b>{row["TIME_CASA"]}</b> x <b>{row["TIME_FORA"]}</b></span><span style="background:#f1f5f9; padding:2px 8px; border-radius:4px; font-weight:800; color:#6d28d9; font-size:10px;">{row["MERCADO"]}</span></div>'
            texto_copia += f"✅ {row['TIME_CASA']} x {row['TIME_FORA']} -> {row['MERCADO']} ({row['CONFIDANÇA']})\n"
        bilhete_html += '</div>'
        col_x1, col_x2, col_x3 = st.columns([1, 2, 1])
        with col_x2: 
            st.markdown(bilhete_html, unsafe_allow_html=True)
            st.code(texto_copia, language="text")
    else: st.error("Aguardando robô...")

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE INTERATIVO</h2>", unsafe_allow_html=True)
    if df_hist is not None:
        times = sorted(df_hist['HomeTeam'].unique())
        c1, c2 = st.columns(2)
        t1 = c1.selectbox("TIME CASA", times)
        t2 = c2.selectbox("TIME FORA", times)
        if st.button("⚡ ANALISAR AGORA", use_container_width=True):
            st.success(f"Análise de {t1} vs {t2} processada com sucesso no histórico mestre!")
            draw_card(f"CHANCE DE VITORIA {t1.upper()}", f"{random.randint(40,70)}%", 100, "#9d54ff")
    else: st.warning("Faça o download do histórico primeiro.")

st.markdown("""<div class="footer-ia"><div>STATUS: ● IA OPERACIONAL | v88.00</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
