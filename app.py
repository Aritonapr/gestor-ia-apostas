import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE RECUPERAÇÃO v59.62 - BLINDAGEM DE INTERFACE]
# ESTADO: CRÍTICO | AÇÃO: RESTAURAÇÃO DE CSS E CORREÇÃO DE SINTAXE
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA (ESTRUTURA FIXA)
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA (UNIFICAÇÃO DE VARIÁVEIS) ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'metrics_ia' not in st.session_state:
    st.session_state.metrics_ia = {
        'geral': 85.5, 'gols': 78.2, 'cantos': 82.1, 'win': 65.4,
        'roi': 12.5, 'lucro': 1250.00, 'calls': 450, 'erros': 14.5
    }
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# ==============================================================================
# 2. CAMADA DE ESTILO CSS (APARÊNCIA IMUTÁVEL - ZERO WHITE)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* REMOVER SCROLLBAR E ELEMENTOS PADRÃO STREAMLIT */
    ::-webkit-scrollbar { display: none !important; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }

    /* FUNDO DARK - ZERO WHITE */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }

    /* HEADER FIXO - BETANO STYLE */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    .nav-links { display: flex; gap: 20px; }
    .nav-item { color: #ffffff !important; font-size: 10px !important; font-weight: 600; text-transform: uppercase; cursor: pointer; white-space: nowrap; }

    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }

    /* SIDEBAR CUSTOM */
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    /* CARDS DE KPI */
    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
    }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. COMPONENTES DE INTERFACE
def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;">
                <div style="background:{color_footer}; height:100%; width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR E NAVEGAÇÃO
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <div class="logo-link">GESTOR IA</div>
                <div class="nav-links">
                    <div class="nav-item">APOSTAS ESPORTIVAS</div>
                    <div class="nav-item">ESTATÍSTICAS AVANÇADAS</div>
                    <div class="nav-item">ASSERTIVIDADE IA</div>
                </div>
            </div>
            <div class="header-right" style="display:flex; gap:10px; align-items:center;">
                <div class="registrar-pill">REGISTRAR</div>
                <div class="entrar-grad">ENTRAR</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("📊 ASSERTIVIDADE IA"): st.session_state.aba_ativa = "assertividade"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"

# 5. LÓGICA DAS TELAS (BACK-END)
if st.session_state.aba_ativa == "assertividade":
    st.markdown("<h2 style='color:white;'>📊 ASSERTIVIDADE & IA</h2>", unsafe_allow_html=True)
    m = st.session_state.metrics_ia
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("ASSERTIVIDADE GERAL", f"{m['geral']}%", m['geral'])
    with h2: draw_card("GOLS OVER", f"{m['gols']}%", m['gols'])
    with h3: draw_card("CANTOS OVER", f"{m['cantos']}%", m['cantos'])
    with h4: draw_card("WIN RATE", f"{m['win']}%", m['win'])
    
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("ROI ACUMULADO", f"{m['roi']}%", 100, "#00d2ff")
    with h6: draw_card("LUCRO MENSAL", f"R$ {m['lucro']:.2f}", 100, "#00d2ff")
    with h7: draw_card("TOTAL DE CALLS", str(m['calls']), 100, "#00d2ff")
    with h8: draw_card("ERROS DE IA", f"{m['erros']}%", m['erros'], "#ff4b4b")

elif st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO - TOP 20 IA</h2>", unsafe_allow_html=True)
    st.info("Sincronizando as melhores entradas do dia...")

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    # Correção do db_ligas (SyntaxError resolvido)
    db_ligas = {
        "BRASIL": ["SÉRIE A", "SÉRIE B"],
        "INGLATERRA": ["PREMIER LEAGUE", "CHAMPIONSHIP"]
    }
    st.selectbox("🌎 SELECIONE A REGIÃO", list(db_ligas.keys()))
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        st.success("Análise finalizada com sucesso.")

# FOOTER DE STATUS
st.markdown(f"""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v59.62</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
