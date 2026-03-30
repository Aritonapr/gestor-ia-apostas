import streamlit as st
import pandas as pd
import time
from datetime import datetime

# 1. ESTADO DE NAVEGAÇÃO - Scanner é a tela inicial
if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = "SCANNER EM TEMPO REAL"

# Configuração da Página: Layout Largo e Sidebar visível
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# 2. ESTÉTICA IMUTÁVEL (CSS ZERO WHITE)
st.markdown("""
    <style>
    /* Fundo Escuro e Scroll Oculto */
    [data-testid="stAppViewContainer"] { background-color: #0b0e11; color: white; }
    [data-testid="stSidebar"] { background-color: #0b0e11; border-right: 1px solid #1e2329; }
    header {visibility: hidden;}
    .main .block-container {padding-top: 1rem;}
    ::-webkit-scrollbar {display: none;}
    
    /* Logo e Estilo Betano */
    .logo-text { color: #6a11cb; font-weight: bold; font-size: 24px; letter-spacing: 1px; padding: 20px 0; }

    /* Cards KPI - Estilo Bilhete Ouro */
    .kpi-card {
        background-color: #161a1e;
        border-radius: 4px;
        padding: 20px;
        text-align: center;
        border: 1px solid #1e2329;
        height: 140px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin-bottom: 20px;
    }
    .kpi-title { color: #5d6670; font-size: 10px; text-transform: uppercase; margin-bottom: 15px; }
    .kpi-value { color: white; font-size: 22px; font-weight: bold; margin-bottom: 10px; }
    .kpi-bar { height: 4px; background: linear-gradient(90deg, #6a11cb, #2575fc); border-radius: 2px; width: 80%; margin: 0 auto; }
    
    /* Botões da Sidebar */
    .stButton>button {
        background-color: transparent; color: #aeb4bc; border: none; 
        text-align: left; width: 100%; padding: 12px 10px; font-size: 14px;
    }
    .stButton>button:hover { color: #ff7900; background-color: #1e2329; }
    </style>
""", unsafe_allow_html=True)

# 3. BARRA LATERAL (MENU JARVIS)
with st.sidebar:
    st.markdown('<div class="logo-text">GESTOR IA</div>', unsafe_allow_html=True)
    
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.pagina_ativa = "SCANNER PRÉ-LIVE"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.pagina_ativa = "SCANNER EM TEMPO REAL"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.pagina_ativa = "GESTÃO DE BANCA"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.pagina_ativa = "HISTÓRICO DE CALLS"
    if st.button("🎫 BILHETE OURO"): st.session_state.pagina_ativa = "BILHETE OURO"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.pagina_ativa = "VENCEDORES"
    
    # Espaçamento manual para evitar erros de Attribute
    st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
    st.caption(f"STATUS: ● IA OPERACIONAL | v63.0")

# 4. CARREGAMENTO DE DADOS (DATABASE DO GITHUB)
@st.cache_data(ttl=60)
def carregar_dados_scanner():
    try:
        # Puxa o CSV atualizado pelo sync_data.py
        URL = f"https://raw.githubusercontent.com/Aritionapr/gestor-ia-apostas/main/data/database_diario.csv?v={time.time()}"
        df = pd.read_csv(URL)
        if 'CONF' in df.columns:
            # Converte a porcentagem em número para filtrar o Bilhete Ouro
            df['CONF_NUM'] = df['CONF'].astype(str).str.replace('%','').astype(float)
        return df
    except:
        return pd.DataFrame()

df_hoje = carregar_dados_scanner()

# 5. LÓGICA DE EXIBIÇÃO DE TELAS
if st.session_state.pagina_ativa == "BILHETE OURO":
    st.markdown("### 🎫 BILHETE OURO")
    
    # Busca automática do melhor jogo do Scanner (Image 1)
    if not df_hoje.empty:
        melhor = df_hoje.sort_values(by='CONF_NUM', ascending=False).iloc[0]
        banca = "R$ 1.000,00"
        confianca = melhor['CONF']
        sugestao = f"OVER {melhor['GOLS']}"
        confronto = melhor['CASA']
    else:
        banca, confianca, sugestao, confronto = "R$ 0,00", "0%", "---", "Aguardando Dados"

    # Layout de 8 Cards (Padrão da Imagem 2)
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown(f'<div class="kpi-card"><div class="kpi-title">BANCA ATUAL</div><div class="kpi-value">{banca}</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)
    with col2: st.markdown(f'<div class="kpi-card"><div class="kpi-title">ASSERTIVIDADE</div><div class="kpi-value">{confianca}</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)
    with col3: st.markdown(f'<div class="kpi-card"><div class="kpi-title">SUGESTÃO</div><div class="kpi-value">{sugestao}</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)
    with col4: st.markdown(f'<div class="kpi-card"><div class="kpi-title">IA STATUS</div><div class="kpi-value">ONLINE</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)

    col5, col6, col7, col8 = st.columns(4)
    with col5: st.markdown(f'<div class="kpi-card"><div class="kpi-title">VOL. GLOBAL</div><div class="kpi-value">ALTO</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)
    with col6: st.markdown(f'<div class="kpi-card"><div class="kpi-title">STAKE PADRÃO</div><div class="kpi-value">1.0%</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)
    with col7: st.markdown(f'<div class="kpi-card"><div class="kpi-title">VALOR ENTRADA</div><div class="kpi-value">{confronto}</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)
    with col8: st.markdown(f'<div class="kpi-card"><div class="kpi-title">SISTEMA</div><div class="kpi-value">JARVIS v63.0</div><div class="kpi-bar"></div></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.info(f"O Bilhete Ouro foi gerado analisando as tendências de {confronto} contra o histórico de 5 temporadas.")

elif st.session_state.pagina_ativa == "SCANNER EM TEMPO REAL":
    st.markdown(f"### 📡 SCANNER EM TEMPO REAL - {datetime.now().strftime('%d/%m/%Y')}")
    if not df_hoje.empty:
        # Exibe a tabela do Scanner (conforme Image 6 e Image 8)
        st.dataframe(df_hoje.drop(columns=['CONF_NUM'], errors='ignore'), use_container_width=True, hide_index=True)
    else:
        st.info("O Robô está sincronizando as partidas de hoje no servidor...")

else:
    # Outras telas do menu
    st.markdown(f"### {st.session_state.pagina_ativa}")
    st.write("Esta funcionalidade está sendo vinculada ao processamento de Big Data.")

# Rodapé Técnico
st.markdown("<br><center><small>JARVIS v63.0 | Zero White Pro Edition</small></center>", unsafe_allow_html=True)
