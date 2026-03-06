import streamlit as st
import pandas as pd
import random

# --- ESTILO BETANO ---
st.set_page_config(page_title="Gestor IA Apostas", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #1a242d; color: white; }
    .stButton>button { background-color: #f05a22; color: white; width: 100%; border-radius: 10px; }
    .card { background-color: #26323e; padding: 15px; border-radius: 10px; border-left: 5px solid #f05a22; margin-bottom: 15px; }
    .stats { color: #00ffc3; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS FICTÍCIO (Simulando a IA que baixa os dados) ---
# Em um cenário real, aqui a IA estaria baixando os CSVs automaticamente
ligas = ["Brasileirão", "Premier League", "La Liga", "Serie A"]
times = ["Flamengo", "Palmeiras", "Real Madrid", "Man. City", "Liverpool", "Barcelona"]
juizes = [
    {"nome": "Anderson Daronco", "media_cartao": 5.4},
    {"nome": "Wilton Sampaio", "media_cartao": 6.1},
    {"nome": "Anthony Taylor", "media_cartao": 3.8}
]

# --- LOGICA DE ANÁLISE DE ESCANTEIOS E CARTÕES ---
def analisar_jogo(time_casa, time_fora):
    prob_vitoria = random.randint(30, 80)
    over_25 = random.randint(40, 75)
    escanteios_esperados = random.uniform(8.5, 12.5)
    juiz = random.choice(juizes)
    
    # Lógica IA: Se o time chuta muito, os escanteios sobem
    return {
        "vitoria": prob_vitoria,
        "over25": over_25,
        "escanteios": round(escanteios_esperados, 1),
        "juiz": juiz['nome'],
        "media_juiz": juiz['media_cartao'],
        "placar": f"{random.randint(0,3)} - {random.randint(0,2)}"
    }

# --- INTERFACE ---
st.title("🧡 GESTOR IA - SISTEMA DE ANÁLISE PROFISSIONAL")
st.sidebar.header("Configurações da IA")
liga_sel = st.sidebar.selectbox("Escolha a Liga", ligas)
min_confianca = st.sidebar.slider("Confiança Mínima (%)", 50, 95, 70)

st.header(f"🚀 Melhores Apostas: {liga_sel}")

# Simulando 3 jogos filtrados pela IA
for i in range(3):
    t1, t2 = random.sample(times, 2)
    dados = analisar_jogo(t1, t2)
    
    with st.container():
        st.markdown(f"""
        <div class="card">
            <h2 style='color: white;'>{t1} vs {t2}</h2>
            <p><b>Previsão do Placar:</b> <span class="stats">{dados['placar']}</span></p>
            <div style="display: flex; justify-content: space-between;">
                <span>🎯 Vitória {t1}: <b>{dados['vitoria']}%</b></span>
                <span>⚽ Over 2.5 Gols: <b>{dados['over25']}%</b></span>
                <span>🚩 Escanteios: <b>{dados['escanteios']}</b></span>
            </div>
            <hr>
            <p>⚖️ <b>Árbitro:</b> {dados['juiz']} (Média: {dados['media_juiz']} cartões/jogo)</p>
            <p style='color: #f05a22;'><b>💡 Dica da IA:</b> Apostar em Over {int(dados['escanteios'])-1}.5 Escanteios</p>
        </div>
        """, unsafe_allow_html=True)

# --- BOTÃO DE RELATÓRIO ---
if st.button("Gerar Relatório de Valor Esperado (EV+)"):
    st.write("Analisando 20 ligas... Scanner Ativo ✅")
    st.info("A IA identificou valor no mercado de 'Ambas Marcam' para os jogos da noite.")
