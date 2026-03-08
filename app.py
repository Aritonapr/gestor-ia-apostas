import streamlit as st
import hashlib

# --- 1. CONFIGURAÇÃO DA PÁGINA (Aumentei a largura da sidebar para acomodar os botões) ---
st.set_page_config(
    page_title="GESTOR IA - PRO EDITION", 
    layout="wide", 
    page_icon="⚽",
    initial_sidebar_state="expanded"
)

# --- 2. BANCO DE DADOS ---
DIC_TIMES = {
    "BRA_A": ["Flamengo", "Palmeiras", "Botafogo", "Fortaleza", "São Paulo", "Bahia", "Cruzeiro", "Internacional", "Atlético-MG", "Vasco", "Corinthians", "Fluminense", "Grêmio", "Athletico-PR", "Vitória", "Juventude", "Criciúma", "Cuiabá", "Atlético-GO", "Bragantino"],
    "BRA_B": ["Santos", "Sport", "Novorizontino", "Mirassol", "Vila Nova", "América-MG", "Ceará", "Coritiba", "Avaí", "Operário-PR", "Amazonas", "Goiás"],
    "BRA_C": ["Náutico", "Remo", "Figueirense", "CSA", "Botafogo-PB", "ABC", "Londrina", "Caxias", "Ferroviária", "São Bernardo", "Volta Redonda", "Ypiranga"],
    "BRA_D": ["Retrô", "Anápolis", "Iguatu", "Itabaiana", "Brasil de Pelotas", "Maringá", "Inter de Limeira", "Treze"],
    "CDB": ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Atlético-MG", "Vasco", "Grêmio", "Bahia", "Internacional", "Fluminense"],
    "CNE": ["Bahia", "Fortaleza", "Sport", "Ceará", "Vitória", "CRB", "Náutico", "Sampaio Corrêa"],
    "ENG_P": ["Man. City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Man. United", "Newcastle"],
    "ESP_L": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Athletic Bilbao", "Real Sociedad", "Sevilla"],
    "ITA_A": ["Inter de Milão", "Milan", "Juventus", "Atalanta", "Roma", "Napoli", "Lazio", "Bologna"],
    "GER_B": ["Bayer Leverkusen", "Bayern de Munique", "Stuttgart", "RB Leipzig", "Borussia Dortmund", "Eintracht Frankfurt"],
    "FRA_L": ["PSG", "Monaco", "Lille", "Brest", "Nice", "Lyon", "Marseille"],
    "UCL": ["Real Madrid", "Man. City", "Bayern", "Arsenal", "Barcelona", "Inter", "PSG", "Bayer Leverkusen"],
    "EURO_C": ["Espanha", "Inglaterra", "França", "Alemanha", "Portugal", "Itália", "Holanda"],
    "SAUDI": ["Al-Hilal", "Al-Nassr", "Al-Ittihad", "Al-Ahli", "Al-Ettifaq"],
    "USA_MLS": ["Inter Miami", "LA Galaxy", "Columbus Crew", "LAFC", "Cincinnati"],
    "LIB": ["Flamengo", "Palmeiras", "River Plate", "Botafogo", "São Paulo", "Atlético-MG"],
    "SUL": ["Cruzeiro", "Corinthians", "Fortaleza", "Racing", "Lanús", "Athletico-PR"]
}

# --- 3. CSS "ICON-BUTTON" BLINDADO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@400;600;800&display=swap');
    
    /* Configurações de Fundo e Sidebar */
    .stApp { background-color: #0b1218; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { 
        background-color: #0b1218 !important; 
        border-right: 2px solid #f05a22 !important; 
        min-width: 300px !important; /* Sidebar levemente mais larga para evitar quebra */
    }

    /* ESTILO DOS BOTÕES DA SIDEBAR (LIGAS) */
    div[data-testid="stSidebar"] .stButton > button { 
        background: linear-gradient(90deg, rgba(240, 90, 34, 0.1) 0%, rgba(26, 36, 45, 0.8) 20%) !important;
        color: #cbd5e0 !important; 
        font-size: 10px !important; /* Fonte ajustada para não sair do botão */
        border-radius: 20px !important; 
        margin-bottom: 2px !important; 
        border: 1px solid rgba(240, 90, 34, 0.2) !important; 
        height: 38px !important; /* Altura fixa para todos */
        width: 100% !important; /* Ocupa toda a coluna */
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 12px !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important; /* Coloca ... se o texto for gigante */
        transition: all 0.3s ease !important;
    }

    div[data-testid="stSidebar"] .stButton > button:hover { 
        background: linear-gradient(90deg, #f05a22 0%, rgba(240, 90, 34, 0.3) 100%) !important;
        color: #ffffff !important; 
        border: 1px solid #f05a22 !important;
        transform: translateX(3px);
    }

    /* BOTÃO SELECIONADO (PRIMARY) */
    div[data-testid="stSidebar"] .stButton > button[kind="primary"] { 
        background: linear-gradient(90deg, #f05a22 0%, #ff8c00 100%) !important;
        color: #ffffff !important; 
        font-weight: 800 !important;
        box-shadow: 0 0 10px rgba(240, 90, 34, 0.3) !important;
        border: none !important;
    }

    /* CATEGORIAS (BOTÕES LARGOS) */
    .cat-button button { 
        background: rgba(240, 90, 34, 0.05) !important; 
        border-radius: 8px !important;
        height: 45px !important;
        border-left: 4px solid #f05a22 !important;
        border-bottom: 1px solid rgba(240, 90, 34, 0.2) !important;
        font-weight: 800 !important;
        letter-spacing: 1px !important;
        margin-top: 10px !important;
    }

    /* BOTÃO PROCESSAR (LARANJA DESTAQUE) */
    div.stButton > button[kind="primary"]:not(div[data-testid="stSidebar"] *) {
        background: linear-gradient(90deg, #f05a22 0%, #ff8c00 100%) !important;
        height: 45px !important;
        border-radius: 25px !important;
        font-weight: 900 !important;
        box-shadow: 0 4px 15px rgba(240, 90, 34, 0.4) !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. ENGINE DE SEGURANÇA (FUNÇÕES) ---
def render_sidebar_button(icon, label, league_id, full_name):
    """Garante que todos os botões de liga sigam o mesmo padrão visual"""
    is_active = st.session_state.liga_ativa == league_id
    if st.button(f"{icon} {label}", key=f"btn_{league_id}", type="primary" if is_active else "secondary", use_container_width=True):
        st.session_state.liga_ativa = league_id
        st.session_state.nome_liga = full_name
        st.rerun()

def render_category(label, menu_id):
    """Garante que as categorias sejam consistentes"""
    st.markdown(f'<div class="cat-button">', unsafe_allow_html=True)
    if st.button(label, key=f"cat_{menu_id}", use_container_width=True):
        st.session_state.menu_aberto = menu_id if st.session_state.menu_aberto != menu_id else None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 5. NAVEGAÇÃO ---
if 'liga_ativa' not in st.session_state: st.session_state.update(liga_ativa='BRA_A', nome_liga='BRASILEIRÃO A')
if 'menu_aberto' not in st.session_state: st.session_state.menu_aberto = 'BR'

with st.sidebar:
    # Logo / Título
    st.markdown('<div style="padding:10px 0; text-align:center;"><h2 style="color:#f05a22; font-family:Orbitron; font-size:18px;">MENU GESTOR</h2></div>', unsafe_allow_html=True)

    # Categoria Brasil
    render_category("📂 FUTEBOL BRASIL", "BR")
    if st.session_state.menu_aberto == "BR":
        c1, c2 = st.columns(2)
        with c1:
            render_sidebar_button("🔘", "SÉRIE A", "BRA_A", "BRASILEIRÃO A")
            render_sidebar_button("🔘", "SÉRIE C", "BRA_C", "BRASILEIRÃO C")
            render_sidebar_button("🏆", "COPA BR", "CDB", "COPA DO BRASIL")
        with c2:
            render_sidebar_button("🔘", "SÉRIE B", "BRA_B", "BRASILEIRÃO B")
            render_sidebar_button("🔘", "SÉRIE D", "BRA_D", "BRASILEIRÃO D")
            render_sidebar_button("☀️", "NORDESTE", "CNE", "COPA DO NORDESTE")

    # Categoria Europa
    render_category("🌍 ELITE EUROPA", "EU_L")
    if st.session_state.menu_aberto == "EU_L":
        c1, c2 = st.columns(2)
        with c1:
            render_sidebar_button("🏴󠁧󠁢󠁥󠁮󠁧󠁿", "PREMIER", "ENG_P", "PREMIER LEAGUE")
            render_sidebar_button("🇮🇹", "SERIE A", "ITA_A", "SERIE A TIM")
        with c2:
            render_sidebar_button("🇪🇸", "LA LIGA", "ESP_L", "LA LIGA")
            render_sidebar_button("🇩🇪", "BUNDES", "GER_B", "BUNDESLIGA")

    # Categoria Inter/Especiais
    render_category("⭐ UEFA / INTER", "UEFA")
    if st.session_state.menu_aberto == "UEFA":
        c1, c2 = st.columns(2)
        with c1: render_sidebar_button("🏆", "CHAMPIONS", "UCL", "UEFA CHAMPIONS LEAGUE")
        with c2: render_sidebar_button("🛡️", "EUROCOPA", "EURO_C", "EUROCOPA 2024")

# --- 6. CABEÇALHO E SELEÇÃO ---
st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
        <div style="color: #f05a22; font-family: 'Orbitron', sans-serif; font-size: 24px; font-weight: 900;">
            GESTOR IA <span style="color: #ffffff; font-size: 12px; opacity: 0.6;">PRO EDITION</span>
        </div>
    </div>
""", unsafe_allow_html=True)

times_lista = DIC_TIMES.get(st.session_state.liga_ativa, ["Selecione..."])

# Grid de seleção alinhado
container_select = st.container()
with container_select:
    col1, col2, col3 = st.columns([3, 3, 2.5])
    with col1: 
        t_casa = st.selectbox("MANDANTE", sorted(times_lista), label_visibility="visible")
    with col2: 
        t_fora = st.selectbox("VISITANTE", sorted([t for t in times_lista if t != t_casa]), label_visibility="visible")
    with col3: 
        st.markdown("<br>", unsafe_allow_html=True) # Alinha o botão com os selects
        executar = st.button("🔥 PROCESSAR ALGORITMO", use_container_width=True, type="primary")

# --- MENSAGEM DE ESPERA ---
if not executar:
    st.markdown(f"<div style='margin-top:50px; text-align:center; color:#444; font-family:Orbitron; border: 1px dashed #444; padding: 40px; border-radius:15px;'>AGUARDANDO CONFRONTO EM {st.session_state.nome_liga}...</div>", unsafe_allow_html=True)
else:
    st.success(f"Analisando {t_casa} vs {t_fora}...")
    # Aqui entraria sua engine de resultados...
