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

# --- 2. BANCO DE DADOS ---
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

# --- 3. CSS REVISADO (FOCO EM ALINHAMENTO E TAMANHO UNIFORME) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    header[data-testid="stHeader"] { background: transparent !important; }
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    [data-testid="stSidebar"] { 
        background-color: #0b1218 !important; 
        border-right: 2px solid #f05a22 !important; 
        min-width: 280px !important; 
    }

    /* ESTILO DOS BOTÕES DAS LIGAS (SUB-BOTÕES) */
    .stButton > button { 
        background: linear-gradient(90deg, rgba(240, 90, 34, 0.1) 0%, rgba(26, 36, 45, 0.8) 100%) !important;
        color: #cbd5e0 !important; 
        font-size: 8.5px !important; 
        font-weight: 700 !important;
        border-radius: 30px !important; 
        border: 1px solid rgba(240, 90, 34, 0.2) !important; 
        height: 35px !important; 
        
        /* AQUI ESTÁ O SEGREDO DO TAMANHO IGUAL E TEXTO CENTRALIZADO */
        width: 100% !important;        /* Força a preencher a coluna inteira */
        display: flex !important;
        justify-content: center !important; /* Centraliza horizontalmente */
        align-items: center !important;     /* Centraliza verticalmente */
        text-align: center !important;
        padding: 0px !important;
        white-space: nowrap !important;
        margin-bottom: 2px !important;
    }

    .stButton > button:hover { 
        background: linear-gradient(90deg, #f05a22 0%, rgba(240, 90, 34, 0.3) 100%) !important;
        color: #ffffff !important; 
        border: 1px solid #f05a22 !important;
        box-shadow: 0 0 10px rgba(240, 90, 34, 0.3) !important;
    }

    /* BOTÃO ATIVO (COR LARANJA) */
    .stButton > button[kind="primary"] { 
        background: linear-gradient(90deg, #f05a22 0%, #ff8c00 100%) !important;
        color: #ffffff !important; 
        border: 1px solid #ffffff !important;
    }

    /* BOTÃO CATEGORIA (MÃE) */
    .cat-button > div > button { 
        background: rgba(240, 90, 34, 0.05) !important; 
        border-radius: 8px !important;
        height: 40px !important;
        border-bottom: 2px solid #f05a22 !important;
        justify-content: flex-start !important; /* Categoria alinha à esquerda */
        padding-left: 15px !important;
        font-family: 'Orbitron' !important;
        font-size: 11px !important;
        color: #f05a22 !important;
    }

    /* Ajuste para as colunas da sidebar não terem espaços diferentes */
    [data-testid="column"] {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. ENGINE DE CÁLCULO ---
def calcular_engine(casa, fora):
    seed = int(hashlib.sha256((casa + fora).encode()).hexdigest(), 16) % 100
    pc = 35 + (seed % 30); pe = 15 + (seed % 15); pf = 100 - pc - pe
    return pc, pe, pf, 50+(seed%40), 60+(seed%35), 65+(seed%30)

# --- 5. NAVEGAÇÃO E SIDEBAR ---
if 'liga_ativa' not in st.session_state: st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A')
if 'menu_aberto' not in st.session_state: st.session_state.menu_aberto = 'BR'

with st.sidebar:
    # Logo / Título
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 25px; padding-left: 10px;">
            <div style="background: #f05a22; width: 30px; height: 30px; clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);"></div>
            <div style="font-family: 'Orbitron'; color: #f05a22; font-size: 18px; font-weight: 900;">GESTOR IA</div>
        </div>
    """, unsafe_allow_html=True)

    def s_btn(icon, display, full, vid):
        label = f"{icon} {display}"
        if st.button(label, key=f"s_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid; st.session_state.nome_liga = full; st.rerun()

    def cat_btn(label, menu_id):
        st.markdown('<div class="cat-button">', unsafe_allow_html=True)
        if st.button(label, key=f"cat_{menu_id}"):
            st.session_state.menu_aberto = menu_id if st.session_state.menu_aberto != menu_id else None; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # Menu Brasil
    cat_btn("📁 FUTEBOL BRASIL", "BR")
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

    # Menu Europa
    cat_btn("🌍 ELITE EUROPA", "EU_L")
    if st.session_state.menu_aberto == "EU_L":
        c1, c2 = st.columns(2)
        with c1: 
            s_btn("🏴󠁧󠁢󠁥󠁮󠁧󠁿", "PREMIER", "PREMIER LEAGUE", "ENG_P")
            s_btn("🇮🇹", "SERIE A", "SERIE A TIM", "ITA_A")
        with c2: 
            s_btn("🇪🇸", "LA LIGA", "LA LIGA", "ESP_L")
            s_btn("🇩🇪", "BUNDES", "BUNDESLIGA", "GER_B")

# --- 6. CABEÇALHO E SELEÇÃO ---
st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <div style="color: #f05a22; font-family: 'Orbitron'; font-size: 11px; border-left: 3px solid #f05a22; padding-left: 10px;">
            ANALISANDO: {st.session_state.nome_liga}
        </div>
    </div>
""", unsafe_allow_html=True)

times_lista = DIC_TIMES.get(st.session_state.liga_ativa, ["Selecione..."])
col1, col2, col3 = st.columns([3, 3, 2.5])
with col1: t_casa = st.selectbox("Mandante", sorted(times_lista), label_visibility="collapsed")
with col2: t_fora = st.selectbox("Visitante", sorted([t for t in times_lista if t != t_casa]), label_visibility="collapsed")
with col3: executar = st.button("🔥 PROCESSAR ALGORITMO", use_container_width=True, type="primary")

# --- 7. RESULTADOS ---
if executar:
    pc, pe, pf, mg, mc, mch = calcular_engine(t_casa, t_fora)
    
    st.markdown(f"""
        <div style="background: #161f27; padding: 30px; border-radius: 12px; border-bottom: 4px solid #f05a22; text-align: center; margin-top: 20px;">
            <div style="color: #fff; font-family: Orbitron; font-size: 22px; font-weight: 800; margin-bottom: 30px; letter-spacing: 2px;">
                {t_casa.upper()} <span style="color:#f05a22">VS</span> {t_fora.upper()}
            </div>
            <div style="display: flex; justify-content: space-around; align-items: center;">
                <div>
                    <div style="color:#f05a22; font-size:40px; font-weight:900; font-family:Orbitron;">{pc}%</div>
                    <div style="color:#8a99a8; font-size:12px; font-weight:800; margin-top:5px;">VITÓRIA CASA</div>
                </div>
                <div style="border-left: 1px solid #2d3748; border-right: 1px solid #2d3748; padding: 0 40px;">
                    <div style="color:#fff; font-size:35px; font-weight:900; font-family:Orbitron; opacity:0.8;">{pe}%</div>
                    <div style="color:#8a99a8; font-size:12px; font-weight:800; margin-top:5px;">EMPATE</div>
                </div>
                <div>
                    <div style="color:#f05a22; font-size:40px; font-weight:900; font-family:Orbitron;">{pf}%</div>
                    <div style="color:#8a99a8; font-size:12px; font-weight:800; margin-top:5px;">VITÓRIA FORA</div>
                </div>
            </div>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; margin-top: 20px;">
            <div style="background:#111a21; padding:15px; border-radius:10px; border:1px solid #2d3748; text-align:center;">
                <div style="color:#fff; font-size:9px; font-weight:800; margin-bottom:8px;">⚽ GOLS +2.5</div>
                <div style="color:#00ffc3; font-size:22px; font-weight:900; font-family:Orbitron;">{mg}%</div>
            </div>
            <div style="background:#111a21; padding:15px; border-radius:10px; border:1px solid #2d3748; text-align:center;">
                <div style="color:#fff; font-size:9px; font-weight:800; margin-bottom:8px;">🚩 CANTOS +9.5</div>
                <div style="color:#00ffc3; font-size:22px; font-weight:900; font-family:Orbitron;">{mc}%</div>
            </div>
            <div style="background:#111a21; padding:15px; border-radius:10px; border:1px solid #2d3748; text-align:center;">
                <div style="color:#fff; font-size:9px; font-weight:800; margin-bottom:8px;">👞 CHUTES +22</div>
                <div style="color:#00ffc3; font-size:22px; font-weight:900; font-family:Orbitron;">{mch}%</div>
            </div>
            <div style="background:#111a21; padding:15px; border-radius:10px; border:1px solid #2d3748; text-align:center;">
                <div style="color:#fff; font-size:9px; font-weight:800; margin-bottom:8px;">🎯 NO GOL +8</div>
                <div style="color:#00ffc3; font-size:22px; font-weight:900; font-family:Orbitron;">{mg-5}%</div>
            </div>
            <div style="background:#111a21; padding:15px; border-radius:10px; border:1px solid #2d3748; text-align:center;">
                <div style="color:#fff; font-size:9px; font-weight:800; margin-bottom:8px;">⚠️ FALTAS +24</div>
                <div style="color:#00ffc3; font-size:22px; font-weight:900; font-family:Orbitron;">{mc+10}%</div>
            </div>
            <div style="background:#111a21; padding:15px; border-radius:10px; border:1px solid #2d3748; text-align:center;">
                <div style="color:#fff; font-size:9px; font-weight:800; margin-bottom:8px;">🟨 CARTÕES +4</div>
                <div style="color:#00ffc3; font-size:22px; font-weight:900; font-family:Orbitron;">{pe+20}%</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<div style='height:200px; display:flex; align-items:center; justify-content:center; color:#2d3748; font-family:Orbitron; font-size:12px; opacity:0.6; letter-spacing:3px;'>SELECIONE UM CONFRONTO...</div>", unsafe_allow_html=True)
