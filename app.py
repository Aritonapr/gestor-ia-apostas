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
    "BRA_A": ["Flamengo", "Palmeiras", "Botafogo", "Fortaleza", "São Paulo", "Bahia", "Cruzeiro", "Internacional", "Atlético-MG", "Vasco", "Corinthians", "Fluminense", "Grêmio", "Athletico-PR", "Vitória", "Juventude", "Criciúma", "Cuiabá", "Atlético-GO", "Bragantino"],
    "BRA_B": ["Santos", "Sport", "Novorizontino", "Mirassol", "Vila Nova", "América-MG", "Ceará", "Coritiba", "Avaí", "Operário-PR", "Amazonas", "Goiás"],
    "BRA_C": ["Náutico", "Remo", "Figueirense", "CSA", "Botafogo-PB", "ABC", "Londrina", "Caxias", "Ferroviária", "São Bernardo", "Volta Redonda", "Ypiranga"],
    "BRA_D": ["Retrô", "Anápolis", "Iguatu", "Itabaiana", "Brasil de Pelotas", "Maringá", "Inter de Limeira", "Treze"],
    "CDB": ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Atlético-MG", "Vasco", "Grêmio", "Bahia", "Internacional", "Fluminense"],
    "SUPER": ["Palmeiras", "São Paulo", "Flamengo", "Atlético-MG", "Corinthians"],
    "CNE": ["Bahia", "Fortaleza", "Sport", "Ceará", "Vitória", "CRB", "Náutico", "Sampaio Corrêa"],
    "SP": ["Palmeiras", "Santos", "São Paulo", "Corinthians", "Bragantino", "Novorizontino", "Inter de Limeira", "Ponte Preta"],
    "RJ": ["Flamengo", "Fluminense", "Botafogo", "Vasco", "Nova Iguaçu", "Boavista"],
    "MG": ["Cruzeiro", "Atlético-MG", "América-MG", "Tombense", "Villa Nova"],
    "RS": ["Grêmio", "Internacional", "Juventude", "Caxias", "Brasil de Pelotas"],
    "ENG_P": ["Man. City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Man. United"],
    "ESP_L": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Athletic Bilbao"],
    "ITA_A": ["Inter de Milão", "Milan", "Juventus", "Atalanta", "Roma", "Napoli"],
    "GER_B": ["Bayer Leverkusen", "Bayern de Munique", "Stuttgart", "RB Leipzig", "Borussia Dortmund"],
    "FRA_L": ["PSG", "Monaco", "Lille", "Brest", "Lyon", "Marseille"],
    "POR_L": ["Sporting", "Benfica", "Porto", "Braga"],
    "HOL_E": ["PSV Eindhoven", "Feyenoord", "Ajax", "AZ Alkmaar"],
    "UCL": ["Real Madrid", "Man. City", "Bayern", "Arsenal", "Barcelona", "Inter", "PSG"],
    "UEL": ["Man. United", "Tottenham", "Roma", "Porto", "Ajax"],
    "EURO_C": ["Espanha", "Inglaterra", "França", "Alemanha", "Portugal", "Itália", "Holanda"],
    "ELIM_W": ["Brasil", "Argentina", "França", "Inglaterra", "Espanha", "Alemanha"],
    "ARG_L": ["River Plate", "Boca Juniors", "Racing", "Talleres", "Estudiantes"],
    "SAUDI": ["Al-Hilal", "Al-Nassr", "Al-Ittihad", "Al-Ahli", "Al-Ettifaq"],
    "USA_MLS": ["Inter Miami", "LA Galaxy", "Columbus Crew", "LAFC", "Cincinnati"],
    "LIB": ["Flamengo", "Palmeiras", "River Plate", "Botafogo", "São Paulo", "Atlético-MG"],
    "SUL": ["Cruzeiro", "Corinthians", "Fortaleza", "Racing", "Lanús", "Athletico-PR"]
}

# --- 3. CSS REALINHADO E FUTURISTA ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    header[data-testid="stHeader"] { background: transparent !important; height: 0 !important; display: none !important; }
    .block-container { padding-top: 0rem !important; padding-bottom: 0rem !important; }
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    [data-testid="stSidebar"] { background-color: #0b1218 !important; border-right: 1px solid rgba(240, 90, 34, 0.4) !important; width: 320px !important; }
    
    .stButton > button { background-color: rgba(26, 36, 45, 0.7) !important; color: #cbd5e0 !important; font-size: 7.2pt !important; border-radius: 4px !important; margin-bottom: 2px !important; border: none !important; }
    .cat-button > div > button { background-color: rgba(240, 90, 34, 0.1) !important; color: #fff !important; height: 42px !important; font-size: 8.5pt !important; letter-spacing: 1px; border-bottom: 1px solid #f05a22 !important; }
    .stButton > button[kind="primary"] { background-color: rgba(240, 90, 34, 0.25) !important; color: #f05a22 !important; border-left: 5px solid #f05a22 !important; }
    
    .card-principal { background-color: #161f27; padding: 25px; border-radius: 15px; border-bottom: 4px solid #f05a22; text-align: center; margin-top: 10px; }
    
    /* CORREÇÃO DOS 6 ÍCONES: FLEXBOX SEM QUEBRA */
    .stats-flex {
        display: flex; 
        justify-content: space-between; 
        gap: 8px; 
        margin-top: 20px; 
        width: 100%;
        flex-wrap: nowrap !important; /* PROÍBE PULAR LINHA */
    }
    .mini-card { 
        flex: 1; /* CADA CARD OCUPA O MESMO ESPAÇO */
        background-color: #111a21; 
        padding: 15px 5px; 
        border-radius: 10px; 
        border: 1px solid #2d3748; 
        text-align: center;
        min-width: 0; /* PERMITE ENCOLHER PARA CABER */
        transition: 0.3s;
    }
    .mini-card:hover { border-color: #f05a22; box-shadow: 0 0 10px rgba(240, 90, 34, 0.2); }
    .mini-label { color: #8a99a8 !important; font-size: 7px !important; font-weight: 800; text-transform: uppercase; margin-bottom: 6px; display: block; white-space: nowrap; }
    .mini-val { color: #00ffc3 !important; font-weight: 900; font-size: 17px !important; margin: 0; }
    </style>
""", unsafe_allow_html=True)

# --- 4. ENGINE ---
def calcular_engine(casa, fora):
    seed = int(hashlib.sha256((casa + fora).encode()).hexdigest(), 16) % 100
    pc = 35 + (seed % 30); pe = 15 + (seed % 15); pf = 100 - pc - pe
    return pc, pe, pf, 50+(seed%40), 60+(seed%35), 65+(seed%30)

# --- 5. NAVEGAÇÃO ---
if 'liga_ativa' not in st.session_state: st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A')
if 'menu_aberto' not in st.session_state: st.session_state.menu_aberto = 'BR'

with st.sidebar:
    def s_btn(display, full, vid):
        if st.button(display, key=f"s_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid; st.session_state.nome_liga = full; st.rerun()

    def cat_btn(label, menu_id):
        st.markdown('<div class="cat-button">', unsafe_allow_html=True)
        if st.button(label, key=f"cat_{menu_id}"):
            st.session_state.menu_aberto = menu_id if st.session_state.menu_aberto != menu_id else None; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    cat_btn("🇧🇷 FUTEBOL BRASILEIRO", "BR")
    if st.session_state.menu_aberto == "BR":
        c1, c2 = st.columns(2)
        with c1: s_btn("SÉRIE A", "BRASILEIRÃO A", "BRA_A"); s_btn("SÉRIE C", "BRASILEIRÃO C", "BRA_C")
        with c2: s_btn("SÉRIE B", "BRASILEIRÃO B", "BRA_B"); s_btn("SÉRIE D", "BRASILEIRÃO D", "BRA_D")
        c3, c4 = st.columns(2)
        with c3: s_btn("COPA BRASIL", "COPA DO BRASIL", "CDB"); s_btn("SUPERCOPA", "SUPERCOPA DO BRASIL", "SUPER")
        with c4: s_btn("NORDESTE", "COPA DO NORDESTE", "CNE")
        c5, c6 = st.columns(2)
        with c5: s_btn("PAULISTÃO", "PAULISTÃO", "SP"); s_btn("MINEIRO", "CAMPEONATO MINEIRO", "MG")
        with c6: s_btn("CARIOCA", "CAMPEONATO CARIOCA", "RJ"); s_btn("GAÚCHO", "CAMPEONATO GAÚCHO", "RS")

    cat_btn("🇪🇺 LIGAS ELITE EUROPA", "EU_L")
    if st.session_state.menu_aberto == "EU_L":
        c1, c2 = st.columns(2)
        with c1: s_btn("🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER", "PREMIER LEAGUE", "ENG_P"); s_btn("🇮🇹 SERIE A", "SERIE A TIM", "ITA_A")
        with c2: s_btn("🇪🇸 LA LIGA", "LA LIGA", "ESP_L"); s_btn("🇩🇪 BUNDES", "BUNDESLIGA", "GER_B")

    cat_btn("🌍 UEFA & SELEÇÕES", "UEFA")
    if st.session_state.menu_aberto == "UEFA":
        s_btn("⭐ CHAMPIONS LEAGUE", "UEFA CHAMPIONS LEAGUE", "UCL")
        s_btn("🛡️ EUROCOPA", "EUROCOPA", "EURO_C")

    cat_btn("🔥 AMÉRICA DO SUL", "SAM")
    if st.session_state.menu_aberto == "SAM":
        s_btn("🏆 LIBERTADORES", "COPA LIBERTADORES", "LIB")
        s_btn("🛰️ SUL-AMERICANA", "COPA SUL-AMERICANA", "SUL")

# --- 6. CABEÇALHO COM ÍCONE FUTURISTA ---
st.markdown("""
    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px; padding-top: 15px;">
        <div style="position: relative; width: 45px; height: 45px; display: flex; align-items: center; justify-content: center;">
            <svg style="position: absolute; width: 100%; height: 100%; filter: drop-shadow(0 0 8px #f05a22);" viewBox="0 0 100 100">
                <path d="M50 5 L93.3 30 L93.3 80 L50 105 L6.7 80 L6.7 30 Z" fill="none" stroke="#f05a22" stroke-width="4"/>
                <path d="M50 20 L76 35 L76 65 L50 80 L24 65 L24 35 Z" fill="#f05a22" opacity="0.4"/>
                <circle cx="50" cy="50" r="8" fill="#fff" />
            </svg>
        </div>
        <div style="color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 22px; font-weight: 900; letter-spacing: 2.5px;">
            GESTOR IA <span style="color: #ffffff; font-size: 11px; letter-spacing: 1px; margin-left: 10px; opacity: 0.8;">PRO EDITION</span>
        </div>
    </div>
""", unsafe_allow_html=True)

times_lista = DIC_TIMES.get(st.session_state.liga_ativa, ["Selecione..."])
col1, col2, col3 = st.columns([3, 3, 2.5])
with col1: t_casa = st.selectbox("Mandante", sorted(times_lista), label_visibility="collapsed")
with col2: t_fora = st.selectbox("Visitante", sorted([t for t in times_lista if t != t_casa]), label_visibility="collapsed")
with col3: executar = st.button("🔥 PROCESSAR ALGORITMO", use_container_width=True, type="primary")

if executar:
    pc, pe, pf, mg, mc, mch = calcular_engine(t_casa, t_fora)
    st.markdown(f'<div style="font-size:11px; color:#f05a22; font-family:Orbitron; border-left:4px solid #f05a22; padding-left:10px; margin-bottom:12px;">📡 DATA-ANALYSIS: {st.session_state.nome_liga}</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="card-principal">
            <div style="color: #fff; font-family: Orbitron; font-size: 24px; font-weight: 800; margin-bottom: 25px;">{t_casa.upper()} <span style="color:#f05a22">vs</span> {t_fora.upper()}</div>
            <div style="display: flex; justify-content: space-around;">
                <div><p style="color:#f05a22; font-size:32px; font-weight:900; margin:0;">{pc}%</p><p style="color:#8a99a8; font-size:10px; font-weight:800;">VITÓRIA CASA</p></div>
                <div><p style="color:#fff; font-size:32px; font-weight:900; margin:0;">{pe}%</p><p style="color:#8a99a8; font-size:10px; font-weight:800;">EMPATE</p></div>
                <div><p style="color:#f05a22; font-size:32px; font-weight:900; margin:0;">{pf}%</p><p style="color:#8a99a8; font-size:10px; font-weight:800;">VITÓRIA FORA</p></div>
            </div>
        </div>
        
        <!-- ESTE BLOCO AGORA ESTÁ BLINDADO PARA FICAR EM UMA SÓ LINHA -->
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
    st.markdown("<div style='height:250px; display:flex; align-items:center; justify-content:center; color:#2d3748; font-family:Orbitron; font-size:12px; opacity:0.6;'>SELECIONE UM CONFRONTO...</div>", unsafe_allow_html=True)
