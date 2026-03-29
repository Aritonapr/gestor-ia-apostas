import streamlit as st
import pandas as pd
import os
import requests
from datetime import datetime
from io import StringIO

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v62.0 - INTEGRIDADE TOTAL]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO) - UI v57.35
# DIRETRIZ 5: CÓDIGO 100% ÍNTEGRO - SEM ABREVIAÇÕES
# MODIFICAÇÃO ATUAL: RESTAURAÇÃO DE ÍCONES E REMOÇÃO DE SCROLLBAR SIDEBAR
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA (ESTRUTURA PRIMÁRIA) ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# --- CARREGAMENTO DE DADOS VIVOS (DIRETRIZ 2: CÉREBRO IA) ---
def carregar_dados_vivos():
    url_d = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    url_h = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/historico_5_temporadas.csv"
    try:
        ts = datetime.now().timestamp()
        r_d = requests.get(f"{url_d}?v={ts}", timeout=10)
        r_h = requests.get(f"{url_h}?v={ts}", timeout=10)
        d = pd.read_csv(StringIO(r_d.text)) if r_d.status_code == 200 else None
        h = pd.read_csv(StringIO(r_h.text)) if r_h.status_code == 200 else None
        return d, h
    except: 
        return None, None

df_diario, df_hist = carregar_dados_vivos()

# ==============================================================================
# 2. CAMADA DE ESTILO CSS INTEGRAL (UI v57.35 + NO-SCROLL SIDEBAR)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* REMOÇÃO DE SCROLLBAR GLOBAL E SIDEBAR */
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    
    [data-testid="stSidebar"] > div:first-child {
        overflow-y: hidden !important;
        -ms-overflow-style: none !important;
        scrollbar-width: none !important;
    }

    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    /* HEADER SUPERIOR DINÂMICO */
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
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600; letter-spacing: 0.5px; transition: 0.3s ease; cursor: pointer; white-space: nowrap; }
    .nav-item:hover { color: #06b6d4 !important; transform: scale(1.05); }

    .header-right { display: flex; align-items: center; gap: 15px; }
    .search-lupa { color: #ffffff; font-size: 15px; cursor: pointer; }
    
    .registrar-pill { 
        color: #ffffff !important; font-size: 9px !important; font-weight: 800; 
        border: 1.5px solid #ffffff !important; padding: 7px 18px !important; 
        border-radius: 20px !important; transition: 0.3s ease; cursor: pointer;
    }
    .registrar-pill:hover { background: white !important; color: #001a4d !important; }
    
    .entrar-grad { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: white !important; padding: 8px 22px !important; border-radius: 5px !important; 
        font-weight: 800; font-size: 9.5px; transition: 0.3s ease; cursor: pointer;
    }

    /* SIDEBAR CUSTOM */
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 11px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: all 0.2s ease !important; font-weight: 600 !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important;
    }

    /* CARDS */
    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
    }
    
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    .banner-green { background: rgba(0,255,136,0.05); border-left: 5px solid #00ff88; padding: 18px; border-radius: 6px; margin-bottom: 25px; color: white; font-size: 11px; font-weight: 800; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SUPERIOR FIXO
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <a href="#" class="logo-link">GESTOR IA</a>
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

    # BOTÕES DE NAVEGAÇÃO NA SIDEBAR (RESTAURADOS COM ÍCONES CONFORME IMAGEM)
    if st.button("🎯  SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡  SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰  GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜  HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅  BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🏆  VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽  APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩  APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

# FUNÇÃO DE RENDERIZAÇÃO DE CARDS
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

# ==============================================================================
# 4. LÓGICA DE TELAS
# ==============================================================================

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    
    # LINHA 1 DE CARDS (OBRIGATÓRIO: 4 COLUNAS)
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with c2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with c3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with c4: draw_card("IA STATUS", "ONLINE", 100)
    
    # LINHA 2 DE CARDS
    c5, c6, c7, c8 = st.columns(4)
    with c5: draw_card("VOL. GLOBAL", "ALTO", 75)
    with c6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with c7: draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
    with c8: draw_card("SISTEMA", "JARVIS v62.0", 100)
    
    st.markdown("<h3 style='color:white; margin-top:30px;'>📋 ANÁLISE COMPLETA DO DIA</h3>", unsafe_allow_html=True)
    if df_diario is not None: 
        st.dataframe(df_diario, use_container_width=True)
    else:
        st.error("DATABASE NÃO LOCALIZADO")

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: t_casa = st.text_input("🏠 TIME DA CASA", "Botafogo")
    with c2: t_fora = st.text_input("🚀 TIME DE FORA", "Palmeiras")
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        st.session_state.analise_bloqueada = {"casa": t_casa, "fora": t_fora, "conf": 88.5}
    if st.session_state.analise_bloqueada:
        a = st.session_state.analise_bloqueada
        st.markdown(f'<div class="banner-green">🟢 JARVIS: ANÁLISE CONCLUÍDA PARA {a["casa"]}</div>', unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("PROBABILIDADE", f"{a['conf']}%", int(a['conf']))
        with r2: draw_card("GOLS", "OVER 1.5", 90)
        with r3: draw_card("STAKE SUGERIDA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
        with r4: draw_card("TENDÊNCIA", "BACK", 82)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total))
    st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, float(st.session_state.stake_padrao))

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    for c in reversed(st.session_state.historico_calls):
        st.markdown(f"<div style='background:#1a202c; padding:15px; border-radius:6px; margin-bottom:10px; border-left:4px solid #6d28d9; color:white;'>[{c['data']}] {c['casa']} x {c['fora']}</div>", unsafe_allow_html=True)

# FOOTER ESTATUTÁRIO
st.markdown("""
    <div class="footer-shield">
        <div>STATUS: ● IA OPERACIONAL | v62.0</div>
        <div>JARVIS PROTECT SYSTEM</div>
    </div>
""", unsafe_allow_html=True)
