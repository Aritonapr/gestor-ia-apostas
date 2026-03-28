import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v58.7 - JARVIS PROTECT]
# REGRAS: APARÊNCIA IMUTÁVEL | ESTRUTURA FIXA | BOT INVISÍVEL
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA (SESSION STATE) ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'historico_calls' not in st.session_state: st.session_state.historico_calls = []
if 'analise_bloqueada' not in st.session_state: st.session_state.analise_bloqueada = None
if 'banca_total' not in st.session_state: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = 1.0
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

# --- CARREGAMENTO DE DADOS ---
def carregar_jogos_diarios():
    path = "data/database_diario.csv"
    if os.path.exists(path):
        try:
            return pd.read_csv(path)
        except:
            return None
    return None

df_diario = carregar_jogos_diarios()

# --- MOTOR DE INTELIGÊNCIA JARVIS (O CÉREBRO INVISÍVEL) ---
def motor_ia_jarvis(df, casa, fora):
    try:
        # Busca inteligente (ignora espaços e letras maiúsculas)
        df_busca = df.copy()
        df_busca['C_ID'] = df_busca['CASA'].astype(str).str.upper().str.strip()
        df_busca['F_ID'] = df_busca['FORA'].astype(str).str.upper().str.strip()
        
        c_alvo = str(casa).upper().strip()
        f_alvo = str(fora).upper().strip()

        # Localiza o jogo
        match = df_busca[(df_busca['C_ID'] == c_alvo) & (df_busca['F_ID'] == f_alvo)].iloc[0]
        
        v_conf = str(match.get('CONF', '0%'))
        v_gols = str(match.get('GOLS', 'ANALISAR'))
        v_cantos = f"{match.get('CANTOS', '0')}+"
        conf_num = float(v_conf.replace('%', '')) if '%' in v_conf else float(v_conf)

        if conf_num >= 55:
            cor, luz, msg = "#00ff88", "🟢", "SISTEMA JARVIS: PADRÃO DE ALTA ASSERTIVIDADE"
        elif conf_num >= 45:
            cor, luz, msg = "#ffcc00", "🟡", "SISTEMA JARVIS: ENTRADA DE RISCO MODERADO"
        else:
            cor, luz, msg = "#ff4b4b", "🔴", "SISTEMA JARVIS: RISCO ALTO / EVITAR"

        return {
            "luz": luz, "motivo": msg, "cor": cor, "confia": v_conf if '%' in v_conf else f"{v_conf}%",
            "vencedor": "ALTA PROB." if conf_num >= 55 else "ANALISAR LIVE",
            "gols": v_gols, "cantos": v_cantos, "pressao": "ALTA" if conf_num >= 50 else "MÉDIA"
        }
    except:
        return {
            "luz": "🔴", "motivo": "SISTEMA JARVIS: JOGO NÃO MONITORADO NO MOMENTO", "cor": "#ff4b4b",
            "vencedor": "---", "gols": "---", "confia": "0%", "cantos": "---", "pressao": "BAIXA"
        }

# 2. CAMADA DE ESTILO CSS (IMUTÁVEL)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp { background-color: #0b0e11 !important; font-family: 'Inter', sans-serif; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    .betano-header { position: fixed; top: 0; left: 0; width: 100%; height: 60px; background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; display: flex; align-items: center; justify-content: space-between; padding: 0 40px !important; z-index: 1000000; }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; }
    .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; font-weight: 600 !important; margin: 0 10px; }
    .registrar-pill { color: #ffffff !important; font-size: 9px !important; font-weight: 800; border: 1.5px solid #ffffff !important; padding: 7px 18px !important; border-radius: 20px !important; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 22px !important; border-radius: 5px !important; font-weight: 800; font-size: 9.5px; }
    [data-testid="stSidebar"] { min-width: 320px !important; max-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { background-color: transparent !important; color: #94a3b8 !important; border: none !important; border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; padding: 18px 25px !important; font-size: 10px !important; text-transform: uppercase !important; border-radius: 0px !important; }
    section[data-testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; color: #06b6d4 !important; border-left: 3px solid #6d28d9 !important; }
    div.stButton > button:not([data-testid="stSidebar"] *) { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: #ffffff !important; border: none !important; padding: 15px 20px !important; font-weight: 900 !important; text-transform: uppercase !important; border-radius: 6px !important; width: 100% !important; margin-top: 10px !important; }
    .highlight-card { background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 155px; margin-bottom: 15px; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR (NAVEGAÇÃO)
with st.sidebar:
    st.markdown("""
        <div class="betano-header">
            <div style="display:flex; align-items:center; gap:20px;">
                <div class="logo-link">GESTOR IA</div>
                <div style="display:flex;">
                    <div class="nav-item">APOSTAS ESPORTIVAS</div>
                    <div class="nav-item">APOSTAS AO VIVO</div>
                </div>
            </div>
            <div style="display:flex; align-items:center; gap:15px;">
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

# 4. LÓGICA DE TELAS
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO</h2>", unsafe_allow_html=True)
    if df_diario is not None:
        c1, c2, c3, c4 = st.columns(4)
        with c1: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.2f}", 100)
        with c2: draw_card("ASSERTIVIDADE IA", "92.4%", 92)
        with c3: draw_card("SUGESTÃO DO DIA", "OVER 1.5", 88)
        with c4: draw_card("STATUS", "ONLINE", 100)
        st.dataframe(df_diario, use_container_width=True)
    else:
        st.warning("⚠️ Sincronize os dados no Bot 3...")

elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    if df_diario is not None:
        paises = sorted(df_diario['PAIS'].unique().tolist())
        sel_pais = st.selectbox("🌎 REGIÃO / PAÍS", paises)
        
        ligas = sorted(df_diario[df_diario['PAIS'] == sel_pais]['LIGA'].unique().tolist())
        sel_liga = st.selectbox("📂 LIGA", ligas)
        
        df_confronto = df_diario[(df_diario['PAIS'] == sel_pais) & (df_diario['LIGA'] == sel_liga)]
        
        col1, col2 = st.columns(2)
        with col1: t_casa = st.selectbox("🏠 TIME DA CASA", sorted(df_confronto['CASA'].unique().tolist()))
        with col2: t_fora = st.selectbox("🚀 TIME DE FORA", sorted(df_confronto[df_confronto['CASA']==t_casa]['FORA'].unique().tolist()))
        
        if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
            res = motor_ia_jarvis(df_diario, t_casa, t_fora)
            v_calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
            
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

            r1, r2, r3, r4 = st.columns(4)
            with r1: draw_card("VENCEDOR", m['vencedor'], 85)
            with r2: draw_card("GOLS", m['gols'], 70)
            with r3: draw_card("STAKE", m['stake_val'], 100)
            with r4: draw_card("CANTOS", m['cantos'], 65)
            
            if st.button("📥 SALVAR NO HISTÓRICO"):
                st.session_state.historico_calls.append(m.copy())
                st.toast("✅ SALVO!")
    else:
        st.error("BASE DE DADOS NÃO ENCONTRADA.")

elif st.session_state.aba_ativa == "historico":
    st.markdown("<h2 style='color:white;'>📜 HISTÓRICO DE CALLS</h2>", unsafe_allow_html=True)
    if not st.session_state.historico_calls: st.info("Sem registros.")
    for call in reversed(st.session_state.historico_calls):
        st.markdown(f"""<div style="background:#161b22; border:1px solid #30363d; padding:15px; border-radius:8px; margin-bottom:10px; color:white;">
            <b>[{call['data']}]</b> {call['casa']} x {call['fora']} | <span style="color:#06b6d4;">{call['gols']} | {call['stake_val']}</span>
        </div>""", unsafe_allow_html=True)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL", value=st.session_state.banca_total)
    st.session_state.stake_padrao = st.slider("STAKE (%)", 0.1, 10.0, st.session_state.stake_padrao)

# RODAPÉ
st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v58.7</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
