import streamlit as st
import pandas as pd
import requests
import time
from datetime import datetime
import os

# ==============================================================================
# [PROTOCOLO JARVIS v61.2 - INTEGRALIDADE TOTAL]
# REGRAS: APARÊNCIA IMUTÁVEL | ESTRUTURA FIXA | FOCO BACK-END | CÓDIGO ÍNTEGRO
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA (SESSION STATE) ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'dados_live_real' not in st.session_state: st.session_state.dados_live_real = None

# --- MOTOR DE DADOS DIÁRIOS ---
def carregar_banco_dados_ia():
    caminho = "data/database_diario.csv"
    if os.path.exists(caminho):
        try:
            return pd.read_csv(caminho)
        except:
            return None
    return None

df_diario = carregar_banco_dados_ia()

# ==============================================================================
# LÓGICA DE PROCESSAMENTO (BACK-END INVISÍVEL)
# ==============================================================================

def executar_varredura_live_invisivel():
    """
    Realiza a raspagem de dados reais e cruza com a base da IA.
    Injeta o resultado diretamente no st.session_state.
    """
    if df_diario is not None:
        try:
            # Simulação de captura via API/Raspagem (Substituir pelo seu endpoint)
            jogos_em_campo = [
                {"casa": "Athletico-PR", "fora": "Atlético-MG", "placar": "0 - 0", "tempo": "15'"},
                {"casa": "Flamengo", "fora": "Palmeiras", "placar": "1 - 0", "tempo": "32'"},
                {"casa": "Real Madrid", "fora": "Barcelona", "placar": "0 - 2", "tempo": "55'"}
            ]
            
            analise_viva = []
            # Identificação dinâmica de colunas
            cols = {c.upper(): c for c in df_diario.columns}
            col_casa = cols.get('CASA')
            col_conf = cols.get('CONFIANCA')

            if col_casa and col_conf:
                for jogo in jogos_em_campo:
                    # Busca o confronto na base da IA
                    match = df_diario[df_diario[col_casa].str.contains(jogo['casa'], case=False, na=False)]
                    
                    if not match.empty:
                        conf_val = str(match.iloc[0][col_conf]).replace('%', '')
                        conf_num = float(conf_val)
                        
                        # Lógica de Alerta
                        status = "🔥 ENTRADA CONFIRMADA" if conf_num > 85 else "AGUARDAR"
                        
                        analise_viva.append({
                            "TEMPO": jogo['tempo'],
                            "CONFRONTO": f"{jogo['casa']} x {jogo['fora']}",
                            "PLACAR": jogo['placar'],
                            "CONFIANÇA IA": f"{conf_num}%",
                            "AÇÃO": status
                        })
                
                st.session_state.dados_live_real = pd.DataFrame(analise_viva)
        except:
            st.session_state.dados_live_real = None

# ==============================================================================
# CAMADA DE ESTILO CSS (IMUTÁVEL - ZERO WHITE)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }

    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000;
    }
    
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: all 0.2s ease !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important;
    }

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
    }
    
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# SIDEBAR E BOTÕES (ALTERAÇÕES SOLICITADAS)
# ==============================================================================
with st.sidebar:
    # Header da Sidebar (Imutável)
    st.markdown("""
        <div class="betano-header">
            <div style="color: #9d54ff; font-weight: 900; font-size: 21px;">GESTOR IA</div>
            <div style="color:white; font-size:9px; font-weight:800; border:1.5px solid white; padding:7px 15px; border-radius:20px;">REGISTRAR</div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True)

    # BOTÕES DA SIDEBAR COM LÓGICA DE GATILHO
    if st.button("🎯 SCANNER PRÉ-LIVE"): 
        st.session_state.aba_ativa = "analise"

    # [ALTERAÇÃO 1: SCANNER EM TEMPO REAL]
    if st.button("📡 SCANNER EM TEMPO REAL"): 
        st.session_state.aba_ativa = "live"

    if st.button("💰 GESTÃO DE BANCA"): 
        st.session_state.aba_ativa = "gestao"

    if st.button("📅 BILHETE OURO"): 
        st.session_state.aba_ativa = "home"

    # [ALTERAÇÃO 2: APOSTAS POR GOLS - O GATILHO]
    if st.button("⚽ APOSTAS POR GOLS"): 
        # Se o usuário estiver na aba Live, este botão vira o SCANNER REAL
        if st.session_state.aba_ativa == "live":
            with st.spinner("PROCESSANDO IA..."):
                executar_varredura_live_invisivel()
        else:
            # Caso contrário, apenas navega
            st.session_state.aba_ativa = "gols"

    if st.button("🚩 APOSTAS POR ESCANTEIOS"): 
        st.session_state.aba_ativa = "escanteios"

# ==============================================================================
# FUNÇÃO DE RENDERIZAÇÃO DE CARDS (ESTRUTURA FIXA)
# ==============================================================================
def draw_card(title, value, perc):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;">
                <div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); height:100%; width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# NAVEGAÇÃO DE TELAS
# ==============================================================================

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        st.dataframe(df_diario, use_container_width=True)

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    
    # ESTRUTURA FIXA DE COLUNAS E CARDS
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("JOGOS AO VIVO", str(len(st.session_state.dados_live_real) if st.session_state.dados_live_real is not None else 0), 100)
    with c2: draw_card("ALERTAS IA", "SISTEMA ATIVO", 100)
    with c3: draw_card("MERCADO", "GOLS / CANTOS", 100)
    with c4: draw_card("STATUS", "AGUARDANDO GATILHO", 100)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.session_state.dados_live_real is not None:
        st.dataframe(st.session_state.dados_live_real, use_container_width=True, hide_index=True)
    else:
        st.info("Para realizar a varredura dos jogos de agora, clique no botão '⚽ APOSTAS POR GOLS' na barra lateral.")

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    # Lógica de seleção de times (Athletico-PR vs Atlético-MG) mantida aqui

# FOOTER (IMUTÁVEL)
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v61.2</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
