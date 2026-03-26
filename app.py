import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime
import random

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v72.00 - FIX FINAL DE BILHETE E HEADER]
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

# 2. CAMADA DE ESTILO CSS (RESTAURAÇÃO TOTAL v57.35)
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
    [data-testid="stMainBlockContainer"] { padding: 95px 40px 20px 40px !important; }
    
    /* HEADER FIXO SUPERIOR */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    
    .header-left { display: flex; align-items: center; gap: 30px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    
    .nav-links { display: flex; gap: 20px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 10.5px !important; text-transform: uppercase; font-weight: 600 !important; cursor: pointer; white-space: nowrap; opacity: 0.9; }
    .nav-item:hover { color: #06b6d4 !important; opacity: 1; }

    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }

    /* SIDEBAR */
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -30px !important; gap: 0px !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    /* CARDS */
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; }
    
    /* BILHETE DE OURO - CORREÇÃO DE CONTAINER */
    .bilhete-master { 
        background: #ffffff !important; color: #111 !important; padding: 25px; 
        border-radius: 2px; font-family: 'Courier New', monospace; 
        max-width: 480px; margin: 0 auto; border-top: 10px solid #9d54ff; 
        box-shadow: 0 10px 40px rgba(0,0,0,0.8);
    }
    .ticket-row { display: flex; justify-content: space-between; font-size: 11px; border-bottom: 1px dashed #ccc; padding: 8px 0; color: #111 !important; }
    
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER HTML FIXO (COM TODOS OS LINKS)
st.markdown("""
    <div class="betano-header">
        <div class="header-left">
            <div class="logo-link">GESTOR IA</div>
            <div class="nav-links">
                <div class="nav-item">APOSTAS ESPORTIVAS</div>
                <div class="nav-item">APOSTAS AO VIVO</div>
                <div class="nav-item">APOSTAS ENCONTRADAS</div>
                <div class="nav-item">ESTATÍSTICAS AVANÇADAS</div>
                <div class="nav-item">MERCADO PROBABILÍSTICO</div>
                <div class="nav-item">ASSERTIVIDADE IA</div>
            </div>
        </div>
        <div class="header-right">
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. SIDEBAR
with st.sidebar:
    st.markdown('<div style="height:75px;"></div>', unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🎟️ GERAR BILHETE DO DIA"): st.session_state.aba_ativa = "bilhete"

def draw_card(title, value, perc):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- LÓGICA DE TELAS ---
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with c2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with c3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with c4: draw_card("SISTEMA", "JARVIS v72.00", 100)

elif st.session_state.aba_ativa == "bilhete":
    st.markdown("<h2 style='color:white; text-align:center;'>🎟️ SEU BILHETE PRONTO</h2>", unsafe_allow_html=True)
    if df_diario is not None and not df_diario.empty:
        top_20 = df_diario.head(20)
        
        # CONSTRUÇÃO DO HTML DO BILHETE EM UMA ÚNICA STRING
        html_bilhete = f"""
        <div class="bilhete-master">
            <div style="text-align:center; font-weight:900; font-size:20px; border-bottom:2px solid #111; margin-bottom:15px; padding-bottom:10px;">GESTOR IA PRO</div>
            <div style="font-size:10px; text-align:center; margin-bottom:15px;">GERADO EM: {datetime.now().strftime('%d/%m/%Y %H:%M')}</div>
        """
        
        for _, row in top_20.iterrows():
            html_bilhete += f"""
            <div class="ticket-row">
                <span>{row['TIME_CASA']} x {row['TIME_FORA']}</span>
                <b>OVER 1.5</b>
            </div>
            """
            
        html_bilhete += "</div>"
        
        col_x1, col_x2, col_x3 = st.columns([1, 2, 1])
        with col_x2:
            st.markdown(html_bilhete, unsafe_allow_html=True)
    else: st.error("Aguardando carregamento de jogos...")

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v72.00</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
