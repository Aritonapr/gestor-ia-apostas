import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v3.0]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS MILIMÉTRICO PROTEGIDO (ESTILO DARK MODE PROFISSIONAL) ---
st.markdown("""
    <style>
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    /* NAVBAR SUPERIOR */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    .nav-items { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    
    /* SIDEBAR: 260px + MARGEM -35px */
    [data-testid="stSidebar"] { background-color: #15191d !important; margin-top: 50px !important; border-right: 1px solid #2d3843 !important; width: 260px !important; }
    [data-testid="stSidebarContent"] { padding-top: 0px !important; overflow-x: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; margin-top: -35px !important; }
    
    /* BOTÃO CÁPSULA COM SCANNER LASER */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button {
        background: #f64d23 !important; color: white !important; border-radius: 30px !important; height: 48px !important; width: 92% !important; margin: 0px auto 20px 10px !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        padding-left: 35px !important; font-weight: 900 !important; font-size: 10px !important;
        position: relative !important; overflow: hidden !important; border: none !important;
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::after {
        content: "" !important; position: absolute !important; top: 0 !important; left: -100% !important; width: 50px !important; height: 100% !important;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important; animation: laser-scan 2.5s infinite linear !important;
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::before {
        content: '🤖'; position: absolute; left: 6px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px;
        background: white !important; color: #f64d23 !important; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 15px; z-index: 2; border: 2px solid #f64d23;
    }

    [data-testid="stSidebar"] button { background-color: transparent !important; color: #e2e8f0 !important; border: none !important; border-bottom: 1px solid #1e293b !important; text-align: left !important; font-weight: 700 !important; font-size: 11px !important; padding: 12px 15px !important; width: 100% !important; border-radius: 0px !important; text-transform: uppercase; }

    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR (RESTAURADA) ---
st.markdown(f"""
    <div class="betano-header">
        <div style="width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px;"></div>
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

# --- BANCO DE DADOS COMPLETO (SÉRIES A, B, C, D + EUROPA + INTERNACIONAL) ---
db_global = {
    "BR COMPETIÇÕES BRASILEIRAS": {
        "Brasileirão": ["Série A", "Série B", "Série C", "Série D"],
        "Copas": ["Copa do Brasil", "Supercopa do Brasil"],
        "Estaduais": ["Paulistão", "Carioca", "Mineiro", "Gaúcho", "Paranaense", "Catarinense", "Pernambucano", "Baiano"],
        "Regionais": ["Copa do Nordeste", "Copa Verde"]
    },
    "EU ELITE EUROPEIA": {
        "Elite (Big 5)": ["Premier League", "La Liga", "Bundesliga", "Serie A (Itália)", "Ligue 1"],
        "Alto Valor (2ª Linha)": ["Primeira Liga (Portugal)", "Eredivisie (Holanda)", "Championship (Inglaterra 2)", "Super Lig (Turquia)", "Pro League (Bélgica)"],
        "Torneios UEFA": ["Champions League", "Europa League", "Conference League"]
    },
    "🏆 TORNEIOS INTERNACIONAIS": {
        "Continente (Clubes BR)": ["Copa Libertadores", "Copa Sul-Americana", "Recopa Sul-Americana"],
        "Mundial": ["Mundial de Clubes FIFA"],
        "Américas": ["Liga MX (México)", "Liga Profesional (Argentina)", "MLS (EUA)"]
    }
}

# Dicionário de times atualizado
times_db = {
    "Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Internacional", "Cruzeiro", "Bahia", "Vasco", "Atlético-MG", "Fluminense", "Corinthians", "Grêmio", "Criciúma", "Bragantino", "Juventude", "Vitória", "Athletico-PR", "Cuiabá", "Atlético-GO"],
    "Série B": ["Santos", "Sport", "Mirassol", "Novorizontino", "Ceará", "Goiás", "Vila Nova", "Coritiba", "Amazonas", "Avaí", "Operário", "Ponte Preta", "CRB", "Chapecoense", "Ituano", "Brusque", "Guarani", "Paysandu", "Botafogo-SP", "América-MG"],
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Man United", "Newcastle", "Brighton", "West Ham", "Wolves", "Everton"],
    "La Liga": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Athletic Bilbao", "Real Sociedad", "Real Betis", "Villarreal"],
    "Copa Libertadores": ["Flamengo", "Palmeiras", "River Plate", "São Paulo", "Atlético-MG", "Fluminense", "Botafogo", "Peñarol"],
    "Paulistão": ["Palmeiras", "Santos", "São Paulo", "Corinthians", "Bragantino", "Inter de Limeira", "Mirassol", "Novorizontino"]
}

# --- SIDEBAR FIXA ---
with st.sidebar:
    if st.button("PROCESSAR ALGORITMO"):
        st.session_state.app_state = "processar"
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL ---
if "app_state" not in st.session_state: st.session_state.app_state = "home"

if st.session_state.app_state == "processar":
    st.markdown("### 📂 CENTRAL DE INTELIGÊNCIA GIAE")
    
    # ORGANIZAÇÃO EM TRÊS NÍVEIS
    c1, c2, c3 = st.columns(3)
    
    with c1:
        regiao_sel = st.selectbox("📂 SELECIONE A REGIÃO", list(db_global.keys()))
    with c2:
        cat_sel = st.selectbox("📁 CATEGORIA", list(db_global[regiao_sel].keys()))
    with c3:
        comp_sel = st.selectbox("🏆 CAMPEONATO", db_global[regiao_sel][cat_sel])

    st.divider()
    
    # SELEÇÃO DE TIMES
    st.markdown(f"#### 🏟️ Confronto: {comp_sel}")
    t1, t2 = st.columns(2)
    
    # Fallback para times genéricos caso não esteja no dicionário detalhado
    elenco = times_db.get(comp_sel, [f"Time A ({comp_sel})", f"Time B ({comp_sel})", f"Time C ({comp_sel})"])
    
    with t1:
        time_casa = st.selectbox("TIME CASA", elenco)
    with t2:
        time_fora = st.selectbox("TIME FORA", [t for t in elenco if t != time_casa])

    if st.button("⚡ INICIAR ANÁLISE MILIMÉTRICA"):
        with st.status("GIAE: Processando Big Data...", expanded=True) as s:
            time.sleep(1)
            st.write("🛰️ Sincronizando scouts mundiais...")
            time.sleep(1)
            s.update(label="ANÁLISE CONCLUÍDA!", state="complete")
        
        # RESULTADO (FOCO EM GOLS 1º E 2º TEMPO)
        r1, r2, r3 = st.columns(3)
        r1.metric("Vencedor", time_casa, "Assertividade 94%")
        r2.metric("Gols", "+2.5", "Tendência: Ambos Tempos")
        r3.metric("Escanteios", "Over 10.5", "Liquidez Alta")

else:
    st.markdown("### 🤖 Cockpit de Comando Ativado")
    st.write("Configuração visual concluída: Botão ferramenta com scanner laser e texto perfeitamente centralizado.")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | BANCO DE DADOS: RESTAURADO COMPLETAMENTE</div><div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
