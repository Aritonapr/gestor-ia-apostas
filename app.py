import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIGURAÇÃO VISUAL (MANTIDA)
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide")
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background-color: #0b0e11; color: white; }
    .card-live {
        background: linear-gradient(145deg, #161a1e, #1c2126);
        border-radius: 12px; padding: 20px; border: 1px solid #2d3439; margin-bottom: 15px;
    }
    .status-live { color: #ff4b4b; font-weight: bold; animation: blinker 2s linear infinite; font-size: 12px; }
    @keyframes blinker { 50% { opacity: 0; } }
    .team-name { font-size: 16px; font-weight: bold; margin: 5px 0; }
    .score { font-size: 24px; color: #00ff88; font-weight: 800; }
</style>
""", unsafe_allow_html=True)

def buscar_dados():
    try:
        # LINK DO SEU REPOSITÓRIO
        url = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/base_jogos_jarvis.csv"
        # Adicionamos um número aleatório no final para o navegador não "viciar" em dados velhos
        url_cache_buster = f"{url}?v={datetime.now().timestamp()}"
        df = pd.read_csv(url_cache_buster)
        return df
    except:
        return pd.DataFrame()

st.title("📡 SCANNER EM TEMPO REAL")

if st.button("🔄 REFRESH DADOS"):
    st.rerun()

df_jogos = buscar_dados()

if df_jogos.empty:
    st.error("⚠️ O ARQUIVO AINDA NÃO FOI ATUALIZADO NO GITHUB.")
else:
    cols = st.columns(4)
    # Mostra os jogos que o BeSoccer capturou
    for i, (idx, jogo) in enumerate(df_jogos.iterrows()):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="card-live">
                <span class="status-live">● AO VIVO ({jogo['MINUTO']}')</span>
                <div class="team-name">{jogo['HOME']}</div>
                <div class="score">{jogo['PLACAR_HOME']} - {jogo['PLACAR_AWAY']}</div>
                <div class="team-name">{jogo['AWAY']}</div>
                <hr style="border: 0.1px solid #2d3439">
                <p style="font-size: 11px; color: #808a9d;">PRESSÃO AP1: {jogo['AP1']}%</p>
            </div>
            """, unsafe_allow_html=True)

st.caption(f"Última sincronização: {datetime.now().strftime('%H:%M:%S')}")
