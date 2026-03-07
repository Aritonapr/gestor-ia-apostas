import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA APOSTAS", layout="wide", page_icon="⚽")

# --- 2. ESTILO VISUAL (ESTRUTURA PROTEGIDA + NOTIFICAÇÃO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap');
    
    .main { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #111a21; border-right: 2px solid #f05a22; min-width: 320px !important; }
    
    /* ÍCONE DE NOTIFICAÇÃO (ESTILO EMAIL) */
    .nav-bar { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #2d3748; margin-bottom: 20px; }
    .notif-box { display: flex; align-items: center; background: #1a242d; padding: 5px 15px; border-radius: 20px; border: 1px solid #f05a22; }
    .pulse-notif { width: 10px; height: 10px; background: #f05a22; border-radius: 50%; margin-right: 10px; animation: pulse-notif 1.5s infinite; }
    @keyframes pulse-notif { 0% { box-shadow: 0 0 0 0 rgba(240, 90, 34, 0.7); } 70% { box-shadow: 0 0 0 10px rgba(240, 90, 34, 0); } 100% { box-shadow: 0 0 0 0 rgba(240, 90, 34, 0); } }

    /* ABAS CUSTOMIZADAS */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #1a242d !important; border: 1px solid #2d3748 !important; 
        color: #5a6b79 !important; border-radius: 10px 10px 0 0 !important; padding: 10px 20px !important; 
    }
    .stTabs [aria-selected="true"] { border-color: #f05a22 !important; color: #f05a22 !important; font-weight: bold !important; }

    /* CARD PRINCIPAL E MINI CARDS */
    .card-principal { background-color: #1a242d; padding: 30px; border-radius: 20px; border-bottom: 4px solid #f05a22; margin-bottom: 20px; text-align: center; }
    .match-title { color: #ffffff !important; font-family: 'Orbitron', sans-serif; font-size: 28px; font-weight: 900; text-transform: uppercase; margin-bottom: 20px; }
    .label-prob { color: #ffffff !important; font-size: 13px; font-weight: 800; text-transform: uppercase; }
    .val-prob { color: #f05a22; font-size: 28px; font-weight: 900; }
    .mini-card { background-color: #111a21; padding: 10px; border-radius: 12px; border: 1px solid #2d3748; text-align: center; height: 100px; display: flex; flex-direction: column; justify-content: center; }
    .mini-label { color: #ffffff !important; font-weight: 800 !important; font-size: 10px; text-transform: uppercase; margin-bottom: 8px; }
    .mini-val { color: #00ffc3 !important; font-weight: 900; font-size: 20px; }
    
    /* RADAR ESTRATÉGICO NO TOPO */
    .radar-topo {
        background: linear-gradient(90deg, rgba(240,90,34,0.1) 0%, rgba(26,36,45,1) 100%);
        border-radius: 12px; padding: 12px 20px; margin-bottom: 15px;
        display: flex; align-items: center; border: 1px solid #f05a22;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. INICIALIZAÇÃO DE ESTADO ---
if 'banca' not in st.session_state: st.session_state.banca = 1000.0
if 'historico' not in st.session_state: st.session_state.historico = []
if 'liga_ativa' not in st.session_state: st.session_state.liga_ativa = 'BRA_A'

# --- 4. ENGINE DE CÁLCULO IA ---
def gerar_analise_completa(t1, t2):
    # Simula cálculo estatístico profundo para 1 jogo
    seed = len(t1) + len(t2)
    np.random.seed(seed)
    win_h = np.random.uniform(20, 60)
    return {
        'vencedor': t1 if win_h > 45 else (t2 if win_h < 30 else "Empate"),
        'win_h': win_h, 'draw': np.random.uniform(20, 30), 'win_a': 100 - win_h - 25,
        'gols': np.random.choice([1, 2, 3, 4], p=[0.2, 0.4, 0.3, 0.1]),
        'cantos': np.random.randint(8, 14),
        'cartoes': np.random.randint(2, 7),
        'chutes_gol': np.random.randint(5, 12),
        'chutes': np.random.randint(15, 28),
        'over25': np.random.uniform(40, 75)
    }

# --- 5. BARRA LATERAL (RESTAURADA) ---
with st.sidebar:
    st.markdown("""<div class="sidebar-header"><div class="ai-logo-box">🤖</div><div class="sidebar-title">GESTOR IA<br>APOSTAS</div></div>""", unsafe_allow_html=True)
    
    def sidebar_button(label, id_liga):
        is_active = st.session_state.liga_ativa == id_liga
        if st.button(label, key=f"btn_{id_liga}", type="primary" if is_active else "secondary"):
            st.session_state.liga_ativa = id_liga
            st.rerun()

    st.markdown('<p class="cat-label">BR NACIONAIS</p>', unsafe_allow_html=True)
    sidebar_button("SÉRIE A - BRASILEIRÃO", 'BRA_A')
    sidebar_button("SÉRIE B - BRASILEIRÃO", 'BRA_B')
    sidebar_button("PAULISTÃO", 'PAULISTÃO')
    st.markdown('<p class="cat-label">🇪🇺 EUROPA</p>', unsafe_allow_html=True)
    sidebar_button("PREMIER LEAGUE", 'E0')
    sidebar_button("LA LIGA", 'SP1')

# --- 6. BARRA DE NOTIFICAÇÃO TOPO ---
st.markdown(f"""
    <div class="nav-bar">
        <div style="font-family:'Orbitron'; font-weight:900; color:#f05a22; letter-spacing:2px;">SISTEMA OPERACIONAL IA</div>
        <div class="notif-box">
            <div class="pulse-notif"></div>
            <span style="font-size:11px; font-weight:bold; color:white;">SCANNER DIÁRIO ATIVO: 12 JOGOS ENCONTRADOS</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 7. SISTEMA DE ABAS ---
tab_radar, tab_scanner, tab_banca, tab_historico = st.tabs(["🎯 RADAR NEURAL", "🔍 SCANNER DIÁRIO", "💰 GESTÃO DE BANCA", "📜 HISTÓRICO"])

# --- ABA 1: RADAR NEURAL (O que já tínhamos) ---
with tab_radar:
    # (Inserir aqui a lógica de seleção de times e exibir os cards igual à v12.0)
    st.button("🔥 EXECUTAR ALGORITMO COMPLETO", key="exec_radar")
    st.info("Selecione os times para uma análise individual profunda.")

# --- ABA 2: SCANNER DIÁRIO (NOVIDADE: PALPITES PRONTOS) ---
with tab_scanner:
    st.markdown("### 🔍 Oportunidades Filtradas pela IA")
    # Simula a varredura automática da liga selecionada
    jogos_dia = [("Botafogo", "Flamengo"), ("Chelsea", "Arsenal"), ("Real Madrid", "Barcelona")]
    
    for mandante, visitante in jogos_dia:
        res = gerar_analise_completa(mandante, visitante)
        with st.expander(f"⭐ {mandante} vs {visitante} - DETALHES COMPLETOS"):
            c1, c2, c3 = st.columns(3)
            with c1: st.success(f"Vencedor: {res['vencedor']}")
            with c2: st.warning(f"Gols: {res['gols']} totais")
            with c3: st.info(f"Escanteios: {res['cantos']}")
            
            # Mini resumo para o scanner
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Chutes no Gol", res['chutes_gol'])
            m2.metric("Chutes Totais", res['chutes'])
            m3.metric("Cartões", res['cartoes'])
            m4.metric("Prob. Over 2.5", f"{res['over25']:.1f}%")

# --- ABA 3: GESTÃO DE BANCA (NOVIDADE) ---
with tab_banca:
    st.markdown("### 💰 Calculadora de Gestão de Risco")
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        st.session_state.banca = st.number_input("Banca Atual (R$)", value=st.session_state.banca)
        perce = st.slider("% de Stake por jogo", 0.5, 5.0, 1.0)
    with col_b2:
        odd = st.number_input("Odd do Jogo", value=2.0)
        valor_aposta = (st.session_state.banca * perce) / 100
        st.markdown(f"""
            <div style='background:#1a242d; padding:20px; border-radius:10px; border:1px solid #00ffc3;'>
                <p style='margin:0; font-size:12px; color:#00ffc3;'>VALOR SUGERIDO DA APOSTA</p>
                <p style='margin:0; font-size:32px; font-weight:900;'>R$ {valor_aposta:.2f}</p>
                <p style='margin:0; font-size:12px; opacity:0.6;'>Lucro possível: R$ {valor_aposta*(odd-1):.2f}</p>
            </div>
        """, unsafe_allow_html=True)

# --- ABA 4: HISTÓRICO (NOVIDADE) ---
with tab_historico:
    st.markdown("### 📜 Relatório de Performance")
    # Exemplo de tabela de histórico
    data_hist = {
        'Data': ['07/03', '06/03', '05/03'],
        'Partida': ['Flamengo vs Vasco', 'Real vs Betis', 'City vs United'],
        'Entrada': ['Vitória Flamengo', 'Over 2.5', 'Cantos +9.5'],
        'Status': ['✅ GREEN', '❌ RED', '✅ GREEN'],
        'Lucro/Perda': ['R$ 50,00', '-R$ 20,00', 'R$ 45,00']
    }
    st.table(data_hist)

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:10px;'>GESTOR IA v13.0 - WORKSTATION COMPLETA</p>", unsafe_allow_html=True)
