import streamlit as st
import time

# [GIAE SHIELD v10.0 - PROTEÇÃO TOTAL DE INTERFACE]
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- BLOCO DE SEGURANÇA CSS (BLINDAGEM CONTRA ALTERAÇÕES INDESEJADAS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* 1. ELIMINAÇÃO DE ELEMENTOS NATIVOS QUE CAUSAM QUEBRA */
    header, [data-testid="stHeader"], 
    [data-testid="stSidebarCollapseButton"], 
    [data-testid="stSidebarNav"] { 
        display: none !important; 
        visibility: hidden !important;
    }

    /* 2. CONFIGURAÇÃO DO APP E FUNDO */
    .stApp { background-color: #0b0e11 !important; }
    
    /* Puxar conteúdo principal para o topo máximo */
    .main .block-container { 
        padding-top: 50px !important; /* Altura exata da Navbar */
        padding-left: 3rem !important;
        padding-right: 3rem !important;
    }

    /* 3. NAVBAR SUPERIOR (FIXA E LARANJA) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 50px; 
        background-color: #f64d23 !important; 
        display: flex; align-items: center; padding: 0 25px; z-index: 999999; 
    }
    .logo-text { color: white !important; font-weight: 900; font-size: 20px; text-transform: uppercase; margin-right: 35px; }
    .nav-items { display: flex; gap: 15px; flex-grow: 1; color: white; font-size: 10px; font-weight: 700; text-transform: uppercase; }

    /* BOTÕES DA NAVBAR */
    .btn-registrar { border: 1px solid white; color: white; padding: 5px 12px; border-radius: 3px; font-size: 11px; font-weight: bold; }
    .btn-entrar { background: #00cc66 !important; color: white !important; padding: 6px 20px; border-radius: 3px; font-weight: bold; border: none; font-size: 11px; }

    /* 4. SIDEBAR BLINDADA (SEM BOTÕES QUADRADOS, ESTILO MENU LISTA) */
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        border-right: 1px solid #2d3843 !important;
        margin-top: 50px !important;
    }
    
    /* Ocultar barra de rolagem lateral */
    [data-testid="stSidebarContent"] { 
        overflow: hidden !important; 
        padding-top: 0px !important; 
    }

    /* Regra de Ouro: Estilo dos itens da Sidebar (Lista) */
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        background: transparent !important;
        color: #adb5bd !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        border-radius: 0px !important;
        text-align: left !important;
        justify-content: flex-start !important;
        width: 100% !important;
        padding: 12px 20px !important;
        font-weight: 700 !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        box-shadow: none !important;
        margin: 0px !important;
    }

    /* Hover nos itens da lista lateral */
    [data-testid="stSidebar"] button:hover {
        color: #f64d23 !important;
        background-color: #1a242d !important;
        border-left: 3px solid #f64d23 !important;
    }

    /* 5. ÁREA CENTRAL - BOTÃO EXECUTAR ALGORITMO (ESTILO CÁPSULA LARANJA) */
    /* Usando seletor de descendência para não afetar a sidebar */
    .main .stButton button {
        background-color: #f64d23 !important;
        color: #ffffff !important;
        border-radius: 50px !important;
        height: 55px !important;
        width: 320px !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        border: none !important;
        margin-top: 25px !important;
        box-shadow: 0 4px 15px rgba(246, 77, 35, 0.4) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        opacity: 1 !important;
        visibility: visible !important;
    }
    
    .main .stButton button:hover {
        background-color: #ff6b4a !important;
        box-shadow: 0 0 25px #f64d23 !important;
        transform: scale(1.02);
    }

    /* 6. ESTILO DOS SELECTBOXES (TEMA DARK) */
    div[data-baseweb="select"] > div { background-color: #1a242d !important; border: 1px solid #2d3843 !important; }
    div[data-baseweb="select"] * { color: white !important; font-size: 13px !important; }
    div[data-testid="stSelectbox"] label p { color: #94a3b8 !important; font-size: 11px !important; font-weight: 700; text-transform: uppercase; }

    /* Puxar o título para cima */
    .css-10trblm, .css-1offfwp { padding-top: 0px !important; }
    
    /* FOOTER */
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR SUPERIOR ---
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
        <div style="margin-left:auto; display:flex; gap:12px; align-items:center;">
            <div class="btn-registrar">REGISTRAR</div>
            <div class="btn-entrar">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (JOGOS DO DIA + LISTA DE MENU) ---
with st.sidebar:
    # Este bloco VerticalBlock agora está blindado contra espaçamentos
    st.button("JOGOS DO DIA")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- CONTEÚDO PRINCIPAL ---
# Título subido ao máximo
st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:20px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)

# Grid de Filtros
c1, c2, c3 = st.columns(3)
with c1: st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
with c2: st.selectbox("CATEGORIA", ["Brasileirão", "Copa do Brasil"])
with c3: st.selectbox("CAMPEONATO", ["Série A", "Série B"])

st.markdown("<hr style='border: 0.1px solid #2d3843; opacity: 0.3; margin: 15px 0;'>", unsafe_allow_html=True)
st.markdown('<div style="color:white; font-weight:700; font-size:18px; margin-bottom:15px;">Confronto: Série A</div>', unsafe_allow_html=True)

t1, t2 = st.columns(2)
with t1: st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "Botafogo"])
with t2: st.selectbox("TIME FORA", ["Flamengo", "Vasco", "Palmeiras"])

# BOTÃO EXECUTAR ALGORITMO (LARANJA, CÁPSULA E VISÍVEL)
if st.button("EXECUTAR ALGORITMO"):
    with st.status("GIAE IA: Processando dados...", expanded=False):
        time.sleep(1)
    st.success("🤖 Análise Concluída!")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN V10.0 BLINDADO</div><div>GESTOR IA PRO v10.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
