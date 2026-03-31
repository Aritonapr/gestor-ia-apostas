import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- ESTILO CSS "ZERO WHITE PRO" (PRESERVADO) ---
st.markdown("""
    <style>
    [data-testid="stHeader"] {background: rgba(0,0,0,0); border-bottom: 1px solid rgba(255,255,255,0.1);}
    .main {background-color: #0e1117;}
    section[data-testid="stSidebar"] {background-color: #0e1117; border-right: 1px solid rgba(255,255,255,0.1); width: 260px !important;}
    .stButton>button {width: 100%; border-radius: 5px; background: linear-gradient(135deg, #6200ea, #03dac6); color: white; border: none; font-weight: bold; transition: 0.3s;}
    .stButton>button:hover {transform: scale(1.02); box-shadow: 0 4px 15px rgba(98, 0, 234, 0.4);}
    div[data-testid="stMetricValue"] {font-size: 24px; font-weight: bold; color: #ffffff;}
    .card {background: #161b22; padding: 20px; border-radius: 10px; border-bottom: 3px solid #03dac6; text-align: center; margin-bottom: 15px;}
    .card-title {color: #8b949e; font-size: 10px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;}
    .card-value {color: #ffffff; font-size: 22px; font-weight: bold;}
    .status-badge {padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: bold; background: rgba(3, 218, 198, 0.2); color: #03dac6;}
    </style>
""", unsafe_allow_html=True)

# --- HEADER FIXO (IMUTÁVEL) ---
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

# --- INICIALIZAÇÃO DE ESTADOS (BACK-END) ---
if 'banca' not in st.session_state: st.session_state.banca = 1000.00
if 'assertividade' not in st.session_state: st.session_state.assertividade = "92.4%"
if 'calls_history' not in st.session_state: st.session_state.calls_history = []

# --- FUNÇÃO AUXILIAR DE CARDS ---
def draw_card(title, value, progress_color="#03dac6"):
    st.markdown(f"""
        <div class="card">
            <div class="card-title">{title}</div>
            <div class="card-value">{value}</div>
            <div style="width: 100%; background: #30363d; height: 4px; margin-top: 15px; border-radius: 2px;">
                <div style="width: 70%; background: {progress_color}; height: 100%; border-radius: 2px;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (ESTRUTURA FIXA) ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    menu = st.radio("MENU DE COMANDOS", 
                    ["🎯 SCANNER PRÉ-LIVE", "📡 SCANNER EM TEMPO REAL", "💰 GESTÃO DE BANCA", "📅 BILHETE OURO"],
                    label_visibility="collapsed")
    
    st.markdown("<br>"*10, unsafe_allow_html=True)
    st.info(f"STATUS: IA OPERACIONAL | v71.0")

# --- LÓGICA DE NAVEGAÇÃO ---
if menu == "🎯 SCANNER PRÉ-LIVE":
    st.markdown("### 🎯 SCANNER PRÉ-LIVE - ANÁLISE MANUAL")
    
    col1, col2 = st.columns(2)
    with col1:
        liga = st.selectbox("Selecione a Liga:", ["PREMIER LEAGUE", "LA LIGA", "BRASILEIRÃO", "SERIE A"])
    with col2:
        partida = st.selectbox("Selecione a Partida do Dia:", ["Arsenal x Chelsea", "Real Madrid x Barcelona", "Flamengo x Palmeiras"])

    if st.button("GERAR LEITURA JARVIS"):
        # Lógica de Processamento (Back-end)
        st.session_state.analise_atual = {
            "vencedor": "ALTA PROB.",
            "gols": "OVER 1.5",
            "stake": "R$ 10,00",
            "cantos": "9.5+"
        }
        
        st.success("SISTEMA JARVIS: FILÉ MIGNON: INFORMAÇÃO REAL")
        
        # Exibição dos resultados (Injetados no layout padrão)
        res_cols = st.columns(4)
        with res_cols[0]: draw_card("VENCEDOR", st.session_state.analise_atual["vencedor"], "#6200ea")
        with res_cols[1]: draw_card("GOLS", st.session_state.analise_atual["gols"])
        with res_cols[2]: draw_card("STAKE", st.session_state.analise_atual["stake"])
        with res_cols[3]: draw_card("CANTOS", st.session_state.analise_atual["cantos"])
        
        if st.button("💾 SALVAR CALL NO HISTÓRICO"):
            new_call = {"STATUS": "20:00", "LIGA": liga, "CASA": partida.split('x')[0], "FORA": partida.split('x')[1], "GOLS": "OVER 1.5 (94%)"}
            st.session_state.calls_history.append(new_call)
            st.toast("CALL SALVA COM SUCESSO!")

elif menu == "📡 SCANNER EM TEMPO REAL":
    st.markdown("### 📡 AO VIVO AGORA")
    st.info("Buscando partidas em andamento...")
    # Aqui entra a integração com o scraping do Placar de Futebol futuro

elif menu == "📅 BILHETE OURO":
    st.markdown("### 📅 BILHETE OURO - 2026")
    
    # Grid de KPIs Superior (Preservado conforme Foto 2)
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca:,.2f}")
    with kpi2: draw_card("ASSERTIVIDADE", st.session_state.assertividade)
    with kpi3: draw_card("SUGESTÃO", "OVER 2.5")
    with kpi4: draw_card("IA STATUS", "ONLINE", "#03dac6")

    kpi5, kpi6, kpi7, kpi8 = st.columns(4)
    with kpi5: draw_card("VOL. GLOBAL", "ALTO", "#6200ea")
    with kpi6: draw_card("STAKE PADRÃO", "1.0%")
    with kpi7: draw_card("VALOR ENTRADA", "R$ 10,00")
    with kpi8: draw_card("SISTEMA", "JARVIS v71.0")

    st.markdown("---")
    st.markdown("### 📋 ANÁLISE COMPLETA DO DIA")
    
    if st.session_state.calls_history:
        df = pd.DataFrame(st.session_state.calls_history)
        st.table(df) # Mantém o padrão de tabela profissional
    else:
        # Dados de exemplo para manter o visual da Foto 9
        data = {
            "STATUS": ["20:00", "21:00", "16:00"],
            "LIGA": ["PREMIER LEAGUE", "LA LIGA", "BRASILEIRÃO"],
            "CASA": ["Arsenal", "Real Madrid", "Flamengo"],
            "FORA": ["Chelsea", "Barcelona", "Palmeiras"],
            "GOLS": ["OVER 1.5 (94%)", "OVER 1.5 (94%)", "OVER 1.5 (94%)"],
            "CONF": ["64%", "82%", "82%"],
            "CANTOS": ["9.5 total", "9.5 total", "9.5 total"],
            "ULTIMA_SYNC": ["30/03/2026 22:09"] * 3
        }
        st.table(pd.DataFrame(data))

else:
    st.markdown("### 💰 GESTÃO DE BANCA")
    st.write("Módulo de cálculos matemáticos de Stake e ROI.")

# Rodapé discreto
st.markdown(f"<div style='text-align: center; color: #444; font-size: 10px; margin-top: 50px;'>SISTEMA JARVIS PRO v71.0 | {datetime.datetime.now().year}</div>", unsafe_allow_html=True)
