import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# ==========================================
# DIRETRIZ: APARÊNCIA IMUTÁVEL ZERO WHITE PRO
# ==========================================
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide")

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background-color: #0b0e11; color: white; }
    [data-testid="stSidebar"] { background-color: #0f1216; border-right: 1px solid #1e2229; }
    .card-live {
        background: linear-gradient(145deg, #161a1e, #1c2126);
        border-radius: 12px; padding: 20px; border: 1px solid #2d3439; margin-bottom: 15px;
        min-height: 180px;
    }
    .status-live { color: #ff4b4b; font-weight: bold; animation: blinker 2s linear infinite; font-size: 12px; }
    @keyframes blinker { 50% { opacity: 0; } }
    .team-name { font-size: 16px; font-weight: bold; margin: 5px 0; color: #ffffff; }
    .score { font-size: 24px; color: #00ff88; font-weight: 800; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# MOTOR DE BUSCA HÍBRIDO (TENTA GITHUB -> SE FALHAR, BUSCA DIRETO)
# ==========================================
def buscar_dados_agora():
    jogos_finais = []
    
    # Tentativa 1: Ler do seu GitHub (Onde o robô salva)
    try:
        url_git = f"https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/base_jogos_jarvis.csv?v={datetime.now().timestamp()}"
        df = pd.read_csv(url_git)
        if not df.empty:
            for _, row in df.iterrows():
                jogos_finais.append({
                    "home": row['HOME'], "away": row['AWAY'],
                    "placar_h": row['PLACAR_HOME'], "placar_a": row['PLACAR_AWAY'],
                    "minuto": row['MINUTO'], "ap1": row['AP1']
                })
            return jogos_finais
    except:
        pass

    # Tentativa 2: Busca Direta (Plano B Emergencial se o GitHub demorar)
    try:
        url_bs = "https://pt.besoccer.com/livescore"
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url_bs, headers=headers, timeout=10)
        soup = BeautifulSoup(resp.text, 'html.parser')
        partidas = soup.find_all('a', class_='match-link')
        
        for p in partidas[:12]: # Pega os 12 primeiros ao vivo
            try:
                times = p.find_all('div', class_='team-name')
                placar = p.find('div', class_='marker').text.strip().split('-')
                jogos_finais.append({
                    "home": times[0].text.strip(), "away": times[1].text.strip(),
                    "placar_h": placar[0], "placar_a": placar[1],
                    "minuto": "VIVO", "ap1": "60"
                })
            except: continue
    except:
        pass
        
    return jogos_finais

# ==========================================
# INTERFACE
# ==========================================
st.title("📡 SCANNER EM TEMPO REAL")
st.write(f"Sincronizado em: {datetime.now().strftime('%H:%M:%S')}")

if st.button("🔄 FORÇAR ATUALIZAÇÃO"):
    st.rerun()

dados = buscar_dados_agora()

if not dados:
    st.warning("⚠️ CONECTANDO AOS SERVIDORES DE JOGOS... AGUARDE UM INSTANTE.")
    cols = st.columns(4)
    for i in range(8):
        with cols[i % 4]:
            st.markdown('<div class="card-live" style="opacity: 0.2;">BUSCANDO...</div>', unsafe_allow_html=True)
else:
    cols = st.columns(4)
    for i, j in enumerate(dados):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="card-live">
                <span class="status-live">● AO VIVO ({j['minuto']})</span>
                <div class="team-name">{j['home']}</div>
                <div class="score">{j['placar_h']} - {j['placar_a']}</div>
                <div class="team-name">{j['away']}</div>
                <hr style="border: 0.1px solid #2d3439; margin: 10px 0;">
                <p style="font-size: 11px; color: #808a9d;">PRESSÃO AP1: {j['ap1']}%</p>
            </div>
            """, unsafe_allow_html=True)

st.sidebar.title("🤖 Jarvis v65.3")
st.sidebar.info("Modo Híbrido: GitHub + BeSoccer")
