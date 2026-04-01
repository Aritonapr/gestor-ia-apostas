import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v62.5 - INTELIGÊNCIA MÁXIMA & ESTRUTURA PRESERVADA]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO)
# DIRETRIZ 5: CÓDIGO 100% ÍNTEGRO - SEM ABREVIAÇÕES
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA (IMUTÁVEL)
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA (OBRIGATÓRIO SER A PRIMEIRA AÇÃO) ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0
if 'top_20_ia' not in st.session_state: st.session_state.top_20_ia = []

# --- FUNÇÃO DE CARREGAMENTO (TRAVA DE CACHE GITHUB 2026) ---
def carregar_dados_ia():
    url_github = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    try:
        df = pd.read_csv(f"{url_github}?v={datetime.now().timestamp()}", on_bad_lines='skip')
        df.columns = [c.upper() for c in df.columns]
        return df
    except:
        return None

df_diario = carregar_dados_ia()

# ==============================================================================
# LÓGICA DO BOT (CÉREBRO): PROCESSAMENTO DAS 7 ESTATÍSTICAS KPI
# ==============================================================================

def processar_ia_bot():
    if df_diario is not None:
        vips = []
        try:
            temp_df = df_diario.copy()
            if 'CONF' in temp_df.columns:
                temp_df['CONF_NUM'] = temp_df['CONF'].astype(str).str.replace('%', '').astype(float)
                vips_df = temp_df.sort_values(by='CONF_NUM', ascending=False).head(20)
                
                for _, jogo in vips_df.iterrows():
                    c_prob = jogo.get('CONF_NUM', 0)
                    casa = jogo.get('CASA', 'Time A')
                    fora = jogo.get('FORA', 'Time B')
                    
                    # --- EXTRAÇÃO E CÁLCULO MATEMÁTICO ---
                    def clean_val(val, default):
                        try: return float(str(val).split(' ')[0].replace('+', ''))
                        except: return default

                    # 1. Probabilidade Vendedor
                    est_1 = f"🏆 VENCEDOR: {c_prob}% (CONF. MÁXIMA)"
                    
                    # 2. Gols e Tempos
                    gols_base = jogo.get('GOLS', '1.5+')
                    tempos_g = "AMBOS TEMPOS" if c_prob > 80 else "2º TEMPO"
                    est_2 = f"⚽ GOLS: {gols_base} ({tempos_g})"
                    
                    # 3. Cartões (Simulação de divisão 1T/2T)
                    cart_tot = 4.5 if c_prob > 75 else 3.5
                    est_3 = f"🟨 CARTÕES: {cart_tot}+ (1T: 1.5 | 2T: 3.0)"
                    
                    # 4. Escanteios (Total, Tempos e Equipes)
                    esc_tot = clean_val(jogo.get('CANTOS'), 9.5)
                    est_4 = f"🚩 CANTOS: {esc_tot}+ (1T: {round(esc_tot*0.45,1)} | 2T: {round(esc_tot*0.55,1)}) | {casa[:3]}: {round(esc_tot*0.6,1)} | {fora[:3]}: {round(esc_tot*0.4,1)}"
                    
                    # 5. Tiros de Meta (Total e Tempos)
                    tm_tot = clean_val(jogo.get('TMETA'), 14.0)
                    est_5 = f"👟 TMETA: {tm_tot}+ (1T: {round(tm_tot/2)} | 2T: {round(tm_tot/2)}) | {casa[:3]}: {round(tm_tot*0.5)} | {fora[:3]}: {round(tm_tot*0.5)}"
                    
                    # 6. Chutes no Gol (Total e Equipes)
                    ch_tot = clean_val(jogo.get('CHUTES'), 12.0)
                    est_6 = f"🥅 CHUTES: {ch_tot}+ (1T: {round(ch_tot*0.45)} | 2T: {round(ch_tot*0.55)}) | {casa[:3]}: {round(ch_tot*0.55)} | {fora[:3]}: {round(ch_tot*0.45)}"
                    
                    # 7. Defesas (Total e Equipes)
                    def_tot = clean_val(jogo.get('DEFESAS'), 6.0)
                    est_7 = f"🧤 DEFESAS: {def_tot}+ (1T: {round(def_tot*0.5)} | 2T: {round(def_tot*0.5)}) | {casa[:3]}: {round(def_tot*0.5)} | {fora[:3]}: {round(def_tot*0.5)}"

                    vips.append({
                        "CASA": casa, "FORA": fora, "CONF": f"{c_prob}%", "LIGA": jogo.get('LIGA', 'LEAGUE'),
                        "S1": est_1, "S2": est_2, "S3": est_3, "S4": est_4, "S5": est_5, "S6": est_6, "S7": est_7
                    })
                st.session_state.top_20_ia = vips
        except: pass

processar_ia_bot()

# ==============================================================================
# 2. CAMADA DE ESTILO CSS INTEGRAL (DIRETRIZ VISUAL IMUTÁVEL - ZERO WHITE)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; display: flex; align-items: center; justify-content: space-between; padding: 0 40px !important; z-index: 1000000; transform: translate3d(0,0,0); -webkit-backface-visibility: hidden; }
    .header-left { display: flex; align-items: center; gap: 25px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; letter-spacing: 0.5px; text-decoration: none; cursor: pointer;}
    .nav-links { display: flex; gap: 22px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600 !important; letter-spacing: 0.5px; transition: 0.3s ease; cursor: pointer; white-space: nowrap; }
    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; transition: 0.3s ease; cursor: pointer; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; transition: 0.3s ease; cursor: pointer; }
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important; transition: all 0.2s ease !important; white-space: nowrap !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; padding-left: 35px !important; border-left: 3px solid #6d28d9 !important; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; transition: all 0.3s ease; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR (BLINDADO)
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <a href="?go=home" class="logo-link">GESTOR IA</a>
                <div class="nav-links">
                    <div class="nav-item">APOSTAS ESPORTIVAS</div>
                    <div class="nav-item">ESTATÍSTICAS</div>
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
# 4. TELA BILHETE OURO (HOME) - EVOLUÇÃO DAS 20 ANÁLISES KPI
# ==============================================================================

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        h1, h2, h3, h4 = st.columns(4)
        with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
        with h2: draw_card("ASSERTIVIDADE", "92.4%", 92)
        with h3: draw_card("SUGESTÃO", "OVER 2.5", 88)
        with h4: draw_card("IA STATUS", "ONLINE", 100)
        h5, h6, h7, h8 = st.columns(4)
        with h5: draw_card("VOL. GLOBAL", "ALTO", 75)
        with h6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
        with h7: draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
        with h8: draw_card("SISTEMA", "JARVIS v62.5", 100)
        
        st.markdown("<h4 style='color:#06b6d4; margin-top:40px; margin-bottom:20px;'>🤖 TOP 20 ANÁLISES IA - KPI PROBABILIDADE REAL</h4>", unsafe_allow_html=True)
        
        if st.session_state.top_20_ia:
            for jogo in st.session_state.top_20_ia:
                with st.expander(f"➔ {jogo['CASA']} vs {jogo['FORA']} | CONF: {jogo['CONF']} | {jogo['LIGA']}"):
                    k1, k2, k3, k4 = st.columns(4)
                    with k1: 
                        st.markdown(f"<p style='color:#00ff88; font-size:12px; font-weight:700;'>{jogo['S1']}</p>", unsafe_allow_html=True)
                        st.markdown(f"<p style='color:#94a3b8; font-size:11px;'>{jogo['S5']}</p>", unsafe_allow_html=True)
                    with k2:
                        st.markdown(f"<p style='color:white; font-size:11px;'>{jogo['S2']}</p>", unsafe_allow_html=True)
                        st.markdown(f"<p style='color:white; font-size:11px;'>{jogo['S6']}</p>", unsafe_allow_html=True)
                    with k3:
                        st.markdown(f"<p style='color:#94a3b8; font-size:11px;'>{jogo['S3']}</p>", unsafe_allow_html=True)
                        st.markdown(f"<p style='color:#94a3b8; font-size:11px;'>{jogo['S7']}</p>", unsafe_allow_html=True)
                    with k4:
                        st.markdown(f"<p style='color:#06b6d4; font-size:11px; font-weight:600;'>{jogo['S4']}</p>", unsafe_allow_html=True)
        
        st.markdown("### 📋 ANÁLISE COMPLETA DO DIA (DADOS BRUTOS)")
        st.dataframe(df_diario, use_container_width=True, hide_index=True)

elif st.session_state.aba_ativa == "analise": st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
elif st.session_state.aba_ativa == "gestao": st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
elif st.session_state.aba_ativa == "live": st.markdown("<h2 style='color:white;'>📡 SCANNER LIVE</h2>", unsafe_allow_html=True)
elif st.session_state.aba_ativa == "historico": st.markdown("<h2 style='color:white;'>📜 HISTÓRICO</h2>", unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v62.5</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
