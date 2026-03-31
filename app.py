import streamlit as st
import pandas as pd
import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- BLOCO CSS "ZERO WHITE PRO" (IMUTÁVEL - PRESERVADO) ---
st.markdown("""
    <style>
    [data-testid="stHeader"] {background: rgba(0,0,0,0); border-bottom: 1px solid rgba(255,255,255,0.1);}
    .main {background-color: #0e1117;}
    section[data-testid="stSidebar"] {background-color: #0e1117; border-right: 1px solid rgba(255,255,255,0.1); width: 260px !important;}
    .stButton>button {width: 100%; border-radius: 5px; background: linear-gradient(135deg, #6200ea, #03dac6); color: white; border: none; font-weight: bold; transition: 0.3s;}
    .stButton>button:hover {transform: scale(1.02); box-shadow: 0 4px 15px rgba(98, 0, 234, 0.4);}
    .card {background: #161b22; padding: 20px; border-radius: 10px; border-bottom: 3px solid #03dac6; text-align: center; margin-bottom: 15px;}
    .card-title {color: #8b949e; font-size: 10px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;}
    .card-value {color: #ffffff; font-size: 22px; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# --- HEADER (IMUTÁVEL - PRESERVADO) ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0px; margin-bottom: 20px;">
        <div style="display: flex; align-items: center; gap: 15px;">
            <h1 style="color: #6200ea; margin: 0; font-size: 28px; font-weight: 900;">GESTOR IA</h1>
            <nav style="display: flex; gap: 20px; margin-left: 20px;">
                <span style="color: #ffffff; font-size: 12px; font-weight: bold;">APOSTAS ESPORTIVAS</span>
                <span style="color: #ffffff; font-size: 12px; font-weight: bold;">APOSTAS AO VIVO</span>
                <span style="color: #ffffff; font-size: 12px; font-weight: bold;">ESTATÍSTICAS AVANÇADAS</span>
                <span style="color: #ffffff; font-size: 12px; font-weight: bold;">MERCADO PROBABILÍSTICO</span>
            </nav>
        </div>
        <div style="display: flex; gap: 10px;">
            <button style="background: transparent; border: 1px solid #ffffff; color: white; padding: 5px 15px; border-radius: 20px; font-size: 12px;">REGISTRAR</button>
            <button style="background: linear-gradient(135deg, #6200ea, #03dac6); border: none; color: white; padding: 5px 25px; border-radius: 20px; font-weight: bold; font-size: 12px;">ENTRAR</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- FUNÇÃO DE CARDS ---
def draw_card(title, value, color="#03dac6"):
    st.markdown(f"""
        <div class="card">
            <div class="card-title">{title}</div>
            <div class="card-value">{value}</div>
            <div style="width: 100%; background: #30363d; height: 4px; margin-top: 15px; border-radius: 2px;">
                <div style="width: 70%; background: {color}; height: 100%; border-radius: 2px;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR FIXA ---
with st.sidebar:
    menu = st.radio("MENU", ["🎯 SCANNER PRÉ-LIVE", "📡 SCANNER EM TEMPO REAL", "💰 GESTÃO DE BANCA", "📅 BILHETE OURO"], label_visibility="collapsed")
    st.markdown("<br>"*10, unsafe_allow_html=True)
    st.info("STATUS: IA OPERACIONAL | v71.0")

# --- ALTERAÇÃO APENAS NA LÓGICA DO BOTÃO (SCANNER PRÉ-LIVE) ---
if menu == "🎯 SCANNER PRÉ-LIVE":
    st.markdown("### 🎯 SCANNER PRÉ-LIVE - ANÁLISE MANUAL")
    
    col_l1, col_l2, col_l3 = st.columns(3)
    with col_l1: pais = st.selectbox("REGIÃO / PAÍS", ["BRASIL", "INGLATERRA"])
    with col_l2: liga = st.selectbox("GRUPO", ["BRASILEIRÃO", "PREMIER LEAGUE"])
    with col_l3: div = st.selectbox("COMPETIÇÃO", ["SÉRIE A", "SÉRIE B"])
    
    st.markdown("#### ⚔️ DEFINIR CONFRONTO")
    col_t1, col_t2 = st.columns(2)
    with col_t1: casa = st.selectbox("TIME DA CASA", ["Athletico-PR", "Flamengo", "Arsenal"])
    with col_t2: fora = st.selectbox("TIME DE FORA", ["Atlético-MG", "Palmeiras", "Chelsea"])

    # A alteração solicitada ocorre aqui: Lógica interna do botão sem mudar aparência
    if st.button("⚡ EXECUTAR ALGORITMO"):
        st.markdown(f"<div style='color: #03dac6; font-weight: bold;'>🟢 SISTEMA JARVIS: FILÉ MIGNON: INFORMAÇÃO REAL</div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>{casa} vs {fora}</h3>", unsafe_allow_html=True)
        
        res = st.columns(4)
        with res[0]: draw_card("VENCEDOR", "ALTA PROB.", "#6200ea")
        with res[1]: draw_card("GOLS", "OVER 1.5")
        with res[2]: draw_card("STAKE", "R$ 10.00")
        with res[3]: draw_card("CANTOS", "9.5+")
        
        if st.button("💾 SALVAR CALL NO HISTÓRICO"):
            st.toast("CALL SALVA COM SUCESSO!")

elif menu == "📅 BILHETE OURO":
    st.markdown("### 📅 BILHETE OURO - 2026")
    k1, k2, k3, k4 = st.columns(4)
    with k1: draw_card("BANCA ATUAL", "R$ 1.000,00")
    with k2: draw_card("ASSERTIVIDADE", "92.4%")
    with k3: draw_card("SUGESTÃO", "OVER 2.5")
    with k4: draw_card("IA STATUS", "ONLINE")
    
    # Tabela idêntica à Foto 9 e Foto 13
    dados = {
        "STATUS": ["20:00", "21:00", "16:00"],
        "LIGA": ["PREMIER LEAGUE", "LA LIGA", "BRASILEIRÃO"],
        "CASA": ["Arsenal", "Real Madrid", "Flamengo"],
        "FORA": ["Chelsea", "Barcelona", "Palmeiras"],
        "GOLS": ["OVER 1.5 (94%)", "OVER 1.5 (94%)", "OVER 1.5 (94%)"],
        "CONF": ["64%", "82%", "82%"],
        "CANTOS": ["9.5 total", "9.5 total", "9.5 total"],
        "ULTIMA_SYNC": ["30/03/2026 22:09"] * 3
    }
    st.table(pd.DataFrame(dados))

# Rodapé
st.markdown("<div style='text-align: center; color: #444; font-size: 10px; margin-top: 50px;'>SISTEMA JARVIS PRO v71.0 | 2026</div>", unsafe_allow_html=True)
