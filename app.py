import streamlit as st
from datetime import datetime

# 1. CONFIGURAÇÃO (Sempre o primeiro)
st.set_page_config(page_title="GESTOR IA", layout="wide", initial_sidebar_state="expanded")

# --- [INICIALIZAÇÃO DE MEMÓRIA] ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []

# --- [ESTILOS CSS ESTABILIZADORES] ---
st.markdown("""
    <style>
    /* Trava o fundo da página para não brilhar branco */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0b0e11 !important;
    }
    
    /* Esconde o cabeçalho nativo que causa o 'salto' de tela */
    [data-testid="stHeader"] { display: none !important; }

    /* CABEÇALHO FIXO: Agora com lógica de persistência */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; 
        border-bottom: 1px solid rgba(255,255,255,0.1); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 30px !important; z-index: 1000000;
        pointer-events: none; /* Deixa cliques passarem para os botões abaixo se necessário */
    }
    
    .logo-text { color: #9d54ff !important; font-weight: 900; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; }
    
    /* Ajuste do conteúdo principal para não sumir atrás do header */
    [data-testid="stMainBlockContainer"] { padding-top: 70px !important; }

    /* Estilo dos botões da Sidebar (Scanner e Gestão) */
    section[data-testid="stSidebar"] div.stButton > button {
        background-color: transparent !important;
        color: #94a3b8 !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        width: 100% !important;
        padding: 18px 25px !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        border-radius: 0px !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        color: white !important;
        border-left: 4px solid #6d28d9 !important;
        background: rgba(26, 36, 45, 0.8) !important;
    }
    
    /* Cards de destaque */
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- [A SOLUÇÃO: HEADER DENTRO DA SIDEBAR] ---
# Colocamos o HTML aqui porque a Sidebar não recarrega do mesmo jeito que o corpo principal
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div style="display:flex; align-items:center; pointer-events: all;">
                <div class="logo-text">GESTOR IA</div>
                <div style="display: flex; gap: 20px; margin-left: 40px; color: white; font-size: 9px; opacity: 0.7; font-weight: 600;">
                    <span>APOSTAS ESPORTIVAS</span>
                    <span>APOSTAS AO VIVO</span>
                    <span style="color: #06b6d4;">SCANNER ATIVO</span>
                </div>
            </div>
            <div style="display: flex; gap: 15px; pointer-events: all;">
                <div style="color:white; border: 1px solid white; padding: 5px 15px; border-radius: 20px; font-size: 10px; font-weight: 700;">REGISTRAR</div>
                <div style="background: linear-gradient(90deg, #6d28d9, #06b6d4); color: white; padding: 6px 18px; border-radius: 4px; font-size: 10px; font-weight: 800;">ENTRAR</div>
            </div>
        </div>
        <div style="height: 50px;"></div>
    """, unsafe_allow_html=True)

    # Botões de Navegação
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"

# --- [CONTEÚDO DAS TELAS] ---
def draw_card(title, value):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">{title}</div><div style="color:white; font-size:18px; font-weight:900;">{value}</div></div>""", unsafe_allow_html=True)

if st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: draw_card("SITUAÇÃO", "BUSCANDO JOGOS...")
    with c2: draw_card("BANCA", f"R$ {st.session_state.banca_total:,.2f}")
    with c3: draw_card("IA", "ONLINE")
    
    # Campo de seleção para testar o "pisca"
    st.selectbox("Selecione a Liga para Analisar", ["Premier League", "Brasileirão", "La Liga"])

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    nova_banca = st.number_input("VALOR ATUAL DA BANCA", value=st.session_state.banca_total)
    if st.button("SALVAR CONFIGURAÇÕES"):
        st.session_state.banca_total = nova_banca
        st.success("Banca salva com sucesso!")

else:
    # Home ou outras abas
    st.markdown("<h2 style='color:white;'>🏠 DASHBOARD IA</h2>", unsafe_allow_html=True)
    st.info("Selecione uma ferramenta na barra lateral para começar.")

# FOOTER FIXO
st.markdown("""<div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #0d0d12; height: 25px; border-top: 1px solid #1e293b; padding: 5px 20px; font-size: 9px; color: #475569;">STATUS: IA OPERACIONAL | v57.23</div>""", unsafe_allow_html=True)
