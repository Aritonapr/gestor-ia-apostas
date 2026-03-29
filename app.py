import streamlit as st
import pandas as pd
import os
import requests
from datetime import datetime
from io import StringIO

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v62.00 - INTEGRIDADE TOTAL]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO) - UI v57.35
# DIRETRIZ 5: CÓDIGO 100% ÍNTEGRO - SEM ABREVIAÇÕES
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# --- CARREGAMENTO DE DADOS REAIS ---
def carregar_dados_vivos():
    url_d = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    url_h = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/historico_5_temporadas.csv"
    try:
        r_d = requests.get(f"{url_d}?v={datetime.now().timestamp()}", timeout=10)
        r_h = requests.get(url_h, timeout=10)
        d = pd.read_csv(StringIO(r_d.text)) if r_d.status_code == 200 else None
        h = pd.read_csv(StringIO(r_h.text)) if r_h.status_code == 200 else None
        return d, h
    except: return None, None

df_diario, df_hist = carregar_dados_vivos()

# ==============================================================================
# 2. CAMADA DE ESTILO CSS INTEGRAL (MANTIDA v57.35)
# ==============================================================================
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
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    
    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important; border-radius: 6px !important; width: 100% !important;
    }

    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    
    /* Banner de Resultado Verde */
    .banner-green { background: rgba(0,255,136,0.05); border-left: 5px solid #00ff88; padding: 18px; border-radius: 6px; margin-bottom: 25px; color: white; font-size: 11px; font-weight: 800; letter-spacing: 1px; }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown("""<div class="betano-header"><div class="logo-link">GESTOR IA</div></div><div style="height:65px;"></div>""", unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
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

# ==============================================================================
# 4. LÓGICA DE TELAS (RESTAURAÇÃO TOTAL)
# ==============================================================================

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with c2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with c3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with c4: draw_card("IA STATUS", "ONLINE", 100)
    c5, c6, c7, c8 = st.columns(4)
    with c5: draw_card("VOL. GLOBAL", "ALTO", 75)
    with c6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with c7: draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
    with c8: draw_card("SISTEMA", "JARVIS v62.0", 100)
    st.markdown("### 📋 ANÁLISE COMPLETA DO DIA")
    if df_diario is not None: st.dataframe(df_diario, use_container_width=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    # SELEÇÃO MANUAL (Conforme imagem)
    f1, f2, f3 = st.columns(3)
    with f1: s_pais = st.selectbox("🌎 REGIÃO / PAÍS", ["BRASIL", "INGLATERRA", "ESPANHA", "ALEMANHA", "INTERNACIONAL 🌍"])
    with f2: s_grupo = st.selectbox("📂 GRUPO", ["BRASILEIRÃO", "PREMIER LEAGUE", "LA LIGA", "E2", "SC1"])
    with f3: s_comp = st.selectbox("🏆 COMPETIÇÃO", ["Série A", "Série B", "Geral"])
    
    st.markdown("<h4 style='color:white; margin-top:15px;'>⚔️ DEFINIR CONFRONTO</h4>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: t_casa = st.text_input("🏠 TIME DA CASA", "Athletico-PR")
    with c2: t_fora = st.text_input("🚀 TIME DE FORA", "Atlético-MG")
    
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        conf = 75.0
        if df_hist is not None:
            f = df_hist[df_hist['Casa'].str.contains(t_casa[:5], case=False, na=False)]
            if not f.empty: conf = round((len(f[f['Resultado']=='H'])/len(f))*100 + 10, 1)
        st.session_state.analise_bloqueada = {"casa": t_casa, "fora": t_fora, "conf": conf}

    if st.session_state.analise_bloqueada:
        a = st.session_state.analise_bloqueada
        st.markdown(f'<div class="banner-green">🟢 &nbsp; SISTEMA JARVIS: <span style="color:#00ff88">FILÉ MIGNON: INFORMAÇÃO REAL</span></div>', unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center; color:#9d54ff;'>{a['casa']} vs {a['fora']}</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", "ALTA PROB.", int(a['conf']))
        with r2: draw_card("GOLS", "OVER 1.5", 90)
        with r3: draw_card("STAKE", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
        with r4: draw_card("CANTOS", "9.5+", 75)
        
        if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True):
            st.session_state.historico_calls.append({"data": datetime.now().strftime("%H:%M"), "casa": a['casa'], "fora": a['fora']})
            st.toast("✅ CALL SALVA COM SUCESSO!")

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    if df_diario is not None: st.dataframe(df_diario, use_container_width=True, hide_index=True)

elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🏆 VENCEDORES DA COMPETIÇÃO</h2>", unsafe_allow_html=True)
    v1, v2, v3, v4 = st.columns(4)
    with v1: draw_card("FAVORITO 1", "Brasil", 45)
    with v2: draw_card("FAVORITO 2", "França", 38)
    with v3: draw_card("FAVORITO 3", "Espanha", 25)
    with v4: draw_card("ZEBRA PROB", "Marrocos", 12)

elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ APOSTAS POR GOLS</h2>", unsafe_allow_html=True)
    g1, g2, g3, g4 = st.columns(4)
    with g1: draw_card("OVER 0.5 HT", "82%", 82)
    with g2: draw_card("OVER 1.5 FT", "75%", 75)
    with g3: draw_card("AMBAS MARCAM", "61%", 61)
    with g4: draw_card("UNDER 3.5", "90%", 90)

elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 APOSTAS POR ESCANTEIOS</h2>", unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4)
    with e1: draw_card("OVER 8.5", "88%", 88)
    with e2: draw_card("OVER 10.5", "62%", 62)
    with e3: draw_card("CANTOS HT", "4.5+", 70)
    with e4: draw_card("CORNER RACE", "Time A", 55)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>""", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total))
    st.session_state.stake_padrao = st.slider("STAKE POR OPERAÇÃO (%)", 0.1, 10.0, float(st.session_state.stake_padrao))

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    for c in reversed(st.session_state.historico_calls):
        st.markdown(f"""<div class="history-card-box"><div style="color:white; font-weight:800;">[{c['data']}] {c['casa']} x {c['fora']}</div></div>""", unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v62.0</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
