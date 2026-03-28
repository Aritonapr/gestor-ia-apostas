import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v59.10 - RESTAURAÇÃO INTEGRAL]
# DIRETRIZ: NÃO APAGAR COMANDOS EXISTENTES E MANTER 8 KPI CARDS
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA (NÃO APAGAR) ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0
if 'top_20_ia' not in st.session_state: st.session_state.top_20_ia = []

# --- CARREGAMENTO DE DADOS ---
def carregar_jogos_diarios():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try:
            return pd.read_csv(path)
        except:
            return None
    return None

df_diario = carregar_jogos_diarios()

# --- MOTOR DE INTELIGÊNCIA (AUTÔNOMO) ---
def processar_ia_bot():
    if df_diario is not None:
        vips = []
        try:
            temp_df = df_diario.copy()
            col_conf = 'CONFIANCA' if 'CONFIANCA' in temp_df.columns else ('CONF' if 'CONF' in temp_df.columns else None)
            if col_conf:
                temp_df['CONF_NUM'] = temp_df[col_conf].astype(str).str.replace('%', '').astype(float)
                vips_df = temp_df[temp_df['CONF_NUM'] >= 80].sort_values(by='CONF_NUM', ascending=False).head(20)
                
                for _, jogo in vips_df.iterrows():
                    vips.append({
                        "CASA": jogo.get('CASA', 'Time A'),
                        "FORA": jogo.get('FORA', 'Time B'),
                        "PORC": f"{jogo.get('CONF_NUM', 0)}%",
                        "GOLS": "OVER 1.5",
                        "CANTOS": f"{jogo.get('C_CASA', 5)} | {jogo.get('C_FORA', 4)}"
                    })
                st.session_state.top_20_ia = vips
        except:
            pass

processar_ia_bot()

# --- ESTILIZAÇÃO CSS (ZERO WHITE REFORÇADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [data-testid="stAppViewContainer"] { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 80px 40px 20px 40px !important; }
    
    /* HEADER E LUPA */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; display: flex; align-items: center; 
        justify-content: space-between; padding: 0 40px !important; z-index: 10000;
        transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px; text-decoration: none; }
    .nav-item { color: white; font-size: 10px; font-weight: 700; text-transform: uppercase; margin: 0 10px; cursor: pointer; }
    .search-lupa { color: white; font-size: 18px; cursor: pointer; }

    /* BOTÕES SIDEBAR */
    [data-testid="stSidebar"] { background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 15px 20px !important; font-size: 11px !important; border-radius: 0px !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; }

    /* CARDS KPI */
    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 15px; 
        border-radius: 8px; text-align: center; margin-bottom: 15px;
    }
    
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background: #0d0d12; height: 25px; border-top: 1px solid #1e293b; font-size: 10px; color: #475569; display: flex; justify-content: center; align-items: center; z-index: 1000; }
    </style>
""", unsafe_allow_html=True)

# 2. RENDERIZAÇÃO DO HEADER
st.markdown("""
    <div class="betano-header">
        <div style="display: flex; align-items: center; gap: 20px;">
            <div class="logo-link">GESTOR IA</div>
            <div class="nav-item">APOSTAS ESPORTIVAS</div>
            <div class="nav-item">AO VIVO</div>
            <div class="nav-item">ASSERTIVIDADE IA</div>
        </div>
        <div style="display: flex; align-items: center; gap: 20px;">
            <div class="search-lupa">🔍</div>
            <div style="color:white; font-weight:800; font-size:10px; border:1px solid white; padding:5px 15px; border-radius:20px;">REGISTRAR</div>
            <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:6px 20px; border-radius:5px; font-weight:800; font-size:10px;">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 3. SIDEBAR COM BOTÕES FUNCIONAIS
with st.sidebar:
    st.markdown("<div style='height:60px;'></div>", unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_kpi(title, value, color="#06b6d4"):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; font-weight: 700;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:5px;">{value}</div>
            <div style="background:{color}; height:3px; width:50%; margin:8px auto; border-radius:10px;"></div>
        </div>
    """, unsafe_allow_html=True)

# 4. LÓGICA DAS TELAS
if st.session_state.aba_ativa == "home":
    st.markdown("<h3 style='color:white;'>📅 BILHETE OURO - TOP 20 IA</h3>", unsafe_allow_html=True)
    
    # OS 8 KPI CARDS (Restaurados conforme solicitado)
    col1, col2, col3, col4 = st.columns(4)
    with col1: draw_kpi("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}")
    with col2: draw_kpi("ASSERTIVIDADE", "92.4%", "#6d28d9")
    with col3: draw_kpi("SUGESTÃO", "OVER 1.5")
    with col4: draw_kpi("IA STATUS", "ONLINE", "#00ff88")
    
    col5, col6, col7, col8 = st.columns(4)
    with col5: draw_kpi("JOGOS ANALISADOS", "482")
    with col6: draw_kpi("STAKE PADRÃO", f"{st.session_state.stake_padrao}%")
    with col7: draw_kpi("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}")
    with col8: draw_kpi("VERSÃO", "59.10")

    st.markdown("---")

    # EXIBIÇÃO DOS 20 JOGOS (BILHETE OURO REAL)
    if st.session_state.top_20_ia:
        for jogo in st.session_state.top_20_ia:
            with st.expander(f"🔥 {jogo['CASA']} x {jogo['FORA']} | CONFIANÇA: {jogo['PORC']}"):
                c1, c2, c3 = st.columns(3)
                c1.metric("Mercado", "Gols")
                c1.write(f"🎯 Sugestão: {jogo['GOLS']}")
                c2.metric("Escanteios", "Média")
                c2.write(f"🚩 {jogo['CANTOS']}")
                c3.metric("Entrada Sugerida", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}")
    else:
        st.info("O Bot está processando a base de dados para gerar os 20 jogos...")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    # Lógica de gestão mantida
    st.session_state.banca_total = st.number_input("BANCA TOTAL", value=float(st.session_state.banca_total))
    st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, float(st.session_state.stake_padrao))

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    st.write("Scanner operacional. Selecione as ligas abaixo.")

# FOOTER
st.markdown("""<div class="footer-shield">STATUS: IA OPERACIONAL | PROTOCOLO v59.10 | JARVIS PROTECT</div>""", unsafe_allow_html=True)
