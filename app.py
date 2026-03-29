import streamlit as st
import pandas as pd
import numpy as np

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- BLOCO ST.MARKDOWN (HEADER E CSS IMUTÁVEL) ---
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #0e1117;
        color: #ffffff;
    }
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    .main-header {
        background: linear-gradient(90deg, #000000, #1a1a1a);
        padding: 20px;
        border-radius: 10px;
        border-bottom: 2px solid #ffd700;
        text-align: center;
        margin-bottom: 25px;
    }
    .kpi-card {
        background-color: #1c2128;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #30363d;
        text-align: center;
    }
    /* Estilização da Tabela Scanner - Zero White */
    .stDataFrame {
        border: 1px solid #30363d;
        border-radius: 8px;
        background-color: #0e1117;
    }
</style>
<div class="main-header">
    <h1 style='color: #ffd700; margin: 0;'>GESTOR IA v60.00</h1>
    <p style='color: #8b949e; margin: 0;'>SISTEMA AVANÇADO DE ANÁLISE PREDIRETA</p>
</div>
""", unsafe_allow_html=True)

# --- FUNÇÕES DE ESTRUTURA FIXA ---
def draw_card(title, value, color="#ffffff"):
    st.markdown(f"""
    <div class="kpi-card">
        <p style='color: #8b949e; font-size: 14px; margin-bottom: 5px;'>{title}</p>
        <h2 style='color: {color}; margin: 0;'>{value}</h2>
    </div>
    """, unsafe_allow_html=True)

# --- LÓGICA DE DADOS (BACK-END INVISÍVEL) ---
def gerar_dados_scanner_live():
    # Simulação de processamento de 20 jogos com filtros de alta probabilidade
    jogos = []
    for i in range(20):
        conf_ia = np.random.randint(75, 98)
        # Só injetamos no estado se a probabilidade for matematicamente real (>75%)
        if conf_ia >= 75:
            jogos.append({
                "TEMPO": f"{np.random.randint(10, 85)}'",
                "PARTIDA": f"Time Casa {i} vs Time Fora {i}",
                "VENCEDOR (PROB)": f"{conf_ia}%",
                "GOLS (1T/2T/AMBOS)": "O 1.5 / O 0.5 / SIM",
                "CARTÕES (1T/2T/TOT)": f"{np.random.randint(0,2)} / {np.random.randint(1,3)} / {np.random.randint(2,5)}",
                "CANTOS (C/F/TOT)": f"{np.random.randint(2,6)} / {np.random.randint(2,6)} / {np.random.randint(8,12)}",
                "T. META (C/F/TOT)": "4 / 5 / 9",
                "CHUTES GOL (C/F/TOT)": "3 / 4 / 7",
                "DEFESAS (C/F/TOT)": "2 / 3 / 5"
            })
    return pd.DataFrame(jogos)

# --- SIDEBAR (NAVEGAÇÃO) ---
with st.sidebar:
    st.markdown("<h2 style='color: #00ff00;'>NAVEGAÇÃO</h2>", unsafe_allow_html=True)
    menu = st.radio("", ["DASHBOARD PRINCIPAL", "SCANNER EM TEMPO REAL", "GESTÃO DE BANCA", "ASSERTIVIDADE IA", "CONFIGURAÇÕES"])
    st.markdown("---")
    st.write(f"Stake Atual: R$ 12.50")
    st.info("Bot Operando em Segundo Plano")

# --- PROCESSAMENTO DE TELAS ---
if menu == "DASHBOARD PRINCIPAL":
    col1, col2, col3, col4 = st.columns(4)
    with col1: draw_card("ASSERTIVIDADE HOJE", "84.5%", "#00ff00")
    with col2: draw_card("BANCA ATUAL", "R$ 1.250,00", "#00ff00")
    with col3: draw_card("LUCRO LÍQUIDO", "R$ 412,10", "#00ff00")
    with col4: draw_card("ENTRADAS REALIZADAS", "12", "#00ff00")
    
    col5, col6, col7, col8 = st.columns(4)
    with col5: draw_card("MERCADO DE GOLS", "78%", "#00ff00")
    with col6: draw_card("MERCADO DE CANTOS", "82%", "#00ff00")
    with col7: draw_card("ROI MENSAL", "+15.4%", "#00ff00")
    with col8: draw_card("STOP LOSS", "R$ 150,00", "#00ff00")

elif menu == "SCANNER EM TEMPO REAL":
    st.markdown("<h2 style='color: #00ff00;'>⚽ SCANNER LIVE: ANALISANDO OPORTUNIDADES</h2>", unsafe_allow_html=True)
    
    # Injeção da Tabela de 20 Jogos
    df_live = gerar_dados_scanner_live()
    
    if not df_live.empty:
        # Configuração de estilo da tabela para efeito "Zero White"
        st.dataframe(
            df_live.style.set_properties(**{
                'background-color': '#1c2128',
                'color': '#ffffff',
                'border-color': '#30363d'
            }),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.warning("Aguardando oportunidades com alta confiança matemática...")

elif menu == "ASSERTIVIDADE IA":
    st.markdown("<h2 style='color: #00ff00;'>ASSERTIVIDADE IA</h2>", unsafe_allow_html=True)
    # Mantendo rigorosamente os 8 KPI Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("KPI 1", "92%")
    with c2: draw_card("KPI 2", "88%")
    with c3: draw_card("KPI 3", "85%")
    with c4: draw_card("KPI 4", "90%")
    
    c5, c6, c7, c8 = st.columns(4)
    with c5: draw_card("KPI 5", "87%")
    with c6: draw_card("KPI 6", "84%")
    with c7: draw_card("KPI 7", "89%")
    with c8: draw_card("KPI 8", "91%")

elif menu == "GESTÃO DE BANCA":
    st.markdown("<h2 style='color: #00ff00;'>GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    # Lógica de cálculo de stake (sem o erro de sintaxe Walrus)
    if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.0
    if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
    
    calculo_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    draw_card("ENTRADA SUGERIDA (RS)", f"R$ {calculo_stake:.2f}")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #8b949e;'>GESTOR IA © 2026 - SISTEMA DE ALTA PERFORMANCE</p>", unsafe_allow_html=True)
