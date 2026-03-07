import streamlit as st
import pandas as pd
import numpy as np
import hashlib

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="GESTOR IA - GLOBAL ELITE", 
    layout="wide", 
    page_icon="⚽",
    initial_sidebar_state="expanded"
)

# --- 2. BANCO DE DADOS (GLOBAL) ---
DIC_TIMES = {
    "BRA_A": ["Flamengo", "Palmeiras", "Botafogo", "Fortaleza", "São Paulo", "Bahia", "Cruzeiro", "Internacional", "Atlético-MG", "Vasco", "Corinthians", "Fluminense", "Grêmio", "Athletico-PR", "Vitória", "Juventude", "Criciúma", "Cuiabá", "Atlético-GO", "Bragantino"],
    "BRA_B": ["Santos", "Sport", "Novorizontino", "Mirassol", "Vila Nova", "América-MG", "Ceará", "Coritiba", "Avaí", "Operário-PR", "Amazonas", "Goiás"],
    "CDB": ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Atlético-MG", "Grêmio", "Vasco", "Bahia", "Botafogo", "Internacional"],
    "CNE": ["Bahia", "Fortaleza", "Sport", "Ceará", "Vitória", "CRB", "Náutico"],
    "ENG_P": ["Man. City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Newcastle", "Man. United", "West Ham", "Brighton"],
    "ESP_L": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Athletic Bilbao", "Real Sociedad", "Villarreal", "Sevilla"],
    "ITA_A": ["Inter de Milão", "Milan", "Juventus", "Atalanta", "Bologna", "Roma", "Lazio", "Napoli"],
    "GER_B": ["Bayer Leverkusen", "Bayern de Munique", "Stuttgart", "RB Leipzig", "Borussia Dortmund", "Eintracht Frankfurt"],
    "FRA_L": ["PSG", "Monaco", "Brest", "Lille", "Nice", "Lyon", "Marseille"],
    "POR_L": ["Sporting", "Benfica", "Porto", "Braga", "Vitória de Guimarães"],
    "HOL_E": ["PSV Eindhoven", "Feyenoord", "Ajax", "AZ Alkmaar", "Twente"],
    "ENG_FA": ["Man. City", "Man. United", "Liverpool", "Arsenal", "Chelsea"],
    "ESP_CR": ["Real Madrid", "Barcelona", "Athletic Bilbao", "Mallorca"],
    "ITA_CI": ["Inter", "Juventus", "Milan", "Atalanta", "Lazio"],
    "GER_C": ["Bayer Leverkusen", "Bayern", "Dortmund", "Leipzig"],
    "UCL": ["Real Madrid", "Man. City", "Bayern", "Arsenal", "Barcelona", "Inter", "PSG", "Bayer Leverkusen"],
    "UEL": ["Man. United", "Tottenham", "Roma", "Porto", "Ajax", "Lazio"],
    "EURO_C": ["Espanha", "Inglaterra", "França", "Alemanha", "Portugal", "Itália", "Holanda"],
    "ELIM_W": ["Brasil", "Argentina", "França", "Inglaterra", "Espanha", "Alemanha", "Uruguai", "Colômbia"],
    "COPA_AME": ["Argentina", "Brasil", "Uruguai", "Colômbia", "Equador", "EUA", "México"],
    "ARG_L": ["River Plate", "Boca Juniors", "Racing", "Talleres", "Estudiantes", "Vélez Sarsfield"],
    "SAUDI": ["Al-Hilal", "Al-Nassr", "Al-Ittihad", "Al-Ahli", "Al-Ettifaq", "Al-Qadsiah"],
    "USA_MLS": ["Inter Miami", "LA Galaxy", "Columbus Crew", "LAFC", "Cincinnati", "New York City"],
    "LIB": ["Flamengo", "Palmeiras", "River Plate", "Botafogo", "São Paulo", "Atlético-MG", "Peñarol"],
    "SUL": ["Cruzeiro", "Corinthians", "Fortaleza", "Racing", "Lanús", "Athletico-PR"]
}

# --- 3. CSS ULTRA-CORRIGIDO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #0b1218; border-right: 1px solid rgba(240, 90, 34, 0.3); width: 300px !important; }
    
    /* BOTOES SIDEBAR */
    .stButton > button { background-color: rgba(26, 36, 45, 0.6) !important; color: #cbd5e0 !important; font-size: 7.2pt !important; border-radius: 4px !important; margin-bottom: 2px !important; border: none !important; }
    .cat-button > div > button { background-color: rgba(240, 90, 34, 0.08) !important; color: #fff !important; height: 38px !important; font-size: 8pt !important; letter-spacing: 1px; border-bottom: 1px solid #f05a22 !important; }
    .stButton > button[kind="primary"] { background-color: rgba(240, 90, 34, 0.15) !important; color: #f05a22 !important; border-left: 4px solid #f05a22 !important; }
    
    /* CARD PRINCIPAL */
    .card-principal { background-color: #161f27; padding: 20px; border-radius: 12px; border-bottom: 4px solid #f05a22; text-align: center; margin-top: 10px; }
    
    /* GRID DE ESTATÍSTICAS - RESOLVE O ERRO DE LAYOUT */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 8px;
        margin-top: 15px;
        width: 100%;
    }
    
    .mini-card { 
        background-color: #111a21; 
        padding: 12px 5px; 
        border-radius: 8px; 
        border: 1px solid #2d3748; 
        text-align: center;
        min-height: 80px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .mini-label { 
        color: #8a99a8 !important; 
        font-size: 7.5px !important; 
        font-weight: 800; 
        text-transform: uppercase; 
        margin-bottom: 5px;
        letter-spacing: 0.5px;
    }
    .mini-val { 
        color: #00ffc3 !important; 
        font-weight: 900; 
        font-size: 18px !important; 
        margin: 0;
        text-shadow: 0 0 10px rgba(0, 255, 195, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. ENGINE DE SIMULAÇÃO ---
def simular_probabilidades(casa, fora):
    seed = int(hashlib.sha256((casa + fora).encode()).hexdigest(), 16) % 100
    p_casa = 35 + (seed % 30)
    p_empate = 15 + (seed % 15)
    p_fora = 100 - p_casa - p_empate
    m_gols = 50 + (seed % 40)
    m_cantos = 60 + (seed % 35)
    m_chutes = 65 + (seed % 30)
    return p_casa, p_empate, p_fora, m_gols, m_cantos, m_chutes

# --- 5. LÓGICA DE NAVEGAÇÃO ---
if 'liga_ativa' not in st.session_state: st.session_state.update(liga_ativa='BRA_A', nome_liga='BRASILEIRÃO A')
if 'menu_aberto' not in st.session_state: st.session_state.menu_aberto = None

with st.sidebar:
    def s_btn(display, full, vid):
        if st.button(display, key=f"s_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid; st.session_state.nome_liga = full; st.rerun()

    def cat_btn(label, menu_id):
        st.markdown('<div class="cat-button">', unsafe_allow_html=True)
        if st.button(label, key=f"cat_{menu_id}"):
            st.session_state.menu_aberto = menu_id if st.session_state.menu_aberto != menu_id else None
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    cat_btn("🇧🇷 BRASIL", "BR")
    if st.session_state.menu_aberto == "BR":
        c1, c2 = st.columns(2)
        with c1: s_btn("SÉRIE A", "BRASILEIRÃO A", "BRA_A"); s_btn("COPA BR", "COPA DO BRASIL", "CDB")
        with c2: s_btn("SÉRIE B", "BRASILEIRÃO B", "BRA_B"); s_btn("NORDESTE", "COPA NORDESTE", "CNE")

    cat_btn("🇪🇺 LIGAS ELITE EURO", "EU_L")
    if st.session_state.menu_aberto == "EU_L":
        c1, c2 = st.columns(2)
        with c1: s_btn("🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER", "PREMIER LEAGUE", "ENG_P"); s_btn("🇮🇹 SERIE A", "SERIE A TIM", "ITA_A"); s_btn("🇵🇹 PORTUGAL", "LIGA PORTUGAL", "POR_L")
        with c2: s_btn("🇪🇸 LA LIGA", "LA LIGA", "ESP_L"); s_btn("🇩🇪 BUNDES", "BUNDESLIGA", "GER_B"); s_btn("🇳🇱 HOLANDA", "EREDIVISIE", "HOL_E")

    cat_btn("🏆 COPAS NACIONAIS", "EU_C")
    if st.session_state.menu_aberto == "EU_C":
        c1, c2 = st.columns(2)
        with c1: s_btn("FA CUP", "FA CUP", "ENG_FA"); s_btn("COP. ITÁLIA", "COPPA ITALIA", "ITA_CI")
        with c2: s_btn("COP. REI", "COPA DEL REY", "ESP_CR"); s_btn("DFB POKAL", "COPA ALEMANHA", "GER_C")

    cat_btn("🌍 UEFA & SELEÇÕES", "UEFA")
    if st.session_state.menu_aberto == "UEFA":
        s_btn("⭐ CHAMPIONS", "CHAMPIONS LEAGUE", "UCL")
        s_btn("🇪🇺 EUROPA LEAGUE", "EUROPA LEAGUE", "UEL")
        s_btn("🛡️ EUROCOPA", "EUROCOPA", "EURO_C")
        s_btn("🌎 ELIMINATÓRIAS", "ELIMINATÓRIAS MUNDIAL", "ELIM_W")

    cat_btn("⭐ NOVOS MERCADOS", "NEW")
    if st.session_state.menu_aberto == "NEW":
        s_btn("🇸🇦 SAUDI PRO", "SAUDI PRO LEAGUE", "SAUDI")
        s_btn("🇺🇸 MLS", "MLS USA", "USA_MLS")
        s_btn("🇦🇷 ARGENTINA", "LIGA ARGENTINA", "ARG_L")

    cat_btn("🔥 AMÉRICA DO SUL", "SAM")
    if st.session_state.menu_aberto == "SAM":
        s_btn("🏆 LIBERTADORES", "LIBERTADORES", "LIB")
        s_btn("🛰️ SUL-AMERICANA", "SUL-AMERICANA", "SUL")
        s_btn("🏟️ COPA AMÉRICA", "COPA AMÉRICA", "COPA_AME")

# --- 6. CONTEÚDO PRINCIPAL ---
st.markdown('<div style="color:#f05a22; font-family:Orbitron; font-size:22px; font-weight:900; margin-bottom:15px;">GESTOR IA <span style="color:#fff; font-size:11px;">GLOBAL EDITION 25/26</span></div>', unsafe_allow_html=True)

times_lista = DIC_TIMES.get(st.session_state.liga_ativa, ["Escolha a Liga"])
col1, col2, col3 = st.columns([3, 3, 2.5])
with col1: t_casa = st.selectbox("Mandante", sorted(times_lista), label_visibility="collapsed")
with col2: t_fora = st.selectbox("Visitante", sorted([t for t in times_lista if t != t_casa]), label_visibility="collapsed")
with col3: executar = st.button("🔥 PROCESSAR ALGORITMO", use_container_width=True, type="primary")

if executar:
    pc, pe, pf, mg, mc, mch = simular_probabilidades(t_casa, t_fora)
    st.markdown(f'<div style="font-size:10px; color:#f05a22; font-family:Orbitron; border-left:4px solid #f05a22; padding-left:10px;">📡 DATA-ANALYSIS: {st.session_state.nome_liga}</div>', unsafe_allow_html=True)
    
    # CARD PRINCIPAL
    st.markdown(f"""
        <div class="card-principal">
            <div style="color: #fff; font-family: Orbitron; font-size: 22px; font-weight: 800; margin-bottom: 25px;">{t_casa.upper()} <span style="color:#f05a22">vs</span> {t_fora.upper()}</div>
            <div style="display: flex; justify-content: space-around; align-items: center;">
                <div><p style="color:#f05a22; font-size:28px; font-weight:900; margin:0;">{pc}%</p><p style="color:#8a99a8; font-size:9px; font-weight:700;">VITÓRIA CASA</p></div>
                <div style="width:1px; height:40px; background:rgba(255,255,255,0.1);"></div>
                <div><p style="color:#fff; font-size:28px; font-weight:900; margin:0;">{pe}%</p><p style="color:#8a99a8; font-size:9px; font-weight:700;">EMPATE</p></div>
                <div style="width:1px; height:40px; background:rgba(255,255,255,0.1);"></div>
                <div><p style="color:#f05a22; font-size:28px; font-weight:900; margin:0;">{pf}%</p><p style="color:#8a99a8; font-size:9px; font-weight:700;">VITÓRIA FORA</p></div>
            </div>
        </div>
        
        <!-- GRID DE ESTATÍSTICAS EM BLOCO ÚNICO -->
        <div class="stats-grid">
            <div class="mini-card"><p class="mini-label">⚽ GOLS +2.5</p><p class="mini-val">{mg}%</p></div>
            <div class="mini-card"><p class="mini-label">🚩 CANTOS +9.5</p><p class="mini-val">{mc}%</p></div>
            <div class="mini-card"><p class="mini-label">👞 CHUTES +22</p><p class="mini-val">{mch}%</p></div>
            <div class="mini-card"><p class="mini-label">🎯 NO GOL +8</p><p class="mini-val">{mg-5}%</p></div>
            <div class="mini-card"><p class="mini-label">⚠️ FALTAS +24</p><p class="mini-val">{mc+10}%</p></div>
            <div class="mini-card"><p class="mini-label">🟨 CARTÕES +4</p><p class="mini-val">{pe+20}%</p></div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<div style='height:250px; display:flex; align-items:center; justify-content:center; color:#4a5568; font-size:11px; letter-spacing:2px; font-family:Orbitron;'>AGUARDANDO SELEÇÃO DE CONFRONTO...</div>", unsafe_allow_html=True)
