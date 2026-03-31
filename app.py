import streamlit as st
import pandas as pd
from datetime import datetime
import time

st.set_page_config(page_title="JARVIS v65.4", layout="wide")

# CSS ZERO WHITE PRO
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background-color: #0b0e11; color: white; }
    .card-live {
        background: linear-gradient(145deg, #161a1e, #1c2126);
        border-radius: 12px; padding: 20px; border: 1px solid #2d3439; margin-bottom: 15px;
    }
    .team-name { font-size: 16px; font-weight: bold; color: #ffffff; }
    .score { font-size: 26px; color: #00ff88; font-weight: 900; }
</style>
""", unsafe_allow_html=True)

def carregar_dados():
    # O segredo do tempo real: timestamp no final da URL para evitar cache
    url = f"https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/base_jogos_jarvis.csv?t={int(time.time())}"
    try:
        return pd.read_csv(url)
    except:
        return pd.DataFrame()

st.title("📡 SCANNER REAL-TIME")

if st.button("🔄 FORÇAR ATUALIZAÇÃO AGORA"):
    st.rerun()

df = carregar_dados()

if df.empty or (len(df) == 1 and df['HOME'].iloc[0] == "BUSCANDO"):
    st.warning("O robô está processando os 11 jogos... Aguarde 30 segundos e aperte o botão acima.")
else:
    cols = st.columns(4)
    for i, (_, jogo) in enumerate(df.iterrows()):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="card-live">
                <div style="color: #ff4b4b; font-size: 10px;">● AO VIVO {jogo['MINUTO']}'</div>
                <div class="team-name">{jogo['HOME']}</div>
                <div class="score">{jogo['PLACAR_HOME']} - {jogo['PLACAR_AWAY']}</div>
                <div class="team-name">{jogo['AWAY']}</div>
                <div style="margin-top:10px; font-size:11px; color:#808a9d;">PRESSÃO: {jogo['AP1']}%</div>
            </div>
            """, unsafe_allow_html=True)
