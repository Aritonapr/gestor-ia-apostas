import streamlit as st
import pandas as pd
import os
import requests
from datetime import datetime
from io import StringIO

# [PROTOCOLO v60.00 - BLINDAGEM TOTAL]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- INICIALIZAÇÃO ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# --- CARREGAMENTO DE DADOS (FORÇANDO ATUALIZAÇÃO) ---
def carregar_dados_vivos():
    url = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    url_h = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/historico_5_temporadas.csv"
    try:
        # Pula o cache com um timestamp
        r = requests.get(f"{url}?v={datetime.now().timestamp()}", timeout=10)
        h = requests.get(url_h, timeout=10)
        d = pd.read_csv(StringIO(r.text)) if r.status_code == 200 else None
        hist = pd.read_csv(StringIO(h.text)) if h.status_code == 200 else None
        return d, hist
    except: return None, None

df_diario, df_hist = carregar_dados_vivos()

# --- CSS PRESERVADO ---
st.markdown("""<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; display: flex; align-items: center; justify-content: space-between; padding: 0 40px !important; z-index: 1000000; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important;}
    div.stButton > button:not([data-testid="stSidebar"] *) { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: #ffffff !important; border: none !important; padding: 15px 20px !important; font-weight: 900 !important; border-radius: 6px !important; width: 100% !important; margin-top: 10px !important;}
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
</style>""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("""<div class="betano-header"><div class="logo-link">GESTOR IA</div></div><div style="height:65px;"></div>""", unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"

def draw_card(title, value, perc):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; border-radius:10px; margin-top:10px;"><div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- TELAS ---
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    if df_diario is not None:
        if "Blackpool" in str(df_diario.iloc[0]):
            st.error("⚠️ SISTEMA EM MANUTENÇÃO: Os dados no GitHub ainda são antigos. Clique em 'Run Workflow' no GitHub.")
        else:
            st.success(f"✅ DADOS ATUALIZADOS: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
            st.dataframe(df_diario, use_container_width=True)

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        if "Blackpool" in str(df_diario.iloc[0]): st.warning("Aguardando robô limpar dados antigos...")
        else: st.dataframe(df_diario, use_container_width=True, hide_index=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    t = st.text_input("🏠 NOME DO TIME", "Flamengo")
    if st.button("⚡ ANALISAR"):
        conf = 75.0
        if df_hist is not None:
            f = df_hist[df_hist['Casa'].str.contains(t[:5], case=False, na=False)]
            if not f.empty: conf = round((len(f[f['Resultado']=='H'])/len(f))*100 + 10, 1)
        st.write(f"### Confiança Jarvis para {t}: {conf}%")

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v61.0</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
