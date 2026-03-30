import streamlit as st
import pandas as pd
import os

# ==============================================================================
# [PROTOCOLO JARVIS v63.3 - LUZ DE EMERGÊNCIA]
# DIRETRIZ: CARREGAR INTERFACE PRIMEIRO, DADOS DEPOIS
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA (LINHA 1 OBRIGATÓRIA)
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide")

# 2. INICIALIZAÇÃO DE MEMÓRIA RELÂMPAGO
for chave, valor in {
    'aba_ativa': "home", 'banca_total': 1000.0, 
    'stake_padrao': 1.0, 'top_20_ia': []
}.items():
    if chave not in st.session_state: st.session_state[chave] = valor

# 3. CAMADA VISUAL: CSS ZERO WHITE PRO (IMUTÁVEL)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px; z-index: 1000000; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px; text-transform: uppercase; text-decoration: none;}
    .nav-links { display: flex; gap: 22px; }
    .nav-item { color: #ffffff; font-size: 11px; text-transform: uppercase; font-weight: 600; }
    .registrar-pill { color: #ffffff; font-size: 9px; font-weight: 800; border: 1.5px solid #ffffff; padding: 7px 18px; border-radius: 20px; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%); color: white; padding: 8px 22px; border-radius: 5px; font-weight: 800; font-size: 9.5px; }
    [data-testid="stSidebar"] { background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px; font-size: 10px; text-transform: uppercase;
    }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 4. SIDEBAR E HEADER (FIXO)
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <div class="logo-link">GESTOR IA</div>
                <div class="nav-links"><div class="nav-item">TRADING REAL-TIME 2026</div></div>
            </div>
            <div class="header-right">
                <div class="registrar-pill">REGISTRAR</div>
                <div class="entrar-grad">ENTRAR</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"

def draw_card(title, value, perc):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div style="background:#1e293b; height:4px; width:80%; margin:10px auto;">
                <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); height:100%; width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# 5. CARREGAMENTO DE DADOS (DENTRO DA TELA)
path_data = "data/database_diario.csv"
df_diario = None
if os.path.exists(path_data):
    try: df_diario = pd.read_csv(path_data)
    except: pass

# 6. DESENHO DAS TELAS
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO - MARÇO 2026</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("BANCA", f"R$ {st.session_state.banca_total}", 100)
    with c2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with c3: draw_card("STATUS", "ONLINE", 100)
    with c4: draw_card("SISTEMA", "JARVIS v63.3", 100)
    
    if df_diario is not None:
        st.dataframe(df_diario, use_container_width=True, hide_index=True)
    else:
        st.info("🤖 Jarvis: O banco de dados de 2026 está sendo criado pelo robô no GitHub. Aguarde a conclusão da primeira sincronia.")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA (R$)", value=st.session_state.banca_total)

st.markdown("""<div class="footer-shield"><div>● IA OPERACIONAL | v63.3 | 2026</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
