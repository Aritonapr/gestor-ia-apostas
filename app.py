import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v8.0 - ANTI-WHITE-BOX BLINDAGEM]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS DE FORÇA BRUTA (PARA ELIMINAR O FUNDO BRANCO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* 1. RESET TOTAL DE FUNDO */
    header, [data-testid="stHeader"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; }
    
    /* Limpeza da Sidebar */
    [data-testid="stSidebar"] { 
        background-color: #11151a !important; 
        border-right: 1px solid #2d3843 !important;
        margin-top: 50px !important;
    }
    
    /* REMOÇÃO DO FUNDO BRANCO DOS BOTÕES DA SIDEBAR */
    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] button {
        background-color: transparent !important; /* Remove o fundo branco */
        background: transparent !important;
        color: #adb5bd !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        border-radius: 0px !important;
        text-align: left !important;
        justify-content: flex-start !important;
        width: 100% !important;
        padding: 15px 20px !important;
        font-weight: 700 !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        box-shadow: none !important; /* Remove sombras que criam bordas brancas */
    }

    /* Efeito de Hover na Sidebar - Apenas uma borda laranja e troca de cor */
    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] button:hover {
        color: #f64d23 !important;
        background-color: #1a242d !important;
        border-left: 3px solid #f64d23 !important;
    }

    /* 2. NAVBAR SUPERIOR (PROTEÇÃO LARANJA) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 50px; 
        background-color: #f64d23 !important; 
        display: flex; align-items: center; padding: 0 25px; z-index: 999999; 
    }
    .logo-text { color: white !important; font-weight: 900; font-size: 20px; letter-spacing: -1px; text-transform: uppercase; margin-right: 35px; }
    .nav-items { display: flex; gap: 15px; flex-grow: 1; color: white; font-size: 10px; font-weight: 700; text-transform: uppercase; }

    /* 3. CORREÇÃO DO BOTÃO CENTRAL "EXECUTAR ALGORITMO" */
    /* Forçando para não ficar branco como na sua foto */
    .main .stButton button {
        background-color: #f64d23 !important; /* COR LARANJA FORÇADA */
        color: white !important;             /* TEXTO BRANCO FORÇADO */
        border-radius: 50px !important;
        height: 55px !important;
        width: 320px !important;
        font-weight: 900 !important;
        text-transform: uppercase !important;
        border: none !important;
        margin-top: 30px !important;
        box-shadow: 0 4px 15px rgba(246, 77, 35, 0.4) !important;
    }
    .main .stButton button:hover {
        background-color: #ff6b4a !important;
        box-shadow: 0 0 25px #f64d23 !important;
    }

    /* 4. AJUSTES DOS SELECTBOXES PARA TEMA DARK */
    div[data-baseweb="select"] > div {
        background-color: #1a242d !important;
        border: 1px solid #2d3843 !important;
        color: white !important;
    }
    div[data-baseweb="select"] * { color: white !important; }

    /* 5. OCULTAR SCROLLBAR DA SIDEBAR */
    [data-testid="stSidebarContent"] { overflow: hidden !important; }

    /* FOOTER */
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR (IDENTIDADE VISUAL) ---
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
            <div style="border:1px solid white; color:white; padding:5px 12px; border-radius:3px; font-size:11px; font-weight:bold;">REGISTRAR</div>
            <div style="background:#00cc66; color:white; padding:6px 20px; border-radius:3px; font-weight:bold; font-size:11px;">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (LIMPA E DISCRETA) ---
with st.sidebar:
    st.button("JOGOS DO DIA")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL ---
st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-top:20px; margin-bottom:25px;">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)

# Filtros em 3 colunas
c1, c2, c3 = st.columns(3)
with c1: st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS", "EUROPA"])
with c2: st.selectbox("CATEGORIA", ["Brasileirão", "Copa do Brasil"])
with c3: st.selectbox("CAMPEONATO", ["Série A", "Série B"])

st.markdown("<hr style='border: 0.1px solid #2d3843; opacity: 0.5;'>", unsafe_allow_html=True)
st.markdown('<div style="color:white; font-weight:700; font-size:18px; margin:20px 0;">Confronto: Série A</div>', unsafe_allow_html=True)

t1, t2 = st.columns(2)
with t1: st.selectbox("TIME CASA", ["Palmeiras", "Flamengo", "Botafogo"])
with t2: st.selectbox("TIME FORA", ["Flamengo", "Vasco", "Palmeiras"])

# Botão Executar (Agora Laranja e Visível)
if st.button("EXECUTAR ALGORITMO"):
    with st.status("GIAE IA: Processando...", expanded=False):
        time.sleep(1)
    st.success("🤖 Concluído!")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN V8.0 BLINDADO</div><div>GESTOR IA PRO v8.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
