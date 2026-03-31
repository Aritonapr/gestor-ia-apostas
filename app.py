import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# CONFIGURAÇÃO DE PÁGINA (ESTILO ZERO WHITE PRO)
st.set_page_config(page_title="JARVIS v66.0", layout="wide")

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background-color: #0b0e11; color: white; }
    .card-live {
        background: linear-gradient(145deg, #161a1e, #1c2126);
        border-radius: 12px; padding: 20px; border: 1px solid #2d3439; margin-bottom: 15px;
        border-left: 5px solid #00ff88;
    }
    .score { font-size: 26px; color: #00ff88; font-weight: 900; margin: 10px 0; }
    .team-name { font-size: 16px; font-weight: bold; color: #ffffff; }
    .status { color: #ff4b4b; font-weight: bold; font-size: 12px; animation: blinker 2s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
</style>
""", unsafe_allow_html=True)

def buscar_jogos_agora():
    jogos_extraidos = []
    try:
        # Busca direta na fonte (Plano de Contingência Total)
        url = "https://pt.besoccer.com/livescore"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Localiza as partidas ao vivo
        partidas = soup.find_all('a', class_='match-link')
        
        for p in partidas:
            try:
                times = p.find_all('div', class_='team-name')
                placar_texto = p.find('div', class_='marker').get_text(strip=True)
                minuto = p.find('div', class_='status-match').get_text(strip=True).replace("'", "")
                
                # Só pega o que for jogo acontecendo (número ou VIVO)
                if '-' in placar_texto and (minuto.isdigit() or "+" in minuto or minuto == "VIVO"):
                    placar = placar_texto.split('-')
                    jogos_extraidos.append({
                        "home": times[0].get_text(strip=True),
                        "away": times[1].get_text(strip=True),
                        "placar_h": placar[0],
                        "placar_a": placar[1],
                        "minuto": minuto
                    })
            except: continue
    except Exception as e:
        st.error(f"Erro na fonte: {e}")
    return jogos_extraidos

# INTERFACE PRINCIPAL
st.title("📡 SCANNER JARVIS - LIVE AGORA")
st.write(f"Atualizado em: {datetime.now().strftime('%H:%M:%S')}")

if st.button("🚀 ATUALIZAR SCANNER"):
    st.rerun()

# Executa a busca
lista_jogos = buscar_jogos_agora()

if not lista_jogos:
    st.warning("⚠️ NENHUM JOGO AO VIVO ENCONTRADO NO MOMENTO. VERIFIQUE A GRADE DE JOGOS.")
else:
    st.success(f"✅ {len(lista_jogos)} JOGOS ENCONTRADOS EM TEMPO REAL!")
    cols = st.columns(4)
    for i, jogo in enumerate(lista_jogos):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="card-live">
                <div class="status">● AO VIVO {jogo['minuto']}'</div>
                <div class="team-name">{jogo['home']}</div>
                <div class="score">{jogo['placar_h']} - {jogo['placar_a']}</div>
                <div class="team-name">{jogo['away']}</div>
                <div style="font-size: 10px; color: gray; margin-top: 10px;">PRESSÃO AP1: 75%</div>
            </div>
            """, unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.info("Modo Direto: O App busca os dados sem depender do GitHub Actions.")
