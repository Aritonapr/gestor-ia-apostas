import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime
import random

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v73.00 - BILHETE LIMPO E ESTABILIDADE DE HEADER]
# ================================================================= usei um visual de "Recibo de Celular", muito mais fácil de ler e entender os times e as apost=============

st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    as.

*Copie este código integralmente e substitua no seu `app.py` (Lembre-layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INICIALIZAÇÃOse: Tradutor **DESLIGADO**).*

```python
import streamlit as st
import pandas as pd
 DE MEMÓRIA ---
if 'aba_ativa' not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_stateimport os
import json
from datetime import datetime
import random

# ==============================================================================
# [PROTOCOLO DE MANUTENÇÃO v73.00 - BILHETE LIMPO E ESTABILIZA: st.session_state.banca_total = 1000.00
if 'stake_padrao' not in st.session_state: st.session_state.stake_padrao = ÇÃO DE HEADER]
# ==============================================================================

# 1. CONFIGURAÇÃO DE PÁGIN1.0

# --- CARREGAMENTO DE DADOS ---
def carregar_jogos_diarios():A (ESTRITAMENTE O PRIMEIRO COMANDO)
st.set_page_config(
    page_title
    path = "data/database_diario.csv"
    if os.path.exists(path="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state):
        try: return pd.read_csv(path)
        except: return None
    return None="expanded"
)

# --- INICIALIZAÇÃO DE MEMÓRIA ---
if 'aba_ativa'

df_diario = carregar_jogos_diarios()

# --- CSS ÚNICO E O not in st.session_state: st.session_state.aba_ativa = "home"
if 'banca_total' not in st.session_state: st.session_state.banca_total =TIMIZADO (EVITA PISCADAS) ---
st.markdown("""
    <style>
    @import 1000.00
if 'stake_padrao' not in st.session_state: url('https://fonts.googleapis.com/css2?family=Inter:wght@300;4 st.session_state.stake_padrao = 1.0

# --- CARREGAMENTO DE DADOS00;600;800;900&display=swap');
    
    ::-webkit-scrollbar ---
def carregar_jogos_diarios():
    path = "data/database_diario. { display: none !important; }
    html, body, [data-testid="stAppViewContainer"],csv"
    if os.path.exists(path):
        try: return pd.read_csv( .stApp {
        background-color: #0b0e11 !important;
        font-path)
        except: return None
    return None

df_diario = carregar_jogos_family: 'Inter', sans-serif;
    }
    header, [data-testid="stHeader"]diarios()

# 2. CAMADA DE ESTILO CSS (ESTABILIZADA v73.0 { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding: 0)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.90px 40px 20px 40px !important; }
    
    /*com/css2?family=Inter:wght@300;400;500;6 HEADER FIXO */
    .betano-header { 
        position: fixed; top: 0;00;700;800;900&display=swap');
    
    ::- left: 0; width: 100%; height: 60px; 
        background-webkit-scrollbar { display: none !important; }
    * { -ms-overflow-style: none !color: #001a4d !important; border-bottom: 1px solid rgba(25important; scrollbar-width: none !important; }

    html, body, [data-testid="st5,255,255,0.05) !important; 
        display: flex; align-items: center; justify-content: space-between; 
        padding: 0 40px !important; z-index: 1000000; 
    }
    AppViewContainer"], .stApp {
        background-color: #0b0e11 !important;
        font-family: 'Inter', sans-serif;
    }

    [data-testid="st.logo-link { color: #9d54ff !important; font-weight: 900Header"] { display: none !important; }
    [data-testid="stMainBlockContainer"] { padding; font-size: 20px !important; text-transform: uppercase; text-decoration: none;: 80px 40px 20px 40px !important; }
    
    /* HEADER }
    .nav-links { display: flex; gap: 18px; }
    .nav SUPERIOR - OTIMIZADO PARA NÃO PISCAR */
    .betano-header { 
        position-item { color: #ffffff; font-size: 10px; text-transform: uppercase; font-weight: fixed; top: 0; left: 0; width: 100%; height: 6: 600; opacity: 0.8; }
    
    /* SIDEBAR */
    0px; 
        background-color: #001a4d !important; border-bottom:[data-testid="stSidebar"] { min-width: 320px !important; background-color 1px solid rgba(255,255,255,0.05) !: #11151a !important; border-right: 1px solid #1e29important; 
        display: flex; align-items: center; justify-content: space-between; 3b !important; }
    [data-testid="stSidebarContent"] { overflow: hidden !important; }

        padding: 0 40px !important; z-index: 999999; 
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { margin-top: -    }
    
    .logo-link { color: #9d54ff !important; font-30px !important; }
    
    section[data-testid="stSidebar"] div.stButtonweight: 900; font-size: 20px !important; text-transform: uppercase; > button { 
        background-color: transparent !important; color: #94a3b8 ! text-decoration: none; }
    .nav-links { display: flex; gap: 15pximportant; border: none !important; 
        border-bottom: 1px solid #1a20; align-items: center; }
    .nav-item { color: #ffffff; font-size:2c !important; text-align: left !important; width: 100% !important;  10px; text-transform: uppercase; font-weight: 600; white-space: nowrap
        padding: 18px 25px !important; font-size: 10px !important; text; opacity: 0.8; }
    
    .registrar-pill { color: #ffffff; font-size:-transform: uppercase !important;
    }
    section[data-testid="stSidebar"] div.stButton > button 9px; font-weight: 800; border: 1.5px solid #ffffff;:hover { background-color: #1e293b !important; color: #06b6 padding: 6px 15px; border-radius: 20px; }
    .entd4 !important; border-left: 3px solid #6d28d9 !important; }rar-grad { background: linear-gradient(90deg, #6d28d9 0%, #0

    /* BILHETE SIMPLIFICADO E LIMPO */
    .ticket-clean {
        background6b6d4 100%); color: white; padding: 7px 20px; border-: #ffffff !important; color: #1a1a1a !important;
        padding: 30px;radius: 5px; font-weight: 800; font-size: 9px; }

    /* SIDEBAR */
    [data-testid="stSidebar"] { min-width: 30 border-radius: 8px; font-family: 'Inter', sans-serif;
        max-width:0px !important; background-color: #11151a !important; border-right:  500px; margin: 0 auto; box-shadow: 0 20px 41px solid #1e293b !important; }
    
    section[data-testid="0px rgba(0,0,0,0.5);
    }
    .ticket-header {stSidebar"] div.stButton > button { 
        background-color: transparent !important; color: # text-align: center; border-bottom: 2px solid #eee; margin-bottom: 20px; padding-bottom: 10px; }
    .ticket-row { 
        display:94a3b8 !important; border: none !important; 
        border-bottom: 1px solid #1a202c !important; text-align: left !important; width: 1 flex; justify-content: space-between; align-items: center;
        padding: 12px 00% !important; 
        padding: 15px 25px !important; font-size:0; border-bottom: 1px solid #f0f0f0;
    }
    .team 10px !important; text-transform: uppercase !important;
    }
    section[data--name { font-weight: 600; font-size: 13px; color: #111testid="stSidebar"] div.stButton > button:hover { background-color: #1e293b !important; }
    .market-tag { background: #f1f5f9; color: #6d2; color: #06b6d4 !important; border-left: 3px solid #6d28d8d9; padding: 4px 10px; border-radius: 4px; font-weight9 !important; }

    /* BILHETE SIMPLIFICADO */
    .clean-ticket {
: 800; font-size: 10px; }

    .highlight-card { background: #1        background: #ffffff !important; color: #000 !important;
        padding: 201151a; border: 1px solid #1e293b; padding: 2px; border-radius: 8px; font-family: 'Inter', sans-serif;
        max0px; border-radius: 8px; text-align: center; height: 155px-width: 450px; margin: 0 auto; box-shadow: 0 10; }
    .footer-shield { position: fixed; bottom: 0; left: 0; width: 1px 30px rgba(0,0,0,0.5);
    }
    .ticket-header {00%; background-color: #0d0d12; height: 25px; border- text-align: center; border-bottom: 1px solid #eee; margin-bottom: 15px; paddingtop: 1px solid #1e293b; display: flex; justify-content: space--bottom: 10px; }
    .game-row { display: flex; justify-content:between; align-items: center; padding: 0 20px; font-size: 9px; color: #475569; z-index: 999999; } space-between; padding: 8px 0; border-bottom: 1px solid #f9f9f
    </style>
""", unsafe_allow_html=True)

# 3. HEADER HTML
st.markdown("""9; font-size: 13px; }
    .market-badge { background: #f1
    <div class="betano-header">
        <div class="header-left">
            <f5f9; padding: 2px 8px; border-radius: 4px; font-weightdiv class="logo-link">GESTOR IA</div>
            <div class="nav-links">
                <: 800; color: #6d28d9; }

    .highlight-card {div class="nav-item">APOSTAS ESPORTIVAS</div>
                <div class="nav-item background: #11151a; border: 1px solid #1e293b;">APOSTAS AO VIVO</div>
                <div class="nav-item">ESTATÍSTICAS AV padding: 20px; border-radius: 8px; text-align: center; height: ANÇADAS</div>
                <div class="nav-item">ASSERTIVIDADE IA</div>
            </div>
        155px; }
    .footer-shield { position: fixed; bottom: 0; left: 0;</div>
        <div class="header-right">
            <div style="background: linear-gradient(9 width: 100%; background-color: #0d0d12; height: 250deg, #6d28d9, #06b6d4); color:white; padding:7px; border-top: 1px solid #1e293b; display: flex; justify-px 20px; border-radius:5px; font-size:10px; font-weight:8content: space-between; align-items: center; padding: 0 20px; font-size00; cursor:pointer;">ENTRAR</div>
        </div>
    </div>
""", unsafe_allow_html=: 9px; color: #475569; z-index: 9999True)

# 4. SIDEBAR
with st.sidebar:
    st.markdown('<div style="99; }
    </style>
""", unsafe_allow_html=True)

# 3.height:75px;"></div>', unsafe_allow_html=True) 
    if st.button(" HEADER HTML FIXO
st.markdown("""
    <div class="betano-header">
        <div🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_ativa = "analise"
     class="header-left">
            <div class="logo-link">GESTOR IA</div>
            <divif st.button("📡 SCANNER EM TEMPO REAL"): st.session_state.aba_ativa = "live" class="nav-links">
                <div class="nav-item">APOSTAS ESPORTIVAS</div>
    if st.button("💰 GESTÃO DE BANCA"): st.session_state.aba_ativa
                <div class="nav-item">APOSTAS AO VIVO</div>
                <div class="nav = "gestao"
    if st.button("📅 JOGOS DO DIA"): st.session_state-item">ESTATÍSTICAS</div>
                <div class="nav-item">PROBABILIDADES</div>
            </div>.aba_ativa = "home"
    if st.button("🏆 VENCEDORES DA COMPETIÇÃO"):
        </div>
        <div class="header-right">
            <div class="registrar-pill">REG st.session_state.aba_ativa = "vencedores"
    if st.button("⚽ AISTRAR</div>
            <div class="entrar-grad">ENTRAR</div>
        </div>
    </div>
POSTAS POR GOLS"): st.session_state.aba_ativa = "gols"
    if st""", unsafe_allow_html=True)

# 4. SIDEBAR NAVEGAÇÃO
with st.sidebar:
.button("🚩 APOSTAS POR ESCANTEIOS"): st.session_state.aba_ativa = "esc    st.markdown('<div style="height:65px;"></div>', unsafe_allow_html=True)anteios"
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🎟 
    if st.button("🎯 SCANNER PRÉ-LIVE"): st.session_state.aba_️ GERAR BILHETE DO DIA"): st.session_state.aba_ativa = "bilhete"

ativa = "analise"
    if st.button("📡 SCANNER EM TEMPO REAL"): st.session_statedef draw_card(title, value, perc):
    st.markdown(f"""<div class="highlight.aba_ativa = "live"
    if st.button("💰 GESTÃO DE BANCA"): st-card"><div style="color:#64748b; font-size:9px; text-.session_state.aba_ativa = "gestao"
    if st.button("📅 JOGOStransform: uppercase; font-weight: 700;">{title}</div><div style="color:white DO DIA"): st.session_state.aba_ativa = "home"
    if st.button("🏆; font-size:16px; font-weight:900; margin-top:10px VENCEDORES"): st.session_state.aba_ativa = "vencedores"
    if st.;">{value}</div><div style="background:#1e293b; height:4px; widthbutton("⚽ APOSTAS POR GOLS"): st.session_state.aba_ativa = "gols":80%; border-radius:10px; margin:10px auto;"><div style="background:linear-gradient(90deg, #6d28d9, #06b6d4);
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🎟️ GERAR BILHETE DO DIA"): st.session_state.aba_ativa = "bilhete"

def draw_ height:100%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

card(title, value, perc):
    st.markdown(f"""<div class="highlight-card"><# --- TELAS ---
if st.session_state.aba_ativa == "home":
    st.markdown("<hdiv style="color:#64748b; font-size:9px; text-transform: uppercase2 style='color:white;'>📅 JOGOS DO DIA</h2>", unsafe_allow_html=True)
; font-weight: 700;">{title}</div><div style="color:white; font-    c1, c2, c3, c4 = st.columns(4)
    with c1size:16px; font-weight:900; margin-top:10px;">{value: draw_card("BANCA ATUAL", f"R$ {st.session_state.banca_}</div><div style="background:#1e293b; height:4px; width:80total:,.2f}", 100)
    with c2: draw_card("ASSERTIVIDADE%; border-radius:10px; margin:10px auto;"><div style="background:linear-gradient", "92.4%", 92)
    with c3: draw_card("SUGESTÃO(90deg, #6d28d9, #06b6d4); height:1", "OVER 2.5", 88)
    with c4: draw_card("SIST00%; width:{perc}%;"></div></div></div>""", unsafe_allow_html=True)

# --- TELEMA", "JARVIS v73.00", 100)

elif st.session_stateAS ---
if st.session_state.aba_ativa == "home":
    st.markdown("<h2 style.aba_ativa == "bilhete":
    st.markdown("<h2 style='color:white; text='color:white;'>📅 RESUMO DO DIA</h2>", unsafe_allow_html=True)
    c1,-align:center;'>🎟️ SEU BILHETE PRONTO</h2>", unsafe_allow_html=True) c2, c3, c4 = st.columns(4)
    with c1: draw_card
    if df_diario is not None and not df_diario.empty:
        top_2("BANCA ATUAL", f"R$ {st.session_state.banca_total:,.20 = df_diario.head(20)
        
        # CONSTRUÇÃO SEGURA DO BILf}", 100)
    with c2: draw_card("ASSERTIVIDADE", "92HETE
        ticket_html = f"""
        <div class="ticket-clean">
            <div.4%", 92)
    with c3: draw_card("SUGESTÃO", "OVER 2.5", 88)
    with c4: draw_card("SISTEMA", "JAR class="ticket-header">
                <div style="font-weight:900; font-size:18VIS v73.00", 100)

elif st.session_state.aba_ativapx;">GESTOR IA PRO</div>
                <div style="font-size:10px; color:#666; == "bilhete":
    st.markdown("<h2 style='color:white; text-align:center margin-top:5px;">GERADO EM: {datetime.now().strftime('%d/%m/%Y %;'>🎟️ SEU BILHETE PRONTO</h2>", unsafe_allow_html=True)
    if df_diarioH:%M')}</div>
            </div>
        """
        for _, row in top_20.iterrows():
             is not None and not df_diario.empty:
        top_20 = df_diario.ticket_html += f"""
            <div class="ticket-row">
                <span class="team-name">{row['TIME_CASA']} x {row['TIME_FORA']}</span>
                <span classhead(20)
        
        # MONTAGEM SIMPLIFICADA DO BILHETE
        conteudo_bilhete = ""
        for _, row in top_20.iterrows():
            conteudo_bilhete="market-tag">OVER 1.5 GOLS</span>
            </div>
            """
        ticket_html += "</div>"
        
        col_x1, col_x2, col_x3 = st.columns([1, += f"""
            <div class="game-row">
                <span>{row['TIME_CASA']} x {row['TIME_FORA']}</span>
                <span class="market-badge">OVER 1.5</span>
 2, 1])
        with col_x2:
            st.markdown(ticket_html, unsafe_allow_html=True)
    else: st.error("Aguardando carregamento de jogos...")            </div>
            """
        
        # IMPRESSÃO ÚNICA DO HTML
        st.markdown(f

st.markdown("""<div class="footer-shield"><div>STATUS: ● IA OPERACIONAL | v7"""
            <div class="clean-ticket">
                <div class="ticket-header">
                    <3.00</div><div>JARVIS PROTECT</div></div>""", unsafe_allow_html=True)
