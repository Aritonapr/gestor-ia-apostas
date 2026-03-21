import streamlit as st
import time
import random
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v57.23 - PROTEÇÃO ATIVA]
# DIRETRIZ 1: HEADER DEVE FICAR DENTRO DA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. [CAMADA DE PROTEÇÃO 1] - CSS DE PERSISTÊNCIA E ESTILIZAÇÃO AVANÇADA
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');
    
    /* BLOQUEIO DE FUNDO - ELIMINA FLASH BRANCO */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    [data-testid="stMainBlockContainer"] { padding-top: 65px !important; padding-bottom: 1rem !important; }
    
    /* [DIRETRIZ 2] HEADER BLINDADO COM ACELERAÇÃO DE HARDWARE */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; 
        border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 30px !important; z-index: 1000000; 
        transform: translate3d(0,0,0);
        -webkit-backface-visibility: hidden;
        contain: strict;
    }
    
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-transform: uppercase; letter-spacing: 1px; text-decoration: none !important; margin-right: 40px; }
    .nav-items { display: flex; gap: 20px; align-items: center; }
    .nav-items span { color: #ffffff; font-size: 9px !important; text-transform: uppercase; opacity: 0.7; font-weight: 600; }
    .header-right { display: flex; align-items: center; gap: 20px; }
    .registrar-pill { color: #ffffff !important; font-size: 10px !important; font-weight: 700; border: 1px solid #ffffff !important; padding: 6px 15px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 7px 20px !important; border-radius: 4px !important; font-weight: 800 !important; font-size: 10px !important; }
    
    /* SIDEBAR DESIGN - BOTÕES COM EFEITO v57.23 */
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: rgba(255,255,255,0.02) !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        white-space: nowrap !important; border-radius: 0px !important; display: block !important;
        transition: all 0.2s ease-in-out !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important;
        padding-left: 35px !important; border-left: 3px solid #6d28d9 !important;
    }

    /* BOTÕES DE AÇÃO (EXECUTAR / SALVAR) - ESTILO PREMIUM */
    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: white !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important;
        letter-spacing: 1.5px !important; border-radius: 6px !important;
        width: 100% !important; transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(109, 40, 217, 0.2) !important;
    }
    div.stButton > button:not([data-testid="stSidebar"] *):hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(109, 40, 217, 0.4) !important;
        filter: brightness(1.2) !important;
    }

    /* UI CARDS */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }
    
    /* HISTÓRICO - ESTILIZAÇÃO DA "PASTA" */
    .history-card-box { 
        background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; 
        border-radius: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;
    }
    .history-info { color: #ffffff !important; font-weight: 800 !important; font-size: 13px !important; }
    .history-time { color: #9d54ff !important; font-weight: 900 !important; margin-right: 15px; }
    .history-stake { color: #06b6d4 !important; font-weight: 900 !important; margin-left: 15px; }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. [DIRETRIZ 1] HEADER ANCORADO NA SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div style="display:flex; align-items:center;">
                <div class="logo-link">GESTOR IA</div>
                <div class="nav-items">
                    <span>APOSTAS ESPORTIVAS</span>
                    <span>APOSTAS AO VIVO</span>
                    <span>OPORTUNIDADES IA</span>
                    <span>ASSERTIVIDADE IA</span>
                </div>
            </div>
            <div class="header-right">
                <div class="registrar-pill">REGISTRAR</div>
                <div class="entrar-grad">ENTRAR</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    # --- [INICIALIZAÇÃO DE MEMÓRIA BLINDADA] ---
    if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
    if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
    if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
    if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
    if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

    # --- [NAVEGAÇÃO] ---
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

# --- [FUNÇÃO DE UI] ---
def draw_card(title, value, perc):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div class="conf-bar-bg"><div class="conf-bar-fill" style="width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- [CONTEÚDO DINÂMICO] ---

# 1. HOME
if st.session_state.aba_ativa == "home":
    st.markdown("""<div class="news-ticker">● LIVE: IA OPERACIONAL ● v57.23 ATIVA</div>""", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE", "92%", 92)
    with h3: draw_card("SUGESTÃO", "OVER 2.5 GOLS", 88)
    with h4: draw_card("MERCADO", "ODDS EM QUEDA", 75)
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("SCANNER", "ALTA PRESSÃO", 60)
    with h6: draw_card("STAKE SUGERIDA", f"{st.session_state.stake_padrao}%", 100)
    with h7: draw_card("VOLUME", "EM ALTA", 80)
    with h8: draw_card("PROTEÇÃO", "JARVIS SUPREME", 100)

# 2. SCANNER PRÉ-LIVE (CORREÇÃO DE SALVAMENTO)
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    cat = c1.selectbox("🌎 CATEGORIA", ["🏆 COPA DO MUNDO 2026", "🇧🇷 BRASIL", "🇪🇺 EUROPA"])
    tip = c2.selectbox("📂 TIPO", ["Seleções", "Brasileirão", "Principais Ligas"])
    cmp = c3.selectbox("🏆 COMPETIÇÃO", ["Série A", "Champions", "Libertadores"])
    
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        v_calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        st.session_state.analise_bloqueada = {
            "casa": "Time Casa", "fora": "Time Visitante", "vencedor": "Casa", 
            "gols": "OVER 1.5", "data": datetime.now().strftime("%H:%M"), 
            "stake_val": f"R$ {v_calc:,.2f}"
        }
            
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<div style='color:#9d54ff; font-weight:900; font-size:18px; margin:20px 0;'>RESULTADO: {m['casa']} vs {m['fora']}</div>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['vencedor'], 85)
        with r2: draw_card("MERCADO GOLS", m['gols'], 70)
        with r3: draw_card("STAKE CALC.", m['stake_val'], 100)
        with r4: draw_card("ESCANTEIOS", "MAIS DE 9.5", 65)
        r5, r6, r7, r8 = st.columns(4)
        with r5: draw_card("CONFIANÇA IA", "94%", 94); with r6: draw_card("PRESSÃO", "ATAQUE TOTAL", 88)
        with r7: draw_card("TENDÊNCIA", "ODDS SUBINDO", 60); with r8: draw_card("ALGORITMO", "JARVIS v57", 100)

        # CORREÇÃO: SALVAMENTO ROBUSTO
        if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True):
            st.session_state.historico_calls.append(m.copy())
            st.toast("✅ ENVIADO PARA O HISTÓRICO!")
            time.sleep(0.5)

# 3. GESTÃO DE BANCA
elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
    st.session_state.stake_padrao = st.slider("STAKE (%)", 0.5, 10.0, st.session_state.stake_padrao)

# 4. HISTÓRICO (A "PASTA" DE ENVIOS)
elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    if not st.session_state.historico_calls: 
        st.info("O histórico está vazio. Realize uma análise e clique em 'Salvar'.")
    else:
        for i, call in enumerate(reversed(st.session_state.historico_calls)):
            idx_real = len(st.session_state.historico_calls) - 1 - i
            col_info, col_del = st.columns([0.9, 0.1])
            with col_info:
                st.markdown(f"""
                    <div class="history-card-box">
                        <div class="history-info">
                            <span class="history-time">[{call['data']}]</span> 
                            {call['casa']} x {call['fora']} 
                            <span class="history-stake">{call['stake_val']} | {call['gols']}</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            with col_del:
                if st.button("🗑️", key=f"del_{idx_real}"):
                    st.session_state.historico_calls.pop(idx_real)
                    st.rerun()

# 5. DEMAIS ABAS (PLACEHOLDERS)
elif st.session_state.aba_ativa == "live": st.info("Módulo Scanner em Tempo Real Ativo.")
elif st.session_state.aba_ativa == "vencedores": st.info("Módulo de Vencedores da Competição.")
elif st.session_state.aba_ativa == "gols": st.info("Módulo de Apostas por Gols.")
elif st.session_state.aba_ativa == "escanteios": st.info("Módulo de Apostas por Escanteios.")

# FOOTER FIXO
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.23</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
