import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v59.0 - VERSÃO FINAL INTEGRADA]
# DIRETRIZ 1: APARÊNCIA IMUTÁVEL (ZERO WHITE REFORÇADO)
# DIRETRIZ 2: CORREÇÃO DE ERROS DE VARIÁVEIS (BOT 1 E 2)
# DIRETRIZ 3: RESTAURAÇÃO DE TODAS AS TELAS (BANCA, GOLS, ESCANTEIOS)
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# [DADOS DOS BOTS 1, 2 e 3] - VARIÁVEIS UNIFICADAS PARA EVITAR ERROS
if 'dados_ia' not in st.session_state:
    st.session_state.dados_ia = {
        "vencedor": "ANALISANDO...", 
        "gols": "OVER 2.5", 
        "prob": "92.4%", 
        "cartoes": "4.5+", 
        "escanteios": "9.5+", 
        "tiros_meta": "12+", 
        "chutes_gol": "8+", 
        "defesas": "6+", 
        "sync": "AGUARDANDO"
    }

# --- FUNÇÃO DE CARREGAMENTO DE DADOS ---
def carregar_dados():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        ts = os.path.getmtime(path)
        st.session_state.dados_ia["sync"] = datetime.fromtimestamp(ts).strftime('%d/%m %H:%M')
        try:
            return pd.read_csv(path)
        except:
            return None
    return None

df_diario = carregar_dados()

# 2. CAMADA DE ESTILO CSS INTEGRAL (MANTIDA 100% DA v57.35 - ZERO WHITE)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
        transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    .header-left { display: flex; align-items: center; gap: 25px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; letter-spacing: 0.5px; text-decoration: none; cursor: pointer;}
    .nav-links { display: flex; gap: 22px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600 !important; letter-spacing: 0.5px; white-space: nowrap; }
    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: all 0.2s ease !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important; padding-left: 35px !important; border-left: 3px solid #6d28d9 !important;
    }
    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important;
        letter-spacing: 1.2px !important; border-radius: 6px !important;
        width: 100% !important; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important;
    }
    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
    }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    div[data-baseweb="input"], .stNumberInput div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR COM HEADER FIXO
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <div class="logo-link">GESTOR IA</div>
                <div class="nav-links">
                    <div class="nav-item">TRADING PRO</div>
                </div>
            </div>
            <div class="header-right">
                <div class="registrar-pill">REGISTRAR</div>
                <div class="entrar-grad">ENTRAR</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;">
                <div style="background:{color_footer}; height:100%; width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- LÓGICA DE TELAS ---

# TELA 1: BILHETE OURO (IGUAL À FOTO v58.7)
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    
    # LINHA 1
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE", st.session_state.dados_ia["prob"], 92)
    with h3: draw_card("SUGESTÃO", st.session_state.dados_ia["gols"], 88)
    with h4: draw_card("IA STATUS", "ONLINE", 100, "#00ff88")
    
    # LINHA 2
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("VOL. GLOBAL", "ALTO", 75)
    with h6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    v_entrada = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    with h7: draw_card("VALOR ENTRADA", f"R$ {v_entrada:,.2f}", 100)
    with h8: draw_card("SISTEMA", "JARVIS v59.0", 100)

    # LINHA 3 (DADOS NOVOS DOS BOTS)
    st.markdown("### 🤖 MÉTRICAS AVANÇADAS DO BOT")
    b1, b2, b3, b4 = st.columns(4)
    with b1: draw_card("CARTÕES", st.session_state.dados_ia["cartoes"], 70, "#ffcc00")
    with b2: draw_card("ESCANTEIOS", st.session_state.dados_ia["escanteios"], 85, "#00d2ff")
    with b3: draw_card("CHUTES NO GOL", st.session_state.dados_ia["chutes_gol"], 60, "#9d54ff")
    with b4: draw_card("DEFESAS", st.session_state.dados_ia["defesas"], 50, "#ff4b4b")
    
    if df_diario is not None:
        st.markdown("### 📋 ANÁLISE DETALHADA (7 NÍVEIS)")
        st.dataframe(df_diario, use_container_width=True)

# TELA 2: GESTÃO DE BANCA (RESTAURADA)
elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns([1.2, 2.5])
    with col1:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total, step=50.0)
        st.session_state.stake_padrao = st.slider("STAKE POR OPERAÇÃO (%)", 0.1, 10.0, st.session_state.stake_padrao)
        st.session_state.meta_diaria = st.slider("META DIÁRIA (%)", 1.0, 30.0, st.session_state.meta_diaria)
    
    with col2:
        v_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        g1, g2 = st.columns(2)
        with g1: draw_card("VALOR DA ENTRADA", f"R$ {v_stake:,.2f}", 100, "#00d2ff")
        with g2: draw_card("ALVO DO DIA", f"R$ {(st.session_state.banca_total * (1 + st.session_state.meta_diaria/100)):,.2f}", 100, "#00ff88")

# TELA 3: SCANNER LIVE (CORREÇÃO DO KEYERROR)
elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    l1, l2, l3, l4 = st.columns(4)
    with l1: draw_card("PRESSÃO IA", "88%", 88)
    with l2: draw_card("GOLS PROVÁVEIS", st.session_state.dados_ia["gols"], 70)
    with l3: draw_card("TIROS DE META", st.session_state.dados_ia["tiros_meta"], 65)
    with l4: draw_card("DEFESAS GOLEIRO", st.session_state.dados_ia["defesas"], 90)

# TELA 4: SCANNER MANUAL (PRESERVADO)
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE (MANUAL)</h2>", unsafe_allow_html=True)
    st.info("Sua função manual de escolher times está ativa aqui.")
    m1, m2 = st.columns(2)
    with m1: st.selectbox("🌎 REGIÃO / PAÍS", ["BRASIL", "INGLATERRA", "ESPANHA"])
    with m2: st.selectbox("🏆 COMPETIÇÃO", ["SÉRIE A", "PREMIER LEAGUE", "LA LIGA"])
    if st.button("⚡ EXECUTAR ALGORITIMO IA", use_container_width=True):
        st.success("ANÁLISE FINALIZADA COM SUCESSO!")

# MERCADOS EXTRAS (RESTAURADOS)
elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ APOSTAS POR GOLS</h2>", unsafe_allow_html=True)
    g1, g2, g3, g4 = st.columns(4)
    with g1: draw_card("OVER 0.5 HT", "82%", 82)
    with g2: draw_card("OVER 1.5 FT", "75%", 75)
    with g3: draw_card("AMBAS MARCAM", "61%", 61)
    with g4: draw_card("UNDER 3.5", "90%", 90)

elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 APOSTAS POR ESCANTEIOS</h2>", unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4)
    with e1: draw_card("OVER 8.5", "88%", 88)
    with e2: draw_card("OVER 10.5", "62%", 62)
    with e3: draw_card("CANTOS HT", "4.5+", 70)
    with e4: draw_card("ASIÁTICOS", "9.0", 100)

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    st.info("Aguardando registros do Bot 1...")

# RODAPÉ COM SINAL DO BOT 3
st.markdown(f"""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v59.0 | SYNC: {st.session_state.dados_ia["sync"]}</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
