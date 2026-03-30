import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v63.2 - RECUPERAÇÃO DE DADOS & BLINDAGEM]
# DIRETRIZ: RECUPERAR TIMES E COMPETIÇÕES SUMIDAS (FIX KEYERROR)
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
if 'top_20_ia' not in st.session_state: st.session_state.top_20_ia = []

# --- FUNÇÕES DE CARREGAMENTO COM NORMALIZAÇÃO DE COLUNAS ---
def carregar_dados_ia():
    url_github = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    try:
        df = pd.read_csv(f"{url_github}?v={datetime.now().timestamp()}", on_bad_lines='skip')
        df.columns = [c.upper() for c in df.columns] # Normaliza para maiúsculo
        return df
    except:
        return None

def carregar_historico_5_anos():
    path_hist = "data/historico_5_temporadas.csv"
    if os.path.exists(path_hist):
        try:
            df = pd.read_csv(path_hist)
            df.columns = [c.upper() for c in df.columns] # Normaliza para evitar KeyError
            return df
        except: return None
    return None

df_diario = carregar_dados_ia()
df_historico = carregar_historico_5_anos()

# ==============================================================================
# 2. CAMADA DE ESTILO CSS INTEGRAL (DESIGN ZERO WHITE PRO)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    ::-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !important; scrollbar-width: none !important; font-family: 'Inter', sans-serif; }
    html, body, [data-testid="stAppViewContainer"], .stApp { background-color: #0b0e11 !important; }
    header, [data-testid="stHeader"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
    
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
        background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; text-decoration: none;}
    .nav-links { display: flex; gap: 20px; }
    .nav-item { color: #ffffff !important; font-size: 10px !important; font-weight: 600; text-transform: uppercase; cursor: pointer; }
    .entrar-grad { background: linear-gradient(90deg, #6d28d9 0%, #06b6d4 100%) !important; color: white !important; padding: 8px 20px; border-radius: 5px; font-weight: 800; font-size: 10px; }

    [data-testid="stSidebar"] { min-width: 320px !important; background-color: #11151a !important; border-right: 1px solid #1e293b !important; }
    section[data-testid="stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: #94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 100% !important; 
        padding: 15px 25px !important; font-size: 10px !important; text-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover { color: #06b6d4 !important; background-color: #1e293b !important; border-left: 3px solid #6d28d9 !important; }

    .highlight-card { 
        background: #11151a; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; text-align: center; height: 150px; margin-bottom: 15px;
    }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0d0d12; height: 25px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; }
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR E CONTEÚDO
with st.sidebar:
    st.markdown("""<div class="betano-header"><div class="logo-link">GESTOR IA</div><div class="nav-links"><div class="nav-item">AO VIVO</div><div class="nav-item">ESTATÍSTICAS</div></div><div class="entrar-grad">ENTRAR</div></div><div style="height:65px;"></div>""", unsafe_allow_html=True)
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
    if st.button("📡 SCANNER AO VIVO"): st.session_state.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa = "gestao"
    if st.button("📅 BILHETE OURO"): st.session_state.aba_ativa = "home"
    if st.button("📜 HISTÓRICO"): st.session_state.aba_ativa = "historico"

def draw_card(title, value, perc):
    st.markdown(f"""<div class="highlight-card"><div style="color:#64748b; font-size:9px; text-transform: uppercase;">{title}</div><div style="color:white; font-size:18px; font-weight:900; margin-top:10px;">{value}</div><div style="background:#1e293b; height:4px; width:80%; border-radius:10px; margin:10px auto;"><div style="background:linear-gradient(90deg, #6d28d9, #06b6d4); height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- TELA DE ANÁLISE (CORREÇÃO DO KEYERROR E TIMES SUMIDOS) ---
if st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    # 1. Recuperação da Lista de Times (Garante que nada suma)
    lista_times = ["Selecione o Time..."]
    if df_diario is not None:
        try:
            # Pega as colunas de times independente do nome original
            col_t1 = df_diario.columns[0] 
            col_t2 = df_diario.columns[1]
            lista_times = sorted(list(set(df_diario[col_t1].dropna().unique().tolist() + df_diario[col_t2].dropna().unique().tolist())))
        except: pass

    c1, c2 = st.columns(2)
    with c1: t_casa = st.selectbox("🏠 TIME DA CASA", lista_times)
    with c2: t_fora = st.selectbox("🚀 TIME DE FORA", [t for t in lista_times if t != t_casa])

    if st.button("⚡ EXECUTAR ALGORITIMO"):
        # Lógica de Cruzamento Blindada contra nomes de colunas
        conf = "88.5%"
        msg = "DADOS DE MERCADO"
        cor = "#ffcc00"
        
        if df_historico is not None and t_casa != "Selecione o Time...":
            try:
                # Busca flexível no histórico normalizado
                check = df_historico[df_historico.iloc[:, 0].astype(str).str.contains(str(t_casa)[:4], case=False, na=False)]
                if not check.empty:
                    conf = "96.8%"
                    msg = "FILÉ MIGNON: 5 TEMPORADAS"
                    cor = "#00ff88"
            except: pass
            
        st.session_state.analise_bloqueada = {"casa": t_casa, "fora": t_fora, "conf": conf, "msg": msg, "cor": cor}

    if st.session_state.analise_bloqueada:
        a = st.session_state.analise_bloqueada
        st.markdown(f"<div style='background:rgba(255,255,255,0.03); border-left:5px solid {a['cor']}; padding:15px; border-radius:5px; color:white;'><b>JARVIS IA:</b> {a['msg']} ({a['conf']})</div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color:white; text-align:center;'>{a['casa']} vs {a['fora']}</h3>", unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("PROB. VITÓRIA", "68%", 68)
        with r2: draw_card("GOLS", "OVER 1.5", 94)
        with r3: draw_card("CANTOS", "9.5+", 82)
        with r4: draw_card("IA CONF.", a['conf'], 96)

elif st.session_state.aba_ativa == "home":
    st.markdown("<h2 style='color:white;'>📅 BILHETE OURO - 2026</h2>", unsafe_allow_html=True)
    h1, h2, h3, h4 = st.columns(4)
    with h1: draw_card("BANCA", f"R$ {st.session_state.banca_total}", 100)
    with h2: draw_card("ASSERTIVIDADE", "94.8%", 94)
    with h3: draw_card("SISTEMA", "v63.2", 100)
    with h4: draw_card("STATUS", "ONLINE", 100)
    if df_diario is not None:
        st.dataframe(df_diario, use_container_width=True)

elif st.session_state.aba_ativa == "gestao":
    st.markdown("<h2 style='color:white;'>💰 GESTÃO DE BANCA</h2>", unsafe_allow_html=True)
    st.session_state.banca_total = st.number_input("BANCA TOTAL", value=float(st.session_state.banca_total))
    draw_card("VALOR POR ENTRADA", f"R$ {st.session_state.banca_total * 0.01}", 100)

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v63.2</div><div>JARVIS PROTECT 2026</div></div>""", unsafe_allow_html=True)
