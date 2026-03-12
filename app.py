import streamlit as st
import time

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v9.0]
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- INJEÇÃO DE CÓDIGO FONTE SUPREMO (REPARO DE ESTRUTURA E HARMONIA) ---
st.markdown("""
    <style>
    /* 1. LIMPEZA E FUNDO */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"] { display: none !important; }
    .stApp { background-color: #0b0e11 !important; color: #e2e8f0 !important; font-family: 'Roboto', sans-serif !important; }
    
    /* 2. SIDEBAR ESTRUTURADA (CORREÇÃO DE SOBREPOSIÇÃO) */
    [data-testid="stSidebar"] { 
        background-color: #15191d !important; 
        margin-top: 50px !important; 
        width: 260px !important; 
        min-width: 260px !important;
        border-right: 1px solid #2d3843 !important;
    }
    
    /* Ajuste do container de botões na sidebar para evitar encavalar */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { 
        gap: 8px !important; /* Espaço vital entre botões */
        padding-top: 0px !important; 
        margin-top: -35px !important; 
    }

    /* 3. NAVBAR SUPERIOR */
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 50px; background-color: #1a242d; border-bottom: 2px solid #f64d23; display: flex; align-items: center; padding: 0 20px; z-index: 999999; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    .nav-items { display: flex; gap: 20px; margin-left: 30px; flex-grow: 1; color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    .logo-hex { width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px; }

    /* 4. BOTÕES GÊMEOS (CÁPSULAS LARANJAS) */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    
    div.stButton > button, [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button {
        background-color: #f64d23 !important;
        color: white !important;
        border-radius: 50px !important;
        height: 45px !important;
        border: none !important;
        font-weight: 900 !important;
        font-size: 12px !important;
        text-transform: uppercase !important;
        position: relative !important;
        overflow: hidden !important;
        width: 100% !important;
    }

    /* Botão FERRAMENTA IA específico */
    [data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child button {
        width: 180px !important;
        margin: 10px auto 15px auto !important;
    }

    /* 5. BOTÕES DE CATEGORIA (CORREÇÃO DE TEXTO LONGO) */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:not(:first-child) button {
        background-color: rgba(255,255,255,0.03) !important;
        color: #e2e8f0 !important;
        border: none !important;
        border-left: 3px solid transparent !important;
        text-align: left !important;
        font-weight: 700 !important;
        font-size: 10px !important;
        padding: 10px 15px !important;
        width: 100% !important;
        min-height: 40px !important; /* Altura mínima para não encavalar */
        border-radius: 0px !important;
        text-transform: uppercase;
        line-height: 1.2 !important;
    }

    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:not(:first-child) button:hover {
        border-left: 3px solid #f64d23 !important;
        background-color: rgba(246, 77, 35, 0.1) !important;
    }

    /* 6. HARMONIZAÇÃO DOS CAMPOS DE SELEÇÃO (SELECTBOX) */
    div[data-baseweb="select"] > div {
        background-color: #1a242d !important;
        color: white !important;
        border: 1px solid #2d3843 !important;
    }
    
    [data-testid="stWidgetLabel"] p {
        color: #94a3b8 !important;
        font-size: 10px !important;
        text-transform: uppercase !important;
        font-weight: 800 !important;
    }

    /* 7. TEXTOS E TÍTULOS */
    .white-title { color: white !important; font-weight: 900; font-size: 26px !important; margin-bottom: 25px !important; }
    .standard-text { color: #e2e8f0 !important; font-weight: 700; font-size: 18px !important; margin-top: 15px !important; }
    
    .betano-footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR ---
st.markdown(f"""
    <div class="betano-header">
        <div class="logo-hex"></div>
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-items">
            <span>Apostas Esportivas</span><span>Apostas ao Vivo</span><span>Apostas Encontradas</span><span>Assertividade IA</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (ESTRUTURA REPARADA) ---
with st.sidebar:
    st.button("FERRAMENTA IA")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO") # Agora com espaço e sem encavalar
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")

# --- ÁREA CENTRAL ---
st.markdown('<div class="white-title">ANÁLISE MÉTRICA DOS JOGOS</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1: st.selectbox("SELECIONE A REGIÃO", ["BR COMPETIÇÕES BRASILEIRAS"])
with c2: st.selectbox("CATEGORIA", ["Copas Nacionais"])
with c3: st.selectbox("CAMPEONATO", ["Copa do Brasil"])

st.divider()

st.markdown('<div class="standard-text">Confronto: Copa do Brasil</div>', unsafe_allow_html=True)
t1, t2 = st.columns(2)
with t1: st.selectbox("TIME CASA", ["Flamengo"])
with t2: st.selectbox("TIME FORA", ["Amazonas FC"])

st.button("PROCESSAR ALGORITMO")

# FOOTER
st.markdown("""<div class="betano-footer"><div>STATUS: ● IA OPERACIONAL | HARMONIA RESTAURADA</div><div>GESTOR IA PRO v9.0</div></div>""", unsafe_allow_html=True)
