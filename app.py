import streamlit as st
import pandas as pd
import time

# PROTOCOLO DE APARÊNCIA IMUTÁVEL - CSS E HEADER
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    /* Preservação total do padrão Zero White */
    [data-testid="stSidebar"] {
        background-color: #000000;
        border-right: 1px solid #1E1E1E;
    }
    .main {
        background-color: #000000;
    }
    .kpi-card {
        background-color: #111111;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #1E1E1E;
        text-align: center;
    }
    .kpi-label {
        color: #888888;
        font-size: 12px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    .kpi-value {
        color: #00FF00;
        font-size: 24px;
        font-weight: bold;
    }
    .status-online {
        color: #00FF00;
        font-weight: bold;
    }
    /* Estilo específico para o Scanner Live solicitado */
    .scanner-table {
        width: 100%;
        border-collapse: collapse;
        background-color: #000000;
    }
    .scanner-header {
        color: #888888;
        text-transform: uppercase;
        font-size: 13px;
        border-bottom: 1px solid #1E1E1E;
        padding: 10px;
        text-align: left;
    }
    .scanner-row {
        border-bottom: 1px solid #1E1E1E;
    }
    .time-red {
        color: #FF0000;
        font-weight: bold;
    }
    .match-text {
        color: #FFFFFF;
        font-weight: 500;
    }
    .score-box {
        background-color: #111111;
        color: #FFFFFF;
        padding: 5px 10px;
        border-radius: 5px;
        border: 1px solid #333333;
    }
    .conf-green {
        color: #00FF00;
        font-weight: bold;
    }
    </style>
    
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0px;">
        <div style="display: flex; align-items: center;">
            <span style="color: #FFFFFF; font-size: 24px; font-weight: bold;">GESTOR IA</span>
            <span style="color: #00FF00; font-size: 18px; font-weight: bold; margin-left: 10px;">v60.00</span>
        </div>
        <div style="color: #FFFFFF; font-size: 14px;">
            STATUS DO SISTEMA: <span class="status-online">● ONLINE</span>
        </div>
    </div>
    <hr style="border: 0; border-top: 1px solid #1E1E1E; margin: 10px 0;">
""", unsafe_allow_html=True)

# INICIALIZAÇÃO DO ESTADO DA SESSÃO (LOGICA BACK-END)
if 'banca_total' not in st.session_state:
    st.session_state.banca_total = 1250.00
if 'stake_padrao' not in st.session_state:
    st.session_state.stake_padrao = 1.0
if 'aba_atual' not in st.session_state:
    st.session_state.aba_atual = "DASHBOARD PRINCIPAL"

# CORREÇÃO DO ERRO DE SINTAXE (IMAGEM 1)
# O cálculo da stake agora é feito fora da instrução with para evitar SyntaxError
k7_val = (st.session_state.banca_total * st.session_state.stake_padrao / 100)

# SIDEBAR FIXA
with st.sidebar:
    st.markdown('<p style="color: #00FF00; font-weight: bold; margin-top: 20px;">NAVEGAÇÃO</p>', unsafe_allow_html=True)
    
    if st.button("📊 DASHBOARD PRINCIPAL", use_container_width=True):
        st.session_state.aba_atual = "DASHBOARD PRINCIPAL"
    if st.button("⚽ SCANNER EM TEMPO REAL", use_container_width=True):
        st.session_state.aba_atual = "SCANNER EM TEMPO REAL"
    if st.button("💰 GESTÃO DE BANCA", use_container_width=True):
        st.session_state.aba_atual = "GESTÃO DE BANCA"
    if st.button("⚙️ CONFIGURAÇÕES", use_container_width=True):
        st.session_state.aba_atual = "CONFIGURAÇÕES"
    
    st.markdown("---")
    st.markdown(f"**Stake Atual: R$ {k7_val:.2f}**")
    st.info("Bot Operando em Segundo Plano")

# FUNÇÃO PARA DESENHAR CARDS DO DASHBOARD
def draw_card(label, value, is_roi=False):
    color = "#00FF00" if "+" in str(value) or "%" in str(value) else "#00FF00"
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value" style="color: {color};">{value}</div>
        </div>
    """, unsafe_allow_html=True)

# LÓGICA DE EXIBIÇÃO POR ABA
if st.session_state.aba_atual == "DASHBOARD PRINCIPAL":
    # MANTENDO OS 8 KPI CARDS CONFORME PROTOCOLO
    col1, col2, col3, col4 = st.columns(4)
    with col1: draw_card("ASSERTIVIDADE HOJE", "84.5%")
    with col2: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}")
    with col3: draw_card("LUCRO LÍQUIDO", "R$ 412,10")
    with col4: draw_card("ENTRADAS REALIZADAS", "12")
    
    col5, col6, col7, col8 = st.columns(4)
    with col5: draw_card("MERCADO DE GOLS", "78%")
    with col6: draw_card("MERCADO DE CANTOS", "82%")
    with col7: draw_card("ROI MENSAL", "+15.4%")
    with col8: draw_card("STOP LOSS", "R$ 150,00")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('### ⚽ JOGOS AO VIVO AGORA <span style="float: right; font-size: 12px; color: #888;">Sincronizado via IA</span>', unsafe_allow_html=True)
    
    # Exemplo rápido na Home
    st.markdown("""
        <table class="scanner-table">
            <tr class="scanner-row">
                <td style="padding: 15px;"><span class="time-red">34'</span></td>
                <td class="match-text">Flamengo vs Palmeiras</td>
                <td><span class="score-box">1 - 1</span></td>
                <td style="color: #888;">Over 2.5</td>
                <td><span class="conf-green">89%</span></td>
            </tr>
        </table>
    """, unsafe_allow_html=True)

elif st.session_state.aba_atual == "SCANNER EM TEMPO REAL":
    st.markdown('### ⚽ SCANNER LIVE: ANALISANDO OPORTUNIDADES <span style="color: #00FF00; font-size: 14px; margin-left: 20px;">● SCANNER ATIVO: CONECTADO ÀS CASAS</span>', unsafe_allow_html=True)
    
    # ESTRUTURA DO SCANNER LIVE (BASEADO NAS IMAGENS 4, 5 e 6)
    html_scanner = """
    <table class="scanner-table">
        <thead>
            <tr>
                <th class="scanner-header">TEMPO</th>
                <th class="scanner-header">PARTIDA</th>
                <th class="scanner-header">PLACAR</th>
                <th class="scanner-header">MERCADO</th>
                <th class="scanner-header">CONF. IA</th>
            </tr>
        </thead>
        <tbody>
            <tr class="scanner-row">
                <td style="padding: 15px;"><span class="time-red">34'</span></td>
                <td class="match-text">Flamengo vs Palmeiras</td>
                <td><span class="score-box">1 - 1</span></td>
                <td style="color: #FFFFFF;">Over 2.5</td>
                <td><span class="conf-green">89%</span></td>
            </tr>
            <tr class="scanner-row">
                <td style="padding: 15px;"><span class="time-red">12'</span></td>
                <td class="match-text">Real Madrid vs Milan</td>
                <td><span class="score-box">0 - 0</span></td>
                <td style="color: #FFFFFF;">Cantos HT</td>
                <td><span class="conf-green">74%</span></td>
            </tr>
            <tr class="scanner-row">
                <td style="padding: 15px;"><span class="time-red">78'</span></td>
                <td class="match-text">Liverpool vs Bayer Leverkusen</td>
                <td><span class="score-box">2 - 0</span></td>
                <td style="color: #FFFFFF;">Under 3.5</td>
                <td><span class="conf-green">92%</span></td>
            </tr>
            <tr class="scanner-row">
                <td style="padding: 15px;"><span class="time-red">61'</span></td>
                <td class="match-text">Sporting vs Man. City</td>
                <td><span class="score-box">1 - 2</span></td>
                <td style="color: #FFFFFF;">Próximo Gol</td>
                <td><span class="conf-green">81%</span></td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(html_scanner, unsafe_allow_html=True)

elif st.session_state.aba_atual == "GESTÃO DE BANCA":
    st.markdown("### 💰 GESTÃO DE BANCA")
    st.write("Módulo de gerenciamento de risco e histórico de apostas.")

elif st.session_state.aba_atual == "CONFIGURAÇÕES":
    st.markdown("### ⚙️ CONFIGURAÇÕES DO SISTEMA")
    st.session_state.stake_padrao = st.slider("Definir Stake Padrão (%)", 0.1, 5.0, st.session_state.stake_padrao)
