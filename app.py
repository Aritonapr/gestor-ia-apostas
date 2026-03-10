import streamlit as st
import pandas as pd

# 1. Configuração da Página e Cores Betano
st.set_page_config(page_title="GIAE - Bet Style", layout="wide")

# CSS para emular a interface da imagem
st.markdown("""
    <style>
    /* Fundo geral e fontes */
    .stApp {
        background-color: #F0F2F5;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Barra Superior Laranja */
    .header-betano {
        background-color: #FF4B21;
        padding: 10px 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin: -60px -50px 20px -50px;
    }
    .logo-giae {
        color: white;
        font-weight: 900;
        font-size: 30px;
        font-style: italic;
    }

    /* Cards de Jogos (Destaque) */
    .highlight-card {
        background: linear-gradient(135deg, #1A242D 0%, #323F4B 100%);
        color: white;
        border-radius: 15px;
        padding: 20px;
        min-height: 180px;
        position: relative;
        border-left: 5px solid #FF4B21;
    }
    
    /* Botões de Odds */
    .odd-button {
        background-color: #E8EDF2;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        color: #1A242D;
        font-weight: bold;
        border: 1px solid #D1D8E0;
        cursor: pointer;
    }
    .odd-button:hover {
        background-color: #FF4B21;
        color: white;
    }

    /* Sidebar Direita (Cupom de Apostas) */
    .bet-slip {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    /* Ajuste de Botões do Streamlit para o estilo Sidebar */
    [data-testid="stSidebar"] {
        background-color: white;
    }
    .stButton > button {
        border-radius: 8px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER (TOPO LARANJA) ---
st.markdown("""
    <div class="header-betano">
        <div class="logo-giae">GIAE</div>
        <div style="color: white; font-weight: bold;">
            <span style="margin-right: 20px;">APOSTAS ESPORTIVAS</span>
            <span style="margin-right: 20px;">AO VIVO</span>
            <button style="background: transparent; border: 1px solid white; color: white; padding: 5px 15px; border-radius: 5px;">ENTRAR</button>
            <button style="background: #00CC66; border: none; color: white; padding: 5px 15px; border-radius: 5px; margin-left: 10px;">REGISTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ESQUERDA (NAVEGAÇÃO) ---
with st.sidebar:
    st.markdown("### 🔍 Categorias")
    st.button("⚽ Próximos Jogos", use_container_width=True)
    st.button("🏆 Vencedores", use_container_width=True)
    st.button("🎯 Especiais IA", use_container_width=True)
    st.divider()
    st.markdown("### 🌍 Competições")
    st.caption("Brasileirão Série A")
    st.caption("Champions League")
    st.caption("Premier League")

# --- CONTEÚDO PRINCIPAL (LAYOUT DE 3 COLUNAS) ---
col_main, col_right = st.columns([3, 1])

with col_main:
    # 1. Carrossel de Destaques (Mock)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
            <div class="highlight-card">
                <p style="color: #FF4B21; font-weight: bold; margin-bottom:0;">Esta noite • 21:30</p>
                <h3 style="margin-top:0;">Botafogo vs Barcelona-EQU</h3>
                <div style="display: flex; justify-content: space-between; margin-top: 30px;">
                    <div class="odd-button" style="flex:1; margin-right:5px;">1 <br> 2.87</div>
                    <div class="odd-button" style="flex:1; margin-right:5px;">X <br> 3.60</div>
                    <div class="odd-button" style="flex:1;">2 <br> 4.10</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with c2:
        st.markdown("""
            <div class="highlight-card">
                <p style="color: #FF4B21; font-weight: bold; margin-bottom:0;">Esta noite • 21:30</p>
                <h3 style="margin-top:0;">Mirassol vs Santos</h3>
                <div style="display: flex; justify-content: space-between; margin-top: 30px;">
                    <div class="odd-button" style="flex:1; margin-right:5px;">1 <br> 1.85</div>
                    <div class="odd-button" style="flex:1; margin-right:5px;">X <br> 3.70</div>
                    <div class="odd-button" style="flex:1;">2 <br> 4.70</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # 2. Filtros de Esportes (Ícones)
    st.write("")
    st.markdown("### 🏟️ JUNTE-SE À AÇÃO")
    tab1, tab2, tab3, tab4 = st.tabs(["⚽ Futebol", "🏀 Basquete", "🎾 Tênis", "🎮 eSports"])
    
    with tab1:
        # Tabela de Jogos Estilo Betano
        data = {
            "Hora": ["10/03 21:30", "10/03 21:30"],
            "Evento": ["⚽ Mirassol vs Santos", "⚽ Botafogo vs Barcelona"],
            "1": [1.85, 2.87],
            "X": [3.70, 3.60],
            "2": [4.70, 4.10]
        }
        st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)

# --- SIDEBAR DIREITA (CUPOM / IA) ---
with col_right:
    st.markdown("""<div class="bet-slip">
        <h4 style="text-align: center; color: #323F4B;">MINHAS APOSTAS</h4>
        <div style="display: flex; justify-content: space-around; border-bottom: 1px solid #EEE; padding-bottom: 10px;">
            <small style="color: #FF4B21; font-weight: bold;">Em Aberto</small>
            <small>Resolvidas</small>
        </div>
        <br>
        <p style="text-align: center; color: gray; font-size: 13px;">Não tem apostas em aberto.</p>
    </div>""", unsafe_allow_html=True)
    
    st.write("")
    
    # Simulação da "BetaniIA" da imagem
    with st.container(border=True):
        st.markdown("<h4 style='color: #FF4B21;'>🤖 GIAE Predictor</h4>", unsafe_allow_html=True)
        valor = st.number_input("Quanto deseja apostar?", value=30)
        ganho = st.select_slider("Quanto quer ganhar?", options=["R$60-200", "R$200-600", "R$600+"])
        if st.button("GERAR APOSTA IA", use_container_width=True, type="primary"):
            st.info("Buscando combinações...")
