import streamlit as st
import pandas as pd
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
    "ENG_P": ["Man. City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Man. United", "Newcastle"],
    "ESP_L": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Athletic Bilbao", "Real Sociedad", "Sevilla"],
    "ITA_A": ["Inter de Milão", "Milan", "Juventus", "Atalanta", "Roma", "Napoli", "Lazio", "Bologna"]
}

# --- 3. CSS CORRIGIDO (FOCO NOS BOTÕES) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    /* Fundo e Geral */
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #0b1218 !important; border-right: 2px solid #f05a22 !important; min-width: 260px !important; }

    /* BOTÃO DA SIDEBAR - CORREÇÃO DE TAMANHO */
    .stButton > button { 
        width: 100% !important;
        height: 42px !important; /* Altura aumentada para caber o texto */
        background: linear-gradient(90deg, rgba(240, 90, 34, 0.1) 0%, rgba(26, 36, 45, 0.8) 100%) !important;
        color: #cbd5e0 !important; 
        font-size: 12px !important; /* Tamanho de fonte legível */
        font-weight: 600 !important;
        border-radius: 8px !important; 
        border: 1px solid rgba(240, 90, 34, 0.2) !important; 
        transition: all 0.3s ease !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 15px !important;
        margin-bottom: 5px !important;
        overflow: hidden !important;
        white-space: nowrap !important;
    }

    /* Efeito de Hover */
    .stButton > button:hover { 
        background: #f05a22 !important;
        color: white !important;
        border: 1px solid #ffffff !important;
        transform: translateX(5px);
    }

    /* Botão Ativo (Destaque) */
    .stButton > button[kind="primary"] { 
        background: #f05a22 !important;
        color: white !important;
        box-shadow: 0 0 15px rgba(240, 90, 34, 0.4) !important;
    }

    /* Títulos das Categorias na Sidebar */
    .cat-header {
        color: #f05a22;
        font-family: 'Orbitron', sans-serif;
        font-size: 13px;
        font-weight: 800;
        margin: 20px 0 10px 10px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Ajuste do Header Principal */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        color: #f05a22;
        font-size: 22px;
        font-weight: 900;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. ENGINE ---
def calcular_engine(casa, fora):
    seed = int(hashlib.sha256((casa + fora).encode()).hexdigest(), 16) % 100
    return 35+(seed%30), 15+(seed%15), 50+(seed%40)

# --- 5. NAVEGAÇÃO SIDEBAR (REORGANIZADA) ---
if 'liga_ativa' not in st.session_state: st.session_state.update(liga_ativa='BRA_A', nome_liga='SÉRIE A')

with st.sidebar:
    st.markdown('<div class="main-title">⚽ GESTOR IA</div>', unsafe_allow_html=True)
    
    # Função para criar botões sem quebrar o layout
    def liga_btn(icon, label, vid):
        if st.button(f"{icon} {label}", key=f"btn_{vid}", 
                     type="primary" if st.session_state.liga_ativa == vid else "secondary"):
            st.session_state.liga_ativa = vid; st.session_state.nome_liga = label; st.rerun()

    st.markdown('<div class="cat-header">📂 FUTEBOL BRASIL</div>', unsafe_allow_html=True)
    liga_btn("🔘", "SÉRIE A", "BRA_A")
    liga_btn("🔘", "SÉRIE B", "BRA_B")
    
    st.markdown('<div class="cat-header">🌍 ELITE EUROPA</div>', unsafe_allow_html=True)
    liga_btn("🏴󠁧󠁢󠁥󠁮󠁧󠁿", "PREMIER LEAGUE", "ENG_P")
    liga_btn("🇪🇸", "LA LIGA", "ESP_L")
    liga_btn("🇮🇹", "SERIE A TIM", "ITA_A")

# --- 6. CONTEÚDO PRINCIPAL ---
st.markdown(f'<div class="main-title"><span>📊</span> {st.session_state.nome_liga}</div>', unsafe_allow_html=True)

times_lista = DIC_TIMES.get(st.session_state.liga_ativa, ["Selecione..."])
c1, c2, c3 = st.columns([3, 3, 2])

with c1: t_casa = st.selectbox("Mandante", sorted(times_lista))
with c2: t_fora = st.selectbox("Visitante", sorted([t for t in times_lista if t != t_casa]))
with c3: 
    st.write(" ") # Espaçador
    st.write(" ")
    executar = st.button("🔥 PROCESSAR", use_container_width=True, type="primary")

if executar:
    pc, pe, mg = calcular_engine(t_casa, t_fora)
    st.success(f"Análise Concluída para {t_casa} x {t_fora}")
    # Aqui entrariam seus cards de resultados...
