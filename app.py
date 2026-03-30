import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# ----------------------------------------------------------------
# 1. INICIALIZAÇÃO DE MEMÓRIA (PRIMEIRA COISA DO ARQUIVO)
# ----------------------------------------------------------------
if 'data_sync' not in st.session_state:
    st.session_state.data_sync = str(int(time.time()))

if 'aba_atual' not in st.session_state:
    st.session_state.aba_atual = "Scanner em Tempo Real"

# Configuração da Página
st.set_page_config(page_title="GESTOR IA - Zero White Pro", layout="wide", initial_sidebar_state="collapsed")

# ----------------------------------------------------------------
# 2. DIRETRIZ VISUAL: APARÊNCIA IMUTÁVEL (CSS ZERO WHITE)
# ----------------------------------------------------------------
st.markdown("""
    <style>
    /* Tema Dark e Remoção de Barras de Rolagem */
    [data-testid="stAppViewContainer"] {
        background-color: #0b0e11;
        color: white;
    }
    header {visibility: hidden;}
    .main .block-container {padding-top: 0rem;}
    ::-webkit-scrollbar {display: none;}
    
    /* Header Estilo Betano Superior */
    .betano-header {
        background-color: #0b0e11;
        padding: 10px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #1e2329;
        position: sticky;
        top: 0;
        z-index: 999;
    }
    .logo-text { color: #ff7900; font-weight: bold; font-size: 24px; letter-spacing: 1px; }
    .nav-links { display: flex; gap: 20px; color: #aeb4bc; font-size: 14px; font-weight: 500; }
    .nav-item:hover { color: white; cursor: pointer; }
    .auth-buttons { display: flex; gap: 10px; }
    .btn-registrar {
        background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
        border: none;
        padding: 8px 16px;
        border-radius: 4px;
        color: white;
        font-weight: bold;
        font-size: 12px;
    }
    .btn-entrar {
        background-color: transparent;
        border: 1px solid #aeb4bc;
        padding: 8px 16px;
        border-radius: 4px;
        color: white;
        font-weight: bold;
        font-size: 12px;
    }

    /* Layout de Cards KPI (Bilhete Ouro) */
    .card-container {
        background-color: #1e2329;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        border: 1px solid #2b3139;
        transition: 0.3s;
    }
    .card-container:hover { border-color: #2575fc; }
    .card-title { color: #aeb4bc; font-size: 12px; margin-bottom: 5px; }
    .card-value { color: white; font-size: 20px; font-weight: bold; }
    .card-sub { color: #00ff00; font-size: 11px; margin-top: 5px; }

    /* Estilo da Tabela do Scanner */
    .stDataFrame {
        border-radius: 8px;
        border: 1px solid #1e2329;
    }
    </style>
    
    <div class="betano-header">
        <div class="logo-text">GESTOR IA</div>
        <div class="nav-links">
            <span class="nav-item">ESPORTES</span>
            <span class="nav-item">AO VIVO</span>
            <span class="nav-item">CASSINO</span>
            <span class="nav-item">CASSINO AO VIVO</span>
            <span class="nav-item">VIRTUAIS</span>
            <span class="nav-item">RASPADINHAS</span>
        </div>
        <div class="auth-buttons">
            <button class="btn-entrar">ENTRAR</button>
            <button class="btn-registrar">REGISTRAR</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------
# 3. DIRETRIZ DO "CÉREBRO" (DATA ENGINE COM TRAVA DE CACHE)
# ----------------------------------------------------------------
@st.cache_data(ttl=60)
def carregar_dados_jarvis():
    # URL Bruta com trava de cache para forçar os jogos de 30/03/2026
    URL_DATABASE = f"https://raw.githubusercontent.com/Aritionapr/gestor-ia-apostas/main/data/database_diario.csv?v={st.session_state.data_sync}"
    
    try:
        df_diario = pd.read_csv(URL_DATABASE)
        # Normalização de nomes e tipos para o Scanner (Image 8)
        df_diario['CASA'] = df_diario['CASA'].astype(str)
        df_diario['FORA'] = df_diario['FORA'].astype(str)
        # Garante que CONF é numérica para ordenação
        df_diario['CONF_NUM'] = df_diario['CONF'].str.replace('%','').astype(float)
        return df_diario
    except:
        # Dados de Emergência para não quebrar o layout (Image 8)
        return pd.DataFrame({
            'STATUS': ['AO VIVO', 'AO VIVO', '21:30'],
            'LIGA': ['CHAMPIONSHIP', 'CHAMPIONSHIP', 'MLS'],
            'CASA': ['Preston', 'Cardiff', 'Inter Miami'],
            'FORA': ['Derby County', 'Hull City', 'Orlando City'],
            'GOLS': ['1.5', '1.5', '1.5'],
            'CONF': ['72%', '72%', '72%'],
            'CANTOS': ['9.5+', '9.5+', '9.5+'],
            'CHUTES': ['12+', '12+', '12+'],
            'DEFESAS': ['4+', '4+', '4+'],
            'TMETA': ['16+', '16+', '16+'],
            'ULTIMA_SYNC': ['30/03/2026 00:04'] * 3,
            'CONF_NUM': [72.0, 72.0, 72.0]
        })

df_hoje = carregar_dados_jarvis()

# ----------------------------------------------------------------
# 4. FUNÇÃO DE DESENHO DOS CARDS DO BILHETE OURO
# ----------------------------------------------------------------
def draw_card(titulo, valor, subtext):
    st.markdown(f"""
        <div class="card-container">
            <div class="card-title">{titulo}</div>
            <div class="card-value">{valor}</div>
            <div class="card-sub">{subtext}</div>
        </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------------------
# 5. O CÉREBRO DO BILHETE OURO (PESCARIA AUTOMÁTICA)
# ----------------------------------------------------------------
if not df_hoje.empty:
    # Ordena pelo jogo com maior confiança IA
    melhor_jogo = df_hoje.sort_values(by='CONF_NUM', ascending=False).iloc[0]
    
    banca_atual = "R$ 1.000,00" # Valor da Image 2
    assertividade = melhor_jogo['CONF']
    sugestao = f"OVER {melhor_jogo['GOLS']}"
    # Se a confiança for alta, o Jarvis sugere um OVER 2.5
    if melhor_jogo['CONF_NUM'] > 75:
        sugestao = "OVER 2.5"
        
    confronto = f"{melhor_jogo['CASA']} vs {melhor_jogo['FORA']}"
    versao = "JARVIS v63.0" # Versão atual (5 Temporadas)
    
    # Preenchimento automático dos 8 Cards (Image 2)
    st.write("") # Espaçamento
    st.write("### 🥇 BILHETE OURO - 30/03/2026")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: draw_card("BANCA ATUAL", banca_atual, f"+{assertividade} hoje")
    with col2: draw_card("ASSERTIVIDADE", assertividade, "Base: 5 Temporadas")
    with col3: draw_card("SUGESTÃO", sugestao, "Confiança Alta")
    with col4: draw_card("IA STATUS", "ONLINE", f"{datetime.now().strftime('%H:%M')} Sinc")
    
    col5, col6, col7, col8 = st.columns(4)
    with col5: draw_card("VOL. GLOBAL", "ALTO", "Probabilidade Encontrada")
    with col6: draw_card("STAKE PADRÃO", "1.0%", "Riscoventura")
    with col7: draw_card("VALOR ENTRADA", confronto, "Melhor Jogo do Scanner")
    with col8: draw_card("SISTEMA", versao, "Blindagem Ativa")

else:
    st.warning("Aguardando sincronia do database_diario.csv...")

st.write("---")

# ----------------------------------------------------------------
# 6. SCANNER EM TEMPO REAL (Image 8)
# ----------------------------------------------------------------
st.subheader("📡 SCANNER EM TEMPO REAL - 30/03/2026")

if not df_hoje.empty:
    # Exibição dos dados respeitando a estética Dark
    st.dataframe(
        df_hoje[['STATUS', 'LIGA', 'CASA', 'FORA', 'GOLS', 'CONF', 'CANTOS', 'CHUTES', 'DEFESAS', 'TMETA', 'ULTIMA_SYNC']],
        use_container_width=True,
        hide_index=True
    )

# Rodapé Técnico
st.markdown(f"""
    <div style='text-align: center; color: #aeb4bc; font-size: 10px; padding: 20px;'>
        JARVIS v63.0 | Sincronia Temporal: {datetime.now().strftime('%d/%m/%Y %H:%M')} | Zero White Pro Edition
    </div>
""", unsafe_allow_html=True)
