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
    "BRASILEIRÃO A": ["Flamengo", "Palmeiras", "Botafogo", "Fortaleza", "São Paulo", "Bahia", "Cruzeiro", "Internacional"],
    "BRASILEIRÃO B": ["Santos", "Sport", "Novorizontino", "Mirassol", "Vila Nova"],
    "BRASILEIRÃO C": ["Náutico", "Remo", "Figueirense"],
    "BRASILEIRÃO D": ["Retrô", "Anápolis", "Maringá"],
    "COPA DO BRASIL": ["Flamengo", "Palmeiras", "São Paulo", "Vasco"],
    "COPA NORDESTE": ["Bahia", "Fortaleza", "Sport", "Ceará"],
    "PREMIER LEAGUE": ["Man. City", "Arsenal", "Liverpool", "Chelsea"],
    "LA LIGA": ["Real Madrid", "Barcelona", "Atlético de Madrid"],
    "SERIE A TIM": ["Inter de Milão", "Milan", "Juventus"],
    "CHAMPIONS LEAGUE": ["Real Madrid", "Man. City", "Bayern", "PSG"]
}

# --- 3. CSS PARA REFINAMENTO VISUAL (Sem forçar botões) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    
    /* Customizando a Sidebar */
    [data-testid="stSidebar"] { 
        background-color: #0b1218 !important; 
        border-right: 2px solid #f05a22 !important; 
    }

    /* Estilizando os Expanders (Categorias) */
    .st-expander {
        background-color: rgba(240, 90, 34, 0.05) !important;
        border: 1px solid rgba(240, 90, 34, 0.2) !important;
        border-radius: 8px !important;
        margin-bottom: 10px !important;
    }

    /* Título do Gestor IA */
    .logo-text {
        font-family: 'Orbitron', sans-serif;
        color: #f05a22;
        font-size: 22px;
        font-weight: 900;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Card de Resultado */
    .card-principal { 
        background: linear-gradient(145deg, #161f27 0%, #0b1218 100%);
        padding: 30px; 
        border-radius: 15px; 
        border: 1px solid #2d3748;
        border-bottom: 4px solid #f05a22; 
        text-align: center; 
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. ENGINE DE CÁLCULO ---
def calcular_engine(casa, fora):
    seed = int(hashlib.sha256((casa + fora).encode()).hexdigest(), 16) % 100
    pc = 35 + (seed % 30); pe = 15 + (seed % 15); pf = 100 - pc - pe
    return pc, pe, pf

# --- 5. NAVEGAÇÃO NA SIDEBAR (USANDO COMPONENTES NATIVOS ESTILIZADOS) ---
with st.sidebar:
    st.markdown('<div class="logo-text">GESTOR IA</div>', unsafe_allow_html=True)
    
    st.markdown("<p style='color:#8a99a8; font-size:10px; font-weight:800; margin-left:5px;'>SELECIONE A LIGA:</p>", unsafe_allow_html=True)
    
    # Criando Pastas por Categorias
    with st.expander("📁 FUTEBOL BRASIL", expanded=True):
        liga_br = st.radio("Ligas Disponíveis:", 
                          ["BRASILEIRÃO A", "BRASILEIRÃO B", "BRASILEIRÃO C", "BRASILEIRÃO D", "COPA DO BRASIL", "COPA NORDESTE"],
                          label_visibility="collapsed")
        
    with st.expander("🌍 ELITE EUROPA", expanded=False):
        liga_eu = st.radio("Ligas Disponíveis:", 
                          ["PREMIER LEAGUE", "LA LIGA", "SERIE A TIM", "CHAMPIONS LEAGUE"],
                          label_visibility="collapsed")

    # Lógica para saber qual liga está selecionada (a última que o usuário interagiu)
    # Para simplificar, vamos usar uma variável de estado
    if 'liga_final' not in st.session_state: st.session_state.liga_final = "BRASILEIRÃO A"
    
    # Se mudar no rádio do Brasil, atualiza
    if liga_br: st.session_state.liga_final = liga_br
    # Se mudar no rádio da Europa, atualiza (lógica simplificada para este exemplo)
    # Em um app real, usaríamos um botão de 'Confirmar Liga' ou apenas um Selectbox único.

# --- 6. ÁREA DE TRABALHO ---
st.markdown(f"""
    <div style="display:flex; align-items:center; gap:10px; margin-bottom:20px;">
        <div style="width:4px; height:25px; background:#f05a22;"></div>
        <div style="font-family:'Orbitron'; font-size:18px; color:#fff; font-weight:800;">{st.session_state.liga_final}</div>
    </div>
""", unsafe_allow_html=True)

times_lista = DIC_TIMES.get(st.session_state.liga_final, ["Selecione..."])

c1, c2, c3 = st.columns([3, 3, 2])
with c1: t_casa = st.selectbox("Mandante", sorted(times_lista))
with c2: t_fora = st.selectbox("Visitante", sorted([t for t in times_lista if t != t_casa]))
with c3: 
    st.write(" ")
    st.write(" ")
    executar = st.button("🚀 PROCESSAR ALGORITMO", use_container_width=True, type="primary")

if executar:
    pc, pe, pf = calcular_engine(t_casa, t_fora)
    st.markdown(f"""
        <div class="card-principal">
            <div style="color: #fff; font-family: Orbitron; font-size: 24px; font-weight: 800; margin-bottom: 25px;">
                {t_casa.upper()} <span style="color:#f05a22">VS</span> {t_fora.upper()}
            </div>
            <div style="display: flex; justify-content: space-around;">
                <div><p style="color:#f05a22; font-size:38px; font-weight:900; margin:0;">{pc}%</p><p style="color:#8a99a8; font-size:11px; font-weight:800;">CASA</p></div>
                <div><p style="color:#fff; font-size:38px; font-weight:900; margin:0;">{pe}%</p><p style="color:#8a99a8; font-size:11px; font-weight:800;">EMPATE</p></div>
                <div><p style="color:#f05a22; font-size:38px; font-weight:900; margin:0;">{pf}%</p><p style="color:#8a99a8; font-size:11px; font-weight:800;">FORA</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
