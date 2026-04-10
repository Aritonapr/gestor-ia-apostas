import streamlit as st
import pandas as pd
import os
from datetime import datetime
import random  # CORREÇÃO: Importação necessária para evitar o erro da imagem

# ==============================================================================
# [PROTOCOLO DE RESTAURAÇÃO v64.0 - FIDELIDADE VISUAL TOTAL]
# DIRETRRIZ: Restaurar ordem original dos botões e corrigir NameError
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

# --- FUNÇÃO DE DADOS ---
def carregar_dados_ia():
    path_local = "data/database_diario.csv"
    if os.path.exists(path_local):
        try:
            df = pd.read_csv(path_local)
            df.columns = [c.upper() for c in df.columns]
            return df
        except: return None
    return None

df_diario = carregar_dados_ia()

# ==============================================================================
# 2. ESTILO CSS (ZERO WHITE IMUTÁVEL - RESTAURADO)
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
    
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important;
    }

    .kpi-detailed-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 15px; 
        border-radius: 8px; margin-bottom: 15px; height: 380px;
    }
    .kpi-stat { font-size: 10px; color: #94a3b8; margin-bottom: 6px; display: flex; justify-content: space-between;}
    .kpi-stat b { color: white; }

    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR - ORDEM ORIGINAL RESTAURADA (CONFORME SUA IMAGEM)
with st.sidebar:
    st.markdown('<div class="betano-header"><div class="logo-link">GESTOR IA</div></div><div style="height:65px;"></div>', unsafe_allow_html=True) 
    
    # Botões na ordem exata da sua imagem
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📄 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"
    if st.button("📈 ASSERTIVIDADE IA"): st.session_state.aba_ativa = "performance"

# 4. CONTEÚDO PRINCIPAL (BILHETE OURO)
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white; margin-bottom:30px;'>📅 BILHETE OURO - TOP 20 ANALISES IA</h2>", unsafe_allow_html=True)
    
    # Lista fixa para garantir que a tela não fique vazia (como na sua imagem)
    jogos = [
        {"C": "Real Madrid", "F": "Barcelona", "P": "82%", "V": "72% (FAVORITO)", "G": "1.5+ (AMBOS TEMPOS)"},
        {"C": "Flamengo", "F": "Palmeiras", "P": "82%", "V": "72% (FAVORITO)", "G": "1.5+ (AMBOS TEMPOS)"},
        {"C": "Arsenal", "F": "Chelsea", "P": "64%", "V": "72% (FAVORITO)", "G": "1.5+ (AMBOS TEMPOS)"},
        {"C": "Arsenal", "F": "Flamengo", "P": "92%", "V": "68% (PROB)", "G": "OVER 1.5 (HT/FT)"}
    ]
    
    cols = st.columns(4)
    for i, j in enumerate(jogos):
        with cols[i]:
            st.markdown(f"""
            <div class="kpi-detailed-card">
                <div style="color:#9d54ff; font-size:10px; font-weight:900; margin-bottom:5px;">IA CONFIANÇA: {j['P']}</div>
                <div style="color:white; font-size:12px; font-weight:800; margin-bottom:12px; border-bottom:1px solid #1e293b; padding-bottom:5px;">{j['C']} vs {j['F']}</div>
                <div class="kpi-stat">🏆 VENCEDOR: <b>{j['V']}</b></div>
                <div class="kpi-stat">⚽ GOLS: <b>{j['G']}</b></div>
                <div class="kpi-stat">🟨 CARTÕES: <b>4.5 (HT: 2 | FT: 2)</b></div>
                <div class="kpi-stat">🚩 ESCANTEIOS: <b>9.5 (C: 5 | F: 4)</b></div>
                <div class="kpi-stat">👟 TIROS META: <b>14+ (HT: 7 | FT: 7)</b></div>
                <div class="kpi-stat">🎯 CHUTES GOL: <b>9+ (HT: 4 | FT: 5)</b></div>
                <div class="kpi-stat">🧤 DEFESAS: <b>7+ (GOLEIROS ATIVOS)</b></div>
                <div style="margin-top:15px; padding-top:10px; border-top:1px dashed #334155; color:#06b6d4; font-size:11px; font-weight:900; text-align:center;">
                    INVESTIMENTO: R$ 10.00
                </div>
            </div>
            """, unsafe_allow_html=True)

# 5. SCANNER EM TEMPO REAL (CORRIGIDO)
elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL (LIVE FILTERS)</h2>", unsafe_allow_html=True)
    st.markdown(f"<div style='color:white; font-weight:800;'>Palmeiras x Dortmund</div>", unsafe_allow_html=True)
    # CORREÇÃO DO ERRO DA IMAGEM: Agora 'random' está definido
    pressao = random.randint(60, 95)
    st.markdown(f"<div style='color:#00ff88;'>PRESSÃO: {pressao}%</div>", unsafe_allow_html=True)

# FOOTER
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v64.0</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
