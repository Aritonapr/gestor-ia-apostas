import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime
import random

# ==============================================================================
# 🔒 [DIRETRIZ DE PROTEÇÃO JARVIS v93.00 - SISTEMA DE MEMÓRIA E DETALHAMENTO]
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba' not in st.session_state: st.session_state.aba = "bilhete"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

def carregar_dados():
    path = "data/database_diario.csv"
    if os.path.exists(path): return pd.read_csv(path)
    return None

df = carregar_dados()

# --- CAMADA DE ESTILO CSS (RESTAURAÇÃO TOTAL + FIX TABELA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, .stApp { background-color: #0b0e11 !important; color: white; font-family: 'Inter', sans-serif; }
    header { display: none !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.1); 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px; z-index: 1000000;
    }
    .logo-ia { color: #9d54ff !important; font-weight: 900; font-size: 21px; text-transform: uppercase; text-decoration: none; }
    
    /* SIDEBAR */
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 16px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 4px solid #6d28d9 !important; }

    /* FIX TABELA: PERMITIR SCROLL HORIZONTAL PARA NÃO CORTAR TEXTO */
    .stDataFrame { background: #161b22; border-radius: 8px; border: 1px solid #30363d; padding: 10px; }
    
    /* CARDS MÉTRICAS */
    .metric-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; margin-bottom: 15px; }
    .metric-title { color: #64748b; font-size: 9px; text-transform: uppercase; font-weight: 700; }
    .metric-value { color: white; font-size: 18px; font-weight: 900; margin-top: 10px; }
    
    /* BILHETE */
    .bilhete-master { background: #ffffff !important; color: #111 !important; padding: 25px; border-radius: 8px; max-width: 500px; margin: 0 auto; border-top: 10px solid #9d54ff; box-shadow: 0 10px 40px rgba(0,0,0,0.8); }
    .ticket-row { display: flex; justify-content: space-between; font-size: 11px; border-bottom: 1px solid #f2f2f2; padding: 8px 0; color: #111 !important; }
    .stCodeBlock { background: #161b22 !important; border: 1px solid #30363d !important; border-radius: 8px !important; }
    
    .history-card { background: #161b22; border-left: 4px solid #9d54ff; padding: 15px; border-radius: 6px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER FIXO ---
st.markdown("""<div class="betano-header"><div class="logo-ia">GESTOR IA</div><div style="display:flex; gap:20px;"><span style="color:white; font-size:10px; font-weight:700;">APOSTAS ESPORTIVAS</span><span style="color:white; font-size:10px; font-weight:700;">AO VIVO</span><span style="color:white; font-size:10px; font-weight:700;">ESTATÍSTICAS</span></div><div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); color:white; padding:8px 25px; border-radius:5px; font-size:9px; font-weight:900; cursor:pointer;">ENTRAR</div></div>""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div style="height:70px;"></div>', unsafe_allow_html=True) 
    if st.button("🎟️ GERAR BILHETE DO DIA"): st.session_state.aba = "bilhete"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba = "scanner"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba = "banca"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba = "historico"
    if st.button("📅 JOGOS ANALISADOS"): st.session_state.aba = "jogos"
    if st.button("🏆 VENCEDORES"): st.session_state.aba = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba = "gols"
    if st.button("🚩 ESCANTEIOS"): st.session_state.aba = "cantos"

st.markdown('<div style="height:40px;"></div>', unsafe_allow_html=True)

# --- LÓGICA DE TELAS ---

if st.session_state.aba == "bilhete":
    st.markdown("<h2 style='text-align:center;'>🎟️ BILHETE MESTRE IA (7 NÍVEIS)</h2>", unsafe_allow_html=True)
    if df is not None:
        b_html = '<div class="bilhete-master"><div style="text-align:center; border-bottom:1px solid #eee; padding-bottom:10px; margin-bottom:15px;"><b style="font-size:16px;">GESTOR IA PRO - ANÁLISE GLOBAL</b></div>'
        s_txt = "🔥 *SINAIS JARVIS IA - RELATÓRIO 7 NÍVEIS*\n\n"
        
        for i, r in df.iterrows():
            b_html += f'<div class="ticket-row"><span><b>{r["CASA"]}</b> x <b>{r["FORA"]}</b></span><span style="background:#f1f5f9; padding:2px 8px; border-radius:4px; font-weight:900; color:#6d28d9; font-size:9px;">{r["GOLS"]}</span></div>'
            
            # TEXTO DETALHADO PARA CÓPIA (7 NÍVEIS)
            s_txt += f"✅ *{r['CASA']} x {r['FORA']}*\n"
            s_txt += f"💰 Vencedor: {r['CONF']} | ⚽ Gols: {r['GOLS']} (Ambos T: SIM)\n"
            s_txt += f"🚩 Cantos: {r['CANTOS']} | 🟨 Cartões: {r['CARTOES']}\n"
            s_txt += f"👟 Chutes: {r['CHUTES']} | 🧤 Defesas: {r['DEFESAS']}\n"
            s_txt += f"🥅 T. Meta: {r['TMETA']}\n--------------------------\n"
        
        b_html += '</div>'
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2: 
            st.markdown(b_html, unsafe_allow_html=True)
            st.markdown("### 📋 COPIAR SINAIS COMPLETOS")
            st.code(s_txt, language="text")

elif st.session_state.aba == "scanner":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    if df is not None:
        confronto = st.selectbox("⚔️ SELECIONE O JOGO", df['CASA'] + " x " + df['FORA'])
        if st.button("⚡ EXECUTAR ALGORITMO", use_container_width=True):
            jogo = df[df['CASA'] + " x " + df['FORA'] == confronto].iloc[0]
            st.session_state.temp_call = jogo # Armazena para salvar
            
            st.markdown(f"<h3 style='color:#9d54ff; text-align:center;'>RESULTADO: {confronto}</h3>", unsafe_allow_html=True)
            k1, k2, k3, k4 = st.columns(4)
            with k1: st.metric("VENCEDOR", jogo['CASA'], jogo['CONF'])
            with k2: st.metric("GOLS", jogo['GOLS'], "OVER 1.5")
            with k3: st.metric("CANTOS", f"{jogo['CANTOS']}+", "ALTO")
            with k4: st.metric("CARTÕES", jogo['CARTOES'], "MÉDIO")
            
            if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True):
                st.session_state.historico_calls.append({
                    "data": datetime.now().strftime("%H:%M"),
                    "jogo": confronto,
                    "resultado": jogo['GOLS'],
                    "conf": jogo['CONF']
                })
                st.toast("✅ CALL SALVA COM SUCESSO!")

elif st.session_state.aba == "historico":
    st.markdown("## 📜 HISTÓRICO DE CALLS SALVAS")
    if not st.session_state.historico_calls:
        st.info("Nenhuma call salva ainda.")
    else:
        for call in reversed(st.session_state.historico_calls):
            st.markdown(f"""<div class="history-card"><b>[{call['data']}]</b> {call['jogo']} <br> Resultado: {call['resultado']} | Confiança: {call['conf']}</div>""", unsafe_allow_html=True)

elif st.session_state.aba == "jogos":
    st.markdown("## 📅 JOGOS ANALISADOS HOJE")
    if df is not None: 
        # Usando st.dataframe em vez de table para evitar cortes e permitir scroll
        st.dataframe(df, use_container_width=True)

elif st.session_state.aba == "banca":
    st.markdown('<div style="background:#003399; padding:20px; border-radius:8px; font-size:24px; font-weight:800; margin-bottom:30px;">💰 GESTÃO DE BANCA INTELIGENTE</div>', unsafe_allow_html=True)
    c_l, c_r = st.columns([1, 2])
    with c_l:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
        st.session_state.stake_padrao = st.slider("STAKE (%)", 0.5, 10.0, 1.0)
    with c_r:
        val_entrada = st.session_state.banca_total * (st.session_state.stake_padrao / 100)
        col1, col2 = st.columns(2)
        col1.metric("VALOR ENTRADA", f"R$ {val_entrada:,.2f}")
        col2.metric("SAÚDE BANCA", "EXCELENTE", "BAIXO RISCO")

st.markdown("""<div style="position:fixed; bottom:0; width:100%; background:#0d0d12; color:#475569; font-size:9px; padding:5px 20px; border-top:1px solid #1e293b;">STATUS: ● IA OPERACIONAL | v93.00 | PROTEÇÃO DE CÓDIGO ATIVA</div>""", unsafe_allow_html=True)
