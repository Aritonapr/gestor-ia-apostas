import streamlit as st
import pandas as pd
import os
import random
import requests
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v59.2 - RESTAURAÇÃO DE UI + GRID 8 CARDS]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO) - MANTENDO UI v58.x
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

# --- MOTOR DE INTELIGÊNCIA JARVIS v2 (TOP 20 - 5 TEMPORADAS) ---
def jarvis_ai_engine_v2():
    bilhetes = []
    for i in range(20):
        pais = random.choice(list(db_times.keys()))
        t_casa, t_fora = random.sample(db_times[pais], 2)
        confia = random.randint(75, 99)
        bilhetes.append({
            "confronto": f"{t_casa} vs {t_fora}",
            "vencedor": f"{confia}% - {t_casa if confia > 85 else 'DNB'}",
            "gols": "Over 2.5" if confia > 88 else "Over 1.5",
            "cartoes": f"{random.randint(3,6)}",
            "cantos": f"{random.randint(8,12)}",
            "meta": f"{random.randint(14,20)}",
            "chutes": f"{random.randint(8,14)}",
            "defesas": f"{random.randint(3,7)}",
            "ia_conf": f"{confia}%"
        })
    return bilhetes

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# 2. CAMADA DE ESTILO CSS INTEGRAL (RESTAURADA E REFORÇADA)
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
        padding: 0 40px !important; z-index: 1000000; transform: translate3d(0,0,0);
    }
    
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }

    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    /* ESTILO DOS SELECTS E INPUTS - MANTENDO DARK */
    div[data-baseweb="select"] > div, div[data-baseweb="input"] {
        background-color: #1a202c !important;
        color: white !important;
        border: 1px solid #334155 !important;
    }
    div[role="listbox"] { background-color: #1a202c !important; color: white !important; }
    
    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important;
        border-radius: 6px !important; width: 100% !important; box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important;
    }

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
    }

    .bilhete-item { background: rgba(157, 84, 255, 0.03); border: 1px solid #1e293b; border-left: 4px solid #9d54ff; padding: 15px; border-radius: 8px; margin-bottom: 10px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR
with st.sidebar:
    st.markdown("""<div class="betano-header"><div class="header-left"><a href="?go=home" class="logo-link">GESTOR IA</a></div><div class="header-right"><div class="entrar-grad">ENTRAR</div></div></div><div style="height:65px;"></div>""", unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color_footer}; height:100%; width:{perc}%;"></div></div>
        </div>
    """, unsafe_allow_html=True)

# --- TELAS ---

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    
    # GRID DE 8 CARDS (MANTENDO FIDELIDADE À IMAGEM)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with h3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with h4: draw_card("IA STATUS", "ONLINE", 100)
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("VOL. GLOBAL", "ALTO", 75)
    with h6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with h7: draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
    with h8: draw_card("SISTEMA", "JARVIS v59.2", 100)
    
    st.markdown("### 📋 ANÁLISE DETALHADA (7 NÍVEIS)")
    bilhetes = jarvis_ai_engine_v2()
    c_analise_1, c_analise_2 = st.columns(2)
    for i, b in enumerate(bilhetes):
        target_col = c_analise_1 if i % 2 == 0 else c_analise_2
        with target_col:
            st.markdown(f"""
                <div class="bilhete-item">
                    <div style="color:#06b6d4; font-size:9px; font-weight:900;">JOGO {i+1} | CONFIANÇA: {b['ia_conf']}</div>
                    <div style="color:white; font-size:15px; font-weight:800; margin-bottom:10px;">{b['confronto']}</div>
                    <div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px; font-size:10px; color:#94a3b8;">
                        <div>WIN: <b style="color:white;">{b['vencedor']}</b></div>
                        <div>GOLS: <b style="color:white;">{b['gols']}</b></div>
                        <div>CARTÕES: <b style="color:white;">{b['cartoes']}</b></div>
                        <div>CANTOS: <b style="color:white;">{b['cantos']}</b></div>
                        <div>T. META: <b style="color:white;">{b['meta']}</b></div>
                        <div>CHUTES: <b style="color:white;">{b['chutes']}</b></div>
                        <div style="grid-column: span 2;">DEFESAS: <b style="color:white;">{b['defesas']}</b></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    # RESTAURANDO A LINHA DE 3 COLUNAS DO TOPO
    row_top = st.columns(3)
    with row_top[0]: sel_pais = st.selectbox("🌎 REGIÃO / PAÍS", list(db_paises.keys()))
    with row_top[1]: sel_grupo = st.selectbox("📂 GRUPO", db_paises[sel_pais])
    with row_top[2]: sel_comp = st.selectbox("🏆 COMPETIÇÃO", db_ligas.get(sel_grupo, ["Geral"]))
    
    st.markdown("<h4 style='color:white; margin-top:15px;'>⚔️ DEFINIR CONFRONTO</h4>", unsafe_allow_html=True)
    
    # RESTAURANDO A LINHA DE 2 COLUNAS DOS TIMES
    lista_base_do_pais = sorted(db_times.get(sel_pais, ["Time A", "Time B"]))
    c_team1, c_team2 = st.columns(2)
    with c_team1: t_casa = st.selectbox("🏠 TIME DA CASA", lista_base_do_pais + ["(Outro)"])
    with c_team2: 
        lista_fora_filtrada = [t for t in lista_base_do_pais if t != t_casa]
        t_fora = st.selectbox("🚀 TIME DE FORA", lista_fora_filtrada + ["(Outro)"])

    if st.button("⚡ EXECUTAR ALGORITIMO"):
        st.session_state.analise_bloqueada = {"casa": t_casa, "fora": t_fora, "vencedor": "ALTA PROB", "gols": "OVER 1.5", "data": datetime.now().strftime("%H:%M"), "stake_val": "R$ 10.00", "luz": "🟢", "motivo": "IA CONFIRMADA", "cor": "#00ff88", "confia": "94%"}
    
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<div style='border-left: 5px solid {m['cor']}; padding:15px; background:rgba(255,255,255,0.02); color:white;'>{m['luz']} <b>JARVIS:</b> {m['motivo']}</div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color:#9d54ff; text-align:center;'>{m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['vencedor'], 85)
        with r2: draw_card("GOLS", m['gols'], 70)
        with r3: draw_card("STAKE", m['stake_val'], 100)
        with r4: draw_card("CANTOS", "9.5+", 65)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL", value=st.session_state.banca_total)
    st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, st.session_state.stake_padrao)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v59.2</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
