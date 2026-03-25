import streamlit as st
import pandas as pd
import os
import unicodedata
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v58.50 - RESTAURAÇÃO INTEGRAL PIT]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO) - MANTER UI v57.35
# DIRETRIZ 5: PROTOCOLO PIT - INTEGRIDADE TOTAL DE CÓDIGO
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

# --- FUNÇÃO AUXILIAR: NORMALIZAR TEXTO (Busca cega a acentos) ---
def normalizar_identificador(texto):
    if not texto: return ""
    texto = str(texto).strip().upper()
    nfkd_form = unicodedata.normalize('NFKD', texto)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

# --- FUNÇÃO DE CARREGAMENTO DE DADOS ---
def carregar_jogos_diarios():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            df.columns = df.columns.str.strip().str.upper()
            return df
        except:
            return None
    return None

df_diario = carregar_jogos_diarios()

# 2. CAMADA DE ESTILO CSS INTEGRAL (MANTIDA 100% DA v57.35)
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
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600 !important; letter-spacing: 0.5px; cursor: pointer; white-space: nowrap;}
    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; cursor: pointer;}
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; cursor: pointer;}

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
        width: 100% !important; box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important; margin-top: 10px !important;
    }
    div[data-baseweb="input"], .stNumberInput div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
    }
    .banca-title-banner {
        background-color: #003399 !important; padding: 15px 25px; border-radius: 5px;
        color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px;
    }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <a href="?go=home" class="logo-link">GESTOR IA</a>
                <div class="nav-links">
                    <div class="nav-item">APOSTAS ESPORTIVAS</div>
                    <div class="nav-item">APOSTAS AO VIVO</div>
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
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    p_val = 100.0
    try: p_val = float(str(perc).replace('%',''))
    except: pass
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;">
                <div style="background:{color_footer}; height:100%; width:{p_val}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- LÓGICA DE TELAS ---

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with h3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with h4: draw_card("IA STATUS", "ONLINE", 100, "#00ff88")
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("VOL. GLOBAL", "ALTO", 75)
    with h6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with h7: draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
    with h8: draw_card("SISTEMA", "JARVIS v58.50", 100)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>""", unsafe_allow_html=True)
    c_in, c_out = st.columns([1.2, 2.5])
    with c_in:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
        st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, st.session_state.stake_padrao)
    with c_out:
        draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100, "#00d2ff")

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    db_paises = {
        "BRASIL": ["BRASILEIRÃO", "CAMPEONATOS ESTADUAIS"],
        "INGLATERRA": ["PREMIER LEAGUE"],
        "ESPANHA": ["LA LIGA"],
        "ITÁLIA": ["SERIE A"],
        "ALEMANHA": ["BUNDESLIGA"],
        "FRANÇA": ["LIGUE 1"],
        "PORTUGAL": ["LIGA PORTUGAL"],
        "HOLANDA": ["EREDIVISIE"]
    }
    
    db_times = {
        "BRASIL": ["Flamengo", "Palmeiras", "Vasco", "São Paulo", "Corinthians", "Atlético-MG", "Cruzeiro", "Grêmio", "Inter"],
        "INGLATERRA": ["Man City", "Arsenal", "Liverpool", "Chelsea", "Man United"],
        "ESPANHA": ["Real Madrid", "Barcelona", "Atlético Madrid"],
        "ITÁLIA": ["Inter Milan", "AC Milan", "Juventus", "Napoli"],
        "ALEMANHA": ["Bayern", "Dortmund", "Leverkusen"],
        "FRANÇA": ["PSG", "Monaco", "Marseille"],
        "PORTUGAL": ["Benfica", "Porto", "Sporting"],
        "HOLANDA": ["Ajax", "PSV", "Feyenoord"]
    }

    row_f = st.columns(2)
    with row_f[0]: sel_pais = st.selectbox("🌎 PAÍS", list(db_paises.keys()))
    with row_f[1]: sel_comp = st.selectbox("🏆 COMPETIÇÃO", db_paises[sel_pais])

    # Unifica Times (CSV + Memória Interna)
    lista_base = db_times.get(sel_pais, ["Time A", "Time B"])
    csv_times = []
    if df_diario is not None:
        try:
            f_csv = df_diario[df_diario['PAÍS'].apply(normalizar_identificador) == normalizar_identificador(sel_pais)]
            csv_times = f_csv['TIME_CASA'].unique().tolist() + f_csv['TIME_FORA'].unique().tolist()
        except: pass
    
    lista_final = sorted(list(set(lista_base + csv_times)))

    c1, c2 = st.columns(2)
    with c1: t_casa = st.selectbox("🏠 CASA", lista_final)
    with c2: t_fora = st.selectbox("🚀 FORA", lista_final)

    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        res = {"vencedor": "Indefinido", "gols": "OVER 1.5", "cantos": "9.5+", "conf": "85%", "sis": "JARVIS v58.50"}
        
        if df_diario is not None:
            try:
                tc = normalizar_identificador(t_casa)
                tf = normalizar_identificador(t_fora)
                match = df_diario[(df_diario['TIME_CASA'].apply(normalizar_identificador) == tc) & (df_diario['TIME_FORA'].apply(normalizar_identificador) == tf)]
                if not match.empty:
                    res = {"vencedor": str(match['VENCEDOR_IA'].values[0]), "gols": str(match['GOLS_IA'].values[0]), "cantos": str(match['CANTOS_IA'].values[0]), "conf": str(match['CONF_IA'].values[0]), "sis": "SYNC: CSV"}
            except: pass

        st.session_state.analise_bloqueada = {
            "casa": t_casa, "fora": t_fora, "vencedor": res['vencedor'], "gols": res['gols'], 
            "data": datetime.now().strftime("%H:%M"), "stake_val": f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}",
            "cantos": res['cantos'], "conf": res['conf'], "sistema": res['sis']
        }
    
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<h3 style='color:#9d54ff; text-align:center;'>{m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['vencedor'], 85)
        with r2: draw_card("GOLS", m['gols'], 70)
        with r3: draw_card("STAKE", m['stake_val'], 100)
        with r4: draw_card("CANTOS", m['cantos'], 65)
        r5, r6, r7, r8 = st.columns(4)
        with r5: draw_card("IA CONF.", m['conf'], m['conf'])
        with r6: draw_card("PRESSÃO", "ALTA", 88)
        with r7: draw_card("TENDÊNCIA", "SUBINDO", 60)
        s_color = "#00ff88" if m['sistema'] == "SYNC: CSV" else "linear-gradient(90deg, #6d28d9, #06b6d4)"
        with r8: draw_card("SISTEMA", m['sistema'], 100, s_color)

elif st.session_state.aba_ativa in ["live", "vencedores", "gols", "escanteios"]:
    st.info(f"Módulo {st.session_state.aba_ativa.upper()} operacional. Aguardando dados de mercado.")

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    for call in reversed(st.session_state.historico_calls):
        st.markdown(f"""<div class="history-card-box"><div style="color:white; font-weight:800;">[{call['data']}] {call['casa']} x {call['fora']} | {call['gols']}</div></div>""", unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v58.50</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
