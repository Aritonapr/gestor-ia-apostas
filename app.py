import streamlit as st
import pandas as pd
import os
import random
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v59.6 - RESTAURAÇÃO TOTAL E BLINDAGEM PIT]
# DIRETRIZ 1: HEADER INTEGRAL NA SIDEBAR (DESIGN BETANO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO) - UI v58.8
# DIRETRIZ 5: PROTOCOLO PIT - INTEGRIDADE TOTAL DE CÓDIGO (SEM ABREVIAÇÕES)
# DIRETRIZ 6: BLOCO GEOGRÁFICO BLINDADO - NÃO ALTERAR SEM COMANDO ESPECÍFICO
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# [ INÍCIO DO BLOCO DE DADOS GEOGRÁFICOS - BLINDAGEM DE INTEGRIDADE ]
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

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# [ FIM DO BLOCO DE DADOS GEOGRÁFICOS ]
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# --- MECANISMO IA JARVIS (BILHETE OURO) ---
def engine_bilhete_ouro():
    bilhetes = []
    paises_keys = list(db_times.keys())
    for i in range(20):
        p = random.choice(paises_keys)
        t1, t2 = random.sample(db_times[p], 2)
        confia = random.randint(82, 99)
        bilhetes.append({
            "jogo": f"{t1} vs {t2}", "winner": f"{confia}% - {t1}", "gols": "Over 2.5",
            "cartoes": f"T: {random.randint(4,6)} | HT: 1", "cantos": "9.5+", "meta": "16+",
            "chutes": "10+", "defesas": "5+", "ia": f"{confia}%"
        })
    return bilhetes

# --- CARREGAMENTO DE DADOS ---
def carregar_jogos_diarios():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try: return pd.read_csv(path)
        except: return None
    return None
df_diario = carregar_jogos_diarios()

# 2. CAMADA DE ESTILO CSS INTEGRAL (UI v58.8 COMPLETA)
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
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; cursor: pointer;}
    .nav-links { display: flex; gap: 22px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600 !important; transition: 0.3s; cursor: pointer; white-space: nowrap; }
    .nav-item:hover { color: #06b6d4 !important; }

    .header-right { display: flex; align-items: center; gap: 15px; }
    .search-lupa { color: #ffffff; font-size: 15px; cursor: pointer; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; cursor: pointer; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; cursor: pointer; }

    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important;
        border-radius: 6px !important; width: 100% !important; 
        box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important;
    }

    div[data-baseweb="input"], div[data-baseweb="select"] > div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; }
    .banca-title-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px; display: flex; align-items: center; gap: 15px; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }
    .bilhete-ouro-box { background: rgba(109, 40, 217, 0.03); border: 1px solid #1e293b; border-left: 4px solid #9d54ff; padding: 15px; border-radius: 8px; margin-bottom: 12px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER INTEGRAL
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <a href="?go=home" class="logo-link">GESTOR IA</a>
                <div class="nav-links">
                    <div class="nav-item">APOSTAS ESPORTIVAS</div>
                    <div class="nav-item">APOSTAS AO VIVO</div>
                    <div class="nav-item">APOSTAS ENCONTRADAS</div>
                    <div class="nav-item">ESTATÍSTICAS AVANÇADAS</div>
                    <div class="nav-item">MERCADO PROBABILÍSTICO</div>
                    <div class="nav-item">ASSERTIVIDADE IA</div>
                </div>
            </div>
            <div class="header-right">
                <div class="search-lupa">🔍</div>
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
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color_footer}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- LÓGICA DE TELAS ---

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with h3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with h4: draw_card("IA STATUS", "ONLINE", 100)
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("VOL. GLOBAL", "ALTO", 75)
    with h6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with h7: draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
    with h8: draw_card("SISTEMA", "JARVIS v59.6", 100)
    
    st.markdown("### 📋 ANÁLISE DETALHADA (7 NÍVEIS)")
    bilhetes = engine_bilhete_ouro()
    c_b_1, c_b_2 = st.columns(2)
    for i, b in enumerate(bilhetes):
        target = c_b_1 if i % 2 == 0 else c_b_2
        with target:
            st.markdown(f"""<div class="bilhete-ouro-box"><div style="color:#06b6d4; font-size:9px; font-weight:900;">JOGO {i+1} | CONFIA: {b['ia']}</div><div style="color:white; font-size:15px; font-weight:800; margin:5px 0;">{b['jogo']}</div><div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px; font-size:10px; color:#94a3b8;"><div>WIN: <b style="color:white;">{b['winner']}</b></div><div>GOLS: <b style="color:white;">{b['gols']}</b></div><div>CARD: <b style="color:white;">{b['cartoes']}</b></div><div>CANTOS: <b style="color:white;">{b['cantos']}</b></div><div>META: <b style="color:white;">{b['meta']}</b></div><div>CHUTES: <b style="color:white;">{b['chutes']}</b></div><div style="grid-column: span 2;">DEFESAS: <b style="color:white;">{b['defesas']}</b></div></div></div>""", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    row_f = st.columns(3)
    with row_f[0]: sel_pais = st.selectbox("🌎 REGIÃO / PAÍS", list(db_paises.keys()))
    with row_f[1]: sel_grupo = st.selectbox("📂 GRUPO", db_paises[sel_pais])
    with row_f[2]: sel_comp = st.selectbox("🏆 COMPETIÇÃO", db_ligas.get(sel_grupo, ["Geral"]))
    st.markdown("<h4 style='color:white; margin-top:15px;'>⚔️ DEFINIR CONFRONTO</h4>", unsafe_allow_html=True)
    lista_base = sorted(db_times.get(sel_pais, ["Time A", "Time B"]))
    c1, c2 = st.columns(2)
    with c1: t_casa = st.selectbox("🏠 TIME DA CASA", lista_base + ["(Outro)"])
    with c2: t_fora = st.selectbox("🚀 TIME DE FORA", [t for t in lista_base if t != t_casa] + ["(Outro)"])

    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        st.session_state.analise_bloqueada = {"casa": t_casa, "fora": t_fora, "vencedor": "ALTA PROB", "gols": "OVER 1.5", "data": datetime.now().strftime("%H:%M"), "stake_val": f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", "luz": "🟢", "motivo": "IA CONFIRMADA", "cor": "#00ff88"}
    
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<div style='border-left: 5px solid {m['cor']}; padding:15px; background:rgba(255,255,255,0.02); color:white; margin-top:20px;'>{m['luz']} <b>JARVIS:</b> {m['motivo']}</div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color:#9d54ff; text-align:center;'>{m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['vencedor'], 85)
        with r2: draw_card("GOLS", m['gols'], 70)
        with r3: draw_card("STAKE", m['stake_val'], 100)
        with r4: draw_card("CANTOS", "9.5+", 65)
        if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True):
            st.session_state.historico_calls.append(m.copy()); st.toast("✅ CALL SALVA!")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>""", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
    st.session_state.stake_padrao = st.slider("STAKE POR OPERAÇÃO (%)", 0.1, 10.0, st.session_state.stake_padrao)

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    if not st.session_state.historico_calls: st.info("Vazio.")
    else:
        for i, call in enumerate(reversed(st.session_state.historico_calls)):
            idx = len(st.session_state.historico_calls) - 1 - i
            c_info, c_del = st.columns([0.9, 0.1])
            with c_info: st.markdown(f"""<div class="history-card-box"><div style="color:white; font-weight:800;"><span style="color:#9d54ff;">[{call['data']}]</span> {call['casa']} x {call['fora']} <span style="color:#06b6d4; margin-left:20px;">{call['stake_val']}</span></div></div>""", unsafe_allow_html=True)
            with c_del: 
                if st.button("🗑️", key=f"del_{idx}"):
                    st.session_state.historico_calls.pop(idx); st.rerun()

elif st.session_state.aba_ativa == "vencedores": st.markdown("<h2 style='color:white;'>🏆 VENCEDORES</h2>", unsafe_allow_html=True)
elif st.session_state.aba_ativa == "gols": st.markdown("<h2 style='color:white;'>⚽ GOLS</h2>", unsafe_allow_html=True)
elif st.session_state.aba_ativa == "escanteios": st.markdown("<h2 style='color:white;'>🚩 ESCANTEIOS</h2>", unsafe_allow_html=True)
elif st.session_state.aba_ativa == "live": st.markdown("<h2 style='color:white;'>📡 LIVE</h2>", unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v59.6</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
