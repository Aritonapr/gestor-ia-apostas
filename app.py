import streamlit as st
import time

# ==============================================================================
# [GIAE KERNEL SHIELD v34.0 - RESTAURAÇÃO TOTAL JARVIS]
# ESTADO: DESIGN "IMAGEM 2" RESTAURADO E TRAVADO
# FIX: SIDEBAR TRANSPARENTE, NEWS TICKER, 6 CARDS DASHBOARD
# CHAVE DE SEGURANÇA: GIAE-JARVIS-ULTIMATE-RECOVERY
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- [LOCK] CONTROLE DE NAVEGAÇÃO ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'cat_selecionada' not in st.session_state: st.session_state.cat_selecionada = None
if 'liga_selecionada' not in st.session_state: st.session_state.liga_selecionada = None

# --- [LOCK] BLOCO DE SEGURANÇA CSS (O DESIGN DA SUA IMAGEM 2) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET TOTAL */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }

    /* [02] SIDEBAR - EXATAMENTE COMO A IMAGEM 2 */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    /* BOTÕES DA SIDEBAR (ESTILO LISTA LIMPA) */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; border-radius: 0px !important;
        text-align: left !important; justify-content: flex-start !important;
        width: 100% !important; padding: 18px 25px !important; 
        font-size: 10px !important; text-transform: uppercase !important; white-space: nowrap !important;
        transition: 0.3s !important;
    }
    [data-testid="stSidebar"] button:hover { 
        color: #ffffff !important; border-left: 4px solid #6d28d9 !important; 
        background: rgba(26, 36, 45, 0.8) !important; 
    }

    /* [03] NAVBAR SUPERIOR AZUL ROYAL (IMUTÁVEL) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; text-decoration: none !important; margin-right: 35px; }
    .nav-items { display: flex; gap: 15px; }
    .nav-items span { color: #ffffff; font-size: 9px !important; font-weight: 500; text-transform: uppercase; white-space: nowrap; cursor: pointer; transition: 0.2s; }
    .nav-items span:hover { color: #9d54ff; }

    /* HEADER DIREITO */
    .header-right { display: flex; align-items: center; gap: 15px; }
    .search-icon { color: #ffffff !important; font-size: 16px !important; cursor: pointer; }
    .registrar-pill { color: #ffffff !important; font-size: 10px !important; font-weight: 700; border: 1px solid #ffffff !important; padding: 6px 15px !important; border-radius: 20px !important; cursor: pointer; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 7px 22px !important; border-radius: 4px !important; font-weight: 800; font-size: 10px !important; cursor: pointer; text-transform: uppercase; }

    /* [04] DASHBOARD ELEMENTS */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; border-radius: 2px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 150px; transition: 0.3s; position: relative; }
    .highlight-card:hover { border-color: #6d28d9; transform: translateY(-3px); }
    
    .pulse-dot { height: 6px; width: 6px; background-color: #22c55e; border-radius: 50%; display: inline-block; margin-right: 5px; animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    /* [05] FOOTER */
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    
    /* [06] ESTILO DE "BOTÕES DE COMPETIÇÃO" (CARD STYLE) */
    .comp-card-btn { background: #11151a !important; border: 1px solid #1e293b !important; color: white !important; padding: 20px !important; border-radius: 8px !important; width: 100%; cursor: pointer; text-align: center; transition: 0.3s; text-transform: uppercase; font-weight: 700; font-size: 11px; }
    .comp-card-btn:hover { border-color: #9d54ff !important; background: #161b22 !important; box-shadow: 0 0 15px rgba(157, 84, 255, 0.2); }
    </style>
    """, unsafe_allow_html=True)

# --- [UI] CABEÇALHO (IMAGEM 2) ---
st.markdown(f"""
    <div class="betano-header">
        <div class="header-left">
            <a href="/" target="_self" class="logo-link">GESTOR IA</a>
            <div class="nav-items">
                <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Apostas Encontradas</span>
                <span>Estatísticas Avançadas</span><span>Mercado Probabilístico</span><span>Assertividade IA</span>
            </div>
        </div>
        <div class="header-right">
            <div class="search-icon">🔍</div><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- [UI] SIDEBAR (IMAGEM 2) ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("📊 LOCALIZAR APOSTA"): 
        st.session_state.aba_ativa = "analise"
        st.session_state.cat_selecionada = None
        st.session_state.liga_selecionada = None
    st.button("📅 JOGOS DO DIA")
    st.button("⏰ PRÓXIMOS JOGOS")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("📈 APOSTAS POR ODDS")
    st.button("⚽ APOSTAS POR GOLS")
    st.button("🚩 APOSTAS POR ESCANTEIOS")
    st.button("⚖️ ÁRBITRO DA PARTIDA")

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- CONTEÚDO CENTRAL ---

# 1. TELA HOME (DASHBOARD COMPLETO - IMAGEM 2)
if st.session_state.aba_ativa == "home":
    st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:10px; letter-spacing:-1px;">HOME / DASHBOARD</div>', unsafe_allow_html=True)
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE ● ALERTA: ODDS EM QUEDA ● DICA: GESTÃO DE BANCA ATUALIZADA</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;"><span class="pulse-dot"></span>Destaque Live</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">FLAMENGO x PALMEIRAS</div><div style="color:#06b6d4; font-size:10px; margin-top:5px;">BRASILEIRÃO - AO VIVO</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Sugestão</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">OVER 2.5 GOLS</div><div style="color:#00cc66; font-size:10px; margin-top:5px;">88% CONFIDÊNCIA</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:88%;"></div></div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">IA Education</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">GESTÃO 3%</div><div style="color:#9d54ff; font-size:10px; margin-top:5px;">PRESERVE SEU CAPITAL</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:100%;"></div></div></div>', unsafe_allow_html=True)
    
    st.markdown('<div style="height:15px;"></div>', unsafe_allow_html=True)
    
    c4, c5, c6 = st.columns(3)
    with c4: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Tendência</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">ODDS DESAJUSTADAS</div><div style="color:#facc15; font-size:10px; margin-top:5px;">PREMIER LEAGUE</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:75%;"></div></div></div>', unsafe_allow_html=True)
    with c5: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;"><span class="pulse-dot"></span>Scanner</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">ALTA PRESSÃO (HT)</div><div style="color:#fb7185; font-size:10px; margin-top:5px;">7 PARTIDAS ENCONTRADAS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:65%;"></div></div></div>', unsafe_allow_html=True)
    with c6: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">IA Performance</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">ASSERTIVIDADE 92%</div><div style="color:#22c55e; font-size:10px; margin-top:5px;">CRIZAL ACTIVE PRO</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:92%;"></div></div></div>', unsafe_allow_html=True)

# 2. TELA LOCALIZAR APOSTA (SISTEMA DE PASTAS SEM QUEBRAR O DESIGN)
elif st.session_state.aba_ativa == "analise":
    
    if st.session_state.cat_selecionada is None:
        st.markdown('<div style="color:white; font-weight:900; font-size:26px; margin-bottom:20px;">CATEGORIAS</div>', unsafe_allow_html=True)
        cats = ["🇧🇷 BR COMPETIÇÕES", "🌎 CLUBES SUL-AM", "🇪🇺 LIGAS NACIONAIS", "🏆 UEFA COMPETIÇÕES", "📅 INTERNACIONAIS 25/26"]
        cols = st.columns(3)
        for i, cat in enumerate(cats):
            if cols[i % 3].button(cat, key=f"cat_{i}"):
                st.session_state.cat_selecionada = cat
                st.rerun()
    
    elif st.session_state.liga_selecionada is None:
        st.markdown(f'<div style="color:white; font-weight:900; font-size:26px; margin-bottom:20px;">{st.session_state.cat_selecionada}</div>', unsafe_allow_html=True)
        # Exemplo de subpastas
        sub = ["SÉRIE A", "SÉRIE B", "COPA DO BRASIL", "ESTADUAIS"] if "BR" in st.session_state.cat_selecionada else ["CHAMPIONS", "EUROPA LEAGUE"]
        cols = st.columns(3)
        for i, liga in enumerate(sub):
            if cols[i % 3].button(liga, key=f"liga_{i}"):
                st.session_state.liga_selecionada = liga
                st.rerun()
        st.button("⬅ VOLTAR PARA CATEGORIAS", on_click=lambda: setattr(st.session_state, 'cat_selecionada', None))
    
    else:
        st.markdown(f'<div style="color:white; font-weight:900; font-size:26px;">{st.session_state.liga_selecionada}</div>', unsafe_allow_html=True)
        st.button("⬅ TROCAR CAMPEONATO", on_click=lambda: setattr(st.session_state, 'liga_selecionada', None))

# --- [LOCK] FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | KEY: GIAE-V17-ELITE-RECOVERY</div><div>GESTOR IA PRO v34.0 | JARVIS PROTECT V34</div></div>""", unsafe_allow_html=True)
