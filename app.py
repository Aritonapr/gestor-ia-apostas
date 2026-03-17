import streamlit as st
import time
import random
from datetime import datetime

# ==============================================================================
# [GIAE KERNEL SHIELD v57.3 - JARVIS NIGHT VISION REFINEMENT]
# FIX: HISTORY VISIBILITY | NEON CONTRAST | TOTAL LAYOUT PRESERVATION
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- [FUNÇÃO DE BACKEND: INJEÇÃO DE DADOS NO HISTÓRICO] ---
def registrar_analise_no_historico():
    if st.session_state.analise_bloqueada:
        # Registra no histórico e ativa o aviso de sucesso
        st.session_state.historico_calls.append(st.session_state.analise_bloqueada)
        st.session_state.mostrar_sucesso = True

# --- [NÚCLEO DE MEMÓRIA PERSISTENTE] ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'banca_atual' not in st.session_state:
    st.session_state.banca_atual = 1000.0
if 'historico_calls' not in st.session_state:
    st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state:
    st.session_state.analise_bloqueada = None
if 'mostrar_sucesso' not in st.session_state:
    st.session_state.mostrar_sucesso = False

# --- [LOCK] BLOCO DE SEGURANÇA CSS (ESTRUTURA INTEGRAL DAS IMAGENS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
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
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; letter-spacing: 1px; text-decoration: none !important; margin-right: 60px; }
    .nav-items { display: flex; gap: 15px; }
    .nav-items span { color: #ffffff; font-size: 10px !important; text-transform: uppercase; opacity: 0.8; }
    .header-right { display: flex; align-items: center; gap: 15px; min-width: 280px; justify-content: flex-end; }
    .registrar-pill { color: #ffffff !important; font-size: 10px !important; font-weight: 700; border: 1px solid #ffffff !important; padding: 6px 15px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 7px 20px !important; border-radius: 4px !important; font-weight: 800 !important; font-size: 10px !important; }

    /* [04] SIDEBAR BOTÕES */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; border-radius: 0px !important;
        text-align: left !important; width: 100% !important; padding: 18px 25px !important; 
        font-size: 10px !important; text-transform: uppercase !important; 
    }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }

    /* [05] CARDS & RESULTADOS */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; transition: 0.3s; }
    .highlight-card:hover { border-color: #6d28d9; transform: translateY(-3px); }
    .pulse-dot { height: 6px; width: 6px; background-color: #22c55e; border-radius: 50%; display: inline-block; margin-right: 5px; animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    /* [06] ESTILIZAÇÃO CARDS DE HISTÓRICO (VISIBILIDADE) */
    .history-card {
        background: #161b22 !important;
        border: 1px solid #30363d !important;
        padding: 15px !important;
        border-radius: 8px !important;
        margin-bottom: 10px !important;
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        transition: 0.3s !important;
    }
    .history-card:hover { border-color: #6d28d9 !important; background: #1c2128 !important; }

    /* FOOTER */
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DADOS COMPLETA ---
DADOS_HIEARARQUIA = {
    "BRASIL": {
        "Nacional": {
            "Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo", "São Paulo", "Grêmio", "Atlético-MG", "Fluminense", "Internacional", "Corinthians", "Bahia", "Cruzeiro", "Vasco", "Athletico-PR", "Fortaleza", "Cuiabá", "Criciúma", "Juventude", "Vitória", "Bragantino", "Atlético-GO"],
            "Brasileirão Série B": ["Santos", "Sport", "Coritiba", "Goiás", "Ceará", "Novorizontino", "Vila Nova", "Amazonas", "Operário-PR", "Avaí", "Chapecoense", "Ponte Preta"],
            "Brasileirão Série C": ["Náutico", "Figueirense", "Remo", "CSA", "Volta Redonda", "Sampaio Corrêa", "ABC", "Botafogo-PB", "Londrina", "Ferroviário"],
            "Brasileirão Série D": ["Santa Cruz", "Inter de Limeira", "Anápolis", "Maringá", "Brasil de Pelotas", "Retrô", "Iguatu", "Treze", "América-RN"]
        }
    },
    "EUROPA": {
        "Competições UEFA": {
            "UEFA Champions League": ["Real Madrid", "Man. City", "Bayern Munique", "Arsenal", "Barcelona", "Inter de Milão", "PSG", "Dortmund", "Juventus", "Bayer Leverkusen"]
        }
    }
}

# --- CABEÇALHO FIXO ---
st.markdown("""<div class="betano-header"><div class="header-left"><a class="logo-link">GESTOR IA</a><div class="nav-items"><span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>OPORTUNIDADES IA</span><span>Estatísticas Avançadas</span><span>PROBABILIDADES REAIS</span><span>Assertividade IA</span></div></div><div class="header-right"><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div></div>""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE"): 
        st.session_state.aba_ativa = "analise"
        st.session_state.analise_bloqueada = None
        st.session_state.mostrar_sucesso = False
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "scanner_live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    st.button("📅 JOGOS DO DIA")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("⚽ APOSTAS POR GOLS")

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- [ABA] HOME (8 CARDS) ---
if st.session_state.aba_ativa == "home":
    st.markdown("""<div class="news-ticker">● LIVE: IA OPERACIONAL ● HIERARQUIA v57.3 ATIVA ● JARVIS NIGHT VISION</div>""", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px;"><span class="pulse-dot"></span>Destaque Live</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">FLAMENGO x PALMEIRAS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:90%;"></div></div></div>""", unsafe_allow_html=True)
    with h2: st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">Sugestão</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">OVER 2.5 GOLS</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:88%;"></div></div></div>""", unsafe_allow_html=True)
    with h3: st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">IA Education</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">GESTÃO 3%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:100%;"></div></div></div>""", unsafe_allow_html=True)
    with h4: st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">Tendência</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">ODDS EM QUEDA</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:75%;"></div></div></div>""", unsafe_allow_html=True)
    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
    h5, h6, h7, h8 = st.columns(4)
    with h5: st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">Scanner</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">ALTA PRESSÃO (HT)</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:60%;"></div></div></div>""", unsafe_allow_html=True)
    with h6: st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">Performance</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">ASSERTIVIDADE 92%</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:92%;"></div></div></div>""", unsafe_allow_html=True)
    with h7: st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">Volume</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">MERCADO EM ALTA</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:80%;"></div></div></div>""", unsafe_allow_html=True)
    with h8: st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">Proteção</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">JARVIS SUPREME</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:100%;"></div></div></div>""", unsafe_allow_html=True)

# --- [ABA] SCANNER PRÉ-LIVE ---
elif st.session_state.aba_ativa == "analise":
    st.markdown("""<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">🎯 SCANNER PRÉ-LIVE</div>""", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: cat = st.selectbox("🌎 CATEGORIA", list(DADOS_HIEARARQUIA.keys()))
    with c2: tip = st.selectbox("📂 TIPO", list(DADOS_HIEARARQUIA[cat].keys()))
    with c3: cmp = st.selectbox("🏆 CAMPEONATO", list(DADOS_HIEARARQUIA[cat][tip].keys()))
    t1, t2 = st.columns(2)
    with t1: casa = st.selectbox("🏠 CASA", DADOS_HIEARARQUIA[cat][tip][cmp])
    with t2: fora = st.selectbox("🚀 VISITANTE", [t for t in DADOS_HIEARARQUIA[cat][tip][cmp] if t != casa])

    if st.button("⚡ EXECUTAR ALGORITIMO"):
        st.session_state.analise_bloqueada = {
            "casa": casa, "fora": fora, "data": datetime.now().strftime("%d/%m %H:%M"),
            "vencedor": casa, "gols": "OVER 1.5 REAL", "cantos": "MAIS DE 9.5"
        }
        st.session_state.mostrar_sucesso = False

    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"""<div style="color:#9d54ff; font-weight:900; font-size:18px; margin: 20px 0 10px 0; text-transform: uppercase;">RESULTADO ALGORITIMO: {m['casa']} vs {m['fora']}</div>""", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">VENCEDOR</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">{m['vencedor']}</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:76%;"></div></div></div>""", unsafe_allow_html=True)
        with r2: st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">MERCADO GOLS</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">{m['gols']}</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:85%;"></div></div></div>""", unsafe_allow_html=True)
        with r3: st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">STAKE</div><div style="color:#22c55e; font-size:18px; font-weight:900; margin-top:10px;">R$ {st.session_state.banca_atual * 0.01:,.2f}</div></div>""", unsafe_allow_html=True)
        with r4: st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">ESCANTEIOS</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">{m['cantos']}</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:82%;"></div></div></div>""", unsafe_allow_html=True)
        st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
        r5, r6, r7, r8 = st.columns(4)
        with r5: st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">TIROS DE META</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">14-16 TOTAIS</div></div>""", unsafe_allow_html=True)
        with r6: st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">CHUTES AO GOL</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">CASA +5.5</div></div>""", unsafe_allow_html=True)
        with r7: st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">DEFESAS</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">VISITANTE 4+</div></div>""", unsafe_allow_html=True)
        with r8: st.markdown("""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">PRESSÃO</div><div style="color:white; font-size:14px; font-weight:900; margin-top:10px;">GOL MADURO 68%</div></div>""", unsafe_allow_html=True)
        st.markdown('<div style="height:20px;"></div>', unsafe_allow_html=True)
        
        st.button("📥 ENVIAR PARA HISTÓRICO", on_click=registrar_analise_no_historico)
        
        if st.session_state.mostrar_sucesso:
            st.success("✅ ANALISE SALVA COM SUCESSO NO HISTÓRICO!")

# --- [ABA] HISTÓRICO (REFINAMENTO VISUAL) ---
elif st.session_state.aba_ativa == "historico":
    st.markdown("""<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">📜 HISTÓRICO DE CALLS SALVAS</div>""", unsafe_allow_html=True)
    if not st.session_state.historico_calls:
        st.info("Nenhuma call salva até o momento.")
    else:
        for call in reversed(st.session_state.historico_calls):
            st.markdown(f"""
                <div class="history-card">
                    <div>
                        <span style="color:#9d54ff; font-weight:900; font-size:13px; letter-spacing:1px;">[{call['data']}]</span>
                        <span style="color:white; font-weight:800; font-size:15px; margin-left:15px;">{call['casa']} x {call['fora']}</span>
                    </div>
                    <div style="display:flex; gap:30px;">
                        <div style="text-align:right;"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Mercado</div><div style="color:#06b6d4; font-size:13px; font-weight:900;">{call['gols']}</div></div>
                        <div style="text-align:right;"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">Win</div><div style="color:#22c55e; font-size:13px; font-weight:900;">{call['vencedor']}</div></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# --- [ABA] GESTÃO ---
elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div style="color:white; font-weight:900; font-size:26px; margin-bottom:15px;">💰 GESTÃO DE BANCA PROFISSIONAL</div>""", unsafe_allow_html=True)
    st.session_state.banca_atual = st.number_input("DEFINIR BANCA TOTAL (R$)", value=st.session_state.banca_atual, step=50.0)

# --- FOOTER ---
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.3 LOCKED</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
