import streamlit as st
import pandas as pd
import numpy as np

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA - DASHBOARD", layout="wide", initial_sidebar_state="expanded")

# --- ESTILO CSS (PRESERVAÇÃO DO PADRÃO ZERO WHITE) ---
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
    /* Estilização da Tabela para efeito bonito e sem fundo branco */
    .stDataFrame {
        border: 1px solid #30363d;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÕES DE INTERFACE (ESTRUTURA FIXA) ---
def draw_header():
    st.markdown("""
    <div class="main-header">
        <h1 style='color: #ffd700; margin: 0;'>GESTOR IA v59.00</h1>
        <p style='color: #8b949e; margin: 0;'>SISTEMA AVANÇADO DE ANÁLISE PREDIRETA</p>
    </div>
    """, unsafe_allow_html=True)

def draw_card(title, value, delta=None):
    with st.container():
        st.markdown(f"""
        <div class="kpi-card">
            <p style='color: #8b949e; font-size: 14px; margin-bottom: 5px;'>{title}</p>
            <h2 style='color: #ffffff; margin: 0;'>{value}</h2>
        </div>
        """, unsafe_allow_html=True)

# --- LÓGICA DO BOT (BACK-END INVISÍVEL) ---
def processar_dados_scanner():
    """
    Simula o processamento de IA para identificar jogos com 
    probabilidade real e matemática de ocorrência.
    """
    # Exemplo de 20 jogos processados pelo motor de assertividade
    dados = []
    for i in range(20):
        # Lógica de filtragem: apenas eventos com prob > 70%
        prob_vitoria = np.random.randint(40, 95)
        if prob_vitoria > 70:
            dados.append({
                "Partida": f"Time A vs Time B {i+1}",
                "Prob. Vencedor": f"{prob_vitoria}%",
                "Gols (1T/2T)": "1.5+ (Ambos)",
                "Cartões (1T/2T/Total)": f"{np.random.randint(1,3)} / {np.random.randint(2,4)} / {np.random.randint(3,7)}",
                "Cantos (Time/Total)": f"L:5 V:4 / Total: 9",
                "Tiros de Meta": f"12 (6/6)",
                "Chutes ao Gol": f"8 (4/4)",
                "Defesas Goleiro": f"5 (3/2)"
            })
    return pd.DataFrame(dados)

# --- SIDEBAR E NAVEGAÇÃO ---
with st.sidebar:
    st.image("https://via.placeholder.com/150x50?text=GESTOR+IA", use_column_width=True)
    st.markdown("---")
    menu = st.radio("NAVEGAÇÃO", ["MERCADO DE GOLS", "MERCADO DE CANTOS", "SCANNER EM TEMPO REAL", "ASSERTIVIDADE IA", "GESTÃO DE BANCA"])

# --- CONTEÚDO PRINCIPAL ---
draw_header()

if menu == "SCANNER EM TEMPO REAL":
    # Linha de Cards Existentes (Estrutura Fixa)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        draw_card("JOGOS ANALISADOS", "142")
    with col2:
        draw_card("ALERTAS ATIVOS", "12")
    with col3:
        draw_card("MÉDIA DE ODDS", "1.85")
    with col4:
        draw_card("CONFIANÇA IA", "88%")

    st.markdown("---")
    st.subheader("📊 ANÁLISE PROBABILÍSTICA - LIVE (20 JOGOS SELECIONADOS)")

    # Injeção da Tabela de Dados (Saída do Bot)
    df_scanner = processar_dados_scanner()
    
    if not df_scanner.empty:
        # Estilização da tabela para manter o padrão escuro e remover fundo branco
        st.dataframe(
            df_scanner,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("O Bot está aguardando oportunidades com alta probabilidade matemática.")

elif menu == "ASSERTIVIDADE IA":
    # Mantendo os 8 KPI Cards conforme regra anterior
    cols = st.columns(4)
    for i in range(8):
        with cols[i % 4]:
            draw_card(f"MÉTRICA {i+1}", f"{85 + i}%")

elif menu == "GESTÃO DE BANCA":
    st.markdown("### GESTÃO DE BANCA")
    # Conteúdo de gestão preservado aqui

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #30363d;'>GESTOR IA © 2026 - SISTEMA DE ALTA PERFORMANCE</p>", unsafe_allow_html=True)
