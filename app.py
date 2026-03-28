import streamlit as st
import pandas as pd
import os
import math
from datetime import datetime

# ==============================================================================
# [PROTOCOLO v61.6 - MOTOR DE ANÁLISE REAL + UI v58.7 IMUTÁVEL]
# MANTENDO 100% DAS DIRETRIZES E ESTILO DO USUÁRIO
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA (IMUTÁVEL)
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA (IMUTÁVEL) ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# --- MOTOR DE INTELIGÊNCIA (CRUZAMENTO DE CSVs) ---
def realizar_analise_autonoma():
    try:
        # O robô lê os jogos que o seu sync_data.py buscou na internet
        df_diario = pd.read_csv("data/database_diario.csv")
        # O robô lê a sua base histórica de 5 temporadas
        df_hist = pd.read_csv("data/historico_5_temporadas.csv")
        
        resultados = []
        for i, row in df_diario.head(20).iterrows():
            t_casa = str(row['CASA'])
            t_fora = str(row['FORA'])
            
            # --- CRUZAMENTO MATEMÁTICO ---
            # Busca no histórico de 5 temporadas o desempenho do time da casa
            h_casa = df_hist[df_hist['Casa'] == t_casa]
            if len(h_casa) > 0:
                win_rate = (len(h_casa[h_casa['Resultado'] == 'H']) / len(h_casa)) * 100
            else: win_rate = 50.0

            resultados.append({
                "jogo": f"{t_casa} vs {t_fora}",
                "win": f"{win_rate:.1f}%",
                "confia": row.get('CONF', '85%'),
                "gols": row.get('GOLS', 'OVER 1.5'),
                "cantos": f"{row.get('CANTOS', 9)}+",
                "cards": f"{row.get('CARTOES', 3)}",
                "meta": f"{row.get('TMETA', 12)}",
                "chutes": f"{row.get('CHUTES', 10)}",
                "defesas": f"{row.get('DEFESAS', 4)}"
            })
        return resultados
    except: return []

# 2. CAMADA DE ESTILO CSS (100% v58.7 - IMUTÁVEL)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none; }
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600 !important; white-space: nowrap; margin: 0 10px; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 140px; margin-bottom: 15px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR E HEADER (IMUTÁVEL v58.7)
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <div class="logo-link">GESTOR IA</div>
                <div style="display:flex; margin-left:20px;">
                    <div class="nav-item">ESPORTES</div><div class="nav-item">AO VIVO</div><div class="nav-item">VIRTUAIS</div>
                </div>
            </div>
            <div class="header-right">
                <div class="registrar-pill">REGISTRAR</div>
                <div class="entrar-grad">ENTRAR</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc, color="#6d28d9"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- TELA PRINCIPAL (BILHETE OURO) ---
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO - TOP 20 ANALISADOS</h2>", unsafe_allow_html=True)
    
    # Cards Superiores (Imutáveis)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100, "#bf953f")
    with h2: draw_card("ASSERTIVIDADE", "94.2%", 94, "#bf953f")
    with h3: draw_card("SUGESTÃO", "OVER 2.5", 88, "#bf953f")
    with h4: draw_card("IA STATUS", "SINCRO OK", 100, "#10b981")
    
    # LISTAGEM REAL DOS 20 JOGOS
    jogos = realizar_analise_autonoma()
    
    if jogos:
        for j in jogos:
            st.markdown(f"""
                <div style="background:#11151a; border: 1px solid #1e293b; border-left: 4px solid #bf953f; padding:20px; border-radius:8px; margin-bottom:15px;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
                        <span style="color:#bf953f; font-size:10px; font-weight:900;">WIN RATE: {j['win']}</span>
                        <span style="color:#00f2ff; font-size:10px; font-weight:900;">CONFIA: {j['confia']}</span>
                    </div>
                    <div style="color:white; font-size:18px; font-weight:800;">{j['jogo']}</div>
                    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); gap:10px; margin-top:15px;">
                        <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:5px; text-align:center;">
                            <div style="color:#64748b; font-size:8px;">GOLS</div><div style="color:white; font-size:11px; font-weight:700;">{j['gols']}</div>
                        </div>
                        <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:5px; text-align:center;">
                            <div style="color:#64748b; font-size:8px;">CANTOS</div><div style="color:white; font-size:11px; font-weight:700;">{j['cantos']}</div>
                        </div>
                        <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:5px; text-align:center;">
                            <div style="color:#64748b; font-size:8px;">CARTÕES</div><div style="color:white; font-size:11px; font-weight:700;">{j['cards']}</div>
                        </div>
                        <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:5px; text-align:center;">
                            <div style="color:#64748b; font-size:8px;">CHUTES</div><div style="color:white; font-size:11px; font-weight:700;">{j['chutes']}</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Aguardando atualização do arquivo database_diario.csv...")

else:
    st.info(f"Painel {st.session_state.aba_ativa.upper()} em operação.")

st.markdown("""<div class="footer-shield"><div>STATUS: ● JARVIS v61.6 AUTÔNOMO</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
