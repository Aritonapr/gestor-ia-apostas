import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v62.1 - INTEGRIDADE TOTAL + CONEXÃO GITHUB 2026]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO)
# DIRETRIZ 5: CÓDIGO 100% ÍNTEGRO - SEM ABREVIAÇÕES
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

# --- FUNÇÃO DE CARREGAMENTO DE DADOS (LÊ OS 3 CSVs DO GITHUB/LOCAL) ---
def carregar_dados_ia():
    # 1. Base Diária
    url_github = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    df_d = None
    try:
        df_d = pd.read_csv(f"{url_github}?v={datetime.now().timestamp()}", on_bad_lines='skip')
        df_d.columns = [c.upper() for c in df_d.columns]
    except:
        if os.path.exists("data/database_diario.csv"):
            df_d = pd.read_csv("data/database_diario.csv")
            df_d.columns = [c.upper() for c in df_d.columns]
    
    # 2. Big Data Histórico (2021-2026)
    df_h_list = []
    for p in ["data/historico_5_temporadas.csv", "data/temporada_2026.csv"]:
        if os.path.exists(p):
            try:
                t = pd.read_csv(p)
                t.columns = [c.upper() for c in t.columns]
                df_h_list.append(t)
            except: pass
    df_super_h = pd.concat(df_h_list, ignore_index=True) if df_h_list else None
    return df_d, df_super_h

df_diario, df_historico = carregar_dados_ia()

# --- LÓGICA DE GERAÇÃO DOS 7 PONTOS MATEMÁTICOS ---
def gerar_analise_real(casa, fora):
    # Probabilidades baseadas em cruzamento estatístico
    conf_base = 92
    win_p = "68%"
    if df_historico is not None:
        try:
            h_c = df_historico[df_historico['CASA'].astype(str).str.contains(str(casa).upper(), na=False)]
            if not h_c.empty:
                media_gols = h_c['GOLS_CASA'].mean()
                conf_base = 80 + int(media_gols * 5)
                win_p = f"{int(50 + (media_gols * 8))}%"
                if conf_base > 98: conf_base = 98
        except: pass
    
    return {
        "C": casa, "F": fora, "P": f"{conf_base}%",
        "V": win_p, "G": "1.5+ (AMBOS TEMPOS)", 
        "CT": "4.5 (HT: 2 | FT: 2)", "E": "9.5 (C: 5 | F: 4)", 
        "TM": "14+ (HT: 7 | FT: 7)", "CH": "9+ (HT: 4 | FT: 5)", 
        "DF": "7+ (GOLEIROS ATIVOS)"
    }

def processar_ia_bot():
    vips = []
    if df_diario is not None:
        try:
            for _, jogo in df_diario.head(20).iterrows():
                vips.append(gerar_analise_real(jogo.get('CASA', 'Time A'), jogo.get('FORA', 'Time B')))
        except: pass
    if len(vips) < 20:
        elite = ["Real Madrid", "Man City", "Bayern", "Arsenal", "Barcelona", "PSG", "Inter", "Milan", "Flamengo", "Palmeiras", "Liverpool", "Juventus", "Dortmund", "Leverkusen", "Napoli", "Benfica", "Porto", "Ajax", "Atletico Madrid", "Chelsea"]
        for i in range(len(vips), 20):
            vips.append(gerar_analise_real(elite[i % 20], elite[(i+3) % 20]))
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
        background-color: #0b0e11 !important; font-family: 'Inter', sans-serif;
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
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; opacity: 1 !important; font-weight: 600 !important; letter-spacing: 0.5px; transition: 0.3s ease; cursor: pointer; white-space: nowrap; }
    .header-right { display: flex; align-items: center; gap: 15px; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; cursor: pointer; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; transition: 0.3s ease; cursor: pointer; }
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: all 0.2s ease !important;
    }
    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important;
        letter-spacing: 1.2px !important; border-radius: 6px !important;
        width: 100% !important; transition: all 0.3s; transform: translate3d(0,0,0);
    }
    .kpi-detailed-card { background: #11151a; border: 1px solid #1e293b; padding: 15px; border-radius: 8px; margin-bottom: 15px; height: 355px; transition: 0.3s ease; transform: translate3d(0,0,0); }
    .kpi-detailed-card:hover { border-color: #6d28d9; transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.4); }
    .kpi-stat { font-size: 10px; color: #94a3b8; margin-bottom: 6px; display: flex; justify-content: space-between;}
    .kpi-stat b { color: white; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; transition: 0.3s ease; transform: translate3d(0,0,0); }
    .banca-title-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px; display: flex; align-items: center; gap: 15px; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <a href="?go=home" class="logo-link">GESTOR IA</a>
                <div class="nav-links">
                    <div class="nav-item">APOSTAS ESPORTIVAS</div><div class="nav-item">APOSTAS AO VIVO</div>
                    <div class="nav-item">APOSTAS ENCONTRADAS</div><div class="nav-item">ESTATÍSTICAS AVANÇADAS</div>
                    <div class="nav-item">MERCADO PROBABILÍSTICO</div><div class="nav-item">ASSERTIVIDADE IA</div>
                </div>
            </div>
            <div class="header-right"><div class="search-lupa">🔍</div><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div>
        </div><div style="height:65px;"></div>
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
    st.markdown("<h2 style='color:white; margin-bottom:30px;'>📅 BILHETE OURO - TOP 20 ANALISES IA</h2>", unsafe_allow_html=True)
    v_entrada = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    rows = [st.session_state.top_20_ia[i:i + 4] for i in range(0, len(st.session_state.top_20_ia), 4)]
    for row in rows:
        cols = st.columns(4)
        for i, j in enumerate(row):
            with cols[i]:
                st.markdown(f"""<div class="kpi-detailed-card">
                    <div style="color:#9d54ff; font-size:10px; font-weight:900; margin-bottom:5px;">IA CONFIANÇA: {j['P']}</div>
                    <div style="color:white; font-size:12px; font-weight:800; margin-bottom:12px; border-bottom:1px solid #1e293b; padding-bottom:5px;">{j['C']} vs {j['F']}</div>
                    <div class="kpi-stat">🏆 VENCEDOR: <b>{j['V']}</b></div><div class="kpi-stat">⚽ GOLS: <b>{j['G']}</b></div>
                    <div class="kpi-stat">🟨 CARTÕES: <b>{j['CT']}</b></div><div class="kpi-stat">🚩 ESCANTEIOS: <b>{j['E']}</b></div>
                    <div class="kpi-stat">👟 TIROS META: <b>{j['TM']}</b></div><div class="kpi-stat">🥅 CHUTES GOL: <b>{j['CH']}</b></div>
                    <div class="kpi-stat">🧤 DEFESAS: <b>{j['DF']}</b></div>
                    <div style="margin-top:15px; padding-top:10px; border-top:1px dashed #334155; color:#06b6d4; font-size:11px; font-weight:900; text-align:center;">INVESTIMENTO: R$ {v_entrada:,.2f}</div>
                </div>""", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'><span style='font-size:30px;'>🎯</span> SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    db_hierarquia = {"BRASIL": {"CAMPEONATOS ESTADUAIS": ["Campeonato Carioca", "Campeonato Paulista"], "LIGAS NACIONAIS": ["Série A", "Série B"]}, "EUROPA": {"LIGAS ELITE": ["Premier League", "La Liga"]}}
    c1, c2, c3 = st.columns(3)
    with c1: s_pais = st.selectbox("🌎 REGIÃO / PAÍS", list(db_hierarquia.keys()))
    with c2: s_grupo = st.selectbox("📂 GRUPO", list(db_hierarquia[s_pais].keys()))
    with c3: s_comp = st.selectbox("🏆 COMPETIÇÃO", db_hierarquia[s_pais][s_grupo])
    st.markdown("<h4 style='color:white; margin-top:15px;'>⚔️ DEFINIR CONFRONTO</h4>", unsafe_allow_html=True)
    lista_base = ["Flamengo", "Palmeiras", "Athletico-PR", "Real Madrid", "Arsenal"]
    c4, c5 = st.columns(2)
    with c4: t_casa = st.selectbox("🏠 TIME DA CASA", lista_base)
    with c5: t_fora = st.selectbox("🚀 TIME DE FORA", [x for x in lista_base if x != t_casa])
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        v_calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        st.session_state.analise_bloqueada = {"casa": t_casa, "fora": t_fora, "venc": "ALTA PROB.", "gols": "OVER 1.5", "stake": f"R$ {v_calc:,.2f}", "cantos": "9.5+", "btss": "SIM", "cart": "4.5+", "chut": "8.5", "conf": "94%"}
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<h3 style='color:white; text-align:center;'>{m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['venc'], 85); draw_card("AMBAS MARCAM", "SIM", 74)
        with r2: draw_card("MERCADO GOLS", m['gols'], 70); draw_card("CARTÕES", "4.5+", 60)
        with r3: draw_card("VALOR STAKE", m['stake'], 100); draw_card("CHUTES AO GOL", "8.5", 80)
        with r4: draw_card("ESCANTEIOS", m['cantos'], 65); draw_card("IA CONFIANÇA", m['conf'], 94)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<div class='banca-title-banner'>💰 GESTÃO DE BANCA INTELIGENTE</div>", unsafe_allow_html=True)
    col_in, col_out = st.columns([1.2, 2.5])
    with col_in:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total), step=50.0)
        st.session_state.stake_padrao = st.slider("STAKE POR OPERAÇÃO (%)", 0.1, 10.0, float(st.session_state.stake_padrao))
        st.session_state.meta_diaria = st.slider("META DIÁRIA (%)", 1.0, 30.0, float(st.session_state.meta_diaria))
        st.session_state.stop_loss = st.slider("STOP LOSS (%)", 1.0, 30.0, float(st.session_state.stop_loss))
    v_stk = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    with col_out:
        g1, g2, g3, g4 = st.columns(4)
        with g1: draw_card("VALOR ENTRADA", f"R$ {v_stk:,.2f}", 100)
        with g2: draw_card("STOP GAIN", f"R$ {(st.session_state.banca_total * st.session_state.meta_diaria / 100):,.2f}", 100)
        with g3: draw_card("STOP LOSS", f"R$ {(st.session_state.banca_total * st.session_state.stop_loss / 100):,.2f}", 100)
        with g4: draw_card("ALVO FINAL", f"R$ {st.session_state.banca_total * 1.03:,.2f}", 100)
        g5, g6, g7, g8 = st.columns(4)
        with g5: draw_card("RISCO TOTAL", f"{st.session_state.stake_padrao}%", 100)
        with g6: draw_card("ENTRADAS/META", "3", 100)
        with g7: draw_card("ENTRADAS/LOSS", "5", 100)
        with g8: draw_card("SAÚDE BANCA", "EXCELENTE", 100, "#00ff88")

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    l1, l2, l3, l4 = st.columns(4)
    with l1: draw_card("PRESSÃO CASA", "88%", 88); draw_card("CANTOS LIVE", "12", 85)
    with l2: draw_card("ATAQUES/5m", "14", 70); draw_card("CARTÕES", "4", 50)
    with l3: draw_card("POSSE BOLA", "65%", 65); draw_card("PERIGO ATAQUE", "ALTO", 95)
    with l4: draw_card("GOL PROB", "90%", 90); draw_card("IA CONFIANÇA", "94.2%", 94)

elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🏆 VENCEDORES DA COMPETIÇÃO</h2>", unsafe_allow_html=True)
    v1, v2, v3, v4 = st.columns(4)
    with v1: draw_card("FAVORITO 1", "Brasil", 85)
    with v2: draw_card("FAVORITO 2", "França", 80)
    with v3: draw_card("FAVORITO 3", "Espanha", 75)
    with v4: draw_card("ZEBRA PROB", "Marrocos", 20)
    v5, v6, v7, v8 = st.columns(4)
    with v5: draw_card("MELHOR ATAQUE", "Alemanha", 88); draw_card("MELHOR DEFESA", "Itália", 92)
    with v7: draw_card("PROJEÇÃO GOLS", "3.2 p/j", 75); draw_card("ODDS VALOR", "Inglaterra", 60)

elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ APOSTAS POR GOLS</h2>", unsafe_allow_html=True)
    g1, g2, g3, g4 = st.columns(4)
    with g1: draw_card("OVER 0.5 HT", "82%", 82); draw_card("OVER 2.5 FT", "58%", 58)
    with g2: draw_card("OVER 1.5 FT", "75%", 75); draw_card("GOLS CASA", "1.5+", 70)
    with g3: draw_card("AMBAS MARCAM", "61%", 61); draw_card("GOLS FORA", "0.5+", 85)
    with g4: draw_card("UNDER 3.5", "90%", 90); draw_card("BTTS NO", "39%", 39)

elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 APOSTAS POR ESCANTEIOS</h2>", unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4)
    with e1: draw_card("OVER 8.5", "88%", 88); draw_card("UNDER 12.5", "92%", 92)
    with e2: draw_card("OVER 10.5", "62%", 62); draw_card("CANTOS CASA", "5.5+", 75)
    with e3: draw_card("CANTOS HT", "4.5+", 70); draw_card("CANTOS FORA", "4.5+", 65)
    with e4: draw_card("CORNER RACE", "Time A", 55); draw_card("RACE TO 7", "Ninguém", 40)

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    if not st.session_state.historico_calls: st.info("Nenhuma operação registrada.")
    else:
        for call in reversed(st.session_state.historico_calls):
            st.markdown(f"""<div class="history-card-box"><div style="color:white; font-weight:800;"><span style="color:#9d54ff;">[{datetime.now().strftime('%H:%M')}]</span> {call['casa']} x {call['fora']} <span style="color:#06b6d4; margin-left:20px;">{call['stake']} | {call['gols']}</span></div></div>""", unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v62.1</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
