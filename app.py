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

# --- 3. CSS "SEGURANÇA" (AJUSTE DE LARGURA DA SIDEBAR E BOTÕES UNIFORMES) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    /* 1. MOVER A LINHA DIVISORA PARA A DIREITA (GANHAR ESPAÇO) */
    [data-testid="stSidebar"] { 
        min-width: 350px !important; 
        max-width: 350px !important; 
        background-color: #0b1218 !important; 
        border-right: 2px solid #f05a22 !important; 
    }

    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    /* 2. BOTÕES DE LIGAS (SUB-BOTÕES) TOTALMENTE IGUAIS E CENTRALIZADOS */
    .stButton > button { 
        background: linear-gradient(90deg, rgba(240, 90, 34, 0.1) 0%, rgba(26, 36, 45, 0.8) 100%) !important;
        color: #cbd5e0 !important; 
        font-size: 10px !important; 
        font-weight: 700 !important;
        border-radius: 30px !important; 
        border: 1px solid rgba(240, 90, 34, 0.2) !important; 
        
        /* TRAVAR O TAMANHO */
        height: 42px !important; 
        width: 100% !important; 
        
        /* CENTRALIZAR TEXTO */
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        text-align: center !important;
        padding: 0px 10px !important;
        
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover { 
        background: #f05a22 !important;
        color: #ffffff !important; 
        border: 1px solid #ffffff !important;
        transform: translateY(-2px);
    }

    /* BOTÃO ATIVO */
    .stButton > button[kind="primary"] { 
        background: linear-gradient(90deg, #f05a22 0%, #ff8c00 100%) !important;
        color: #ffffff !important; 
        border: 1px solid #ffffff !important;
        box-shadow: 0 0 15px rgba(240, 90, 34, 0.4) !important;
    }

    /* BOTÃO MÃE (CATEGORIA) */
    .cat-button > div > button { 
        background: rgba(240, 90, 34, 0.05) !important; 
        border-radius: 8px !important;
        height: 45px !important;
        border-bottom: 2px solid #f05a22 !important;
        justify-content: flex-start !important;
        padding-left: 15px !important;
        font-family: 'Orbitron' !important;
        font-size: 12px !important;
        color: #f05a22 !important;
    }

    /* Ajuste de colunas na sidebar */
    [data-testid="column"] { padding: 0 5px !important; }
    </style>
""", unsafe_allow_html=True)

# --- 4. ENGINE ---
def calcular_engine(casa, fora):
    seed = int(hashlib.sha256((casa + fora).encode()).hexdigest(), 16) % 100
    pc = 35 + (seed % 30); pe = 15 + (seed % 15); pf = 100 - pc - pe
    return pc, pe, pf, 50+(seed%40), 60+(seed%35), 65+(seed%30)

# --- 5. NAVEGAÇÃO SIDEBAR ---
if 'liga_ativa' not in st.session_state: st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A')
if 'menu_aberto' not in st.session_state: st.session_state.menu_aberto = 'BR'

with st.sidebar:
    st.markdown("""
        <div style="text-align:center; margin-bottom:20px;">
            <span style="font-family:'Orbitron'; color:#f05a22; font-size:22px; font-weight:900;">GESTOR IA</span>
            <hr style="border-color: rgba(240, 90, 34, 0.3);">
        </div>
    """, unsafe_allow_html=True)

    # REMOVI O PARÂMETRO "ICON" DA FUNÇÃO PARA LIMPAR O BOTÃO
    def s_btn(display, full, vid):
        if st.button(display, key=f"s_{vid}", type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid; st.session_state.nome_liga = full; st.rerun()

    def cat_btn(label, menu_id):
        st.markdown('<div class="cat-button">', unsafe_allow_html=True)
        if st.button(label, key=f"cat_{menu_id}"):
            st.session_state.menu_aberto = menu_id if st.session_state.menu_aberto != menu_id else None; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    cat_btn("📁 FUTEBOL BRASIL", "BR")
    if st.session_state.menu_aberto == "BR":
        c1, c2 = st.columns(2)
        with c1: 
            s_btn("SÉRIE A", "BRASILEIRÃO A", "BRA_A")
            s_btn("SÉRIE C", "BRASILEIRÃO C", "BRA_C")
            s_btn("COPA BR", "COPA DO BRASIL", "CDB")
        with c2: 
            s_btn("SÉRIE B", "BRASILEIRÃO B", "BRA_B")
            s_btn("SÉRIE D", "BRASILEIRÃO D", "BRA_D")
            s_btn("NORDESTE", "COPA NORDESTE", "CNE")

    cat_btn("🌍 ELITE EUROPA", "EU_L")
    if st.session_state.menu_aberto == "EU_L":
        c1, c2 = st.columns(2)
        with c1: 
            s_btn("PREMIER", "PREMIER LEAGUE", "ENG_P")
            s_btn("SERIE A", "SERIE A TIM", "ITA_A")
        with c2: 
            s_btn("LA LIGA", "LA LIGA", "ESP_L")
            s_btn("BUNDES", "BUNDESLIGA", "GER_B")

# --- 6. ÁREA DE TRABALHO ---
st.markdown(f"""
    <div style="border-left: 4px solid #f05a22; padding-left: 15px; margin-bottom: 20px;">
        <span style="color: #f05a22; font-family: 'Orbitron'; font-size: 12px;">MODO DE ANÁLISE ATIVO</span><br>
        <span style="color: #fff; font-family: 'Orbitron'; font-size: 18px; font-weight: 800;">{st.session_state.nome_liga}</span>
    </div>
""", unsafe_allow_html=True)

times_lista = DIC_TIMES.get(st.session_state.liga_ativa, ["Selecione..."])
col1, col2, col3 = st.columns([3, 3, 2.5])
with col1: t_casa = st.selectbox("Mandante", sorted(times_lista), label_visibility="collapsed")
with col2: t_fora = st.selectbox("Visitante", sorted([t for t in times_lista if t != t_casa]), label_visibility="collapsed")
with col3: executar = st.button("🔥 PROCESSAR ALGORITMO", use_container_width=True, type="primary")

if executar:
    pc, pe, pf, mg, mc, mch = calcular_engine(t_casa, t_fora)
    st.markdown(f"""
        <div style="background: #161f27; padding: 25px; border-radius: 12px; border-bottom: 4px solid #f05a22; text-align: center;">
            <div style="color: #fff; font-family: Orbitron; font-size: 20px; font-weight: 800; margin-bottom: 20px;">{t_casa.upper()} vs {t_fora.upper()}</div>
            <div style="display: flex; justify-content: space-around;">
                <div><p style="color:#f05a22; font-size:32px; font-weight:900; margin:0;">{pc}%</p><p style="color:#8a99a8; font-size:10px; font-weight:800;">VITÓRIA CASA</p></div>
                <div><p style="color:#fff; font-size:32px; font-weight:900; margin:0;">{pe}%</p><p style="color:#8a99a8; font-size:10px; font-weight:800;">EMPATE</p></div>
                <div><p style="color:#f05a22; font-size:32px; font-weight:900; margin:0;">{pf}%</p><p style="color:#8a99a8; font-size:10px; font-weight:800;">VITÓRIA FORA</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
