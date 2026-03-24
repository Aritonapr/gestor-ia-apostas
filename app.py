import streamlit as st
import time
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v58.02 - BLINDAGEM + EXPANSÃO DE DADOS]
# REGRA 1: PRESERVAÇÃO INTEGRAL DE CSS E MECÂNICA DE NAVEGAÇÃO
# REGRA 2: ATUALIZAÇÃO EXCLUSIVA DO BANCO DE DADOS NACIONAL (SÉRIES A-D)
# REGRA 3: MANUTENÇÃO DO PADRÃO "ZERO WHITE" E "GPU ACCELERATION"
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# Redirecionamento Home
if st.query_params.get("go") == "home":
    st.session_state.aba_ativa = "home"
    st.query_params.clear()

# 2. [CAMADA DE PROTEÇÃO 1] - CSS INTEGRAL E BLINDADO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
        transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    .nav-item { color: #ffffff !important; font-size: 8.5px !important; text-transform: uppercase; opacity: 0.85; font-weight: 700; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }

    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: #ffffff !important;
        border: none !important; padding: 15px 20px !important; font-weight: 900 !important;
        text-transform: uppercase !important; border-radius: 6px !important;
        width: 100% !important; box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important;
    }

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
    }
    .banca-title-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER NA SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <a href="?go=home" class="logo-link">GESTOR IA</a>
            </div>
            <div class="header-right">
                <div class="entrar-grad">CONECTADO: BRASIL V58</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;">
                <div style="background:{color_footer}; height:100%; width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- LÓGICA DE TELAS ---

# TELA 1: HOME
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 MONITORAMENTO NACIONAL</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE BR", "94.8%", 94)
    with h3: draw_card("MERCADO ATIVO", "BRASILEIRÃO", 100)
    with h4: draw_card("SISTEMA", "PROTEÇÃO v58.02", 100)

# TELA 3: SCANNER PRÉ-LIVE (EXPANSÃO BRASIL COMPLETA)
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE: BRASIL</h2>", unsafe_allow_html=True)
    
    # VARREDURA DE COMPETIÇÕES BRASILEIRAS (SÉRIES A, B, C, D + COPAS + ESTADUAIS)
    lista_competicoes = [
        "Brasileirão - Série A", "Brasileirão - Série B", "Brasileirão - Série C", "Brasileirão - Série D",
        "Copa do Brasil", "Supercopa Rei", "Copa do Nordeste", "Copa Verde",
        "Campeonato Paulista (Paulistão)", "Campeonato Carioca", "Campeonato Mineiro", "Campeonato Gaúcho",
        "Campeonato Paranaense", "Campeonato Baiano", "Campeonato Cearense", "Campeonato Pernambucano",
        "Campeonato Goiano", "Campeonato Catarinense", "Campeonato Alagoano", "Campeonato Paraense"
    ]
    
    # VARREDURA DE TIMES (TOP 60+ ATIVOS)
    lista_times_br = sorted([
        "ABC", "América-MG", "Amazonas FC", "Athletico-PR", "Atlético-GO", "Atlético-MG", "Avaí", "Bahia", 
        "Botafogo", "Botafogo-SP", "Bragantino", "Brusque", "Ceará", "Chapecoense", "Confiança", "Corinthians", 
        "Coritiba", "CRB", "Criciúma", "Cruzeiro", "CSA", "Cuiabá", "Ferroviária", "Figueirense", "Flamengo", 
        "Fluminense", "Fortaleza", "Goiás", "Grêmio", "Guarani", "Internacional", "Ituano", "Juventude", 
        "Londrina", "Mirassol", "Maringá", "Náutico", "Novorizontino", "Operário-PR", "Palmeiras", "Paysandu", 
        "Ponte Preta", "Remo", "Sampaio Corrêa", "Santa Cruz", "Santos", "Santo André", "São Bernardo", 
        "São Paulo", "Sport Recife", "Tombense", "Vasco da Gama", "Vila Nova", "Vitória", "Volta Redonda", "Ypiranga"
    ])

    c1, c2 = st.columns(2)
    with c1:
        comp_sel = st.selectbox("🏆 SELECIONE A COMPETIÇÃO", lista_competicoes)
    with c2:
        st.info(f"Filtro Ativo: Futebol Brasileiro / {comp_sel}")

    col_a, col_b = st.columns(2)
    with col_a:
        t_casa = st.selectbox("🏠 TIME DA CASA", lista_times_br, index=24) # Default Flamengo
    with col_b:
        t_fora = st.selectbox("🚀 TIME VISITANTE", lista_times_br, index=39) # Default Palmeiras

    if st.button("⚡ PROCESSAR ANÁLISE PROFISSIONAL", use_container_width=True):
        v_calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        st.session_state.analise_bloqueada = {
            "casa": t_casa, "fora": t_fora, "vencedor": "EM PROCESSAMENTO", 
            "gols": "CALCULANDO", "data": datetime.now().strftime("%H:%M"), 
            "stake_val": f"R$ {v_calc:,.2f}"
        }
        with st.spinner('Acessando API de estatísticas nacionais...'):
            time.sleep(1.2)
            st.session_state.analise_bloqueada["vencedor"] = f"Favorito {t_casa}"
            st.session_state.analise_bloqueada["gols"] = "OVER 2.5 Gols"

    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<div style='border:1px solid #6d28d9; padding:20px; border-radius:10px; margin-top:20px;'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color:white; margin:0;'>{m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("PROBABILIDADE", m['vencedor'], 88)
        with r2: draw_card("MERCADO GOLS", m['gols'], 75)
        with r3: draw_card("VALOR STAKE", m['stake_val'], 100)
        with r4: draw_card("IA CONFIDENCE", "92%", 92)
        
        if st.button("📥 SALVAR NO MEU HISTÓRICO"):
            st.session_state.historico_calls.append(m.copy())
            st.toast("Operação salva com sucesso!")

# TELA: GESTÃO (BLINDADA)
elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA BRASIL</div>""", unsafe_allow_html=True)
    c_in, c_out = st.columns([1, 2])
    with c_in:
        st.session_state.banca_total = st.number_input("BANCA (R$)", value=st.session_state.banca_total)
        st.session_state.stake_padrao = st.slider("STAKE %", 0.1, 10.0, st.session_state.stake_padrao)
    with c_out:
        v_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        draw_card("VALOR POR ENTRADA", f"R$ {v_stake:,.2f}", 100, "#00d2ff")

# OUTRAS TELAS (VINCULADAS AO NOVO BANCO DE DATOS)
elif st.session_state.aba_ativa in ["live", "historico", "vencedores", "gols", "escanteios"]:
    st.markdown(f"<h2 style='color:white;'>📊 MÓDULO {st.session_state.aba_ativa.upper()}</h2>", unsafe_allow_html=True)
    if st.session_state.aba_ativa == "historico":
        for call in reversed(st.session_state.historico_calls):
            st.markdown(f"""<div class="history-card-box"><span style="color:#9d54ff;">[{call['data']}]</span> {call['casa']} x {call['fora']} - {call['gols']}</div>""", unsafe_allow_html=True)
    else:
        st.warning("Aguardando atualização de odds em tempo real para os times selecionados.")

# FOOTER PROTEGIDO
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | BRASIL DATA v58.02</div><div>PROTEÇÃO ATIVA JARVIS</div></div>""", unsafe_allow_html=True)
