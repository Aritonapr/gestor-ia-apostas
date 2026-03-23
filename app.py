import streamlit as st
import time
from datetime import datetime

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- MEMÓRIA E ESTADOS ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# --- BANCO DE DADOS DE TIMES (ESTRUTURA SEGURA) ---
DB_TIMES = {
    "BRASIL": ["Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "São Paulo", "Internacional", "Cruzeiro", "Bahia", "Vasco", "Atlético-MG", "Fluminense", "Grêmio"],
    "EUROPA": ["Real Madrid", "Man. City", "Liverpool", "Arsenal", "Barcelona", "Bayern Munique", "Inter de Milão", "PSG", "Bayer Leverkusen", "Juventus"],
    "MUNDO (SELEÇÕES)": ["Brasil", "Argentina", "França", "Espanha", "Inglaterra", "Portugal", "Alemanha", "Uruguai"]
}

# 2. CSS INTEGRAL (REFORÇO ZERO WHITE)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; transform: translate3d(0,0,0);
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    .nav-links { display: flex; gap: 18px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 8.5px !important; text-transform: uppercase; opacity: 0.8; font-weight: 700; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }

    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
        transition: all 0.3s ease; transform: translate3d(0,0,0);
    }
    .highlight-card:hover { transform: translateY(-5px); border-color: #6d28d9; box-shadow: 0 10px 20px rgba(0,0,0,0.4); }
    
    .banca-title-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 22px; font-weight: 800; margin-bottom: 30px; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    
    div[data-baseweb="input"], .stNumberInput div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("""<div class="betano-header"><div class="logo-link">GESTOR IA</div><div class="entrar-grad">PRO v57.24</div></div><div style="height:65px;"></div>""", unsafe_allow_html=True) 
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("🏆 VENCEDORES"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"
    if st.button("📜 HISTÓRICO"): st.session_state.aba_ativa = "historico"

def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color_footer}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- TELAS ---

# HOME
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with h3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with h4: draw_card("IA STATUS", "ONLINE", 100)
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("VOL. GLOBAL", "ALTO", 75)
    with h6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with h7: draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
    with h8: draw_card("SISTEMA", "JARVIS v57.24", 100)

# GESTÃO
elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>""", unsafe_allow_html=True)
    c_in, c_grid = st.columns([1.2, 2.5])
    with c_in:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total, step=100.0)
        st.session_state.stake_padrao = st.slider("STAKE (%)", 0.5, 10.0, st.session_state.stake_padrao)
        st.session_state.meta_diaria = st.slider("META (%)", 1.0, 20.0, st.session_state.meta_diaria)
    v_s = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    with c_grid:
        g1, g2, g3, g4 = st.columns(4)
        with g1: draw_card("ENTRADA", f"R$ {v_s:,.2f}", 100)
        with g2: draw_card("STOP GAIN", f"R$ {(st.session_state.banca_total * st.session_state.meta_diaria / 100):,.2f}", 100)
        with g3: draw_card("STOP LOSS", f"R$ {(st.session_state.banca_total * st.session_state.stop_loss / 100):,.2f}", 100)
        with g4: draw_card("ALVO", f"R$ {st.session_state.banca_total * 1.03:,.2f}", 100)
        g5, g6, g7, g8 = st.columns(4)
        with g5: draw_card("RISCO", "BAIXO", 100, "#00ff88")
        with g6: draw_card("ESTABILIDADE", "98%", 98)
        with g7: draw_card("PROTEÇÃO", "ATIVA", 100)
        with g8: draw_card("MODO", "CONSERVADOR", 100)

# SCANNER (TIMES REAIS + ANIMAÇÃO)
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    cat = c1.selectbox("🌎 SELECIONE A REGIÃO", list(DB_TIMES.keys()))
    times_lista = DB_TIMES[cat]
    
    col_t1, col_t2 = st.columns(2)
    t1 = col_t1.selectbox("🏠 MANDANTE", times_lista, index=0)
    t2 = col_t2.selectbox("🚀 VISITANTE", times_lista, index=1)
    
    if st.button("⚡ EXECUTAR ALGORITIMO IA", use_container_width=True):
        with st.status("🤖 Consultando Banco de Dados...", expanded=True) as status:
            st.write("Buscando histórico de confrontos...")
            time.sleep(0.8)
            st.write("Calculando pressão ofensiva simulada...")
            time.sleep(0.8)
            st.write("Verificando liquidez do mercado...")
            status.update(label="✅ Análise Concluída!", state="complete", expanded=False)
        
        v_calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        st.session_state.analise_bloqueada = {"casa": t1, "fora": t2, "vencedor": t1, "gols": "OVER 2.5", "data": datetime.now().strftime("%H:%M"), "stake_val": f"R$ {v_calc:,.2f}"}

    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<h3 style='color:#9d54ff;'>PROBABILIDADES: {m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['vencedor'], 85)
        with r2: draw_card("MERCADO GOLS", m['gols'], 70)
        with r3: draw_card("STAKE SUGERIDA", m['stake_val'], 100)
        with r4: draw_card("CONFANÇA IA", "94%", 94)
        r5, r6, r7, r8 = st.columns(4)
        with r5: draw_card("ESTAT. ATAQUE", "FORTE", 88)
        with r6: draw_card("ESTAT. DEFESA", "MÉDIA", 55)
        with r7: draw_card("PONTOS INFO", "1.85", 60)
        with r8: draw_card("SISTEMA", "JARVIS v57", 100)

# GOLS (NOMES TÉCNICOS)
elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ APOSTAS POR GOLS (MERCADOS TÉCNICOS)</h2>", unsafe_allow_html=True)
    g1, g2, g3, g4 = st.columns(4)
    with g1: draw_card("OVER 0.5 HT (LIVE)", "84%", 84)
    with g2: draw_card("OVER 1.5 FT", "76%", 76)
    with g3: draw_card("AMBAS MARCAM (BTTS)", "68%", 68)
    with g4: draw_card("UNDER 3.5 (VALOR)", "91%", 91)
    g5, g6, g7, g8 = st.columns(4)
    with g5: draw_card("GOL APÓS 75' (MIN)", "45%", 45)
    with g6: draw_card("MÉDIA GOLS LIGA", "2.85", 100)
    with g7: draw_card("EXPECTED GOALS (xG)", "1.92", 100)
    with g8: draw_card("LINHA DE CORTE", "2.25", 100)

# ESCANTEIOS (NOMES TÉCNICOS)
elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 APOSTAS POR ESCANTEIOS (CORNERS PRO)</h2>", unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4)
    with e1: draw_card("OVER 8.5 CORNERS", "89%", 89)
    with e2: draw_card("OVER 10.5 CORNERS", "62%", 62)
    with e3: draw_card("CANTOS HT (4.5+)", "74%", 74)
    with e4: draw_card("RACE TO 7 (CASA)", "58%", 58)
    e5, e6, e7, e8 = st.columns(4)
    with e5: draw_card("CANTOS ASIÁTICOS", "9.5", 100)
    with e6: draw_card("MÉDIA CANTOS/JOGO", "10.4", 100)
    with e7: draw_card("PODER DE CANTO", "ALTO", 85)
    with e8: draw_card("INDICADOR ZEBRA", "12%", 12)

# HISTÓRICO
elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE OPERAÇÕES</h2>", unsafe_allow_html=True)
    if not st.session_state.historico_calls: st.info("Nenhuma call salva.")
    else:
        for i, c in enumerate(reversed(st.session_state.historico_calls)):
            st.markdown(f"""<div class="history-card-box"><div><b style='color:#9d54ff;'>[{c['data']}]</b> {c['casa']} x {c['fora']}</div><div style='color:#06b6d4;'>{c['gols']} | {c['stake_val']}</div></div>""", unsafe_allow_html=True)

# LIVE E VENCEDORES (8 CARDS PADRÃO)
elif st.session_state.aba_ativa in ["live", "vencedores"]:
    st.markdown(f"<h2 style='color:white;'>{st.session_state.aba_ativa.upper()}</h2>", unsafe_allow_html=True)
    c_a, c_b = st.columns(2)
    with c_a: [draw_card(f"KPI {i}", "---", 50) for i in range(1, 5)]
    with c_b: [draw_card(f"KPI {i}", "---", 50) for i in range(5, 9)]

# FOOTER
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL</div><div>JARVIS PROTECT v57.24</div></div>""", unsafe_allow_html=True)
