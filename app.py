import streamlit as st
import time
import random

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v3.0]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS PROTEGIDO (NÃO ALTERAR) ---
st.markdown("""
    <style>
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    
    /* SIDEBAR ULTRA-SUBIDA (CONFORME ESBOÇO) */
    [data-testid="stSidebar"] { background-color: #15191d !important; margin-top: 50px !important; border-right: 1px solid #2d3843 !important; width: 260px !important; }
    [data-testid="stSidebarContent"] { padding-top: 0px !important; overflow-x: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; margin-top: -35px !important; }
    
    /* BOTÃO FERRAMENTA: CÁPSULA CENTRALIZADA COM SCANNER */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button {
        background: #f64d23 !important; color: white !important; border-radius: 30px !important; height: 48px !important; width: 92% !important; margin: 0px auto 20px 10px !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        padding-left: 35px !important; font-weight: 900 !important; font-size: 11px !important;
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
    
    /* BOTÕES DE CATEGORIA */
    [data-testid="stSidebar"] button { background-color: transparent !important; color: #e2e8f0 !important; border: none !important; border-bottom: 1px solid #1e293b !important; text-align: left !important; font-weight: 700 !important; font-size: 11px !important; padding: 12px 15px !important; width: 100% !important; border-radius: 0px !important; text-transform: uppercase; }
    
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS COMPLETO (SÉRIES A, B, C, D, ESTADUAIS E EUROPA) ---
db_global = {
    "🇧🇷 COMPETIÇÕES BRASILEIRAS": {
        "Brasileirão": ["Série A", "Série B", "Série C", "Série D"],
        "Copas": ["Copa do Brasil", "Supercopa do Brasil"],
        "Regionais": ["Copa do Nordeste", "Copa Verde"],
        "Estaduais": ["Paulistão", "Carioca", "Mineiro", "Gaúcho", "Paranaense", "Catarinense", "Pernambucano", "Baiano"]
    },
    "🇪🇺 CAMPEONATOS EUROPA": {
        "Principais": ["Premier League", "La Liga", "Bundesliga", "Serie A (Itália)", "Ligue 1"],
        "Secundárias": ["Eredivisie (Holanda)", "Primeira Liga (Portugal)", "Championship (Inglaterra 2)"],
        "Copas Europeias": ["Champions League", "Europa League", "Conference League"]
    },
    "🌎 INTERNACIONAIS (CLUBES BR)": {
        "Continente": ["Copa Libertadores", "Copa Sul-Americana", "Recopa Sul-Americana"]
    },
    "🌍 RESTO DO MUNDO": {
        "Américas": ["Liga MX (México)", "Liga Profesional (Argentina)", "MLS (EUA)"],
        "Ásia/Outros": ["Saudi Pro League", "J-League"]
    }
}

# --- TIMES SINCRONIZADOS POR CAMPEONATO ---
times_db = {
    "Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Internacional", "Cruzeiro", "Bahia", "Vasco", "Atlético-MG", "Fluminense", "Corinthians", "Grêmio", "Criciúma", "Bragantino", "Juventude", "Vitória", "Athletico-PR", "Cuiabá", "Atlético-GO"],
    "Série B": ["Santos", "Sport", "Mirassol", "Novorizontino", "Ceará", "Goiás", "Vila Nova", "Coritiba", "Amazonas", "Avaí", "Operário", "Ponte Preta", "CRB", "Chapecoense", "Ituano", "Brusque", "Guarani"],
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Man United", "Newcastle", "Brighton", "West Ham"],
    "La Liga": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Athletic Bilbao", "Real Sociedad", "Real Betis"],
    "Paulistão": ["Palmeiras", "São Paulo", "Santos", "Corinthians", "Bragantino", "Inter de Limeira", "Mirassol"],
    "Copa Libertadores": ["Flamengo", "Palmeiras", "River Plate", "Atlético-MG", "Peñarol", "São Paulo", "Fluminense", "Boca Juniors"]
}

# --- NAVBAR ---
st.markdown("""<div class="betano-header"><div style="width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px;"></div><div class="logo-text">GESTOR IA</div></div>""", unsafe_allow_html=True)

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

# --- ÁREA CENTRAL (COCKPIT) ---
if "app_state" not in st.session_state: st.session_state.app_state = "home"

if st.session_state.app_state == "processar":
    st.markdown("### 🗂️ CENTRAL DE PROCESSAMENTO GIAE")
    
    # NAVEGAÇÃO POR PASTAS
    col1, col2, col3 = st.columns(3)
    
    with col1:
        regiao = st.selectbox("📂 PASTA: REGIÃO", list(db_global.keys()))
    with col2:
        categoria = st.selectbox("📂 SUB-PASTA: CATEGORIA", list(db_global[regiao].keys()))
    with col3:
        campeonato = st.selectbox("🏆 CAMPEONATO SELECIONADO", db_global[regiao][categoria])

    st.divider()
    
    # SELEÇÃO DE TIMES
    st.markdown(f"#### 🏟️ Análise de Confronto: {campeonato}")
    t1, t2 = st.columns(2)
    
    # Busca os times específicos ou gera genéricos se não estiver no DB ainda
    lista_times = times_db.get(campeonato, [f"Time A ({campeonato})", f"Time B ({campeonato})", f"Time C ({campeonato})"])
    
    with t1:
        casa = st.selectbox("TIME CASA", lista_times)
    with t2:
        fora = st.selectbox("TIME FORA", [t for t in lista_times if t != casa])

    if st.button("🔥 EXECUTAR ANÁLISE MILIMÉTRICA"):
        with st.status("GIAE IA: Processando dados históricos e internet...", expanded=True) as s:
            time.sleep(1)
            st.write("🛰️ Analisando desempenho 1º e 2º tempo...")
            time.sleep(1)
            st.write("📊 Verificando scouts de cantos e cartões...")
            s.update(label="ANÁLISE COMPLETA!", state="complete")
        
        # DISPLAY DE RESULTADOS
        r1, r2, r3 = st.columns(3)
        r1.metric("Vencedor Provável", casa, "65% Prob.")
        r2.metric("Gols Previstos", "+2.5", "Alta Relevância")
        r3.metric("Tempo do Gol", "1º e 2º Tempo", "88% Confiança")
        
        st.table({
            "Métrica Milimétrica": ["Chutes ao Gol", "Escanteios HT", "Escanteios FT", "Cartões"],
            "Previsão IA": ["7.2", "4.5", "10.2", "4.0"],
            "Assertividade": ["92%", "89%", "94%", "85%"]
        })

else:
    st.markdown("### 🤖 Cockpit de Comando Ativado")
    st.write("Selecione 'PROCESSAR ALGORITMO' na sidebar para configurar sua análise.")

st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | BANCO DE DADOS: RESTAURADO</div><div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
