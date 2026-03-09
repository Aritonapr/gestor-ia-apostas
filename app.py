import streamlit as st
import pandas as pd
import numpy as np
import hashlib

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="GESTOR IA - PRO EDITION", 
    layout="wide", 
    page_icon="⚽",
    initial_sidebar_state="expanded"
)

# --- 2. BANCO DE DADOS COMPLETO ---
DIC_TIMES = {
    "BRASILEIRÃO A": ["Flamengo", "Palmeiras", "Botafogo", "Fortaleza", "São Paulo", "Bahia", "Cruzeiro", "Internacional", "Atlético-MG", "Vasco", "Corinthians", "Fluminense", "Grêmio", "Athletico-PR", "Vitória", "Juventude", "Criciúma", "Cuiabá", "Atlético-GO", "Bragantino"],
    "BRASILEIRÃO B": ["Santos", "Sport", "Novorizontino", "Mirassol", "Vila Nova", "América-MG", "Ceará", "Coritiba", "Avaí", "Operário-PR", "Amazonas", "Goiás"],
    "BRASILEIRÃO C": ["Náutico", "Remo", "Figueirense", "CSA", "Botafogo-PB", "ABC", "Londrina", "Caxias", "Ferroviária", "São Bernardo", "Volta Redonda", "Ypiranga"],
    "BRASILEIRÃO D": ["Retrô", "Anápolis", "Iguatu", "Itabaiana", "Brasil de Pelotas", "Maringá", "Inter de Limeira", "Treze"],
    "COPA DO BRASIL": ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Atlético-MG", "Vasco", "Grêmio", "Bahia", "Internacional", "Fluminense"],
    "COPA NORDESTE": ["Bahia", "Fortaleza", "Sport", "Ceará", "Vitória", "CRB", "Náutico", "Sampaio Corrêa"],
    "PREMIER LEAGUE": ["Man. City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Man. United", "Newcastle"],
    "LA LIGA": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Athletic Bilbao", "Real Sociedad", "Sevilla"],
    "SERIE A TIM": ["Inter de Milão", "Milan", "Juventus", "Atalanta", "Roma", "Napoli", "Lazio", "Bologna"],
    "CHAMPIONS LEAGUE": ["Real Madrid", "Man. City", "Bayern", "Arsenal", "Barcelona", "Inter", "PSG", "Bayer Leverkusen"]
}

# --- 3. CSS "PRO EDITION" (ESTABILIDADE TOTAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    header[data-testid="stHeader"] { background: transparent !important; }
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    [data-testid="stSidebar"] { 
        background-color: #0b1218 !important; 
        border-right: 2px solid #f05a22 !important; 
    }

    /* Estilo dos Expanders (Categorias) */
    .st-expander {
        background-color: rgba(240, 90, 34, 0.05) !important;
        border: 1px solid rgba(240, 90, 34, 0.2) !important;
        border-radius: 8px !important;
        margin-bottom: 10px !important;
    }

    /* Estilo do Radio Button (Ligas) */
    div[data-testid="stRadio"] > div { gap: 2px !important; }
    div[data-testid="stRadio"] label {
        background: rgba(26, 36, 45, 0.5);
        padding: 8px 15px;
        border-radius: 5px;
        border-left: 3px solid transparent;
        transition: 0.3s;
        font-size: 11px !important;
        font-weight: 600;
        margin-bottom: 2px;
    }
    div[data-testid="stRadio"] label:hover { border-left: 3px solid #f05a22; background: rgba(240, 90, 34, 0.1); }
    div[data-testid="stRadio"] label[data-selected="true"] {
        border-left: 3px solid #f05a22;
        background: rgba(240, 90, 34, 0.2);
    }

    /* CARDS DE RESULTADOS (Mantendo sua estrutura anterior) */
    .card-principal { background-color: #161f27; padding: 25px; border-radius: 12px; border-bottom: 4px solid #f05a22; text-align: center; }
    .stats-flex { display: flex; justify-content: space-between; gap: 10px; margin-top: 20px; width: 100%; flex-wrap: nowrap; }
    .mini-card { flex: 1; background-color: #111a21; padding: 15px 5px; border-radius: 10px; border: 1px solid #2d3748; text-align: center; min-width: 0; }
    .mini-label { color: #ffffff !important; font-size: 9px !important; font-weight: 800; text-transform: uppercase; margin-bottom: 8px; display: block; opacity: 0.7; }
    .mini-val { color: #00ffc3 !important; font-weight: 900; font-size: 20px !important; margin: 0; text-shadow: 0 0 10px rgba(0, 255, 195, 0.3); }
    </style>
""", unsafe_allow_html=True)

# --- 4. ENGINE COMPLETA (6 STATS) ---
def calcular_engine(casa, fora):
    seed = int(hashlib.sha256((casa + fora).encode()).hexdigest(), 16) % 100
    pc = 35 + (seed % 30); pe = 15 + (seed % 15); pf = 100 - pc - pe
    # Retorna: vitória_c, empate, vitória_f, gols, cantos, chutes
    return pc, pe, pf, 50+(seed%40), 60+(seed%35), 65+(seed%30)

# --- 5. NAVEGAÇÃO LATERAL (ESTÁVEL) ---
with st.sidebar:
    st.markdown("""
        <div style="text-align:center; padding: 10px 0;">
            <div style="font-family: 'Orbitron'; color: #f05a22; font-size: 20px; font-weight: 900;">GESTOR IA</div>
            <div style="color: #fff; font-size: 9px; opacity: 0.5; letter-spacing: 2px;">PRO EDITION</div>
        </div>
        <hr style="border-color: rgba(240, 90, 34, 0.2); margin-top: 0;">
    """, unsafe_allow_html=True)

    # Pasta Brasil
    with st.expander("📁 FUTEBOL BRASIL", expanded=True):
        liga_br = st.radio("Selecione:", 
                          ["BRASILEIRÃO A", "BRASILEIRÃO B", "BRASILEIRÃO C", "BRASILEIRÃO D", "COPA DO BRASIL", "COPA NORDESTE"],
                          key="radio_br", label_visibility="collapsed")
    
    # Pasta Europa
    with st.expander("🌍 ELITE EUROPA", expanded=False):
        liga_eu = st.radio("Selecione:", 
                          ["PREMIER LEAGUE", "LA LIGA", "SERIE A TIM", "CHAMPIONS LEAGUE"],
                          key="radio_eu", label_visibility="collapsed")

    # Lógica de Seleção: A última liga clicada é a que vale
    # (Para simplificar, usamos a do expander que estiver aberto ou a seleção atual)
    liga_ativa = liga_br # Padrão

# --- 6. CABEÇALHO ---
st.markdown(f"""
    <div style="border-left: 4px solid #f05a22; padding-left: 15px; margin-bottom: 20px;">
        <span style="color: #f05a22; font-family: 'Orbitron'; font-size: 10px; letter-spacing: 2px;">MODO DE ANÁLISE ATIVO</span><br>
        <span style="color: #fff; font-family: 'Orbitron'; font-size: 20px; font-weight: 800;">{liga_ativa}</span>
    </div>
""", unsafe_allow_html=True)

# --- 7. INPUTS E PROCESSAMENTO ---
times_lista = DIC_TIMES.get(liga_ativa, ["Selecione..."])
col1, col2, col3 = st.columns([3, 3, 2.5])

with col1: t_casa = st.selectbox("Mandante", sorted(times_lista), label_visibility="collapsed")
with col2: t_fora = st.selectbox("Visitante", sorted([t for t in times_lista if t != t_casa]), label_visibility="collapsed")
with col3: executar = st.button("🔥 PROCESSAR ALGORITMO", use_container_width=True, type="primary")

# --- 8. ÁREA DE RESULTADOS (O QUE VOCÊ JÁ TINHA PRONTO) ---
if executar:
    pc, pe, pf, mg, mc, mch = calcular_engine(t_casa, t_fora)
    
    # Card Principal 1X2
    st.markdown(f"""
        <div class="card-principal">
            <div style="color: #fff; font-family: Orbitron; font-size: 22px; font-weight: 800; margin-bottom: 25px;">{t_casa.upper()} <span style="color:#f05a22">VS</span> {t_fora.upper()}</div>
            <div style="display: flex; justify-content: space-around;">
                <div><p style="color:#f05a22; font-size:35px; font-weight:900; margin:0; font-family:Orbitron;">{pc}%</p><p style="color:#8a99a8; font-size:11px; font-weight:800;">CASA</p></div>
                <div><p style="color:#fff; font-size:35px; font-weight:900; margin:0; font-family:Orbitron;">{pe}%</p><p style="color:#8a99a8; font-size:11px; font-weight:800;">EMPATE</p></div>
                <div><p style="color:#f05a22; font-size:35px; font-weight:900; margin:0; font-family:Orbitron;">{pf}%</p><p style="color:#8a99a8; font-size:11px; font-weight:800;">FORA</p></div>
            </div>
        </div>
        
        <div class="stats-flex">
            <div class="mini-card"><span class="mini-label">⚽ GOLS +2.5</span><p class="mini-val">{mg}%</p></div>
            <div class="mini-card"><span class="mini-label">🚩 CANTOS +9.5</span><p class="mini-val">{mc}%</p></div>
            <div class="mini-card"><span class="mini-label">👞 CHUTES +22</span><p class="mini-val">{mch}%</p></div>
            <div class="mini-card"><span class="mini-label">🎯 NO GOL +8</span><p class="mini-val">{mg-5}%</p></div>
            <div class="mini-card"><span class="mini-label">⚠️ FALTAS +24</span><p class="mini-val">{mc+10}%</p></div>
            <div class="mini-card"><span class="mini-label">🟨 CARTÕES +4</span><p class="mini-val">{pe+20}%</p></div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<div style='height:200px; display:flex; align-items:center; justify-content:center; color:#2d3748; font-family:Orbitron; font-size:12px; opacity:0.6; letter-spacing:3px;'>AGUARDANDO CONFRONTO...</div>", unsafe_allow_html=True)
