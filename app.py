import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

# CONFIGURAÇÃO DE PÁGINA (IMUTÁVEL)
st.set_page_config(page_title="JARVIS v65.5", layout="wide")

# ESTILO ZERO WHITE PRO
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background-color: #0b0e11; color: white; }
    .card-live {
        background: linear-gradient(145deg, #161a1e, #1c2126);
        border-radius: 10px; padding: 15px; border: 1px solid #2d3439; margin-bottom: 10px;
    }
    .score { font-size: 22px; color: #00ff88; font-weight: bold; }
    .team { font-size: 14px; font-weight: bold; text-transform: uppercase; }
</style>
""", unsafe_allow_html=True)

def buscar_dados_vivos():
    # TENTATIVA 1: LER O SEU ARQUIVO DO GITHUB
    try:
        # Forçamos o link a ser ÚNICO a cada segundo para o GitHub não nos enganar
        url_csv = f"https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/base_jogos_jarvis.csv?nocache={int(time.time())}"
        df = pd.read_csv(url_csv)
        if not df.empty and len(df) > 1:
            return df
    except:
        pass

    # TENTATIVA 2: BUSCA DIRETA (EMERGÊNCIA)
    # Se o arquivo CSV falhar, o próprio App vai no site buscar os 11 jogos
    jogos = []
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get("https://pt.besoccer.com/livescore", headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        links = soup.find_all('a', class_='match-link')
        for l in links[:12]:
            try:
                t = l.find_all('div', class_='team-name')
                m = l.find('div', class_='marker').text.strip().split('-')
                jogos.append({"HOME": t[0].text.strip(), "AWAY": t[1].text.strip(), 
                              "PLACAR_HOME": m[0], "PLACAR_AWAY": m[1], "MINUTO": "VIVO", "AP1": "60"})
            except: continue
    except: pass
    return pd.DataFrame(jogos)

# INTERFACE
st.title("📡 SCANNER JARVIS v65.5")
st.sidebar.write(f"Última tentativa: {datetime.now().strftime('%H:%M:%S')}")

# Botão que realmente funciona (Força o reinício do script)
if st.button("🚀 ATUALIZAR AGORA E BUSCAR JOGOS"):
    st.cache_data.clear() # Limpa a memória do Streamlit
    st.rerun()

dados = buscar_dados_vivos()

if dados.empty:
    st.error("ERRO DE CONEXÃO: O GitHub ainda não liberou os dados. Tente novamente em 1 minuto.")
else:
    st.success(f"CONECTADO! Exibindo {len(dados)} jogos encontrados.")
    cols = st.columns(4)
    for i, (_, j) in enumerate(dados.iterrows()):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="card-live">
                <div style="color:red; font-size:10px;">● AO VIVO {j['MINUTO']}</div>
                <div class="team">{j['HOME']}</div>
                <div class="score">{j['PLACAR_HOME']} - {j['PLACAR_AWAY']}</div>
                <div class="team">{j['AWAY']}</div>
                <div style="font-size:11px; color:gray;">PRESSÃO: {j['AP1']}%</div>
            </div>
            """, unsafe_allow_html=True)
