import streamlit as st
import time
from datetime import datetime
import random

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v57.23 - PROTEÇÃO ATIVA]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO)
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# BANCO DE DADOS HIERÁRQUICO EXPANDIDO (PESQUISA REAL DE TIMES E LIGAS)
DADOS_MUNDIAIS = {
    "🏆 COPA DO MUNDO 2026": {
        "Internacional": {
            "Principais Seleções": ["Brasil", "Argentina", "França", "Alemanha", "Espanha", "Inglaterra", "Portugal", "Holanda", "Itália", "Uruguai", "Bélgica", "Croácia"],
            "Eliminatórias": ["Colômbia", "Equador", "Chile", "Paraguai", "Japão", "Coreia do Sul", "Marrocos", "Senegal", "México", "Estados Unidos", "Canadá"]
        }
    },
    "🇧🇷 BRASIL (LIGAS & COPAS)": {
        "Nacional": {
            "Brasileirão Série A": ["Flamengo", "Palmeiras", "Botafogo", "Atlético-MG", "São Paulo", "Cruzeiro", "Fortaleza", "Internacional", "Fluminense", "Grêmio", "Vasco", "Corinthians", "Bahia", "Athletico-PR", "Vitória", "Cuiabá", "Criciúma", "Juventude", "Bragantino", "Atlético-GO"],
            "Brasileirão Série B": ["Santos", "Sport", "Coritiba", "Goiás", "Ceará", "Vila Nova", "América-MG", "Novorizontino", "Mirassol", "Operário", "Amazonas", "Avaí", "Chapecoense", "Ponte Preta"],
            "Copa do Brasil": ["Todos os Clubes da Série A", "Todos os Clubes da Série B", "Campeões Estaduais"]
        },
        "Estaduais": {
            "Paulistão": ["Corinthians", "Palmeiras", "Santos", "São Paulo", "Bragantino", "Ituano", "Novorizontino", "Água Santa"],
            "Cariocão": ["Flamengo", "Fluminense", "Botafogo", "Vasco", "Nova Iguaçu", "Portuguesa-RJ", "Boavista"],
            "Gauchão": ["Grêmio", "Internacional", "Juventude", "Caxias", "Brasil de Pelotas"]
        }
    },
    "🌍 AMÉRICA DO SUL (CONMEBOL)": {
        "Continentais": {
            "Libertadores": ["River Plate", "Boca Juniors", "Peñarol", "Nacional", "Colo-Colo", "LDU", "Ind. del Valle", "Olimpia", "Libertad", "Cerro Porteño", "Bolívar"],
            "Copa Sul-Americana": ["Racing", "Lanús", "Defensa y Justicia", "Ind. Medellín", "Coquimbo Unido", "Belgrano"]
        },
        "Ligas Nacionais": {
            "Campeonato Argentino": ["Boca Juniors", "River Plate", "Racing", "Independiente", "San Lorenzo", "Talleres", "Estudiantes"],
            "Campeonato Chileno": ["Colo-Colo", "Univ. Católica", "Univ. de Chile", "Palestino"]
        }
    },
    "🇪🇺 EUROPA (PRINCIPAIS LIGAS)": {
        "UEFA (Continentais)": {
            "Champions League": ["Real Madrid", "Man. City", "Bayern de Munique", "PSG", "Inter de Milão", "Dortmund", "Barcelona", "Arsenal", "Atlético Madrid", "Leverkusen", "Benfica", "Milan"],
            "Europa League": ["Roma", "Man. United", "Tottenham", "Ajax", "Porto", "Lazio", "Real Sociedad", "Sevilla"]
        },
        "Ligas Nacionais": {
            "Premier League (Inglaterra)": ["Man. City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Man. United", "Newcastle", "West Ham", "Brighton"],
            "La Liga (Espanha)": ["Real Madrid", "Barcelona", "Girona", "Atlético de Madrid", "Athletic Bilbao", "Real Sociedad", "Villarreal", "Valencia"],
            "Bundesliga (Alemanha)": ["Bayer Leverkusen", "Bayern de Munique", "Stuttgart", "RB Leipzig", "Dortmund", "Eintracht Frankfurt"],
            "Serie A (Itália)": ["Inter de Milão", "Milan", "Juventus", "Atalanta", "Napoli", "Roma", "Lazio", "Fiorentina"],
            "Ligue 1 (França)": ["PSG", "Monaco", "Marseille", "Lille", "Nice", "Lyon"]
        }
    },
    "🇸🇦 ORIENTE MÉDIO & ÁSIA": {
        "Ligas": {
            "Saudi Pro League": ["Al-Hilal", "Al-Nassr", "Al-Ittihad", "Al-Ahli", "Al-Ettifaq", "Al-Shabab"],
            "AFC Champions League": ["Al-Ain", "Yokohama F. Marinos", "Ulsan Hyundai", "Shandong Taishan"]
        }
    },
    "🇺🇸 AMÉRICA DO NORTE (MLS)": {
        "Ligas": {
            "MLS Pro": ["Inter Miami", "LA Galaxy", "Columbus Crew", "LAFC", "Seattle Sounders", "FC Cincinnati", "NY Red Bulls"]
        }
    }
}

# 2. [CAMADA DE PROTEÇÃO 1] - CSS INTEGRAL E BLINDADO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; padding: 0 40px !important; z-index: 1000000; transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
    }
    .header-left { display: flex; align-items: center; gap: 25px; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; letter-spacing: 0.5px; text-decoration: none !important; cursor: pointer; transition: 0.3s; }
    .logo-link:hover { filter: brightness(1.3); transform: scale(1.02); }
    .nav-links { display: flex; gap: 18px; align-items: center; }
    .nav-item { color: #ffffff !important; font-size: 8.5px !important; text-transform: uppercase; opacity: 0.85; font-weight: 700; letter-spacing: 0.8px; transition: 0.3s ease; cursor: pointer; white-space: nowrap; }
    .nav-item:hover { opacity: 1 !important; color: #06b6d4 !important; transform: scale(1.05); }
    .header-right { display: flex; align-items: center; gap: 15px; }
    .search-lupa { color: #ffffff; font-size: 15px; cursor: pointer; transition: 0.3s; }
    .search-lupa:hover { color: #9d54ff; transform: scale(1.2); }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; transition: 0.3s ease; cursor: pointer; }
    .registrar-pill:hover { background: white !important; color: #001a4d !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; transition: 0.3s ease; cursor: pointer; }
    .entrar-grad:hover { filter: brightness(1.15); box-shadow: 0 0 15px rgba(109, 40, 217, 0.4); }

    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important; transition: all 0.2s ease !important; white-space: nowrap !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; padding-left: 35px !important; border-left: 3px solid #6d28d9 !important; }

    div.stButton > button:not([data-testid="stSidebar"] *) { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: #ffffff !important; border: none !important; padding: 15px 20px !important; font-weight: 900 !important; text-transform: uppercase !important; letter-spacing: 1.2px !important; border-radius: 6px !important; width: 100% !important; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important; box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important; margin-top: 10px !important; }
    div.stButton > button:not([data-testid="stSidebar"] *):hover { transform: translateY(-2px) !important; filter: brightness(1.2) !important; }

    div[data-baseweb="input"], .stNumberInput div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    div[data-baseweb="input"] input { background-color: #1a202c !important; color: white !important; }
    div[data-baseweb="select"] > div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; transition: all 0.3s ease; }
    .highlight-card:hover { transform: translateY(-5px); border-color: #6d28d9; box-shadow: 0 10px 20px rgba(0,0,0,0.4); }
    
    .banca-title-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px; display: flex; align-items: center; gap: 15px; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    
    label[data-testid="stWidgetLabel"] p { color: #64748b !important; font-size: 10px !important; text-transform: uppercase !important; font-weight: 700 !important; letter-spacing: 0.5px !important; }
    </style>
""", unsafe_allow_html=True)

# 3. [DIRETRIZ 1] HEADER ANCORADO NA SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <div class="logo-link" onclick="window.parent.location.reload()">GESTOR IA</div>
                <div class="nav-links">
                    <div class="nav-item">APOSTAS ESPORTIVAS</div>
                    <div class="nav-item">APOSTAS AO VIVO</div>
                    <div class="nav-item">OPORTUNIDADES IA</div>
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

    if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
    if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
    if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
    if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
    if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
    if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
    if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 JOGOS DO DIA"): st.session_state.aba_ativa = "home"
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

# --- LÓGICA DE TELAS ---

# TELA 1: HOME
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
    with h2: draw_card("ASSERTIVIDADE", "92.4%", 92)
    with h3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with h4: draw_card("IA STATUS", "ONLINE", 100)
    h5, h6, h7, h8 = st.columns(4)
    with h5: draw_card("VOL. GLOBAL", "ALTO", 75)
    with h6: draw_card("STAKE PADRÃO", f"{st.session_state.stake_padrao}%", 100)
    with h7: draw_card("VALOR ENTRADA", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
    with h8: draw_card("SISTEMA", "JARVIS v57.23", 100)

# TELA 2: GESTÃO DE BANCA
elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>""", unsafe_allow_html=True)
    col_input, col_display = st.columns([1.2, 2.5])
    with col_input:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total, step=50.0)
        st.session_state.stake_padrao = st.slider("STAKE POR OPERAÇÃO (%)", 0.1, 10.0, st.session_state.stake_padrao)
        st.session_state.meta_diaria = st.slider("META DIÁRIA - STOP GAIN (%)", 1.0, 30.0, st.session_state.meta_diaria)
        st.session_state.stop_loss = st.slider("LIMITE DE PERDA - STOP LOSS (%)", 1.0, 30.0, st.session_state.stop_loss)
    v_stake, v_meta, v_loss = (st.session_state.banca_total * st.session_state.stake_padrao / 100), (st.session_state.banca_total * st.session_state.meta_diaria / 100), (st.session_state.banca_total * st.session_state.stop_loss / 100)
    alvo_final = st.session_state.banca_total + v_meta
    with col_display:
        g1, g2, g3, g4 = st.columns(4); with g1: draw_card("VALOR ENTRADA", f"R$ {v_stake:,.2f}", 100, "#00d2ff"); with g2: draw_card("STOP GAIN (R$)", f"R$ {v_meta:,.2f}", 100, "#00d2ff"); with g3: draw_card("STOP LOSS (R$)", f"R$ {v_loss:,.2f}", 100, "#00d2ff"); with g4: draw_card("ALVO FINAL", f"R$ {alvo_final:,.2f}", 100, "#00d2ff")
        g5, g6, g7, g8 = st.columns(4); with g5: draw_card("RISCO TOTAL", f"{st.session_state.stake_padrao}%", 100, "#00d2ff"); with g6: draw_card("ENTRADAS/META", f"{int(v_meta/v_stake) if v_stake > 0 else 0}", 100, "#00d2ff"); with g7: draw_card("ENTRADAS/LOSS", f"{int(v_loss/v_stake) if v_stake > 0 else 0}", 100, "#00d2ff"); with g8: st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase; font-weight: 700;">SAÚDE BANCA</div><div style="color:#00ff88; font-size:16px; font-weight:900; margin-top:10px;">EXCELENTE</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:#00d2ff; height:100%; width:100%;"></div></div></div>""", unsafe_allow_html=True)

# TELA 3: SCANNER PRÉ-LIVE (ARMONIA E DADOS COMPLETOS)
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: cat_sel = st.selectbox("🌎 CATEGORIA", list(DADOS_MUNDIAIS.keys()))
    with c2: tipo_sel = st.selectbox("📂 TIPO", list(DADOS_MUNDIAIS[cat_sel].keys()))
    with c3: camp_sel = st.selectbox("🏆 CAMPEONATO", list(DADOS_MUNDIAIS[cat_sel][tipo_sel].keys()))
    
    times_atuais = DADOS_MUNDIAIS[cat_sel][tipo_sel][camp_sel]
    if "Todos os Clubes" in times_atuais[0]: times_atuais = DADOS_MUNDIAIS["🇧🇷 BRASIL (LIGAS & COPAS)"]["Nacional"]["Brasileirão Série A"]
    
    cm1, cm2 = st.columns(2)
    with cm1: mandante = st.selectbox("🏠 MANDANTE", times_atuais, index=0)
    with cm2: visitante = st.selectbox("🚀 VISITANTE", times_atuais, index=min(1, len(times_atuais)-1))
    
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        v_calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        st.session_state.analise_bloqueada = {"casa": mandante, "fora": visitante, "vencedor": random.choice(["Casa", "Fora", "Empate"]), "gols": random.choice(["OVER 1.5", "OVER 2.5", "AMBAS MARCAM"]), "data": datetime.now().strftime("%H:%M"), "stake_val": f"R$ {v_calc:,.2f}"}
    
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<h3 style='color:#9d54ff; text-align:center;'>RESULTADO: {m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4); with r1: draw_card("VENCEDOR", m['vencedor'], 85); with r2: draw_card("GOLS", m['gols'], 70); with r3: draw_card("STAKE", m['stake_val'], 100); with r4: draw_card("CANTOS", "9.5+", 65)
        r5, r6, r7, r8 = st.columns(4); with r5: draw_card("IA CONF.", "94%", 94); with r6: draw_card("PRESSÃO", "ALTA", 88); with r7: draw_card("TENDÊNCIA", "SUBINDO", 60); with r8: draw_card("SISTEMA", "v57.23", 100)
        if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True): st.session_state.historico_calls.append(m.copy()); st.toast("✅ CALL SALVA COM SUCESSO!")

# TELA 4: LIVE
elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER LIVE</h2>", unsafe_allow_html=True)
    l1, l2, l3, l4 = st.columns(4); with l1: draw_card("PRESSÃO CASA", "88%", 88); with l2: draw_card("ATAQUES", "14/5m", 70); with l3: draw_card("POSSE", "65%", 65); with l4: draw_card("GOL PROB", "90%", 90)
    l5, l6, l7, l8 = st.columns(4); with l5: draw_card("ODDS ATUAIS", "1.85", 100); with l6: draw_card("VARIAÇÃO", "+0.12", 40); with l7: draw_card("CORNERS LIVE", "8", 80); with l8: draw_card("STAKE LIVE", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)

# TELA 5: VENCEDORES DA COMPETIÇÃO (RESTAURADA)
elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🏆 VENCEDORES DA COMPETIÇÃO</h2>", unsafe_allow_html=True)
    v1, v2, v3, v4 = st.columns(4); with v1: draw_card("FAVORITO 1", "Real Madrid", 45); with v2: draw_card("FAVORITO 2", "Man. City", 38); with v3: draw_card("FAVORITO 3", "Flamengo", 25); with v4: draw_card("ZEBRA PROB", "Bayer Leverkusen", 12)
    v5, v6, v7, v8 = st.columns(4); with v5: draw_card("ROI MÉDIO", "12.4%", 100); with v6: draw_card("VOLATILIDADE", "BAIXA", 20); with v7: draw_card("TENDÊNCIA", "ESTÁVEL", 50); with v8: draw_card("LIQUIDEZ", "ALTA", 90)

# TELA 6: APOSTAS POR GOLS (RESTAURADA)
elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ APOSTAS POR GOLS</h2>", unsafe_allow_html=True)
    g1, g2, g3, g4 = st.columns(4); with g1: draw_card("OVER 0.5 HT", "82%", 82); with g2: draw_card("OVER 1.5 FT", "75%", 75); with g3: draw_card("AMBAS MARCAM", "61%", 61); with g4: draw_card("UNDER 3.5", "90%", 90)
    g5, g6, g7, g8 = st.columns(4); with g5: draw_card("UNDER 1.5 HT", "65%", 65); with g6: draw_card("OVER 2.5 FT", "54%", 54); with g7: draw_card("BTTS NO", "39%", 39); with g8: draw_card("OVER 1.5 HT", "22%", 22)

# TELA 7: APOSTAS POR ESCANTEIOS (RESTAURADA)
elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 APOSTAS POR ESCANTEIOS</h2>", unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4); with e1: draw_card("OVER 8.5", "88%", 88); with e2: draw_card("OVER 10.5", "62%", 62); with e3: draw_card("CANTOS HT", "4.5+", 70); with e4: draw_card("CORNER RACE", "Time A", 55)
    e5, e6, e7, e8 = st.columns(4); with e5: draw_card("RACE TO 5", "72%", 72); with e6: draw_card("OVER 12.5", "18%", 18); with e7: draw_card("UNDER 7.5", "12%", 12); with e8: draw_card("CANTOS ASIÁT.", "9.0", 100)

# TELA 8: HISTÓRICO
elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    if not st.session_state.historico_calls: st.info("Nenhuma operação registrada.")
    else:
        for i, call in enumerate(reversed(st.session_state.historico_calls)):
            idx = len(st.session_state.historico_calls) - 1 - i
            ci, cd = st.columns([0.92, 0.08]); with ci: st.markdown(f"""<div class="history-card-box"><div style="color:white; font-weight:800;"><span style="color:#9d54ff;">[{call['data']}]</span> {call['casa']} x {call['fora']} <span style="color:#06b6d4; margin-left:20px;">{call['stake_val']} | {call['gols']}</span></div></div>""", unsafe_allow_html=True)
            with cd: 
                if st.button("🗑️", key=f"del_{idx}"): st.session_state.historico_calls.pop(idx); st.rerun()

# FOOTER
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v57.23</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
