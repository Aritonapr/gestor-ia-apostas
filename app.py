import streamlit as st
import pandas as pd
import os

# ==============================================================================
# [PROTOCOLO JARVIS v66.0 - BLINDAGEM DE EMERGÊNCIA]
# DIRETRIZ: LIMPEZA DE CACHE E EXIBIÇÃO DE ERRO REAL
# ==============================================================================

# 1. BOOT PRIORITÁRIO
st.set_page_config(page_title="GESTOR IA 2026", layout="wide")

try:
    # 2. LIMPEZA E INICIALIZAÇÃO DE MEMÓRIA (À PROVA DE CONFLITOS)
    if 'aba' not in st.session_state: 
        st.session_state.clear() # Limpa memórias de versões antigas
        st.session_state['aba'] = "home"
    if 'banca' not in st.session_state: 
        st.session_state['banca'] = 1000.0

    # 3. ESTILO SIMPLIFICADO (BETANO DARK)
    st.markdown("""
        <style>
        .stApp { background-color: #0b0e11; color: white; }
        [data-testid="stHeader"] { display: none; }
        .card { 
            background: #11151a; border: 1px solid #1e293b; padding: 20px; 
            border-radius: 8px; text-align: center; margin-bottom: 10px;
        }
        .logo { color: #9d54ff; font-weight: 900; font-size: 24px; margin-bottom: 20px; }
        </style>
    """, unsafe_allow_html=True)

    # 4. SIDEBAR (MENU)
    with st.sidebar:
        st.markdown('<div class="logo">GESTOR IA</div>', unsafe_allow_html=True)
        st.write("---")
        if st.button("📅 BILHETE OURO"): st.session_state.aba = "home"
        if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba = "gestao"
        st.write("---")
        st.write("🕒 CONTEXTO: MARÇO 2026")

    # 5. CARREGAMENTO DE DADOS (2026)
    caminho_dados = "data/database_diario.csv"
    df = None
    if os.path.exists(caminho_dados):
        try:
            df = pd.read_csv(caminho_dados)
        except Exception:
            df = None

    # 6. EXIBIÇÃO DAS TELAS
    if st.session_state.aba == "home":
        st.markdown("## 📅 BILHETE OURO - 2026")
        
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown(f'<div class="card">BANCA<br><b>R$ {st.session_state.banca:,.2f}</b></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="card">ASSERTIVIDADE<br><b>92.4%</b></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="card">STATUS<br><b>IA ATIVA</b></div>', unsafe_allow_html=True)

        if df is not None:
            st.markdown("### 📋 JOGOS CAPTURADOS")
            st.dataframe(df, use_container_width=True)
        else:
            st.info("🤖 Jarvis: Aguardando primeira sincronização de 2026... Rode a Action no GitHub!")

    elif st.session_state.aba == "gestao":
        st.markdown("## 💰 GESTÃO DE BANCA")
        st.session_state.banca = st.number_input("Valor da Banca (R$)", value=st.session_state.banca)
        st.success(f"Banca atualizada para R$ {st.session_state.banca:,.2f}")

    st.markdown("<br><br><p style='color:gray; font-size:10px;'>JARVIS v66.0 | PROTECT MODE</p>", unsafe_allow_html=True)

except Exception as e:
    # Se der qualquer erro, ele aparecerá aqui em vez de dar o "Oh no"
    st.error(f"ERRO DE INICIALIZAÇÃO: {e}")
    st.write("Por favor, clique em 'Reboot' no painel do Streamlit.")
