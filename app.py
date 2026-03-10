import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="GIAE - Gestor IA", layout="wide")

# --- CSS AVANÇADO (Design, Logo e Fundo) ---
st.markdown("""
    <style>
    /* 1. Fundo da Aplicação */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #ffffff;
    }

    /* 2. Estilização do Logo "GIAE" */
    .logo-container {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 20px;
        padding: 10px;
    }
    .logo-box {
        background: linear-gradient(45deg, #3b82f6, #2563eb);
        color: white;
        font-family: 'Arial Black', sans-serif;
        font-size: 35px;
        padding: 5px 15px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.5);
        letter-spacing: 2px;
    }
    .logo-text {
        font-size: 28px;
        font-weight: 800;
        color: #f8fafc;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* 3. Botões Personalizados */
    div.stButton > button {
        width: 100%;
        height: 85px;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.05);
        color: #e2e8f0;
        font-weight: 700;
        font-size: 14px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        text-transform: uppercase;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    div.stButton > button:hover {
        background: linear-gradient(45deg, #3b82f6, #1d4ed8);
        color: white;
        border: none;
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(37, 99, 235, 0.4);
    }

    /* 4. Tabela e Containers */
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.03);
        padding: 15px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* 5. Títulos de Seção */
    .section-title {
        color: #60a5fa;
        font-size: 14px;
        font-weight: 700;
        margin-bottom: 10px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    hr {
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(255,255,255,0), rgba(255,255,255,0.5), rgba(255,255,255,0));
        margin: 30px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER COM LOGO ---
st.markdown("""
    <div class="logo-container">
        <div class="logo-box">GIAE</div>
        <div class="logo-text">Gestor IA Aposta Esportiva</div>
    </div>
    """, unsafe_allow_html=True)

# --- DADOS FICTÍCIOS ---
dados = [
    {"Jogo": "Real Madrid vs Man City", "Liga": "Europa", "IA": "88%", "Odd": 1.95},
    {"Jogo": "Flamengo vs Palmeiras", "Liga": "America do Sul", "IA": "65%", "Odd": 1.80},
    {"Jogo": "Brasil vs Argentina", "Liga": "UEFA / INTER", "IA": "72%", "Odd": 2.10},
]
df = pd.DataFrame(dados)

# --- GRID DE COMANDOS ---
col1, col2, col3, col4 = st.columns([1, 1.2, 1.2, 1])

with col1:
    st.markdown('<p class="section-title">📂 CATEGORIAS</p>', unsafe_allow_html=True)
    if st.button("🏆 CAMPEONATOS"): pass
    st.write("")
    if st.button("🇪🇺 EUROPA"): pass
    st.write("")
    if st.button("🌍 UEFA / INTER"): pass
    st.write("")
    if st.button("🌎 AMERICA DO SUL"): pass

with col2:
    st.markdown('<p class="section-title">⚡ PROCESSAMENTO</p>', unsafe_allow_html=True)
    if st.button("🤖 PROCESSAR APOSTAS\nDO DIA"):
        with st.spinner("Analisando probabilidades..."):
            st.toast("IA trabalhando nos dados!")

with col3:
    st.markdown('<p class="section-title">📅 AGENDAMENTO</p>', unsafe_allow_html=True)
    if st.button("⏭️ APOSTAS DO DIA\nSEGUINTE"): pass

with col4:
    st.markdown('<p class="section-title">🎯 RESULTADOS</p>', unsafe_allow_html=True)
    if st.button("💰 OPORTUNIDADES\nENCONTRADAS"):
        st.balloons()
    st.write("")
    if st.button("📋 TABELA\nAUTOMÁTICA"): pass

# --- ÁREA DE DASHBOARD ---
st.markdown("<hr>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label="Jogos Analisados hoje", value="142", delta="+12%")
with c2:
    st.metric(label="Confiança Média IA", value="74%", delta="5%")
with c3:
    st.metric(label="ROI Estimado", value="12.5%", delta="2.1%")

st.write("")
st.markdown("### 📋 Melhores Picks Identificadas")
st.dataframe(df, use_container_width=True, hide_index=True)

# --- RODAPÉ ---
st.markdown("""
    <div style="text-align: center; color: #64748b; font-size: 12px; margin-top: 50px;">
        GIAE Intelligence System &copy; 2023 | Powered by Advanced AI Models
    </div>
    """, unsafe_allow_html=True)
