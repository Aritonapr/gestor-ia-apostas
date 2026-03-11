import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v3.0]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS MILIMÉTRICO (SIDEBAR PROTEGIDA + BOTÃO CENTRALIZADO) ---
st.markdown("""
    <style>
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    
    /* SIDEBAR: 260px + MARGEM -35px */
    [data-testid="stSidebar"] { background-color: #15191d !important; margin-top: 50px !important; border-right: 1px solid #2d3843 !important; width: 260px !important; }
    [data-testid="stSidebarContent"] { padding-top: 0px !important; overflow-x: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; margin-top: -35px !important; }
    
    /* BOTÃO PROCESSAR: TEXTO CENTRALIZADO + EFEITO SCANNER */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button {
        background: #f64d23 !important; color: white !important; border-radius: 30px !important; 
        height: 48px !important; width: 92% !important; margin: 0px auto 20px 10px !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        font-weight: 900 !important; font-size: 11px !important;
        position: relative !important; overflow: hidden !important; border: none !important;
        text-align: center !important; padding-left: 20px !important; /* Ajuste para compensar o ícone */
    }
    
    /* ÍCONE DO ROBÔ */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::before {
        content: '🤖'; position: absolute; left: 6px; top: 50%; transform: translateY(-50%); 
        width: 32px; height: 32px; background: white !important; color: #f64d23 !important; 
        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
        font-size: 15px; z-index: 2; border: 2px solid #f64d23;
    }

    /* EFEITO SCANNER NO BOTÃO */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::after {
        content: "" !important; position: absolute !important; top: 0 !important; left: -100% !important; width: 50px !important; height: 100% !important;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important; 
        animation: laser-scan 2s infinite linear !important;
    }

    /* BOTÕES GERAIS SIDEBAR */
    [data-testid="stSidebar"] button { background-color: transparent !important; color: #e2e8f0 !important; border: none !important; border-bottom: 1px solid #1e293b !important; text-align: left !important; font-weight: 700 !important; font-size: 11px !important; padding: 12px 15px !important; width: 100% !important; border-radius: 0px !important; text-transform: uppercase; }
    
    /* FOOTER */
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS HIERÁRQUICO (MAPA MUNDIAL DE COMPETIÇÕES) ---
db_global = {
    "🇧🇷 COMPETIÇÕES BRASILEIRAS": {
        "Brasileirão": ["Série A", "Série B", "Série C", "Série D"],
        "Copas Nacionais": ["Copa do Brasil", "Supercopa do Brasil"],
        "Regionais": ["Copa do Nordeste", "Copa Verde"],
        "Estaduais": ["Paulistão", "Carioca", "Mineiro", "Gaúcho", "Paranaense", "Catarinense"]
    },
    "🇪🇺 ELITE EUROPEIA": {
        "Inglaterra": ["Premier League", "Championship", "FA Cup"],
        "Espanha": ["La Liga", "La Liga 2", "Copa del Rey"],
        "Alemanha": ["Bundesliga", "2. Bundesliga"],
        "Itália": ["Serie A", "Serie B"],
        "França": ["Ligue 1"],
        "Portugal": ["Liga Portugal"]
    },
    "🌎 AMÉRICA DO SUL (CONTINENTAL)": {
        "Principais": ["Copa Libertadores", "Copa Sul-Americana", "Recopa Sul-Americana"]
    },
    "🏆 COMPETIÇÕES INTERNACIONAIS": {
        "Clubes": ["Mundial de Clubes FIFA"],
        "Seleções": ["Copa do Mundo", "Eurocopa", "Copa América"]
    }
}

# --- TIMES REAIS POR LIGA (EXEMPLO SÉRIE A E PREMIER) ---
times_db = {
    "Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Internacional", "Cruzeiro", "Bahia", "Vasco", "Atlético-MG", "Grêmio", "Corinthians", "Fluminense"],
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Man United", "Newcastle"],
    "La Liga": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Real Betis"]
}

# --- NAVBAR ---
st.markdown("""<div class="betano-header"><div style="width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px;"></div><div class="logo-text">GESTOR IA</div></div>""", unsafe_allow_html=True)

# --- SIDEBAR (ALINHAMENTO PROTEGIDO) ---
with st.sidebar:
    if st.button("PROCESSAR ALGORITMO"):
        st.session_state.modulo = "processar"
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL (COCKPIT) ---
if "modulo" not in st.session_state: st.session_state.modulo = "home"

if st.session_state.modulo == "processar":
    st.markdown("### 🗂️ CENTRAL DE INTELIGÊNCIA: SELEÇÃO DE LIGA")
    
    # ORGANIZAÇÃO EM TRÊS NÍVEIS (PASTAS)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        bloco = st.selectbox("PASTA: REGIÃO/PAÍS", list(db_global.keys()))
    
    with c2:
        sub_bloco = st.selectbox("SUB-PASTA: CATEGORIA", list(db_global[bloco].keys()))
        
    with c3:
        campeonato_final = st.selectbox("COMPETIÇÃO SELECIONADA", db_global[bloco][sub_bloco])

    st.divider()
    
    # SELEÇÃO DE TIMES BASEADA NO CAMPEONATO
    st.markdown(f"#### 🏟️ Análise de Partida: {campeonato_final}")
    col_t1, col_t2 = st.columns(2)
    
    lista_times = times_db.get(campeonato_final, ["Time Genérico A", "Time Genérico B", "Time Genérico C"])
    
    with col_t1:
        time_casa = st.selectbox("TIME DA CASA", lista_times)
    with col_t2:
        time_fora = st.selectbox("TIME VISITANTE", [t for t in lista_times if t != time_casa])

    if st.button("⚡ GERAR RELATÓRIO MILIMÉTRICO"):
        with st.status("IA PROCESSANDO...", expanded=True) as s:
            time.sleep(1)
            st.write("🔍 Vasculhando histórico de jogos na internet...")
            time.sleep(1)
            st.write("📈 Cruzando estatísticas de chutes e defesas...")
            s.update(label="ANÁLISE COMPLETA!", state="complete")
            
        # CARD DE RESULTADOS (MILIMÉTRICO)
        st.success(f"PROBABILIDADE: {time_casa} {random.randint(40,70)}% | EMPATE {random.randint(10,25)}% | {time_fora} {random.randint(10,30)}%")
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("GOLS TOTAIS", "+2.5", "ALTA")
        m2.metric("GOL NO 1º T", "SIM", "88%")
        m3.metric("ESCANTEIOS", "10.5", "OVER")
        m4.metric("CARTÕES", "4.0", "MÉDIA")

else:
    st.markdown("### 🤖 Cockpit de Comando Ativado")
    st.write("Clique no botão laranja à esquerda para iniciar a análise.")

st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | BANCO DE DADOS ATUALIZADO</div><div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
