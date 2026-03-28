import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v59.61 - CORREÇÃO DE ESTRUTURA]
# DIRETRIZ: RECUPERAÇÃO DE INTERFACE E UNIFICAÇÃO DE VARIÁVEIS
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# Correção NameError: Unificando para 'metrics_ia' conforme v59.6
if 'metrics_ia' not in st.session_state:
    st.session_state.metrics_ia = {
        'geral': 85.5, 'gols': 78.2, 'cantos': 82.1, 'win': 65.4,
        'roi': 12.5, 'lucro': 1250.00, 'calls': 450, 'erros': 14.5
    }

# ==============================================================================
# 2. CAMADA DE ESTILO CSS INTEGRAL (RESTAURAÇÃO ZERO WHITE)
# ==============================================================================
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
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
        transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    
    .header-left { display: flex; align-items: center; gap: 25px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; letter-spacing: 0.5px; text-decoration: none; cursor: pointer;}
    
    .nav-links { display: flex; gap: 22px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600 !important; letter-spacing: 0.5px; transition: 0.3s ease; cursor: pointer; white-space: nowrap; }
    .nav-item:hover { color: #06b6d4 !important; transform: scale(1.05); }

    .header-right { display: flex; align-items: center; gap: 15px; }
    .search-lupa { color: #ffffff; font-size: 15px; cursor: pointer; }
    
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; transition: 0.3s ease; cursor: pointer; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; transition: 0.3s ease; cursor: pointer; }

    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: all 0.2s ease !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important;
        border-radius: 6px !important; width: 100% !important; margin-top: 10px !important;
    }

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
    }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR - IMUTÁVEL
with st.sidebar:
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
                <div class="search-lupa">🔍</div>
                <div class="registrar-pill">REGISTRAR</div>
                <div class="entrar-grad">ENTRAR</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    # BOTÕES DA SIDEBAR (Correção de Indentação - Imagem 1)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("📊 ASSERTIVIDADE IA"): st.session_state.aba_ativa = "assertividade"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

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

# 4. LÓGICA DE TELAS
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
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with c2: draw_card("ASSERTIVIDADE", f"{st.session_state.metrics_ia['geral']}%", st.session_state.metrics_ia['geral'])
    with c3: draw_card("STATUS IA", "ONLINE", 100, "#00ff88")
    with c4: draw_card("VERSÃO", "v59.61", 100)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    st.selectbox("🌎 REGIÃO / PAÍS", ["BRASIL", "INGLATERRA", "ESPANHA", "ALEMANHA"])
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        st.session_state.analise_bloqueada = {"casa": "Time A", "fora": "Time B", "vencedor": "ALTA", "gols": "OVER 1.5", "cor": "#00ff88", "data": datetime.now().strftime("%H:%M")}
    
    if st.session_state.analise_bloqueada:
        st.success("ANÁLISE CONCLUÍDA")
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", "INDEFINIDO", 50)
        with r2: draw_card("GOLS", "REVISAR", 40)
        with r3: draw_card("STAKE", "R$ 10.00", 100)
        with r4: draw_card("CANTOS", "9.5+", 65)

# FOOTER FIXO
st.markdown(f"""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v59.61 | {datetime.now().strftime("%d/%m/%Y %H:%M")}</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
