import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v60.00 - INTEGRIDADE TOTAL]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO) - UI v57.35
# DIRETRIZ 5: CÓDIGO 100% ÍNTEGRO - SEM ABREVIAÇÕES
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
if 'top_20_ia' not in st.session_state: st.session_state.top_20_ia = []

# --- FUNÇÃO DE CARREGAMENTO DE DADOS ---
def carregar_dados(path):
    if os.path.exists(path):
        try: return pd.read_csv(path)
        except: return None
    return None

df_diario = carregar_dados("data/database_diario.csv")
df_hist = carregar_dados("data/historico_5_temporadas.csv")

# ==============================================================================
# LÓGICA DO BOT (BACK-END): MOTOR DE PROCESSAMENTO INVISÍVEL
# ==============================================================================

def calcular_analise_real(time_casa, time_fora):
    """
    IA JARVIS: Cruza sua escolha manual com o Big Data de 5 anos.
    """
    conf_base = 75.0
    palpite_gols = "OVER 1.5"
    
    if df_hist is not None:
        # Busca flexível (ignora maiúsculas/minúsculas)
        filtro = df_hist[df_hist['Casa'].str.contains(time_casa, case=False, na=False)]
        if not filtro.empty:
            jogos_total = len(filtro)
            vitorias_casa = len(filtro[filtro['Resultado'] == 'H'])
            taxa_win = (vitorias_casa / jogos_total) * 100
            conf_base = round(taxa_win + 10, 1)
            if conf_base > 98: conf_base = 98.4
    
    # Se o jogo estiver na Betano hoje, a IA valida como "Filé Mignon"
    luz = "🔴"
    motivo = "ALERTA: ESTATÍSTICA FRIA"
    if df_diario is not None:
        if any(df_diario['CASA'].str.contains(time_casa, case=False, na=False)):
            luz = "🟢"
            motivo = "FILÉ MIGNON: INFORMAÇÃO REAL"
            conf_base += 5

    return min(conf_base, 99.0), palpite_gols, luz, motivo

# ==============================================================================
# 2. CAMADA DE ESTILO CSS INTEGRAL (TRAVA DE SEGURANÇA v57.35)
# ==============================================================================
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
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important;}
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; padding-left: 35px !important; border-left: 3px solid #6d28d9 !important;}
    div.stButton > button:not([data-testid="stSidebar"] *) { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: #ffffff !important; border: none !important; padding: 15px 20px !important; font-weight: 900 !important; text-transform: uppercase !important; letter-spacing: 1.2px !important; border-radius: 6px !important; width: 100% !important; box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important; margin-top: 10px !important;}
    div[data-baseweb="input"], .stNumberInput div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    div[data-baseweb="select"] > div { background-color: #1a202c !important; color: white !important; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; }
    .banca-title-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px; display: flex; align-items: center; gap: 15px; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR
with st.sidebar:
    st.markdown("""<div class="betano-header"><div class="header-left"><div class="logo-link">GESTOR IA</div><div class="nav-links"><div class="nav-item">APOSTAS ESPORTIVAS</div><div class="nav-item">APOSTAS AO VIVO</div></div></div><div class="header-right"><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div></div><div style="height:65px;"></div>""", unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color_footer}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# 4. LÓGICA DE TELAS
# ==============================================================================

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    if df_diario is not None: st.dataframe(df_diario, use_container_width=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    db_paises = {"BRASIL": ["BRASILEIRÃO A", "BRASILEIRÃO B"], "INGLATERRA": ["PREMIER LEAGUE"], "ESPANHA": ["LA LIGA"], "INTERNACIONAL 🌍": ["E2", "SC1", "SP2"]}
    db_times = {"BRASILEIRÃO A": ["Flamengo", "Palmeiras", "Athletico-PR", "Atlético-MG"], "PREMIER LEAGUE": ["Man City", "Arsenal", "Liverpool"], "E2": ["Blackpool", "Reading", "Wigan"]}
    
    col_reg, col_grp, col_tm = st.columns(3)
    with col_reg: sel_p = st.selectbox("🌎 REGIÃO / PAÍS", list(db_paises.keys()))
    with col_grp: sel_l = st.selectbox("📂 GRUPO", db_paises[sel_p])
    with col_tm: sel_t = st.selectbox("🏠 TIME DA CASA", db_times.get(sel_l, ["Time A"]))
    
    if st.button("⚡ EXECUTAR ALGORITMO"):
        conf, gol, luz, txt = calcular_analise_real(sel_t, "Rival")
        st.session_state.analise_bloqueada = {"casa": sel_t, "conf": conf, "gol": gol, "luz": luz, "txt": txt}

    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<div style='background:rgba(255,255,255,0.03); border-left:5px solid #00ff88; padding:15px;'>{m['luz']} <b style='color:white;'>SISTEMA JARVIS:</b> <span style='color:#00ff88;'>{m['txt']}</span></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center; color:#9d54ff;'>{m['casa']} vs Rival</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", "ALTA PROB.", int(m['conf']))
        with r2: draw_card("GOLS", m['gol'], 90)
        with r3: draw_card("STAKE", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
        with r4: draw_card("CANTOS", "9.5+", 75)
        
        if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True):
            st.session_state.historico_calls.append({"data": datetime.now().strftime("%H:%M"), "casa": m['casa'], "fora": "Rival", "stake_val": f"R$ {10:,.2f}", "gols": m['gol']})
            st.toast("✅ CALL SALVA COM SUCESSO!")

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        df_l = df_diario[df_diario['PAIS'].str.contains("LIVE", na=False)]
        if df_l.empty: st.info("Buscando jogos ao vivo...")
        else: st.dataframe(df_l, use_container_width=True, hide_index=True)

elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🏆 VENCEDORES DA COMPETIÇÃO</h2>", unsafe_allow_html=True)
    v1, v2, v3, v4 = st.columns(4)
    with v1: draw_card("FAVORITO 1", "Brasil", 45)
    with v2: draw_card("FAVORITO 2", "França", 38)
    with v3: draw_card("FAVORITO 3", "Espanha", 25)
    with v4: draw_card("ZEBRA PROB", "Marrocos", 12)

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
    with e4: draw_card("CORNER RACE", "Time A", 55)

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    if not st.session_state.historico_calls: st.info("Nenhuma operação registrada.")
    else:
        for i, call in enumerate(reversed(st.session_state.historico_calls)):
            st.markdown(f"""<div class="history-card-box"><div style="color:white; font-weight:800;"><span style="color:#9d54ff;">[{call['data']}]</span> {call['casa']} x {call['fora']} <span style="color:#06b6d4; margin-left:20px;">{call['stake_val']} | {call['gols']}</span></div></div>""", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>""", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total))
    st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, float(st.session_state.stake_padrao))
    draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100, "#00d2ff")

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v60.0</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
