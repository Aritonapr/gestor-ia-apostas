import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO JARVIS v63.4 - ESTABILIDADE DIAMANTE]
# DIRETRIZ: ESTRUTURA PRIMEIRO, ESTILO DEPOIS (EVITA TELA PRETA)
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA (LINHA 1 OBRIGATÓRIA)
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. INICIALIZAÇÃO DE MEMÓRIA (BLINDADA)
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# 3. CARREGAMENTO DE DADOS (SEGURO)
path_data = "data/database_diario.csv"
df_diario = None
if os.path.exists(path_data):
    try:
        df_diario = pd.read_csv(path_data)
    except:
        df_diario = None

# 4. ESTRUTURA DA SIDEBAR (BOTÕES REAIS)
with st.sidebar:
    st.markdown("<h2 style='color:#9d54ff; text-align:center;'>GESTOR IA</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#475569; font-size:10px; text-align:center;'>VERSÃO v63.4 | 2026</p>", unsafe_allow_html=True)
    st.write("---")
    
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    
    st.write("---")
    st.info("🤖 Jarvis Status: Operacional")

# 5. FUNÇÃO PARA DESENHAR OS CARDS (O SEU DESIGN)
def draw_card(title, value, perc):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div>
            <div style="color:white; font-size:18px; font-weight:900; margin-top:10px;">{value}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:15px auto;">
                <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); height:100%; width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# 6. CONTEÚDO DAS TELAS
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO - MARÇO 2026</h2>", unsafe_allow_html=True)
    
    # Linha de métricas
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with c2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with c3: draw_card("SISTEMA", "JARVIS v63.4", 100)
    with c4: draw_card("STATUS", "ONLINE", 100)
    
    if df_diario is not None:
        st.markdown("<h4 style='color:#06b6d4; margin-top:20px;'>🤖 JOGOS ENCONTRADOS PELA IA</h4>", unsafe_allow_html=True)
        st.dataframe(df_diario, use_container_width=True, hide_index=True)
    else:
        st.warning("🤖 Jarvis: Aguardando sincronização de dados de 2026. Por favor, execute a Action no GitHub.")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total))
    st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, float(st.session_state.stake_padrao))
    
    v_entrada = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    draw_card("VALOR POR OPERAÇÃ
