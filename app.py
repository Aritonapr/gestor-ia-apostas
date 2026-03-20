import streamlit as st
from datetime import datetime

# 1. CONFIGURAÇÃO DE PÁGINA (DEVE SER A PRIMEIRA COISA)
st.set_page_config(page_title="GESTOR IA", layout="wide", initial_sidebar_state="expanded")

# --- LÓGICA DE NAVEGAÇÃO ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []

def navegar(aba):
    st.session_state.aba_ativa = aba

# 2. ESTILIZAÇÃO CSS (O SEGREDO PARA NÃO PISCAR)
# Injetamos o CSS de uma forma que ele "trava" o layout antes de renderizar os widgets
st.markdown("""
    <style>
    /* 1. TRAVA O FUNDO E O HEADER NO NAVEGADOR */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0b0e11 !important;
    }
    
    /* Remove a barra nativa do Streamlit que causa o "pulo" no topo */
    header[data-testid="stHeader"] {
        display: none !important;
    }

    /* 2. HEADER FIXO COM PRIORIDADE DE RENDERIZAÇÃO */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; 
        border-bottom: 1px solid rgba(255,255,255,0.1);
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 30px; z-index: 1000000;
        /* Hardware Acceleration - Impede o piscar */
        transform: translateZ(0);
        backface-visibility: hidden;
    }

    /* 3. ESTABILIZA O CONTEÚDO PARA NÃO SUBIR AO CLICAR */
    [data-testid="stMainBlockContainer"] {
        padding-top: 80px !important; /* Espaço exato para o header não cobrir nada */
    }

    /* Estilos dos Botões da Sidebar para parecerem abas nativas */
    section[data-testid="stSidebar"] div.stButton > button {
        background-color: transparent !important;
        color: #94a3b8 !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        border-radius: 0px !important;
        text-align: left !important;
        width: 100% !important;
        padding: 15px 20px !important;
        transition: 0.2s;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        color: white !important;
        background-color: #1e293b !important;
        border-left: 4px solid #6d28d9 !important;
    }

    /* Cards Estilizados */
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }
    </style>

    <div class="betano-header">
        <div style="display:flex; align-items:center;">
            <div style="color: #9d54ff; font-weight: 900; font-size: 20px; text-transform: uppercase; letter-spacing: 1px;">GESTOR IA</div>
            <div style="display: flex; gap: 20px; align-items: center; margin-left: 40px;">
                <span style="color:white; font-size:9px; opacity:0.7;">APOSTAS AO VIVO</span>
                <span style="color:white; font-size:9px; opacity:0.7;">OPORTUNIDADES IA</span>
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 20px;">
            <div style="color: white; border: 1px solid white; padding: 5px 15px; border-radius: 20px; font-size: 10px;">REGISTRAR</div>
            <div style="background: linear-gradient(90deg, #6d28d9, #06b6d4); color: white; padding: 6px 18px; border-radius: 4px; font-size: 10px; font-weight: 800;">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 3. SIDEBAR (NAVEGAÇÃO)
with st.sidebar:
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    st.button("🎯 SCANNER PRÉ-LIVE", on_click=navegar, args=("analise",))
    st.button("📡 SCANNER AO VIVO", on_click=navegar, args=("live",))
    st.button("💰 GESTÃO DE BANCA", on_click=navegar, args=("gestao",))
    st.button("📜 HISTÓRICO", on_click=navegar, args=("historico",))

# 4. FUNÇÃO AUXILIAR DE UI
def draw_card(title, value, perc):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform:uppercase;">{title}</div>
            <div style="color:white; font-size:18px; font-weight:900; margin-top:5px;">{value}</div>
            <div class="conf-bar-bg"><div class="conf-bar-fill" style="width:{perc}%;"></div></div>
        </div>
    """, unsafe_allow_html=True)

# 5. CONTEÚDO DINÂMICO
if st.session_state.aba_ativa == "home" or st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 Scanner Especializado</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: draw_card("Banca Atual", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with c2: draw_card("Confiança IA", "88%", 88)
    with c3: draw_card("Risco Sugerido", f"{st.session_state.stake_padrao}%", 100)
    
    # Exemplo de interação que faria piscar (mas agora está estável)
    st.selectbox("Escolha a Liga", ["Brasileirão Série A", "Premier League", "La Liga"])

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 Gestão Financeira</h2>", unsafe_allow_html=True)
    new_bank = st.number_input("Valor da Banca", value=st.session_state.banca_total)
    if st.button("Salvar"):
        st.session_state.banca_total = new_bank
        st.success("Banca Atualizada")

elif st.session_state.aba_ativa == "live":
    st.warning("Scanner em Tempo Real carregando dados...")

# FOOTER FIXO
st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #0d0d12; height: 25px; border-top: 1px solid #1e293b; padding: 5px 20px; font-size: 9px; color: #475569; z-index: 999;">
        STATUS: IA OPERACIONAL | PROTEÇÃO JARVIS ATIVA
    </div>
""", unsafe_allow_html=True)
