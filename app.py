import streamlit as st

# 1. Configuração inicial
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. CSS PARA A MOLDURA NEON DA FERRAMENTA (SEM QUADRADO SÓLIDO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap');

    /* ANIMAÇÃO DE SCANNER (LINHA DE LUZ PASSANDO) */
    @keyframes scanner-light {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }

    /* ELIMINAR TUDO DO STREAMLIT */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] {
        display: none !important;
    }

    .stApp { 
        background-color: #0b0e11 !important; 
        color: #e2e8f0 !important; 
        font-family: 'Roboto', sans-serif !important;
    }

    /* --- BARRA SUPERIOR FIXA --- */
    .betano-header {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 50px;
        background-color: #1a242d;
        border-bottom: 2px solid #f64d23;
        display: flex; align-items: center;
        padding: 0 20px; z-index: 999999;
    }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }

    /* --- SIDEBAR CORRIGIDA --- */
    [data-testid="stSidebar"] {
        background-color: #15191d !important;
        margin-top: 50px !important;
        border-right: 1px solid #2d3843 !important;
        width: 260px !important;
    }
    [data-testid="stSidebarContent"] { padding-top: 0px !important; }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0px !important; padding-top: 0px !important; }

    /* --- ESTILIZAÇÃO DA FERRAMENTA "PROCESSAR" (MOLDURA NEON) --- */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button {
        background: rgba(246, 77, 35, 0.05) !important; /* Fundo quase invisível */
        color: #f64d23 !important; /* Texto Laranja Neon */
        border: 1px solid #f64d23 !important; /* Borda fina neon */
        font-weight: 900 !important;
        font-size: 11.5px !important;
        height: 45px !important;
        margin: 10px 5px 20px 5px !important; /* Espaçamento externo */
        border-radius: 4px !important;
        box-shadow: 0 0 10px rgba(246, 77, 35, 0.2) !important; /* Brilho externo sutil */
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
    }

    /* ADICIONANDO O EFEITO DE SCANNER (BRILHO PASSANDO) */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::after {
        content: "";
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        background-size: 200% 100%;
        animation: scanner-light 3s infinite linear;
    }

    /* ÍCONE DE ALVO NO PROCESSAR */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child button::before {
        content: '🎯 '; 
        margin-right: 5px;
    }

    /* ESTILO DOS OUTROS BOTÕES (CATEGORIAS) */
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
    [data-testid="stSidebar"] button:hover {
        color: #f64d23 !important;
        background-color: #1e293b !important;
    }

    /* CONTEÚDO CENTRAL */
    .main .block-container { padding-top: 60px !important; }

    /* RODAPÉ */
    .betano-footer {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background-color: #1a242d; height: 25px; border-top: 1px solid #2d3843;
        display: flex; justify-content: space-between; align-items: center;
        padding: 0 20px; font-size: 9px; color: #94a3b8; z-index: 999999;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVBAR SUPERIOR (MANTENDO O LOGO PULSANTE)
st.markdown("""
    <div class="betano-header">
        <div style="display:flex; align-items:center; gap:10px;">
            <div style="width:20px; height:24px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); filter: drop-shadow(0 0 5px #f64d23);"></div>
            <div class="logo-text">GESTOR IA</div>
        </div>
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

# 4. SIDEBAR - COM MOLDURA NEON NA FERRAMENTA
with st.sidebar:
    # A Ferramenta (Recebe a moldura neon via CSS)
    st.button("PROCESSAR ALGORITMO")
    
    # Categorias de Apoio
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. CONTEÚDO PRINCIPAL
st.markdown("### 💠 Cockpit de Operação Profissional")
st.info("A ferramenta 'PROCESSAR ALGORITMO' agora possui uma moldura neon com efeito de scanner, separando o comando das categorias.")

# 6. RODAPÉ
st.markdown("""
    <div class="betano-footer">
        <div>STATUS: ● IA OPERACIONAL | SERVIDOR: PRINCIPAL</div>
        <div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div>
    </div>
    """, unsafe_allow_html=True)
