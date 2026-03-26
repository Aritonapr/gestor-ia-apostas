import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime
import random

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v76.00 - ANTI-FLICKER & SIDEBAR REORDENADA]
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# --- CARREGAMENTO DE DADOS ---
def carregar_jogos_diarios():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try: return pd.read_csv(path)
        except: return None
    return None

df_diario = carregar_jogos_diarios()

# 2. CAMADA DE ESTILO CSS (OTIMIZADA PARA ESTABILIDADE)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }

    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 90px 40px 20px 40px !important; }
    
    /* HEADER FIXO - SEM PISCAR */
    .fixed-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    .logo-txt { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; }
    .nav-box { display: flex; gap: 18px; }
    .nav-txt { color: #ffffff; font-size: 10px; text-transform: uppercase; font-weight: 600; opacity: 0.8; }
    
    .btn-registrar { color: #ffffff; font-size: 9px; font-weight: 800; border: 1.5px solid #ffffff; padding: 6px 15px; border-radius: 20px; }
    .btn-entrar { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 7px 20px; border-radius: 5px; font-weight: 800; font-size: 9px; }

    /* SIDEBAR */
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow-y: auto !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -10px !important; gap: 0px !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 14px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    /* BILHETE DE OURO - VISUAL LIMPO */
    .bilhete-master { 
        background: #ffffff !important; color: #111 !important; padding: 25px; 
        border-radius: 8px; font-family: 'Inter', sans-serif; 
        max-width: 480px; margin: 0 auto; border-top: 10px solid #9d54ff; 
        box-shadow: 0 10px 40px rgba(0,0,0,0.8);
    }
    .ticket-row { display: flex; justify-content: space-between; font-size: 12px; border-bottom: 1px solid #f2f2f2; padding: 10px 0; }
    .badge-market { background: #f1f5f9; padding: 3px 10px; border-radius: 4px; font-weight: 900; color: #6d28d9; font-size: 10px; }

    .card-ia { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; }
    .footer-ia { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER HTML (IMPRESSÃO ÚNICA)
st.markdown("""
    <div class="fixed-header">
        <div class="nav-box">
            <div class="logo-txt">GESTOR IA</div>
            <div class="nav-txt">APOSTAS ESPORTIVAS</div>
            <div class="nav-txt">APOSTAS AO VIVO</div>
            <div class="nav-txt">ESTATÍSTICAS</div>
            <div class="nav-txt">PROBABILIDADES</div>
        </div>
        <div style="display:flex; gap:10px;">
            <div class="btn-registrar">REGISTRAR</div>
            <div class="btn-entrar">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. SIDEBAR REORDENADA
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    # BOTÕES PRINCIPAIS NO TOPO
    if st.button("🎟️ GERAR BILHETE DO DIA"): st.session_state.aba_ativa = "bilhete"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("🏆 VENCEDORES"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc):
    st.markdown(f"""<div class="card-ia"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- LÓGICA DE TELAS ---
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 RESUMO DO DIA</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with c2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with c3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with c4: draw_card("SISTEMA", "JARVIS v76.00", 100)

elif st.session_state.aba_ativa == "bilhete":
    st.markdown("<h2 style='color:white; text-align:center;'>🎟️ SEU BILHETE PRONTO</h2>", unsafe_allow_html=True)
    if df_diario is not None and not df_diario.empty:
        top_20 = df_diario.head(20)
        bilhete_html = f"""
        <div class="bilhete-master">
            <div style="text-align:center; border-bottom:1px solid #eee; padding-bottom:10px; margin-bottom:15px;">
                <b style="font-size:18px;">GESTOR IA PRO</b><br>
                <span style="font-size:10px; color:#666;">ID: #JARVIS-{random.randint(100,999)} | {datetime.now().strftime('%d/%m/%Y')}</span>
            </div>
        """
        for _, row in top_20.iterrows():
            bilhete_html += f"""<div class="ticket-row"><span><b>{row['TIME_CASA']}</b> x <b>{row['TIME_FORA']}</b></span><span class="badge-market">OVER 1.5 GOLS</span></div>"""
        bilhete_html += "</div>"
        
        col_x1, col_x2, col_x3 = st.columns([1, 2, 1])
        with col_x2: st.markdown(bilhete_html, unsafe_allow_html=True)
    else: st.error("Aguardando carregamento de jogos do robô...")

else:
    st.markdown(f"<h2 style='color:white;'>📊 {st.session_state.aba_ativa.upper()}</h2>", unsafe_allow_html=True)
    st.info("Scanner operando. Os dados estatísticos estão sendo processados pela IA.")

st.markdown("""<div class="footer-ia"><div>STATUS: ● IA OPERACIONAL | v76.00</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
