import streamlit as st
import pandas as pd
from datetime import datetime
import time

# ==========================================
# CONFIGURAÇÃO VISUAL ZERO WHITE PRO
# ==========================================
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    /* PRESERVAÇÃO DO CSS ORIGINAL JARVIS */
    [data-testid="stAppViewContainer"] { background-color: #0b0e11; color: white; }
    [data-testid="stSidebar"] { background-color: #0f1216; border-right: 1px solid #1e2229; }
    .stMetric { background-color: #161a1e; padding: 15px; border-radius: 10px; border: 1px solid #2d3439; }
    
    /* CARD DESIGN PRO */
    .card-live {
        background: linear-gradient(145deg, #161a1e, #1c2126);
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #2d3439;
        margin-bottom: 15px;
        transition: transform 0.3s ease;
    }
    .card-live:hover { transform: translateY(-5px); border-color: #00ff88; }
    .live-tag { color: #ff4b4b; font-weight: bold; font-size: 12px; }
    .timer { float: right; color: #808a9d; font-size: 12px; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# LÓGICA DE DADOS REAIS (30/03/2026)
# ==========================================
def carregar_dados_reais():
    try:
        # Tenta ler o arquivo sincronizado pelo GitHub Actions
        df = pd.read_csv('base_jogos_jarvis.csv') 
        
        # Converte a data para garantir a comparação correta
        hoje = "2026-03-30" 
        df_hoje = df[df['DATA'] == hoje]
        
        return df_hoje
    except:
        # Se o arquivo não existir ou estiver vazio, retorna um DataFrame vazio
        return pd.DataFrame()

# ==========================================
# INTERFACE DO SCANNER (20 SLOTS)
# ==========================================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2586/2586488.png", width=50)
st.sidebar.title("GESTOR IA")

menu = st.sidebar.radio("Navegação", ["🎯 SCANNER PRÉ-LIVE", "📡 SCANNER EM TEMPO REAL", "💰 GESTÃO DE BANCA"])

if menu == "📡 SCANNER EM TEMPO REAL":
    st.title("📡 SCANNER EM TEMPO REAL (20 JOGOS)")
    
    jogos_hoje = carregar_dados_reais()
    
    if jogos_hoje.empty:
        st.warning("⚠️ NENHUM JOGO AO VIVO ENCONTRADO PARA HOJE (30/03/2026).")
        st.info("Aguardando sincronização do GitHub Actions com o Placar de Futebol...")
    else:
        # Grade de 20 Slots (4 colunas x 5 linhas)
        cols = st.columns(4)
        
        # Itera sobre os jogos reais (limitado a 20)
        for i, (index, jogo) in enumerate(jogos_hoje.head(20).iterrows()):
            with cols[i % 4]:
                st.markdown(f"""
                <div class="card-live">
                    <span class="live-tag">● AO VIVO</span>
                    <span class="timer">{jogo['MINUTO']}'</span>
                    <h4 style="margin: 10px 0;">{jogo['HOME']} vs {jogo['AWAY']}</h4>
                    <h2 style="color: #00ff88;">{jogo['PLACAR_HOME']} - {jogo['PLACAR_AWAY']}</h2>
                    <p style="font-size: 12px; color: #808a9d;">PRESSÃO (AP1): {jogo['AP1']}%</p>
                    <div style="background: #2d3439; height: 4px; border-radius: 2px;">
                        <div style="background: #00ff88; width: {jogo['AP1']}%; height: 100%; border-radius: 2px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"ANALISAR {i+1}", key=f"btn_{i}"):
                    st.session_state.jogo_selecionado = jogo['HOME']

# ==========================================
# RODAPÉ STATUS
# ==========================================
st.markdown("---")
st.caption(f"STATUS: ● IA OPERACIONAL | v62.3 | DATA: 30/03/2026 | JOGOS HOJE: {len(jogos_hoje)}")
