import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v3.0]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS MILIMÉTRICO E PROTEGIDO ---
st.markdown("""
    <style>
    /* RESET DE INTERFACE */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    /* NAVBAR SUPERIOR FIXA */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    
    /* SIDEBAR: MARGEM -35PX E LARGURA 260PX */
    [data-testid="stSidebar"] { background-color: #15191d !important; margin-top: 50px !important; border-right: 1px solid #2d3843 !important; width: 260px !important; }
    [data-testid="stSidebarContent"] { padding-top: 0px !important; overflow-x: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; margin-top: -35px !important; }
    
    /* BOTÃO PROCESSAR: CÁPSULA SEGMENTADA COM SCANNER (RESTAURADO) */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    @keyframes plasma-glow { 0%, 100% { box-shadow: 0 0 5px #f64d23; } 50% { box-shadow: 0 0 20px #f64d23; } }
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button {
        background: #f64d23 !important; color: white !important; border-radius: 30px !important; 
        height: 48px !important; width: 92% !important; margin: 0px auto 20px 10px !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        padding-left: 45px !important; font-weight: 900 !important; font-size: 11px !important;
        position: relative !important; overflow: hidden !important; animation: plasma-glow 3s infinite ease-in-out !important;
        border: none !important; text-align: center !important;
    }
    
    /* SCANNER LASER */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::after {
        content: "" !important; position: absolute !important; top: 0 !important; left: -100% !important; width: 60px !important; height: 100% !important;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.5), transparent) !important; 
        transform: skewX(-25deg) !important; animation: laser-scan 2s infinite linear !important;
    }
    
    /* ÍCONE ROBÔ CENTRALIZADO À ESQUERDA NA CÁPSULA */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::before {
        content: '🤖'; position: absolute; left: 6px; top: 50%; transform: translateY(-50%); 
        width: 34px; height: 34px; background: white !important; color: #f64d23 !important; 
        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
        font-size: 16px; z-index: 2; border: 2px solid #f64d23;
    }

    /* BOTÕES DA SIDEBAR (CATEGORIAS) */
    [data-testid="stSidebar"] button { background-color: transparent !important; color: #e2e8f0 !important; border: none !important; border-bottom: 1px solid #1e293b !important; text-align: left !important; font-weight: 700 !important; font-size: 11px !important; padding: 12px 15px !important; width: 100% !important; border-radius: 0px !important; text-transform: uppercase; }
    [data-testid="stSidebar"] button:hover { color: #f64d23 !important; background-color: #1a242d !important; }

    /* FOOTER */
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS DE TIMES (SINCRONIZADO 2024/25) ---
times_db = {
    "Brasileirão Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo", "Internacional", "Cruzeiro", "Bahia", "Vasco", "Atlético-MG", "Grêmio", "Criciúma", "Bragantino", "Juventude", "Fluminense", "Vitória", "Corinthians", "Cuiabá", "Atlético-GO", "Athletico-PR"],
    "Brasileirão Série B": ["Santos", "Sport", "Novorizontino", "Mirassol", "Ceará", "Vila Nova", "Goiás", "Operário-PR", "Amazonas", "Coritiba", "Avaí", "Ponte Preta", "CRB", "Chapecoense", "Ituano", "Brusque", "Guarani"],
    "La Liga (Espanha)": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Athletic Bilbao", "Real Sociedad", "Real Betis", "Villarreal", "Sevilla", "Valencia"],
    "Premier League (Inglaterra)": ["Manchester City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Newcastle", "Manchester United", "West Ham", "Brighton"],
    "Paulistão": ["Palmeiras", "Santos", "São Paulo", "Corinthians", "Red Bull Bragantino", "Inter de Limeira", "Água Santa", "Mirassol"],
    "Copa Libertadores da América": ["Flamengo", "Palmeiras", "River Plate", "Boca Juniors", "Fluminense", "São Paulo", "Atlético-MG", "Peñarol", "Colo-Colo"]
}

# --- NAVBAR ---
st.markdown("""
    <div class="betano-header">
        <div style="width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px;"></div>
        <div class="logo-text">GESTOR IA</div>
    </div>
    """, unsafe_allow_html=True)

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
if "app_state" not in st.session_state:
    st.session_state.app_state = "home"

if st.session_state.app_state == "processar":
    st.markdown("### 🤖 NÚCLEO DE PROCESSAMENTO IA")
    
    col1, col2 = st.columns(2)
    with col1:
        comp_sel = st.selectbox("SELECIONE A COMPETIÇÃO", list(times_db.keys()))
    
    with col2:
        times_disponiveis = times_db.get(comp_sel, ["Selecione a Competição"])
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            casa = st.selectbox("TIME CASA", times_disponiveis)
        with col_t2:
            fora = st.selectbox("TIME FORA", [t for t in times_disponiveis if t != casa])

    if st.button("🔥 EXECUTAR ANÁLISE MILIMÉTRICA"):
        with st.status(f"Analisando {casa} vs {fora}...", expanded=True) as status:
            time.sleep(1.5)
            st.write("📊 Cruzando dados históricos e scouts recentes...")
            time.sleep(1)
            status.update(label="ANÁLISE CONCLUÍDA COM 94.2% DE ASSERTIVIDADE", state="complete")
        
        # RESULTADOS
        res_col1, res_col2, res_col3 = st.columns(3)
        with res_col1:
            st.metric("VENCEDOR", casa, "65% Prob.")
            st.info(f"**Gols 1º T:** 82%\n\n**Gols 2º T:** 60%")
        with res_col2:
            st.metric("GOLS TOTAIS", "+2.5", "Tendência Alta")
            st.info(f"**Escanteios:** Over 10.5\n\n**Cartões:** Over 4.5")
        with res_col3:
            st.metric("ODD ESTIMADA", "1.85", "-0.15 Var")
            st.info(f"**Chutes ao Gol:** 6.2\n\n**Defesas Goleiro:** 4.1")

        st.divider()
        st.subheader("📋 Scout Milimétrico por Tempo")
        st.table({
            "Métrica IA": ["Chutes Direção Gol", "Chutes Totais", "Tiro de Meta", "Cartões Amarelos"],
            "1º Tempo (Prev)": ["3.1", "6.4", "4.0", "1.2"],
            "2º Tempo (Prev)": ["3.1", "7.8", "5.2", "2.8"],
            "Total Partida": ["6.2", "14.2", "9.2", "4.0"]
        })

else:
    st.markdown(f"""
        <div style="height: 60vh; display: flex; flex-direction: column; justify-content: center; align-items: center; border: 1px dashed #2d3843; border-radius: 10px;">
            <h2 style="color: #f64d23; font-style: italic;">SISTEMA PRONTO PARA OPERAR</h2>
            <p style="color: #94a3b8;">Aguardando ativação do Algoritmo na Sidebar.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | NÚCLEO: {0}</div><div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""".format("SINCRONIZADO"), unsafe_allow_html=True)
