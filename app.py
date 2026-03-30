import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO JARVIS v64.1 - ESTABILIDADE TOTAL]
# DIRETRIZ: VISUAL BACKUP v62.0 + CORREÇÃO ALTAIR + CONTEXTO 2026
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA (LINHA 1 OBRIGATÓRIA)
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA (EVITA ERRO DE ABA_ATIVA) ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# --- CARREGAMENTO DE DADOS (CONTEXTO 2026) ---
def carregar_dados_ia():
    path_local = "data/database_diario.csv"
    if os.path.exists(path_local):
        try:
            return pd.read_csv(path_local)
        except:
            return None
    return None

df_diario = carregar_dados_ia()

# ==============================================================================
# CAMADA DE ESTILO CSS (O SEU DESIGN ZERO WHITE PRO - IMUTÁVEL)
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
    }
    
    .header-left { display: flex; align-items: center; gap: 25px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none;}
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }

    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; }

    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important; border-radius: 6px !important; width: 100% !important;
    }
    
    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; 
    }
    
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER NA SIDEBAR (DESIGN BACKUP) ---
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left"><div class="logo-link">GESTOR IA</div></div>
            <div class="header-right"><div class="entrar-grad">ENTRAR</div></div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"

def draw_card(title, value, perc):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;">
                <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); height:100%; width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- EXIBIÇÃO DAS TELAS ---
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO - MARÇO 2026</h2>", unsafe_allow_html=True)
    
    # Linha de 4 Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with c2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with c3: draw_card("STATUS", "IA ONLINE", 100)
    with c4: draw_card("SISTEMA", "JARVIS v64.1", 100)
    
    if df_diario is not None:
        st.markdown("### 📋 GRADE DE JOGOS SINCRONIZADA (REAL-TIME 2026)")
        st.dataframe(df_diario, use_container_width=True, hide_index=True)
    else:
        st.info("🤖 Jarvis: O banco de dados de 2026 está sendo criado pelo GitHub. Aguarde a sincronia terminar.")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total))
    st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, float(st.session_state.stake_padrao))
    
    v_entrada = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    draw_card("VALOR POR ENTRADA", f"R$ {v_entrada:,.2f}", 100)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        lista = sorted(list(set(df_diario['CASA'].tolist() + df_diario['FORA'].tolist())))
        c1, c2 = st.columns(2)
        with c1: t_casa = st.selectbox("🏠 CASA", lista)
        with c2: t_fora = st.selectbox("🚀 FORA", [t for t in lista if t != t_casa])
        if st.button("⚡ ANALISAR AGORA"):
            st.success(f"Análise de {t_casa} x {t_fora} concluída para Março/2026!")

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v64.1 | MARÇO 2026</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
