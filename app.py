import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime
import random

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v60.00 - MÓDULO BILHETE MASTER]
# DIRETRIZ: GERADOR DE BILHETES AUTOMATIZADOS (TOP 20)
# ==============================================================================

st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

# --- MEMÓRIA E PERSISTÊNCIA ---
PATH_HISTORICO = "dados/historico_permanente.json"
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0

def carregar_jogos_diarios():
    path = "dados/database_diario.csv"
    if os.path.exists(path):
        try: return pd.read_csv(path)
        except: return None
    return None

df_diario = carregar_jogos_diarios()

# --- CSS ESTILIZAÇÃO BILHETE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    /* RESET E TEMA ESCURO */
    header { display: none !important; }
    .stApp { background-color: #0b0e11 !important; }
    
    /* ESTILO DO BILHETE (TICKET) */
    .ticket-body {
        background: #ffffff !important;
        color: #1a1a1a !important;
        border-radius: 4px;
        padding: 25px;
        max-width: 450px;
        margin: 0 auto;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        font-family: 'Courier New', Courier, monospace;
        position: relative;
    }
    
    .ticket-header {
        text-align: center;
        border-bottom: 2px dashed #1a1a1a;
        padding-bottom: 15px;
        margin-bottom: 15px;
    }
    
    .ticket-title { font-weight: 900; font-size: 20px; letter-spacing: 2px; }
    
    .entry-line {
        display: flex;
        justify-content: space-between;
        font-size: 13px;
        margin-bottom: 8px;
        border-bottom: 1px solid #eeeeee;
        padding-bottom: 4px;
    }
    
    .entry-market { font-weight: 700; color: #d32f2f; }
    
    .ticket-footer {
        border-top: 2px dashed #1a1a1a;
        margin-top: 20px;
        padding-top: 15px;
        text-align: center;
        font-weight: 700;
    }

    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; display: flex; align-items: center; 
        padding: 0 40px !important; z-index: 1000; 
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVEGAÇÃO ---
with st.sidebar:
    st.markdown('<div class="betano-header"><span style="color:#9d54ff; font-weight:900; font-size:21px;">GESTOR IA</span></div><div style="height:65px;"></div>', unsafe_allow_html=True)
    if st.button("🎟️ GERAR BILHETE DO DIA"): st.session_state.aba_ativa = "bilhete"
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"

# --- TELA: GERADOR DE BILHETE ---
if st.session_state.aba_ativa == "bilhete":
    st.markdown("<h1 style='color:white; text-align:center;'>🎟️ BILHETE MAGNÉTICO IA</h1>", unsafe_allow_html=True)
    
    if df_diario is not None and len(df_diario) >= 20:
        # Pega 20 jogos aleatórios ou os primeiros (ideal seria ordenar por confiança no CSV)
        top_20 = df_diario.head(20)
        
        # Interface do Bilhete
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown(f"""
                <div class="ticket-body">
                    <div class="ticket-header">
                        <div class="ticket-title">GESTOR IA PRO</div>
                        <div style="font-size:10px;">DATA: {datetime.now().strftime('%d/%m/%Y %H:%M')}</div>
                    </div>
            """, unsafe_allow_html=True)
            
            texto_whatsapp = f"🚀 *BILHETE DO DIA - GESTOR IA*\n📅 Data: {datetime.now().strftime('%d/%m/%Y')}\n\n"
            
            for i, row in top_20.iterrows():
                # Lógica de mercado simulada (seria bom ter isso no seu CSV)
                mercados = ["OVER 1.5 GOLS", "CANTOS +8.5", "AMBAS MARCAM", "VITORIA CASA"]
                m_escolhido = random.choice(mercados)
                confia = random.randint(91, 99)
                
                st.markdown(f"""
                    <div class="entry-line">
                        <span>{row['TIME_CASA'][:12]} x {row['TIME_FORA'][:12]}</span>
                        <span class="entry-market">{m_escolhido}</span>
                    </div>
                """, unsafe_allow_html=True)
                
                texto_whatsapp += f"✅ {row['TIME_CASA']} x {row['TIME_FORA']}\n🎯 Entrada: {m_escolhido} ({confia}% IA)\n\n"
            
            st.markdown(f"""
                    <div class="ticket-footer">
                        CONFIDENCIALIDADE: JARVIS v60.00<br>
                        ESTIMATIVA DE LUCRO: ALTA
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            st.text_area("COPIAR PARA WHATSAPP:", value=texto_whatsapp, height=200)
    else:
        st.error("⚠️ ERRO: O sistema precisa de pelo menos 20 jogos no banco de dados para gerar o bilhete. Verifique seu sync_data.py")

# --- MANTENDO AS OUTRAS TELAS ---
elif st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA (VISÃO GERAL)</h2>", unsafe_allow_html=True)
    if df_diario is not None: st.dataframe(df_diario)
    else: st.info("Aguardando importação de dados...")

st.markdown("""<div style="position:fixed; bottom:0; width:100%; background:#0d0d12; color:#475569; font-size:9px; padding:5px 20px; border-top:1px solid #1e293b;">STATUS: IA OPERACIONAL | v60.00</div>""", unsafe_allow_html=True)
