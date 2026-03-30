import streamlit as st
import pandas as pd
import time
from datetime import datetime

# 1. MEMÓRIA DE NAVEGAÇÃO (Define o Scanner como tela inicial)
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = "Scanner em Tempo Real"

if 'data_sync' not in st.session_state:
    st.session_state.data_sync = str(int(time.time()))

# Configuração Base
st.set_page_config(page_title="GESTOR IA - Zero White Pro", layout="wide", initial_sidebar_state="expanded")

# 2. ESTÉTICA IMUTÁVEL (CSS)
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #0b0e11; color: white; }
    header {visibility: hidden;}
    .main .block-container {padding-top: 1rem;}
    ::-webkit-scrollbar {display: none;}
    
    /* Estilo Betano Header */
    .betano-header {
        background-color: #0b0e11; padding: 10px 20px; display: flex;
        justify-content: space-between; align-items: center; border-bottom: 1px solid #1e2329;
    }
    .logo-text { color: #ff7900; font-weight: bold; font-size: 24px; }
    
    /* Cards KPI */
    .card-container {
        background-color: #1e2329; border-radius: 8px; padding: 15px;
        text-align: center; border: 1px solid #2b3139;
    }
    .card-title { color: #aeb4bc; font-size: 12px; }
    .card-value { color: white; font-size: 20px; font-weight: bold; }
    </style>
    <div class="betano-header"><div class="logo-text">GESTOR IA</div></div>
""", unsafe_allow_html=True)

# 3. BARRA LATERAL (MENU DE BOTÕES)
with st.sidebar:
    st.markdown("### 🤖 MENU JARVIS")
    if st.button("📡 SCANNER EM TEMPO REAL"):
        st.session_state.pagina_ativa = "Scanner em Tempo Real"
    
    if st.button("🎫 BILHETE OURO"):
        st.session_state.pagina_ativa = "Bilhete Ouro"
    
    st.write("---")
    st.write(f"**Status:** IA Operacional")
    st.write(f"**Versão:** v63.0")

# 4. CARREGAMENTO DE DADOS
@st.cache_data(ttl=60)
def carregar_dados():
    URL = f"https://raw.githubusercontent.com/Aritionapr/gestor-ia-apostas/main/data/database_diario.csv?v={st.session_state.data_sync}"
    try:
        df = pd.read_csv(URL)
        df['CONF_NUM'] = df['CONF'].str.replace('%','').astype(float)
        return df
    except:
        return pd.DataFrame()

df_hoje = carregar_dados()

# 5. LÓGICA DE EXIBIÇÃO POR CLIQUE
if st.session_state.pagina_ativa == "Scanner em Tempo Real":
    st.subheader(f"📡 SCANNER EM TEMPO REAL - {datetime.now().strftime('%d/%m/%Y')}")
    if not df_hoje.empty:
        st.dataframe(df_hoje[['STATUS', 'LIGA', 'CASA', 'FORA', 'GOLS', 'CONF', 'CANTOS', 'CHUTES', 'ULTIMA_SYNC']], 
                     use_container_width=True, hide_index=True)
    else:
        st.warning("Aguardando sincronia de dados...")

elif st.session_state.pagina_ativa == "Bilhete Ouro":
    st.subheader(f"🥇 BILHETE OURO DO DIA")
    if not df_hoje.empty:
        # Pega o melhor jogo do Scanner automaticamente
        melhor = df_hoje.sort_values(by='CONF_NUM', ascending=False).iloc[0]
        
        col1, col2, col3, col4 = st.columns(4)
        with col1: 
            st.markdown(f'<div class="card-container"><div class="card-title">BANCA</div><div class="card-value">R$ 1.000,00</div></div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="card-container"><div class="card-title">ASSERTIVIDADE</div><div class="card-value">{melhor["CONF"]}</div></div>', unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div class="card-container"><div class="card-title">SUGESTÃO</div><div class="card-value">OVER {melhor["GOLS"]}</div></div>', unsafe_allow_html=True)
        with col4:
            st.markdown(f'<div class="card-container"><div class="card-title">ENTRADA</div><div class="card-value">{melhor["CASA"]}</div></div>', unsafe_allow_html=True)
            
        st.write("---")
        st.info(f"Análise baseada em 5 temporadas para o jogo: {melhor['CASA']} vs {melhor['FORA']}")
    else:
        st.error("Dados históricos insuficientes para gerar o bilhete.")

# Rodapé
st.markdown("<br><center><small>JARVIS v63.0 | Zero White Pro</small></center>", unsafe_allow_html=True)
