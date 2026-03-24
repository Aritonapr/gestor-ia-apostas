import streamlit as st
import time
from datetime import datetime

# ==============================================================================
# [PROTOCOLO v57.30 - VERSÃO BLINDADA E ORGANIZADA]
# ==============================================================================

# 1. CONFIGURAÇÃO INICIAL DA PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- MEMÓRIA DO SISTEMA (IMPEDE QUEBRAS AO CLICAR) ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None

# 2. ESTILO VISUAL (CORREÇÃO DE CORES E MENU 11px)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    /* FUNDO ESCURO TOTAL */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    /* REMOVER CABEÇALHO PADRÃO DO STREAMLIT */
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 80px 40px 20px 40px !important; }

    /* MENU SUPERIOR AZUL (ESTILO BETANO) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid #1e293b;
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px; z-index: 9999;
    }
    .logo-ia { color: #9d54ff; font-weight: 900; font-size: 20px; text-transform: uppercase; }
    .menu-texto { color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; margin-left: 20px; }

    /* BOTÕES DA LATERAL (SIDEBAR) */
    [data-testid="stSidebar"] { background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 15px 20px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important; border-left: 4px solid #6d28d9 !important;
    }

    /* QUADRADOS DE INFORMAÇÃO (CARDS) */
    .quadrado-info { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 150px; margin-bottom: 15px;
    }

    /* RODAPÉ STATUS */
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; background: #0d0d12; height: 25px; border-top: 1px solid #1e293b; font-size: 9px; color: #475569; display: flex; align-items: center; padding: 0 20px; z-index: 9999; }
    </style>
""", unsafe_allow_html=True)

# 3. CONSTRUÇÃO DO MENU SUPERIOR E LATERAL
st.markdown("""
    <div class="betano-header">
        <div style="display: flex; align-items: center;">
            <div class="logo-ia">GESTOR IA</div>
            <div class="menu-texto">Apostas Esportivas</div>
            <div class="menu-texto">Estatísticas</div>
            <div class="menu-texto">Mercado Pro</div>
        </div>
        <div style="background: linear-gradient(90deg, #6d28d9, #06b6d4); color: white; padding: 8px 20px; border-radius: 5px; font-weight: 800; font-size: 10px;">ENTRAR</div>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("🏆 VENCEDORES"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

# FUNÇÃO PARA CRIAR OS QUADRADOS (CARDS)
def criar_quadrado(titulo, valor, progresso, cor="#6d28d9"):
    st.markdown(f"""
        <div class="quadrado-info">
            <div style="color:#64748b; font-size:9px; font-weight: 700; text-transform: uppercase;">{titulo}</div>
            <div style="color:white; font-size:18px; font-weight:900; margin-top:15px;">{valor}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:15px auto;">
                <div style="background:{cor}; height:100%; width:{progresso}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- LÓGICA DE NAVEGAÇÃO (CONTEÚDO DAS PÁGINAS) ---

# TELA 1: HOME
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: criar_quadrado("Banca Atual", f"R$ {st.session_state.banca_total}", 100)
    with c2: criar_quadrado("Sinal do Dia", "Real Madrid", 95, "#00ff88")
    with c3: criar_quadrado("Dica IA", "Over 1.5 Gols", 88)
    with c4: criar_quadrado("Status IA", "Online", 100, "#06b6d4")

# TELA 2: SCANNER PRÉ-LIVE (ORGANIZADO PARA NÃO QUEBRAR)
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    # Lista de Campeonatos (Simples e Direta)
    campeonatos = ["Brasileirão Série A", "Champions League", "Premier League", "La Liga", "Libertadores"]
    escolha = st.selectbox("🏆 ESCOLHA O CAMPEONATO", campeonatos)
    
    col1, col2 = st.columns(2)
    with col1: time_casa = st.text_input("🏠 Mandante", "Time da Casa")
    with col2: time_fora = st.text_input("🚀 Visitante", "Time de Fora")
    
    if st.button("⚡ ANALISAR JOGO AGORA"):
        st.session_state.analise_bloqueada = {"time": time_casa, "odd": "1.85", "conf": "92%"}
    
    if st.session_state.analise_bloqueada:
        st.markdown(f"<div style='color:#9d54ff; font-weight:800; margin-bottom:15px;'>RESULTADO PARA: {escolha}</div>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: criar_quadrado("Decisão IA", "Vitória Casa", 92, "#00ff88")
        with r2: criar_quadrado("Mercado", "Match Odds", 100)
        with r3: criar_quadrado("Confiança", "92%", 92)
        with r4: criar_quadrado("Sugestão", "Stake 1%", 100, "#06b6d4")

# TELA 3: GESTÃO DE BANCA
elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("Valor da Banca", value=st.session_state.banca_total)
    st.session_state.stake_padrao = st.slider("Stake %", 0.5, 5.0, st.session_state.stake_padrao)
    
    valor_entrada = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    st.markdown("<br>", unsafe_allow_html=True)
    criar_quadrado("Valor por Entrada", f"R$ {valor_entrada:,.2f}", 100, "#00d2ff")

# TELA 4: LIVE
elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER LIVE</h2>", unsafe_allow_html=True)
    l1, l2, l3, l4 = st.columns(4)
    with l1: criar_quadrado("Decisão Live", "Over 0.5 HT", 85, "#00ff88")
    with l2: criar_quadrado("Ataques", "MUITO ALTO", 90)
    with l3: criar_quadrado("Pressão", "88%", 88)
    with l4: criar_quadrado("Entrada", "AGORA", 100, "#06b6d4")

# OUTRAS TELAS (SIMPLIFICADAS PARA EVITAR ERROS)
elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🏆 VENCEDORES</h2>", unsafe_allow_html=True)
    criar_quadrado("Favorito Título", "Man. City", 94, "#00ff88")

elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ MERCADO DE GOLS</h2>", unsafe_allow_html=True)
    criar_quadrado("Sugestão Gols", "Over 2.5 FT", 85, "#9d54ff")

elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 MERCADO DE CANTOS</h2>", unsafe_allow_html=True)
    criar_quadrado("Sugestão Cantos", "Over 9.5", 89, "#06b6d4")

# RODAPÉ
st.markdown("""<div class="footer">STATUS: ● JARVIS IA v57.30 OPERACIONAL</div>""", unsafe_allow_html=True)
