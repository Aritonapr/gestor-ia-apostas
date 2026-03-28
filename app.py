import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# CONFIGURAÇÃO E ESTILO (DESIGN DO PAINEL)
# ==========================================
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização para garantir que os menus e botões fiquem alinhados
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    [data-testid="stSidebar"] {
        min-width: 320px !important;
        max-width: 320px !important;
        background-color: #11151a !important;
    }
    /* Estilo dos KPI Cards para Assertividade */
    .kpi-card {
        background-color: #1e2530;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #2d343f;
        text-align: center;
    }
    /* Títulos e Nav */
    .nav-title { color: #8e44ad; font-weight: bold; font-size: 26px; }
    
    /* Ajuste para botões não cortarem o texto */
    .stButton > button {
        width: 100%;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# GESTÃO DE ESTADO (MEMÓRIA DO APP)
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
# Corrigindo o layout que apareceu "quebrado" na imagem 10
header_1, header_2, header_3 = st.columns([1.5, 5, 2])

with header_1:
    st.markdown('<span class="nav-title">GESTOR IA</span>', unsafe_allow_html=True)

with header_2:
    # Botões Horizontais Superiores
    h_col1, h_col2, h_col3, h_col4, h_col5, h_col6 = st.columns(6)
    with h_col1:
        if st.button("📊 ESPORTIVAS"): st.session_state.aba_ativa = "Apostas Esportivas"
    with h_col2:
        if st.button("📡 AO VIVO"): st.session_state.aba_ativa = "Apostas Ao Vivo"
    with h_col3:
        if st.button("🔍 ENCONTRADAS"): st.session_state.aba_ativa = "Apostas Encontradas"
    with h_col4:
        if st.button("📈 ESTATÍSTICAS"): st.session_state.aba_ativa = "Estatísticas"
    with h_col5:
        if st.button("⚖️ MERCADO"): st.session_state.aba_ativa = "Mercado"
    with h_col6:
        if st.button("🎯 ASSERTIVIDADE"): st.session_state.aba_ativa = "assertividade"

with header_3:
    act_col1, act_col2, act_col3 = st.columns([1, 1, 0.5])
    with act_col1: st.button("REGISTRAR")
    with act_col2: st.button("ENTRAR")
    with act_col3: st.markdown("🔍")

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
# ÁREA DE CONTEÚDO DINÂMICO
# ==========================================

# 1. ABA DE ASSERTIVIDADE (COM OS 8 KPI CARDS)
if st.session_state.aba_ativa == "assertividade":
    st.header("📊 ASSERTIVIDADE & IA")
    m = st.session_state.metrics_ia
    
    # Linha 1 de KPIs
    kpi_r1_1, kpi_r1_2, kpi_r1_3, kpi_r1_4 = st.columns(4)
    kpi_r1_1.metric("Assertividade Geral", f"{m['assertividade_geral']}%")
    kpi_r1_2.metric("Gols Over", f"{m['gols_over']}%")
    kpi_r1_3.metric("Cantos Over", f"{m['cantos_over']}%")
    kpi_r1_4.metric("Win Rate", f"{m['win_rate']}%")
    
    # Linha 2 de KPIs
    kpi_r2_1, kpi_r2_2, kpi_r2_3, kpi_r2_4 = st.columns(4)
    kpi_r2_1.metric("ROI", f"{m['roi']}%")
    kpi_r2_2.metric("Lucro Mensal", f"R$ {m['lucro_mensal']:.2f}")
    kpi_r2_3.metric("Total de Calls", m['total_calls'])
    kpi_r2_4.metric("Erros de IA", f"{m['erros_ia']}%")

# 2. GESTÃO DE BANCA
elif st.session_state.aba_ativa == "gestao_banca":
    st.header("💰 GESTÃO DE BANCA")
    col_gb1, col_gb2 = st.columns(2)
    with col_gb1:
        st.number_input("Saldo Atual da Banca", value=1000.0)
    with col_gb2:
        st.number_input("Unidade (Stake)", value=10.0)

# 3. SCANNER PRÉ-LIVE (CORREÇÃO DA SINTAXE)
elif st.session_state.aba_ativa == "scanner_pre":
    st.header("🎯 SCANNER PRÉ-LIVE")
    # Corrigindo o erro de dicionário não fechado da imagem 7
    db_ligas = {
        "Brasileirão Série A": "Ativo",
        "Premier League": "Ativo",
        "Bundesliga": "Ativo"
    }
    st.write("Monitorando ligas principais...", db_ligas)

# 4. HISTÓRICO DE CALLS
elif st.session_state.aba_ativa == "historico":
    st.header("📜 HISTÓRICO DE CALLS")
    st.success("[19:51] Athletico-PR x Atlético-MG | R$ 10.00 | REVISAR")

else:
    st.header(f"Seção: {st.session_state.aba_ativa}")
    st.info("Esta funcionalidade está sendo processada pela IA para a v59.00.")

# ==========================================
# RODAPÉ (FOOTER)
# ==========================================
st.markdown("---")
st.caption(f"STATUS: ● IA OPERACIONAL | v59.00 | {datetime.now().strftime('%d/%m/%Y %H:%M')}")
