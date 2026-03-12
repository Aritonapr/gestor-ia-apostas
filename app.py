import streamlit as st

# ==========================================
# PROTOCOLO GIAE-PRIME-V9: NÚCLEO DE ESTABILIDADE
# ==========================================

st.set_page_config(page_title="GESTOR IA - PRIME V9", layout="wide", initial_sidebar_state="expanded")

# Injeção de CSS de Alta Prioridade (Force Dark Mode)
st.markdown("""
    <style>
        /* 1. Reset Total do Fundo do Streamlit */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stMainBlockContainer"] {
            background-color: #0a0a0a !important;
            color: #e0e0e0 !important;
        }

        /* 2. Remoção de Linhas e Bordas do Tema Padrão */
        footer {visibility: hidden;}
        header {background-color: rgba(0,0,0,0) !important;}

        /* 3. Sidebar Profissional - 260px */
        [data-testid="stSidebar"] {
            width: 260px !important;
            min-width: 260px !important;
            background-color: #000000 !important;
            border-right: 1px solid #f64d23 !important;
        }

        /* 4. Ajuste de Margem Superior (-35px) */
        [data-testid="stMainBlockContainer"] {
            padding-top: 0rem !important;
            margin-top: -35px !important;
        }

        /* 5. Estilização dos Botões Gêmeos Laranja #f64d23 */
        div.stButton > button {
            width: 100% !important;
            height: 50px !important;
            background-color: #f64d23 !important;
            color: white !important;
            border-radius: 50px !important;
            border: none !important;
            font-weight: 800 !important;
            text-transform: uppercase !important;
            box-shadow: 0 0 15px rgba(246, 77, 35, 0.3) !important;
            transition: all 0.3s ease !important;
        }

        div.stButton > button:hover {
            box-shadow: 0 0 25px rgba(246, 77, 35, 0.7) !important;
            transform: scale(1.02) !important;
        }

        /* 6. Card de Análise Métrica */
        .card-analise {
            background-color: #151515 !important;
            border: 1px solid #f64d23 !important;
            padding: 25px !important;
            border-radius: 12px !important;
            margin-bottom: 25px !important;
        }

        .titulo-card {
            color: #f64d23 !important;
            font-size: 22px !important;
            font-weight: bold !important;
            border-left: 5px solid #f64d23 !important;
            padding-left: 15px !important;
            margin-bottom: 10px !important;
        }

        /* 7. Ajuste dos Métricas (Labels e Valores) */
        [data-testid="stMetric"] {
            background-color: #1a1a1a !important;
            padding: 15px !important;
            border-radius: 10px !important;
            border: 1px solid #333 !important;
        }
        
        [data-testid="stMetricValue"] {
            color: #ffffff !important;
        }

        [data-testid="stMetricLabel"] {
            color: #888888 !important;
        }

    </style>
""", unsafe_allow_html=True)

# ==========================================
# INTERFACE SIDEBAR
# ==========================================

with st.sidebar:
    st.markdown("<h2 style='color:#f64d23;'>JARVIS GIAE</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#555; font-size:12px;'>PROTOCOL PRIME V9</p>", unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("### 🏟️ LIGAS INDEXADAS")
    st.markdown("""
    <div style='font-size:14px; color:#bbb; line-height:2;'>
    • Brasileirão A, B, C, D<br>
    • Estaduais (SP, RJ, MG, RS)<br>
    • Copa do Brasil<br>
    • Big 5 Europa
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("SINCRONIZAR BANCO"):
        st.toast("Sincronizando Banco de Dados...")

# ==========================================
# CONTEÚDO PRINCIPAL
# ==========================================

# Botões Gêmeos Laranja (Layout Superior)
col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    st.button("ANÁLISE ATIVA")
with col_btn2:
    st.button("RELATÓRIO DE RISCO")

# Card Central de Análise
st.markdown("""
    <div class="card-analise">
        <div class="titulo-card">ANÁLISE MÉTRICA DOS JOGOS: COPA DO BRASIL</div>
        <p style="color: #888; margin-left: 20px;">CONFRONTO: <b>FLAMENGO vs AMAZONAS</b></p>
    </div>
""", unsafe_allow_html=True)

# Grid de Métricas Customizadas
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(label="VITÓRIA MANDANTE", value="82%", delta="Fator Casa")
with m2:
    st.metric(label="OVER 2.5 GOLS", value="64%", delta="Tendência")
with m3:
    st.metric(label="CANTOS (MÉDIA)", value="10.5", delta="Alta")
with m4:
    st.metric(label="AMBAS MARCAM", value="38%", delta="Baixa", delta_color="inverse")

st.markdown("<br><br>", unsafe_allow_html=True)
st.success("Protocolo Estabilizado. Interface Dark Mode Ativa.")
