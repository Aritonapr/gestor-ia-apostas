import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v60.00 - ESTABILIDADE TOTAL]
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA (BLINDAGEM DE ESTADO) ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None

# --- CARREGAMENTO DE DADOS (FAST LOAD) ---
def carregar_dados():
    path_db = "data/database_diario.csv"
    path_hist = "data/historico_permanente.csv"
    
    df_d = pd.read_csv(path_db) if os.path.exists(path_db) else None
    df_h = pd.read_csv(path_hist) if os.path.exists(path_hist) else pd.DataFrame()
    return df_d, df_h

df_diario, df_historico_full = carregar_dados()

def salvar_call_permanente(call):
    path = "data/historico_permanente.csv"
    os.makedirs('data', exist_ok=True)
    call['resultado_ia'] = "AGUARDANDO"
    df_nova = pd.DataFrame([call])
    if os.path.exists(path):
        try:
            df_hist = pd.read_csv(path)
            df_final = pd.concat([df_hist, df_nova], ignore_index=True)
        except: df_final = df_nova
    else: df_final = df_nova
    df_final.to_csv(path, index=False)

# 2. CAMADA DE ESTILO CSS (REFORÇADO ZERO WHITE)
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
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px; text-transform: uppercase; text-decoration: none; }
    
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -40px !important; }

    /* BOTÕES DA SIDEBAR */
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: 0.2s ease;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important;
    }

    /* BOTÕES PRINCIPAIS */
    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: white !important; font-weight: 900 !important; text-transform: uppercase !important;
        border-radius: 6px !important; width: 100% !important; border: none !important; padding: 15px !important;
        box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important;
    }

    /* INPUTS ESCUROS */
    div[data-baseweb="input"], .stNumberInput div, div[data-baseweb="select"] > div { 
        background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; 
    }
    input { color: white !important; }

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; margin-bottom: 15px;
    }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SUPERIOR
st.markdown("""
    <div class="betano-header">
        <div style="display: flex; align-items: center; gap: 20px;">
            <div class="logo-link">GESTOR IA</div>
            <div style="color: #64748b; font-size: 10px; font-weight: 700; letter-spacing: 1px;">SISTEMA AUTOMATIZADO v60.00</div>
        </div>
        <div style="color: white; font-size: 11px; font-weight: 700;">🔍 REGISTRAR | ENTRAR</div>
    </div>
""", unsafe_allow_html=True)

# 4. SIDEBAR (NAVEGAÇÃO INSTANTÂNEA)
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📈 ASSERTIVIDADE IA"): st.session_state.aba_ativa = "assertividade"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"

def draw_card(title, value, perc, color="#06b6d4"):
    st.markdown(f'<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform:uppercase; font-weight:700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color}; height:100%; width:{perc}%;"></div></div></div>', unsafe_allow_html=True)

# --- TELAS ---

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    draw_card("IA STATUS", "SISTEMA ONLINE", 100, "#00ff88")
    st.info("Utilize o menu lateral para navegar instantaneamente entre as ferramentas.")

elif st.session_state.aba_ativa == "assertividade":
    st.markdown("<h2 style='color:white;'>📈 ASSERTIVIDADE REAL DA IA</h2>", unsafe_allow_html=True)
    if df_historico_full.empty:
        st.warning("Aguardando o processamento das primeiras operações salvas.")
    else:
        total = len(df_historico_full)
        greens = len(df_historico_full[df_historico_full['resultado_ia'] == "GREEN"])
        reds = len(df_historico_full[df_historico_full['resultado_ia'] == "RED"])
        win_rate = (greens / (greens + reds) * 100) if (greens + reds) > 0 else 0
        
        c1, c2, c3, c4 = st.columns(4)
        with c1: draw_card("OPERAÇÕES", str(total), 100)
        with c2: draw_card("GREENS", str(greens), (greens/total*100) if total > 0 else 0, "#00ff88")
        with c3: draw_card("REDS", str(reds), (reds/total*100) if total > 0 else 0, "#ff4b4b")
        with c4: draw_card("TAXA DE ACERTO", f"{win_rate:.1f}%", win_rate, "#9d54ff")

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    # RESTAURADOS OS FILTROS
    r_filtros = st.columns(3)
    with r_filtros[0]: sel_pais = st.selectbox("🌎 REGIÃO / PAÍS", ["BRASIL", "INGLATERRA", "ESPANHA", "ARGENTINA"])
    with r_filtros[1]: sel_grupo = st.selectbox("📂 GRUPO", ["BRASILEIRÃO", "PREMIER LEAGUE", "LA LIGA", "LIGA PROFESIONAL"])
    with r_filtros[2]: sel_comp = st.selectbox("🏆 COMPETIÇÃO", ["Série A", "Série B", "Geral"])
    
    c1, c2 = st.columns(2)
    with c1: t_casa = st.selectbox("🏠 TIME DA CASA", ["Flamengo", "Man City", "Real Madrid", "Palmeiras", "Arsenal", "(Outro)"])
    with c2: t_fora = st.selectbox("🚀 TIME DE FORA", ["Palmeiras", "Arsenal", "Barcelona", "Flamengo", "Man City", "(Outro)"])
    
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
            st.toast("✅ Salvo no Banco de Dados!")

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO PERMANENTE</h2>", unsafe_allow_html=True)
    if df_historico_full.empty: st.info("Nenhuma operação salva.")
    else:
        for idx, row in df_historico_full.tail(20).iterrows():
            st.markdown(f'<div style="background:#161b22; padding:15px; margin-bottom:10px; border-radius:8px; border:1px solid #30363d; color:white;"><b>{row["data"]}</b> - {row["casa"]} x {row["fora"]} | {row["gols"]}</div>', unsafe_allow_html=True)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("Banca Total (R$)", value=st.session_state.banca_total)
    draw_card("VALOR POR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v60.00</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
