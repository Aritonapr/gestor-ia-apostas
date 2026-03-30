import streamlit as st
import pandas as pd
import time
from datetime import datetime

# 1. ESTADO DE NAVEGAÇÃO (Inicia no Scanner como a Imagem 2)
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = "SCANNER EM TEMPO REAL"

# Configuração da Página (Layout Largo e Sidebar visível como Imagem 2)
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# 2. ESTÉTICA IMUTÁVEL: CSS DA IMAGEM 2 (ZERO WHITE)
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #0b0e11; color: white; }
    [data-testid="stSidebar"] { background-color: #0b0e11; border-right: 1px solid #1e2329; }
    header {visibility: hidden;}
    .main .block-container {padding-top: 1rem;}
    ::-webkit-scrollbar {display: none;}
    
    /* Logo e Header Estilo Imagem 2 */
    .logo-container { padding: 10px 0px; margin-bottom: 20px; border-bottom: 1px solid #1e2329; }
    .logo-text { color: #6a11cb; font-weight: bold; font-size: 24px; letter-spacing: 1px; }

    /* Cards KPI - Estilo Exato da Imagem 2 */
    .kpi-card {
        background-color: #161a1e;
        border-radius: 4px;
        padding: 20px;
        text-align: center;
        border: 1px solid #1e2329;
        height: 150px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .kpi-title { color: #5d6670; font-size: 10px; text-transform: uppercase; margin-bottom: 15px; }
    .kpi-value { color: white; font-size: 22px; font-weight: bold; margin-bottom: 10px; }
    .kpi-bar { height: 4px; background: linear-gradient(90deg, #6a11cb, #2575fc); border-radius: 2px; width: 80%; margin: 0 auto; }
    
    /* Botões da Sidebar */
    .stButton>button {
        background-color: transparent; color: #aeb4bc; border: none; 
        text-align: left; width: 100%; padding: 10px 0; font-size: 14px;
    }
    .stButton>button:hover { color: #ff7900; background-color: #1e2329; }
    </style>
""", unsafe_allow_html=True)

# 3. BARRA LATERAL - MENU DA IMAGEM 2
with st.sidebar:
    st.markdown('<div class="logo-text">GESTOR IA</div>', unsafe_allow_html=True)
    st.write("")
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.pagina_ativa = "SCANNER PRÉ-LIVE"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.pagina_ativa = "SCANNER EM TEMPO REAL"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.pagina_ativa = "GESTÃO DE BANCA"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.pagina_ativa = "HISTÓRICO DE CALLS"
    if st.button("🎫 BILHETE OURO"): st.session_state.pagina_ativa = "BILHETE OURO"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.pagina_ativa = "VENCEDORES"
    
    st.v_spacer(height=100)
    st.caption(f"STATUS: ● IA OPERACIONAL | v63.0")

# 4. CARREGAMENTO DE DADOS (DATABASE DA IMAGEM 1)
@st.cache_data(ttl=60)
def carregar_brain():
    try:
        URL = f"https://raw.githubusercontent.com/Aritionapr/gestor-ia-apostas/main/data/database_diario.csv?v={time.time()}"
        df = pd.read_csv(URL)
        return df
    except:
        return pd.DataFrame()

df_brain = carregar_brain()

# 5. LÓGICA DE TELAS
if st.session_state.pagina_ativa == "BILHETE OURO":
    st.markdown("### 🎫 BILHETE OURO")
    
    # Pegando dados da Imagem 1 para os cards da Imagem 2
    banca = "R$ 1.250,00" # Dado da Imagem 1
    assertividade = "87.2%" # Dado da Imagem 1
    sugestao = "OVER 1.5"   # Dado da Imagem 1
    odds = "1.85"           # Dado da Imagem 1
    
    # Linha 1 de Cards (Estilo Imagem 2)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown(f'<div class="kpi-card"><div class="kpi-title">BANCA ATUAL</div><div class="kpi-value">{banca}</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="kpi-card"><div class="kpi-title">ASSERTIVIDADE</div><div class="kpi-value">{assertividade}</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)
    with c3: st.markdown(f'<div class="kpi-card"><div class="kpi-title">SUGESTÃO</div><div class="kpi-value">{sugestao}</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)
    with c4: st.markdown(f'<div class="kpi-card"><div class="kpi-title">IA STATUS</div><div class="kpi-value">ONLINE</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)

    # Linha 2 de Cards (Estilo Imagem 2)
    c5, c6, c7, c8 = st.columns(4)
    with c5: st.markdown(f'<div class="kpi-card"><div class="kpi-title">VOL. GLOBAL</div><div class="kpi-value">ALTO</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)
    with c6: st.markdown(f'<div class="kpi-card"><div class="kpi-title">MÉDIA ODDS</div><div class="kpi-value">{odds}</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)
    with c7: st.markdown(f'<div class="kpi-card"><div class="kpi-title">STAKE PADRÃO</div><div class="kpi-value">1.0%</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)
    with c8: st.markdown(f'<div class="kpi-card"><div class="kpi-title">SISTEMA</div><div class="kpi-value">JARVIS v63.0</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📋 ANÁLISE COMPLETA DO DIA")
    st.info("O Bilhete Ouro é gerado cruzando o Scanner Live com o histórico de 5 temporadas.")

else:
    # TELA PADRÃO: SCANNER EM TEMPO REAL (Conforme Imagem 2)
    st.markdown(f"### 📡 SCANNER EM TEMPO REAL - {datetime.now().strftime('%d/%m/%Y')}")
    if not df_brain.empty:
        st.dataframe(df_brain, use_container_width=True, hide_index=True)
    else:
        st.warning("Aguardando sincronia do servidor...")
