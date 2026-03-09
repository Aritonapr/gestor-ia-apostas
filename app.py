import streamlit as st
import pandas as pd
import hashlib

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="GESTOR IA - BET EDITION", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- 2. BANCO DE DADOS ---
DIC_TIMES = {
    "Brasileirão - Série A": ["Flamengo", "Palmeiras", "Botafogo", "Fortaleza", "São Paulo", "Bahia", "Cruzeiro", "Internacional"],
    "Brasileirão - Série B": ["Santos", "Sport", "Novorizontino", "Mirassol", "Vila Nova"],
    "Inglaterra - Premier League": ["Man. City", "Arsenal", "Liverpool", "Aston Villa"],
    "Espanha - La Liga": ["Real Madrid", "Barcelona", "Atlético de Madrid"],
    "Europa - Champions League": ["Real Madrid", "Man. City", "Bayern", "PSG"]
}

# --- 3. CSS ESTILO BETANO (Interface Light & Clean) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    /* Fundo Geral */
    .stApp { background-color: #f0f2f5; font-family: 'Roboto', sans-serif; color: #1a1b1d; }
    
    /* Sidebar Estilo Betano */
    [data-testid="stSidebar"] { 
        background-color: #ffffff !important; 
        border-right: 1px solid #dee2e6 !important; 
        min-width: 280px !important;
    }

    /* Topo Laranja Estilo Betano */
    .betano-header {
        background-color: #f05a22; /* Laranja Betano */
        padding: 15px;
        color: white;
        font-weight: 700;
        font-size: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 20px;
        border-radius: 5px;
    }

    /* Botões da Sidebar (Menu Lateral) */
    .stButton > button {
        width: 100% !important;
        background-color: transparent !important;
        color: #495057 !important;
        border: none !important;
        text-align: left !important;
        padding: 10px 15px !important;
        font-size: 13px !important;
        border-radius: 0px !important;
        border-left: 3px solid transparent !important;
        transition: 0.2s;
    }
    .stButton > button:hover {
        background-color: #f8f9fa !important;
        color: #f05a22 !important;
        border-left: 3px solid #f05a22 !important;
    }
    .stButton > button[kind="primary"] {
        background-color: #e9ecef !important;
        color: #f05a22 !important;
        border-left: 3px solid #f05a22 !important;
        font-weight: 700 !important;
    }

    /* Container de Seleção de Jogo */
    .match-selector {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }

    /* Cards de Probabilidade (Estilo Odds da Betano) */
    .odds-container {
        display: flex;
        gap: 10px;
        margin-top: 15px;
    }
    .odd-box {
        flex: 1;
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 4px;
        padding: 10px;
        text-align: center;
        cursor: default;
    }
    .odd-label { color: #6c757d; font-size: 11px; font-weight: 700; margin-bottom: 5px; }
    .odd-val { color: #008143; font-size: 18px; font-weight: 700; } /* Verde Betano para Odds */

    /* Mini Stats */
    .mini-stat-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
        margin-top: 15px;
    }
    .mini-stat-card {
        background: white;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #dee2e6;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. ENGINE ---
def calcular_engine(casa, fora):
    seed = int(hashlib.sha256((casa + fora).encode()).hexdigest(), 16) % 100
    return 35+(seed%30), 15+(seed%15), 50+(seed%40), 60+(seed%20), 70+(seed%15)

# --- 5. NAVEGAÇÃO SIDEBAR (ESTILO COMPETIÇÕES) ---
if 'liga' not in st.session_state: st.session_state.liga = "Brasileirão - Série A"

with st.sidebar:
    st.markdown("<div style='padding: 10px; font-weight:700; color:#495057;'>⚽ COMPETIÇÕES</div>", unsafe_allow_html=True)
    
    for liga in DIC_TIMES.keys():
        if st.button(liga, key=f"btn_{liga}", type="primary" if st.session_state.liga == liga else "secondary"):
            st.session_state.liga = liga
            st.rerun()

# --- 6. CONTEÚDO PRINCIPAL ---
# Header Betano
st.markdown(f"""
    <div class="betano-header">
        <span style="background: white; color:#f05a22; padding: 2px 8px; border-radius: 4px; font-size: 14px;">IA</span>
        GESTOR IA - ANALYTICS
    </div>
""", unsafe_allow_html=True)

# Área de Seleção
st.markdown('<div class="match-selector">', unsafe_allow_html=True)
st.markdown(f"<div style='color:#6c757d; font-size:12px; margin-bottom:10px;'>{st.session_state.liga}</div>", unsafe_allow_html=True)

times_lista = DIC_TIMES.get(st.session_state.liga)
c1, c2, c3 = st.columns([3, 3, 2])
with c1: t_casa = st.selectbox("Mandante", sorted(times_lista), label_visibility="collapsed")
with c2: t_fora = st.selectbox("Visitante", sorted([t for t in times_lista if t != t_casa]), label_visibility="collapsed")
with c3: executar = st.button("🔥 ANALISAR JOGO", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Resultados
if executar:
    pc, pe, pf, mg, mc = calcular_engine(t_casa, t_fora)
    
    # Simulação de Placar/Odds
    st.markdown(f"""
        <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
            <div style="font-weight:700; font-size:16px; margin-bottom:15px; display:flex; align-items:center; gap:10px;">
                <span style="color:#f05a22;">●</span> RESULTADO DA PARTIDA (PROBABILIDADE)
            </div>
            <div style="text-align:center; font-size:20px; font-weight:700; margin-bottom:20px;">
                {t_casa} <span style="color:#f05a22; font-size:14px;">VS</span> {t_fora}
            </div>
            <div class="odds-container">
                <div class="odd-box"><div class="odd-label">1 (CASA)</div><div class="odd-val">{pc}%</div></div>
                <div class="odd-box"><div class="odd-label">X (EMPATE)</div><div class="odd-val">{pe}%</div></div>
                <div class="odd-box"><div class="odd-label">2 (FORA)</div><div class="odd-val">{pf}%</div></div>
            </div>
        </div>
        
        <div class="mini-stat-grid">
            <div class="mini-stat-card"><div class="odd-label">GOLS +2.5</div><div class="odd-val" style="color:#1a1b1d">{mg}%</div></div>
            <div class="mini-stat-card"><div class="odd-label">CANTOS +9.5</div><div class="odd-val" style="color:#1a1b1d">{mc}%</div></div>
            <div class="mini-stat-card"><div class="odd-label">AMBAS MARCAM</div><div class="odd-val" style="color:#1a1b1d">{pe+10}%</div></div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.info("Selecione os times acima e clique em Analisar Jogo para ver as probabilidades.")
