import streamlit as st

# 1. Configuração inicial
st.set_page_config(
    page_title="GESTOR IA - TRADING PRO", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. CSS "ULTRA-TIGHT" (SUBIDA MÁXIMA)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700;900&display=swap');

    /* ELIMINAR TUDO DO STREAMLIT */
    header, [data-testid="stHeader"], [data-testid="stSidebarCollapseButton"], [data-testid="collapsedControl"] {
        display: none !important;
    }

    /* FUNDO DARK PROFISSIONAL */
    .stApp { 
        background-color: #0b0e11 !important; 
        color: #e2e8f0 !important; 
        font-family: 'Roboto', sans-serif !important;
    }

    /* --- BARRA SUPERIOR FIXA (50px) --- */
    .betano-header {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 50px;
        background-color: #1a242d;
        border-bottom: 2px solid #f64d23;
        display: flex; align-items: center;
        padding: 0 20px; z-index: 999999;
    }
    .gestor-logo { display: flex; align-items: center; gap: 10px; }
    .logo-text { color: #f64d23; font-weight: 900; font-size: 19px; font-style: italic; }

    /* --- SIDEBAR: FORÇAR SUBIDA TOTAL --- */
    [data-testid="stSidebar"] {
        background-color: #15191d !important;
        margin-top: 50px !important; /* Exatamente abaixo da barra */
        border-right: 1px solid #2d3843 !important;
        width: 260px !important;
    }

    /* REMOVER ESPAÇO NO TOPO DA SIDEBAR */
    [data-testid="stSidebarContent"] {
        padding-top: 0px !important; 
    }
    
    /* REMOVER GAP ENTRE BOTÕES NA SIDEBAR */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0px !important;
        padding-top: 0px !important;
    }

    /* ESTILO DOS BOTÕES (COLADOS UM NO OUTRO) */
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
        border-left: 4px solid #f64d23 !important;
    }

    /* --- CONTEÚDO CENTRAL: SUBIDA TOTAL --- */
    .main .block-container {
        padding-top: 60px !important; /* Espaço apenas para não ficar sob o header */
        max-width: 95% !important;
    }

    /* --- RODAPÉ --- */
    .betano-footer {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background-color: #1a242d;
        height: 25px; border-top: 1px solid #2d3843;
        display: flex; justify-content: space-between; align-items: center;
        padding: 0 20px; font-size: 9px; color: #94a3b8;
        z-index: 999999;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. NAVBAR SUPERIOR
st.markdown("""
    <div class="betano-header">
        <div class="gestor-logo">
            <div style="width:25px; height:28px; background:#f64d23; clip-path:polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); box-shadow: 0 0 10px #f64d23;"></div>
            <div class="logo-text">GESTOR IA</div>
        </div>
        <div style="display:flex; gap:20px; margin-left:30px; flex-grow:1; color:white; font-size:11px; font-weight:700; text-transform:uppercase;">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div style="margin-left:auto; display:flex; gap:15px; align-items:center;">
            <div style="color:white; font-size:14px; cursor:pointer;">🔍</div>
            <div style="border:1px solid #adb5bd; color:white; padding:4px 12px; border-radius:3px; font-size:11px; font-weight:bold; cursor:pointer;">REGISTRAR</div>
            <button style="background:#00cc66; color:white; padding:6px 20px; border-radius:3px; font-weight:bold; border:none; font-size:11px; cursor:pointer;">ENTRAR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. SIDEBAR - OS 8 ITENS DO SEU PAPEL (SUBIDOS)
with st.sidebar:
    st.button("PROCESSAR ALGORITMO")
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# 5. CONTEÚDO PRINCIPAL
st.markdown("### 📊 Dashboard de Análise Profissional")
st.info("A lateral esquerda e o título central foram subidos para encostar no cabeçalho.")

# 6. RODAPÉ
st.markdown("""
    <div class="betano-footer">
        <div>STATUS: ● ONLINE | SERVIDOR: CLOUD-IA</div>
        <div>GESTOR IA PRO v3.0 | 18+ JOGUE COM RESPONSABILIDADE</div>
    </div>
    """, unsafe_allow_html=True)
