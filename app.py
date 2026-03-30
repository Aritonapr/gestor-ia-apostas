import streamlit as st
import pandas as pd
import os

# ==============================================================================
# [PROTOCOLO JARVIS v64.0 - RESSURREIÇÃO TOTAL]
# DIRETRIZ: ABERTURA FORÇADA E DESIGN ZERO WHITE PRO
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA (A PRIMEIRA LINHA SEMPRE)
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide")

# 2. INICIALIZAÇÃO DE MEMÓRIA (MÉTODO À PROVA DE BALAS)
if 'aba_ativa' not in st.session_state: st.session_state['aba_ativa'] = "home"
if 'banca_total' not in st.session_state: st.session_state['banca_total'] = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state['stake_padrao'] = 1.0

# 3. CARREGAMENTO DE DADOS (SEGURO)
def carregar_dados():
    caminho = "data/database_diario.csv"
    if os.path.exists(caminho):
        try:
            return pd.read_csv(caminho)
        except:
            return None
    return None

df_diario = carregar_dados()

# 4. DESIGN CSS (ZERO WHITE PRO - INJETADO DE FORMA SEGURA)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    /* RESET DE CORES */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
        color: white !important;
    }

    /* ESCONDER ELEMENTOS NATIVOS */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    
    /* SIDEBAR */
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        border-right: 1px solid #1e293b !important; 
    }

    /* BOTÕES DA SIDEBAR */
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { 
        background-color: #1e293b !important; color: #06b6d4 !important; 
    }

    /* CARDS DE DESTAQUE */
    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; margin-bottom: 15px; 
    }

    /* FOOTER */
    .footer-shield { 
        position: fixed; bottom: 0; left: 0; width: 100%; 
        background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; 
        display: flex; justify-content: space-between; align-items: center; 
        padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; 
    }
    </style>
""", unsafe_allow_html=True)

# 5. SIDEBAR (MENU DE NAVEGAÇÃO)
with st.sidebar:
    st.markdown("<h2 style='color:#9d54ff; text-align:center; font-weight:900;'>GESTOR IA</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#475569; font-size:10px; text-align:center;'>SINCRONIA TEMPORAL v64.0</p>", unsafe_allow_html=True)
    st.write("---")
    
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"

# 6. FUNÇÃO DE DESENHAR CARDS
def desenhar_card(titulo, valor, progresso):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase;">{titulo}</div>
            <div style="color:white; font-size:18px; font-weight:900; margin-top:10px;">{valor}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;">
                <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); height:100%; width:{progresso}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# 7. EXIBIÇÃO DAS TELAS
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO - 2026</h2>", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: desenhar_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with c2: desenhar_card("ASSERTIVIDADE", "92.4%", 92)
    with c3: desenhar_card("STATUS", "IA ONLINE", 100)
    with c4: desenhar_card("SISTEMA", "JARVIS v64.0", 100)
    
    if df_diario is not None:
        st.markdown("### 📋 JOGOS DO DIA (2026)")
        st.dataframe(df_diario, use_container_width=True, hide_index=True)
    else:
        st.info("🤖 Jarvis: O banco de dados está sendo gerado. Por favor, certifique-se de rodar a Action no GitHub.")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total))
    st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, float(st.session_state.stake_padrao))
