import streamlit as st
import time
import random

# ==============================================================================
# [GIAE KERNEL SHIELD v31.0 - RESTAURAÇÃO TOTAL E LÓGICA DE ELITE]
# ESTADO: DESIGN RECUPERADO (6 CARDS + NEWS TICKER)
# FIX: PROTEÇÃO DE CABEÇALHO, LUPA E RODAPÉ FIXO
# CHAVE DE SEGURANÇA: GIAE-JARVIS-ULTIMATE-RECOVERY
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CONTROLE DE NAVEGAÇÃO ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'liga_selecionada' not in st.session_state:
    st.session_state.liga_selecionada = None

# --- [LOCK] BLOCO DE SEGURANÇA CSS (O DESIGN PERFEITO RESTAURADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }

    /* [02] SIDEBAR LOCK (320PX) */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    /* [03] NAVBAR SUPERIOR AZUL ROYAL */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; 
    }
    .header-left { display: flex; align-items: center; }
    .logo-link { 
        color: #9d54ff !important; font-weight: 900; font-size: 20px !important; 
        text-transform: uppercase; letter-spacing: 1px; margin-right: 40px; 
        text-decoration: none !important; cursor: pointer !important; transition: 0.3s;
    }
    .logo-link:hover { text-shadow: 0 0 15px #9d54ff; filter: brightness(1.2); }

    .nav-items { display: flex; gap: 15px; }
    .nav-items span { color: #ffffff; font-size: 10px !important; text-transform: uppercase; cursor: pointer; white-space: nowrap; transition: 0.2s; }
    .nav-items span:hover { color: #9d54ff; }

    /* HEADER DIREITO - EFEITOS RESTAURADOS */
    .header-right { display: flex; align-items: center; gap: 15px; min-width: 250px; justify-content: flex-end; }
    .search-icon { color: #ffffff !important; cursor: pointer !important; font-size: 16px !important; transition: 0.3s !important; }
    .search-icon:hover { color: #9d54ff !important; transform: scale(1.2); }
    
    .registrar-pill { 
        color: #ffffff !important; font-size: 10px !important; font-weight: 700 !important; border: 1px solid #ffffff !important; 
        padding: 6px 15px !important; border-radius: 20px !important; cursor: pointer !important; transition: 0.3s; white-space: nowrap;
    }
    .registrar-pill:hover { background: #ffffff !important; color: #002366 !important; }

    .entrar-grad { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: white !important; padding: 7px 20px !important; border-radius: 4px !important; 
        font-weight: 800 !important; font-size: 10px !important; cursor: pointer !important; transition: 0.3s; white-space: nowrap;
    }
    .entrar-grad:hover { filter: brightness(1.2) !important; box-shadow: 0 0 15px rgba(109, 40, 217, 0.4); }

    /* [04] SIDEBAR BOTÕES */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; border-radius: 0px !important;
        text-align: left !important; width: 100% !important; padding: 18px 25px !important; 
        font-size: 10px !important; text-transform: uppercase !important; white-space: nowrap !important;
    }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }

    /* [05] DASHBOARD ELEMENTS */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; transition: 0.3s; }
    .highlight-card:hover { border-color: #6d28d9; transform: translateY(-3px); }
    
    .pulse-dot { height: 6px; width: 6px; background-color: #22c55e; border-radius: 50%; display: inline-block; margin-right: 5px; animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    /* MÓDULOS DE RESULTADOS */
    .result-box { background: rgba(0, 35, 102, 0.1); border-left: 4px solid #9d54ff; padding: 15px; margin-bottom: 10px; border-radius: 4px; }
    .result-title { color: #64748b; font-size: 10px; text-transform: uppercase; font-weight: 700; }
    .result-value { color: white; font-size: 16px; font-weight: 900; }
    .prob-badge { background: #22c55e; color: black; padding: 2px 8px; border-radius: 10px; font-size: 9px; font-weight: 900; float: right; }

    /* FOOTER FIXO NO FUNDO */
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- [LOCK] CABEÇALHO ---
st.markdown(f"""
    <div class="betano-header">
        <div class="header-left">
            <a href="/" target="_self" class="logo-link">GESTOR IA</a>
            <div class="nav-items">
                <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Estatísticas Avançadas</span>
            </div>
        </div>
        <div class="header-right">
            <div class="search-icon">🔍</div>
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- [LOCK] SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("📊 LOCALIZAR APOSTA"): 
        st.session_state.aba_ativa = "analise"
        st.session_state.liga_selecionada = None
    st.button("📅 JOGOS DO DIA")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("⚽ APOSTAS POR GOLS")
    st.button("🚩 APOSTAS POR ESCANTEIOS")

# --- CONTEÚDO CENTRAL ---
st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# TELA HOME / DASHBOARD (RESTAURADA INTEGRALMENTE)
if st.session_state.aba_ativa == "home":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:10px; letter-spacing:-1px;">HOME / DASHBOARD</div>', unsafe_allow_html=True)
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE ● ALERTA: ODDS EM QUEDA ● DICA: GESTÃO DE BANCA ATUALIZADA</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;"><span class="pulse-dot"></span>Destaque Live</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">FLAMENGO x PALMEIRAS</div><div style="color:#06b6d4; font-size:10px; margin-top:5px;">BRASILEIRÃO - AO VIVO</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Sugestão de Mercado</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">OVER 2.5 GOLS</div><div style="color:#00cc66; font-size:10px; margin-top:5px;">CONFIDÊNCIA: 88%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:88%;"></div></div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">IA Education</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">GESTÃO 3%</div><div style="color:#9d54ff; font-size:10px; margin-top:5px;">PRESERVE SEU CAPITAL</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)
    
    st.markdown('<div style="height:15px;"></div>', unsafe_allow_html=True)
    
    c4, c5, c6 = st.columns(3)
    with c4: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Tendência de Valor</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">ODDS DESAJUSTADAS</div><div style="color:#facc15; font-size:10px; margin-top:5px;">PREMIER LEAGUE - LIVE</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:75%;"></div></div></div>', unsafe_allow_html=True)
    with c5: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;"><span class="pulse-dot"></span>Scanner de Cantos</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">ALTA PRESSÃO (HT)</div><div style="color:#fb7185; font-size:10px; margin-top:5px;">7 PARTIDAS ENCONTRADAS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:60%;"></div></div></div>', unsafe_allow_html=True)
    with c6: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Performance Semanal</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">ASSERTIVIDADE 92%</div><div style="color:#22c55e; font-size:10px; margin-top:5px;">PROTOCOLO CRIZAL ACTIVE</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:92%;"></div></div></div>', unsafe_allow_html=True)

# TELA DE ANÁLISE PROFUNDA
elif st.session_state.aba_ativa == "analise":
    if st.session_state.liga_selecionada is None:
        st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:20px;">SELECIONE O CAMPEONATO</div>', unsafe_allow_html=True)
        ligas = ["PREMIER LEAGUE", "LA LIGA", "BRASILEIRÃO SÉRIE A", "CHAMPIONS LEAGUE", "BUNDESLIGA", "SERIE A TIM"]
        cols = st.columns(3)
        for i, liga in enumerate(ligas):
            if cols[i % 3].button(liga, use_container_width=True):
                st.session_state.liga_selecionada = liga
                st.rerun()
    else:
        st.markdown(f'<div style="color:white; font-weight:900; font-size:26px; margin-bottom:5px;">{st.session_state.liga_selecionada}</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        time_a = col1.selectbox("TIME MANDANTE", ["Real Madrid", "Barcelona", "Flamengo", "Man. City", "Liverpool"])
        time_b = col2.selectbox("TIME VISITANTE", ["Atlético Madrid", "Palmeiras", "Arsenal", "Bayern", "PSG"])
        
        if st.button("⚡ EXECUTAR ALGORITMO GIAE"):
            with st.spinner("JARVIS CALCULANDO PROBABILIDADES..."):
                time.sleep(1.5)
                st.markdown('<div style="color:#9d54ff; font-weight:900; font-size:18px; margin:20px 0;">RESULTADOS DE ALTA PROBABILIDADE MATEMÁTICA:</div>', unsafe_allow_html=True)
                
                # Lista de métricas solicitadas
                metrics = [
                    {"title": "Probabilidade Vendedor", "val": f"Vitória {time_a}", "prob": 82},
                    {"title": "Gols estimados", "val": "Over 1.5 Gols (Ambos os tempos)", "prob": 89},
                    {"title": "Cartões", "val": "Mais de 4.5 cartões no jogo", "prob": 77},
                    {"title": "Escanteios (Total e por Time)", "val": f"{time_a} Over 5.5 / Jogo Over 9.5", "prob": 91},
                    {"title": "Tiros de Meta", "val": "Média de 14.5 tiros de meta totais", "prob": 85},
                    {"title": "Chutes no Gol", "val": f"Média de 6.5 chutes do {time_a}", "prob": 88},
                    {"title": "Defesas do Goleiro", "val": f"Goleiro do {time_b} fará 4+ defesas", "prob": 80}
                ]
                
                # Regra: Só listar se probabilidade for > 75 (Exemplo)
                for m in metrics:
                    if m['prob'] > 75:
                        st.markdown(f"""
                        <div class="result-box">
                            <span class="prob-badge">{m['prob']}%</span>
                            <div class="result-title">{m['title']}</div>
                            <div class="result-value">{m['val']}</div>
                        </div>
                        """, unsafe_allow_html=True)

# --- [LOCK] FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v18.0 | JARVIS PROTECT V31</div></div>""", unsafe_allow_html=True)
