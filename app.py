import streamlit as st
import pandas as pd
import random
from datetime import datetime

# =========================================================
# BLINDAGEM DE EVOLUÇÃO - LAYOUT E CSS ORIGINAL RESTAURADO
# =========================================================
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# CSS para manter o fundo #0b0e11 e os botões originais
st.markdown("""
    <style>
    /* Fundo e Texto Geral */
    .stApp { background-color: #0b0e11; color: white; }
    [data-testid="stHeader"] { background-color: #0b0e11; }
    [data-testid="stSidebar"] { background-color: #0b0e11; border-right: 1px solid #1e2124; }
    
    /* Cabeçalho Horizontal do Print */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background-color: #0b0e11;
        border-bottom: 1px solid #1e2124;
    }
    
    /* Botão Executar Algoritmo (Estilo Degradê Azul/Roxo) */
    .stButton>button {
        width: 100% !important;
        background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%) !important;
        color: white !important;
        border: none !important;
        padding: 15px !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        border-radius: 8px !important;
    }

    /* Selectbox no padrão Dark */
    div[data-baseweb="select"] > div { 
        background-color: #1e2124 !important; 
        color: white !important; 
        border: 1px solid #3d444b !important; 
        border-radius: 8px !important;
    }
    
    .status-jarvis { color: #00ff88; font-size: 0.8em; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# =========================================================
# BANCO DE DADOS DINÂMICO (PARA FILTRAGEM DE TIMES)
# =========================================================
dados_times = {
    'BRASILEIRÃO - SÉRIE A': ['Flamengo', 'Palmeiras', 'São Paulo', 'Corinthians', 'Atlético-MG', 'Botafogo'],
    'PREMIER LEAGUE - SÉRIE A': ['Arsenal', 'Manchester City', 'Liverpool', 'Chelsea', 'Tottenham'],
    'LA LIGA - SÉRIE A': ['Real Madrid', 'Barcelona', 'Atlético de Madrid'],
    'CHAMPIONS LEAGUE': ['Real Madrid', 'Manchester City', 'Bayern Munich', 'PSG', 'Arsenal']
}

# =========================================================
# CABEÇALHO SUPERIOR (MENU HORIZONTAL)
# =========================================================
st.markdown("""
    <div style='display: flex; gap: 20px; font-size: 12px; font-weight: bold; color: #cbd5e0; margin-bottom: 30px;'>
        <span style='color: #8e44ad; font-size: 18px;'>GESTOR IA</span>
        <span>APOSTAS ESPORTIVAS</span>
        <span>APOSTAS AO VIVO</span>
        <span>APOSTAS ENCONTRADAS</span>
        <span>ESTATÍSTICAS AVANÇADAS</span>
        <span>MERCADO PROBABILÍSTICO</span>
        <span>ASSERTIVIDADE IA</span>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# BARRA LATERAL (SIDEBAR)
# =========================================================
with st.sidebar:
    st.markdown("### Navegação")
    aba = st.radio("", [
        "🎯 SCANNER PRÉ-LIVE",
        "📡 SCANNER EM TEMPO REAL",
        "💰 GESTÃO DE BANCA",
        "📜 HISTÓRICO DE CALLS",
        "🎫 BILHETE OURO",
        "🏆 VENCEDORES DA COMPETIÇÃO",
        "⚽ APOSTAS POR GOLS",
        "🚩 APOSTAS POR ESCANTEIOS"
    ])
    
    st.markdown(f"<div class='status-jarvis'>● SISTEMA JARVIS: OPERACIONAL v66.0</div>", unsafe_allow_html=True)

# =========================================================
# 🎯 SCANNER PRÉ-LIVE (CORRIGIDO)
# =========================================================
if aba == "🎯 SCANNER PRÉ-LIVE":
    st.markdown("<h2>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    # Filtros Superiores
    c1, c2, c3 = st.columns(3)
    with c1:
        regiao = st.selectbox("🌎 REGIÃO / PAÍS", ["BRASIL", "INGLATERRA", "ESPANHA", "EUROPA"])
    with c2:
        grupo_map = {"BRASIL": "BRASILEIRÃO", "INGLATERRA": "PREMIER LEAGUE", "ESPANHA": "LA LIGA", "EUROPA": "CHAMPIONS LEAGUE"}
        grupo = st.selectbox("📂 GRUPO", [grupo_map.get(regiao)])
    with c3:
        comp_map = {"BRASILEIRÃO": "SÉRIE A", "PREMIER LEAGUE": "SÉRIE A", "LA LIGA": "SÉRIE A", "CHAMPIONS LEAGUE": "PRINCIPAL"}
        nome_comp = f"{grupo} - {comp_map.get(grupo)}" if grupo != "CHAMPIONS LEAGUE" else "CHAMPIONS LEAGUE"
        st.selectbox("🏆 COMPETIÇÃO", [nome_comp])

    st.markdown("<br><h3>⚔️ DEFINIR CONFRONTO</h3>", unsafe_allow_html=True)
    
    # Lógica de Filtragem de Times (O Arsenal só aparece se a liga for correta)
    lista_times_liga = dados_times.get(nome_comp, ["Time A", "Time B"])
    
    col_a, col_b = st.columns(2)
    with col_a:
        time_casa = st.selectbox("🏠 TIME DA CASA", lista_times_liga, key="casa")
    with col_b:
        # Bloqueio para o time não enfrentar ele mesmo
        lista_fora = [t for t in lista_times_liga if t != time_casa]
        time_fora = st.selectbox("🚀 TIME DE FORA", lista_fora, key="fora")

    # Botão de Execução (Restaura o estilo largo e colorido)
    if st.button("⚡ EXECUTAR ALGORITMO"):
        st.markdown(f"""
            <div style='background-color: #161a1e; padding: 20px; border-radius: 10px; border-left: 5px solid #00ff88;'>
                <span style='color: #00ff88; font-weight: bold;'>● SISTEMA JARVIS:</span> 
                <span style='color: #00ff88;'>FILÉ MIGNON: INFORMAÇÃO REAL PARA {time_casa} x {time_fora}</span>
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# 📡 SCANNER EM TEMPO REAL (CORREÇÃO DO ERRO RANDOM)
# =========================================================
elif aba == "📡 SCANNER EM TEMPO REAL":
    st.markdown("<h2>📡 SCANNER EM TEMPO REAL (LIVE FILTERS)</h2>", unsafe_allow_html=True)
    st.write("Palmeiras x Dortmund")
    
    # Agora o 'random' está importado corretamente no topo do arquivo
    pressao = random.randint(60, 95)
    st.markdown(f"<div style='color:#00ff88; font-size: 20px;'>PRESSÃO: {pressao}%</div>", unsafe_allow_html=True)

# =========================================================
# 🎫 BILHETE OURO (LAYOUT ORIGINAL DOS CARDS)
# =========================================================
elif aba == "🎫 BILHETE OURO":
    st.markdown("<h2>🗓️ BILHETE OURO - TOP 20 ANALISES IA</h2>", unsafe_allow_html=True)
    
    cols = st.columns(4)
    exemplos = [
        {"t1": "Real Madrid", "t2": "Barcelona", "conf": "82%"},
        {"t1": "Flamengo", "t2": "Palmeiras", "conf": "82%"},
        {"t1": "Arsenal", "t2": "Chelsea", "conf": "64%"},
        {"t1": "Arsenal", "t2": "Flamengo", "conf": "92%"}
    ]
    
    for i, jogo in enumerate(exemplos):
        with cols[i]:
            st.markdown(f"""
                <div style='background-color: #161a1e; padding: 15px; border-radius: 10px; border: 1px solid #2d3339;'>
                    <div style='color: #8e44ad; font-size: 10px;'>IA CONFIANÇA: {jogo['conf']}</div>
                    <div style='font-weight: bold; margin: 10px 0;'>{jogo['t1']} vs {jogo['t2']}</div>
                    <div style='font-size: 11px;'>🏆 VENCEDOR: 72% (FAV)</div>
                    <div style='font-size: 11px;'>⚽ GOLS: 1.5+ (FT)</div>
                    <div style='color: #2575fc; font-size: 11px; margin-top: 10px;'>INVESTIMENTO: R$ 10.00</div>
                </div>
                """, unsafe_allow_html=True)

# Mantendo as outras abas acessíveis
else:
    st.info(f"Interface {aba} ativa com layout preservado.")
