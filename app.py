import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# PROTOCOLO GESTOR IA - v62.00 (ESTABILIDADE TOTAL)
# RECOMPOSIÇÃO VISUAL v58.00 + ABA ASSERTIVIDADE
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []

# --- CARREGAMENTO DE DADOS ---
def carregar_dados():
    path_perm = 'data/historico_permanente.csv'
    if os.path.exists(path_perm):
        try: return pd.read_csv(path_perm)
        except: return pd.DataFrame()
    return pd.DataFrame()

df_hist = carregar_dados()

# 2. CAMADA DE ESTILO CSS (REFORÇADA PARA EVITAR BOTÕES BRANCOS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    /* Reset Geral */
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* Header Azul Institucional */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    
    .logo-ia { color: #9d54ff !important; font-weight: 900; font-size: 22px; text-decoration: none; }
    
    /* Estilo dos Links do Menu (Para não virarem botões brancos) */
    .nav-container { display: flex; gap: 20px; }
    .nav-link { 
        color: white !important; font-size: 11px; font-weight: 600; 
        text-transform: uppercase; cursor: pointer; text-decoration: none;
        opacity: 0.8; transition: 0.3s;
    }
    .nav-link:hover { opacity: 1; color: #06b6d4 !important; }

    /* Sidebar Customizada */
    [data-testid="stSidebar"] { background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    
    /* Botões da Sidebar */
    section[data-testid="stSidebar"] .stButton > button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        text-align: left !important; width: 100% !important; padding: 12px 20px !important;
        font-size: 11px !important; text-transform: uppercase !important; border-bottom: 1px solid #1a202c !important;
    }
    section[data-testid="stSidebar"] .stButton > button:hover {
        color: #06b6d4 !important; background: #1e293b !important; border-left: 3px solid #6d28d9 !important;
    }

    /* Cards Estilo v58 */
    .highlight-card { 
        background: #161b22; border: 1px solid #30363d; padding: 20px; 
        border-radius: 8px; text-align: center; margin-bottom: 15px;
        transition: 0.3s;
    }
    .highlight-card:hover { border-color: #6d28d9; transform: translateY(-3px); }

    .metric-title { color: #8b949e; font-size: 10px; text-transform: uppercase; font-weight: 700; margin-bottom: 8px;}
    .metric-value { color: white; font-size: 18px; font-weight: 800; }
    
    /* Progress Bar */
    .bar-bg { background: #30363d; height: 4px; width: 80%; border-radius: 10px; margin: 12px auto; }
    .bar-fill { height: 100%; border-radius: 10px; }

    /* Banner Assertividade */
    .box-liga { padding: 15px; border-radius: 5px; margin-bottom: 10px; font-weight: bold; font-size: 13px; }
    .green-box { background: rgba(0, 255, 136, 0.1); border-left: 5px solid #00ff88; color: #00ff88; }
    .yellow-box { background: rgba(255, 193, 7, 0.1); border-left: 5px solid #ffc107; color: #ffc107; }

    /* Ajuste de Margem para o Header Fixo */
    [data-testid="stMainBlockContainer"] { padding-top: 80px !important; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER FIXO (HTML PURO PARA EVITAR CONFLITO)
st.markdown(f"""
    <div class="betano-header">
        <div style="display: flex; align-items: center; gap: 30px;">
            <div class="logo-ia">GESTOR IA</div>
            <div class="nav-container">
                <div class="nav-link">APOSTAS ESPORTIVAS</div>
                <div class="nav-link">AO VIVO</div>
                <div class="nav-link">ESTATÍSTICAS</div>
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 15px;">
            <div style="color:white; font-size:18px;">🔍</div>
            <div style="border: 1px solid white; color:white; padding: 5px 15px; border-radius:20px; font-size:10px; font-weight:800;">REGISTRAR</div>
            <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding: 6px 18px; border-radius:5px; font-size:10px; font-weight:800;">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. SIDEBAR DE NAVEGAÇÃO
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("📈 ASSERTIVIDADE IA"): st.session_state.aba_ativa = "assertividade"
    if st.button("🎯 SCANNER PRE-LIVE"): st.session_state.aba_ativa = "scanner"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background: rgba(6, 182, 212, 0.1); padding: 15px; border-radius: 8px; border: 1px solid #06b6d4;">
            <p style="color: #06b6d4; font-size: 10px; margin: 0;"><b>O JUIZ:</b> Processamento de Greens e Reds automático às 23:00.</p>
        </div>
    """, unsafe_allow_html=True)

# 5. FUNÇÃO PARA DESENHAR CARDS (GRID 2x4)
def draw_card(title, value, perc, color="#06b6d4"):
    st.markdown(f"""
        <div class="highlight-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            <div class="bar-bg">
                <div class="bar-fill" style="width: {perc}%; background: {color};"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# 6. LOGICA DAS TELAS

# TELA: HOME (JOGOS DO DIA - GRID 2x4)
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with col2: draw_card("ASSERTIVIDADE", "92.4%", 92, "#00ff88")
    with col3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with col4: draw_card("IA STATUS", "ONLINE", 100, "#00ff88")
    
    col5, col6, col7, col8 = st.columns(4)
    with col5: draw_card("VOL. GLOBAL", "ALTO", 75, "#6d28d9")
    with col6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with col7: draw_card("VALOR ENTRADA", f"R$ {st.session_state.banca_total*0.01:,.2f}", 100)
    with col8: draw_card("SISTEMA", "JARVIS v62.00", 100, "#6d28d9")

# TELA: ASSERTIVIDADE (A PÁGINA NOVA)
elif st.session_state.aba_ativa == "assertividade":
    st.markdown("<h2 style='color:white;'>📈 ASSERTIVIDADE DA INTELIGÊNCIA</h2>", unsafe_allow_html=True)
    
    # Simulação de dados para manter o visual do seu print
    m1, m2, m3, m4 = st.columns(4)
    with m1: draw_card("ACERTOS TOTAIS", "142", 100, "#00ff88")
    with m2: draw_card("ERROS TOTAIS", "12", 30, "#ff4b4b")
    with m3: draw_card("TAXA DE WIN", "92.2%", 92, "#00ff88")
    with m4: draw_card("MERCADO LÍDER", "OVER 1.5", 100, "#8257e5")

    st.markdown("<br><h4 style='color:white;'>📊 ONDE O JARVIS MAIS ACERTA:</h4>", unsafe_allow_html=True)
    st.markdown('<div class="box-liga green-box">✅ PREMIER LEAGUE: 96% de acerto</div>', unsafe_allow_html=True)
    st.markdown('<div class="box-liga yellow-box">⚠️ BUNDESLIGA: 65% de acerto (IA em aprendizado)</div>', unsafe_allow_html=True)

# TELA: GESTÃO DE BANCA
elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("VALOR DA BANCA (R$)", value=st.session_state.banca_total)
    st.write(f"Sua banca atualizada é de R$ {st.session_state.banca_total}")

# RODAPÉ DE STATUS
st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #0b0e11; padding: 5px 20px; border-top: 1px solid #1e293b; color: #475569; font-size: 9px; display: flex; justify-content: space-between;">
        <div>STATUS: ● IA OPERACIONAL | v62.00</div>
        <div>PROTEÇÃO JARVIS ATIVA</div>
    </div>
""", unsafe_allow_html=True)
