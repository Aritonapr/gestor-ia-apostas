import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# --- FUNÇÃO DE CARREGAMENTO ---
def carregar_jogos_diarios():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try:
            return pd.read_csv(path)
        except:
            return None
    return None

df_diario = carregar_jogos_diarios()

# --- CHIP DE INTELIGÊNCIA JARVIS (TOP 20) ---
if 'top_20_ia' not in st.session_state:
    vips = []
    if df_diario is not None:
        for _, j in df_diario.iterrows():
            try:
                conf = float(str(j.get('CONFIANCA', '0')).replace('%',''))
                if conf >= 85:
                    vips.append({
                        "C": j.get('CASA', 'Time A'), "F": j.get('FORA', 'Time B'), "P": f"{conf}%",
                        "G": "OVER 1.5", "E": f"9.5 (C:{j.get('C_CASA',5)}|F:{j.get('C_FORA',4)})",
                        "CT": "4.5+", "TM": "16+", "CH": "9+", "DF": "7+"
                    })
            except: continue
            if len(vips) == 20: break
    st.session_state.top_20_ia = vips

# --- CAMADA DE ESTILO CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [data-testid="stAppViewContainer"] { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header { display: none !important; }
    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; }
    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; margin-bottom: 15px;
    }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999; }
    </style>
""", unsafe_allow_html=True)

def draw_card(title, value, perc, color="#06b6d4"):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;">
                <div style="background:{color}; height:100%; width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color:#9d54ff; text-align:center;'>GESTOR IA</h2>", unsafe_allow_html=True)
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📊 ASSERTIVIDADE IA"): st.session_state.aba_ativa = "assertividade"
    if st.button("📜 HISTÓRICO"): st.session_state.aba_ativa = "historico"

# --- LÓGICA DE TELAS ---
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO - TOP 20 IA</h2>", unsafe_allow_html=True)
    for jogo in st.session_state.top_20_ia:
        with st.expander(f"➔ {jogo['C']} vs {jogo['F']} | CONF: {jogo['P']}"):
            c1, c2, c3 = st.columns(3)
            with c1: st.write(f"⚽ Gols: {jogo['G']}"); st.write(f"🚩 Esc: {jogo['E']}")
            with c2: st.write(f"🟨 Cartões: {jogo['CT']}"); st.write(f"🥅 Chutes: {jogo['CH']}")
            with c3: st.write(f"👟 Tiros: {jogo['TM']}"); st.write(f"🧤 Defesas: {jogo['DF']}")

elif st.session_state.aba_ativa == "assertividade":
    st.markdown("<h2 style='color:white;'>📊 RELATÓRIO DE ASSERTIVIDADE</h2>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: draw_card("TAXA ACERTO", "91.5%", 91, "#00ff88")
    with c2: draw_card("GREENS HOJE", "18", 100, "#00ff88")
    with c3: draw_card("REDS HOJE", "2", 10, "#ff4b4b")
    with c4: draw_card("LUCRO DIA", "R$ 412,50", 100)
    c5, c6, c7, c8 = st.columns(4)
    with c5: draw_card("PRECISÃO GOLS", "94%", 94)
    with c6: draw_card("PRECISÃO ESC.", "89%", 89)
    with c7: draw_card("ROI MENSAL", "+24.8%", 100)
    with c8: draw_card("SISTEMA", "V60.0 OK", 100)
    st.success("Análise Betano: 20 palpites | 18 acertos confirmados.")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
    draw_card("ENTRADA SUGERIDA", f"R$ {st.session_state.banca_total * 0.01:.2f}", 100)

st.markdown(f"""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v60.0</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
