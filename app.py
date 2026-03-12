import streamlit as st

# ==========================================
# PROTOCOLO GIAE-PRIME-V9: NÚCLEO ESTÁVEL
# ==========================================

st.set_page_config(
    page_title="GESTOR IA - PRIME V9",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Injeção de CSS de Alta Performance (Resolução de Conflitos)
st.markdown("""
    <style>
        /* 1. Reset de Cores e Fundo Profundo */
        [data-testid="stAppViewContainer"] {
            background-color: #0a0a0a !important;
            background-image: radial-gradient(circle at 2px 2px, rgba(246, 77, 35, 0.05) 1px, transparent 0);
            background-size: 40px 40px;
        }
        
        [data-testid="stHeader"] {
            background: rgba(0,0,0,0) !important;
        }

        /* 2. Sidebar Profissional - 260px */
        [data-testid="stSidebar"] {
            width: 260px !important;
            background-color: #000000 !important;
            border-right: 2px solid #f64d23 !important;
        }

        /* 3. Correção de Margem Superior (-35px) */
        .main .block-container {
            padding-top: 1rem !important;
            margin-top: -35px !important;
        }

        /* 4. BOTÕES GÊMEOS CÁPSULA #f64d23 COM LASER SCAN */
        div.stButton > button {
            width: 100% !important;
            height: 50px !important;
            background: #f64d23 !important;
            color: #ffffff !important;
            border-radius: 50px !important;
            border: none !important;
            font-weight: 800 !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
            box-shadow: 0 0 15px rgba(246, 77, 35, 0.4) !important;
            position: relative !important;
            overflow: hidden !important;
            transition: all 0.3s ease-in-out !important;
        }

        /* Efeito Laser Scan Simulation */
        div.stButton > button:hover {
            box-shadow: 0 0 30px rgba(246, 77, 35, 0.8) !important;
            transform: translateY(-2px) !important;
        }

        div.stButton > button::after {
            content: "";
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: 0.5s;
        }

        div.stButton > button:active::after {
            left: 100%;
            transition: 0.5s;
        }

        /* 5. Card de Análise Métrica */
        .card-giae {
            background: #141414 !important;
            border: 1px solid #f64d23 !important;
            border-radius: 15px !important;
            padding: 30px !important;
            margin-top: 20px !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important;
        }

        .titulo-giae {
            color: #f64d23 !important;
            font-family: 'Courier New', monospace !important;
            font-size: 24px !important;
            font-weight: bold !important;
            border-left: 6px solid #f64d23 !important;
            padding-left: 20px !important;
            margin-bottom: 20px !important;
        }

        /* 6. Ajuste de Texto e Métricas */
        [data-testid="stMetricValue"] {
            color: #ffffff !important;
            font-size: 32px !important;
        }
        
        [data-testid="stMetricLabel"] {
            color: #f64d23 !important;
            font-weight: bold !important;
        }

        p, span, label {
            color: #e0e0e0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# INTERFACE SIDEBAR (JARVIS)
# ==========================================

with st.sidebar:
    st.markdown("<h1 style='color:#f64d23; margin-bottom:0;'>JARVIS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#555; margin-top:0;'>SISTEMA GIAE-PRIME V9</p>", unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("### 🏟️ LIGAS EM MEMÓRIA")
    st.markdown("""
    - **BRASIL:** SÉRIES A-D / ESTADUAIS
    - **COPA:** COPA DO BRASIL
    - **EUROPA:** ELITE EUROPEIA
    """)
    
    st.write("")
    st.write("")
    if st.button("SINCRONIZAR BANCO"):
        st.toast("Acessando Banco de Dados...", icon="🚀")

# ==========================================
# CONTEÚDO PRINCIPAL (COMANDO DO COMANDANTE)
# ==========================================

# ÁREA DOS BOTÕES GÊMEOS (Layout Superior)
col_btn_1, col_btn_2 = st.columns(2)

with col_btn_1:
    st.button("🎯 ANÁLISE ATIVA")

with col_btn_2:
    st.button("📊 RELATÓRIO DE RISCO")

# CARD DE ANÁLISE MÉTRICA
st.markdown("""
    <div class="card-giae">
        <div class="titulo-giae">ANÁLISE MÉTRICA DOS JOGOS: COPA DO BRASIL</div>
        <div style="color: #888; margin-bottom: 20px;">
            Sincronizando dados de confronto: <b style="color:#fff;">FLAMENGO vs AMAZONAS</b>
        </div>
    </div>
""", unsafe_allow_html=True)

# GRID DE DADOS EM TEMPO REAL
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("VITÓRIA MANDANTE", "82%", "DOMÍNIO")
with m2:
    st.metric("OVER 2.5 GOLS", "64%", "TENDÊNCIA")
with m3:
    st.metric("CANTOS (MÉDIA)", "10.5", "ALTA")
with m4:
    st.metric("AMBAS MARCAM", "38%", "-BAIXA", delta_color="inverse")

st.write("---")
st.info("Status do Sistema: Operacional. Aguardando diretrizes do Comandante.")
