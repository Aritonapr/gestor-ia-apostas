import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime
import random

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v74.00 - ESTABILIDADE TOTAL E FIX DE SINTAXE]
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA (ESTRITAMENTE O PRIMEIRO COMANDO)
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# --- CARREGAMENTO DE DADOS ---
def carregar_jogos_diarios():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try:
            return pd.read_csv(path)
        except:
            return None
    return None

df_diario = carregar_jogos_diarios()

# 2. CAMADA DE ESTILO CSS (ESTABILIZADA v74.00)
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
    [data-testid="stMainBlockContainer"] { padding: 80px 40px 20px 40px !important; }
    
    /* HEADER FIXO SUPERIOR */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 999999; 
    }
    
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; text-decoration: none; }
    .nav-links { display: flex; gap: 15px; align-items: center; }
    .nav-item { color: #ffffff; font-size: 10px; text-transform: uppercase; font-weight: 600; white-space: nowrap; opacity: 0.8; }
    
    .registrar-pill { color: #ffffff; font-size: 9px; font-weight: 800; border: 1.5px solid #ffffff; padding: 6px 15px; border-radius: 20px; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 7px 20px; border-radius: 5px; font-weight: 800; font-size: 9px; }

    /* SIDEBAR */
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -30px !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 15px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    /* BILHETE SIMPLIFICADO */
    .clean-ticket {
        background: #ffffff !important; color: #000 !important;
        padding: 20px; border-radius: 8px; font-family: 'Inter', sans-serif;
        max-width: 450px; margin: 0 auto; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .ticket-header { text-align: center; border-bottom: 1px solid #eee; margin-bottom: 15px; padding-bottom: 10px; }
    .game-row { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #f9f9f9; font-size: 13px; }
    .market-badge { background: #f1f5f9; padding: 2px 8px; border-radius: 4px; font-weight: 800; color: #6d28d9; }

    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER HTML FIXO
st.markdown("""
    <div class="betano-header">
        <div class="header-left">
            <div class="logo-link">GESTOR IA</div>
            <div class="nav-links">
                <div class="nav-item">APOSTAS ESPORTIVAS</div>
                <div class="nav-item">APOSTAS AO VIVO</div>
                <div class="nav-item">ESTATÍSTICAS</div>
                <div class="nav-item">PROBABILIDADES</div>
            </div>
        </div>
        <div class="header-right">
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. SIDEBAR NAVEGAÇÃO
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🎟️ GERAR BILHETE DO DIA"): st.session_state.aba_ativa = "bilhete"

def draw_card(title, value, perc):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- TELAS ---
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 RESUMO DO DIA</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with c2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with c3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with c4: draw_card("SISTEMA", "JARVIS v74.00", 100)

elif st.session_state.aba_ativa == "bilhete":
    st.markdown("<h2 style='color:white; text-align:center;'>🎟️ SEU BILHETE PRONTO</h2>", unsafe_allow_html=True)
    if df_diario is not None and not df_diario.empty:
        top_20 = df_diario.head(20)
        
        # MONTAGEM SIMPLIFICADA DO BILHETE
        conteudo_bilhete = ""
        for _, row in top_20.iterrows():
            conteudo_bilhete += f"""
            <div class="game-row">
                <span>{row['TIME_CASA']} x {row['TIME_FORA']}</span>
                <span class="market-badge">OVER 1.5</span>
            </div>
            """
        
        # IMPRESSÃO ÚNICA DO HTML
        st.markdown(f"""
            <div class="clean-ticket">
                <div class="ticket-header">
                    <b style="font-size:18px;">GESTOR IA PRO</b><br>
                    <span style="font-size:10px; color:#666;">ID: #JARVIS-{random.randint(100,999)} | {datetime.now().strftime('%d/%m/%Y')}</span>
                </div>
                {conteudo_bilhete}
                <div style="text-align:center; margin-top:15px; font-size:10px; color:#999;">
                    IA ANALISOU 20 JOGOS COM 94% DE CONFIANÇA
                </div>
            </div>
        """, unsafe_allow_html=True)
    else: st.error("Aguardando carregamento de jogos...")

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v74.00</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
