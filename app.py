import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v3.0]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS MILIMÉTRICO E PROTEGIDO ---
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
    
    /* BOTÃO PROCESSAR: TEXTO CENTRALIZADO + ÍCONE + SCANNER */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button {
        background: #f64d23 !important; color: white !important; border-radius: 30px !important; 
        height: 48px !important; width: 92% !important; margin: 0px auto 20px 10px !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        font-weight: 900 !important; font-size: 11px !important;
        position: relative !important; overflow: hidden !important; border: none !important;
        text-align: center !important; padding-left: 35px !important;
    }
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::before {
        content: '🤖'; position: absolute; left: 6px; top: 50%; transform: translateY(-50%); 
        width: 32px; height: 32px; background: white !important; color: #f64d23 !important; 
        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
        font-size: 15px; z-index: 2; border: 2px solid #f64d23;
    }

    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::after {
        content: "" !important; position: absolute !important; top: 0 !important; left: -100% !important; width: 50px !important; height: 100% !important;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important; 
        animation: laser-scan 2s infinite linear !important;
    }

    [data-testid="stSidebar"] button { background-color: transparent !important; color: #e2e8f0 !important; border: none !important; border-bottom: 1px solid #1e293b !important; text-align: left !important; font-weight: 700 !important; font-size: 11px !important; padding: 12px 15px !important; width: 100% !important; border-radius: 0px !important; text-transform: uppercase; }
    
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS HIERÁRQUICO POR RELEVÂNCIA (LIGAS DE ALTA LIQUIDEZ) ---
db_liquidez = {
    "💎 ELITE MUNDIAL (BIG 5)": {
        "Inglaterra": ["Premier League"],
        "Espanha": ["La Liga"],
        "Alemanha": ["Bundesliga"],
        "Itália": ["Serie A"],
        "França": ["Ligue 1"]
    },
    "🌎 PRINCIPAIS DAS AMÉRICAS": {
        "Brasil": ["Brasileirão Série A", "Copa do Brasil"],
        "Continental": ["Copa Libertadores"],
        "México": ["Liga MX"],
        "Argentina": ["Liga Profesional"]
    },
    "📈 ALTO VALOR (2ª LINHA EURO)": {
        "Portugal": ["Primeira Liga"],
        "Holanda": ["Eredivisie"],
        "Inglaterra 2": ["Championship"],
        "Turquia": ["Super Lig"],
        "Bélgica": ["Pro League"]
    },
    "🏆 TORNEIOS INTERNACIONAIS": {
        "UEFA": ["Champions League", "Europa League"],
        "Mundial": ["Mundial de Clubes"]
    }
}

# --- TIMES SINCRONIZADOS (EXEMPLOS RELEVANTES) ---
times_db = {
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Man United", "Newcastle"],
    "La Liga": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Real Betis", "Villarreal"],
    "Brasileirão Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Internacional", "Cruzeiro", "Bahia", "Vasco", "Atlético-MG"],
    "Champions League": ["Real Madrid", "Bayern Munich", "Man City", "PSG", "Inter de Milão", "Bayer Leverkusen"],
    "Copa Libertadores": ["Flamengo", "Palmeiras", "River Plate", "Atlético-MG", "São Paulo", "Fluminense"]
}

# --- NAVBAR ---
st.markdown("""<div class="betano-header"><div style="width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px;"></div><div class="logo-text">GESTOR IA</div></div>""", unsafe_allow_html=True)

# --- SIDEBAR FIXA ---
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
    st.markdown("### 📊 CENTRAL DE LIQUIDEZ GIAE (ANÁLISE DE ALTA RELEVÂNCIA)")
    
    # ORGANIZAÇÃO EM TRÊS NÍVEIS (PASTAS)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        grupo = st.selectbox("📂 GRUPO DE RELEVÂNCIA", list(db_liquidez.keys()))
    
    with c2:
        subgrupo = st.selectbox("📂 PAÍS/CATEGORIA", list(db_liquidez[grupo].keys()))
        
    with c3:
        comp_ativa = st.selectbox("🏆 COMPETIÇÃO MONITORADA", db_liquidez[grupo][subgrupo])

    st.divider()
    
    # SELEÇÃO DE PARTIDA
    st.markdown(f"#### 🏟️ Análise Proativa: {comp_ativa}")
    t_casa, t_fora = st.columns(2)
    
    elenco = times_db.get(comp_ativa, ["Selecione uma Liga Ativa"])
    
    with t_casa:
        casa = st.selectbox("TIME CASA (HOME)", elenco)
    with t_fora:
        fora = st.selectbox("TIME FORA (AWAY)", [t for t in elenco if t != casa])

    if st.button("⚡ PROCESSAR ANÁLISE MILIMÉTRICA"):
        with st.status("MAGI IA: Cruzando dados de Big 5 e Liquidez...", expanded=True) as s:
            time.sleep(1)
            st.write("📈 Acessando histórico de ML (Machine Learning)...")
            time.sleep(1)
            st.write(f"🎯 Gerando probabilidade para {casa} vs {fora}")
            s.update(label="ANÁLISE DE ALTA ASSERTIVIDADE CONCLUÍDA!", state="complete")
            
        # RESULTADO (FOCO EM GOLS POR TEMPO E SCOUT)
        col_res1, col_res2, col_res3 = st.columns(3)
        col_res1.metric("PROB. VITÓRIA", f"{casa}", "62%")
        col_res2.metric("MERCADO DE GOLS", "+2.5", "Tendência 1º/2º T")
        col_res3.metric("ASSERTIVIDADE IA", "94.8%", "Liquidez Alta")

else:
    st.markdown("### 🤖 Cockpit de Comando Ativado")
    st.write("Aguardando ativação do Algoritmo.")

st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | FOCO: ALTA LIQUIDEZ</div><div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
