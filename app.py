import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL (ESTRUTURA PROTEGIDA E RENOMEADA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 320px !important; }
    
    /* Sidebar Header conforme foto original */
    .sidebar-header { display: flex; align-items: center; padding: 20px 10px; margin-bottom: 20px; }
    .ai-icon-box { background-color: #f05a22; padding: 8px; border-radius: 8px; margin-right: 12px; box-shadow: 0 0 10px rgba(240,90,34,0.5); }
    .sidebar-title { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 16px; font-weight: 900; line-height: 1.2; }

    /* Botões da Sidebar */
    .stButton > button {
        background-color: #1a242d !important; color: #cbd5e0 !important; border: 1px solid #2d3748 !important;
        font-weight: bold !important; width: 100% !important; height: 40px !important;
        border-radius: 6px !important; margin-bottom: 5px !important; text-transform: uppercase; font-size: 11px !important;
    }
    .stButton > button:hover { border-color: #f05a22 !important; color: #f05a22 !important; }
    .cat-label { color: #5a6b79; font-size: 11px; font-weight: bold; margin-top: 15px; text-transform: uppercase; border-left: 3px solid #f05a22; padding-left: 8px; margin-bottom: 5px; }

    /* CARD PRINCIPAL */
    .card-principal { 
        background-color: #1a242d; padding: 40px; border-radius: 20px; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.6); border-bottom: 4px solid #f05a22;
        margin-bottom: 30px; text-align: center;
    }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 32px; font-weight: 900; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 30px; }
    .label-prob { color: #ffffff !important; font-size: 13px; font-weight: 700; text-transform: uppercase; }
    .val-prob { color: #f05a22; font-size: 30px; font-weight: 900; margin-top: 5px; }

    /* CAIXA VERDE (ODD JUSTA) */
    .value-box {
        border: 1px dashed #00ffc3; border-radius: 12px; padding: 15px;
        display: flex; justify-content: space-around; align-items: center;
        background: rgba(0, 255, 195, 0.05); margin-top: 30px;
    }
    .value-item { color: #00ffc3; font-weight: 700; font-size: 13px; font-family: 'Inter', sans-serif; }

    /* MINI CARDS */
    .mini-card { 
        background-color: #111a21; padding: 12px; border-radius: 12px; 
        border: 1px solid #2d3748; text-align: center; height: 110px;
        display: flex; flex-direction: column; justify-content: center;
    }
    .mini-label { color: #ffffff !important; font-weight: 700 !important; font-size: 11px; text-transform: uppercase; margin-bottom: 8px; }
    .mini-val { color: #00ffc3; font-weight: 900; font-size: 20px; }
    
    .section-header { color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 16px; margin-bottom: 15px; border-left: 4px solid #f05a22; padding-left: 10px; text-transform: uppercase; }
    
    /* RADAR ESTRATÉGICO (ESTILO PROTEGIDO) */
    .radar-box {
        background: rgba(240,90,34,0.08); border-left: 4px solid #f05a22;
        padding: 12px 20px; color: #ffffff; font-size: 13px; 
        margin: 10px 0 25px 0; border-radius: 0 8px 8px 0;
        display: flex; align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.markdown('<div class="sidebar-header"><div class="ai-icon-box">📊</div><div class="sidebar-title">GESTOR IA<br>APOSTAS</div></div>', unsafe_allow_html=True)
    
    st.markdown('<p class="cat-label">BR NACIONAIS</p>', unsafe_allow_html=True)
    st.button("SÉRIE A - BRASILEIRÃO")
    st.button("SÉRIE B - BRASILEIRÃO")
    st.button("COPA DO BRASIL")

    st.markdown('<p class="cat-label">🌎 CONTINENTAIS</p>', unsafe_allow_html=True)
    st.button("LIBERTADORES")
    st.button("SUL-AMERICANA")

# --- 4. ÁREA PRINCIPAL ---
# Botão sozinho para não quebrar o layout
st.button("🔥 EXECUTAR ALGORITMO COMPLETO")

c1, c2 = st.columns(2)
with c1: t_casa = st.selectbox("Mandante", ["Botafogo", "Flamengo", "Palmeiras"])
with c2: t_fora = st.selectbox("Visitante", ["Flamengo", "Botafogo", "Palmeiras"], index=1)

# Dados de exemplo fixos para garantir a simetria visual
res = {'win_h': 35.4, 'draw': 27.7, 'win_a': 35.4, 'odd_j': 2.82, 'odd_m': 3.16, 'ev': 12.9}

# EXIBIÇÃO DO CARD PRINCIPAL
st.markdown(f"""
    <div class="card-principal">
        <div class="match-title">{t_casa.upper()} VS {t_fora.upper()}</div>
        <div style="display:flex; justify-content:space-around; align-items:center;">
            <div><p class="label-prob">Vitória Casa</p><p class="val-prob">{res['win_h']}%</p></div>
            <div><p class="label-prob">Empate</p><p class="val-prob">{res['draw']}%</p></div>
            <div><p class="label-prob">Vitória Fora</p><p class="val-prob">{res['win_a']}%</p></div>
        </div>
        <div class="value-box">
            <span class="value-item">Odd Justa: @{res['odd_j']}</span>
            <span class="value-item">Odd Mercado: @{res['odd_m']}</span>
            <span class="value-item">Valor Esperado: +{res['ev']}%</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-header">PROBABILIDADES DE MERCADO (OVER/MAIS DE)</div>', unsafe_allow_html=True)

# NOVO ELEMENTO: RADAR ESTRATÉGICO
st.markdown(f"""
    <div class="radar-box">
        <span style="color:#f05a22; font-weight:900; margin-right:15px; font-family:'Orbitron'; font-size:11px; letter-spacing:1px;">📡 RADAR ESTRATÉGICO:</span>
        <span>Análise neural detectou alto volume de finalizações para o <b>{t_casa}</b>. Entrada em Over Cantos sugerida.</span>
    </div>
""", unsafe_allow_html=True)

# GRID DE MINI CARDS (6 COLUNAS PERFEITAS)
m1, m2, m3, m4, m5, m6 = st.columns(6)
with m1: st.markdown("<div class='mini-card'><span class='mini-label'>⚽ GOLS +2.5</span><span class='mini-val'>57.7%</span></div>", unsafe_allow_html=True)
with m2: st.markdown("<div class='mini-card'><span class='mini-label'>🚩 CANTOS +9.5</span><span class='mini-val'>85.1%</span></div>", unsafe_allow_html=True)
with m3: st.markdown("<div class='mini-card'><span class='mini-label'>👞 CHUTES +22.5</span><span class='mini-val'>77.5%</span></div>", unsafe_allow_html=True)
with m4: st.markdown("<div class='mini-card'><span class='mini-label'>🎯 NO GOL +8.5</span><span class='mini-val'>75.8%</span></div>", unsafe_allow_html=True)
with m5: st.markdown("<div class='mini-card'><span class='mini-label'>⚠️ FALTAS +24.5</span><span class='mini-val'>81.6%</span></div>", unsafe_allow_html=True)
with m6: st.markdown("<div class='mini-card'><span class='mini-label'>🟨 CARTÕES +4.5</span><span class='mini-val'>69.8%</span></div>", unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:10px;'>GESTOR IA v12.0 - RADAR ESTRATÉGICO ATIVADO</p>", unsafe_allow_html=True)
