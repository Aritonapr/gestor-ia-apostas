import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v7.0]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS DE ENGENHARIA SUPREMA (BLINDAGEM TOTAL CONTRA ALTERAÇÕES) ---
st.markdown("""
    <style>
    /* 1. ELIMINAÇÃO DE ELEMENTOS PADRÃO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    /* 2. SIDEBAR MILIMÉTRICA (TRAVADA) */
    [data-testid="stSidebar"] { 
        background-color: #15191d !important; 
        margin-top: 50px !important; 
        width: 260px !important; 
        min-width: 260px !important;
        border-right: 1px solid #2d3843 !important;
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }
    
    /* ALINHAMENTO SUPERIOR (-35PX) */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; margin-top: -35px !important; }

    /* 3. NAVBAR SUPERIOR PROFISSIONAL */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    .nav-items { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    @keyframes pulse-hex { 0%, 100% { transform: scale(0.8); opacity: 0.8; } 50% { transform: scale(1.1); opacity: 1; } }
    .logo-hex { width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px; animation: pulse-hex 2s infinite ease-in-out; }

    /* 4. DESIGN DOS BOTÕES GÊMEOS (CÁPSULAS LARANJAS) */
    /* Este seletor ataca todos os botões principais para garantir que fiquem idênticos */
    
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    @keyframes plasma-glow { 0%, 100% { box-shadow: 0 0 5px #f64d23; } 50% { box-shadow: 0 0 20px #f64d23; } }

    /* SELETOR MESTRE PARA OS BOTÕES LARANJAS */
    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button,
    .main .stButton button {
        background-color: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        height: 52px !important;
        width: 100% !important;
        max-width: 280px !important;
        border: none !important;
        font-weight: 900 !important;
        font-size: 13px !important;
        text-transform: uppercase !important;
        position: relative !important;
        overflow: hidden !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        animation: plasma-glow 3s infinite ease-in-out !important;
        margin-bottom: 15px !important;
    }

    /* REMOÇÃO ABSOLUTA DO QUADRADO BRANCO/CINZA AO PASSAR O MOUSE */
    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button:hover,
    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button:active,
    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button:focus,
    .main .stButton button:hover,
    .main .stButton button:active,
    .main .stButton button:focus {
        background-color: #f64d23 !important;
        color: white !important;
        border: none !important;
        outline: none !important;
        box-shadow: 0 0 30px #f64d23 !important;
        border-radius: 50px !important;
    }

    /* SCANNER LASER NOS BOTÕES GÊMEOS */
    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button::after,
    .main .stButton button::after {
        content: "" !important; position: absolute; top: 0; left: -100%; width: 80px; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important;
        animation: laser-scan 2.5s infinite linear !important;
        transform: skewX(-20deg);
    }

    /* 5. BOTÕES DE CATEGORIA (ESTILO MENU) */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:not(:first-child) button {
        background-color: transparent !important;
        color: #e2e8f0 !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        font-weight: 700 !important;
        font-size: 11px !important;
        padding: 12px 15px !important;
        width: 100% !important;
        border-radius: 0px !important;
        text-transform: uppercase;
    }

    /* 6. TÍTULOS E LABELS */
    .white-title { color: white !important; font-weight: 900; font-size: 26px !important; margin-bottom: 25px !important; }
    .standard-text { color: #e2e8f0 !important; font-weight: 700; font-size: 18px !important; margin-top: 15px !important; }
    
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR (FIXADA) ---
st.markdown(f"""
    <div class="betano-header">
        <div class="logo-hex"></div>
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-items">
            <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Apostas Encontradas</span><span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:12px; align-items:center;">
            <div style="border:1px solid #adb5bd; color:white; padding:4px 12px; border-radius:3px; font-size:11px; font-weight:bold; cursor:pointer;">REGISTRAR</div>
            <button style="background:#00cc66; color:white; padding:6px 20px; border-radius:3px; font-weight:bold; border:none; font-size:11px; cursor:pointer;">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS INTEGRAL (RESTAURADO) ---
db_global = {
    "BR COMPETIÇÕES BRASILEIRAS": {
        "Brasileirão": ["Série A", "Série B", "Série C", "Série D"],
        "Copas Nacionais": ["Copa do Brasil", "Supercopa do Brasil"],
        "Estaduais": ["Paulistão", "Carioca", "Mineiro", "Gaúcho"],
        "Regionais": ["Copa do Nordeste", "Copa Verde"]
    },
    "EU ELITE EUROPEIA (BIG 5)": {
        "Inglaterra": ["Premier League"], "Espanha": ["La Liga"], "Alemanha": ["Bundesliga"], "Itália": ["Serie A"], "França": ["Ligue 1"]
    },
    "🌎 AMÉRICAS (SUL / CENTRAL)": {
        "Continental": ["Copa Libertadores", "Copa Sul-Americana"], "Nacionais": ["Liga MX", "Liga Profesional ARG"]
    },
    "🏆 TORNEIOS INTERNACIONAIS": {
        "UEFA": ["Champions League", "Europa League"], "Mundial": ["Mundial de Clubes FIFA"]
    }
}

# TIMES SINCRONIZADOS
times_db = {
    "Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Internacional", "Cruzeiro", "Bahia", "Vasco", "Atlético-MG"],
    "Série B": ["Santos", "Sport", "Novorizontino", "Mirassol", "Ceará", "Goiás", "Coritiba"],
    "Série C": ["Náutico", "Remo", "ABC", "CSA", "Figueirense"],
    "Série D": ["Santa Cruz", "Brasil de Pelotas", "Maringá"],
    "Carioca": ["Flamengo", "Vasco", "Fluminense", "Botafogo"],
    "Gaúcho": ["Grêmio", "Internacional", "Juventude", "Caxias"],
    "Copa do Nordeste": ["Fortaleza", "Bahia", "Sport", "Vitória", "Ceará", "CRB"],
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Chelsea", "Tottenham"],
    "Serie A": ["Inter de Milão", "Milan", "Juventus", "Atalanta", "Napoli"],
    "Bundesliga": ["Bayer Leverkusen", "Bayern Munich", "Dortmund"],
    "Ligue 1": ["PSG", "Monaco", "Lille", "Nice"]
}

# --- SIDEBAR ---
with st.sidebar:
    if st.button("FERRAMENTA IA"): st.session_state.app_state = "processar"
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL (COCKPIT) ---
if "app_state" not in st.session_state: st.session_state.app_state = "home"

if st.session_state.app_state == "processar":
    st.markdown('<div class="white-title">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1: reg_sel = st.selectbox("SELECIONE A REGIÃO", list(db_global.keys()))
    with c2: cat_sel = st.selectbox("CATEGORIA", list(db_global[reg_sel].keys()))
    with c3: comp_sel = st.selectbox("CAMPEONATO", db_global[reg_sel][cat_sel])

    st.divider()
    st.markdown(f'<div class="standard-text">Confronto: {comp_sel}</div>', unsafe_allow_html=True)
    
    elenco = times_db.get(comp_sel, [f"Time A ({comp_sel})", f"Time B ({comp_sel})"])
    t1, t2 = st.columns(2)
    with t1: casa = st.selectbox("TIME CASA", elenco)
    with t2: fora = st.selectbox("TIME FORA", [t for t in elenco if t != casa])

    if st.button("PROCESSAR ALGORITMO"):
        with st.status("GIAE IA: Processando métricas...", expanded=True) as s:
            time.sleep(1.2); s.update(label="analise de algoritimo concluida", state="complete")
        st.success(f"🤖 Análise métrica de {casa} vs {fora} finalizada.")
else:
    st.markdown("### 🤖 Cockpit de Comando Ativado")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN GÊMEOS V7.0 BLINDADO</div><div>GESTOR IA PRO v7.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
