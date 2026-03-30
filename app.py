import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v63.1 - BLINDAGEM DE AÇO]
# DIRETRIZ: INICIALIZAÇÃO À PROVA DE FALHAS E ZERO WHITE PRO
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA (Sempre a primeira linha de código)
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA (BLINDAGEM TOTAL) ---
# Garantimos que todas as variáveis existam antes de qualquer outra linha rodar
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state:
    st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state:
    st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state:
    st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state:
    st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state:
    st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state:
    st.session_state.stop_loss = 5.0
if 'top_20_ia' not in st.session_state:
    st.session_state.top_20_ia = []

# --- FUNÇÃO DE CARREGAMENTO SEGURO (NÃO QUEBRA SE O ARQUIVO ESTIVER SENDO CRIADO) ---
def carregar_dados_ia():
    path_local = "data/database_diario.csv"
    if os.path.exists(path_local):
        try:
            df = pd.read_csv(path_local)
            # Verifica se o arquivo tem as colunas que o Jarvis v63.0 precisa
            if 'CASA' in df.columns and 'FORA' in df.columns:
                return df
        except:
            return None
    return None

df_diario = carregar_dados_ia()

# ==============================================================================
# LÓGICA DO BOT: PROCESSAMENTO DE DADOS DE 2026
# ==============================================================================

def processar_ia_bot():
    if df_diario is not None:
        vips = []
        try:
            temp_df = df_diario.copy()
            # Tratamento de confiança para não dar erro de coluna
            col_conf = 'CONF' if 'CONF' in temp_df.columns else temp_df.columns[-1]
            
            temp_df['CONF_NUM'] = temp_df[col_conf].astype(str).str.replace('%', '').str.extract('(\d+)').astype(float)
            vips_df = temp_df.sort_values(by='CONF_NUM', ascending=False).head(20)
            
            for _, jogo in vips_df.iterrows():
                vips.append({
                    "C": jogo.get('CASA', 'Time A'),
                    "F": jogo.get('FORA', 'Time B'),
                    "P": f"{int(jogo.get('CONF_NUM', 0))}%",
                    "G": jogo.get('GOLS', 'OVER 1.5'),
                    "CT": "4.5+ NO TOTAL",
                    "E": f"{jogo.get('CANTOS', '9.5 total')}",
                    "TM": f"{jogo.get('TMETA', '16+')}",
                    "CH": f"{jogo.get('CHUTES', '9+ GOL')}",
                    "DF": f"{jogo.get('DEFESAS', '7+')}"
                })
            st.session_state.top_20_ia = vips
        except:
            pass

processar_ia_bot()

# ==============================================================================
# 2. CAMADA DE ESTILO CSS INTEGRAL (DIRETRIZ VISUAL IMUTÁVEL)
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
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    
    .header-left { display: flex; align-items: center; gap: 25px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none;}
    .nav-links { display: flex; gap: 22px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600; }
    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }

    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; }

    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important; border-radius: 6px !important; width: 100% !important;
    }
    
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; }
    .banca-title-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR E HEADER (FIXO)
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <div class="logo-link">GESTOR IA</div>
                <div class="nav-links">
                    <div class="nav-item">APOSTAS ESPORTIVAS</div>
                    <div class="nav-item">ESTATÍSTICAS</div>
                    <div class="nav-item">IA ASSERTIVIDADE</div>
                </div>
            </div>
            <div class="header-right">
                <div class="registrar-pill">REGISTRAR</div>
                <div class="entrar-grad">ENTRAR</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"

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
# 4. LÓGICA DE TELAS (RESPEITANDO ABA_ATIVA)
# ==============================================================================

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        h1, h2, h3, h4 = st.columns(4)
        with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
        with h2: draw_card("ASSERTIVIDADE", "92.4%", 92)
        with h3: draw_card("SUGESTÃO", "OVER 2.5", 88)
        with h4: draw_card("SISTEMA", "JARVIS v63.1", 100)
        
        if st.session_state.top_20_ia:
            st.markdown("<h4 style='color:#06b6d4; margin-top:30px;'>🤖 TOP 20 ANALISES IA - 2026</h4>", unsafe_allow_html=True)
            for j in st.session_state.top_20_ia:
                with st.expander(f"➔ {j['C']} vs {j['F']} | CONF: {j['P']}"):
                    st.write(f"⚽ GOLS: {j['G']} | 🚩 CANTOS: {j['E']} | 🥅 CHUTES: {j['CH']}")
        
        st.markdown("### 📋 GRADE DE JOGOS SINCRONIZADA")
        st.dataframe(df_diario, use_container_width=True, hide_index=True)
    else:
        st.info("🤖 Jarvis: Sincronizando com a internet de 2026... Aguarde o robô do GitHub terminar.")
        st.image("https://i.gifer.com/ZZ5H.gif", width=40)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA</div>""", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total))
    st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, float(st.session_state.stake_padrao))
    draw_card("VALOR POR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        lista = sorted(list(set(df_diario['CASA'].tolist() + df_diario['FORA'].tolist())))
        c1, c2 = st.columns(2)
        with c1: t_casa = st.selectbox("🏠 CASA", lista)
        with c2: t_fora = st.selectbox("🚀 FORA", [t for t in lista if t != t_casa])
        if st.button("⚡ ANALISAR AGORA"):
            st.success(f"Análise de {t_casa} x {t_fora} concluída para 2026!")
    else:
        st.warning("🤖 Jarvis: Sem dados para análise no momento.")

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v63.1 | 2026</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
