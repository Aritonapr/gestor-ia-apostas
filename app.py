import streamlit as st
import pandas as pd
import requests
from datetime import datetime
from io import StringIO
import math

# ==============================================================================
# [PROTOCOLO DE RESTAURAÇÃO SIMÉTRICA v63.0]
# FOCO: ALINHAMENTO GEOMÉTRICO IDENTICO À IMAGEM REFERÊNCIA
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- MEMÓRIA DO SISTEMA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "gestao"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_gain' not in st.session_state: st.session_state.meta_gain = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# ==============================================================================
# CSS DE ALTA PRECISÃO (ZERO WHITE & SYMMETRY)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
    
    ::-webkit-scrollbar { display: none !important; }
    
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    /* HEADER (ESTILO BETANO IDENTICO) */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid #1e293b;
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px; z-index: 1000;
    }
    .logo-text { color: #9d54ff; font-weight: 900; font-size: 22px; text-transform: uppercase; }
    .nav-container { display: flex; gap: 20px; }
    .nav-link { color: #ffffff; font-size: 11px; font-weight: 700; text-transform: uppercase; opacity: 0.9; }

    /* SIDEBAR SEM SCROLL */
    [data-testid="stSidebar"] { background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    
    .stButton > button {
        background: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important;
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    .stButton > button:hover { color: #06b6d4 !important; background: #1e293b !important; }

    /* TITULO BANCA COM ICONE DINHEIRO */
    .banca-header-box { display: flex; align-items: center; gap: 15px; margin-bottom: 30px; }
    .banca-title { background: #003399; color: white; font-size: 28px; font-weight: 800; padding: 5px 15px; border-radius: 4px; }

    /* CARDS DE RESUMO (GRID 4x2) */
    .card-resumo {
        background: #11151a; border: 1px solid #1e293b; border-radius: 8px;
        padding: 20px; text-align: center; height: 150px; display: flex;
        flex-direction: column; justify-content: center; align-items: center;
    }
    .card-label { color: #64748b; font-size: 9px; font-weight: 700; text-transform: uppercase; margin-bottom: 12px; }
    .card-value { color: #ffffff; font-size: 18px; font-weight: 900; }
    .card-indicator { height: 4px; width: 60px; border-radius: 10px; margin-top: 15px; }

    /* INPUTS LATERAIS */
    .stNumberInput label, .stSlider label { color: #64748b !important; font-size: 11px !important; font-weight: 700 !important; text-transform: uppercase !important; }
    
    .footer-bar { position: fixed; bottom: 0; left: 0; width: 100%; background: #0d0d12; padding: 5px 20px; font-size: 9px; color: #475569; border-top: 1px solid #1e293b; z-index: 1000; }
    </style>
""", unsafe_allow_html=True)

# --- ESTRUTURA LATERAL ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "pre"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "hist"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "venc"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "esc"

# --- HEADER FIXO ---
st.markdown("""
    <div class="betano-header">
        <div style="display:flex; align-items:center; gap:25px;">
            <div class="logo-text">GESTOR IA</div>
            <div class="nav-container">
                <div class="nav-link">ESPORTES</div><div class="nav-link">AO VIVO</div>
                <div class="nav-link">VIRTUAIS</div><div class="nav-link">E-SPORTS</div>
                <div class="nav-link">OPORTUNIDADES IA</div><div class="nav-link">RESULTADOS</div>
            </div>
        </div>
        <div style="display:flex; gap:15px; align-items:center;">
            <div style="color:white;">🔍</div>
            <div style="border:1.5px solid white; padding:6px 15px; border-radius:20px; font-size:9px; font-weight:800; color:white;">REGISTRAR</div>
            <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); padding:7px 20px; border-radius:5px; font-size:9px; font-weight:800; color:white;">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- ABA GESTÃO DE BANCA (SIMETRIA IDENTICA) ---
if st.session_state.aba_ativa == "gestao":
    st.markdown("""
        <div class="banca-header-box">
            <span style="font-size:35px;">💰</span>
            <div class="banca-title">GESTÃO DE BANCA INTELIGENTE</div>
        </div>
    """, unsafe_allow_html=True)

    # Divisão Simétrica: Esquerda (Inputs) | Direita (Cards)
    col_left, col_right = st.columns([1.2, 2.8])

    with col_left:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total), step=50.0)
        st.markdown("<br>", unsafe_allow_html=True)
        st.session_state.stake_padrao = st.slider("STAKE POR OPERAÇÃO (%)", 0.1, 10.0, float(st.session_state.stake_padrao))
        st.session_state.meta_gain = st.slider("META DIÁRIA - STOP GAIN (%)", 0.1, 20.0, float(st.session_state.meta_gain))
        st.session_state.stop_loss = st.slider("LIMITE DE PERDA - STOP LOSS (%)", 0.1, 30.0, float(st.session_state.stop_loss))

    with col_right:
        # Cálculos Matemáticos
        v_entrada = st.session_state.banca_total * (st.session_state.stake_padrao / 100)
        v_gain = st.session_state.banca_total * (st.session_state.meta_gain / 100)
        v_loss = st.session_state.banca_total * (st.session_state.stop_loss / 100)
        alvo = st.session_state.banca_total + v_gain
        
        # Grid de 8 Cards (Exatamente como na imagem)
        r1_c1, r1_c2, r1_c3, r1_c4 = st.columns(4)
        with r1_c1:
            st.markdown(f'<div class="card-resumo"><div class="card-label">VALOR ENTRADA</div><div class="card-value">R$ {v_entrada:,.2f}</div><div class="card-indicator" style="background:#06b6d4;"></div></div>', unsafe_allow_html=True)
        with r1_c2:
            st.markdown(f'<div class="card-resumo"><div class="card-label">STOP GAIN (R$)</div><div class="card-value">R$ {v_gain:,.2f}</div><div class="card-indicator" style="background:#06b6d4;"></div></div>', unsafe_allow_html=True)
        with r1_c3:
            st.markdown(f'<div class="card-resumo"><div class="card-label">STOP LOSS (R$)</div><div class="card-value">R$ {v_loss:,.2f}</div><div class="card-indicator" style="background:#6d28d9;"></div></div>', unsafe_allow_html=True)
        with r1_c4:
            st.markdown(f'<div class="card-resumo"><div class="card-label">ALVO FINAL</div><div class="card-value">R$ {alvo:,.2f}</div><div class="card-indicator" style="background:#6d28d9;"></div></div>', unsafe_allow_html=True)

        st.markdown("<div style='height:15px;'></div>", unsafe_allow_html=True)

        r2_c1, r2_c2, r2_c3, r2_c4 = st.columns(4)
        with r2_c1:
            st.markdown(f'<div class="card-resumo"><div class="card-label">RISCO TOTAL</div><div class="card-value">{st.session_state.stake_padrao}%</div><div class="card-indicator" style="background:#06b6d4;"></div></div>', unsafe_allow_html=True)
        with r2_c2:
            st.markdown(f'<div class="card-resumo"><div class="card-label">ENTRADAS/META</div><div class="card-value">{math.ceil(v_gain/v_entrada) if v_entrada > 0 else 0}</div><div class="card-indicator" style="background:#06b6d4;"></div></div>', unsafe_allow_html=True)
        with r2_c3:
            st.markdown(f'<div class="card-resumo"><div class="card-label">ENTRADAS/LOSS</div><div class="card-value">{math.ceil(v_loss/v_entrada) if v_entrada > 0 else 0}</div><div class="card-indicator" style="background:#6d28d9;"></div></div>', unsafe_allow_html=True)
        with r2_c4:
            st.markdown(f'<div class="card-resumo"><div class="card-label">SAÚDE BANCA</div><div class="card-value" style="color:#00ff88; font-size:14px;">EXCELENTE</div><div class="card-indicator" style="background:#00ff88;"></div></div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""<div class="footer-bar">STATUS: ● IA OPERACIONAL | v63.0 | JARVIS PROTECT</div>""", unsafe_allow_html=True)
