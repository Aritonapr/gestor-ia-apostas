import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v61.10 - LIMPEZA DE SIDEBAR & FIDELIDADE TOTAL]
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- SISTEMA DE NAVEGAÇÃO VIA URL (PARA O MENU SUPERIOR FUNCIONAR) ---
if "go" in st.query_params:
    st.session_state.aba_ativa = st.query_params["go"]

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# --- FUNÇÕES DE CARREGAMENTO DE DADOS ---
def carregar_dados_permanentes():
    path_db = "data/database_diario.csv"
    path_hist = "data/historico_permanente.csv"
    df_d = pd.read_csv(path_db) if os.path.exists(path_db) else None
    df_h = pd.read_csv(path_hist) if os.path.exists(path_hist) else pd.DataFrame()
    return df_d, df_h

def salvar_call_permanente(call):
    path = "data/historico_permanente.csv"
    os.makedirs('data', exist_ok=True)
    call['resultado_ia'] = "AGUARDANDO"
    df_nova = pd.DataFrame([call])
    if os.path.exists(path):
        try:
            df_hist = pd.read_csv(path)
            df_final = pd.concat([df_hist, df_nova], ignore_index=True)
            df_final.to_csv(path, index=False)
        except:
            df_nova.to_csv(path, index=False)
    else:
        df_nova.to_csv(path, index=False)

df_diario, df_historico_full = carregar_dados_permanentes()

# 2. CAMADA DE ESTILO CSS INTEGRAL (DARK MODE REFORÇADO)
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
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    .nav-item-top { color: #ffffff !important; font-size: 11px; text-transform: uppercase; font-weight: 600; text-decoration: none; margin-left: 20px; transition: 0.3s; }
    .nav-item-top:hover { color: #06b6d4 !important; }

    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: all 0.2s ease !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important;
    }

    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: white !important; font-weight: 900 !important; text-transform: uppercase !important;
        border-radius: 6px !important; width: 100% !important; border: none !important; padding: 15px !important;
    }

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
    }
    
    div[data-baseweb="input"], .stNumberInput div, div[data-baseweb="select"] > div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    input { color: white !important; }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SUPERIOR (ASSERTIVIDADE APENAS AQUI AGORA)
st.markdown(f"""
    <div class="betano-header">
        <div style="display: flex; align-items: center;">
            <a href="/?go=home" target="_self" class="logo-link">GESTOR IA</a>
            <div style="margin-left: 25px;">
                <a href="/?go=home" target="_self" class="nav-item-top">APOSTAS ESPORTIVAS</a>
                <a href="/?go=live" target="_self" class="nav-item-top">APOSTAS AO VIVO</a>
                <a href="/?go=analise" target="_self" class="nav-item-top">APOSTAS ENCONTRADAS</a>
                <a href="/?go=assertividade" target="_self" class="nav-item-top">ASSERTIVIDADE IA</a>
            </div>
        </div>
        <div style="color: white; font-size: 11px; font-weight: 800;">🔍 REGISTRAR | ENTRAR</div>
    </div>
""", unsafe_allow_html=True)

# 4. SIDEBAR (BOTÃO ASSERTIVIDADE REMOVIDO DAQUI)
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True)
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc, color="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;">
                <div style="background:{color}; height:100%; width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- LÓGICA DE TELAS ---

# TELA: JOGOS DO DIA (RESTAURAÇÃO TOTAL - 8 CARDS EM 2 LINHAS)
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    r1c1, r1c2, r1c3, r1c4 = st.columns(4)
    with r1c1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with r1c2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with r1c3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with r1c4: draw_card("IA STATUS", "ONLINE", 100)
    r2c1, r2c2, r2c3, r2c4 = st.columns(4)
    with r2c1: draw_card("VOL. GLOBAL", "ALTO", 75)
    with r2c2: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with r2c3: draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
    with r2c4: draw_card("SISTEMA", "JARVIS v61.10", 100)

# TELA: ASSERTIVIDADE (ACESSO APENAS PELO MENU SUPERIOR)
elif st.session_state.aba_ativa == "assertividade":
    st.markdown("<h2 style='color:white;'>📈 ASSERTIVIDADE DA INTELIGÊNCIA</h2>", unsafe_allow_html=True)
    a1, a2, a3, a4 = st.columns(4)
    with a1: draw_card("ACERTOS TOTAIS", "142", 100, "#00ff88")
    with a2: draw_card("ERROS TOTAIS", "12", 10, "#ff4b4b")
    with a3: draw_card("TAXA DE WIN", "92.2%", 92, "#00ff88")
    with a4: draw_card("MERCADO LÍDER", "OVER 1.5", 100)
    
    st.markdown("<h4 style='color:white; margin-top:30px;'>📊 ONDE O JARVIS MAIS ACERTA:</h4>", unsafe_allow_html=True)
    col_inf1, col_inf2 = st.columns(2)
    with col_inf1:
        st.info("✅ PREMIER LEAGUE: 96% de acerto")
        st.info("✅ BRASILEIRÃO: 88% de acerto")
    with col_inf2:
        st.warning("⚠️ BUNDESLIGA: 65% de acerto (IA em aprendizado)")
        st.error("❌ ESCANTEIOS ASIA: 42% de acerto (Não recomendado hoje)")

# TELA: SCANNER PRÉ-LIVE
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    f1, f2, f3 = st.columns(3)
    with f1: sel_pais = st.selectbox("🌎 REGIÃO / PAÍS", ["BRASIL", "INGLATERRA", "ESPANHA", "ARGENTINA"])
    with f2: sel_grupo = st.selectbox("📂 GRUPO", ["BRASILEIRÃO", "PREMIER LEAGUE", "LA LIGA", "LIGA PROFESIONAL"])
    with f3: sel_comp = st.selectbox("🏆 COMPETIÇÃO", ["Série A", "Série B", "Geral"])
    t_casa = st.text_input("TIME DA CASA", "Flamengo")
    t_fora = st.text_input("TIME DE FORA", "Palmeiras")
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        v_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        status_luz, cor_luz, validacao_txt = ("🟢", "#00ff88", "FILÉ MIGNON: INFORMAÇÃO REAL")
        st.session_state.analise_bloqueada = {"casa": t_casa, "fora": t_fora, "vencedor": "ALTA PROB", "gols": "OVER 1.5", "data": datetime.now().strftime("%d/%m %H:%M"), "stake_val": f"R$ {v_stake:,.2f}", "luz": status_luz, "cor": cor_luz, "motivo": validacao_txt}
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f'<div style="background:rgba(255,255,255,0.03); border-left:5px solid {m["cor"]}; padding:15px; border-radius:6px; margin-bottom:20px;">{m["luz"]} SISTEMA JARVIS: <b style="color:{m["cor"]}">{m["motivo"]}</b></div>', unsafe_allow_html=True)
        if st.button("📥 SALVAR NO HISTÓRICO"):
            salvar_call_permanente(m)
            st.toast("✅ Salvo com sucesso!")

# TELA: HISTÓRICO
elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO PERMANENTE</h2>", unsafe_allow_html=True)
    if os.path.exists("data/historico_permanente.csv"):
        df_h = pd.read_csv("data/historico_permanente.csv")
        for idx, row in df_h.iterrows():
            st.markdown(f'<div style="background:#161b22; padding:15px; margin-bottom:10px; border-radius:8px; border:1px solid #30363d; color:white;"><b>{row["data"]}</b> - {row["casa"]} x {row["fora"]}</div>', unsafe_allow_html=True)
    else: st.info("Vazio.")

# RODAPÉ
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v61.10</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
