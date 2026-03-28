import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# CONFIGURAÇÃO E DESIGN DO PAINEL
# ==========================================
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS para garantir a simetria e visibilidade
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    [data-testid="stSidebar"] {
        min-width: 320px !important;
        max-width: 320px !important;
        background-color: #11151a !important;
    }
    .nav-title { color: #8e44ad; font-weight: bold; font-size: 26px; }
    
    /* Ajuste para botões superiores não cortarem o texto */
    .stButton > button {
        width: 100%;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        background-color: #1e2530;
        color: white;
        border: 1px solid #2d343f;
    }
    
    /* Estilo dos 8 KPI Cards */
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
# MEMÓRIA DO SISTEMA (ESTADO)
# ==========================================
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "Apostas Esportivas"

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
# BARRA SUPERIOR (HEADER)
# ==========================================
header_col1, header_col2, header_col3 = st.columns([1.5, 6, 2.5])

with header_col1:
    st.markdown('<span class="nav-title">GESTOR IA</span>', unsafe_allow_html=True)

with header_col2:
    # Navegação Horizontal
    h_cols = st.columns(6)
    with h_cols[0]:
        if st.button("📊 ESPORTIVAS"): st.session_state.aba_ativa = "Apostas Esportivas"
    with h_cols[1]:
        if st.button("📡 AO VIVO"): st.session_state.aba_ativa = "Apostas Ao Vivo"
    with h_cols[2]:
        if st.button("🔍 ENCONTRADAS"): st.session_state.aba_ativa = "Apostas Encontradas"
    with h_cols[3]:
        if st.button("📈 ESTATÍSTICAS"): st.session_state.aba_ativa = "Estatísticas"
    with h_cols[4]:
        if st.button("⚖️ MERCADO"): st.session_state.aba_ativa = "Mercado"
    with h_cols[5]:
        if st.button("🎯 ASSERTIVIDADE"): st.session_state.aba_ativa = "assertividade"

with header_col3:
    btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 0.5])
    with btn_col1: st.button("REGISTRAR")
    with btn_col2: st.button("ENTRAR")
    with btn_col3: st.markdown("🔍")

# ==========================================
# MENU LATERAL (SIDEBAR)
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
# CONTEÚDO DAS SEÇÕES
# ==========================================

# 1. ASSERTIVIDADE IA (COM 8 KPI CARDS)
if st.session_state.aba_ativa == "assertividade":
    st.header("🎯 ASSERTIVIDADE & IA")
    m = st.session_state.metrics_ia
    
    # Primeira Linha - 4 Cards
    row1_c1, row1_c2, row1_c3, row1_c4 = st.columns(4)
    row1_c1.metric("Assertividade Geral", f"{m['assertividade_geral']}%")
    row1_c2.metric("Gols Over", f"{m['gols_over']}%")
    row1_c3.metric("Cantos Over", f"{m['cantos_over']}%")
    row1_c4.metric("Win Rate", f"{m['win_rate']}%")
    
    # Segunda Linha - 4 Cards
    row2_c1, row2_c2, row2_c3, row2_c4 = st.columns(4)
    row2_c1.metric("ROI", f"{m['roi']}%")
    row2_c2.metric("Lucro Mensal", f"R$ {m['lucro_mensal']:.2f}")
    row2_c3.metric("Total de Calls", m['total_calls'])
    row2_c4.metric("Erros de IA", f"{m['erros_ia']}%")

# 2. GESTÃO DE BANCA
elif st.session_state.aba_ativa == "gestao_banca":
    st.header("💰 GESTÃO DE BANCA")
    c1, c2 = st.columns(2)
    with c1:
        st.number_input("Saldo da Banca", value=1000.0)
    with c2:
        st.number_input("Stake Recomendada", value=10.0)

# 3. SCANNER PRÉ-LIVE (CORREÇÃO DE SINTAXE)
elif st.session_state.aba_ativa == "scanner_pre":
    st.header("🎯 SCANNER PRÉ-LIVE")
    # Correção do erro SyntaxError: '{' was never closed
    db_ligas = {
        "Liga": "Brasileirão",
        "Jogos": 10,
        "Status": "Ativo"
    }
    st.write("Dados de Monitoramento:", db_ligas)

# 4. HISTÓRICO
elif st.session_state.aba_ativa == "historico":
    st.header("📜 HISTÓRICO DE CALLS")
    st.info("[19:51] Athletico-PR x Atlético-MG | R$ 10.00 | Pendente")

# 5. BILHETE OURO
elif st.session_state.aba_ativa == "bilhete_ouro":
    st.header("📅 BILHETE OURO - TOP 20 IA")
    st.success("Bilhete gerado com sucesso para os jogos de hoje.")

else:
    st.header(f"Seção: {st.session_state.aba_ativa}")
    st.info("Funcionalidade em processamento para a v59.00.")

# ==========================================
# RODAPÉ
# ==========================================
st.markdown("---")
st.caption(f"STATUS: ● IA OPERACIONAL | v59.00 | {datetime.now().strftime('%d/%m/%Y %H:%M')}")
