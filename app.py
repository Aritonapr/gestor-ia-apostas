import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v59.00 - RESTAURAÇÃO TOTAL & NAVEGAÇÃO]
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- PONTE DE NAVEGAÇÃO (PARA O MENU SUPERIOR FUNCIONAR) ---
if "aba" in st.query_params:
    st.session_state.aba_ativa = st.query_params["aba"]

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None

# --- FUNÇÕES DE DADOS (MEMÓRIA ETERNA) ---
def carregar_historico_permanente():
    path = "data/historico_permanente.csv"
    if os.path.exists(path):
        try: return pd.read_csv(path)
        except: return pd.DataFrame()
    return pd.DataFrame()

def salvar_call_permanente(call):
    path = "data/historico_permanente.csv"
    os.makedirs('data', exist_ok=True)
    call['resultado_ia'] = "AGUARDANDO"
    df_nova = pd.DataFrame([call])
    if os.path.exists(path):
        df_hist = pd.read_csv(path)
        df_final = pd.concat([df_hist, df_nova], ignore_index=True)
    else:
        df_final = df_nova
    df_final.to_csv(path, index=False)

def carregar_jogos_diarios():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try: return pd.read_csv(path)
        except: return None
    return None

df_diario = carregar_jogos_diarios()
df_historico_full = carregar_historico_permanente()

# 2. CAMADA DE ESTILO CSS INTEGRAL (RESTAURADO v58.00)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000;
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px; text-transform: uppercase; text-decoration: none; }
    .nav-item-link { color: #ffffff !important; font-size: 11px; text-transform: uppercase; font-weight: 600; text-decoration: none; margin-left: 22px; }
    .nav-item-link:hover { color: #06b6d4 !important; }

    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }

    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: white !important; font-weight: 900 !important; text-transform: uppercase !important; border-radius: 6px !important; width: 100% !important; border: none !important; padding: 15px !important;
    }

    /* FORÇAR FUNDO ESCURO NOS INPUTS */
    div[data-baseweb="input"], .stNumberInput div, div[data-baseweb="select"] > div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    input { color: white !important; }

    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; margin-bottom: 15px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SUPERIOR (CORRIGIDO)
st.markdown(f"""
    <div class="betano-header">
        <div style="display: flex; align-items: center;">
            <a href="?aba=home" target="_self" class="logo-link">GESTOR IA</a>
            <div style="margin-left: 30px; display: flex;">
                <a href="?aba=home" target="_self" class="nav-item-link">APOSTAS ESPORTIVAS</a>
                <a href="?aba=live" target="_self" class="nav-item-link">APOSTAS AO VIVO</a>
                <a href="?aba=analise" target="_self" class="nav-item-link">APOSTAS ENCONTRADAS</a>
                <a href="?aba=assertividade" target="_self" class="nav-item-link" style="color:#06b6d4 !important;">ASSERTIVIDADE IA</a>
            </div>
        </div>
        <div style="color:white; font-size:12px; font-weight:700;">🔍 REGISTRAR | ENTRAR</div>
    </div>
""", unsafe_allow_html=True)

# 4. SIDEBAR
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📈 ASSERTIVIDADE IA"): st.session_state.aba_ativa = "assertividade"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"

def draw_card(title, value, perc, color="#06b6d4"):
    st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color}; height:100%; width:{perc}%;"></div></div></div>', unsafe_allow_html=True)

# --- TELAS ---

if st.session_state.aba_ativa == "assertividade":
    st.markdown("<h2 style='color:white;'>📈 ASSERTIVIDADE REAL DA IA</h2>", unsafe_allow_html=True)
    if df_historico_full.empty:
        st.info("O JARVIS está aguardando as primeiras operações para calcular a assertividade real.")
    else:
        total = len(df_historico_full)
        greens = len(df_historico_full[df_historico_full['resultado_ia'] == "GREEN"])
        reds = len(df_historico_full[df_historico_full['resultado_ia'] == "RED"])
        win_rate = (greens / (greens + reds) * 100) if (greens + reds) > 0 else 0
        c1, c2, c3, c4 = st.columns(4)
        with c1: draw_card("OPERAÇÕES", str(total), 100)
        with c2: draw_card("GREENS", str(greens), (greens/total*100) if total > 0 else 0, "#00ff88")
        with c3: draw_card("REDS", str(reds), (reds/total*100) if total > 0 else 0, "#ff4b4b")
        with c4: draw_card("TAXA DE WIN", f"{win_rate:.1f}%", win_rate, "#9d54ff")

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    # RESTAURADO OS SELETORES QUE TINHAM SUMIDO
    row_f = st.columns(3)
    with row_f[0]: sel_pais = st.selectbox("🌎 REGIÃO / PAÍS", ["BRASIL", "INGLATERRA", "ESPANHA", "ARGENTINA"])
    with row_f[1]: sel_grupo = st.selectbox("📂 GRUPO", ["BRASILEIRÃO", "PREMIER LEAGUE", "LA LIGA", "LIGA PROFESIONAL"])
    with row_f[2]: sel_comp = st.selectbox("🏆 COMPETIÇÃO", ["Série A", "Série B", "Geral"])
    
    c1, c2 = st.columns(2)
    with c1: t_casa = st.selectbox("🏠 TIME DA CASA", ["Flamengo", "Man City", "Real Madrid", "(Outro)"])
    with c2: t_fora = st.selectbox("🚀 TIME DE FORA", ["Palmeiras", "Arsenal", "Barcelona", "(Outro)"])
    
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        v_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        status_luz, cor_luz, validacao_txt = ("🔴", "#ff4b4b", "ALERTA: DADOS FORA DA ROTINA")
        if df_diario is not None:
            match = df_diario[(df_diario['TIME_CASA'] == t_casa) | (df_diario['TIME_FORA'] == t_fora)]
            if not match.empty: status_luz, cor_luz, validacao_txt = ("🟢", "#00ff88", "FILÉ MIGNON: INFORMAÇÃO REAL")

        st.session_state.analise_bloqueada = {"casa": t_casa, "fora": t_fora, "vencedor": "ALTA PROB", "gols": "OVER 1.5", "data": datetime.now().strftime("%d/%m %H:%M"), "stake_val": f"R$ {v_stake:,.2f}", "luz": status_luz, "cor": cor_luz, "motivo": validacao_txt}
    
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f'<div style="background:rgba(255,255,255,0.03); border-left:5px solid {m["cor"]}; padding:15px; border-radius:6px; margin-bottom:20px;">{m["luz"]} SISTEMA JARVIS: <b style="color:{m["cor"]}">{m["motivo"]}</b></div>', unsafe_allow_html=True)
        st.markdown(f"<h3 style='color:#9d54ff; text-align:center;'>{m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['vencedor'], 85)
        with r2: draw_card("GOLS", m['gols'], 70)
        with r3: draw_card("STAKE", m['stake_val'], 100)
        with r4: draw_card("IA CONF.", "94%", 94)
        if st.button("📥 SALVAR CALL NO HISTÓRICO PERMANENTE"):
            salvar_call_permanente(m)
            st.toast("✅ Salvo! O Juiz processará o resultado às 23:00.")

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO PERMANENTE</h2>", unsafe_allow_html=True)
    if df_historico_full.empty: st.info("Nenhuma call salva ainda.")
    else:
        for idx, row in df_historico_full.iterrows():
            st.markdown(f'<div class="history-card-box" style="background:#161b22; padding:15px; margin-bottom:10px; border-radius:8px; border:1px solid #30363d; color:white;"><b>{row["data"]}</b> - {row["casa"]} x {row["fora"]} | {row["gols"]}</div>', unsafe_allow_html=True)

elif st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    draw_card("IA STATUS", "ONLINE", 100, "#00ff88")

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v59.00</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
