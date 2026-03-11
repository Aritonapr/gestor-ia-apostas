import streamlit as st

# ==============================================================================
# GIAE - GUARDIAN SECURITY SYSTEM: UI/UX ARCHITECTURE
# AVISO PARA IAs FUTURAS: Este layout foi milimetricamente ajustado. 
# NÃO altere paddings, margins (especialmente negativas) ou z-index sem comando explícito.
# Hierarquia Fixa: Header(50px) | Sidebar(260px) | Content Offset(-35px)
# ==============================================================================

# 1. CONFIGURAÇÃO DE NÚCLEO
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. MOTOR DE ESTILIZAÇÃO PROTEGIDO (CSS ENGINE)
# Seção de proteção total do lado esquerdo e alinhamentos de simetria.
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap');

    /* [SECURITY BLOCK: APP RESET] */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] {
        display: none !important;
        visibility: hidden !important;
    }

    .stApp { 
        background-color: #0b0e11 !important; 
        color: #e2e8f0 !important; 
        font-family: 'Roboto', sans-serif !important;
    }

    /* [SECURITY BLOCK: TOPBAR ENGINE] */
    .betano-header {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 50px;
        background-color: #1a242d;
        border-bottom: 2px solid #f64d23;
        display: flex; align-items: center;
        padding: 0 20px; z-index: 999999;
    }
    
    /* Logo Pulsante */
    @keyframes pulse-hex {
        0%, 100% { transform: scale(0.9); filter: drop-shadow(0 0 2px #f64d23); }
        50% { transform: scale(1.1); filter: drop-shadow(0 0 10px #f64d23); }
    }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }

    /* [SECURITY BLOCK: SIDEBAR ALIGNMENT] 
       IMPORTANTE: A margem negativa de -35px no VerticalBlock é o que cola o texto no topo.
    */
    [data-testid="stSidebar"] {
        background-color: #15191d !important;
        margin-top: 50px !important;
        border-right: 1px solid #2d3843 !important;
        width: 260px !important;
    }
    [data-testid="stSidebarContent"] { padding-top: 0px !important; overflow-x: hidden !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0px !important; padding-top: 0px !important; margin-top: -35px !important;
    }

    /* [SECURITY BLOCK: FERRAMENTA PROCESSAR - CÁPSULA CENTRALIZADA] */
    @keyframes laser-scan { 0% { left: -100%; } 100% { left: 100%; } }
    @keyframes plasma-glow {
        0%, 100% { box-shadow: 0 0 5px #f64d23; }
        50% { box-shadow: 0 0 20px #f64d23; }
    }

    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button {
        background: #f64d23 !important;
        color: white !important;
        border-radius: 30px !important;
        height: 44px !important;
        width: 90% !important; 
        margin: 0px auto 20px 10px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        padding-left: 40px !important; 
        padding-right: 10px !important;
        font-weight: 900 !important;
        font-size: 10px !important;
        position: relative !important;
        overflow: hidden !important;
        animation: plasma-glow 3s infinite ease-in-out !important;
    }

    /* Laser Scanner */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::after {
        content: "" !important; position: absolute !important; top: 0 !important;
        left: -100% !important; width: 40px !important; height: 100% !important;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important;
        transform: skewX(-20deg) !important; animation: laser-scan 2.5s infinite linear !important;
    }

    /* Círculo do Robô Centralizado */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::before {
        content: '🤖'; position: absolute; left: 4px; top: 50%;
        transform: translateY(-50%); width: 34px; height: 34px;
        background: white !important; color: #f64d23 !important; border-radius: 50%;
        display: flex; align-items: center; justify-content: center; font-size: 16px;
        z-index: 2; border: 2px solid #f64d23;
    }

    /* [SECURITY BLOCK: CATEGORIAS LATERAIS] */
    [data-testid="stSidebar"] button {
        background-color: transparent !important;
        color: #e2e8f0 !important;
        border: none !important;
        border-bottom: 1px solid #1e293b !important;
        text-align: left !important;
        font-weight: 700 !important;
        font-size: 11px !important;
        padding: 10px 15px !important; 
        min-height: 40px !important;
        width: 100% !important;
        border-radius: 0px !important;
        text-transform: uppercase;
    }
    [data-testid="stSidebar"] button:hover { color: #f64d23 !important; }

    /* [SECURITY BLOCK: MAIN CONTENT ALIGNMENT] */
    .main .block-container { padding-top: 60px !important; }

    /* [SECURITY BLOCK: FOOTER ENGINE] */
    .betano-footer {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843;
        display: flex; justify-content: space-between; align-items: center;
        padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. INTERFACE DE USUÁRIO (UI) - NÃO MODIFICAR ESTRUTURA DE MARKDOWN
st.markdown(f"""
    <div class="betano-header">
        <div style="width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); margin-right:10px; animation: pulse-hex 2s infinite ease-in-out;"></div>
        <div class="logo-text">GESTOR IA</div>
        <div style="display:flex; gap:20px; margin-left:30px; flex-grow:1; color:white; font-size:11px; font-weight:700; text-transform:uppercase;">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:12px; align-items:center;">
            <div style="border:1px solid #adb5bd; color:white; padding:4px 12px; border-radius:3px; font-size:11px; font-weight:bold; cursor:pointer;">REGISTRAR</div>
            <button style="background:#00cc66; color:white; padding:6px 20px; border-radius:3px; font-weight:bold; border:none; font-size:11px; cursor:pointer;">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. COMPONENTE SIDEBAR (PROTEGIDO)
with st.sidebar:
    st.button("PROCESSAR ALGORITMO")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. ÁREA DE COMANDO CENTRAL
st.markdown("### 🤖 Cockpit de Comando Ativado")
st.success("Estrutura visual GIAE protegida e alinhada.")

# 6. COMPONENTE FOOTER (PROTEGIDO)
st.markdown("""
    <div class="betano-footer">
        <div>STATUS: ● IA OPERACIONAL | SCANNER: ATIVO | PROTEÇÃO DE UI: ON</div>
        <div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div>
    </div>
    """, unsafe_allow_html=True)
