import streamlit as st
import time
import random
from datetime import datetime

# 1. CONFIGURAÇÃO DE PÁGINA (ESTÁTICO)
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- [FUNÇÕES DE NAVEGAÇÃO PARA EVITAR PISCAR] ---
def mudar_aba(nome_aba):
    st.session_state.aba_ativa = nome_aba

# --- [INICIALIZAÇÃO DE MEMÓRIA] ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# 2. ISOLAMENTO DO CABEÇALHO E ESTILOS (MELHORADO PARA NÃO PISCAR)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');
    
    /* BLOQUEIO DE FUNDO - EVITA FLASH BRANCO */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    /* ESCONDE ELEMENTOS NATIVOS QUE CAUSAM SALTO DE TELA */
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding-top: 60px !important; }
    
    /* HEADER FIXO - OTIMIZADO COM HARDWARE ACCELERATION */
    .betano-header { 
        position: fixed; 
        top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; 
        border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 30px !important; 
        z-index: 999999;
        /* Força estabilidade visual */
        backface-visibility: hidden;
        transform: translate3d(0,0,0);
        -webkit-font-smoothing: antialiased;
    }
    
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; letter-spacing: 1px; text-decoration: none !important; margin-right: 40px; }
    .nav-items { display: flex; gap: 20px; align-items: center; }
    .nav-items span { color: #ffffff; font-size: 9px !important; text-transform: uppercase; opacity: 0.7; font-weight: 600; }
    
    /* SIDEBAR DESIGN */
    [data-testid="stSidebar"] { background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; 
        color: #94a3b8 !important; 
        border: none !important; 
        border-bottom: 1px solid #1a202c !important; 
        text-align: left !important; 
        width: 100% !important; 
        padding: 18px 25px !important; 
        font-size: 10px !important; 
        text-transform: uppercase !important;
        border-radius: 0px !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { 
        color: #ffffff !important; 
        border-left: 4px solid #6d28d9 !important; 
        background: rgba(26, 36, 45, 0.8) !important; 
    }
    
    /* CARDS E HIGHLIGHTS */
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }
    
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px !important; border-radius: 8px; margin-bottom: 10px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>

    <div class="betano-header">
        <div style="display:flex; align-items:center;">
            <div class="logo-link">GESTOR IA</div>
            <div class="nav-items">
                <span>APOSTAS ESPORTIVAS</span>
                <span>APOSTAS AO VIVO</span>
                <span>OPORTUNIDADES IA</span>
                <span>ESTATÍSTICAS AVANÇADAS</span>
                <span>MERCADO PROBABILÍSTICO</span>
                <span>ASSERTIVIDADE IA</span>
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 20px;">
            <div style="color:white; font-size:14px;">🔍</div>
            <div style="color: #ffffff; font-size: 10px; font-weight: 700; border: 1px solid #ffffff; padding: 6px 15px; border-radius: 20px;">REGISTRAR</div>
            <div style="background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 7px 20px; border-radius: 4px; font-weight: 800; font-size: 10px;">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- [FUNÇÃO GLOBAL DE RENDERIZAÇÃO DE CARDS] ---
def draw_card(title, value, perc):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div class="conf-bar-bg">
                <div class="conf-bar-fill" style="width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- [DADOS] ---
DADOS_HIEARARQUIA = {
    "🏆 COPA DO MUNDO 2026": {"Seleções FIFA": {"Principais": ["Brasil", "Argentina", "França"]}},
    "🇧🇷 BRASIL (LIGAS & COPAS)": {"Campeonato Brasileiro": {"Série A": ["Flamengo", "Palmeiras", "Botafogo"]}},
    "🇪🇺 EUROPA (PRINCIPAIS LIGAS)": {"Ligas Nacionais": {"Premier League (Ing)": ["Man. City", "Arsenal", "Liverpool"]}}
}

# --- [SIDEBAR NAVEGAÇÃO OTIMIZADA] ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    # O uso de on_click resolve o "piscar" pois processa a mudança antes de reconstruir a página
    st.button("🎯 SCANNER PRÉ-LIVE", key="btn_nav_analise", on_click=mudar_aba, args=("analise",))
    st.button("📡 SCANNER EM TEMPO REAL", key="btn_nav_live", on_click=mudar_aba, args=("live",))
    st.button("💰 GESTÃO DE BANCA", key="btn_nav_gestao", on_click=mudar_aba, args=("gestao",))
    st.button("📜 HISTÓRICO DE CALLS", key="btn_nav_hist", on_click=mudar_aba, args=("historico",))

# --- [CONTEÚDO DINÂMICO] ---

if st.session_state.aba_ativa == "home":
    st.markdown("""<div style="background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px;">● LIVE: IA OPERACIONAL ● v57.23 GLOBAL DATABASE LOADED</div>""", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("Sugestão", "OVER 2.5 GOLS", 88)
    with h3: draw_card("IA Education", f"STAKE {st.session_state.stake_padrao}%", 100)
    with h4: draw_card("Tendência", "ODDS EM QUEDA", 75)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    cat = c1.selectbox("🌎 CATEGORIA", list(DADOS_HIEARARQUIA.keys()))
    tip = c2.selectbox("📂 TIPO", list(DADOS_HIEARARQUIA[cat].keys()))
    cmp = c3.selectbox("🏆 CAMPEONATO", list(DADOS_HIEARARQUIA[cat][tip].keys()))
    
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        st.session_state.analise_bloqueada = {"casa": "Time A", "fora": "Time B", "gols": "OVER 1.5", "stake_val": "R$ 10,00", "data": "14:00", "vencedor": "Time A"}
    
    if st.session_state.analise_bloqueada:
        st.success("Análise Concluída!")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    nova_banca = st.number_input("VALOR TOTAL DA BANCA", value=st.session_state.banca_total)
    if st.button("ATUALIZAR BANCA"):
        st.session_state.banca_total = nova_banca
        st.toast("Banca atualizada!")

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO</h2>", unsafe_allow_html=True)
    st.info("Aguardando novas entradas...")

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 AO VIVO</h2>", unsafe_allow_html=True)
    draw_card("JOGO ATUAL", "FLAMENGO 0x0 PALMEIRAS", 45)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.23</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
