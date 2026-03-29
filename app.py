import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v60.00 - INTEGRIDADE TOTAL]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO) - UI v57.35
# DIRETRIZ 5: CÓDIGO 100% ÍNTEGRO - SEM ABREVIAÇÕES
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA BLINDADA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0
if 'top_20_ia' not in st.session_state: st.session_state.top_20_ia = []

# --- FUNÇÃO DE CARREGAMENTO DE DADOS ---
def carregar_jogos_diarios():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            return df
        except:
            return None
    return None

df_diario = carregar_jogos_diarios()

# ==============================================================================
# LÓGICA DO BOT (BACK-END): MOTOR DE PROCESSAMENTO INVISÍVEL
# ==============================================================================

def processar_ia_bot():
    if df_diario is not None:
        vips = []
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
                        "P": f"{jogo.get('CONF_NUM', 0)}%",
                        "G": jogo.get('GOLS', 'OVER 1.5'),
                        "CT": jogo.get('CARTOES', '3+'),
                        "E": jogo.get('CANTOS', '9.5 total'),
                        "TM": jogo.get('TMETA', '16+'),
                        "CH": jogo.get('CHUTES', '9+'),
                        "DF": jogo.get('DEFESAS', '7+')
                    })
                st.session_state.top_20_ia = vips
        except: pass

processar_ia_bot()

# ==============================================================================
# 2. CAMADA DE ESTILO CSS INTEGRAL (TRAVA DE SEGURANÇA v57.35)
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
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -45px !important; gap: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important;}
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; padding-left: 35px !important; border-left: 3px solid #6d28d9 !important;}
    div.stButton > button:not([data-testid="stSidebar"] *) { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: #ffffff !important; border: none !important; padding: 15px 20px !important; font-weight: 900 !important; text-transform: uppercase !important; letter-spacing: 1.2px !important; border-radius: 6px !important; width: 100% !important; box-shadow: 0 4px 15px rgba(109, 40, 217, 0.3) !important; margin-top: 10px !important;}
    div[data-baseweb="input"], .stNumberInput div { background-color: #1a202c !important; color: white !important; border: 1px solid #334155 !important; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; transform: translate3d(0,0,0); }
    .banca-title-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px; display: flex; align-items: center; gap: 15px; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }
    [data-testid="stDataFrame"] { border: 1px solid #1e293b !important; border-radius: 8px !important; background-color: #0b0e11 !important; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left"><div class="logo-link">GESTOR IA</div><div class="nav-links"><div class="nav-item">APOSTAS ESPORTIVAS</div><div class="nav-item">APOSTAS AO VIVO</div><div class="nav-item">ESTATÍSTICAS AVANÇADAS</div></div></div>
            <div class="header-right"><div class="registrar-pill">REGISTRAR</div><div class="entrar-grad">ENTRAR</div></div>
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
# 4. LÓGICA DE TELAS (RESTAURAÇÃO COMPLETA)
# ==============================================================================

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        h1, h2, h3, h4 = st.columns(4); draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
        st.markdown("<h4 style='color:#06b6d4; margin-top:30px;'>🤖 TOP 20 ANALISES IA - PROBABILIDADE REAL</h4>", unsafe_allow_html=True)
        for j in st.session_state.top_20_ia:
            with st.expander(f"➔ {j['C']} vs {j['F']} | CONF: {j['P']}"):
                c1, c2, c3 = st.columns(3)
                with c1: st.markdown(f"<p style='font-size:11px; color:#94a3b8;'>⚽ GOLS: <b style='color:white;'>{j['G']}</b></p>", unsafe_allow_html=True)
                with c2: st.markdown(f"<p style='font-size:11px; color:#94a3b8;'>🟨 CARTÕES: <b style='color:white;'>{j['CT']}</b></p>", unsafe_allow_html=True)
                with c3: st.markdown(f"<p style='font-size:11px; color:#94a3b8;'>🚩 ESCANTEIOS: <b style='color:white;'>{j['E']}</b></p>", unsafe_allow_html=True)
        st.dataframe(df_diario, use_container_width=True)

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        st.markdown("### Selecione a Região e Confronto")
        col_reg, col_grp, col_comp = st.columns(3)
        with col_reg: sel_pais = st.selectbox("🌎 REGIÃO / PAÍS", sorted(df_diario['PAIS'].unique().tolist()))
        df_filtrado = df_diario[df_diario['PAIS'] == sel_pais]
        with col_grp: sel_liga = st.selectbox("📂 GRUPO", sorted(df_filtrado['LIGA'].unique().tolist()))
        df_final_filtro = df_filtrado[df_filtrado['LIGA'] == sel_liga]
        with col_comp: t_casa = st.selectbox("🏠 TIME DA CASA", sorted(df_final_filtro['CASA'].unique().tolist()))
        
        jogo = df_final_filtro[df_final_filtro['CASA'] == t_casa].iloc[0]
        if st.button("⚡ EXECUTAR ALGORITMO"):
            st.session_state.analise_bloqueada = jogo
            
        if st.session_state.analise_bloqueada:
            j = st.session_state.analise_bloqueada
            st.markdown(f"<div style='background:rgba(0,255,136,0.1); border-left:5px solid #00ff88; padding:15px;'>🟢 SISTEMA JARVIS: FILÉ MIGNON: INFORMAÇÃO REAL</div>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center; color:#9d54ff;'>{j['CASA']} vs {j['FORA']}</h3>", unsafe_allow_html=True)
            r1, r2, r3, r4 = st.columns(4)
            with r1: draw_card("VENCEDOR", "ALTA PROB.", 85)
            with r2: draw_card("GOLS", str(j['GOLS']), 90)
            with r3: draw_card("STAKE", f"R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}", 100)
            with r4: draw_card("CANTOS", str(j['CANTOS']), 80)
            if st.button("📥 SALVAR NO HISTÓRICO"):
                st.session_state.historico_calls.append({"data": datetime.now().strftime("%H:%M"), "casa": j['CASA'], "fora": j['FORA'], "stake_val": f"R$ {10:,.2f}", "gols": j['GOLS']})
                st.toast("✅ CALL SALVA!")

elif st.session_state.aba_ativa == "live":
    st.markdown("<h2 style='color:white;'>📡 SCANNER EM TEMPO REAL</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        df_live = df_diario[df_diario['PAIS'].str.contains("LIVE", na=False)]
        if df_live.empty: st.info("Aguardando jogos ao vivo da Betano...")
        else: st.dataframe(df_live, use_container_width=True, hide_index=True)

elif st.session_state.aba_ativa == "vencedores":
    st.markdown("<h2 style='color:white;'>🏆 VENCEDORES DA COMPETIÇÃO</h2>", unsafe_allow_html=True)
    v1, v2, v3, v4 = st.columns(4)
    with v1: draw_card("FAVORITO 1", "Brasil", 45)
    with v2: draw_card("FAVORITO 2", "França", 38)
    with v3: draw_card("FAVORITO 3", "Espanha", 25)
    with v4: draw_card("ZEBRA PROB", "Marrocos", 12)

elif st.session_state.aba_ativa == "gols":
    st.markdown("<h2 style='color:white;'>⚽ APOSTAS POR GOLS</h2>", unsafe_allow_html=True)
    g1, g2, g3, g4 = st.columns(4)
    with g1: draw_card("OVER 0.5 HT", "82%", 82)
    with g2: draw_card("OVER 1.5 FT", "75%", 75)
    with g3: draw_card("AMBAS MARCAM", "61%", 61)
    with g4: draw_card("UNDER 3.5", "90%", 90)

elif st.session_state.aba_ativa == "escanteios":
    st.markdown("<h2 style='color:white;'>🚩 APOSTAS POR ESCANTEIOS</h2>", unsafe_allow_html=True)
    e1, e2, e3, e4 = st.columns(4)
    with e1: draw_card("OVER 8.5", "88%", 88)
    with e2: draw_card("OVER 10.5", "62%", 62)
    with e3: draw_card("CANTOS HT", "4.5+", 70)
    with e4: draw_card("CORNER RACE", "Time A", 55)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>""", unsafe_allow_html=True)
    col_input, col_display = st.columns([1.2, 2.5])
    with col_input:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total), step=50.0)
        st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, float(st.session_state.stake_padrao))
    with col_display:
        v_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        draw_card("VALOR ENTRADA", f"R$ {v_stake:,.2f}", 100, "#00d2ff")

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v60.0</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
