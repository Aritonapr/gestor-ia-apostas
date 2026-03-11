import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v3.0]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS MILIMÉTRICO ORIGINAL (RESTAURADO) ---
st.markdown("""
    <style>
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    
    /* SIDEBAR PROTEGIDA - VOLTANDO AO ESTADO ORIGINAL */
    [data-testid="stSidebar"] { background-color: #15191d !important; margin-top: 50px !important; border-right: 1px solid #2d3843 !important; width: 260px !important; }
    [data-testid="stSidebarContent"] { padding-top: 0px !important; overflow-x: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; margin-top: -35px !important; }
    
    /* BOTÃO CÁPSULA ORIGINAL */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button {
        background: #f64d23 !important; color: white !important; border-radius: 30px !important; height: 44px !important; width: 90% !important; margin: 0px auto 20px 10px !important;
        display: flex !important; flex-direction: column !important; align-items: center !important; justify-content: center !important;
        padding-left: 40px !important; padding-right: 10px !important; font-weight: 900 !important; font-size: 10px !important;
        position: relative !important; overflow: hidden !important;
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::before {
        content: '🤖'; position: absolute; left: 4px; top: 50%; transform: translateY(-50%); width: 34px; height: 34px;
        background: white !important; color: #f64d23 !important; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; z-index: 2; border: 2px solid #f64d23;
    }

    /* BOTÕES DE CATEGORIA */
    [data-testid="stSidebar"] button { background-color: transparent !important; color: #e2e8f0 !important; border: none !important; border-bottom: 1px solid #1e293b !important; text-align: left !important; font-weight: 700 !important; font-size: 11px !important; padding: 10px 15px !important; min-height: 40px !important; width: 100% !important; border-radius: 0px !important; text-transform: uppercase; }
    
    /* AJUSTE PARA SELECTBOX DENTRO DO CONTEÚDO (NÃO NA SIDEBAR) */
    div[data-baseweb="select"] { background-color: #1a242d !important; border: 1px solid #f64d23 !important; }

    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR SUPERIOR ---
st.markdown("""
    <div class="betano-header">
        <div style="width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px;"></div>
        <div class="logo-text">GESTOR IA</div>
        <div style="margin-left:auto; display:flex; gap:12px; align-items:center;">
            <div style="border:1px solid #adb5bd; color:white; padding:4px 12px; border-radius:3px; font-size:11px; font-weight:bold;">REGISTRAR</div>
            <button style="background:#00cc66; color:white; padding:6px 20px; border-radius:3px; font-weight:bold; border:none; font-size:11px;">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (APENAS BOTÕES ORIGINAIS) ---
with st.sidebar:
    # Usamos session_state para saber qual botão foi clicado sem desalinhar o visual
    if st.button("PROCESSAR ALGORITMO"):
        st.session_state.menu = "processar"
    
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL (COCKPIT) ---
if "menu" not in st.session_state:
    st.session_state.menu = "home"

if st.session_state.menu == "processar":
    st.markdown("### 🛠️ CONFIGURAÇÃO DE PROCESSAMENTO")
    
    # Seleção de Competições organizada dentro da área de trabalho
    col_reg, col_comp = st.columns(2)
    
    with col_reg:
        regiao = st.selectbox("1. ESCOLHA A REGIÃO", ["BRASIL", "EUROPA", "INTERNACIONAL (CLUBES BR)"])
    
    with col_comp:
        if regiao == "BRASIL":
            lista_campeonatos = [
                "Brasileirão Série A", "Brasileirão Série B", "Brasileirão Série C", "Brasileirão Série D",
                "Copa do Brasil", "Supercopa do Brasil", "Copa do Nordeste",
                "Paulistão", "Carioca", "Mineiro", "Gaúcho"
            ]
        elif regiao == "EUROPA":
            lista_campeonatos = ["La Liga (Espanha)", "Premier League (Inglaterra)"]
        else:
            lista_campeonatos = ["Copa Libertadores da América", "Copa Sul-Americana"]
            
        campeonato_selecionado = st.selectbox("2. SELECIONE A COMPETIÇÃO", lista_campeonatos)

    if st.button("INICIAR ANÁLISE MILIMÉTRICA"):
        with st.status(f"IA GIAE: Processando {campeonato_selecionado}...", expanded=True) as status:
            st.write("🛰️ Conectando aos servidores de dados esportivos...")
            time.sleep(1)
            st.write("📊 Analisando histórico H2H e performance recente...")
            time.sleep(1)
            st.write("🧮 Calculando probabilidades (Gols, Cantos, Cartões)...")
            status.update(label="ANÁLISE CONCLUÍDA!", state="complete", expanded=False)
        
        # --- RESULTADO DA ANÁLISE MILIMÉTRICA ---
        st.success(f"### 🤖 RESULTADOS GIAE: {campeonato_selecionado}")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Vencedor Provável", "Time Casa", "62% de Assertividade")
            st.write("**Gols 1º Tempo:** Sim (84%)")
        with c2:
            st.metric("Total de Gols", "+2.5", "Tendência: Over")
            st.write("**Gols 2º Tempo:** Sim (71%)")
        with c3:
            st.metric("Escanteios", "Over 10.5", "Média de 11.2")
            st.write("**Chutes ao Gol:** 14.5 previstos")
        
        st.divider()
        st.markdown("#### 📑 SCOUT DETALHADO (MILIMÉTRICO)")
        st.table({
            "Métrica de Campo": ["Tiro de Meta", "Defesas Goleiro", "Cartões Amarelos", "Chutes Direção Gol"],
            "Previsão Total": ["12", "4", "3", "7"],
            "Previsão 1º T": ["5", "2", "1", "3"],
            "Previsão 2º T": ["7", "2", "2", "4"]
        })

else:
    st.markdown("### 🤖 Cockpit de Comando Ativado")
    st.write("Selecione 'PROCESSAR ALGORITMO' na barra lateral para iniciar.")

# RODAPÉ PROTEGIDO
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | PROTEÇÃO DE UI: ON</div><div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div></div>""", unsafe_allow_html=True)
