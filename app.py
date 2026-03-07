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

# --- 2. BANCO DE DADOS COMPLETO (BRASIL + GLOBAL) ---
DIC_TIMES = {
    # BRASIL COMPLETO
    "BRA_A": ["Flamengo", "Palmeiras", "Botafogo", "Fortaleza", "São Paulo", "Bahia", "Cruzeiro", "Internacional", "Atlético-MG", "Vasco", "Corinthians", "Fluminense", "Grêmio", "Athletico-PR", "Vitória", "Juventude", "Criciúma", "Cuiabá", "Atlético-GO", "Bragantino"],
    "BRA_B": ["Santos", "Sport", "Novorizontino", "Mirassol", "Vila Nova", "América-MG", "Ceará", "Coritiba", "Avaí", "Operário-PR", "Amazonas", "Goiás"],
    "BRA_C": ["Náutico", "Remo", "Figueirense", "CSA", "Botafogo-PB", "ABC", "Londrina", "Caxias", "Ferroviária", "São Bernardo", "Volta Redonda", "Ypiranga"],
    "BRA_D": ["Retrô", "Anápolis", "Iguatu", "Itabaiana", "Brasil de Pelotas", "Maringá", "Inter de Limeira", "Treze"],
    "CDB": ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Atlético-MG", "Grêmio", "Vasco", "Bahia", "Botafogo", "Internacional"],
    "SUPER": ["Palmeiras", "São Paulo", "Flamengo", "Atlético-MG"],
    "CNE": ["Bahia", "Fortaleza", "Sport", "Ceará", "Vitória", "CRB", "Náutico", "Sampaio Corrêa"],
    "SP": ["Palmeiras", "Santos", "São Paulo", "Corinthians", "Bragantino", "Novorizontino", "Inter de Limeira", "Ponte Preta"],
    "RJ": ["Flamengo", "Fluminense", "Vasco", "Botafogo", "Nova Iguaçu", "Portuguesa-RJ", "Boavista"],
    "MG": ["Atlético-MG", "Cruzeiro", "América-MG", "Tombense", "Villa Nova", "Ipatinga"],
    "RS": ["Grêmio", "Internacional", "Juventude", "Caxias", "Brasil de Pelotas", "São José"],

    # INTERNACIONAL
    "ENG_P": ["Man. City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Man. United"],
    "ESP_L": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Athletic Bilbao", "Sevilla"],
    "UCL": ["Real Madrid", "Man. City", "Bayern", "Arsenal", "Barcelona", "Inter", "PSG"],
    "LIB": ["Flamengo", "Palmeiras", "River Plate", "Botafogo", "São Paulo", "Atlético-MG"],
    "SAUDI": ["Al-Hilal", "Al-Nassr", "Al-Ittihad", "Al-Ahli"],
    "USA_MLS": ["Inter Miami", "LA Galaxy", "Columbus Crew", "LAFC"]
}

# --- 3. CSS BLINDADO (RE-ESTRUTURADO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #0b1218; border-right: 1px solid rgba(240, 90, 34, 0.3); width: 300px !important; }
    
    .stButton > button { background-color: rgba(26, 36, 45, 0.6) !important; color: #cbd5e0 !important; font-size: 6.8pt !important; border-radius: 4px !important; margin-bottom: 2px !important; border: none !important; }
    .cat-button > div > button { background-color: rgba(240, 90, 34, 0.08) !important; color: #fff !important; height: 38px !important; font-size: 8pt !important; border-bottom: 1px solid #f05a22 !important; }
    .stButton > button[kind="primary"] { background-color: rgba(240, 90, 34, 0.15) !important; color: #f05a22 !important; border-left: 4px solid #f05a22 !important; }
    
    .card-principal { background-color: #161f27; padding: 20px; border-radius: 12px; border-bottom: 4px solid #f05a22; text-align: center; margin-top: 10px; }
    
    /* GRID FLEXÍVEL QUE NÃO QUEBRA */
    .stats-wrapper {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 10px;
        margin-top: 20px;
    }
    
    .mini-card { 
        background-color: #111a21; padding: 15px 5px; border-radius: 8px; border: 1px solid #2d3748; text-align: center;
    }
    .mini-label { color: #8a99a8 !important; font-size: 7.5px !important; font-weight: 800; text-transform: uppercase; margin-bottom: 5px; display: block; }
    .mini-val { color: #00ffc3 !important; font-weight: 900; font-size: 18px !important; margin: 0; }
    </style>
""", unsafe_allow_html=True)

# --- 4. ENGINE ---
def simular_probabilidades(casa, fora):
    seed = int(hashlib.sha256((casa + fora).encode()).hexdigest(), 16) % 100
    pc = 35 + (seed % 30); pe = 15 + (seed % 15); pf = 100 - pc - pe
    return pc, pe, pf, 50+(seed%40), 60+(seed%35), 65+(seed%30)

# --- 5. NAVEGAÇÃO SIDEBAR ---
if 'liga_ativa' not in st.session_state: st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A')
if 'menu_aberto' not in st.session_state: st.session_state.menu_aberto = None

with st.sidebar:
    def s_btn(display, full, vid):
        if st.button(display, key=f"s_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid; st.session_state.nome_liga = full; st.rerun()

    def cat_btn(label, menu_id):
        st.markdown('<div class="cat-button">', unsafe_allow_html=True)
        if st.button(label, key=f"cat_{menu_id}"):
            st.session_state.menu_aberto = menu_id if st.session_state.menu_aberto != menu_id else None; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # CATEGORIA BRASIL (RESTAURADA E COMPLETA)
    cat_btn("🇧🇷 BRASIL COMPLETO", "BR")
    if st.session_state.menu_aberto == "BR":
        st.markdown('<p style="font-size:8px; color:#5a6b79; margin:5px 0;">NACIONAIS</p>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: s_btn("SÉRIE A", "BRASILEIRÃO A", "BRA_A"); s_btn("SÉRIE C", "BRASILEIRÃO C", "BRA_C")
        with c2: s_btn("SÉRIE B", "BRASILEIRÃO B", "BRA_B"); s_btn("SÉRIE D", "BRASILEIRÃO D", "BRA_D")
        
        st.markdown('<p style="font-size:8px; color:#5a6b79; margin:5px 0;">COPAS</p>', unsafe_allow_html=True)
        c3, c4 = st.columns(2)
        with c3: s_btn("COPA BR", "COPA DO BRASIL", "CDB"); s_btn("SUPERCOPA", "SUPERCOPA DO BR", "SUPER")
        with c4: s_btn("NORDESTE", "COPA DO NORDESTE", "CNE")
        
        st.markdown('<p style="font-size:8px; color:#5a6b79; margin:5px 0;">ESTADUAIS</p>', unsafe_allow_html=True)
        c5, c6 = st.columns(2)
        with c5: s_btn("PAULISTÃO", "PAULISTÃO", "SP"); s_btn("MINEIRO", "CAMPEONATO MINEIRO", "MG")
        with c6: s_btn("CARIOCA", "CAMPEONATO CARIOCA", "RJ"); s_btn("GAÚCHO", "CAMPEONATO GAÚCHO", "RS")

    cat_btn("🇪🇺 ELITE EUROPA", "EU")
    if st.session_state.menu_aberto == "EU":
        s_btn("🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER LEAGUE", "PREMIER LEAGUE", "ENG_P")
        s_btn("🇪🇸 LA LIGA", "LA LIGA", "ESP_L")
        s_btn("⭐ CHAMPIONS LEAGUE", "CHAMPIONS LEAGUE", "UCL")

    cat_btn("🔥 AMÉRICA DO SUL", "SAM")
    if st.session_state.menu_aberto == "SAM":
        s_btn("🏆 LIBERTADORES", "LIBERTADORES", "LIB")

# --- 6. CABEÇALHO ---
st.markdown("""
    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
        <div style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;">
            <svg style="width: 100%; height: 100%; fill: none; stroke: #f05a22; stroke-width: 4;" viewBox="0 0 100 100">
                <path d="M50 5 L90 25 L90 75 L50 95 L10 75 L10 25 Z" />
            </svg>
        </div>
        <div style="color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 19px; font-weight: 900;">
            GESTOR IA <span style="color: #ffffff; font-size: 10px; margin-left: 5px;">GLOBAL EDITION</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# SELEÇÃO
times_lista = DIC_TIMES.get(st.session_state.liga_ativa, ["Selecione..."])
col1, col2, col3 = st.columns([3, 3, 2.5])
with col1: t_casa = st.selectbox("Mandante", sorted(times_lista), label_visibility="collapsed", key="casa")
with col2: t_fora = st.selectbox("Visitante", sorted([t for t in times_lista if t != t_casa]), label_visibility="collapsed", key="fora")
with col3: executar = st.button("🔥 PROCESSAR ALGORITMO", use_container_width=True, type="primary")

if executar:
    pc, pe, pf, mg, mc, mch = simular_probabilidades(t_casa, t_fora)
    st.markdown(f'<div style="font-size:10px; color:#f05a22; font-family:Orbitron; border-left:3px solid #f05a22; padding-left:10px;">📡 ANALISANDO: {st.session_state.nome_liga}</div>', unsafe_allow_html=True)
    
    # RESULTADO PRINCIPAL
    st.markdown(f"""
        <div class="card-principal">
            <div style="color: #fff; font-family: Orbitron; font-size: 20px; font-weight: 800; margin-bottom: 20px;">{t_casa.upper()} vs {t_fora.upper()}</div>
            <div style="display: flex; justify-content: space-around;">
                <div><p style="color:#f05a22; font-size:28px; font-weight:900; margin:0;">{pc}%</p><p style="color:#8a99a8; font-size:9px;">CASA</p></div>
                <div><p style="color:#fff; font-size:28px; font-weight:900; margin:0;">{pe}%</p><p style="color:#8a99a8; font-size:9px;">EMPATE</p></div>
                <div><p style="color:#f05a22; font-size:28px; font-weight:900; margin:0;">{pf}%</p><p style="color:#8a99a8; font-size:9px;">FORA</p></div>
            </div>
        </div>
        
        <div class="stats-wrapper">
            <div class="mini-card"><span class="mini-label">⚽ GOLS +2.5</span><p class="mini-val">{mg}%</p></div>
            <div class="mini-card"><span class="mini-label">🚩 CANTOS +9.5</span><p class="mini-val">{mc}%</p></div>
            <div class="mini-card"><span class="mini-label">👞 CHUTES +22</span><p class="mini-val">{mch}%</p></div>
            <div class="mini-card"><span class="mini-label">🎯 NO GOL +8</span><p class="mini-val">{mg-5}%</p></div>
            <div class="mini-card"><span class="mini-label">⚠️ FALTAS +24</span><p class="mini-val">{mc+10}%</p></div>
            <div class="mini-card"><span class="mini-label">🟨 CARTÕES +4</span><p class="mini-val">{pe+20}%</p></div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<div style='height:200px; display:flex; align-items:center; justify-content:center; color:#2d3748; font-family:Orbitron; font-size:10px;'>AGUARDANDO SELEÇÃO...</div>", unsafe_allow_html=True)
