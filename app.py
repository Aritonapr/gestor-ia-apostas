import streamlit as st

# Configuração da Página
st.set_page_config(page_title="GESTOR IA - PRO", layout="wide")

# --- CSS PARA PADRÃO BETANO + SEU ESBOÇO ---
st.markdown("""
    <style>
    /* 1. Reset e Fundo */
    .stApp {
        background-color: #f0f2f5; /* Fundo cinza claro da Betano */
    }

    /* 2. BARRA SUPERIOR (NAVBAR) - EXATO AO SEU DESENHO */
    .navbar {
        background-color: #1a242d; /* Azul escuro Betano */
        color: white;
        padding: 0 20px;
        display: flex;
        align-items: center;
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 60px;
        z-index: 1000;
        border-bottom: 3px solid #f64d23; /* Linha laranja clássica */
    }
    .logo-gestor {
        font-weight: 900;
        font-size: 22px;
        color: white;
        margin-right: 40px;
        letter-spacing: -1px;
    }
    .nav-items {
        display: flex;
        gap: 25px;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        color: #adb5bd;
    }
    .nav-items span:hover { color: white; cursor: pointer; }
    
    .nav-right {
        margin-left: auto;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .btn-registrar {
        border: 1px solid #adb5bd;
        padding: 5px 15px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: bold;
    }
    .btn-entrar {
        background-color: #00cc66; /* Verde Betano */
        padding: 6px 18px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: bold;
        border: none;
    }

    /* 3. SIDEBAR (MENU LATERAL) - CONFORME O PAPEL */
    [data-testid="stSidebar"] {
        background-color: white !important;
        border-right: 1px solid #ddd;
        padding-top: 80px;
    }
    /* Estilo dos botões da sidebar para parecerem lista de menu */
    .stButton > button {
        width: 100%;
        background: none;
        border: none;
        border-bottom: 1px solid #f0f2f5;
        border-radius: 0;
        color: #1a242d;
        text-align: left;
        padding: 12px 10px;
        font-weight: 600;
        font-size: 13px;
        text-transform: uppercase;
    }
    .stButton > button:hover {
        background-color: #f6f7f9;
        color: #f64d23;
    }

    /* Espaçamento do conteúdo principal */
    .main-box {
        margin-top: 80px;
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVBAR HTML (TOP BAR) ---
st.markdown("""
    <div class="navbar">
        <div class="logo-gestor">GESTOR IA</div>
        <div class="nav-items">
            <span>Apostas Esportivas</span>
            <span>Apostas ao Vivo</span>
            <span>Apostas Encontradas</span>
            <span>Assertividade IA</span>
        </div>
        <div class="nav-right">
            <span>🔍</span>
            <div class="btn-registrar">REGISTRAR</div>
            <div class="btn-entrar">ENTRAR</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (CONTEÚDO DO PAPEL) ---
with st.sidebar:
    # Estado para controlar o que aparece no centro
    if 'view' not in st.session_state:
        st.session_state.view = "home"

    if st.button("PROCESSAR ALGORITMO"):
        st.session_state.view = "processar"
    
    st.button("PRÓXIMOS JOGOS")
    st.button("VENCEDORES DA COMPETIÇÃO")
    st.button("APOSTAS POR ODDS")
    st.button("APOSTAS POR GOLS")
    st.button("APOSTAS POR ESCANTEIOS")
    st.button("APOSTAS POR CARTÕES")
    st.button("ÁRBITRO DA PARTIDA")

# --- ÁREA CENTRAL (CONTEÚDO DINÂMICO) ---
st.markdown('<div class="main-box">', unsafe_allow_html=True)

if st.session_state.view == "home":
    st.subheader("Bem-vindo ao Gestor IA")
    st.write("Utilize o menu lateral para iniciar as análises.")

elif st.session_state.view == "processar":
    st.markdown("### 🏟️ Seleção de Campeonato")
    
    # Grid de Campeonatos conforme solicitado
    camp_col = st.selectbox(
        "Escolha o Campeonato para análise:",
        ["Selecione...", "BRASIL (Série A, B, C, D)", "LA LIGA (Espanha)", "PREMIER LEAGUE (Inglaterra)"]
    )

    if camp_col != "Selecione...":
        st.markdown("---")
        st.markdown("### ⚽ Escolha os Times")
        
        col_time_a, col_vs, col_time_b = st.columns([2, 0.5, 2])
        
        # Dados fictícios para mostrar a funcionalidade
        times_map = {
            "BRASIL (Série A, B, C, D)": ["Flamengo", "Palmeiras", "Santos", "Botafogo", "Amazonas", "América-MG"],
            "LA LIGA (Espanha)": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Sevilla"],
            "PREMIER LEAGUE (Inglaterra)": ["Man City", "Arsenal", "Liverpool", "Man United"]
        }
        
        lista_times = times_map.get(camp_col, [])

        with col_time_a:
            time_1 = st.selectbox("Mandante", ["Selecione..."] + lista_times)
        with col_vs:
            st.markdown("<h3 style='text-align:center; padding-top:25px;'>VS</h3>", unsafe_allow_html=True)
        with col_time_b:
            time_2 = st.selectbox("Visitante", ["Selecione..."] + lista_times)

        if time_1 != "Selecione..." and time_2 != "Selecione...":
            if st.button("🚀 EXECUTAR ANÁLISE DO CONFRONTO", use_container_width=True):
                st.success(f"Analisando: {time_1} vs {time_2}. Aguarde o processamento dos algoritmos...")

st.markdown('</div>', unsafe_allow_html=True)

# Rodapé (opcional)
st.markdown("""
    <div style="text-align: center; color: #999; font-size: 11px; margin-top: 30px;">
        GESTOR IA - Sistema de Gestão Esportiva Profissional
    </div>
    """, unsafe_allow_html=True)
