import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v60.02 - LIVE ENGINE REAL-TIME]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO) - UI v57.35
# DIRETRIZ 5: CÓDIGO 100% ÍNTEGRO - SEM ABREVIAÇÕES
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
if 'top_20_ia' not in st.session_state: st.session_state.top_20_ia = []
if 'df_live_monitor' not in st.session_state: st.session_state.df_live_monitor = None

# --- MOTOR DE DADOS EM TEMPO REAL (SIMULADOR DE API) ---
def executar_varredura_live_realtime():
    """
    Simula uma requisição de API em tempo real.
    Gera placares, tempos e tendências aleatórias a cada clique.
    """
    times_casa = ["Flamengo", "Man City", "Real Madrid", "Inter Milan", "Bayern", "PSG", "Liverpool", "Arsenal"]
    times_fora = ["Palmeiras", "Arsenal", "Barcelona", "AC Milan", "Dortmund", "Monaco", "Chelsea", "Spurs"]
    tendencias = ["OVER 1.5", "OVER 2.5", "UNDER 3.5", "BTTS YES", "HOME WIN", "CANTOS 9.5+", "GOL NO HT"]
    
    # Embaralha os times para garantir que o confronto mude
    random.shuffle(times_casa)
    random.shuffle(times_fora)

    dados_atualizados = {
        "TEMPO": [f"{random.randint(1, 90)}'" for _ in range(5)],
        "CONFRONTO": [f"{times_casa[i]} vs {times_fora[i]}" for i in range(5)],
        "PLACAR": [f"{random.randint(0, 3)} - {random.randint(0, 3)}" for _ in range(5)],
        "PRESSÃO (C/F)": [f"{random.randint(30, 80)} / {random.randint(20, 70)}" for _ in range(5)],
        "CANTOS": [random.randint(0, 15) for _ in range(5)],
        "TENDÊNCIA IA": [random.choice(tendencias) for _ in range(5)]
    }
    st.session_state.df_live_monitor = pd.DataFrame(dados_atualizados)

# Carregamento inicial do monitor se estiver vazio
if st.session_state.df_live_monitor is None:
    executar_varredura_live_realtime()

# --- FUNÇÃO DE CARREGAMENTO DE DADOS ESTÁTICOS ---
def carregar_jogos_diarios():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            return df
        except:
            return None
    return None

df_diario = carregar_jogos_diarios()

# ==============================================================================
# LÓGICA DO BOT (BACK-END): MOTOR DE PROCESSAMENTO INVISÍVEL
# ==============================================================================

def processar_ia_bot():
    if df_diario is not None:
        vips = []
        try:
            temp_df = df_diario.copy()
            if 'CONFIANCA' in temp_df.columns:
                temp_df['CONF_NUM'] = temp_df['CONFIANCA'].astype(str).str.replace('%', '').astype(float)
                vips_df = temp_df[temp_df['CONF_NUM'] >= 85].head(20)
                
                for _, jogo in vips_df.iterrows():
                    vips.append({
                        "C": jogo.get('CASA', 'Time A'),
                        "F": jogo.get('FORA', 'Time B'),
                        "P": f"{jogo.get('CONF_NUM', 0)}%",
                        "G": "OVER 1.5 (PROB. 94%)",
                        "CT": "4.5+ NO TOTAL",
                        "E": f"9.5 total",
                        "TM": "16+ (8 POR TEMPO)",
                        "CH": "9+ AO GOL",
                        "DF": "7+ DEFESAS"
                    })
                st.session_state.top_20_ia = vips
        except:
            pass

processar_ia_bot()

# ==============================================================================
# 2. CAMADA DE ESTILO CSS INTEGRAL (v57.35)
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
        transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none;}
    .nav-links { display: flex; gap: 22px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600; cursor: pointer; white-space: nowrap;}
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important;}
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px;}
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important;}
    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important; border-radius: 6px !important;
        width: 100% !important; box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important;
    }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;}
    .banca-title-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px;}
    [data-testid="stDataFrame"] { border: 1px solid #1e293b !important; border-radius: 8px !important; background-color: #0b0e11 !important; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("""<div class="betano-header"><div class="header-left"><a class="logo-link">GESTOR IA</a><div class="nav-links"><div class="nav-item">LIVE SCANNER</div></div></div><div class="header-right"><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div></div><div style="height:65px;"></div>""", unsafe_allow_html=True) 

    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    
    # GATILHO DE ATUALIZAÇÃO EM TEMPO REAL
    if st.button("⚽ APOSTAS POR GOLS"): 
        if st.session_state.aba_ativa == "live":
            executar_varredura_live_realtime()
            st.toast("⚡ DADOS ATUALIZADOS EM TEMPO REAL!")
        else:
            st.session_state.aba_ativa = "gols"

def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color_footer}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# 4. TELAS
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with h3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with h4: draw_card("IA STATUS", "ONLINE", 100)
    if st.session_state.top_20_ia:
        st.markdown("<h4 style='color:#06b6d4;'>🤖 TOP 20 ANALISES IA</h4>", unsafe_allow_html=True)
        for j in st.session_state.top_20_ia[:5]:
            st.write(f"➔ {j['C']} vs {j['F']} | {j['G']}")

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    l1, l2, l3, l4 = st.columns(4)
    with l1: draw_card("PRESSÃO CASA", f"{random.randint(60,95)}%", 85)
    with l2: draw_card("ATAQUES/5m", f"{random.randint(5,18)}", 70)
    with l3: draw_card("POSSE BOLA", f"{random.randint(40,60)}%", 65)
    with l4: draw_card("GOL PROB", f"{random.randint(70,99)}%", 90)
    
    st.markdown("<h4 style='color:#06b6d4; margin-top:30px;'>🎮 MONITORAMENTO LIVE (CLIQUE EM 'APOSTAS POR GOLS' PARA ATUALIZAR)</h4>", unsafe_allow_html=True)
    st.dataframe(st.session_state.df_live_monitor, use_container_width=True, hide_index=True)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA</div>""", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total))

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v60.02</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
