import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v58.7 - INTEGRADO COM IA AUTÔNOMA]
# DIRETRIZ 1: HEADER NA SIDEBAR (TRAVA DE CICLO)
# DIRETRIZ 2: MANTER TRANSLATE3D E BACKFACE-VISIBILITY (TRAVA DE GPU)
# DIRETRIZ 3: NAVEGAÇÃO APENAS POR SESSION_STATE (ESTABILIDADE)
# DIRETRIZ 4: ESTILIZAÇÃO PRIORITÁRIA (ZERO WHITE REFORÇADO)
# DIRETRIZ 5: BOT INVISÍVEL - PROCESSAMENTO VIA CSV REAL
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

# Redirecionamento Home via URL
if st.query_params.get("go") == "home":
    st.session_state.aba_ativa = "home"
    st.query_params.clear()

# --- FUNÇÃO DE CARREGAMENTO DE DADOS ---
def carregar_jogos_diarios():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try:
            return pd.read_csv(path)
        except:
            return None
    return None

df_diario = carregar_jogos_diarios()

# --- MOTOR DE INTELIGÊNCIA JARVIS (BOT INVISÍVEL) ---
def motor_ia_jarvis(df, casa, fora):
    try:
        # Busca exata no CSV (Colunas: CASA, FORA, CONF, GOLS, CANTOS)
        match = df[(df['CASA'] == casa) & (df['FORA'] == fora)].iloc[0]
        v_conf = str(match.get('CONF', '0%'))
        v_gols = str(match.get('GOLS', 'ANALISAR'))
        v_cantos = f"{match.get('CANTOS', '0')}+"
        conf_num = float(v_conf.replace('%', ''))

        if conf_num >= 55:
            cor, luz, msg = "#00ff88", "🟢", "SISTEMA JARVIS: PADRÃO DE ALTA ASSERTIVIDADE"
        elif conf_num >= 45:
            cor, luz, msg = "#ffcc00", "🟡", "SISTEMA JARVIS: ENTRADA DE RISCO MODERADO"
        else:
            cor, luz, msg = "#ff4b4b", "🔴", "SISTEMA JARVIS: DADOS INSUFICIENTES / RISCO ALTO"

        return {
            "luz": luz, "motivo": msg, "cor": cor, "confia": v_conf,
            "vencedor": "ALTA PROB." if conf_num >= 55 else "REVISAR LIVE",
            "gols": v_gols, "cantos": v_cantos, "pressao": "ALTA" if conf_num >= 50 else "MÉDIA"
        }
    except:
        return {
            "luz": "🔴", "motivo": "SISTEMA JARVIS: CONFRONTO NÃO MONITORADO", "cor": "#ff4b4b",
            "vencedor": "---", "gols": "---", "confia": "0%", "cantos": "---", "pressao": "BAIXA"
        }

# 2. CAMADA DE ESTILO CSS INTEGRAL (MANTIDA 100%)
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
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600 !important; cursor: pointer; white-space: nowrap; }
    .header-right { display: flex; align-items: center; gap: 15px; }
    .search-lupa { color: #ffffff; font-size: 15px; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }
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
        border-radius: 6px !important; width: 100% !important; margin-top: 10px !important;
    }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; }
    .banca-title-banner { background-color: #003399 !important; padding: 15px 25px; border-radius: 5px; color: white !important; font-size: 24px; font-weight: 800; margin-bottom: 35px; }
    .history-card-box { background: #161b22 !important; border: 1px solid #30363d !important; padding: 15px 25px !important; border-radius: 8px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER SIDEBAR
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div class="header-left">
                <div class="logo-link">GESTOR IA</div>
                <div class="nav-links">
                    <div class="nav-item">APOSTAS ESPORTIVAS</div>
                    <div class="nav-item">APOSTAS AO VIVO</div>
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
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📜 HISTÓRICO DE CALLS"): st.session_state.aba_ativa = "historico"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
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

if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        h1, h2, h3, h4 = st.columns(4)
        with h1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
        with h2: draw_card("ASSERTIVIDADE", "92.4%", 92)
        with h3: draw_card("SUGESTÃO", "OVER 2.5", 88)
        with h4: draw_card("IA STATUS", "ONLINE", 100)
        st.dataframe(df_diario, use_container_width=True)
    else:
        st.warning("Sincronize os dados no Bot 3...")

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    # Filtros Dinâmicos baseados no seu CSV
    if df_diario is not None:
        lista_paises = sorted(df_diario['PAIS'].unique().tolist())
        sel_pais = st.selectbox("🌎 REGIÃO / PAÍS", lista_paises)
        
        df_filtrado = df_diario[df_diario['PAIS'] == sel_pais]
        lista_ligas = sorted(df_filtrado['LIGA'].unique().tolist())
        sel_liga = st.selectbox("📂 LIGA", lista_ligas)
        
        df_confronto = df_filtrado[df_filtrado['LIGA'] == sel_liga]
        
        c1, c2 = st.columns(2)
        with c1: t_casa = st.selectbox("🏠 TIME DA CASA", sorted(df_confronto['CASA'].unique().tolist()))
        with c2: t_fora = st.selectbox("🚀 TIME DE FORA", sorted(df_confronto[df_confronto['CASA']==t_casa]['FORA'].unique().tolist()))
    else:
        st.error("ERRO: Base de dados não encontrada.")

    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        v_calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        res = motor_ia_jarvis(df_diario, t_casa, t_fora)
        
        st.session_state.analise_bloqueada = {
            "casa": t_casa, "fora": t_fora, "vencedor": res['vencedor'], "gols": res['gols'], 
            "data": datetime.now().strftime("%H:%M"), "stake_val": f"R$ {v_calc:,.2f}",
            "luz": res['luz'], "motivo": res['motivo'], "cor": res['cor'], 
            "confia": res['confia'], "cantos": res['cantos'], "pressao": res['pressao']
        }
    
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"""<div style="background: rgba(255,255,255,0.03); border-left: 5px solid {m['cor']}; padding: 18px; border-radius: 6px; margin-bottom: 25px;">
            <span style="font-size: 20px;">{m['luz']}</span> <b style="color: white; margin-left: 10px; font-size: 11px;">{m['motivo']}</b></div>""", unsafe_allow_html=True)

        st.markdown(f"<h3 style='color:#9d54ff; text-align:center;'>{m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['vencedor'], 85)
        with r2: draw_card("GOLS", m['gols'], 70)
        with r3: draw_card("STAKE", m['stake_val'], 100)
        with r4: draw_card("CANTOS", m['cantos'], 65)
        r5, r6, r7, r8 = st.columns(4)
        with r5: draw_card("IA CONF.", m['confia'], 94)
        with r6: draw_card("PRESSÃO", m['pressao'], 88)
        with r7: draw_card("TENDÊNCIA", "ESTÁVEL", 60)
        with r8: draw_card("SISTEMA", "v58.7", 100)
        
        if st.button("📥 SALVAR CALL NO HISTÓRICO"):
            st.session_state.historico_calls.append(m.copy())
            st.toast("✅ CALL SALVA!")

elif st.session_state.aba_ativa == "gestao":
    st.markdown("""<div class="banca-title-banner">💰 GESTÃO DE BANCA</div>""", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=st.session_state.banca_total)
    st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, st.session_state.stake_padrao)
    st.write(f"Valor por entrada: R$ {(st.session_state.banca_total * st.session_state.stake_padrao / 100):,.2f}")

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO</h2>", unsafe_allow_html=True)
    for call in reversed(st.session_state.historico_calls):
        st.markdown(f"""<div class="history-card-box"><div>{call['casa']} x {call['fora']} | {call['gols']} | {call['stake_val']}</div></div>""", unsafe_allow_html=True)

# RODAPÉ FIXO
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v58.7</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
