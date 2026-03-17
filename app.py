import streamlit as st
import time
import random
from datetime import datetime

# ==============================================================================
# [GIAE KERNEL SHIELD v56.2 - PERSISTENCE LOCK & UI SYNC]
# FIX: NESTED BUTTON LOGIC | CALC STABILITY | JARVIS THEME ALERTS
# ==============================================================================

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CONTROLE DE NAVEGAÇÃO E ESTADO DO SISTEMA ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"
if 'analise_travada' not in st.session_state:
    st.session_state.analise_travada = False
if 'banca_atual' not in st.session_state:
    st.session_state.banca_atual = 1000.0
if 'historico_calls' not in st.session_state:
    st.session_state.historico_calls = []
if 'dados_da_analise' not in st.session_state:
    st.session_state.dados_da_analise = {}

# --- [LOCK] BLOCO DE SEGURANÇA CSS (ESTRUTURA COMPLETA RESTAURADA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');

    /* [01] RESET E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; visibility: hidden !important; }
    .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    [data-testid="stMainBlockContainer"] { padding-top: 0rem !important; padding-bottom: 1rem !important; }

    /* [02] SIDEBAR LOCK (320PX) */
    [data-testid="stSidebar"] { 
        min-width: 320px !important; max-width: 320px !important; width: 320px !important;
        background-color: #11151a !important; border-right: 1px solid #1e293b !important; 
    }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebarContent"]::-webkit-scrollbar { display: none !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }

    /* [03] NAVBAR SUPERIOR AZUL ROYAL + LOGO + LUPA + BOTÕES */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #002366 !important; border-bottom: 1px solid rgba(255,255,255,0.1) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 30px !important; z-index: 999999; 
    }
    .header-left { display: flex; align-items: center; }
    
    .logo-link { 
        color: #9d54ff !important; font-weight: 900; font-size: 20px !important; 
        text-transform: uppercase; letter-spacing: 1px; margin-right: 60px; 
        text-decoration: none !important; cursor: pointer !important; transition: 0.3s;
    }
    .logo-link:hover { text-shadow: 0 0 15px #9d54ff; filter: brightness(1.2); }

    .nav-items { display: flex; gap: 15px; }
    .nav-items span { color: #ffffff; font-size: 10px !important; text-transform: uppercase; cursor: pointer; white-space: nowrap; transition: 0.2s; opacity: 0.8; }
    .nav-items span:hover { color: #9d54ff; opacity: 1; }

    .header-right { display: flex; align-items: center; gap: 15px; min-width: 280px; justify-content: flex-end; }
    .search-icon { color: #ffffff !important; cursor: pointer !important; font-size: 16px !important; transition: 0.3s !important; margin-right: 10px; }
    .search-icon:hover { color: #9d54ff !important; transform: scale(1.2); }
    
    .registrar-pill { 
        color: #ffffff !important; font-size: 10px !important; font-weight: 700 !important; border: 1px solid #ffffff !important; 
        padding: 6px 15px !important; border-radius: 20px !important; cursor: pointer !important; transition: 0.3s; white-space: nowrap;
        text-decoration: none !important; display: inline-block;
    }
    .registrar-pill:hover { background: #ffffff !important; color: #002366 !important; }

    .entrar-grad { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: white !important; padding: 7px 20px !important; border-radius: 4px !important; 
        font-weight: 800 !important; font-size: 10px !important; cursor: pointer !important; transition: 0.3s; white-space: nowrap;
    }
    .entrar-grad:hover { filter: brightness(1.2) !important; box-shadow: 0 0 15px rgba(109, 40, 217, 0.4); }

    /* [04] SIDEBAR BOTÕES (UMA LINHA SÓ) */
    [data-testid="stSidebar"] button {
        background-color: transparent !important; color: #94a3b8 !important; border: none !important;
        border-bottom: 1px solid #1a202c !important; border-radius: 0px !important;
        text-align: left !important; width: 100% !important; padding: 18px 25px !important; 
        font-size: 10px !important; text-transform: uppercase !important; 
        white-space: nowrap !important; overflow: hidden !important;
    }
    [data-testid="stSidebar"] button:hover { color: #ffffff !important; border-left: 4px solid #6d28d9 !important; background: rgba(26, 36, 45, 0.8) !important; }

    /* [05] CARDS & RESULTADOS */
    .news-ticker { background: rgba(0, 35, 102, 0.2); border: 1px solid #1e293b; padding: 10px; color: #06b6d4; font-size: 10px; font-weight: 700; text-transform: uppercase; margin-bottom: 15px; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; transition: 0.3s; }
    .highlight-card:hover { border-color: #6d28d9; transform: translateY(-3px); }
    
    .pulse-dot { height: 6px; width: 6px; background-color: #22c55e; border-radius: 50%; display: inline-block; margin-right: 5px; animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
    .conf-bar-bg { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 10px auto; overflow: hidden; }
    .conf-bar-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    /* [06] INPUTS DARK */
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div, div[data-baseweb="base-input"] {
        background-color: #11151a !important; color: white !important; border: 1px solid #1e293b !important;
    }
    .stSelectbox label p, .stNumberInput label p {
        color: #94a3b8 !important; font-size: 10px !important; text-transform: uppercase !important; font-weight: 700 !important;
    }

    /* [07] EFEITO PULSANTE BOTÃO EXECUTAR */
    [data-testid="stMainBlockContainer"] .stButton > button {
        background: linear-gradient(90deg, #6d28d9 0%, #4f46e5 100%) !important;
        color: white !important; border: none !important; font-weight: 900 !important;
        padding: 10px 25px !important; border-radius: 4px !important;
        transition: 0.4s all ease-in-out !important;
        animation: pulse-glow 2s infinite !important;
    }
    @keyframes pulse-glow {
        0% { box-shadow: 0 0 5px rgba(109, 40, 217, 0.4); }
        50% { box-shadow: 0 0 15px rgba(109, 40, 217, 0.7); }
        100% { box-shadow: 0 0 5px rgba(109, 40, 217, 0.4); }
    }

    /* FOOTER */
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DADOS HIERÁRQUICA (MASTER DATABASE v55.0) ---
DADOS_HIEARARQUIA = {
    "BRASIL": {
        "Nacional": {
            "Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo", "São Paulo", "Grêmio", "Atlético-MG", "Fluminense", "Internacional", "Corinthians", "Bahia", "Cruzeiro", "Vasco", "Athletico-PR", "Fortaleza", "Cuiabá", "Criciúma", "Juventude", "Vitória", "Bragantino", "Atlético-GO"],
            "Brasileirão Série B": ["Santos", "Sport", "Coritiba", "Goiás", "Ceará", "Novorizontino", "Vila Nova", "Amazonas", "Operário-PR", "Avaí", "Chapecoense", "Ponte Preta"],
            "Brasileirão Série C": ["Náutico", "Figueirense", "Remo", "CSA", "Volta Redonda", "Sampaio Corrêa", "ABC", "Botafogo-PB", "Londrina", "Ferroviário"],
            "Brasileirão Série D": ["Santa Cruz", "Inter de Limeira", "Anápolis", "Maringá", "Brasil de Pelotas", "Retrô", "Iguatu", "Treze", "América-RN"]
        },
        "Regionais (Estaduais)": {
            "Paulistão - A1": ["Palmeiras", "Santos", "São Paulo", "Corinthians", "Bragantino", "Ituano", "São Bernardo", "Ponte Preta", "Novorizontino"],
            "Paulistão - A2": ["Portuguesa", "Guarani", "São Bento", "XV de Piracicaba", "Taubaté"],
            "Carioca": ["Flamengo", "Fluminense", "Botafogo", "Vasco", "Nova Iguaçu", "Boavista", "Madureira", "Volta Redonda"],
            "Mineiro": ["Atlético-MG", "Cruzeiro", "América-MG", "Tombense", "Ipatinga", "Villa Nova"],
            "Gaúcho": ["Grêmio", "Internacional", "Juventude", "Caxias", "Brasil de Pelotas", "Ypiranga"],
            "Paranaense": ["Athletico-PR", "Coritiba", "Maringá", "Operário-PR", "Cianorte", "Londrina"],
            "Catarinense": ["Criciúma", "Avaí", "Figueirense", "Chapecoense", "Brusque", "Marcílio Dias"]
        },
        "Copas": {
            "Copa do Brasil": ["Vasco", "Flamengo", "São Paulo", "Palmeiras", "Juventude", "Athletico-PR", "Bahia", "Cruzeiro", "Corinthians", "Atlético-MG", "Fluminense"],
            "Copa do Nordeste": ["Fortaleza", "Bahia", "Ceará", "Sport", "Vitória", "CRB", "Náutico", "Sampaio Corrêa", "Treze", "ABC"],
            "Copa Verde": ["Paysandu", "Vila Nova", "Cuiabá", "Remo", "Goiás", "Amazonas"]
        }
    },
    "EUROPA": {
        "Competições UEFA": {
            "UEFA Champions League": ["Real Madrid", "Man. City", "Bayern Munique", "Arsenal", "Barcelona", "Inter de Milão", "PSG", "Dortmund", "Juventus", "Bayer Leverkusen", "AC Milan", "Atletico Madrid"],
            "UEFA Europa League": ["Liverpool", "AC Milan", "AS Roma", "Benfica", "Ajax", "Porto", "Tottenham", "Man. United", "Sporting CP", "Villareal"],
            "UEFA Conference League": ["Chelsea", "Fiorentina", "Real Betis", "Nice", "Lazio", "Heidenheim"]
        },
        "Ligas Nacionais": {
            "Premier League": ["Man. City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Newcastle", "Man. United", "West Ham", "Brighton"],
            "La Liga": ["Real Madrid", "Barcelona", "Girona", "Atlético Madrid", "Athletic Bilbao", "Real Sociedad", "Real Betis", "Valencia"],
            "Bundesliga": ["Bayer Leverkusen", "Bayern Munique", "Stuttgart", "RB Leipzig", "Dortmund", "Frankfurt", "Hoffenheim"],
            "Serie A (Itália)": ["Inter de Milão", "AC Milan", "Juventus", "Atalanta", "Bologna", "AS Roma", "Lazio", "Napoli", "Fiorentina"],
            "Ligue 1 (França)": ["PSG", "Monaco", "Brest", "Lille", "Nice", "Lyon", "Marseille", "Lens"],
            "Liga Portugal": ["Sporting CP", "Benfica", "Porto", "Braga", "Vitória SC", "Moreirense"]
        }
    },
    "AMÉRICA DO SUL": {
        "Continental": {
            "Copa Libertadores": ["Flamengo", "Palmeiras", "River Plate", "Boca Juniors", "Fluminense", "Atlético-MG", "Peñarol", "Colo-Colo", "Nacional", "Talleres", "Bolívar", "LDU Quito"],
            "Copa Sul-Americana": ["Internacional", "Cruzeiro", "Corinthians", "Racing Club", "Fortaleza", "Lanús", "Athletico-PR", "Ind. Medellín", "Cuiabá", "Libertad"]
        },
        "Ligas Locais": {
            "Liga Profissional (Argentina)": ["River Plate", "Boca Juniors", "Racing Club", "Independiente", "San Lorenzo", "Talleres", "Estudiantes", "Velez Sarsfield"],
            "Campeonato Chileno": ["Colo-Colo", "Universidad de Chile", "Universidad Católica", "Huachipato"],
            "Liga BetPlay (Colômbia)": ["Junior", "Millonarios", "Atlético Nacional", "América de Cali", "Santa Fe", "Ind. Medellín"]
        }
    },
    "MERCADOS EMERGENTES": {
        "Arábia Saudita": {
            "Saudi Pro League": ["Al-Hilal", "Al-Nassr", "Al-Ittihad", "Al-Ahli", "Al-Ettifaq", "Al-Shabab", "Al-Taawoun"]
        },
        "Estados Unidos": {
            "MLS": ["Inter Miami", "LA Galaxy", "Columbus Crew", "LAFC", "Seattle Sounders", "FC Cincinnati", "New York Red Bulls"]
        },
        "Ásia": {
            "J-League (Japão)": ["Vissel Kobe", "Yokohama F. Marinos", "Kawasaki Frontale", "Urawa Reds"],
            "Qatar Stars League": ["Al-Sadd", "Al-Duhail", "Al-Rayyan", "Al-Gharafa"]
        }
    }
}

# --- [LOCK] CABEÇALHO ---
st.markdown("""
    <div class="betano-header">
        <div class="header-left">
            <a href="/" target="_self" class="logo-link">GESTOR IA</a>
            <div class="nav-items">
                <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>OPORTUNIDADES IA</span>
                <span>Estatísticas Avançadas</span><span>PROBABILIDADES REAIS</span><span>Assertividade IA</span>
            </div>
        </div>
        <div class="header-right">
            <div class="search-icon">🔍</div>
            <div class="registrar-pill">REGISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True) 
    if st.button("🎯 SCANNER PRÉ-LIVE"): 
        st.session_state.aba_ativa = "analise"
        st.session_state.analise_travada = False
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "scanner_live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    st.button("📅 JOGOS DO DIA")
    st.button("🏆 VENCEDORES DA COMPETIÇÃO")
    st.button("⚽ APOSTAS POR GOLS")

st.markdown('<div style="height: 65px;"></div>', unsafe_allow_html=True)

# --- [ABA] HOME ---
if st.session_state.aba_ativa == "home":
    st.markdown('<div class="news-ticker">● LIVE: IA DETECTA ALTA PROBABILIDADE EM MERCADO DE GOLS HOJE ● ALERTA: ODDS EM QUEDA ● HIERARQUIA v56.2 ATIVA</div>', unsafe_allow_html=True)
    
    h1, h2, h3, h4 = st.columns(4)
    with h1: st.markdown('<div class="highlight-card"><div style="color:#64748b; font-size:9px;"><span class="pulse-dot"></span>Destaque Live</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">FLAMENGO x PALMEIRAS</div><div class="conf-bar-bg"><div
