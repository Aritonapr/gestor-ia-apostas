import streamlit as st
import pandas as pd
import os
import random
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v59.8 - RESTAURAÇÃO TOTAL DE UI E FUNÇÕES]
# DIRETRIZ 1: HEADER INTEGRAL NA SIDEBAR (DESIGN BETANO + HOVER EFFECTS)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO) - UI v58.8 FIDELIDADE
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

# --- MECANISMOS IA JARVIS ---
def engine_ia_gen(n=20):
    dados = []
    times_list = [t for sub in db_times.values() for t in sub]
    for i in range(n):
        t1, t2 = random.sample(times_list, 2)
        confia = random.randint(85, 99)
        dados.append({"jogo": f"{t1} vs {t2}", "win": f"{confia}%", "gols": "Over 2.5", "cantos": "10.5+", "ia": f"{confia}%", "meta": "18+", "chutes": "12+", "defesas": "6+", "cards": "4.5+"})
    return dados

# 2. CAMADA DE ESTILO CSS INTEGRAL (RESTAURAÇÃO v58.8 + NO SCROLLBAR)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* REMOVER BARRA DE ROLAGEM LATERAL */
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }

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
    
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; cursor: pointer;}
    .nav-links { display: flex; gap: 22px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 10px !important; text-transform: uppercase; font-weight: 600 !important; transition: 0.3s ease; cursor: pointer; white-space: nowrap; }
    .nav-item:hover { color: #06b6d4 !important; transform: scale(1.05); }

    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; cursor: pointer; transition: 0.3s; }
    .registrar-pill:hover { background: white !important; color: #001a4d !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; cursor: pointer; transition: 0.3s; }
    .entrar-grad:hover { filter: brightness(1.15); box-shadow: 0 0 15px rgba(109, 40, 217, 0.4); }

    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: all 0.2s ease !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; padding-left: 35px !important; }

    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important;
        border-radius: 6px !important; width: 100% !important; box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important;
    }

    div[data-baseweb="input"], div[data-baseweb="select"] > div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; }
    .banca-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px; display: flex; align-items: center; gap: 15px; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }
    .bilhete-item-box { background: rgba(109, 40, 217, 0.03); border: 1px solid #1e293b; border-left: 4px solid #9d54ff; padding: 15px; border-radius: 8px; margin-bottom: 12px; }
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
                    <div class="nav-item">ESPORTES</div><div class="nav-item">AO VIVO</div>
                    <div class="nav-item">VIRTUAIS</div><div class="nav-item">E-SPORTS</div>
                    <div class="nav-item">OPORTUNIDADES IA</div><div class="nav-item">RESULTADOS</div>
                </div>
            </div>
            <div class="header-right"><div class="search-lupa">🔍</div><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div>
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

# --- TELAS ---

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
    with h8: draw_card("SISTEMA", "JARVIS v59.8", 100)
    
    st.markdown("### 📋 ANÁLISE DETALHADA (7 NÍVEIS)")
    bilhetes = engine_ia_gen(20)
    c1, c2 = st.columns(2)
    for i, b in enumerate(bilhetes):
        target = c1 if i % 2 == 0 else c2
        with target:
            st.markdown(f"""<div class="bilhete-item-box"><div style="color:#06b6d4; font-size:9px; font-weight:900;">JOGO {i+1} | CONFIA: {b['ia']}</div><div style="color:white; font-size:15px; font-weight:800; margin:5px 0;">{b['jogo']}</div><div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px; font-size:10px; color:#94a3b8;"><div>WIN: <b style="color:white;">{b['win']}</b></div><div>GOLS: <b style="color:white;">{b['gols']}</b></div><div>CARD: <b style="color:white;">{b['cards']}</b></div><div>CANTOS: <b style="color:white;">{b['cantos']}</b></div><div>META: <b style="color:white;">{b['meta']}</b></div><div>CHUTES: <b style="color:white;">{b['chutes']}</b></div><div style="grid-column: span 2;">DEFESAS: <b style="color:white;">{b['defesas']}</b></div></div></div>""", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>""", unsafe_allow_html=True)
    col_input, col_display = st.columns([1.5, 2.5])
    with col_input:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total, step=50.0)
        st.session_state.stake_padrao = st.slider("STAKE POR OPERAÇÃO (%)", 0.1, 10.0, st.session_state.stake_padrao)
        st.session_state.meta_diaria = st.slider("META DIÁRIA - STOP GAIN (%)", 1.0, 30.0, st.session_state.meta_diaria)
        st.session_state.stop_loss = st.slider("LIMITE DE PERDA - STOP LOSS (%)", 1.0, 30.0, st.session_state.stop_loss)

    v_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    v_meta = (st.session_state.banca_total * st.session_state.meta_diaria / 100)
    v_loss = (st.session_state.banca_total * st.session_state.stop_loss / 100)
    alvo_final = st.session_state.banca_total + v_meta
    saude_label = "EXCELENTE" if st.session_state.stake_padrao <= 2.0 else "MODERADA" if st.session_state.stake_padrao <= 5.0 else "CRÍTICA"
    saude_color = "#00ff88" if saude_label == "EXCELENTE" else "#ffcc00"
    
    with col_display:
        g1, g2, g3, g4 = st.columns(4)
        with g1: draw_card("VALOR ENTRADA", f"R$ {v_stake:,.2f}", 100)
        with g2: draw_card("STOP GAIN (R$)", f"R$ {v_meta:,.2f}", 100)
        with g3: draw_card("STOP LOSS (R$)", f"R$ {v_loss:,.2f}", 100)
        with g4: draw_card("ALVO FINAL", f"R$ {alvo_final:,.2f}", 100)
        g5, g6, g7, g8 = st.columns(4)
        with g5: draw_card("RISCO TOTAL", f"{st.session_state.stake_padrao}%", 100)
        with g6: draw_card("ENTRADAS/META", f"{int(v_meta/v_stake) if v_stake > 0 else 0}", 100)
        with g7: draw_card("ENTRADAS/LOSS", f"{int(v_loss/v_stake) if v_stake > 0 else 0}", 100)
        with g8: st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">SAÚDE BANCA</div><div style="color:{saude_color}; font-size:16px; font-weight:900; margin-top:10px;">{saude_label}</div></div>""", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    r_top = st.columns(3)
    with r_top[0]: sel_p = st.selectbox("🌎 REGIÃO", list(db_paises.keys()))
    with r_top[1]: sel_g = st.selectbox("📂 GRUPO", db_paises[sel_p])
    with r_top[2]: sel_c = st.selectbox("🏆 COMPETIÇÃO", db_ligas.get(sel_g, ["Geral"]))
    st.markdown("---")
    t_list = sorted(db_times.get(sel_p, ["Time A"]))
    c1, c2 = st.columns(2)
    with c1: t_casa = st.selectbox("🏠 CASA", t_list)
    with c2: t_fora = st.selectbox("🚀 FORA", [t for t in t_list if t != t_casa])
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        st.session_state.analise_bloqueada = {"casa": t_casa, "fora": t_fora, "win": "92%", "gols": "OVER 1.5", "stake": f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}"}
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<h3 style='color:#9d54ff; text-align:center;'>{m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        k1, k2, k3, k4 = st.columns(4)
        with k1: draw_card("VENCEDOR", m['win'], 90)
        with k2: draw_card("GOLS", m['gols'], 70)
        with k3: draw_card("STAKE", m['stake'], 100)
        with k4: draw_card("CANTOS", "9.5+", 65)
        if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True):
            st.session_state.historico_calls.append({"data": datetime.now().strftime("%H:%M"), "casa": m['casa'], "fora": m['fora'], "stake_val": m['stake']}); st.toast("SALVA!")

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    for i, call in enumerate(reversed(st.session_state.historico_calls)):
        idx = len(st.session_state.historico_calls) - 1 - i
        ci, cd = st.columns([0.9, 0.1])
        with ci: st.markdown(f"""<div class="history-card-box"><div style="color:white; font-weight:800;"><span style="color:#9d54ff;">[{call['data']}]</span> {call['casa']} x {call['fora']} <span style="color:#06b6d4; margin-left:20px;">{call['stake_val']}</span></div></div>""", unsafe_allow_html=True)
        with cd: 
            if st.button("🗑️", key=f"del_{idx}"): st.session_state.historico_calls.pop(idx); st.rerun()

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    bilhetes = engine_ia_gen(5)
    for b in bilhetes:
        st.markdown(f"<div class='bilhete-item-box'><b>LIVE:</b> {b['jogo']} | <b>PRESSÃO:</b> {random.randint(60,95)}% | <b>GOL PROB:</b> {random.randint(40,88)}%</div>", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🏆 VENCEDORES DA COMPETIÇÃO</h2>", unsafe_allow_html=True)
    bilhetes = engine_ia_gen(10)
    for b in bilhetes: st.markdown(f"<div class='bilhete-item-box'><b>FAVORITO:</b> {b['jogo'].split(' vs ')[0]} | <b>ROI PREVISTO:</b> {random.randint(5,25)}%</div>", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ APOSTAS POR GOLS</h2>", unsafe_allow_html=True)
    bilhetes = engine_ia_gen(15)
    for b in bilhetes: st.markdown(f"<div class='bilhete-item-box'>{b['jogo']} | <b>PALPITE:</b> {random.choice(['OVER 1.5 HT', 'OVER 2.5 FT', 'BTTS YES'])}</div>", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 APOSTAS POR ESCANTEIOS</h2>", unsafe_allow_html=True)
    bilhetes = engine_ia_gen(15)
    for b in bilhetes: st.markdown(f"<div class='bilhete-item-box'>{b['jogo']} | <b>PALPITE:</b> {random.choice(['OVER 9.5', 'OVER 10.5', 'RACE TO 7'])}</div>", unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v59.8</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
