import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [COFRE VISUAL v58.7 - BLINDAGEM DE INTERFACE - NÃO ALTERAR ESTA SEÇÃO]
# ==============================================================================
def aplicar_layout_blindado():
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
        .logo-link:hover { filter: brightness(1.2); }
        .nav-links { display: flex; gap: 22px; align-items: center; }
        .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; opacity: 1 !important; font-weight: 600 !important; letter-spacing: 0.5px; transition: 0.3s ease; cursor: pointer; white-space: nowrap; }
        .nav-item:hover { color: #06b6d4 !important; transform: scale(1.05); }
        .header-right { display: flex; align-items: center; gap: 15px; }
        .search-lupa { color: #ffffff; font-size: 15px; cursor: pointer; transition: 0.3s; }
        .search-lupa:hover { color: #9d54ff; transform: scale(1.2); }
        .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; transition: 0.3s ease; cursor: pointer; }
        .registrar-pill:hover { background: white !important; color: #001a4d !important; }
        .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; transition: 0.3s ease; cursor: pointer; }
        .entrar-grad:hover { filter: brightness(1.15); box-shadow: 0 0 15px rgba(109, 40, 217, 0.4); }
        [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
        [data-testid="stSidebarContent"] { overflow: hidden !important; }
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
        section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important; transition: all 0.2s ease !important; white-space: nowrap !important; }
        section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; padding-left: 35px !important; border-left: 3px solid #6d28d9 !important; }
        div.stButton > button:not([data-testid="stSidebar"] *) { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: #ffffff !important; border: none !important; padding: 15px 20px !important; font-weight: 900 !important; text-transform: uppercase !important; letter-spacing: 1.2px !important; border-radius: 6px !important; width: 100% !important; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important; box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important; margin-top: 10px !important; transform: translate3d(0,0,0); }
        div.stButton > button:not([data-testid="stSidebar"] *):hover { transform: translateY(-2px) !important; filter: brightness(1.2) !important; box-shadow: 0 8px 25px rgba(109, 40, 217, 0.5) !important; }
        div[data-baseweb="input"], .stNumberInput div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
        div[data-baseweb="input"] input { background-color: #1a202c !important; color: white !important; }
        div[data-baseweb="select"] > div { background-color: #1a202c !important; color: white !important; }
        .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; transition: all 0.3s ease; transform: translate3d(0,0,0); }
        .highlight-card:hover { transform: translateY(-5px); border-color: #6d28d9; box-shadow: 0 10px 20px rgba(0,0,0,0.4); }
        .banca-title-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px; display: flex; align-items: center; gap: 15px; }
        .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }
        .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("""<div class="betano-header"><div class="header-left"><a href="?go=home" class="logo-link">GESTOR IA</a></div><div class="header-right"><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div></div><div style="height:65px;"></div>""", unsafe_allow_html=True)

# 1. CONFIGURAÇÃO
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")
aplicar_layout_blindado()

# --- MEMÓRIA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# --- DADOS ---
def carregar_jogos_diarios():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try: return pd.read_csv(path)
        except: return None
    return None
df_diario = carregar_jogos_diarios()

# --- NAVEGAÇÃO ---
with st.sidebar:
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color_footer}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# ==============================================================================
# [TELA: SCANNER PRÉ-LIVE - LISTA COMPLETA DE CAMPEONATOS]
# ==============================================================================
if st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    # 1. DEFINIÇÃO DA ESTRUTURA DE CATEGORIAS E LIGAS
    db_competicoes = {
        "BRASIL": ["BRASILEIRÃO SÉRIE A", "BRASILEIRÃO SÉRIE B", "BRASILEIRÃO SÉRIE C", "BRASILEIRÃO SÉRIE D", "BRASILEIRÃO SUB-20", "CARIOQUÃO", "PAULISTÃO", "MINEIRO", "GAÚCHO", "PARANAENSE", "CATARINENSE", "COPA DO BRASIL", "COPA DO NORDESTE", "COPA SUL-SUDESTE", "COPA VERDE"],
        "INGLATERRA": ["PREMIER LEAGUE", "COPA DA LIGA INGLESA", "COPA DA INGLATERRA"],
        "ESPANHA": ["LA LIGA", "COPA DO REI"],
        "ITÁLIA": ["CAMPEONATO ITALIANO", "COPA DA ITÁLIA"],
        "ALEMANHA": ["BUNDESLIGA", "COPA DA ALEMANHA"],
        "FRANÇA": ["CAMPEONATO FRANCÊS", "COPA DA FRANÇA"],
        "INTERNACIONAL (UEFA)": ["CHAMPIONS LEAGUE", "LIGA EUROPA", "LIGA CONFERÊNCIA"],
        "SELEÇÕES / MUNDIAL": ["COPA DO MUNDO 2026", "ELIMINATÓRIAS EUROPA", "REPESCAGEM MUNDIAL"],
        "ÁSIA / ARÁBIA": ["CAMPEONATO SAUDITA", "CHAMPIONS LEAGUE DA ÁSIA"],
        "BASE / JOVENS": ["SUL-AMERICANO SUB 17"]
    }

    # 2. DEFINIÇÃO DE TIMES (TOP TIMES POR REGIÃO)
    db_times = {
        "BRASIL": ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Fluminense", "Vasco", "Grêmio", "Inter", "Atlético-MG", "Cruzeiro", "Botafogo", "Bahia", "Athletico-PR", "Santos"],
        "INGLATERRA": ["Man City", "Arsenal", "Liverpool", "Man United", "Chelsea", "Tottenham", "Aston Villa"],
        "ESPANHA": ["Real Madrid", "Barcelona", "Atlético Madrid", "Sevilla", "Real Sociedad"],
        "ITÁLIA": ["Inter", "Milan", "Juventus", "Napoli", "Roma", "Lazio", "Atalanta"],
        "ALEMANHA": ["Bayern", "Leverkusen", "Dortmund", "RB Leipzig"],
        "FRANÇA": ["PSG", "Monaco", "Marseille", "Lyon"],
        "INTERNACIONAL (UEFA)": ["Real Madrid", "Man City", "Bayern", "PSG", "Inter", "Liverpool"],
        "SELEÇÕES / MUNDIAL": ["Brasil", "França", "Argentina", "Espanha", "Inglaterra", "Portugal", "Alemanha"],
        "ÁSIA / ARÁBIA": ["Al-Hilal", "Al-Nassr", "Al-Ittihad", "Al-Ahli"],
        "BASE / JOVENS": ["Brasil U17", "Argentina U17", "Uruguai U17", "Equador U17"]
    }

    c1, c2 = st.columns(2)
    with c1: sel_regiao = st.selectbox("🌎 REGIÃO / PAÍS", list(db_competicoes.keys()))
    with c2: sel_liga = st.selectbox("🏆 COMPETIÇÃO", db_competicoes[sel_regiao])

    c3, c4 = st.columns(2)
    with c3: t_casa = st.selectbox("🏠 TIME CASA", db_times.get(sel_regiao, ["Time A", "Time B"]))
    with c4: t_fora = st.selectbox("🚀 TIME FORA", [t for t in db_times.get(sel_regiao, ["Time A", "Time B"]) if t != t_casa])

    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        v_calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        st.session_state.analise_bloqueada = {
            "liga": sel_liga, "casa": t_casa, "fora": t_fora, "vencedor": "CASA",
            "gols": "OVER 1.5", "stake": f"R$ {v_calc:,.2f}", "cantos": "9.5+", "data": datetime.now().strftime("%H:%M")
        }

    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<h3 style='color:#9d54ff; text-align:center; margin-top:20px;'>{m['casa']} vs {m['fora']} ({m['liga']})</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['vencedor'], 85)
        with r2: draw_card("GOLS", m['gols'], 70)
        with r3: draw_card("STAKE", m['stake'], 100)
        with r4: draw_card("CANTOS", m['cantos'], 65)
        if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True):
            st.session_state.historico_calls.append(m.copy())
            st.toast("✅ CALL SALVA NO HISTÓRICO!")

# ==============================================================================
# [OUTRAS TELAS]
# ==============================================================================
elif st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE", "92.4%", 92); with h3: draw_card("SUGESTÃO", "OVER 2.5", 88); with h4: draw_card("IA STATUS", "ONLINE", 100)
    if df_diario is not None: st.dataframe(df_diario, use_container_width=True)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
    st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, st.session_state.stake_padrao)

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    if not st.session_state.historico_calls: st.info("Nenhuma call salva.")
    else:
        for call in reversed(st.session_state.historico_calls):
            st.markdown(f"""<div class="history-card-box"><div style="color:white;"><b>[{call['data']}]</b> {call['casa']} x {call['fora']} <span style="color:#64748b; font-size:10px;">({call['liga']})</span> | <span style="color:#06b6d4;">{call['stake']}</span> | {call['gols']}</div></div>""", unsafe_allow_html=True)

else:
    st.markdown(f"<h2 style='color:white;'>{st.session_state.aba_ativa.upper()}</h2>", unsafe_allow_html=True)
    st.info("Processando dados...")

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v58.7</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
