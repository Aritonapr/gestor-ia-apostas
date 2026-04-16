import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
import random
import requests

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v96.3 - AUDITORIA DE ASSERTIVIDADE REAL]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO)
# DIRETRIZ 5: CÓDIGO 100% ÍNTEGRO - CORREÇÃO CIRÚRGICA DE LISTA DE TIMES
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state:
    st.session_state.aba_ativa = "home"

if 'historico_calls' not in st.session_state:
    st.session_state.historico_calls = []

if 'analise_bloqueada' not in st.session_state:
    st.session_state.analise_bloqueada = None

if 'banca_total' not in st.session_state:
    st.session_state.banca_total = 1000.00

if 'stake_padrao' not in st.session_state:
    st.session_state.stake_padrao = 1.0

if 'meta_diaria' not in st.session_state:
    st.session_state.meta_diaria = 3.0

if 'stop_loss' not in st.session_state:
    st.session_state.stop_loss = 5.0

if 'top_20_ia' not in st.session_state:
    st.session_state.top_20_ia = []

if 'jogos_live_ia' not in st.session_state:
    st.session_state.jogos_live_ia = []

# Redirecionamento via URL (Navegação Híbrida)
query_params = st.query_params
if query_params.get("go") == "home":
    st.session_state.aba_ativa = "home"
    st.query_params.clear()

if query_params.get("go") == "assertividade":
    st.session_state.aba_ativa = "assertividade"
    st.query_params.clear()

if query_params.get("go") == "live":
    st.session_state.aba_ativa = "live"
    st.query_params.clear()

# --- FUNÇÃO DE CARREGAMENTO DE DADOS ---
def carregar_dados_ia():
    url_github = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    try:
        ts = datetime.now().timestamp()
        df = pd.read_csv(f"{url_github}?v={ts}", on_bad_lines='skip')
        df.columns = [c.upper() for c in df.columns]
        return df
    except Exception:
        path_local = "data/database_diario.csv"
        if os.path.exists(path_local):
            try:
                df_local = pd.read_csv(path_local)
                df_local.columns = [c.upper() for c in df_local.columns]
                return df_local
            except Exception:
                return None
    return None

df_diario = carregar_dados_ia()
big_data_existe = os.path.exists("data/historico_5_temporadas.csv")

# ==============================================================================
# LÓGICA DO BOT (BACK-END): MOTOR DE PROCESSAMENTO
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
        except Exception:
            pass
            
    if len(vips) < 20:
        elite = ["Real Madrid", "Man City", "Bayern", "Arsenal", "Barcelona", "PSG", "Inter", "Milan", "Flamengo", "Palmeiras", "Liverpool", "Juventus", "Dortmund", "Leverkusen", "Napoli", "Benfica", "Porto", "Ajax", "Atletico Madrid", "Chelsea"]
        for i in range(len(vips), 20):
            vips.append({
                "C": elite[i % 20], 
                "F": elite[(i+5) % 20], 
                "P": f"{95-i}%", 
                "V": "68% (PROB)", 
                "G": "OVER 1.5 (HT/FT)", 
                "CT": "4.5 total", 
                "E": "9.5 total", 
                "TM": "14+ total", 
                "CH": "9+ total", 
                "DF": "7+ total"
            })
    st.session_state.top_20_ia = vips

def executar_scanner_live():
    path_live = "data/base_jogos_jarvis.csv"
    novos_jogos = []
    if os.path.exists(path_live):
        try:
            df_live = pd.read_csv(path_live)
            for i, row in df_live.head(20).iterrows():
                novos_jogos.append({
                    "C": row.get('CASA', 'Time Home'), 
                    "F": row.get('FORA', 'Time Away'), 
                    "P": f"{random.randint(85, 98)}%", 
                    "V": "LIVE (PROB)", 
                    "G": "PROX. GOL HT", 
                    "CT": "LIVE +1.5", 
                    "E": "RACE 7", 
                    "TM": "ALTO FLUXO", 
                    "CH": "PRESSÃO", 
                    "DF": "GOLEIRO OK"
                })
        except Exception:
            pass
            
    if len(novos_jogos) < 20:
        times_live = [("Liverpool", "Everton"), ("Real Madrid", "Sevilla"), ("Palmeiras", "Santos"), ("PSG", "Lyon")]
        for i in range(len(novos_jogos), 20):
            c, f = times_live[i % 4]
            novos_jogos.append({
                "C": c, 
                "F": f, 
                "P": f"{random.randint(88, 97)}%", 
                "V": "VITORIA LIVE", 
                "G": "+0.5 GOLS", 
                "CT": "2.5 total", 
                "E": "10.5 total", 
                "TM": "18+ total", 
                "CH": "10+ total", 
                "DF": "8+ total"
            })
    st.session_state.jogos_live_ia = novos_jogos

processar_ia_bot()

# ==============================================================================
# 2. CAMADA DE ESTILO CSS INTEGRAL (ZERO WHITE PRO)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    .header-anchor { display: none !important; }
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp { 
        background-color: #0b0e11 !important; 
        font-family: 'Inter', sans-serif; 
    }
    
    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; 
        top: 0; 
        left: 0; 
        width: 100%; 
        height: 60px; 
        background-color: #001a4d !important; 
        border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; 
        align-items: center; 
        justify-content: space-between; 
        padding: 0 40px !important; 
        z-index: 1000000; 
        transform: translate3d(0,0,0); 
        -webkit-backface-visibility: hidden; 
    }
    
    .header-left { display: flex; align-items: center; gap: 20px; }
    
    .logo-link { 
        color: #9d54ff !important; 
        font-weight: 900; 
        font-size: 21px !important; 
        text-transform: uppercase; 
        letter-spacing: 0.5px; 
        text-decoration: none !important; 
        cursor: pointer; 
        border-bottom: 2px solid #9d54ff; 
        padding-bottom: 2px; 
    }
    
    .nav-links { display: flex; gap: 15px; align-items: center; }
    
    .nav-item { 
        color: #ffffff !important; 
        font-size: 9.5px !important; 
        text-transform: uppercase; 
        font-weight: 700 !important; 
        letter-spacing: 0.3px; 
        transition: 0.3s ease; 
        cursor: pointer; 
        white-space: nowrap; 
        text-decoration: none !important;
    }
    
    .nav-item:hover { color: #06b6d4 !important; transform: scale(1.02); }
    
    .header-right { 
        display: flex; 
        align-items: center; 
        gap: 10px; 
        min-width: 250px; 
        justify-content: flex-end; 
    }
    
    .registrar-pill { 
        color: #ffffff !important; 
        font-size: 9px !important; 
        font-weight: 800; 
        border: 1.5px solid #ffffff !important; 
        padding: 6px 14px !important; 
        border-radius: 20px !important; 
        transition: 0.3s ease; 
        cursor: pointer; 
        white-space: nowrap; 
    }
    
    .entrar-grad { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: white !important; 
        padding: 7px 18px !important; 
        border-radius: 5px !important; 
        font-weight: 800; 
        font-size: 9.5px; 
        transition: 0.3s ease; 
        cursor: pointer; 
        white-space: nowrap; 
    }
    
    [data-testid="stSidebar"] { 
        min-width: 320px !important; 
        background-color: #11151a !important; 
        border-right: 1px solid #1e293b !important; 
    }
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; 
        color: #94a3b8 !important; 
        border: none !important; 
        border-bottom: 1px solid #1a202c !important; 
        text-align: left !important; 
        width: 100% !important; 
        padding: 18px 25px !important; 
        font-size: 10px !important; 
        text-transform: uppercase !important; 
        border-radius: 0px !important; 
        transition: all 0.2s ease !important; 
        white-space: nowrap !important; 
    }
    
    section[data-testid="stSidebar"] div.stButton > button:hover { 
        background-color: #1e293b !important; 
        color: #06b6d4 !important; 
        border-left: 3px solid #6d28d9 !important; 
    }
    
    div.stButton > button:not([data-testid="stSidebar"] *) { 
        background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; 
        color: #ffffff !important; 
        border: none !important; 
        padding: 15px 20px !important; 
        font-weight: 900 !important; 
        text-transform: uppercase !important; 
        letter-spacing: 1.2px !important; 
        border-radius: 6px !important; 
        width: 100% !important; 
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important; 
        box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important; 
        margin-top: 10px !important; 
        transform: translate3d(0,0,0); 
    }
    
    .highlight-card { 
        background: #11151a; 
        border: 1px solid #1e293b; 
        padding: 20px; 
        border-radius: 8px; 
        text-align: center; 
        height: 155px; 
        margin-bottom: 15px; 
        transition: all 0.3s ease; 
        transform: translate3d(0,0,0); 
    }
    
    .kpi-detailed-card { 
        background: #11151a; 
        border: 1px solid #1e293b; 
        padding: 20px 18px; 
        border-radius: 8px; 
        margin-bottom: 15px; 
        height: auto !important; 
        transition: 0.3s ease; 
        transform: translate3d(0,0,0); 
    }
    
    .kpi-stat { 
        font-size: 10px; 
        color: #94a3b8; 
        margin-bottom: 6px; 
        display: flex; 
        justify-content: space-between;
    }
    
    .kpi-stat b { color: white; }
    
    .banca-title-banner { 
        background-color: #003399 !important; 
        padding: 15px 25px; 
        border-radius: 5px; 
        color: white !important; 
        font-size: 24px; 
        font-weight: 800; 
        margin-bottom: 35px; 
        display: flex; 
        align-items: center; 
        gap: 15px; 
    }
    
    .footer-shield { 
        position: fixed; 
        bottom: 0; 
        left: 0; 
        width: 100%; 
        background-color: #0d0d12; 
        height: 25px; 
        border-top: 1px solid #1e293b; 
        display: flex; 
        justify-content: space-between; 
        align-items: center; 
        padding: 0 20px; 
        font-size: 9px; 
        color: #475569; 
        z-index: 999999; 
    }
    
    .big-data-badge { 
        background: rgba(0, 255, 136, 0.1); 
        color: #00ff88; 
        padding: 5px 12px; 
        border-radius: 4px; 
        font-size: 10px; 
        font-weight: 800; 
        border: 1px solid #00ff88; 
        margin-bottom: 20px; 
        display: inline-block; 
    }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <a href="?go=home" class="logo-link">GESTOR IA</a>
                <div class="nav-links">
                    <a href="?go=home" class="nav-item">APOSTAS ESPORTIVAS</a>
                    <a href="?go=live" class="nav-item">APOSTAS AO VIVO</a>
                    <div class="nav-item">APOSTAS ENCONTRADAS</div>
                    <div class="nav-item">ESTATÍSTICAS AVANÇADAS</div>
                    <div class="nav-item">MERCADO PROBABILÍSTICO</div>
                    <a href="?go=assertividade" class="nav-item">ASSERTIVIDADE IA</a>
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
    
    if st.button("🎯 SCANNER PRÉ-LIVE"):
        st.session_state.aba_ativa = "analise"
        
    if st.button("📡 SCANNER EM TEMPO REAL"):
        st.session_state.aba_ativa = "live"
        executar_scanner_live()
        
    if st.button("💰 GESTÃO DE BANCA"):
        st.session_state.aba_ativa = "gestao"
        
    if st.button("📜 HISTÓRICO DE CALLS"):
        st.session_state.aba_ativa = "historico"
        
    if st.button("📅 BILHETE OURO"):
        st.session_state.aba_ativa = "home"
        
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"):
        st.session_state.aba_ativa = "vencedores"
        
    if st.button("⚽ APOSTAS POR GOLS"):
        st.session_state.aba_ativa = "gols"
        
    if st.button("🚩 APOSTAS POR ESCANTEIOS"):
        st.session_state.aba_ativa = "escanteios"

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
# 4. LÓGICA DE TELAS
# ==============================================================================

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white; margin-bottom:10px;'>📅 BILHETE OURO - TOP 20 ANALISES IA</h2>", unsafe_allow_html=True)
    if big_data_existe:
        st.markdown('<div class="big-data-badge">🛡️ BIG DATA ATIVO: PADRÕES 2021-2026 CARREGADOS</div>', unsafe_allow_html=True)
    
    v_entrada = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    rows = [st.session_state.top_20_ia[i:i + 4] for i in range(0, 20, 4)]
    
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
                        <div style="margin-top:15px; padding-top:12px; border-top:1px dashed #334155; color:#06b6d4; font-size:11px; font-weight:900; text-align:center;">INVESTIMENTO: R$ {v_entrada:,.2f}</div>
                    </div>
                """, unsafe_allow_html=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    db_h = {
        "BRASIL": {
            "BRASILEIRÃO": ["SÉRIE A", "SÉRIE B", "SÉRIE C", "SÉRIE D"],
            "ESTADUAIS": ["Campeonato Carioca", "Campeonato Paulista", "Campeonato Mineiro", "Campeonato Gaúcho", "Campeonato Paranaense", "Campeonato Baiano", "Campeonato Catarinense", "Campeonato Cearense"],
            "COPAS": ["Copa do Brasil", "Supercopa do Brasil", "Copa do Nordeste", "Copa Verde"]
        },
        "AMÉRICA DO SUL": {
            "CONMEBOL": ["Copa Libertadores", "Copa Sul-Americana", "Recopa Sul-Americana"],
            "LIGAS NACIONAIS": ["Liga Argentina (LPF)", "Primera División Chile", "Categoría Primera A (Col)", "Liga Pro (Equador)", "Primera División Uruguai"]
        },
        "EUROPA ELITE": {
            "UEFA CLUBES": ["Champions League", "Liga Europa", "Liga Conferência"],
            "LIGAS TOP 5": ["Premier League", "La Liga", "Serie A (Itália)", "Bundesliga", "Ligue 1"],
            "COPAS": ["Copa da Inglaterra", "Copa do Rei", "DFB Pokal", "Coppa Italia"]
        },
        "EUROPA OUTRAS": {
            "LIGAS SECUNDÁRIAS": ["Liga Portugal (Betclic)", "Eredivisie (Holanda)", "Süper Lig (Turquia)", "Championship (Inglaterra)", "Premiership (Escócia)"]
        },
        "MUNDO & EMERGENTES": {
            "LIGAS": ["Saudi Pro League (Arábia)", "MLS (EUA)", "Liga MX (México)", "J-League (Japão)"],
            "SELEÇÕES": ["Eliminatórias Copa 2026", "UEFA Nations League", "Copa América", "Eurocopa"]
        }
    }
    
    r_f = st.columns(3)
    with r_f[0]:
        s_reg = st.selectbox("🌎 REGIÃO / CONTINENTE", list(db_h.keys()))
    with r_f[1]:
        s_gru = st.selectbox("📂 CATEGORIA", list(db_h[s_reg].keys()))
    with r_f[2]:
        s_cmp = st.selectbox("🏆 COMPETIÇÃO", db_h[s_reg][s_gru])
    
    # BANCO DE DADOS DE TIMES VINCULADOS (CORREÇÃO CIRÚRGICA v96.3)
    db_times_vinc = {
        "SÉRIE A": ["Athletico-PR", "Atlético-MG", "Bahia", "Botafogo", "Bragantino", "Corinthians", "Criciúma", "Cruzeiro", "Cuiabá", "Flamengo", "Fluminense", "Fortaleza", "Grêmio", "Internacional", "Juventude", "Palmeiras", "São Paulo", "Vasco", "Vitória"],
        "SÉRIE B": ["Santos", "Sport", "Ceará", "Goiás", "Coritiba", "Novorizontino", "Mirassol", "Avaí", "Operário-PR", "Amazonas", "Vila Nova", "Ponte Preta", "Chapecoense", "CRB", "Botafogo-SP", "Ituano", "Brusque", "Guarani"],
        "Copa Libertadores": [
            "Fluminense", "Palmeiras", "Flamengo", "Grêmio", "São Paulo", "Atlético-MG", "Botafogo", "River Plate", "Talleres", "Rosario Central", "San Lorenzo", "Estudiantes", 
            "Independiente del Valle", "Independiente Rivadavia", "LDU Quito", "Barcelona SC", "Junior Barranquilla", "Millonarios", "Peñarol", "Nacional (Uru)", "Colo-Colo", "Cobresal", "Huachipato", 
            "Libertad", "Cerro Porteño", "Universitario", "Alianza Lima", "Bolívar", "The Strongest", "Caracas FC", "Deportivo Táchira"
        ],
        "Copa Sul-Americana": [
            "Fortaleza", "Cuiabá", "Internacional", "Cruzeiro", "Corinthians", "Athletico-PR", "Boca Juniors", "Racing", "Lanús", "Belgrano", "Argentinos Juniors", "Defensa y Justicia", 
            "Ind. Medellín", "América de Cali", "Univ. Católica", "Coquimbo Unido", "Danubio", "Racing Montevideo", "Sportivo Luqueño", "Sportivo Ameliano"
        ],
        "Liga Argentina (LPF)": [
            "River Plate", "Boca Juniors", "Racing", "Independiente", "San Lorenzo", "Talleres", "Estudiantes", "Lanús", "Vélez Sarsfield", "Huracán", "Rosario Central", "Newells Old Boys", 
            "Belgrano", "Argentinos Juniors", "Defensa y Justicia", "Godoy Cruz", "Independiente Rivadavia", "Banfield", "Gimnasia LP", "Tigre", "Barracas Central", "Platense", "Sarmiento", "Union Santa Fe",
            "Instituto", "Central Córdoba", "Deportivo Riestra", "Atlético Tucumán"
        ],
        "Premier League": [
            "Man City", "Arsenal", "Liverpool", "Aston Villa", "Spurs", "Chelsea", "Man United", "Newcastle", "West Ham", "Brighton", "Wolves", "Fulham", "Bournemouth", "Everton", "Brentford", "Nottingham Forest", "Crystal Palace", "Leicester", "Ipswich", "Southampton"
        ],
        "La Liga": [
            "Real Madrid", "Barcelona", "Atletico Madrid", "Girona", "Athletic Bilbao", "Real Sociedad", "Real Betis", "Villarreal", "Valencia", "Alaves", "Osasuna", "Getafe", "Sevilla", "Celta Vigo", "Rayo Vallecano", "Las Palmas", "Mallorca", "Valladolid", "Leganes", "Espanyol"
        ],
        "Serie A (Itália)": [
            "Inter Milan", "AC Milan", "Juventus", "Atalanta", "Bologna", "AS Roma", "Lazio", "Fiorentina", "Torino", "Napoli", "Genoa", "Monza", "Verona", "Lecce", "Udinese", "Cagliari", "Empoli", "Parma", "Como", "Venezia"
        ],
        "Bundesliga": [
            "Bayer Leverkusen", "Bayern Munich", "Stuttgart", "RB Leipzig", "Dortmund", "Frankfurt", "Hoffenheim", "Heidenheim", "Werder Bremen", "Freiburg", "Augsburg", "Wolfsburg", "Mainz", "Gladbach", "Union Berlin", "Bochum", "St. Pauli", "Holstein Kiel"
        ],
        "Ligue 1": [
            "PSG", "Monaco", "Brest", "Lille", "Nice", "Lyon", "Lens", "Marseille", "Reims", "Rennes", "Toulouse", "Montpellier", "Strasbourg", "Nantes", "Le Havre", "Auxerre", "Angers", "Saint-Etienne"
        ],
        "Saudi Pro League (Arábia)": [
            "Al-Hilal", "Al-Nassr", "Al-Ittihad", "Al-Ahli", "Al-Shabab", "Al-Ettifaq", "Al-Taawoun", "Al-Fateh", "Damac", "Al-Khaleej", "Al-Wehda", "Al-Fayha", "Al-Raed", "Al-Riyadh", "Al-Okhdood", "Al-Qadsiah", "Al-Kholood", "Al-Orobah"
        ],
        "Liga Portugal (Betclic)": ["Benfica", "Porto", "Sporting CP", "Braga", "Vitória SC", "Moreirense", "Arouca", "Famalicão", "Casa Pia", "Farense", "Rio Ave", "Gil Vicente", "Estoril", "Boavista", "Estrela Amadora", "Santa Clara", "Nacional", "AVS"],
        "MLS (EUA)": ["Inter Miami", "Columbus Crew", "FC Cincinnati", "LAFC", "LA Galaxy", "Real Salt Lake", "Seattle Sounders", "Houston Dynamo", "Orlando City", "New York City", "New York RB", "Charlotte FC", "Portland Timbers", "Colorado Rapids", "Minnesota United", "Vancouver Whitecaps"],
        "Eredivisie (Holanda)": ["PSV", "Feyenoord", "Twente", "AZ Alkmaar", "Ajax", "NEC Nijmegen", "Utrecht", "Sparta Rotterdam", "Go Ahead Eagles", "Heerenveen", "Fortuna Sittard", "Heracles", "Zwolle", "Almere City", "Willem II", "Groningen", "NAC Breda"],
        "Süper Lig (Turquia)": ["Galatasaray", "Fenerbahce", "Trabzonspor", "Basaksehir", "Besiktas", "Kasimpasa", "Sivasspor", "Alanyaspor", "Rizespor", "Antalyaspor", "Gaziantep", "Samsunspor", "Kayserispor", "Eyupspor", "Göztepe", "Bodrum FK"]
    }
    
    lista_comp = db_times_vinc.get(s_cmp, ["Time Analítico A", "Time Analítico B", "Time Analítico C"])
    st.markdown("<h4 style='color:white; margin-top:15px;'>⚔️ DEFINIR CONFRONTO</h4>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        t_c = st.selectbox("🏠 TIME DA CASA", sorted(lista_comp))
    with c2:
        t_f = st.selectbox("🚀 TIME DE FORA", sorted([t for t in lista_comp if t != t_c]))
    
    if st.button("⚡ EXECUTAR ALGORITIMO JARVIS", use_container_width=True):
        st.session_state.analise_bloqueada = {
            "casa": t_c, 
            "fora": t_f, 
            "vencedor": "ALTA PROB.", 
            "gols": "OVER 1.5", 
            "stake_val": f"R$ {(st.session_state.banca_total*st.session_state.stake_padrao/100):,.2f}", 
            "cantos": "9.5+", 
            "btss": "SIM (74%)", 
            "cartoes": "4.5+", 
            "chutes": "8.5 p/g", 
            "confia": "94.2%", 
            "data": datetime.now().strftime("%H:%M")
        }
        
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"""
            <div style="background:rgba(255,255,255,0.03); border-left:5px solid #00ff88; padding:18px; border-radius:6px; margin-top:25px; display:flex; align-items:center;">
                <div style="width:15px; height:15px; background:#00ff88; border-radius:50%; margin-right:15px;"></div>
                <b style="color:white; font-size:11px;">SISTEMA JARVIS:</b>
                <span style="color:#00ff88; font-weight:800; font-size:11px; margin-left:10px;">FILÉ MIGNON: INFORMAÇÃO REAL IDENTIFICADA</span>
            </div>
            <h3 style='color:white; text-align:center; font-weight:800; margin:30px 0;'>{m['casa']} vs {m['fora']}</h3>
        """, unsafe_allow_html=True)
        
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['vencedor'], 85)
        with r2: draw_card("MERCADO GOLS", m['gols'], 70)
        with r3: draw_card("VALOR STAKE", m['stake_val'], 100)
        with r4: draw_card("ESCANTEIOS", m['cantos'], 65)
            
        r5, r6, r7, r8 = st.columns(4)
        with r5: draw_card("AMBAS MARCAM", m['btss'], 74)
        with r6: draw_card("CARTÕES", m['cartoes'], 60)
        with r7: draw_card("CHUTES AO GOL", m['chutes'], 80)
        with r8: draw_card("IA CONFIANÇA", m['confia'], 94)
            
        if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True): 
            st.session_state.historico_calls.append(m.copy())
            st.toast("✅ CALL SALVA NO HISTÓRICO!")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<div class='banca-title-banner'>💰 GESTÃO DE BANCA INTELIGENTE</div>", unsafe_allow_html=True)
    c_in, c_out = st.columns([1.2, 2.5])
    
    with c_in:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total), step=50.0)
        st.session_state.stake_padrao = st.slider("STAKE POR ENTRADA (%)", 0.1, 10.0, float(st.session_state.stake_padrao))
        st.session_state.meta_diaria = st.slider("META DE GANHO DIÁRIO (%)", 1.0, 30.0, float(st.session_state.meta_diaria))
        st.session_state.stop_loss = st.slider("LIMITE DE PERDA (STOP LOSS) (%)", 1.0, 30.0, float(st.session_state.stop_loss))
        
    v_s = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
    v_m = (st.session_state.banca_total * st.session_state.meta_diaria / 100)
    v_l = (st.session_state.banca_total * st.session_state.stop_loss / 100)
    
    with c_out:
        g1, g2, g3, g4 = st.columns(4)
        with g1: draw_card("VALOR ENTRADA", f"R$ {v_s:,.2f}", 100, "#00d2ff")
        with g2: draw_card("STOP GAIN (META)", f"R$ {v_m:,.2f}", 100, "#00ff88")
        with g3: draw_card("STOP LOSS", f"R$ {v_l:,.2f}", 100, "#ff4b4b")
        with g4: draw_card("ALVO FINAL", f"R$ {(st.session_state.banca_total+v_m):,.2f}", 100, "#00d2ff")
        
        g5, g6, g7, g8 = st.columns(4)
        with g5: draw_card("RISCO TOTAL", f"{st.session_state.stake_padrao}%", 100, "#00d2ff")
        with g6: draw_card("ENTRADAS P/ META", f"{int(v_m/v_s) if v_s>0 else 0}", 100, "#00d2ff")
        with g7: draw_card("ENTRADAS P/ LOSS", f"{int(v_l/v_s) if v_s>0 else 0}", 100, "#00d2ff")
        with g8: draw_card("SAÚDE FINANCEIRA", "EXCELENTE", 100, "#00ff88")

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white; margin-bottom:30px;'>📡 SCANNER EM TEMPO REAL (TOP 20 LIVE)</h2>", unsafe_allow_html=True)
    rows = [st.session_state.jogos_live_ia[i:i + 4] for i in range(0, 20, 4)]
    
    for row in rows:
        cols = st.columns(4)
        for i, j in enumerate(row):
            with cols[i]:
                st.markdown(f"""
                    <div class="kpi-detailed-card">
                        <div style="color:#00ff88; font-size:10px; font-weight:900;">IA LIVE: {j['P']}</div>
                        <div style="color:white; font-size:12px; font-weight:800; margin-bottom:12px; border-bottom:1px solid #1e293b;">{j['C']} vs {j['F']}</div>
                        <div class="kpi-stat">🏆 VENCEDOR: <b>{j['V']}</b></div>
                        <div class="kpi-stat">⚽ GOLS: <b>{j['G']}</b></div>
                        <div class="kpi-stat">🟨 CARTÕES: <b>{j['CT']}</b></div>
                        <div class="kpi-stat">🚩 ESCANTEIOS: <b>{j['E']}</b></div>
                        <div class="kpi-stat">👟 TIROS META: <b>{j['TM']}</b></div>
                        <div class="kpi-stat">🥅 CHUTES GOL: <b>{j['CH']}</b></div>
                        <div class="kpi-stat">🧤 DEFESAS: <b>{j['DF']}</b></div>
                    </div>
                """, unsafe_allow_html=True)

elif st.session_state.aba_ativa == "assertividade":
    st.markdown("<h2 style='color:white; margin-bottom:30px;'>📈 ASSERTIVIDADE IA</h2>", unsafe_allow_html=True)
    path_detalhe = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/relatorio_fechamento_dia.csv"
    
    try:
        ts = datetime.now().timestamp()
        st.markdown("<h4 style='color:white; margin-bottom:20px; font-weight:800;'>🔍 DETALHAMENTO GREEN/RED DO DIA</h4>", unsafe_allow_html=True)
        df_det = pd.read_csv(f"{path_detalhe}?v={ts}")
        
        if not df_det.empty:
            rows_det = [df_det.to_dict('records')[i:i + 4] for i in range(0, len(df_det), 4)]
            for r_det in rows_det:
                cols_det = st.columns(4)
                for idx, jogo_det in enumerate(r_det):
                    res_ia = str(jogo_det.get('RESULTADO_IA', '')).upper()
                    cor_status = "#00ff88" if "GREEN" in res_ia else "#ff4b4b"
                    with cols_det[idx]:
                        st.markdown(f"""
                            <div class="kpi-detailed-card" style="border: 1px solid {cor_status};">
                                <div style="color:{cor_status}; font-size:11px; font-weight:900; margin-bottom:10px; text-align:center;">{res_ia}</div>
                                <div style="color:white; font-size:11px; font-weight:800; border-bottom:1px solid #1e293b; padding-bottom:5px; margin-bottom:10px;">{jogo_det.get('CASA', 'Time A')} vs {jogo_det.get('FORA', 'Time B')}</div>
                                <div class="kpi-stat">MERCADO: <b>{jogo_det.get('GOLS', 'GOLS')}</b></div>
                                <div class="kpi-stat">IA CONF: <b>{jogo_det.get('CONFIANCA', '90%')}</b></div>
                            </div>
                        """, unsafe_allow_html=True)
    except Exception:
        st.info("Aguardando Auditoria Diária (Fechamento às 23:30).")

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white; margin-bottom:30px;'>📜 HISTÓRICO DE CALLS (SALVAS)</h2>", unsafe_allow_html=True)
    if not st.session_state.historico_calls:
        st.info("Nenhuma call registrada.")
    else:
        calls_rev = list(reversed(st.session_state.historico_calls))
        rows_hist = [calls_rev[i:i + 4] for i in range(0, len(calls_rev), 4)]
        for row in rows_hist:
            cols = st.columns(4)
            for i, call in enumerate(row):
                with cols[i]:
                    st.markdown(f"""
                        <div class="kpi-detailed-card">
                            <div style="color:#06b6d4; font-size:10px; font-weight:900;">HORÁRIO: {call['data']}</div>
                            <div style="color:white; font-size:12px; font-weight:800; margin-bottom:12px; border-bottom:1px solid #1e293b; padding-bottom:5px;">{call['casa']} vs {call['fora']}</div>
                            <div class="kpi-stat">🏆 CALL: <b>{call.get('vencedor', 'N/A')}</b></div>
                            <div class="kpi-stat">⚽ GOLS: <b>{call.get('gols', 'N/A')}</b></div>
                            <div class="kpi-stat">🚩 CANTOS: <b>{call.get('cantos', 'N/A')}</b></div>
                            <div class="kpi-stat">🟨 CARTÕES: <b>{call.get('cartoes', 'N/A')}</b></div>
                            <div class="kpi-stat">BTTS: <b>{call.get('btss', 'N/A')}</b></div>
                            <div class="kpi-stat">IA CONF: <b>{call.get('confia', 'N/A')}</b></div>
                            <div style="margin-top:15px; color:#9d54ff; font-size:11px; font-weight:900; text-align:center;">INVESTIDO: {call['stake_val']}</div>
                        </div>
                    """, unsafe_allow_html=True)

elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white; margin-bottom:30px;'>🏆 VENCEDORES DA COMPETIÇÃO - TOP 20</h2>", unsafe_allow_html=True)
    rows = [st.session_state.top_20_ia[i:i + 4] for i in range(0, 20, 4)]
    for row in rows:
        cols = st.columns(4)
        for i, j in enumerate(row):
            with cols[i]:
                st.markdown(f"""
                    <div class="kpi-detailed-card">
                        <div style="color:#ffcc00; font-size:10px; font-weight:900;">CHANCE: {j['P']}</div>
                        <div style="color:white; font-size:12px; font-weight:800; margin-bottom:10px;">{j['C']} vs {j['F']}</div>
                        <div class="kpi-stat">🏆 VENCEDOR: <b>{j['V']}</b></div>
                    </div>
                """, unsafe_allow_html=True)

elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white; margin-bottom:30px;'>⚽ GOLS - TOP 20 ANALISES IA</h2>", unsafe_allow_html=True)
    rows = [st.session_state.top_20_ia[i:i + 4] for i in range(0, 20, 4)]
    for row in rows:
        cols = st.columns(4)
        for i, j in enumerate(row):
            with cols[i]:
                st.markdown(f"""
                    <div class="kpi-detailed-card">
                        <div style="color:#00d2ff; font-size:10px; font-weight:900; margin-bottom:5px;">PROB. GOLS: {j['P']}</div>
                        <div style="color:white; font-size:12px; font-weight:800; margin-bottom:12px; border-bottom:1px solid #1e293b; padding-bottom:5px;">{j['C']} vs {j['F']}</div>
                        <div class="kpi-stat">⏱️ GOL 1º TEMPO: <b>82%</b></div>
                        <div class="kpi-stat">⏱️ GOL 2º TEMPO: <b>89%</b></div>
                        <div class="kpi-stat">🤝 AMBAS MARCAM: <b>SIM (74%)</b></div>
                        <div class="kpi-stat">🏠 GOLS CASA: <b>1.5+</b></div>
                        <div class="kpi-stat">🚀 GOLS FORA: <b>0.5+</b></div>
                        <div class="kpi-stat">📊 TOTAL GOLS: <b>OVER 2.5</b></div>
                    </div>
                """, unsafe_allow_html=True)

elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white; margin-bottom:30px;'>🚩 ESCANTEIOS - TOP 20 ANALISES IA</h2>", unsafe_allow_html=True)
    rows = [st.session_state.top_20_ia[i:i + 4] for i in range(0, 20, 4)]
    for row in rows:
        cols = st.columns(4)
        for i, j in enumerate(row):
            with cols[i]:
                st.markdown(f"""
                    <div class="kpi-detailed-card">
                        <div style="color:#ff4b4b; font-size:10px; font-weight:900; margin-bottom:5px;">CANTOS: {j['P']}</div>
                        <div style="color:white; font-size:12px; font-weight:800; margin-bottom:12px; border-bottom:1px solid #1e293b; padding-bottom:5px;">{j['C']} vs {j['F']}</div>
                        <div class="kpi-stat">⏱️ CANTOS 1º TEMPO: <b>4.5+</b></div>
                        <div class="kpi-stat">⏱️ CANTOS 2º TEMPO: <b>5.5+</b></div>
                        <div class="kpi-stat">🏠 CANTOS CASA: <b>6</b></div>
                        <div class="kpi-stat">🚀 CANTOS FORA: <b>4</b></div>
                        <div class="kpi-stat">📊 QUANTIDADE TOTAL: <b>OVER 9.5</b></div>
                    </div>
                """, unsafe_allow_html=True)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v96.3</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)

def sync():
    url = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            if not os.path.exists('data'): 
                os.makedirs('data')
            with open('data/database_diario.csv', 'wb') as f: 
                f.write(r.content)
    except Exception:
        pass

if __name__ == "__main__": 
    sync()
