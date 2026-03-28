import streamlit as st
import pandas as pd
import os
import random
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE RECUPERAÇÃO v60.2 - REPARO TOTAL DE NAVEGAÇÃO E UI]
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# [ BLOCO DE DADOS GEOGRÁFICOS - INTEGRAL ]
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

db_paises = {
    "BRASIL": ["BRASILEIRÃO", "BRASILEIRÃO SUB-20", "CAMPEONATOS ESTADUAIS", "COPAS NACIONAIS / REGIONAIS"],
    "AMÉRICA DO SUL (CONMEBOL)": ["COPA LIBERTADORES", "COPA SUL-AMERICANA", "COPA AMÉRICA"],
    "INGLATERRA": ["PREMIER LEAGUE", "COPAS DA INGLATERRA"],
    "ESPANHA": ["LA LIGA", "COPA DO REI DA ESPANHA"],
    "ITÁLIA": ["CAMPEONATO ITALIANO", "COPA DA ITÁLIA"],
    "ALEMANHA": ["BUNDESLIGA", "COPA DA ALEMANHA"],
    "FRANÇA": ["CAMPEONATO FRANCÊS", "COPA DA FRANÇA"],
    "INTERNACIONAL (UEFA)": ["CHAMPIONS LEAGUE", "LIGA EUROPA", "LIGA CONFERÊNCIA", "EUROCOPA"],
    "ÁSIA": ["CAMPEONATO SAUDITA", "CHAMPIONS LEAGUE DA ÁSIA"],
    "SELEÇÕES / MUNDIAL": ["COPA DO MUNDO 2026", "ELIMINATÓRIAS DA COPA-EUROPA", "ELIMINATÓRIAS - REPESCAGEM", "MUNDIAL DE CLUBES"],
    "BASE / JOVENS": ["SUL-AMERICANO SUB 17"]
}

db_ligas = {
    "BRASILEIRÃO": ["Série A", "Série B", "Série C", "Série D"],
    "BRASILEIRÃO SUB-20": ["Temporada Regular", "Fase Final"],
    "CAMPEONATOS ESTADUAIS": ["Campeonato Carioca", "Campeonato Paulistano", "Campeonato Mineiro", "Campeonato Gaucho", "Campeonato Paranaense", "Campeonato Catarinense"],
    "COPAS NACIONAIS / REGIONAIS": ["Copa do Brasil", "Copa do Nordeste", "Copa Sul-Sudeste", "Copa Verde"],
    "COPA LIBERTADORES": ["Fase de Grupos", "Oitavas", "Quartas", "Semi", "Final"],
    "COPA SUL-AMERICANA": ["Fase de Grupos", "Mata-Mata"],
    "COPA AMÉRICA": ["Fase de Grupos", "Mata-Mata"],
    "PREMIER LEAGUE": ["Premier League (1ª Div)", "EFL Championship (2ª)"],
    "COPAS DA INGLATERRA": ["FA Cup (Copa da Inglaterra)", "EFL Cup (Copa da Liga Inglesa)"],
    "LA LIGA": ["Primeira Divisão"],
    "COPA DO REI DA ESPANHA": ["Fases Finais"],
    "CAMPEONATO ITALIANO": ["Serie A TIM"],
    "COPA DA ITÁLIA": ["Coppa Italia"],
    "BUNDESLIGA": ["1. Bundesliga"],
    "COPA DA ALEMANHA": ["DFB Pokal"],
    "CAMPEONATO FRANCÊS": ["Ligue 1"],
    "COPA DA FRANÇA": ["Coupe de France"],
    "CHAMPIONS LEAGUE": ["Fase de Grupos", "Mata-Mata"],
    "LIGA EUROPA": ["Fase de Grupos", "Mata-Mata"],
    "LIGA CONFERÊNCIA": ["Fase de Grupos", "Mata-Mata"],
    "EUROCOPA": ["Fase de Grupos", "Mata-Mata"],
    "CAMPEONATO SAUDITA": ["Saudi Pro League"],
    "CHAMPIONS LEAGUE DA ÁSIA": ["Champions League Ásia"],
    "COPA DO MUNDO 2026": ["Fase de Grupos", "Mata-Mata"],
    "ELIMINATÓRIAS DA COPA-EUROPA": ["Qualificação"],
    "ELIMINATÓRIAS - REPESCAGEM": ["Playoffs Intercontinentais"],
    "MUNDIAL DE CLUBES": ["Fase Final"],
    "SUL-AMERICANO SUB 17": ["Fase Final"]
}

db_times = {
    "BRASIL": ["Flamengo", "Palmeiras", "Vasco", "São Paulo", "Corinthians", "Fluminense", "Botafogo", "Grêmio", "Inter", "Atlético-MG", "Cruzeiro", "Santos", "Bahia", "Fortaleza", "Athletico-PR"],
    "AMÉRICA DO SUL (CONMEBOL)": ["Flamengo", "Palmeiras", "River Plate", "Boca Juniors", "Independiente", "LDU", "Peñarol", "Atlético-MG"],
    "INGLATERRA": ["Man City", "Arsenal", "Liverpool", "Chelsea", "Man United", "Tottenham", "Aston Villa", "Newcastle"],
    "ESPANHA": ["Real Madrid", "Barcelona", "Atlético Madrid", "Sevilla", "Real Sociedad"],
    "ITÁLIA": ["Inter Milan", "AC Milan", "Juventus", "Napoli", "Roma", "Lazio", "Atalanta"],
    "ALEMANHA": ["Bayern Munchen", "Bayer Leverkusen", "Borussia Dortmund", "RB Leipzig"],
    "FRANÇA": ["PSG", "Monaco", "Marseille", "Lyon", "Lille"],
    "ÁSIA": ["Al-Hilal", "Al-Nassr", "Al-Ittihad", "Al-Ahli"],
    "INTERNACIONAL (UEFA)": ["Real Madrid", "Man City", "Bayern", "PSG", "Inter Milan", "Liverpool"],
    "SELEÇÕES / MUNDIAL": ["Brasil", "França", "Argentina", "Inglaterra", "Espanha", "Portugal", "Alemanha", "Itália"],
    "BASE / JOVENS": ["Brasil U17", "Argentina U17", "Equador U17", "Uruguai U17"]
}

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

def engine_ia_gen(n=20):
    dados = []
    times_list = [t for sub in db_times.values() for t in sub]
    for i in range(n):
        t1, t2 = random.sample(times_list, 2)
        confia = random.randint(85, 99)
        dados.append({"jogo": f"{t1} vs {t2}", "win": f"{confia}%", "gols": "Over 2.5", "cantos": "10.5+", "ia": f"{confia}%", "meta": "18+", "chutes": "12+", "defesas": "6+", "cards": "4.5+"})
    return dados

# 2. CAMADA DE ESTILO CSS INTEGRAL
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 90px 40px 20px 40px !important; }
    
    /* REPARO DO HEADER - LOGO SEPARADO DO MENU */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.1); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 30px !important; z-index: 9999999;
    }
    .header-left { display: flex; align-items: center; }
    .logo-box { color: #9d54ff !important; font-weight: 900; font-size: 20px; text-transform: uppercase; margin-right: 60px; min-width: 150px; }
    .nav-links { display: flex; gap: 20px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 10px; text-transform: uppercase; font-weight: 600; cursor: pointer; white-space: nowrap; }
    
    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { color: #ffffff; font-size: 9px; font-weight: 800; border: 1.5px solid #ffffff; padding: 7px 18px; border-radius: 20px; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 8px 22px; border-radius: 5px; font-weight: 800; font-size: 9.5px; }

    /* SIDEBAR ESTILO BETANO */
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 16px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    /* BOTÕES DA TELA CENTRAL */
    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important; border-radius: 6px !important;
    }

    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; margin-bottom: 15px; }
    .bilhete-item-box { background: rgba(109, 40, 217, 0.05); border-left: 4px solid #9d54ff; padding: 15px; border-radius: 8px; margin-bottom: 12px; border: 1px solid #1e293b; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR FIXO
st.sidebar.markdown(f"""
    <div class="betano-header">
        <div class="header-left">
            <div class="logo-box">GESTOR IA</div>
            <div class="nav-links">
                <div class="nav-item">ESPORTES</div><div class="nav-item">AO VIVO</div>
                <div class="nav-item">VIRTUAIS</div><div class="nav-item">E-SPORTS</div>
                <div class="nav-item">OPORTUNIDADES IA</div><div class="nav-item">RESULTADOS</div>
            </div>
        </div>
        <div class="header-right"><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div>
    </div>
    <div style="height:70px;"></div>
""", unsafe_allow_html=True)

# 4. MENU LATERAL (BOTÕES)
with st.sidebar:
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc=100, color_val="white", bar_color="#06b6d4"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:{color_val}; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{bar_color}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- NAVEGAÇÃO ---

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}")
    with h2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with h3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with h4: draw_card("IA STATUS", "ONLINE", 100)
    
    st.markdown("### 📋 ANÁLISE DETALHADA (7 NÍVEIS)")
    bilhetes = engine_ia_gen(20)
    c1, c2 = st.columns(2)
    for i, b in enumerate(bilhetes):
        target = c1 if i % 2 == 0 else c2
        with target:
            st.markdown(f"""<div class="bilhete-item-box"><div style="color:#06b6d4; font-size:9px; font-weight:900;">JOGO {i+1} | CONFIA: {b['ia']}</div><div style="color:white; font-size:15px; font-weight:800; margin:5px 0;">{b['jogo']}</div><div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px; font-size:10px; color:#94a3b8;"><div>WIN: <b style="color:white;">{b['win']}</b></div><div>GOLS: <b style="color:white;">{b['gols']}</b></div><div>CANTOS: <b style="color:white;">{b['cantos']}</b></div><div>META: <b style="color:white;">{b['meta']}</b></div></div></div>""", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    r1, r2, r3 = st.columns(3)
    with r1: sel_p = st.selectbox("🌎 REGIÃO", list(db_paises.keys()))
    with r2: sel_g = st.selectbox("📂 GRUPO", db_paises[sel_p])
    with r3: sel_c = st.selectbox("🏆 COMPETIÇÃO", db_ligas.get(sel_g, ["Geral"]))
    st.markdown("---")
    t_list = sorted(db_times.get(sel_p, ["Time A"]))
    c1, c2 = st.columns(2)
    with c1: t_casa = st.selectbox("🏠 CASA", t_list)
    with c2: t_fora = st.selectbox("🚀 FORA", [t for t in t_list if t != t_casa])
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        st.session_state.analise_bloqueada = {"casa": t_casa, "fora": t_fora, "win": "94.2%", "gols": "OVER 1.5"}
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<h3 style='color:#9d54ff; text-align:center;'>{m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        if st.button("📥 SALVAR NO HISTÓRICO", use_container_width=True):
            st.session_state.historico_calls.append({"data": datetime.now().strftime("%H:%M"), "casa": m['casa'], "fora": m['fora']})
            st.toast("✅ CALL SALVA!")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
    st.write(f"Sua stake atual é de 1%: R$ {st.session_state.banca_total * 0.01:,.2f}")

elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ APOSTAS POR GOLS</h2>", unsafe_allow_html=True)
    for b in engine_ia_gen(15): st.markdown(f"<div class='bilhete-item-box'>{b['jogo']} | <b>PALPITE:</b> OVER 2.5 FT</div>", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 APOSTAS POR ESCANTEIOS</h2>", unsafe_allow_html=True)
    for b in engine_ia_gen(15): st.markdown(f"<div class='bilhete-item-box'>{b['jogo']} | <b>PALPITE:</b> OVER 9.5 CANTOS</div>", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO</h2>", unsafe_allow_html=True)
    for call in reversed(st.session_state.historico_calls):
        st.write(f"[{call['data']}] {call['casa']} x {call['fora']}")

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 AO VIVO</h2>", unsafe_allow_html=True)
    st.write("Scanner monitorando partidas em tempo real...")

elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🏆 VENCEDORES</h2>", unsafe_allow_html=True)
    st.write("Projeções de campeões por liga...")

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v60.2</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
