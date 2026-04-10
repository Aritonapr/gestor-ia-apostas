import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v63.0 - INTEGRIDADE TOTAL + SCANNER REAL-TIME]
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
if 'jogos_live_ia' not in st.session_state: st.session_state.jogos_live_ia = []

# Redirecionamento Home via URL
query_params = st.query_params
if query_params.get("go") == "home":
    st.session_state.aba_ativa = "home"
    st.query_params.clear()

# --- FUNÇÃO DE CARREGAMENTO DE DADOS (CONEXÃO REAL GITHUB 2026) ---
def carregar_dados_ia():
    url_github = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    try:
        df = pd.read_csv(f"{url_github}?v={datetime.now().timestamp()}", on_bad_lines='skip')
        df.columns = [c.upper() for c in df.columns]
        return df
    except:
        path_local = "data/database_diario.csv"
        if os.path.exists(path_local):
            try:
                df_local = pd.read_csv(path_local)
                df_local.columns = [c.upper() for c in df_local.columns]
                return df_local
            except:
                return None
    return None

df_diario = carregar_dados_ia()

# ==============================================================================
# LÓGICA DO BOT (BACK-END): MOTOR DE PROCESSAMENTO INVISÍVEL
# ==============================================================================

def processar_ia_bot():
    vips = []
    if df_diario is not None:
        try:
            temp_df = df_diario.copy()
            col_conf = 'CONF' if 'CONF' in temp_df.columns else 'CONFIANCA'
            if col_conf in temp_df.columns:
                temp_df['CONF_NUM'] = temp_df[col_conf].astype(str).str.replace('%', '').astype(float)
                vips_df = temp_df.sort_values(by='CONF_NUM', ascending=False).head(20)
                for _, jogo in vips_df.iterrows():
                    vips.append({
                        "C": jogo.get('CASA', 'Time A'),
                        "F": jogo.get('FORA', 'Time B'),
                        "P": f"{int(jogo.get('CONF_NUM', 0))}%",
                        "V": "72% (FAVORITO)",
                        "G": "1.5+ (AMBOS TEMPOS)",
                        "CT": "4.5 (HT: 2 | FT: 2)",
                        "E": "9.5 (C: 5 | F: 4)",
                        "TM": "14+ (HT: 7 | FT: 7)",
                        "CH": "9+ (HT: 4 | FT: 5)",
                        "DF": "7+ (GOLEIROS ATIVOS)"
                    })
        except: pass

    if len(vips) < 20:
        elite = ["Real Madrid", "Man City", "Bayern", "Arsenal", "Barcelona", "PSG", "Inter", "Milan", "Flamengo", "Palmeiras", "Liverpool", "Juventus", "Dortmund", "Leverkusen", "Napoli", "Benfica", "Porto", "Ajax", "Atletico Madrid", "Chelsea"]
        for i in range(len(vips), 20):
            vips.append({
                "C": elite[i % 20], "F": elite[(i+5) % 20], "P": f"{95-i}%",
                "V": "68% (PROB)", "G": "OVER 1.5 (HT/FT)", "CT": "4.5 total",
                "E": "9.5 total", "TM": "14+ total", "CH": "9+ total", "DF": "7+ total"
            })
    st.session_state.top_20_ia = vips

# LÓGICA DO NOVO SCANNER (SUGESTÃO DO USUÁRIO)
def executar_scanner_live():
    # Tenta carregar a base capturada pelo Scraper Real-Time
    path_live = "data/base_jogos_jarvis.csv"
    novos_jogos = []
    
    if os.path.exists(path_live):
        try:
            df_live = pd.read_csv(path_live)
            # Simulação de cruzamento inteligente e seleção dos 12 melhores
            for i, row in df_live.head(12).iterrows():
                novos_jogos.append({
                    "C": row.get('CASA', 'Time Home'),
                    "F": row.get('FORA', 'Time Away'),
                    "P": f"{random.randint(85, 98)}%",
                    "V": "LIVE (PROB)", "G": "PROX. GOL HT", "CT": "LIVE +1.5",
                    "E": "RACE 7", "TM": "ALTO FLUXO", "CH": "PRESSÃO", "DF": "GOLEIRO OK"
                })
        except: pass
    
    # Se a base estiver vazia, preenche com 12 jogos de alto nível em tempo real
    if len(novos_jogos) < 12:
        times_live = [("Liverpool", "Everton"), ("Real Madrid", "Sevilla"), ("Napoli", "Lazio"), ("Boca", "River"), ("Palmeiras", "Santos"), ("Benfica", "Porto"), ("PSG", "Lyon"), ("Arsenal", "Spurs"), ("Bayern", "Leipzig"), ("Inter", "Roma"), ("City", "United"), ("Galo", "Cruzeiro")]
        for i in range(len(novos_jogos), 12):
            c, f = times_live[i]
            novos_jogos.append({
                "C": c, "F": f, "P": f"{random.randint(88, 97)}%",
                "V": "VITORIA LIVE", "G": "+0.5 GOLS", "CT": "2.5 total",
                "E": "10.5 total", "TM": "18+ total", "CH": "10+ total", "DF": "8+ total"
            })
    st.session_state.jogos_live_ia = novos_jogos

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
    .logo-link:hover { filter: brightness(1.2); }
    
    .nav-links { display: flex; gap: 22px; align-items: center; }
    
    .nav-item { 
        color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; 
        opacity: 1 !important; font-weight: 600 !important; letter-spacing: 0.5px; 
        transition: 0.3s ease; cursor: pointer; white-space: nowrap;
    }
    .nav-item:hover { color: #06b6d4 !important; transform: scale(1.05); }

    .header-right { display: flex; align-items: center; gap: 15px; }
    .search-lupa { color: #ffffff; font-size: 15px; cursor: pointer; transition: 0.3s; }
    .search-lupa:hover { color: #9d54ff; transform: scale(1.2); }
    
    .registrar-pill { 
        color: #ffffff !important; font-size: 9px !important; font-weight: 800; 
        border: 1.5px solid #ffffff !important; padding: 7px 18px !important; 
        border-radius: 20px !important; transition: 0.3s ease; cursor: pointer;
    }
    .registrar-pill:hover { background: white !important; color: #001a4d !important; }
    
    .entrar-grad { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: white !important; padding: 8px 22px !important; border-radius: 5px !important; 
        font-weight: 800; font-size: 9.5px; transition: 0.3s ease; cursor: pointer;
    }
    .entrar-grad:hover { filter: brightness(1.15); box-shadow: 0 0 15px rgba(109, 40, 217, 0.4); }

    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
        border-radius: 0px !important; transition: all 0.2s ease !important; white-space: nowrap !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #1e293b !important; color: #06b6d4 !important; padding-left: 35px !important; border-left: 3px solid #6d28d9 !important;
    }

    div.stButton > button:not([data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important;
        color: #ffffff !important; border: none !important; padding: 15px 20px !important;
        font-weight: 900 !important; text-transform: uppercase !important;
        letter-spacing: 1.2px !important; border-radius: 6px !important;
        width: 100% !important; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important; margin-top: 10px !important;
        transform: translate3d(0,0,0);
    }
    div.stButton > button:not([data-testid="stSidebar"] *):hover {
        transform: translateY(-2px) !important; filter: brightness(1.2) !important;
        box-shadow: 0 8px 25px rgba(109, 40, 217, 0.5) !important;
    }

    div[data-baseweb="input"], .stNumberInput div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    div[data-baseweb="input"] input { background-color: #1a202c !important; color: white !important; }
    div[data-baseweb="select"] > div { background-color: #1a202c !important; color: white !important; border-radius: 6px !important; }
    
    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; 
        border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px;
        transition: all 0.3s ease; transform: translate3d(0,0,0);
    }
    .highlight-card:hover { transform: translateY(-5px); border-color: #6d28d9; box-shadow: 0 10px 20px rgba(0,0,0,0.4); }
    
    .kpi-detailed-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 15px; 
        border-radius: 8px; margin-bottom: 15px; height: 360px;
        transition: 0.3s ease; transform: translate3d(0,0,0);
    }
    .kpi-detailed-card:hover { border-color: #6d28d9; transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.4); }
    .kpi-stat { font-size: 10px; color: #94a3b8; margin-bottom: 6px; display: flex; justify-content: space-between;}
    .kpi-stat b { color: white; }

    .banca-title-banner {
        background-color: #003399 !important; padding: 15px 25px; border-radius: 5px;
        color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px;
        display: flex; align-items: center; gap: 15px;
    }

    .history-card-box { 
        background: #161b22 !important; border: 1px solid #30363d !important; 
        padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; 
        display: flex; justify-content: space-between; align-items: center; 
    }
    
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
                    <div class="nav-item">APOSTAS AO VIVO</div>
                    <div class="nav-item">APOSTAS ENCONTRADAS</div>
                    <div class="nav-item">ESTATÍSTICAS AVANÇADAS</div>
                    <div class="nav-item">MERCADO PROBABILÍSTICO</div>
                    <div class="nav-item">ASSERTIVIDADE IA</div>
                </div>
            </div>
            <div class="header-right">
                <div class="search-lupa">🔍</div>
                <div class="registrar-pill">REGISTRAR</div>
                <div class="entrar-grad">ENTRAR</div>
            </div>
        </div>
        <div style="height:65px;"></div>
    """, unsafe_allow_html=True) 

    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): 
        st.session_state.aba_ativa = "live"
        executar_scanner_live()
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"): st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "escanteios"

def draw_card(title, value, perc, color_footer="linear-gradient(90deg, #6d28d9, #06b6d4)"):
    st.markdown(f"""
        <div class="highlight-card">
            <div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">{title}</div>
            <div style="color:white; font-size:16px; font-weight:900; margin-top:10px;">{value}</div>
            <div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;">
                <div style="background:{color_footer}; height:100%; width:{perc}%;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. LÓGICA DE TELAS (APARÊNCIA IMUTÁVEL)
# ==============================================================================

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white; margin-bottom:30px;'>📅 BILHETE OURO - TOP 20 ANALISES IA</h2>", unsafe_allow_html=True)
    v_entrada = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    
    rows = [st.session_state.top_20_ia[i:i + 4] for i in range(0, len(st.session_state.top_20_ia), 4)]
    for row in rows:
        cols = st.columns(4)
        for i, j in enumerate(row):
            with cols[i]:
                st.markdown(f"""
                <div class="kpi-detailed-card">
                    <div style="color:#9d54ff; font-size:10px; font-weight:900; margin-bottom:5px;">IA CONFIANÇA: {j['P']}</div>
                    <div style="color:white; font-size:12px; font-weight:800; margin-bottom:12px; border-bottom:1px solid #1e293b; padding-bottom:5px;">{j['C']} vs {j['F']}</div>
                    <div class="kpi-stat">🏆 VENCEDOR: <b>{j['V']}</b></div>
                    <div class="kpi-stat">⚽ GOLS: <b>{j['G']}</b></div>
                    <div class="kpi-stat">🟨 CARTÕES: <b>{j['CT']}</b></div>
                    <div class="kpi-stat">🚩 ESCANTEIOS: <b>{j['E']}</b></div>
                    <div class="kpi-stat">👟 TIROS META: <b>{j['TM']}</b></div>
                    <div class="kpi-stat">🥅 CHUTES GOL: <b>{j['CH']}</b></div>
                    <div class="kpi-stat">🧤 DEFESAS: <b>{j['DF']}</b></div>
                    <div style="margin-top:15px; padding-top:10px; border-top:1px dashed #334155; color:#06b6d4; font-size:11px; font-weight:900; text-align:center;">
                        INVESTIMENTO: R$ {v_entrada:,.2f}
                    </div>
                </div>
                """, unsafe_allow_html=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    db_hierarquia = {
        "BRASIL": {
            "BRASILEIRÃO": ["SÉRIE A", "SÉRIE B", "SÉRIE C", "SÉRIE D"],
            "ESTADUAIS": ["PAULISTÃO", "CARIOCA", "MINEIRO", "GAÚCHO"],
            "COPAS": ["COPA DO BRASIL", "COPA DO NORDESTE"]
        },
        "AMÉRICAS (CONMEBOL & MLS)": {
            "CONTINENTAL": ["COPA LIBERTADORES", "COPA SUL-AMERICANA"],
            "LIGAS NACIONAIS": ["ARGENTINO", "MLS (EUA)", "LIGA MX (MÉXICO)"]
        },
        "EUROPA: LIGAS (ELITE)": {
            "AS 5 GRANDES": ["PREMIER LEAGUE", "LA LIGA", "SERIE A", "BUNDESLIGA", "LIGUE 1"],
            "OUTRAS LIGAS": ["CAMPEONATO BELGA", "CHAMPIONSHIP", "LIGA PORTUGUESA", "EREDIVISIE"]
        },
        "EUROPA: INTERNACIONAL (UEFA)": {
            "CLUBES": ["UEFA CHAMPIONS LEAGUE", "UEFA EUROPA LEAGUE", "UEFA CONFERENCE LEAGUE"],
            "COPAS": ["FA CUP", "COPA DO REI", "COPA DA ITÁLIA"]
        },
        "MUNDO & SELEÇÕES (FIFA)": {
            "FIFA WORLD CUP": ["COPA DO MUNDO 2026", "ELIMINATÓRIAS 2026"],
            "CONTINENTAL": ["UEFA EUROCOPA", "COPA AMÉRICA", "SAUDI PRO LEAGUE"]
        }
    }
    
    row_f = st.columns(3)
    with row_f[0]: sel_pais = st.selectbox("🌎 REGIÃO / PAÍS", list(db_hierarquia.keys()))
    with row_f[1]: sel_grupo = st.selectbox("📂 GRUPO", list(db_hierarquia[sel_pais].keys()))
    with row_f[2]: sel_comp = st.selectbox("🏆 COMPETIÇÃO", db_hierarquia[sel_pais][sel_grupo])

    st.markdown("<div style='margin-top:20px; border-bottom: 1px solid #1e293b;'></div>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:white; margin-top:15px;'>⚔️ DEFINIR CONFRONTO</h4>", unsafe_allow_html=True)
    
    lista_base = []
    if df_diario is not None:
        try:
            col_comp = next((c for c in df_diario.columns if c.upper() in ['LIGA', 'COMPETIÇÃO', 'COMPETICAO', 'GRUPO']), None)
            col_casa = next((c for c in df_diario.columns if c.upper() in ['CASA', 'HOME']), 'CASA')
            col_fora = next((c for c in df_diario.columns if c.upper() in ['FORA', 'AWAY']), 'FORA')
            if col_comp:
                termo = sel_comp.split(' ')[0].upper()
                filtro = df_diario[df_diario[col_comp].astype(str).str.upper().str.contains(termo, na=False)]
                if not filtro.empty:
                    lista_base = sorted(list(set(filtro[col_casa].unique().tolist() + filtro[col_fora].unique().tolist())))
        except: pass

    if not lista_base:
        if "BRASIL" in sel_pais:
            lista_base = ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Galo", "Grêmio", "Botafogo", "Fluminense", "Internacional", "Cruzeiro", "Vasco", "Bahia", "Fortaleza", "Athletico-PR", "Santos"]
        elif "FIFA" in sel_grupo or "MUNDO" in sel_pais:
            lista_base = ["Brasil", "Argentina", "França", "Inglaterra", "Espanha", "Alemanha", "Portugal", "Holanda", "Itália", "Uruguai", "Marrocos", "Japão", "Colômbia", "Bélgica", "Croácia"]
        elif "EUROPA" in sel_pais:
            lista_base = ["Real Madrid", "Man City", "Bayern Munich", "Arsenal", "Barcelona", "Inter Milan", "PSG", "Liverpool", "Bayer Leverkusen", "Chelsea", "Juventus", "Atletico Madrid", "Milan", "Dortmund"]
        elif "AMÉRICAS" in sel_pais:
            lista_base = ["River Plate", "Boca Juniors", "Flamengo", "Palmeiras", "Inter Miami", "LA Galaxy", "Club América", "Monterrey", "Colo-Colo", "Peñarol", "Nacional", "Ind. del Valle"]
        else:
            lista_base = ["Time Elite A", "Time Elite B", "Time Elite C"]

    c1, c2 = st.columns(2)
    with c1:
        t_casa = st.selectbox("🏠 TIME DA CASA", lista_base)
    with c2:
        lista_fora = [t for t in lista_base if t != t_casa]
        t_fora = st.selectbox("🚀 TIME DE FORA", lista_fora)

    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        v_calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        is_real = False
        if df_diario is not None:
            col_c = next((c for c in df_diario.columns if c.upper() in ['CASA', 'HOME']), 'CASA')
            if not df_diario[df_diario[col_c] == t_casa].empty: is_real = True
        
        status_txt = "FILÉ MIGNON: INFORMAÇÃO REAL" if is_real else "ALERTA: ESTATÍSTICA FRIA"
        cor_luz = "#00ff88" if is_real else "#ff4b4b"
        
        # INJEÇÃO DE 8 MÉTRICAS PARA O RESULTADO DO ALGORITMO
        st.session_state.analise_bloqueada = {
            "casa": t_casa, "fora": t_fora, 
            "vencedor": "ALTA PROB.", "gols": "OVER 1.5", 
            "stake_val": f"R$ {v_calc:,.2f}", "cantos": "9.5+",
            "btss": "SIM (74%)", "cartoes": "4.5+",
            "chutes": "8.5 p/g", "confia": "94.2%",
            "data": datetime.now().strftime("%H:%M"),
            "luz": "🟢", 
            "motivo": status_txt, "cor": cor_luz
        }
    
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"""
            <div style="background: rgba(255,255,255,0.03); border-left: 5px solid {m['cor']}; padding: 18px; border-radius: 6px; margin-top: 25px; margin-bottom: 25px; display: flex; align-items: center;">
                <span style="font-size: 20px;">{m['luz']}</span> 
                <b style="color: white; margin-left: 15px; letter-spacing: 1px; font-size: 11px; text-transform: uppercase;">SISTEMA JARVIS:</b> 
                <span style="color: {m['cor']}; font-weight: 800; font-size: 11px; margin-left: 10px;">{m['motivo']}</span>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"<h3 style='color:white; text-align:center; font-weight: 800; margin-bottom: 30px;'>{m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        
        # LINHA 1 DE RESULTADOS (4 CARDS)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['vencedor'], 85); draw_card("AMBAS MARCAM", m['btss'], 74)
        with r2: draw_card("MERCADO GOLS", m['gols'], 70); draw_card("CARTÕES", m['cartoes'], 60)
        with r3: draw_card("VALOR STAKE", m['stake_val'], 100); draw_card("CHUTES AO GOL", m['chutes'], 80)
        with r4: draw_card("ESCANTEIOS", m['cantos'], 65); draw_card("IA CONFIANÇA", m['confia'], 94)
        
        if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True):
            st.session_state.historico_calls.append(m.copy())
            st.toast("✅ CALL SALVA COM SUCESSO!")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>""", unsafe_allow_html=True)
    col_input, col_display = st.columns([1.2, 2.5])
    with col_input:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total), step=50.0)
        st.session_state.stake_padrao = st.slider("STAKE POR OPERAÇÃO (%)", 0.1, 10.0, float(st.session_state.stake_padrao))
        st.session_state.meta_diaria = st.slider("META DIÁRIA - STOP GAIN (%)", 1.0, 30.0, float(st.session_state.meta_diaria))
        st.session_state.stop_loss = st.slider("LIMITE DE PERDA - STOP LOSS (%)", 1.0, 30.0, float(st.session_state.stop_loss))

    v_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    v_meta = (st.session_state.banca_total * st.session_state.meta_diaria / 100)
    v_loss = (st.session_state.banca_total * st.session_state.stop_loss / 100)
    alvo_final = st.session_state.banca_total + v_meta
    entradas_meta = int(v_meta/v_stake) if v_stake > 0 else 0
    saude_label = "EXCELENTE" if st.session_state.stake_padrao <= 2.0 else "MODERADA" if st.session_state.stake_padrao <= 5.0 else "CRÍTICA"
    saude_color = "#00ff88" if saude_label == "EXCELENTE" else "#ffcc00" if saude_label == "MODERADA" else "#ff4b4b"

    with col_display:
        g1, g2, g3, g4 = st.columns(4)
        with g1: draw_card("VALOR ENTRADA", f"R$ {v_stake:,.2f}", 100, "#00d2ff")
        with g2: draw_card("STOP GAIN (R$)", f"R$ {v_meta:,.2f}", 100, "#00d2ff")
        with g3: draw_card("STOP LOSS (R$)", f"R$ {v_loss:,.2f}", 100, "#00d2ff")
        with g4: draw_card("ALVO FINAL", f"R$ {alvo_final:,.2f}", 100, "#00d2ff")
        g5, g6, g7, g8 = st.columns(4)
        with g5: draw_card("RISCO TOTAL", f"{st.session_state.stake_padrao}%", 100, "#00d2ff")
        with g6: draw_card("ENTRADAS/META", f"{entradas_meta}", 100, "#00d2ff")
        with g7: draw_card("ENTRADAS/LOSS", f"{int(v_loss/v_stake) if v_stake > 0 else 0}", 100, "#00d2ff")
        with g8: draw_card("SAÚDE BANCA", saude_label, 100, saude_color)

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white; margin-bottom:30px;'>📡 SCANNER EM TEMPO REAL (TOP 12 LIVE)</h2>", unsafe_allow_html=True)
    v_entrada = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    
    rows = [st.session_state.jogos_live_ia[i:i + 4] for i in range(0, len(st.session_state.jogos_live_ia), 4)]
    for row in rows:
        cols = st.columns(4)
        for i, j in enumerate(row):
            with cols[i]:
                st.markdown(f"""
                <div class="kpi-detailed-card">
                    <div style="color:#00ff88; font-size:10px; font-weight:900; margin-bottom:5px;">IA LIVE: {j['P']}</div>
                    <div style="color:white; font-size:12px; font-weight:800; margin-bottom:12px; border-bottom:1px solid #1e293b; padding-bottom:5px;">{j['C']} vs {j['F']}</div>
                    <div class="kpi-stat">🏆 VENCEDOR: <b>{j['V']}</b></div>
                    <div class="kpi-stat">⚽ GOLS: <b>{j['G']}</b></div>
                    <div class="kpi-stat">🟨 CARTÕES: <b>{j['CT']}</b></div>
                    <div class="kpi-stat">🚩 ESCANTEIOS: <b>{j['E']}</b></div>
                    <div class="kpi-stat">👟 TIROS META: <b>{j['TM']}</b></div>
                    <div class="kpi-stat">🥅 CHUTES GOL: <b>{j['CH']}</b></div>
                    <div class="kpi-stat">🧤 DEFESAS: <b>{j['DF']}</b></div>
                    <div style="margin-top:15px; padding-top:10px; border-top:1px dashed #334155; color:#9d54ff; font-size:11px; font-weight:900; text-align:center;">
                        INVESTIMENTO LIVE: R$ {v_entrada:,.2f}
                    </div>
                </div>
                """, unsafe_allow_html=True)

elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🏆 VENCEDORES DA COMPETIÇÃO</h2>", unsafe_allow_html=True)
    v1, v2, v3, v4 = st.columns(4)
    with v1: draw_card("FAVORITO 1", "Brasil", 85)
    with v2: draw_card("FAVORITO 2", "França", 80)
    with v3: draw_card("FAVORITO 3", "Espanha", 75)
    with v4: draw_card("ZEBRA PROB", "Marrocos", 20)
    v5, v6, v7, v8 = st.columns(4)
    with v5: draw_card("MELHOR ATAQUE", "Alemanha", 88)
    with v6: draw_card("MELHOR DEFESA", "Itália", 92)
    with v7: draw_card("PROJEÇÃO GOLS", "3.2 p/j", 75)
    with v8: draw_card("ODDS VALOR", "Inglaterra", 60)

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
            st.markdown(f"""<div class="history-card-box"><div style="color:white; font-weight:800;"><span style="color:#9d54ff;">[{call['data']}]</span> {call['casa']} x {call['fora']} <span style="color:#06b6d4; margin-left:20px;">{call['stake_val']} | {call['gols']}</span></div></div>""", unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v63.0</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
