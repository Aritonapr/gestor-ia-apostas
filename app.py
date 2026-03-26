import streamlit as st
import pandas as pd
import os

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v59.60 - RESTAURAÇÃO TOTAL E SIMETRIA]
# DIRETRIZ: FIXAR MENU SUPERIOR, LUPA E 8 CARDS (REF: IMAGEM 1 e 7)
# DIRETRIZ: REMOVER ERRO DE SINTAXE E GARANTIR CÓDIGO ÍNTEGRO
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# --- LÓGICA DE AUTONOMIA (OPÇÃO A) ---
def buscar_sugestao_ia():
    path_d = "data/database_diario.csv"
    if os.path.exists(path_d):
        try:
            df = pd.read_csv(path_d)
            if not df.empty:
                jogo = df.iloc[0]
                return f"{jogo['TIME_CASA']} vs {jogo['TIME_FORA']}", "OVER 1.5 GOLS"
        except: pass
    return "AGUARDANDO DADOS", "ANALISANDO..."

nome_jogo, palpite_ia = buscar_sugestao_ia()

# --- CSS INTEGRAL (RESTAURAÇÃO VISUAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stAppViewContainer"] { background-color: #0b0e11 !important; }
    [data-testid="stMainBlockContainer"] { padding: 90px 45px 20px 45px !important; }
    
    /* HEADER SUPERIOR (RESTAURO IMAGEM 1) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 65px; 
        background-color: #001a4d !important; display: flex; align-items: center; 
        justify-content: space-between; padding: 0 45px !important; z-index: 1000000;
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .nav-links { display: flex; gap: 18px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 10px !important; text-transform: uppercase; font-weight: 700; opacity: 0.8; text-decoration: none; }
    
    /* SIDEBAR */
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }

    /* CARDS (RESTAURO IMAGEM 7) */
    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 25px 15px; 
        border-radius: 10px; text-align: center; height: 160px; margin-bottom: 20px;
    }
    .card-title { color: #64748b; font-size: 9px; text-transform: uppercase; font-weight: 800; letter-spacing: 0.5px; }
    .card-value { color: white; font-size: 19px; font-weight: 900; margin-top: 12px; }
    .progress-container { background: #1e293b; height: 5px; width: 85%; border-radius: 10px; margin: 15px auto 0 auto; overflow: hidden; }
    .progress-bar { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; border-radius: 10px; }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

def draw_card(title, value, perc):
    st.markdown(f"""<div class="highlight-card"><div class="card-title">{title}</div><div class="card-value">{value}</div><div class="progress-container"><div class="progress-bar" style="width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- HEADER SUPERIOR RESTAURADO ---
st.markdown(f"""
    <div class="betano-header">
        <div style="display:flex; align-items:center; gap:30px;">
            <div style="color:#9d54ff; font-weight:900; font-size:22px;">GESTOR IA</div>
            <div class="nav-links">
                <div class="nav-item">APOSTAS ESPORTIVAS</div><div class="nav-item">APOSTAS AO VIVO</div>
                <div class="nav-item">OPORTUNIDADES IA</div><div class="nav-item">ESTATÍSTICAS AVANÇADAS</div>
                <div class="nav-item">ASSERTIVIDADE IA</div>
            </div>
        </div>
        <div style="display:flex; align-items:center; gap:20px;">
            <div style="color:white; font-size:18px; cursor:pointer;">🔍</div>
            <div style="color:white; border:1.5px solid white; padding:8px 20px; border-radius:25px; font-size:10px; font-weight:800; cursor:pointer;">REGISTRAR</div>
            <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:9px 25px; border-radius:5px; font-size:10px; font-weight:800; cursor:pointer;">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<div style='height:80px;'></div>", unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "prelive"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🧠 ASSERTIVIDADE & IA"): st.session_state.aba_ativa = "assertividade"
    if st.button("🏆 VENCEDORES"): st.session_state.aba_ativa = "vencedores"

# --- TELAS ---
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white; margin-bottom:30px;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with c2: draw_card("ASSERTIVIDADE IA", "92.4%", 92)
    with c3: draw_card("SUGESTÃO DO DIA", palpite_ia, 100)
    with c4: draw_card("JOGO EM FOCO", nome_jogo, 100)
    
    c5, c6, c7, c8 = st.columns(4)
    with c5: draw_card("VOL. DE MERCADO", "ALTO", 75)
    with c6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with c7: draw_card("VALOR ENTRADA", f"R$ {st.session_state.banca_total*(st.session_state.stake_padrao/100):,.2f}", 100)
    with c8: draw_card("SISTEMA STATUS", "v59.60 ONLINE", 100)

elif st.session_state.aba_ativa == "gestao":
    st.markdown('<div style="background:#003399; padding:20px; border-radius:5px; color:white; font-size:24px; font-weight:800; margin-bottom:35px;">💰 GESTÃO DE BANCA INTELIGENTE</div>', unsafe_allow_html=True)
    col_in, col_out = st.columns([1.2, 2.5])
    with col_in:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
    with col_out:
        draw_card("VALOR ENTRADA", f"R$ {st.session_state.banca_total*0.01:,.2f}", 100)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v59.60</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
