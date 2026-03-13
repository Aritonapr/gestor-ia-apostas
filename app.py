import streamlit as st
import time

# ==============================================================================
# [SISTEMA DE SEGURANÇA GIAE-V17-ELITE-RECOVERY ACTIVATED]
# ESTADO: PRESERVAÇÃO DE ESTRUTURA TOTAL (PROTOCOLO ANTI-PERDA)
# DATA DE BACKUP: 13/03/2024 (Conforme sua imagem)
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- BLINDAGEM CSS (NÃO ALTERAR ESTE BLOCO PARA MANTER A ESTRUTURA DA IMAGEM) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* Reset Geral */
    .stApp { background-color: #0b0e11 !important; color: white !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { visibility: hidden !important; display: none !important; }

    /* NAVBAR SUPERIOR - EXATAMENTE COMO NA IMAGEM */
    .nav-bar {
        position: fixed; top: 0; left: 0; width: 100%; height: 60px;
        background-color: #000000 !important;
        display: flex; align-items: center; justify-content: space-between;
        padding: 0 30px; border-bottom: 1px solid #1e293b; z-index: 9999;
    }
    .logo { font-weight: 900; font-size: 22px; color: white; letter-spacing: -1px; }
    .nav-links { display: flex; gap: 20px; font-size: 10px; text-transform: uppercase; color: #cbd5e1; }
    .auth-buttons { display: flex; gap: 10px; }
    .btn-reg { border: 1px solid #334155; padding: 6px 15px; border-radius: 4px; font-size: 11px; font-weight: 700; cursor: pointer; }
    .btn-ent { background: #00cc66; color: white; padding: 6px 20px; border-radius: 4px; font-size: 11px; font-weight: 800; cursor: pointer; }

    /* SIDEBAR - ESTILO LISTA (FUNDO ESCURO) */
    [data-testid="stSidebar"] { background-color: #0b0e11 !important; border-right: 1px solid #1e293b !important; min-width: 250px !important; }
    [data-testid="stSidebarNav"] { display: none !important; } /* Esconde o nav padrão */
    
    .side-btn {
        width: 100%; padding: 15px 20px; background: transparent;
        border: none; border-bottom: 1px solid #1a202c;
        color: #94a3b8; text-align: left; font-size: 11px;
        text-transform: uppercase; cursor: pointer; transition: 0.3s;
    }
    .side-btn:hover { color: white; background: #1a202c; border-left: 3px solid #f64d23; }

    /* SELECTBOXES DARK */
    div[data-baseweb="select"] > div { background-color: #1a202c !important; border: 1px solid #2d3748 !important; color: white !important; }
    label { color: #64748b !important; font-size: 10px !important; text-transform: uppercase !important; }

    /* BOTÃO EXECUTAR (BRANCO/CINZA CONFORME IMAGEM) */
    .stButton > button {
        background-color: #ffffff !important; color: #000000 !important;
        font-weight: 700; text-transform: uppercase; border-radius: 4px;
        padding: 10px 30px; border: none; font-size: 12px;
    }

    /* FOOTER STATUS */
    .footer-status {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background: #000; padding: 5px 20px; font-size: 9px;
        color: #475569; border-top: 1px solid #1e293b;
        display: flex; justify-content: space-between; z-index: 9999;
    }
    </style>
    """, unsafe_allow_html=True)

# --- COMPONENTES FIXOS (HEADER) ---
st.markdown("""
    <div class="nav-bar">
        <div class="logo">GESTOR IA</div>
        <div class="nav-links">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Estatísticas Avançadas</span>
            <span>Mercado Probabilístico</span>
            <span>Assertividade IA</span>
        </div>
        <div class="auth-buttons">
            <div class="btn-reg">REGISTRADOR</div>
            <div class="btn-ent">ENTRAR</div>
        </div>
    </div>
    <div style="margin-top: 80px;"></div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ESTRUTURADA ---
with st.sidebar:
    st.markdown('<div style="margin-top: 40px;"></div>', unsafe_allow_html=True)
    sidebar_menus = [
        "JOGOS DO DIA", "PRÓXIMOS JOGOS", "VENCEDORES DA COMPETIÇÃO",
        "APOSTAS POR ODDS", "APOSTAS POR GOLS", "APOSTAS POR ESCANTEIOS",
        "APOSTAS POR CARTÕES", "ÁRBITRO DA PARTIDA"
    ]
    for menu in sidebar_menus:
        st.markdown(f'<button class="side-btn">{menu}</button>', unsafe_allow_html=True)

# --- ÁREA CENTRAL (FILTROS) ---
st.markdown('<h2 style="font-weight: 900; letter-spacing: -1px;">ANÁLISE MÉTRICA DOS JOGOS</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
with col2:
    st.selectbox("CATEGORIA", ["Brasileirão", "Copa do Brasil"])
with col3:
    st.selectbox("CAMPEONATO", ["Série A", "Série B"])

st.markdown("<br><h4 style='font-size: 16px; font-weight: 700;'>Confronto: Série A</h4>", unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "São Paulo"])
with c2:
    st.selectbox("TIME FORA", ["Flamengo", "Corinthians", "Vasco"])

# BOTÃO EXECUTAR
st.markdown("<br>", unsafe_allow_html=True)
if st.button("EXECUTAR ALGORITMO"):
    with st.spinner("PROCESSANDO..."):
        time.sleep(2)
        st.success("CÁLCULO CONCLUÍDO!")

# --- FOOTER DE SEGURANÇA ---
st.markdown("""
    <div class="footer-status">
        <div>STATUS: ● IA OPERACIONAL | DESIGN V17.0 | KEY: GIAE-V17-ELITE-RECOVERY</div>
        <div>GESTOR IA PRO v18.0</div>
    </div>
    """, unsafe_allow_html=True)
