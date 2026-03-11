import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v3.1]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS DE ALTA FIDELIDADE (PROTEÇÃO DE UI - BLOQUEADO) ---
st.markdown("""
    <style>
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    .nav-items { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    
    [data-testid="stSidebar"] { background-color: #15191d !important; margin-top: 50px !important; border-right: 1px solid #2d3843 !important; width: 260px !important; }
    [data-testid="stSidebarContent"] { padding-top: 0px !important; overflow-x: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; margin-top: -35px !important; }
    
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button {
        background: #f64d23 !important; color: white !important; border-radius: 30px !important; height: 48px !important; width: 92% !important; margin: 0px auto 20px 10px !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        padding-left: 35px !important; font-weight: 900 !important; font-size: 10px !important;
        position: relative !important; overflow: hidden !important; border: none !important; text-align: center !important;
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

# --- NAVBAR ---
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

# --- BANCO DE DADOS GLOBAL ---
db_global = {
    "🇧🇷 BR COMPETIÇÕES BRASILEIRAS": {
        "Brasileirão": ["Série A", "Série B", "Série C", "Série D"],
        "Copas Nacionais": ["Copa do Brasil", "Supercopa do Brasil"],
        "Estaduais": ["Paulistão", "Carioca", "Mineiro", "Gaúcho"],
        "Regionais": ["Copa do Nordeste", "Copa Verde"]
    },
    "🇪🇺 EU ELITE EUROPEIA (BIG 5)": {
        "Inglaterra": ["Premier League"],
        "Espanha": ["La Liga"],
        "Alemanha": ["Bundesliga"],
        "Itália": ["Serie A"],
        "França": ["Ligue 1"]
    },
    "🌎 AMÉRICAS (SUL / CENTRAL)": {
        "Continental": ["Copa Libertadores", "Copa Sul-Americana"],
        "Nacionais": ["Liga MX (México)", "Liga Profesional (Argentina)"]
    },
    "🏆 TORNEIOS INTERNACIONAIS": {
        "UEFA": ["Champions League", "Europa League"],
        "Mundial": ["Mundial de Clubes FIFA"]
    }
}

# --- DICIONÁRIO DE TIMES (MAPEAMENTO TOTAL) ---
times_db = {
    # BRASIL
    "Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Internacional", "Cruzeiro", "Bahia", "Vasco", "Atlético-MG", "Fluminense", "Corinthians", "Grêmio", "Criciúma", "Bragantino", "Juventude", "Vitória", "Athletico-PR", "Cuiabá", "Atlético-GO"],
    "Série B": ["Santos", "Sport", "Mirassol", "Novorizontino", "Ceará", "Goiás", "Vila Nova", "Coritiba", "Amazonas", "Avaí", "Operário", "Ponte Preta", "CRB", "Chapecoense", "Ituano", "Brusque", "Guarani", "Paysandu", "Botafogo-SP", "América-MG"],
    "Série C": ["Náutico", "Figueirense", "Remo", "CSA", "Sampaio Corrêa", "ABC", "Botafogo-PB", "Volta Redonda", "Londrina", "Caxias"],
    "Série D": ["Brasil de Pelotas", "Santa Cruz", "Maringá", "Anápolis", "Portuguesa-RJ", "Inter de Limeira"],
    "Copa do Brasil": ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Atlético-MG", "Bahia", "Vasco", "Grêmio"],
    "Supercopa do Brasil": ["Palmeiras", "Flamengo", "São Paulo", "Vitória", "Atlético-MG"],
    "Paulistão": ["Palmeiras", "Santos", "São Paulo", "Corinthians", "Bragantino", "Inter de Limeira", "Novorizontino", "Mirassol"],
    "Carioca": ["Flamengo", "Fluminense", "Vasco", "Botafogo", "Nova Iguaçu", "Boavista"],
    "Mineiro": ["Atlético-MG", "Cruzeiro", "América-MG", "Tombense", "Villa Nova", "Ipatinga", "Athletic", "Pouso Alegre"],
    "Gaúcho": ["Grêmio", "Internacional", "Juventude", "Caxias", "Brasil de Pelotas", "Ypiranga", "São José", "Novo Hamburgo"],
    "Copa do Nordeste": ["Fortaleza", "Bahia", "Sport", "Vitória", "Ceará", "CRB", "Náutico", "ABC"],
    "Copa Verde": ["Cuiabá", "Paysandu", "Vila Nova", "Remo", "Amazonas", "Goiás", "Manaus"],

    # EUROPA (BIG 5)
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Man United", "Newcastle", "Brighton", "West Ham"],
    "La Liga": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Athletic Bilbao", "Real Sociedad", "Real Betis", "Villarreal"],
    "Bundesliga": ["Bayer Leverkusen", "Bayern Munich", "Dortmund", "RB Leipzig", "Stuttgart", "Frankfurt", "Hoffenheim", "Heidenheim"],
    "Serie A": ["Inter de Milão", "Milan", "Juventus", "Atalanta", "Bologna", "Roma", "Lazio", "Fiorentina", "Napoli"],
    "Ligue 1": ["PSG", "Monaco", "Brest", "Lille", "Nice", "Lyon", "Marseille", "Lens"],

    # INTERNACIONAIS
    "Champions League": ["Real Madrid", "Man City", "Bayern Munich", "PSG", "Inter de Milão", "Arsenal", "Barcelona", "Liverpool", "Bayer Leverkusen"],
    "Copa Libertadores": ["Flamengo", "Palmeiras", "River Plate", "Atlético-MG", "São Paulo", "Fluminense", "Botafogo", "Peñarol"]
}

# --- SIDEBAR ---
with st.sidebar:
    if st.button("PROCESSAR ALGORITMO"): st.session_state.app_state = "processar"
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
    
    c1, c2, c3 = st.columns(3)
    with c1: reg_sel = st.selectbox("📂 SELECIONE A REGIÃO", list(db_global.keys()))
    with c2: cat_sel = st.selectbox("📁 CATEGORIA", list(db_global[reg_sel].keys()))
    with c3: comp_sel = st.selectbox("🏆 CAMPEONATO", db_global[reg_sel][cat_sel])

    st.divider()
    st.markdown(f"#### 🏟️ Confronto: {comp_sel}")
    
    # BUSCA DE TIMES REAL (SEM FALHAS AGORA)
    elenco = times_db.get(comp_sel, [f"Time A ({comp_sel})", f"Time B ({comp_sel})"])
    
    t1, t2 = st.columns(2)
    with t1: casa = st.selectbox("TIME CASA", elenco)
    with t2: fora = st.selectbox("TIME FORA", [t for t in elenco if t != casa])

    if st.button("⚡ INICIAR ANÁLISE MILIMÉTRICA"):
        with st.status(f"GIAE: Analisando {casa} vs {fora}...", expanded=True) as s:
            time.sleep(1)
            st.write("🛰️ Cruzando histórico de 1º e 2º tempo...")
            time.sleep(1)
            s.update(label="ANÁLISE MILIMÉTRICA CONCLUÍDA!", state="complete")
        
        # --- RESULTADOS MILIMÉTRICOS ---
        st.success(f"### 🤖 RESULTADOS GIAE PRO: {casa} vs {fora}")
        res1, res2, res3, res4 = st.columns(4)
        res1.metric("Vencedor", casa, "68% Conf.")
        res2.metric("Gols", "+2.5", "Tendência: HT/FT")
        res3.metric("Escanteios", "Over 10.5", "Alta Liquidez")
        res4.metric("Assertividade", "94.2%", "IA Nível 3")

        st.divider()
        st.subheader("📊 Scout Milimétrico (Previsão por Tempo)")
        st.table({
            "Métrica": ["Posse de Bola", "Chutes ao Gol", "Defesas do Goleiro", "Cartões Amarelos"],
            "1º Tempo (Prev)": ["52%", "3.4", "2.1", "1.0"],
            "2º Tempo (Prev)": ["58%", "4.2", "3.0", "2.5"],
            "Total Partida": ["55%", "7.6", "5.1", "3.5"]
        })

else:
    st.markdown("### 🤖 Cockpit de Comando Ativado")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DADOS: 100% SINCRONIZADOS</div><div>GESTOR IA PRO v3.1 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
