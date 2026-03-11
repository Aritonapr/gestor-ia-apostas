import streamlit as st

# [GUARDIAN UI PROTECTION SYSTEM - GIAE v3.0] - PROTOCOLO JARVIS ATIVADO
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- INJEÇÃO DE CSS E ESTILIZAÇÃO CRÍTICA (NÃO ALTERAR) ---
st.markdown("""
    <style>
    /* REMOÇÃO DE HEADER E SETAS PADRÃO STREAMLIT */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] { 
        display: none !important; 
    }
    
    /* DEFINIÇÃO DO DARK MODE PROFISSIONAL */
    .stApp { 
        background-color: #0b0e11 !important; 
        color: #e2e8f0 !important; 
        font-family: 'Roboto', sans-serif !important; 
    }
    
    /* NAVBAR SUPERIOR FIXA */
    .betano-header { 
        position: fixed; top: 0; left: 0; width: 100%; height: 50px; 
        background-color: #1a242d; border-bottom: 2px solid #f64d23; 
        display: flex; align-items: center; padding: 0 20px; z-index: 999999; 
    }
    
    @keyframes pulse-hex { 
        0%, 100% { transform: scale(0.9); filter: drop-shadow(0 0 2px #f64d23); } 
        50% { transform: scale(1.1); filter: drop-shadow(0 0 10px #f64d23); } 
    }
    
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }
    
    /* SIDEBAR ULTRA-SUBIDA (PRESERVAÇÃO DE 260PX) */
    [data-testid="stSidebar"] { 
        background-color: #15191d !important; 
        margin-top: 50px !important; 
        border-right: 1px solid #2d3843 !important; 
        width: 260px !important; 
    }
    
    [data-testid="stSidebarContent"] { 
        padding-top: 0px !important; 
        overflow-x: hidden !important; 
    }
    
    /* AJUSTE MILIMÉTRICO DO TOPO DA SIDEBAR (MARGIN-TOP -35PX) */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { 
        gap: 0px !important; 
        padding-top: 0px !important; 
        margin-top: -35px !important; 
    }
    
    /* BOTÃO FERRAMENTA: CÁPSULA SEGMENTADA COM SCANNER LASER */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    @keyframes plasma-glow { 0%, 100% { box-shadow: 0 0 5px #f64d23; } 50% { box-shadow: 0 0 20px #f64d23; } }
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button {
        background: #f64d23 !important; color: white !important; border-radius: 30px !important; 
        height: 44px !important; width: 90% !important; margin: 0px auto 20px 10px !important;
        display: flex !important; flex-direction: column !important; align-items: center !important; 
        justify-content: center !important; padding-left: 40px !important; padding-right: 10px !important; 
        font-weight: 900 !important; font-size: 10px !important; position: relative !important; 
        overflow: hidden !important; animation: plasma-glow 3s infinite ease-in-out !important;
        border: none !important;
    }
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::after {
        content: "" !important; position: absolute !important; top: 0 !important; left: -100% !important; 
        width: 40px !important; height: 100% !important;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important; 
        transform: skewX(-20deg) !important; animation: laser-scan 2.5s infinite linear !important;
    }
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::before {
        content: '🤖'; position: absolute; left: 4px; top: 50%; transform: translateY(-50%); 
        width: 34px; height: 34px; background: white !important; color: #f64d23 !important; 
        border-radius: 50%; display: flex; align-items: center; justify-content: center; 
        font-size: 16px; z-index: 2; border: 2px solid #f64d23;
    }
    
    /* BOTÕES DE CATEGORIA DA SIDEBAR */
    [data-testid="stSidebar"] button { 
        background-color: transparent !important; color: #e2e8f0 !important; 
        border: none !important; border-bottom: 1px solid #1e293b !important; 
        text-align: left !important; font-weight: 700 !important; font-size: 11px !important; 
        padding: 10px 15px !important; min-height: 40px !important; width: 100% !important; 
        border-radius: 0px !important; text-transform: uppercase; 
    }
    
    [data-testid="stSidebar"] button:hover { 
        color: #f64d23 !important; 
        background-color: rgba(246, 77, 35, 0.05) !important;
    }
    
    /* CONTEÚDO PRINCIPAL E RODAPÉ */
    .main .block-container { padding-top: 60px !important; }
    
    .betano-footer { 
        position: fixed; bottom: 0; left: 0; width: 100%; background-color: #1a242d; 
        height: 25px; border-top: 1px solid #2d3843; display: flex; 
        justify-content: space-between; align-items: center; padding: 0 20px; 
        font-size: 9px; color: #94a3b8; z-index: 999999; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- ESTRUTURA HEADER ---
st.markdown(f"""
    <div class="betano-header">
        <div style="width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px; animation: pulse-hex 2s infinite ease-in-out;"></div>
        <div class="logo-text">GESTOR IA</div>
        <div style="display:flex; gap:20px; margin-left:30px; flex-grow:1; color:white; font-size:11px; font-weight:700; text-transform:uppercase;">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span style="color:#f64d23;">Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:12px; align-items:center;">
            <div style="border:1px solid #adb5bd; color:white; padding:4px 12px; border-radius:3px; font-size:11px; font-weight:bold; cursor:pointer;">REGISTRAR</div>
            <button style="background:#00cc66; color:white; padding:6px 20px; border-radius:3px; font-weight:bold; border:none; font-size:11px; cursor:pointer;">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (SISTEMA DE MENU) ---
with st.sidebar:
    st.button("PROCESSAR ALGORITMO") # Botão com efeito Scanner (Primeiro da lista)
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL (COCKPIT) ---
st.markdown("### 🤖 Cockpit de Comando Ativado")
st.info("O sistema está monitorando os mercados em tempo real. Os dados abaixo são processados via Redes Neurais.")

# Conteúdo simulado do cockpit
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Oportunidades Ativas", "12", "+2")
with col2:
    st.metric("Assertividade Média", "87.4%", "+1.2%")
with col3:
    st.metric("Tempo de Resposta", "45ms", "-5ms")

# --- FOOTER ---
st.markdown("""
    <div class="betano-footer">
        <div>STATUS: ● IA OPERACIONAL | PROTEÇÃO DE UI: ON | CONEXÃO ENCRIPTADA</div>
        <div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div>
    </div>
    """, unsafe_allow_html=True)
