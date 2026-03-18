import streamlit as st
import time
import random
from datetime import datetime

# ==============================================================================
# [GIAE KERNEL SHIELD v57.6 - ANTI-GHOSTING & FRAGMENTATION LOCK]
# FIX: ISOLAMENTO DE RENDERIZAÇÃO VIA st.fragment | CSS PERSISTENCE
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- [LOCK] BLOCO DE SEGURANÇA CSS (INJETADO UMA ÚNICA VEZ) ---
def inject_stable_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');
        header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
        .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
        [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }
        [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
        .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; }
        .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; letter-spacing: 1px; text-decoration: none !important; margin-right: 60px; }
        .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; transition: 0.2s; }
        .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px !important; border-radius: 8px; margin-bottom: 10px; }
        /* Anti-Ghosting: Remove transições de botões que causam flicker */
        button { transition: none !important; }
        </style>
        """, unsafe_allow_html=True)

inject_stable_css()

# --- [FUNÇÕES DE NÚCLEO] ---
def acao_salvar():
    if st.session_state.analise_bloqueada:
        st.session_state.historico_calls.append(st.session_state.analise_bloqueada)
        st.toast("✅ ANÁLISE SALVA!") # Toast não causa re-render de layout

def acao_apagar(idx):
    st.session_state.historico_calls.pop(idx)
    # st.rerun() não é mais necessário aqui dentro do fragmento

# --- [INICIALIZAÇÃO DE MEMÓRIA] ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_atual' not in st.session_state: st.session_state.banca_atual = 1000.0
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None

# --- BASE DE DADOS ---
DADOS_HIEARARQUIA = {
    "BRASIL": {
        "Nacional": {
            "Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo", "São Paulo", "Grêmio", "Atlético-MG", "Fluminense", "Internacional", "Corinthians", "Bahia", "Cruzeiro", "Vasco", "Athletico-PR", "Fortaleza", "Cuiabá", "Criciúma", "Juventude", "Vitória", "Bragantino", "Atlético-GO"],
            "Brasileirão Série B": ["Santos", "Sport", "Coritiba", "Goiás", "Ceará", "Novorizontino", "Vila Nova", "Amazonas", "Operário-PR", "Avaí", "Chapecoense", "Ponte Preta"]
        }
    },
    "EUROPA": {
        "Competições UEFA": {
            "UEFA Champions League": ["Real Madrid", "Man. City", "Bayern Munique", "Arsenal", "Barcelona", "Inter de Milão", "PSG", "Dortmund", "Juventus", "Bayer Leverkusen"]
        }
    }
}

# --- CABEÇALHO FIXO (FORA DO RE-RENDER) ---
st.markdown("""<div class="betano-header"><div class="header-left"><a class="logo-link">GESTOR IA</a></div><div style="color:white; font-size:10px; opacity:0.5;">JARVIS v57.6 - STABLE</div></div>""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE", use_container_width=True): st.session_state.aba_ativa = "analise"
    if st.button("📜 HISTÓRICO", use_container_width=True): st.session_state.aba_ativa = "historico"
    if st.button("🏠 HOME", use_container_width=True): st.session_state.aba_ativa = "home"

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- [FRAGMENTO: SCANNER] ---
@st.fragment
def render_scanner():
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    cat = c1.selectbox("🌎 CATEGORIA", list(DADOS_HIEARARQUIA.keys()))
    tip = c2.selectbox("📂 TIPO", list(DADOS_HIEARARQUIA[cat].keys()))
    cmp = c3.selectbox("🏆 CAMPEONATO", list(DADOS_HIEARARQUIA[cat][tip].keys()))
    
    t1, t2 = st.columns(2)
    casa = t1.selectbox("🏠 CASA", DADOS_HIEARARQUIA[cat][tip][cmp])
    fora = t2.selectbox("🚀 VISITANTE", [t for t in DADOS_HIEARARQUIA[cat][tip][cmp] if t != casa])

    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        st.session_state.analise_bloqueada = {"casa": casa, "fora": fora, "data": datetime.now().strftime("%d/%m %H:%M"), "vencedor": casa, "gols": "OVER 1.5", "cantos": "9.5+"}
        st.rerun()

    if st.session_state.analise_bloqueada:
        st.button("📥 SALVAR NO HISTÓRICO", on_click=acao_salvar, use_container_width=True)

# --- [FRAGMENTO: HISTÓRICO - ONDE O PISCADO OCORRE] ---
@st.fragment
def render_historico():
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    if not st.session_state.historico_calls:
        st.info("Vazio.")
    else:
        # Criamos o container do histórico que vai sofrer o update isolado
        for i, call in enumerate(reversed(st.session_state.historico_calls)):
            idx_real = len(st.session_state.historico_calls) - 1 - i
            cols = st.columns([0.85, 0.15])
            cols[0].markdown(f"""<div class="history-card-box"><span style="color:#9d54ff; font-weight:900;">[{call['data']}]</span> <span style="color:white; margin-left:15px;">{call['casa']} x {call['fora']}</span></div>""", unsafe_allow_html=True)
            # O segredo: Este botão agora só recarrega este fragmento!
            if cols[1].button("🗑️", key=f"del_v576_{idx_real}"):
                acao_apagar(idx_real)
                st.rerun(scope="fragment") # Recarrega apenas o histórico!

# --- RENDERIZAÇÃO LÓGICA ---
if st.session_state.aba_ativa == "home":
    st.markdown("""<div class="news-ticker">● LIVE: IA OPERACIONAL ● HIERARQUIA v57.6 ATIVA</div>""", unsafe_allow_html=True)
    # (Restante dos 8 cards da Home aqui...)
    st.info("Interface Principal Estabilizada. Acesse o Scanner ou Histórico pelo menu.")

elif st.session_state.aba_ativa == "analise":
    render_scanner()

elif st.session_state.aba_ativa == "historico":
    render_historico()

st.markdown("""<div style="position:fixed; bottom:0; left:0; width:100%; background:#0d0d12; height:25px; border-top:1px solid #1e293b; display:flex; justify-content:center; align-items:center; font-size:9px; color:#475569; z-index:999999;">STATUS: ● IA OPERACIONAL | ANTI-GHOSTING ACTIVE</div>""", unsafe_allow_html=True)
