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
    "CNE": ["Bahia", "Fortaleza", "Sport", "Ceará", "Vitória", "CRB", "Náutico", "Sampaio Corrêa"],
    "ENG_P": ["Man. City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Man. United", "Newcastle"],
    "ESP_L": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Athletic Bilbao", "Real Sociedad", "Sevilla"],
    "ITA_A": ["Inter de Milão", "Milan", "Juventus", "Atalanta", "Roma", "Napoli", "Lazio", "Bologna"],
    "GER_B": ["Bayer Leverkusen", "Bayern de Munique", "Stuttgart", "RB Leipzig", "Borussia Dortmund", "Eintracht Frankfurt"],
    "FRA_L": ["PSG", "Monaco", "Lille", "Brest", "Nice", "Lyon", "Marseille"],
    "UCL": ["Real Madrid", "Man. City", "Bayern", "Arsenal", "Barcelona", "Inter", "PSG", "Bayer Leverkusen"],
    "EURO_C": ["Espanha", "Inglaterra", "França", "Alemanha", "Portugal", "Itália", "Holanda"],
    "SAUDI": ["Al-Hilal", "Al-Nassr", "Al-Ittihad", "Al-Ahli", "Al-Ettifaq"],
    "USA_MLS": ["Inter Miami", "LA Galaxy", "Columbus Crew", "LAFC", "Cincinnati"],
    "LIB": ["Flamengo", "Palmeiras", "River Plate", "Botafogo", "São Paulo", "Atlético-MG"],
    "SUL": ["Cruzeiro", "Corinthians", "Fortaleza", "Racing", "Lanús", "Athletico-PR"]
}

# --- 3. CSS "ICON-BUTTON" RESTAURADO E MELHORADO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    header[data-testid="stHeader"] { background: transparent !important; }
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    [data-testid="stSidebar"] { 
        background-color: #0b1218 !important; 
        border-right: 2px solid #f05a22 !important; 
    }

    /* BOTÕES DAS LIGAS (PILL STYLE) */
    .stButton > button { 
        background: linear-gradient(90deg, rgba(240, 90, 34, 0.1) 0%, rgba(26, 36, 45, 0.8) 20%) !important;
        color: #cbd5e0 !important; 
        font-size: 10px !important; /* Tamanho fixo para caber o texto */
        border-radius: 30px !important; 
        margin-bottom: 4px !important; 
        border: 1px solid rgba(240, 90, 34, 0.2) !important; 
        height: 35px !important; 
        transition: all 0.3s ease !important;
        white-space: nowrap !important;
        text-align: left !important;
        padding-left: 15px !important;
        width: 100% !important;
        display: block !important;
    }

    .stButton > button:hover { 
        background: linear-gradient(90deg, #f05a22 0%, rgba(240, 90, 34, 0.3) 100%) !important;
        color: #ffffff !important; 
        border: 1px solid #f05a22 !important;
        transform: translateX(5px);
    }

    /* BOTÃO ATIVO */
    .stButton > button[kind="primary"] { 
        background: linear-gradient(90deg, #f05a22 0%, #ff8c00 100%) !important;
        color: #ffffff !important; 
        font-weight: 800 !important;
        box-shadow: 0 0 15px rgba(240, 90, 34, 0.4) !important;
    }

    /* ESTILO DAS CATEGORIAS */
    .cat-button > div > button { 
        background: rgba(240, 90, 34, 0.05) !important; 
        border-radius: 8px !important;
        height: 40px !important;
        border: none !important;
        border-bottom: 2px solid #f05a22 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 12px !important;
        color: #fff !important;
    }

    /* RESULTADOS VISUAIS */
    .card-principal { background-color: #161f27; padding: 20px; border-radius: 12px; border-bottom: 4px solid #f05a22; text-align: center; margin-top: 20px;}
    .stats-flex { display: flex; justify-content: space-between; gap: 10px; margin-top: 25px; width: 100%; flex-wrap: nowrap !important; }
    .mini-card { flex: 1; background-color: #111a21; padding: 15px 5px; border-radius: 10px; border: 1px solid #2d3748; text-align: center; min-width: 0; }
    .mini-label { color: #ffffff !important; font-size: 9px !important; font-weight: 800; text-transform: uppercase; margin-bottom: 8px; display: block; }
    .mini-val { color: #00ffc3 !important; font-weight: 900; font-size: 20px !important; margin: 0; text-shadow: 0 0 10px rgba(0, 255, 195, 0.4); }
    </style>
""", unsafe_allow_html=True)

# --- 4. ENGINE DE CÁLCULO ---
def calcular_engine(casa, fora):
    seed = int(hashlib.sha256((casa + fora).encode()).hexdigest(), 16) % 100
    pc = 35 + (seed % 30); pe = 15 + (seed % 15); pf = 100 - pc - pe
    return pc, pe, pf, 50+(seed%40), 60+(seed%35), 65+(seed%30)

# --- 5. NAVEGAÇÃO SIDEBAR ---
if 'liga_ativa' not in st.session_state: st.session_state.update(liga_ativa='BRA_A', nome_liga='BRASILEIRÃO A')
if 'menu_aberto' not in st.session_state: st.session_state.menu_aberto = 'BR'

with st.sidebar:
    st.markdown('<h2 style="color:#f05a22; font-family:Orbitron; font-size:18px; text-align:center; margin-bottom:20px;">MENU GESTOR</h2>', unsafe_allow_html=True)

    def s_btn(icon, display, full, vid):
        label = f"{icon}  {display}"
        if st.button(label, key=f"s_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid; st.session_state.nome_liga = full; st.rerun()

    # CATEGORIA BRASIL
    st.markdown('<div class="cat-button">', unsafe_allow_html=True)
    if st.button("📂 FUTEBOL BRASIL", key="cat_br"):
        st.session_state.menu_aberto = "BR"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.session_state.menu_aberto == "BR":
        c1, c2 = st.columns(2)
        with c1:
            s_btn("🔘", "SÉRIE A", "BRASILEIRÃO A", "BRA_A")
            s_btn("🔘", "SÉRIE C", "BRASILEIRÃO C", "BRA_C")
            s_btn("🏆", "COPA BR", "COPA DO BRASIL", "CDB")
        with c2:
            s_btn("🔘", "SÉRIE B", "BRASILEIRÃO B", "BRA_B")
            s_btn("🔘", "SÉRIE D", "BRASILEIRÃO D", "BRA_D")
            s_btn("☀️", "NORDESTE", "COPA NORDESTE", "CNE")

    # CATEGORIA EUROPA
    st.markdown('<div class="cat-button">', unsafe_allow_html=True)
    if st.button("🌍 ELITE EUROPA", key="cat_eu"):
        st.session_state.menu_aberto = "EU_L"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.menu_aberto == "EU_L":
        c1, c2 = st.columns(2)
        with c1:
            s_btn("🏴󠁧󠁢󠁥󠁮󠁧󠁿", "PREMIER", "PREMIER LEAGUE", "ENG_P")
            s_btn("🇮🇹", "SERIE A", "SERIE A TIM", "ITA_A")
            s_btn("🇫🇷", "LIGUE 1", "LIGUE 1", "FRA_L")
        with c2:
            s_btn("🇪🇸", "LA LIGA", "LA LIGA", "ESP_L")
            s_btn("🇩🇪", "BUNDES", "BUNDESLIGA", "GER_B")

    # CATEGORIA INTERNACIONAIS
    st.markdown('<div class="cat-button">', unsafe_allow_html=True)
    if st.button("⭐ UEFA / INTER", key="cat_int"):
        st.session_state.menu_aberto = "UEFA"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.menu_aberto == "UEFA":
        s_btn("🏆", "CHAMPIONS", "CHAMPIONS LEAGUE", "UCL")
        s_btn("🛡️", "EUROCOPA", "EUROCOPA", "EURO_C")

# --- 6. ÁREA DE PROCESSAMENTO ---
st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
        <div style="color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 20px; font-weight: 900;">
            GESTOR IA <span style="color: #ffffff; font-size: 10px; margin-left: 5px; opacity: 0.6;">PRO EDITION</span>
        </div>
    </div>
""", unsafe_allow_html=True)

times_lista = DIC_TIMES.get(st.session_state.liga_ativa, ["Selecione..."])
col1, col2, col3 = st.columns([3, 3, 2.5])

with col1: 
    st.markdown('<p style="font-size:11px; color:rgba(255,255,255,0.3); margin-bottom:5px;">MANDANTE</p>', unsafe_allow_html=True)
    t_casa = st.selectbox("Mandante", sorted(times_lista), label_visibility="collapsed")
with col2: 
    st.markdown('<p style="font-size:11px; color:rgba(255,255,255,0.3); margin-bottom:5px;">VISITANTE</p>', unsafe_allow_html=True)
    t_fora = st.selectbox("Visitante", sorted([t for t in times_lista if t != t_casa]), label_visibility="collapsed")
with col3: 
    st.markdown('<br>', unsafe_allow_html=True)
    executar = st.button("🔥 PROCESSAR ALGORITMO", use_container_width=True, type="primary")

# --- 7. EXIBIÇÃO DOS RESULTADOS ---
if executar:
    pc, pe, pf, mg, mc, mch = calcular_engine(t_casa, t_fora)
    
    st.markdown(f'<div style="font-size:11px; color:#f05a22; font-family:Orbitron; border-left:4px solid #f05a22; padding-left:10px; margin-top:20px;">📡 ANALISANDO: {st.session_state.nome_liga}</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="card-principal">
            <div style="color: #fff; font-family: Orbitron; font-size: 22px; font-weight: 800; margin-bottom: 25px;">{t_casa.upper()} <span style="color:#f05a22">vs</span> {t_fora.upper()}</div>
            <div style="display: flex; justify-content: space-around;">
                <div><p style="color:#f05a22; font-size:32px; font-weight:900; margin:0;">{pc}%</p><p style="color:#8a99a8; font-size:10px; font-weight:800;">VITÓRIA CASA</p></div>
                <div><p style="color:#fff; font-size:32px; font-weight:900; margin:0;">{pe}%</p><p style="color:#8a99a8; font-size:10px; font-weight:800;">EMPATE</p></div>
                <div><p style="color:#f05a22; font-size:32px; font-weight:900; margin:0;">{pf}%</p><p style="color:#8a99a8; font-size:10px; font-weight:800;">VITÓRIA FORA</p></div>
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
    st.markdown("<div style='height:200px; display:flex; align-items:center; justify-content:center; color:#2d3748; font-family:Orbitron; font-size:12px; opacity:0.6;'>SELECIONE UM CONFRONTO...</div>", unsafe_allow_html=True)
