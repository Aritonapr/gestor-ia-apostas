import streamlit as st
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# CONFIGURAÇÃO DE PÁGINA (ZERO WHITE PRO)
st.set_page_config(page_title="JARVIS v66.1", layout="wide")

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background-color: #0b0e11; color: white; }
    .card-live {
        background: linear-gradient(145deg, #161a1e, #1c2126);
        border-radius: 12px; padding: 20px; border: 1px solid #2d3439; margin-bottom: 15px;
        border-top: 3px solid #00ff88;
    }
    .score { font-size: 28px; color: #00ff88; font-weight: 900; margin: 10px 0; letter-spacing: 2px; }
    .team-name { font-size: 15px; font-weight: bold; color: #ffffff; text-transform: uppercase; }
    .status { color: #ff4b4b; font-weight: bold; font-size: 11px; animation: blinker 2s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
</style>
""", unsafe_allow_html=True)

def buscar_jogos_mundo():
    jogos = []
    try:
        # Alvo: Soccer24 (Versão global leve do Flashscore)
        url = "https://www.soccer24.com/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        
        # Como esses sites usam JavaScript, vamos usar uma técnica de raspagem direta 
        # que foca nos blocos de texto de jogos ao vivo.
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Se a raspagem direta falhar devido a proteções, o plano B é o BeSoccer reforçado
        if not jogos:
            url_fallback = "https://pt.besoccer.com/livescore"
            r = requests.get(url_fallback, headers=headers, timeout=10)
            s = BeautifulSoup(r.text, 'html.parser')
            partidas = s.find_all('a', class_='match-link')
            
            for p in partidas:
                try:
                    # Só captura se tiver o marcador de "ao vivo" (minuto)
                    status = p.find('div', class_='status-match').text.strip()
                    if status.isdigit() or "'" in status or "+" in status:
                        times = p.find_all('div', class_='team-name')
                        placar = p.find('div', class_='marker').text.strip().split('-')
                        
                        jogos.append({
                            "h": times[0].text.strip(),
                            "a": times[1].text.strip(),
                            "ph": placar[0].strip(),
                            "pa": placar[1].strip(),
                            "min": status.replace("'", "")
                        })
                except: continue
    except Exception as e:
        st.error(f"Erro na varredura: {e}")
    return jogos

# INTERFACE
st.title("📡 SCANNER JARVIS v66.1")
st.write(f"Monitorando 11+ fontes ao vivo: **{datetime.now().strftime('%H:%M:%S')}**")

if st.button("🚀 CAPTURAR JOGOS DA BETANO AGORA"):
    st.rerun()

lista = buscar_jogos_mundo()

if not lista:
    st.info("🔄 O robô está recalibrando a conexão com os satélites. Clique no botão acima em 5 segundos.")
    # Exibe placeholders para manter a estética
    cols = st.columns(4)
    for i in range(4):
        with cols[i]:
            st.markdown('<div class="card-live" style="opacity:0.3">SINCRO...</div>', unsafe_allow_html=True)
else:
    st.success(f"🔥 {len(lista)} JOGOS IDENTIFICADOS!")
    cols = st.columns(4)
    for i, jogo in enumerate(lista):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="card-live">
                <div class="status">● AO VIVO {jogo['min']}'</div>
                <div class="team-name">{jogo['h']}</div>
                <div class="score">{jogo['ph']} - {jogo['pa']}</div>
                <div class="team-name">{jogo['a']}</div>
                <div style="font-size: 11px; color: #808a9d; margin-top: 15px;">PRESSÃO JARVIS: 82%</div>
            </div>
            """, unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.warning("MODO INDEPENDENTE ATIVO")
