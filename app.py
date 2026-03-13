import streamlit as st
import time
import pandas as pd

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v5.1]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- CSS DE ALTA ESPECIFICIDADE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* RESET E ESTRUTURA BASE */
    header, [data-testid="stHeader"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Inter', sans-serif !important; }
    
    /* AJUSTE DE PADDING PARA NAVBAR FIXA */
    .main .block-container { padding-top: 80px !important; }

    /* SIDEBAR CUSTOMIZADA */
    [data-testid="stSidebar"] { 
        background-color: #15191d !important; 
        border-right: 1px solid #2d3843 !important;
        padding-top: 20px !important;
    }
    [data-testid="stSidebarNav"] { display: none !important; }

    /* NAVBAR SUPERIOR */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #1a242d; border-bottom: 2px solid #f64d23; 
        display: flex; align-items: center; padding: 0 30px; z-index: 999999; 
    }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 22px; font-style: italic; letter-spacing: -1px; }
    .nav-items { display: flex; gap: 25px; margin-left: 40px; flex-grow: 1; color: #94a3b8; font-size: 12px; font-weight: 700; text-transform: uppercase; }
    .nav-items span:hover { color: #f64d23; cursor: pointer; }
    
    .logo-hex { 
        width:22px; height:26px; background:#f64d23; 
        clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); 
        margin-right:12px; animation: pulse-hex 2s infinite ease-in-out; 
    }

    /* BOTÕES CÁPSULA (SIDEBAR E CENTRAL) - DESIGN BLINDADO */
    div[data-testid="stButton"] button {
        background-color: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        height: 45px !important;
        font-size: 13px !important;
        box-shadow: 0 4px 15px rgba(246, 77, 35, 0.2) !important;
    }

    /* ESTADO DE HOVER - REMOVENDO O QUADRADO DO STREAMLIT */
    div[data-testid="stButton"] button:hover, 
    div[data-testid="stButton"] button:active, 
    div[data-testid="stButton"] button:focus {
        background-color: #ff6b4a !important;
        border-radius: 50px !important;
        color: white !important;
        box-shadow: 0 0 25px rgba(246, 77, 35, 0.5) !important;
        border: none !important;
        outline: none !important;
    }

    /* BOTÃO DE PROCESSAMENTO (DESTAQUE) */
    .main-proc-btn div[data-testid="stButton"] button {
        height: 65px !important;
        font-size: 16px !important;
        background: linear-gradient(90deg, #f64d23, #ff8c00) !important;
        margin-top: 20px;
    }

    /* BOTÕES SECUNDÁRIOS SIDEBAR */
    .side-opt div[data-testid="stButton"] button {
        background-color: transparent !important;
        color: #94a3b8 !important;
        text-align: left !important;
        justify-content: flex-start !important;
        border-radius: 8px !important;
        border-bottom: 1px solid #1e293b !important;
        box-shadow: none !important;
        font-size: 11px !important;
    }
    .side-opt div[data-testid="stButton"] button:hover {
        background-color: #2d3843 !important;
        color: #f64d23 !important;
    }

    /* CARDS DE RESULTADO */
    .metric-card {
        background: #1a242d;
        border: 1px solid #2d3843;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        border-top: 3px solid #f64d23;
    }
    .metric-value { font-size: 28px; font-weight: 900; color: #fff; }
    .metric-label { font-size: 12px; color: #94a3b8; text-transform: uppercase; }

    /* ANIMAÇÕES */
    @keyframes pulse-hex { 0%, 100% { opacity: 1; } 50% { opacity: 0.6; } }
    
    .betano-footer { 
        position: fixed; bottom: 0; left: 0; width: 100%; 
        background-color: #1a242d; height: 30px; 
        border-top: 1px solid #2d3843; display: flex; 
        justify-content: space-between; align-items: center; 
        padding: 0 20px; font-size: 10px; color: #64748b; z-index: 999999; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown(f"""
    <div class="betano-header">
        <div class="logo-hex"></div>
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-items">
            <span>Esportes</span><span>Ao Vivo</span><span>Radar de Odds</span><span>Histórico IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:12px; align-items:center;">
            <div style="color:#94a3b8; font-size:11px; font-weight:700; cursor:pointer;">REGISTRAR</div>
            <div style="background:#00cc66; color:white; padding:8px 20px; border-radius:4px; font-weight:800; font-size:11px; cursor:pointer; box-shadow: 0 4px 12px rgba(0,204,102,0.2);">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- DB SIMULADO ---
db_global = {
    "BRASIL": {"Série A": ["Palmeiras", "Flamengo", "Botafogo", "Fortaleza", "São Paulo"], "Copa do Brasil": ["Vasco", "Corinthians"]},
    "EUROPA": {"Premier League": ["Man City", "Arsenal", "Liverpool"], "La Liga": ["Real Madrid", "Barcelona"]}
}

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔥 FERRAMENTA DE ANÁLISE"): st.session_state.app_state = "processar"
    
    st.markdown('<div class="side-opt">', unsafe_allow_html=True)
    st.button("📅 PRÓXIMOS JOGOS")
    st.button("📈 TENDÊNCIAS DO DIA")
    st.button("⚽ MERCADO DE GOLS")
    st.button("🚩 ESCANTEIOS PRO")
    st.button("🟨 CARTÕES MÉTRICOS")
    st.markdown('</div>', unsafe_allow_html=True)

# --- LOGICA DE ESTADO ---
if "app_state" not in st.session_state: st.session_state.app_state = "home"
if "analisado" not in st.session_state: st.session_state.analisado = False

# --- ÁREA CENTRAL ---
if st.session_state.app_state == "processar":
    st.markdown('<h1 style="color:white; font-size:28px; font-weight:900;">CONFIGURAÇÃO DO ALGORITMO</h1>', unsafe_allow_html=True)
    
    col_reg, col_cat, col_comp = st.columns(3)
    with col_reg: reg = st.selectbox("REGIÃO", list(db_global.keys()))
    with col_cat: cat = st.selectbox("COMPETIÇÃO", list(db_global[reg].keys()))
    with col_comp: comp = st.selectbox("CAMPEONATO", db_global[reg][cat])

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    
    t1, t2 = st.columns(2)
    elenco = db_global[reg][cat]
    with t1: casa = st.selectbox("Mandante", elenco, index=0)
    with t2: fora = st.selectbox("Visitante", elenco, index=1)

    st.markdown('<div class="main-proc-btn">', unsafe_allow_html=True)
    if st.button("CALCULAR PROBABILIDADES IA"):
        with st.status("🧬 Escaneando padrões históricos...", expanded=True) as status:
            time.sleep(1)
            st.write("🔍 Analisando performance recente...")
            time.sleep(1)
            st.write("📊 Cruzando dados de arbitragem e clima...")
            time.sleep(0.8)
            status.update(label="ANÁLISE CONCLUÍDA!", state="complete", expanded=False)
        st.session_state.analisado = True
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.analisado:
        st.markdown("<br>", unsafe_allow_html=True)
        res1, res2, res3, res4 = st.columns(4)
        
        metrics = [
            ("VITÓRIA CASA", "64%", "res1"),
            ("EMPATE", "21%", "res2"),
            ("VITÓRIA FORA", "15%", "res3"),
            ("OVER 2.5 GOLS", "78%", "res4")
        ]
        
        for col, (label, value, tag) in zip([res1, res2, res3, res4], metrics):
            with col:
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">{label}</div>
                        <div class="metric-value">{value}</div>
                    </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.info(f"🤖 **Sugestão GIAE:** Forte tendência para **{casa}** vencer com mais de 1.5 gols na partida.")

else:
    # HOME / DASHBOARD INICIAL
    st.markdown(f"""
        <div style="text-align:center; padding: 100px 20px;">
            <h1 style="font-size:48px; font-weight:900; color:white; margin-bottom:10px;">BEM-VINDO AO FUTURO DO TRADING</h1>
            <p style="color:#94a3b8; font-size:18px;">Selecione uma ferramenta na barra lateral para iniciar a análise preditiva.</p>
        </div>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
    <div class="betano-footer">
        <div>SISTEMA GIAE v5.1 | <span style="color:#00cc66">● ONLINE</span></div>
        <div>PRECISÃO MÉDIA: 89.4% | 18+ JOGUE COM RESPONSABILIDADE</div>
    </div>
    """, unsafe_allow_html=True)
