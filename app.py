import streamlit as st
import time

# [GIAE PROTOCOLO SOBERANO v16.0 - DISTRIBUIÇÃO DE ESPAÇO ELITE]
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- BLOCO DE SEGURANÇA E ALINHAMENTO DE MARGEM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');

    /* 1. RESET E BLINDAGEM */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; }

    /* 2. NAVBAR ESTILO "CONTAINER LARGO" (IGUAL A BETANO) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 55px; 
        background-color: #121212 !important; 
        border-bottom: 1px solid #2d3843 !important; 
        display: flex; align-items: center; 
        /* O SEGREDO DO ESPAÇO: PADDING LATERAL DE 100PX */
        padding: 0 100px !important; 
        z-index: 999999; 
    }
    .logo-text { 
        color: #ffffff !important; font-weight: 900; font-size: 22px; 
        text-transform: uppercase; margin-right: 50px; letter-spacing: -1.2px; 
    }
    .nav-items { 
        display: flex; 
        /* GAP AMPLIADO PARA DAR SENSAÇÃO DE LARGURA */
        gap: 35px !important; 
        flex-grow: 1; 
        color: #ffffff !important; 
        font-size: 12px !important; 
        font-weight: 400 !important; 
        text-transform: uppercase; 
        letter-spacing: 0.8px; 
    }

    /* BOTÕES DA NAVBAR (ESTILO REFINADO) */
    .btn-registrar { border: 1px solid #475569; color: white; padding: 6px 15px; border-radius: 4px; font-size: 11px; font-weight: 700; cursor: pointer; }
    .btn-entrar { background: #00cc66 !important; color: white !important; padding: 8px 22px; border-radius: 4px; font-weight: 800; border: none; font-size: 11px; cursor: pointer; }

    /* 3. SIDEBAR (SUBIDA MÁXIMA E LIMPEZA) */
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        border-right: 1px solid #2d3843 !important;
        margin-top: 55px !important;
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; padding-top: 0px !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { 
        margin-top: -65px !important; /* PUXA JOGOS DO DIA PARA O TOPO */
        gap: 0px !important; 
    }
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        color: #94a3b8 !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        border-radius: 0px !important;
        text-align: left !important;
        width: 100% !important;
        padding: 12px 20px !important;
        font-weight: 400 !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.8px;
    }
    [data-testid="stSidebar"] button:hover { color: #f64d23 !important; border-left: 3px solid #f64d23 !important; }

    /* 4. CONTEÚDO CENTRAL (ELEVAÇÃO MÁXIMA ITEM 1) */
    [data-testid="stAppViewBlockContainer"] { 
        padding-top: 10px !important; /* ENCOSTA O TÍTULO NA NAVBAR */
        padding-left: 5rem !important; 
        padding-right: 5rem !important; 
    }

    /* 5. BOTÃO EXECUTAR ALGORITMO (REFORÇO LARANJA - ITEM 3) */
    /* Usei seletores mais fortes para garantir a cor da sua foto */
    div.stButton > button {
        background-color: #f64d23 !important; /* LARANJA OBRIGATÓRIO */
        background: #f64d23 !important; 
        color: #ffffff !important; 
        border-radius: 50px !important;
        height: 42px !important; 
        width: 240px !important; 
        font-weight: 800 !important;
        font-size: 12px !important;
        text-transform: uppercase !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(246, 77, 35, 0.4) !important;
        visibility: visible !important;
        display: flex !important;
    }

    /* 6. SELECTBOXES DARK */
    div[data-baseweb="select"] > div { background-color: #1a242d !important; border: 1px solid #2d3843 !important; }
    div[data-baseweb="select"] * { color: #e2e8f0 !important; font-weight: 400 !important; }

    /* FOOTER */
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #121212; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #64748b; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR (IDENTIDADE BETANO) ---
st.markdown(f"""
    <div class="betano-header">
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-items">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Estatísticas Avançadas</span>
            <span>Mercado Probabilístico</span>
            <span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:15px; align-items:center;">
            <div class="btn-registrar">REGISTRAR</div>
            <div class="btn-entrar">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (TOTALMENTE ELEVADA) ---
with st.sidebar:
    st.button("JOGOS DO DIA")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL (ENCOSTADA NO TOPO) ---
st.markdown('<div style="color:white; font-weight:900; font-size:24px; margin-bottom:15px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1: st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
with c2: st.selectbox("CATEGORIA", ["Brasileirão", "Copa do Brasil"])
with c3: st.selectbox("CAMPEONATO", ["Série A", "Série B"])

st.markdown("<hr style='border: 0.1px solid #2d3843; opacity: 0.2; margin: 15px 0;'>", unsafe_allow_html=True)
st.markdown('<div style="color:white; font-weight:700; font-size:16px; margin-bottom:10px;">Confronto: Série A</div>', unsafe_allow_html=True)

t1, t2 = st.columns(2)
with t1: st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "Botafogo"])
with t2: st.selectbox("TIME FORA", ["Flamengo", "Vasco", "Palmeiras"])

# BOTÃO EXECUTAR (AGORA OBRIGATORIAMENTE LARANJA)
if st.button("EXECUTAR ALGORITMO"):
    with st.status("GIAE IA: Processando...", expanded=False):
        time.sleep(1)
    st.success("🤖 Análise pronta!")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN V16.0</div><div>GESTOR IA PRO v16.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
