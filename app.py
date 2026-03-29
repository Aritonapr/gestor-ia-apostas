import streamlit as st
import pandas as pd
import os
import requests
from datetime import datetime
from io import StringIO

# [PROTOCOLO v60.00 - BLINDAGEM TOTAL]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

def carregar_dados():
    url = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    try:
        r = requests.get(f"{url}?v={datetime.now().timestamp()}")
        if r.status_code == 200:
            return pd.read_csv(StringIO(r.text))
    except: return None
    return None

df_diario = carregar_dados()

# --- CSS PRESERVADO ---
st.markdown("""<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; display: flex; align-items: center; justify-content: space-between; padding: 0 40px !important; z-index: 1000000; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
</style>""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""<div class="betano-header"><div class="logo-link">GESTOR IA</div></div><div style="height:65px;"></div>""", unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        st.success(f"✅ JARVIS OPERANDO NO SEU TEMPO: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        st.dataframe(df_diario, use_container_width=True)

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        st.dataframe(df_diario, use_container_width=True, hide_index=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v62.0</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
