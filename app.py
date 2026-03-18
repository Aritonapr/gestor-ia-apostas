import streamlit as st
import time
import random
from datetime import datetime

# ==============================================================================
# [GIAE KERNEL SHIELD v57.20 - WORLD CUP 2026 FORCED INJECTION]
# FIX: COPA DO MUNDO 2026 DISPONÍVEL NO SCANNER | GRID 8 CARDS | DESIGN ELITE
# INTEGRITY: NO ABBREVIATIONS | FULL CODE RESTORED | INTERFACE LOCKED
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- [FUNÇÃO GLOBAL DE RENDERIZAÇÃO DE CARDS] ---
def draw_card(title, value, perc):
    """Renderiza os cards de alta performance do Anderson conforme padrão visual."""
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div class="conf-bar-bg">
                <div class="conf-bar-fill" style="width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- [LOCK] BLOCO DE SEGURANÇA CSS (NÃO ALTERAR ESTRUTURA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');
    
    /* RESET DE INTERFACE STREAMLIT */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }
    
    /* SIDEBAR: DESIGN TRANSPARENTE COM LINHA E TEXTO EM UMA LINHA */
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; 
        color: #94a3b8 !important; 
        border: none !important; 
        border-bottom: 1px solid #1a202c !important; 
        text-align: left !important; 
        width: 100% !important; 
        padding: 18px 25px !important; 
        font-size: 10px !important; 
        text-transform: uppercase !important;
        white-space: nowrap !important; 
        border-radius: 0px !important;
        display: block !important;
        cursor: pointer !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { 
        color: #ffffff !important; 
        border-left: 4px solid #6d28d9 !important; 
        background: rgba(26, 36, 45, 0.8) !important; 
    }
    
    /* BOTÕES DA ÁREA PRINCIPAL: REMOÇÃO DO BRANCO + GRADIENTE ROXO */
    [data-testid="stMainBlockContainer"] div.stButton > button {
        background: linear-gradient(90deg, #6d28d9 0%, #4c1d95 100%) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        font-size: 11px !important;
        border-radius: 4px !important;
        padding: 12px 20px !important;
        transition: 0.3s !important;
        cursor: pointer !important;
    }
    [data-testid="stMainBlockContainer"] div.stButton > button:hover {
        background: linear-gradient(90deg, #7c3aed 0%, #6d28d9 100%) !important;
        box-shadow: 0 0 15px rgba(109, 40, 217, 0.3) !important;
    }

    /* CABEÇALHO (HEADER) COM EFEITOS, LUPA E CURSOR MAOZINHA */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; }
    
    .logo-link { 
        color: #9d54ff !important; 
        font-weight: 900; 
        font-size: 20px !important; 
        text-transform: uppercase; 
        letter-spacing: 1px; 
        text-decoration: none !important; 
        margin-right: 40px; 
        cursor: pointer !important;
    }
    
    .nav-items { display: flex; gap: 20px; align-items: center; }
    .nav-items span { 
        color: #ffffff; 
        font-size: 9px !important; 
        text-transform: uppercase; 
        opacity: 0.7; 
        white-space: nowrap; 
        cursor: pointer !important; 
        transition: 0.3s ease; 
        font-weight: 600;
    }
    .nav-items span:hover { 
        opacity: 1; 
        color: #9d54ff !important; 
        text-shadow: 0 0 10px rgba(157, 84, 255, 0.5);
    }
    
    .header-right { display: flex; align-items: center; gap: 20px; }
    .search-icon { color: #ffffff; font-size: 14px; cursor: pointer !important; opacity: 0.8; transition: 0.3s; }
    
    .registrar-pill { 
        color: #ffffff !important; 
        font-size: 10px !important; 
        font-weight: 700; 
        border: 1px solid #ffffff !important; 
        padding: 6px 15px !important; 
        border-radius: 20px !important; 
        transition: 0.3s; 
        cursor: pointer !important;
    }
    .entrar-grad { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: white !important; 
        padding: 7px 20px !important; 
        border-radius: 4px !important; 
        font-weight: 800 !important; 
        font-size: 10px !important; 
        transition: 0.3s; 
        cursor: pointer !important;
    }
    
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; transition: 0.3s; }
    .highlight-card:hover { border-color: #6d28d9; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }
    
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px !important; border-radius: 8px; margin-bottom: 10px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    
    div[data-baseweb="select"] > div { background-color: #1a202c !important; color: white !important; border-color: #334155 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- [INICIALIZAÇÃO DE MEMÓRIA] ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None

# --- [BASE DE DADOS INTEGRAL 2025/2026] ---
DADOS_HIEARARQUIA = {
    "COPA DO MUNDO 2026": {
        "Fase de Grupos": {
            "Grupo Principal": ["Brasil", "Argentina", "França", "Alemanha", "Espanha", "Portugal", "Inglaterra", "Itália", "Holanda", "Bélgica", "EUA", "México", "Canadá", "Uruguai", "Colômbia", "Japão"]
        }
    },
    "FUTEBOL BRASIL": {
        "Campeonato Brasileiro": {
            "Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo", "São Paulo", "Grêmio", "Atlético-MG", "Fluminense", "Internacional", "Corinthians", "Bahia", "Cruzeiro", "Vasco", "Athletico-PR", "Fortaleza", "Cuiabá", "Criciúma", "Juventude", "Vitória", "Bragantino", "Atlético-GO"],
            "Brasileirão Série B": ["Santos", "Sport", "Coritiba", "Goiás", "Ceará", "Novorizontino", "Vila Nova", "Amazonas", "Operário-PR", "Avaí", "Chapecoense", "Ponte Preta"],
            "Brasileirão Série C": ["Náutico", "Figueirense", "Remo", "CSA", "Volta Redonda", "Sampaio Corrêa", "ABC", "Botafogo-PB", "Londrina", "Caxias"],
            "Brasileirão Série D": ["Santa Cruz", "Portuguesa", "Treze", "Iguatu", "Brasil de Pelotas", "Anápolis", "Maringá", "Itabuna"]
        },
        "Copas Nacionais": {
            "Copa do Brasil": ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Atlético-MG", "Grêmio", "Bahia", "Internacional"],
            "Copa do Nordeste": ["Bahia", "Vitória", "Fortaleza", "Ceará", "Sport", "Náutico", "CRB", "Sampaio Corrêa"]
        },
        "Campeonatos Estaduais": {
            "Paulistão": ["Palmeiras", "Santos", "São Paulo", "Corinthians", "Bragantino"],
            "Carioca": ["Flamengo", "Fluminense", "Vasco", "Botafogo"],
            "Mineiro": ["Atlético-MG", "Cruzeiro", "América-MG"],
            "Gaúcho": ["Grêmio", "Internacional", "Juventude"]
        }
    },
    "EUROPA (LIGAS E COPAS)": {
        "Principais Ligas": {
            "Premier League": ["Man. City", "Arsenal", "Liverpool", "Chelsea", "Tottenham"],
            "La Liga": ["Real Madrid", "Barcelona", "Atlético Madrid", "Girona"],
            "Serie A (Itália)": ["Inter de Milão", "Milan", "Juventus", "Napoli"],
            "Bundesliga": ["Bayer Leverkusen", "Bayern Munique", "Dortmund"],
            "UEFA Champions League": ["Real Madrid", "Man. City", "Bayern Munique", "Arsenal", "PSG"]
        }
    }
}

# --- [CABECALHO: IDENTIDADE VISUAL ELITE] ---
st.markdown("""
    <div class="betano-header">
        <div style="display:flex; align-items:center;">
            <a class="logo-link">GESTOR IA</a>
            <div class="nav-items">
                <span>APOSTAS ESPORTIVAS</span>
                <span>APOSTAS AO VIVO</span>
                <span>OPORTUNIDADES IA</span>
                <span>ESTATÍSTICAS AVANÇADAS</span>
                <span>MERCADO PROBABILÍSTICO</span>
                <span>ASSERTIVIDADE IA</span>
            </div>
        </div>
        <div class="header-right">
            <div class="search-icon">🔍</div>
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- [SIDEBAR: NAVEGAÇÃO] ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): pass
    if st.button("💰 GESTÃO DE BANCA"): pass
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): pass
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): pass
    if st.button("⚽ APOSTAS POR GOLS"): pass

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- [ABA: HOME - 8 CARDS] ---
if st.session_state.aba_ativa == "home":
    st.markdown("""<div class="news-ticker">● LIVE: IA OPERACIONAL ● HIERARQUIA v57.20 ATIVA ● COPA 2026 DISPONÍVEL</div>""", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("Destaque Live", "FLAMENGO x PALMEIRAS", 90)
    with h2: draw_card("Sugestão", "OVER 2.5 GOLS", 88)
    with h3: draw_card("IA Education", "GESTÃO 3%", 100)
    with h4: draw_card("Tendência", "ODDS EM QUEDA", 75)
    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("Scanner", "ALTA PRESSÃO (HT)", 60)
    with h6: draw_card("Performance", "ASSERTIVIDADE 92%", 92)
    with h7: draw_card("Volume", "MERCADO EM ALTA", 80)
    with h8: draw_card("Proteção", "JARVIS SUPREME", 100)

# --- [ABA: SCANNER - 8 CARDS COM COPA DO MUNDO] ---
elif st.session_state.aba_ativa == "analise":
    @st.fragment
    def area_scanner():
        st.markdown("""<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">🎯 SCANNER PRÉ-LIVE</div>""", unsafe_allow_html=True)
        
        # Seletores Hierárquicos
        c1, c2, c3 = st.columns(3)
        categoria_selecionada = c1.selectbox("🌎 CATEGORIA", list(DADOS_HIEARARQUIA.keys()))
        tipo_selecionado = c2.selectbox("📂 TIPO", list(DADOS_HIEARARQUIA[categoria_selecionada].keys()))
        campeonato_selecionado = c3.selectbox("🏆 CAMPEONATO", list(DADOS_HIEARARQUIA[categoria_selecionada][tipo_selecionado].keys()))
        
        # Seleção de Times
        t1, t2 = st.columns(2)
        lista_times = DADOS_HIEARARQUIA[categoria_selecionada][tipo_selecionado][campeonato_selecionado]
        casa = t1.selectbox("🏠 CASA", lista_times)
        fora = t2.selectbox("🚀 VISITANTE", [x for x in lista_times if x != casa])
        
        if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
            st.session_state.analise_bloqueada = {"casa": casa, "fora": fora, "vencedor": casa, "gols": "OVER 1.5 REAL", "data": datetime.now().strftime("%H:%M")}
            st.rerun()
            
        if st.session_state.analise_bloqueada:
            m = st.session_state.analise_bloqueada
            st.markdown(f"<div style='color:#9d54ff; font-weight:900; font-size:18px; margin:20px 0;'>RESULTADO: {m['casa']} vs {m['fora']}</div>", unsafe_allow_html=True)
            
            # GRADE DE 8 QUADROS NO SCANNER
            r1, r2, r3, r4 = st.columns(4)
            with r1: draw_card("VENCEDOR", m['vencedor'], 85)
            with r2: draw_card("MERCADO GOLS", m['gols'], 70)
            with r3: draw_card("STAKE", "R$ 10.00", 100)
            with r4: draw_card("ESCANTEIOS", "MAIS DE 9.5", 65)
            st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
            r5, r6, r7, r8 = st.columns(4)
            with r5: draw_card("TIROS DE META", "14-16 TOTAIS", 40)
            with r6: draw_card("CHUTES AO GOL", "CASA +5.5", 50)
            with r7: draw_card("DEFESAS GOLEIRO", "VISITANTE 4+", 30)
            with r8: draw_card("ÍNDICE PRESSÃO", "GOL MADURO 68%", 68)
            
            if st.button("📥 ENVIAR PARA HISTÓRICO", use_container_width=True):
                st.session_state.historico_calls.append(m)
                st.toast("✅ ADICIONADO AO HISTÓRICO!")
                
    area_scanner()

# --- [ABA: HISTÓRICO - SEM FLASH] ---
elif st.session_state.aba_ativa == "historico":
    st.markdown("""<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">📜 HISTÓRICO DE CALLS</div>""", unsafe_allow_html=True)
    @st.fragment
    def render_history_list():
        if not st.session_state.historico_calls: st.info("Histórico vazio.")
        else:
            for i, call in enumerate(reversed(st.session_state.historico_calls)):
                idx_real = len(st.session_state.historico_calls) - 1 - i
                col_info, col_del = st.columns([0.9, 0.1])
                with col_info: st.markdown(f"""<div class="history-card-box"><span style="color:#9d54ff; font-weight:900;">[{call['data']}]</span> <span style="color:white; margin-left:15px;">{call['casa']} x {call['fora']}</span><span style="color:#06b6d4; float:right;">{call['gols']}</span></div>""", unsafe_allow_html=True)
                with col_del: 
                    if st.button("🗑️", key=f"del_v20_{idx_real}"):
                        st.session_state.historico_calls.pop(idx_real)
                        st.rerun(scope="fragment")
    render_history_list()

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.20 LOCKED</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
