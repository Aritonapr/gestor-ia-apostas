import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# 1. CONFIGURAÇÃO E IDENTIDADE VISUAL
# ==========================================
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS para manter a aparência profissional e simetria dos menus
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    [data-testid="stSidebar"] {
        min-width: 320px !important;
        max-width: 320px !important;
        background-color: #11151a !important;
    }
    .nav-title { color: #8e44ad; font-weight: bold; font-size: 26px; }
    
    /* Botões do Menu Lateral */
    .stButton > button {
        width: 100%;
        background-color: #1e2530;
        color: white;
        border: 1px solid #2d343f;
        text-align: left;
        padding-left: 15px;
    }

    /* Estilo dos 8 KPI Cards na Assertividade */
    div[data-testid="stMetric"] {
        background-color: #1e2530;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #2d343f;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SISTEMA DE ESTADO (SESSION STATE)
# ==========================================
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "Apostas Esportivas"

# Dados da Assertividade IA (8 KPIs)
if 'metrics_ia' not in st.session_state:
    st.session_state.metrics_ia = {
        'assertividade_geral': 85.5,
        'gols_over': 78.2,
        'cantos_over': 82.1,
        'win_rate': 65.4,
        'roi': 12.5,
        'lucro_mensal': 1250.00,
        'total_calls': 450,
        'erros_ia': 14.5
    }

# ==========================================
# 3. CABEÇALHO (BARRA SUPERIOR)
# ==========================================
header_l, header_m, header_r = st.columns([1.5, 6, 2.5])

with header_l:
    st.markdown('<span class="nav-title">GESTOR IA</span>', unsafe_allow_html=True)

with header_m:
    # Menu Superior de Navegação
    m_cols = st.columns(6)
    with m_cols[0]:
        if st.button("📊 ESPORTIVAS"): st.session_state.aba_ativa = "Apostas Esportivas"
    with m_cols[1]:
        if st.button("📡 AO VIVO"): st.session_state.aba_ativa = "Apostas Ao Vivo"
    with m_cols[2]:
        if st.button("🔍 ENCONTRADAS"): st.session_state.aba_ativa = "Apostas Encontradas"
    with m_cols[3]:
        if st.button("📈 ESTATÍSTICAS"): st.session_state.aba_ativa = "Estatísticas"
    with m_cols[4]:
        if st.button("⚖️ MERCADO"): st.session_state.aba_ativa = "Mercado"
    with m_cols[5]:
        if st.button("🎯 ASSERTIVIDADE"): st.session_state.aba_ativa = "assertividade"

with header_r:
    r_col1, r_col2, r_col3 = st.columns([1, 1, 0.5])
    with r_col1: st.button("REGISTRAR")
    with r_col2: st.button("ENTRAR")
    with r_col3: st.markdown("🔍")

# ==========================================
# 4. MENU LATERAL (SIDEBAR)
# ==========================================
with st.sidebar:
    st.markdown("### MENU PRINCIPAL")
    
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "scanner_pre"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "scanner_realtime"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao_banca"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "bilhete_ouro"
    if st.button("🏆 VENCEDORES"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

# ==========================================
# 5. ÁREA DE CONTEÚDO (MÓDULOS)
# ==========================================

# MÓDULO: ASSERTIVIDADE IA (REQUISITO DOS 8 CARDS)
if st.session_state.aba_ativa == "assertividade":
    st.header("🎯 ASSERTIVIDADE & IA")
    m = st.session_state.metrics_ia
    
    # Linha superior de métricas
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Assertividade Geral", f"{m['assertividade_geral']}%")
    c2.metric("Gols Over", f"{m['gols_over']}%")
    c3.metric("Cantos Over", f"{m['cantos_over']}%")
    c4.metric("Win Rate", f"{m['win_rate']}%")
    
    # Linha inferior de métricas
    c5, c6, c7, c8 = st.columns(4)
    c5.metric("ROI", f"{m['roi']}%")
    c6.metric("Lucro Mensal", f"R$ {m['lucro_mensal']:.2f}")
    c7.metric("Total de Calls", m['total_calls'])
    c8.metric("Erros de IA", f"{m['erros_ia']}%")

# MÓDULO: GESTÃO DE BANCA
elif st.session_state.aba_ativa == "gestao_banca":
    st.header("💰 GESTÃO DE BANCA")
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        st.number_input("Saldo Inicial", value=1000.0)
    with col_b2:
        st.number_input("Valor da Stake", value=10.0)

# MÓDULO: SCANNER PRÉ-LIVE (CORREÇÃO DE ERRO DE SINTAXE)
elif st.session_state.aba_ativa == "scanner_pre":
    st.header("🎯 SCANNER PRÉ-LIVE")
    # Garantindo que o dicionário de ligas esteja fechado corretamente
    ligas_monitoradas = {
        "Série A": "Ativo",
        "Premier": "Ativo",
        "La Liga": "Ativo"
    }
    st.write("Monitoramento em tempo real:", ligas_monitoradas)

# OUTRAS SEÇÕES (RESERVADO PARA V59.00)
else:
    st.header(f"Seção: {st.session_state.aba_ativa}")
    st.info("Funcionalidade sendo integrada pela IA para a versão 59.00.")

# ==========================================
# 6. RODAPÉ TÉCNICO
# ==========================================
st.markdown("---")
st.caption(f"STATUS: ● IA OPERACIONAL | v59.00 | {datetime.now().strftime('%d/%m/%Y %H:%M')}")
