import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v9.0] - ESTRUTURA BLINDADA
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- INJEÇÃO DE CÓDIGO FONTE SUPREMO (PRESERVAÇÃO TOTAL) ---
st.markdown("""
    <style>
    /* 1. LIMPEZA TOTAL DE INTERFACE */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    /* 2. SIDEBAR MILIMÉTRICA (260PX / TOP -35PX) */
    [data-testid="stSidebar"] { 
        background-color: #15191d !important; 
        margin-top: 50px !important; 
        width: 260px !important; 
        min-width: 260px !important;
        border-right: 1px solid #2d3843 !important;
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; margin-top: -35px !important; }

    /* 3. NAVBAR SUPERIOR PROFISSIONAL */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    .nav-items { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    @keyframes pulse-hex { 0%, 100% { transform: scale(0.9); } 50% { transform: scale(1.1); } }
    .logo-hex { width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px; animation: pulse-hex 2s infinite ease-in-out; }

    /* 4. BOTÕES GÊMEOS (CÁPSULAS LARANJAS) */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    @keyframes plasma-glow { 0%, 100% { box-shadow: 0 0 5px #f64d23; } 50% { box-shadow: 0 0 15px #f64d23; } }

    div.stButton > button, [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button {
        background-color: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        height: 50px !important;
        border: none !important;
        font-weight: 900 !important;
        font-size: 12px !important;
        text-transform: uppercase !important;
        position: relative !important;
        overflow: hidden !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        animation: plasma-glow 3s infinite ease-in-out !important;
        transition: none !important;
        text-align: center !important;
    }

    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button {
        width: 180px !important;
        margin: 10px auto 25px auto !important;
    }

    .main div.stButton > button {
        width: 280px !important;
        margin-top: 20px !important;
    }

    div.stButton > button::after, 
    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button::after {
        content: "" !important; position: absolute; top: 0; left: -100%; width: 70px; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important;
        animation: laser-scan 2.5s infinite linear !important;
        transform: skewX(-20deg);
    }

    div.stButton > button:hover, div.stButton > button:active, div.stButton > button:focus,
    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button:hover {
        background-color: #f64d23 !important;
        color: white !important;
        border: none !important;
        outline: none !important;
        box-shadow: 0 0 25px #f64d23 !important;
    }

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

    .white-title { color: white !important; font-weight: 900; font-size: 26px !important; margin-bottom: 25px !important; }
    .standard-text { color: #e2e8f0 !important; font-weight: 700; font-size: 18px !important; margin-top: 15px !important; }
    
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR (MANTIDA) ---
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

# --- BANCO DE DADOS (EXPANDIDO PARA COPA DO BRASIL) ---
db_global = {
    "BR COMPETIÇÕES BRASILEIRAS": {
        "Copas Nacionais": ["Copa do Brasil", "Supercopa do Brasil"],
        "Brasileirão": ["Série A", "Série B", "Série C", "Série D"],
        "Estaduais": ["Paulistão", "Carioca", "Mineiro", "Gaúcho"]
    },
    "EU ELITE EUROPEIA (BIG 5)": {
        "Inglaterra": ["Premier League"], "Espanha": ["La Liga"], "Alemanha": ["Bundesliga"], "Itália": ["Serie A"], "França": ["Ligue 1"]
    }
}

times_db = {
    "Copa do Brasil": ["Flamengo", "Amazonas FC", "Bahia", "Grêmio", "Palmeiras", "Botafogo-SP", "Corinthians", "Atlético-MG", "São Paulo", "Vasco"],
    "Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Internacional", "Cruzeiro", "Bahia", "Vasco", "Atlético-MG"],
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Chelsea", "Tottenham"]
}

# --- SIDEBAR ---
with st.sidebar:
    if st.button("FERRAMENTA IA"): 
        st.session_state.app_state = "processar"
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")

# --- ÁREA CENTRAL ---
if "app_state" not in st.session_state: st.session_state.app_state = "home"

if st.session_state.app_state == "processar":
    st.markdown('<div class="white-title">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    # Foco automático na Copa do Brasil conforme solicitado
    with c1: reg_sel = st.selectbox("SELECIONE A REGIÃO", list(db_global.keys()), index=0)
    with c2: cat_sel = st.selectbox("CATEGORIA", list(db_global[reg_sel].keys()), index=0)
    with c3: comp_sel = st.selectbox("CAMPEONATO", db_global[reg_sel][cat_sel], index=0)

    st.divider()
    st.markdown(f'<div class="standard-text">Confronto: {comp_sel}</div>', unsafe_allow_html=True)
    
    elenco = times_db.get(comp_sel, ["Time A", "Time B"])
    t1, t2 = st.columns(2)
    with t1: casa = st.selectbox("TIME CASA", elenco, index=0)
    with t2: fora = st.selectbox("TIME FORA", [t for t in elenco if t != casa], index=1 if len(elenco)>1 else 0)

    if st.button("PROCESSAR ALGORITMO"):
        with st.status("GIAE IA: Analisando volitividade...", expanded=True) as s:
            time.sleep(1.5); s.update(label="ANÁLISE COPA DO BRASIL CONCLUÍDA", state="complete")
        
        st.success(f"🤖 GIAE PRO: {casa} vs {fora}")
        res1, res2, res3 = st.columns(3)
        res1.metric("Prob. Vitória", "74%" if casa == "Flamengo" else "52%", "ALTA")
        res2.metric("Tendência Gols", "Over 2.5", "88%")
        res3.metric("Escanteios", "11.5", "POWER INDEX")
else:
    st.markdown("### 🤖 Cockpit de Comando Ativado")
    st.info("Protocolo GIAE-PRIME-V9 operando em modo de espera. Aguardando input.")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DESIGN FINAL BLINDADO</div><div>GESTOR IA PRO v9.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
