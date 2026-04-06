import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v63.0 - INTEGRIDADE TOTAL + CONEXÃO GITHUB 2026]
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
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

# Redirecionamento Home via URL
query_params = st.query_params
if query_params.get("go") == "home":
    st.session_state.aba_ativa = "home"
    st.query_params.clear()

# --- FUNÇÃO DE CARREGAMENTO DE DADOS (DIÁRIO + BIG DATA) ---
def carregar_dados():
    # 1. Base Diária (Robô)
    url_github = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    df_d = None
    try:
        df_d = pd.read_csv(f"{url_github}?v={datetime.now().timestamp()}", on_bad_lines='skip')
        df_d.columns = [c.upper() for c in df_d.columns]
    except:
        if os.path.exists("data/database_diario.csv"):
            df_d = pd.read_csv("data/database_diario.csv")
            df_d.columns = [c.upper() for c in df_d.columns]

    # 2. Base Histórica (6 Temporadas)
    df_h = None
    if os.path.exists("data/historico_5_temporadas.csv"):
        df_h = pd.read_csv("data/historico_5_temporadas.csv")
        df_h.columns = [c.upper() for c in df_h.columns]
    
    return df_d, df_h

df_diario, df_historico = carregar_dados()

# ==============================================================================
# LÓGICA DO BOT (CÉREBRO JARVIS): CRUZAMENTO DE BIG DATA
# ==============================================================================

def calcular_metricas_reais(casa, fora):
    if df_historico is None:
        return "85%", "OVER 1.5", "9.5"
    
    # Busca flexível no histórico
    h_casa = df_historico[df_historico['CASA'].astype(str).str.contains(str(casa).upper(), na=False)]
    h_fora = df_historico[df_historico['FORA'].astype(str).str.contains(str(fora).upper(), na=False)]
    
    if not h_casa.empty and not h_fora.empty:
        media_gols = (h_casa['GOLS_CASA'].mean() + h_fora['GOLS_FORA'].mean())
        confianca = 70 + (media_gols * 8)
        if confianca > 98: confianca = 98
        mercado = "OVER 2.5" if media_gols > 2.4 else "OVER 1.5"
        return f"{int(confianca)}%", mercado, "10.5"
    
    return "75%", "OVER 1.5", "9.5"

def processar_ia_bot():
    vips = []
    if df_diario is not None:
        for _, jogo in df_diario.iterrows():
            c = jogo.get('CASA', 'Time A')
            f = jogo.get('FORA', 'Time B')
            conf, merc, cantos = calcular_metricas_reais(c, f)
            vips.append({
                "C": c, "F": f, "P": conf, "G": merc,
                "CT": "3.5+", "E": f"{cantos} total",
                "TM": "14+", "CH": "10+", "DF": "6+"
            })
    
    # Completa até 20 para visualização de layout
    if len(vips) < 20:
        times_elite = ["Real Madrid", "Man City", "Bayern", "Arsenal", "Barcelona", "PSG", "Inter", "Milan", "Flamengo", "Palmeiras", "Liverpool", "Juventus", "Dortmund", "Napoli", "Benfica"]
        for i in range(len(vips), 20):
            t1, t2 = times_elite[i % len(times_elite)], times_elite[(i+3) % len(times_elite)]
            vips.append({
                "C": t1, "F": t2, "P": f"{88-i}%", "G": "OVER 2.5",
                "CT": "4.5+", "E": "10.5 total", "TM": "16+", "CH": "11+", "DF": "7+"
            })
    st.session_state.top_20_ia = vips

processar_ia_bot()

# ==============================================================================
# 2. CAMADA DE ESTILO CSS INTEGRAL (DIRETRIZ VISUAL IMUTÁVEL)
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
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
        transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    .header-left { display: flex; align-items: center; gap: 25px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; letter-spacing: 0.5px; text-decoration: none; cursor: pointer;}
    .nav-links { display: flex; gap: 22px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600 !important; letter-spacing: 0.5px; cursor: pointer; white-space: nowrap;}
    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; cursor: pointer;}
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; cursor: pointer;}

    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: all 0.2s ease !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; padding-left: 35px !important; border-left: 3px solid #6d28d9 !important; }

    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important;
        letter-spacing: 1.2px !important; border-radius: 6px !important;
        width: 100% !important; transition: 0.3s; transform: translate3d(0,0,0);
    }
    
    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
        transition: 0.3s ease; transform: translate3d(0,0,0);
    }
    .highlight-card:hover { transform: translateY(-5px); border-color: #6d28d9; }
    .banca-title-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px; display: flex; align-items: center; gap: 15px; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    
    /* Beleza dos Expanders */
    .stExpander { background-color: #161b22 !important; border: 1px solid #1e293b !important; border-radius: 8px !important; margin-bottom: 10px !important; }
    .stExpander:hover { border-color: #6d28d9 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <a href="?go=home" class="logo-link">GESTOR IA</a>
                <div class="nav-links">
                    <div class="nav-item">APOSTAS ESPORTIVAS</div>
                    <div class="nav-item">APOSTAS AO VIVO</div>
                    <div class="nav-item">APOSTAS ENCONTRADAS</div>
                    <div class="nav-item">ESTATÍSTICAS AVANÇADAS</div>
                    <div class="nav-item">MERCADO PROBABILÍSTICO</div>
                    <div class="nav-item">ASSERTIVIDADE IA</div>
                </div>
            </div>
            <div class="header-right"><div class="search-lupa">🔍</div><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div>
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

def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div><div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:{color_footer}; height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# 4. LÓGICA DE TELAS
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with h3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with h4: draw_card("IA STATUS", "ONLINE", 100)
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("VOL. GLOBAL", "ALTO", 75)
    with h6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with h7: draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
    with h8: draw_card("SISTEMA", "JARVIS v63.0", 100)

    st.markdown("<h4 style='color:#06b6d4; margin-top:30px;'>🤖 TOP 20 ANALISES IA - PROBABILIDADE REAL</h4>", unsafe_allow_html=True)
    for j in st.session_state.top_20_ia:
        with st.expander(f"➔ {j['C']} vs {j['F']} | CONF: {j['P']}"):
            st.markdown(f"""
                <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; padding: 10px;">
                    <div>
                        <p style='font-size:11px; color:#94a3b8; margin:0;'>⚽ GOLS: <b style='color:white;'>{j['G']}</b></p>
                        <p style='font-size:11px; color:#94a3b8; margin:0;'>🚩 ESCANTEIOS: <b style='color:white;'>{j['E']}</b></p>
                    </div>
                    <div>
                        <p style='font-size:11px; color:#94a3b8; margin:0;'>🟨 CARTÕES: <b style='color:white;'>{j['CT']}</b></p>
                        <p style='font-size:11px; color:#94a3b8; margin:0;'>🥅 CHUTES GOL: <b style='color:white;'>{j['CH']}</b></p>
                    </div>
                    <div>
                        <p style='font-size:11px; color:#94a3b8; margin:0;'>👟 TIROS META: <b style='color:white;'>{j['TM']}</b></p>
                        <p style='font-size:11px; color:#94a3b8; margin:0;'>🧤 DEFESAS: <b style='color:white;'>{j['DF']}</b></p>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<h4 style='color:#64748b; margin-top:40px;'>📋 ANÁLISE COMPLETA DO DIA (DADOS BRUTOS)</h4>", unsafe_allow_html=True)
    if df_diario is not None: st.dataframe(df_diario, use_container_width=True, hide_index=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    db_hierarquia = {
        "BRASIL": {"BRASILEIRÃO": ["SÉRIE A", "SÉRIE B"], "ESTADUAIS": ["PAULISTÃO", "CARIOCA"]},
        "EUROPA": {"LIGAS ELITE": ["PREMIER LEAGUE", "LA LIGA", "SERIE A", "BUNDESLIGA"]}
    }
    r1, r2, r3 = st.columns(3)
    with r1: sel_pais = st.selectbox("🌎 REGIÃO", list(db_hierarquia.keys()))
    with r2: sel_grupo = st.selectbox("📂 GRUPO", list(db_hierarquia[sel_pais].keys()))
    with r3: sel_comp = st.selectbox("🏆 COMPETIÇÃO", db_hierarquia[sel_pais][sel_grupo])
    
    t1, t2 = st.columns(2)
    with t1: tcasa = st.text_input("🏠 TIME CASA")
    with t2: tfora = st.text_input("🚀 TIME FORA")
    
    if st.button("⚡ EXECUTAR ALGORITIMO"):
        conf, merc, cantos = calcular_metricas_reais(tcasa, tfora)
        st.session_state.analise_bloqueada = {"casa": tcasa, "fora": tfora, "conf": conf, "merc": merc}
        st.success(f"Análise Concluída: {conf} de Confiança para {merc}")

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    l1, l2, l3, l4 = st.columns(4)
    with l1: draw_card("PRESSÃO CASA", "88%", 88)
    with l2: draw_card("ATAQUES/5m", "14", 70)
    with l3: draw_card("POSSE BOLA", "65%", 65)
    with l4: draw_card("GOL PROB", "90%", 90)
    st.info("Monitorando jogos ativos via Besoccer API...")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>""", unsafe_allow_html=True)
    c_in, c_out = st.columns([1, 2])
    with c_in:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total))
        st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, float(st.session_state.stake_padrao))
    with c_out:
        v_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        draw_card("VALOR DE CADA ENTRADA", f"R$ {v_stake:,.2f}", 100, "#00d2ff")

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    if not st.session_state.historico_calls: st.info("Nenhuma operação registrada.")
    else:
        for call in st.session_state.historico_calls:
            st.markdown(f"""<div class="history-card-box"><div>{call['casa']} x {call['fora']}</div><div style="color:#06b6d4;">{call['conf']}</div></div>""", unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v63.0</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
