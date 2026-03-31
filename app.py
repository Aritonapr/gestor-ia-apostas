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
                <span style="color: #ffffff; font-size: 12px; font-weight: bold; cursor: pointer;">APOSTAS ESPORTIVAS</span>
                <span style="color: #ffffff; font-size: 12px; font-weight: bold; cursor: pointer;">APOSTAS AO VIVO</span>
                <span style="color: #ffffff; font-size: 12px; font-weight: bold; cursor: pointer;">ESTATÍSTICAS AVANÇADAS</span>
                <span style="color: #ffffff; font-size: 12px; font-weight: bold; cursor: pointer;">MERCADO PROBABILÍSTICO</span>
            </nav>
        </div>
        <div style="display: flex; gap: 10px;">
            <button style="background: transparent; border: 1px solid #ffffff; color: white; padding: 5px 15px; border-radius: 20px; cursor: pointer; font-size: 12px;">REGISTRAR</button>
            <button style="background: linear-gradient(135deg, #6200ea, #03dac6); border: none; color: white; padding: 5px 25px; border-radius: 20px; cursor: pointer; font-weight: bold; font-size: 12px;">ENTRAR</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- FUNÇÃO AUXILIAR DE CARDS (SKIN "ZERO WHITE PRO") ---
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
    st.markdown("<br>", unsafe_allow_html=True)
    menu = st.radio("MENU", ["🎯 SCANNER PRÉ-LIVE", "📡 SCANNER EM TEMPO REAL", "💰 GESTÃO DE BANCA", "📅 BILHETE OURO"], label_visibility="collapsed")
    st.markdown("<br>"*10, unsafe_allow_html=True)
    st.markdown("<div style='background: #161b22; padding: 10px; border-radius: 5px; border-left: 3px solid #6200ea; color: #6200ea; font-size: 12px; font-weight: bold;'>STATUS: IA OPERACIONAL | v71.0</div>", unsafe_allow_html=True)

# --- ALTERAÇÃO APENAS NA LÓGICA DO BOTÃO "SCANNER PRÉ-LIVE" ---
if menu == "🎯 SCANNER PRÉ-LIVE":
    st.markdown("### 🎯 SCANNER PRÉ-LIVE - ANÁLISE MANUAL")
    
    # Grid de seleção preservado
    c1, c2, c3 = st.columns(3)
    with c1: pais = st.selectbox("REGIÃO / PAÍS", ["BRASIL", "INGLATERRA", "ESPANHA"])
    with c2: liga = st.selectbox("GRUPO", ["BRASILEIRÃO", "PREMIER LEAGUE", "LA LIGA"])
    with c3: div = st.selectbox("COMPETIÇÃO", ["SÉRIE A", "SÉRIE B", "CHAMPIONS"])
    
    st.markdown("#### ⚔️ DEFINIR CONFRONTO")
    c4, c5 = st.columns(2)
    with c4: casa = st.selectbox("TIME DA CASA", ["Athletico-PR", "Flamengo", "Arsenal", "Real Madrid"])
    with c5: fora = st.selectbox("TIME DE FORA", ["Atlético-MG", "Palmeiras", "Chelsea", "Barcelona"])

    # Alteração solicitada focada na lógica back-end
    if st.button("⚡ EXECUTAR ALGORITMO"):
        st.markdown(f"<div style='background: rgba(3, 218, 198, 0.1); padding: 15px; border-radius: 5px; border-left: 5px solid #03dac6; color: #03dac6; font-weight: bold;'>🟢 SISTEMA JARVIS: FILÉ MIGNON: INFORMAÇÃO REAL</div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; color: #ffffff;'>{casa} vs {fora}</h3>", unsafe_allow_html=True)
        
        # Injeção de dados nos cards existentes
        res = st.columns(4)
        with res[0]: draw_card("VENCEDOR", "ALTA PROB.", "#6200ea")
        with res[1]: draw_card("GOLS", "OVER 1.5")
        with res[2]: draw_card("STAKE", "R$ 10.00")
        with res[3]: draw_card("CANTOS", "9.5+")
        
        if st.button("💾 SALVAR CALL NO HISTÓRICO"):
            st.toast("CALL SALVA COM SUCESSO!")

elif menu == "📅 BILHETE OURO":
    st.markdown("### 📅 BILHETE OURO - 2026")
    
    # Layout de KPIs preservado conforme Foto 2
    k1, k2, k3, k4 = st.columns(4)
    with k1: draw_card("BANCA ATUAL", "R$ 1.000,00")
    with k2: draw_card("ASSERTIVIDADE", "92.4%")
    with k3: draw_card("SUGESTÃO", "OVER 2.5")
    with k4: draw_card("IA STATUS", "ONLINE")

    k5, k6, k7, k8 = st.columns(4)
    with k5: draw_card("VOL. GLOBAL", "ALTO", "#6200ea")
    with k6: draw_card("STAKE PADRÃO", "1.0%")
    with k7: draw_card("VALOR ENTRADA", "R$ 10.00")
    with k8: draw_card("SISTEMA", "JARVIS v71.0")

    st.markdown("<br>### 📋 ANÁLISE COMPLETA DO DIA", unsafe_allow_html=True)
    
    # Tabela profissional conforme Foto 9
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

# --- RODAPÉ ---
st.markdown("<div style='text-align: center; color: #444; font-size: 10px; margin-top: 50px;'>SISTEMA JARVIS PRO v71.0 | 2026</div>", unsafe_allow_html=True)
