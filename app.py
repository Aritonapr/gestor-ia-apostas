import streamlit as st
import pandas as pd
import os
from datetime import datetime
import random

# ==============================================================================
# 🔒 [DIRETRIZ DE PROTEÇÃO JARVIS v92.00 - INTEGRIDADE TOTAL DE UI]
# ESTE CÓDIGO INTEGRA AS IMAGENS 1, 2, 3 E 4 EM UM ÚNICO AMBIENTE PROTEGIDO.
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba' not in st.session_state: st.session_state.aba = "bilhete"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

def carregar_dados():
    path = "data/database_diario.csv"
    if os.path.exists(path): return pd.read_csv(path)
    return None

df = carregar_dados()

# --- CAMADA DE ESTILO CSS (RESTAURAÇÃO TOTAL v57.35 + FIX LEITURA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, .stApp { background-color: #0b0e11 !important; color: white; font-family: 'Inter', sans-serif; }
    header { display: none !important; }
    
    /* HEADER BETANO STYLE */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.1); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px; z-index: 1000000; transform: translate3d(0,0,0);
    }
    .logo-txt { color: #9d54ff !important; font-weight: 900; font-size: 21px; text-transform: uppercase; text-decoration: none; }
    .nav-item-top { color: white; font-size: 10px; font-weight: 700; text-transform: uppercase; opacity: 0.8; margin-right: 20px; }

    /* SIDEBAR CUSTOM */
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 16px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 4px solid #6d28d9 !important; }

    /* CARDS DE MÉTRICAS (ESTILO IMAGEM 1) */
    .metric-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 140px; margin-bottom: 15px;
        transition: all 0.3s ease;
    }
    .metric-card:hover { border-color: #6d28d9; transform: translateY(-3px); }
    .metric-title { color: #64748b; font-size: 9px; text-transform: uppercase; font-weight: 700; margin-bottom: 10px; }
    .metric-value { color: white; font-size: 18px; font-weight: 900; }
    .progress-bar { background: #1e293b; height: 4px; width: 80%; border-radius: 10px; margin: 15px auto; overflow: hidden; }
    .progress-fill { background: linear-gradient(90deg, #6d28d9, #06b6d4); height: 100%; }

    /* TABELA (ESTILO IMAGEM 3 - FIX LEITURA) */
    [data-testid="stTable"] { background: #161b22 !important; border-radius: 8px; overflow: hidden; }
    th { background-color: #1e293b !important; color: #94a3b8 !important; text-transform: uppercase; font-size: 10px !important; padding: 15px !important; }
    td { color: #ffffff !important; font-size: 12px !important; border-bottom: 1px solid #222 !important; padding: 12px !important; }

    /* BILHETE */
    .bilhete-master { background: #ffffff !important; color: #111 !important; padding: 25px; border-radius: 8px; max-width: 500px; margin: 0 auto; border-top: 10px solid #9d54ff; box-shadow: 0 10px 40px rgba(0,0,0,0.8); }
    .ticket-row { display: flex; justify-content: space-between; font-size: 11px; border-bottom: 1px solid #f2f2f2; padding: 8px 0; color: #111 !important; }
    
    .banca-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 22px; font-weight: 800; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

# 3. COMPONENTES DE UI REUTILIZÁVEIS
def draw_metric(title, value, perc, color="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            <div class="progress-bar"><div class="progress-fill" style="width:{perc}%; background:{color};"></div></div>
        </div>
    """, unsafe_allow_html=True)

# --- HEADER FIXO ---
st.markdown("""<div class="betano-header"><div class="logo-txt">GESTOR IA</div><div style="display:flex;"><span class="nav-item-top">APOSTAS ESPORTIVAS</span><span class="nav-item-top">AO VIVO</span><span class="nav-item-top">OPORTUNIDADES IA</span><span class="nav-item-top">ESTATÍSTICAS AVANÇADAS</span></div><div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:8px 25px; border-radius:5px; font-size:10px; font-weight:900; cursor:pointer;">ENTRAR</div></div>""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:70px;"></div>', unsafe_allow_html=True) 
    if st.button("🎟️ GERAR BILHETE DO DIA"): st.session_state.aba = "bilhete"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba = "scanner"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba = "banca"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba = "jogos"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba = "cantos"

st.markdown('<div style="height:40px;"></div>', unsafe_allow_html=True)

# --- LÓGICA DE TELAS ---

if st.session_state.aba == "bilhete":
    st.markdown("<h2 style='text-align:center;'>🎟️ BILHETE MESTRE IA (TOP 20)</h2>", unsafe_allow_html=True)
    if df is not None:
        b_html = '<div class="bilhete-master"><div style="text-align:center; border-bottom:1px solid #eee; padding-bottom:10px; margin-bottom:15px;"><b style="font-size:18px;">GESTOR IA PRO</b><br><span style="font-size:10px; color:#666;">ANÁLISE PROFISSIONAL 20 JOGOS</span></div>'
        s_txt = "🔥 *SINAIS JARVIS IA*\n\n"
        for i, r in df.iterrows():
            b_html += f'<div class="ticket-row"><span><b>{r["CASA"]}</b> x <b>{r["FORA"]}</b></span><span style="background:#f1f5f9; padding:2px 8px; border-radius:4px; font-weight:900; color:#6d28d9; font-size:9px;">{r["GOLS"]}</span></div>'
            s_txt += f"✅ {r['CASA']} x {r['FORA']} -> {r['GOLS']} ({r['CONF']})\n"
        b_html += '</div>'
        c1, c2, c3 = st.columns([1, 2, 1])
        with col2 if 'col2' in locals() else c2: 
            st.markdown(b_html, unsafe_allow_html=True)
            st.code(s_txt, language="text")

elif st.session_state.aba == "banca":
    st.markdown('<div class="banca-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>', unsafe_allow_html=True)
    col_l, col_r = st.columns([1.2, 2.8])
    with col_l:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total, step=50.0)
        st.session_state.stake_padrao = st.slider("STAKE POR OPERAÇÃO (%)", 0.1, 10.0, st.session_state.stake_padrao)
        st.session_state.meta_diaria = st.slider("META DIÁRIA (%)", 1.0, 30.0, st.session_state.meta_diaria)
        st.session_state.stop_loss = st.slider("LIMITE DE PERDA (%)", 1.0, 30.0, st.session_state.stop_loss)
    
    with col_r:
        v_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        v_meta = (st.session_state.banca_total * st.session_state.meta_diaria / 100)
        v_loss = (st.session_state.banca_total * st.session_state.stop_loss / 100)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_metric("VALOR ENTRADA", f"R$ {v_stake:,.2f}", 100)
        with r2: draw_metric("STOP GAIN (R$)", f"R$ {v_meta:,.2f}", 100)
        with r3: draw_metric("STOP LOSS (R$)", f"R$ {v_loss:,.2f}", 100)
        with r4: draw_metric("ALVO FINAL", f"R$ {st.session_state.banca_total + v_meta:,.2f}", 100)
        r5, r6, r7, r8 = st.columns(4)
        with r5: draw_metric("RISCO TOTAL", f"{st.session_state.stake_padrao}%", 100)
        with r6: draw_metric("ENTRADAS/META", f"{int(v_meta/v_stake) if v_stake > 0 else 0}", 100)
        with r7: draw_metric("ENTRADAS/LOSS", f"{int(v_loss/v_stake) if v_stake > 0 else 0}", 100)
        with r8: draw_metric("SAÚDE BANCA", "EXCELENTE", 100, "#00ff88")

elif st.session_state.aba == "scanner":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    sel_cat = c1.selectbox("🌎 CATEGORIA", ["BRASIL", "EUROPA", "AMÉRICA DO SUL"])
    sel_tipo = c2.selectbox("📂 TIPO (COMPETIÇÃO)", ["Série A", "Premier League", "La Liga", "Champions"])
    sel_campeon = c3.selectbox("🏆 CAMPEONATO", ["Rodada Atual", "Fase Eliminatória"])
    
    if df is not None:
        confronto = st.selectbox("⚔️ DEFINIR CONFRONTO", df['CASA'] + " x " + df['FORA'])
        if st.button("⚡ EXECUTAR ALGORITMO", use_container_width=True):
            jogo = df[df['CASA'] + " x " + df['FORA'] == confronto].iloc[0]
            st.markdown(f"<h3 style='color:#9d54ff; text-align:center;'>RESULTADO: {confronto}</h3>", unsafe_allow_html=True)
            k1, k2, k3, k4 = st.columns(4)
            with k1: draw_metric("VENCEDOR", f"{jogo['CASA'] if float(jogo['CONF'].replace('%','')) > 50 else 'Empate'}", 85)
            with k2: draw_metric("GOLS", f"{jogo['GOLS']}", 90)
            with k3: draw_metric("STAKE", f"R$ {st.session_state.banca_total * st.session_state.stake_padrao / 100:,.2f}", 100)
            with k4: draw_metric("CANTOS", f"{jogo['CANTOS']}+", 80)

elif st.session_state.aba == "jogos":
    st.markdown("## 📅 JOGOS ANALISADOS HOJE")
    if df is not None: st.table(df)

elif st.session_state.aba == "vencedores":
    st.markdown("## 🏆 PROBABILIDADE DE VENCEDORES (TOP 20)")
    if df is not None:
        for i, r in df.iterrows():
            st.write(f"✅ **{r['CASA']}** tem **{r['CONF']}** de probabilidade contra {r['FORA']}")

elif st.session_state.aba == "gols":
    st.markdown("## ⚽ ANALISADOR DE GOLS (TOP 20)")
    if df is not None:
        for i, r in df.iterrows():
            st.write(f"🔥 **{r['CASA']} x {r['FORA']}** -> Tendência Real de **{r['GOLS']}**")

elif st.session_state.aba == "cantos":
    st.markdown("## 🚩 ANALISADOR DE ESCANTEIOS")
    if df is not None:
        for i, r in df.iterrows():
            st.write(f"🚩 **{r['CASA']} x {r['FORA']}** -> Média Estimada: **{r['CANTOS']} Cantos**")

st.markdown("""<div class="footer-ia"><div>STATUS: ● IA OPERACIONAL | v92.00 | PROTEÇÃO DE CÓDIGO ATIVA</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
