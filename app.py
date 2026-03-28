import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO IA v62.0 - ATIVAÇÃO DO CÉREBRO MATEMÁTICO]
# DIRETRIZ: SUBSTITUIR DADOS FIXOS POR CÁLCULOS REAIS DO CSV
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- 1. INICIALIZAÇÃO E CARREGAMENTO ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

# MEMÓRIA DOS BOTS (AGORA SERÁ PREENCHIDA PELA LÓGICA)
if 'dados_ia' not in st.session_state:
    st.session_state.dados_ia = {
        "vencedor": "ANALISANDO...", "gols": "---", "prob": "0%", 
        "cartoes": "---", "escanteios": "---", "tiros_meta": "---", 
        "chutes_gol": "---", "defesas": "---", "sync": "OFFLINE"
    }

def carregar_e_processar():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        ts = os.path.getmtime(path)
        st.session_state.dados_ia["sync"] = datetime.fromtimestamp(ts).strftime('%d/%m %H:%M')
        try:
            df = pd.read_csv(path)
            # --- LÓGICA DO BOT 1 (BILHETE OURO) ---
            # Ele busca o jogo com maior confiança no CSV
            if not df.empty:
                melhor_jogo = df.sort_values(by='CONF', ascending=False).iloc[0]
                st.session_state.dados_ia.update({
                    "vencedor": f"{melhor_jogo['CASA']} vs {melhor_jogo['FORA']}",
                    "gols": str(melhor_jogo['GOLS']),
                    "prob": str(melhor_jogo['CONF']),
                    "cartoes": str(melhor_jogo['CARTOES']) + " AVG",
                    "escanteios": str(melhor_jogo['CANTOS']) + " AVG",
                    "tiros_meta": str(melhor_jogo['TMETA']) + " AVG",
                    "chutes_gol": str(melhor_jogo['CHUTES']) + " AVG",
                    "defesas": str(melhor_jogo['DEFESAS']) + " AVG"
                })
            return df
        except: return None
    return None

df_diario = carregar_e_processar()

# --- 2. ESTILO CSS (MANTIDO 100% IMUTÁVEL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { width: 0px; background: transparent; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; display: flex; align-items: center; justify-content: space-between; padding: 0 40px !important; z-index: 1000000; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 20px !important; text-decoration: none; text-transform: uppercase; }
    [data-testid="stSidebar"] { min-width: 300px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow-y: auto !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 14px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color_footer}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("""<div class="betano-header"><a href="#" class="logo-link">GESTOR IA</a></div><div style="height:65px;"></div>""", unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

# --- 4. TELAS ---

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO (IA REAL)</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE", st.session_state.dados_ia["prob"], 92)
    with h3: draw_card("SUGESTÃO GOLS", st.session_state.dados_ia["gols"], 88)
    with h4: draw_card("JOGO ESCOLHIDO", st.session_state.dados_ia["vencedor"], 100, "#00ff88")
    
    st.markdown("### 📊 ESTATÍSTICAS MATEMÁTICAS DO JOGO")
    b1, b2, b3, b4 = st.columns(4)
    with b1: draw_card("CARTÕES", st.session_state.dados_ia["cartoes"], 70, "#ffcc00")
    with b2: draw_card("ESCANTEIOS", st.session_state.dados_ia["escanteios"], 85, "#00d2ff")
    with b3: draw_card("CHUTES NO GOL", st.session_state.dados_ia["chutes_gol"], 60, "#9d54ff")
    with b4: draw_card("TIROS DE META", st.session_state.dados_ia["tiros_meta"], 50, "#ff4b4b")
    
    if df_diario is not None:
        st.markdown("### 📋 TODOS OS JOGOS DISPONÍVEIS")
        st.dataframe(df_diario, use_container_width=True)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
    draw_card("VALOR DA STAKE", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE (MANUAL)</h2>", unsafe_allow_html=True)
    lista_times = sorted(df_diario['CASA'].unique().tolist()) if df_diario is not None else ["Aguardando CSV..."]
    c1, c2 = st.columns(2)
    with c1: st.selectbox("TIME CASA", lista_times)
    with c2: st.selectbox("TIME FORA", lista_times)
    st.button("EXECUTAR ANÁLISE MANUAL")

else:
    st.markdown(f"<h2 style='color:white;'>{st.session_state.aba_ativa.upper()}</h2>", unsafe_allow_html=True)
    st.info("Mercado sendo processado pelo motor Jarvis...")

# RODAPÉ
st.markdown(f"""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v62.0 | SYNC: {st.session_state.dados_ia["sync"]}</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
