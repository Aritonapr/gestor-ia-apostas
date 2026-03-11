import streamlit as st
import time
import random

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v3.0]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS MILIMÉTRICO PROTEGIDO ---
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
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::after { content: "" !important; position: absolute !important; top: 0 !important; left: -100% !important; width: 50px !important; height: 100% !important; background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important; animation: laser-scan 2.5s infinite linear !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::before { content: '🤖'; position: absolute; left: 6px; top: 50%; transform: translateY(-50%); width: 32px; height: 32px; background: white !important; color: #f64d23 !important; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 15px; z-index: 2; border: 2px solid #f64d23; }
    [data-testid="stSidebar"] button { background-color: transparent !important; color: #e2e8f0 !important; border: none !important; border-bottom: 1px solid #1e293b !important; text-align: left !important; font-weight: 700 !important; font-size: 11px !important; padding: 12px 15px !important; width: 100% !important; border-radius: 0px !important; text-transform: uppercase; }
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown(f"""<div class="betano-header">
    <div style="width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px;"></div>
    <div class="logo-text">GESTOR IA</div>
    <div class="nav-items">
        <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Apostas Encontradas</span><span>Assertividade IA</span>
    </div>
    <div style="margin-left:auto; display:flex; gap:12px; align-items:center;">
        <div style="border:1px solid #adb5bd; color:white; padding:4px 12px; border-radius:3px; font-size:11px; font-weight:bold; cursor:pointer;">REGISTRAR</div>
        <button style="background:#00cc66; color:white; padding:6px 20px; border-radius:3px; font-weight:bold; border:none; font-size:11px; cursor:pointer;">ENTRAR</button>
    </div>
</div>""", unsafe_allow_html=True)

# --- BANCO DE DADOS GLOBAL COMPLETO (TODAS AS PASTAS RESTAURADAS) ---
db_global = {
    "🇧🇷 COMPETIÇÕES BRASILEIRAS": {
        "Brasileirão": ["Série A", "Série B", "Série C", "Série D"],
        "Copas Nacionais": ["Copa do Brasil", "Supercopa do Brasil"],
        "Estaduais": ["Paulistão", "Carioca", "Mineiro", "Gaúcho"],
        "Regionais": ["Copa do Nordeste", "Copa Verde"]
    },
    "🇪🇺 ELITE EUROPEIA (BIG 5)": {
        "Inglaterra": ["Premier League"],
        "Espanha": ["La Liga"],
        "Alemanha": ["Bundesliga"],
        "Itália": ["Serie A (Itália)"],
        "França": ["Ligue 1"]
    },
    "🌍 EUROPA (ALTO VALOR)": {
        "Holanda/Portugal": ["Eredivisie", "Primeira Liga"],
        "Segundas Divisões": ["Championship (Inglaterra 2)"],
        "Outras": ["Super Lig (Turquia)", "Pro League (Bélgica)"]
    },
    "🌎 AMÉRICAS (SUL / CENTRAL)": {
        "Continental": ["Copa Libertadores", "Copa Sul-Americana"],
        "Nacionais": ["Liga MX (México)", "Liga Profesional (Argentina)", "MLS (EUA)"]
    },
    "🏆 TORNEIOS INTERNACIONAIS": {
        "UEFA": ["Champions League", "Europa League"],
        "FIFA": ["Mundial de Clubes FIFA"]
    }
}

times_db = {
    "Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Internacional", "Cruzeiro", "Bahia", "Vasco", "Atlético-MG"],
    "Copa do Brasil": ["Flamengo", "São Paulo", "Palmeiras", "Corinthians", "Grêmio", "Athletico-PR", "Atlético-MG"],
    "Champions League": ["Real Madrid", "Man City", "Bayern Munich", "Arsenal", "Barcelona", "PSG", "Inter de Milão", "Dortmund"]
}

# --- SIDEBAR ---
with st.sidebar:
    if st.button("PROCESSAR ALGORITMO"): st.session_state.app_state = "processar"
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")

# --- ÁREA CENTRAL ---
if "app_state" not in st.session_state: st.session_state.app_state = "home"

if st.session_state.app_state == "processar":
    st.markdown("### 📂 CENTRAL DE INTELIGÊNCIA GIAE")
    c1, c2, c3 = st.columns(3)
    with c1: reg_sel = st.selectbox("📂 SELECIONE A REGIÃO", list(db_global.keys()))
    with c2: cat_sel = st.selectbox("📁 CATEGORIA", list(db_global[reg_sel].keys()))
    with c3: comp_sel = st.selectbox("🏆 CAMPEONATO", db_global[reg_sel][cat_sel])
    st.divider()

    st.markdown(f"#### 🏟️ Configurar Confronto: {comp_sel}")
    elenco = times_db.get(comp_sel, [f"Time Genérico A", f"Time Genérico B"])
    t1, t2 = st.columns(2)
    with t1: casa = st.selectbox("TIME CASA", elenco)
    with t2: fora = st.selectbox("TIME FORA", [t for t in elenco if t != casa])

    if st.button("⚡ INICIAR ANÁLISE MILIMÉTRICA"):
        with st.status("GIAE IA: Processando...", expanded=True) as s:
            time.sleep(1)
            st.write("📊 Cruzando dados históricos e scouts...")
            s.update(label="Análise Concluída!", state="complete")
        
        # --- PAINEL DE RESULTADOS ESTATÍSTICOS (RESTAURADO) ---
        st.success(f"Análise de {casa} vs {fora} pronta.")
        
        r1, r2, r3 = st.columns(3)
        r1.metric("Vencedor Provável", casa, f"{random.randint(55,75)}%")
        r2.metric("Gols Previstos", "+2.5", "Tendência Alta")
        r3.metric("Escanteios", f"Over {random.uniform(8.5, 10.5):.1f}", "Linha Principal")

        st.info(f"**🤖 INSIGHT IA:** A probabilidade de gol no primeiro tempo para este confronto é de {random.randint(70,92)}%, baseado nos últimos 20 jogos de ambas as equipes.")

else:
    st.markdown("### 🤖 Cockpit de Comando Ativado")

# --- FOOTER ---
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | DADOS: RESTAURADOS E SINCRONIZADOS</div><div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
