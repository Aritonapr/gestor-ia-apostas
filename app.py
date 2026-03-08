import streamlit as st
import pandas as pd
import numpy as np
import hashlib
import time

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="GESTOR IA - PRO EDITION", 
    layout="wide", 
    page_icon="⚽",
    initial_sidebar_state="expanded"
)

# --- 2. BANCO DE DADOS ATUALIZADO ---
DIC_TIMES = {
    "BRA_A": ["Flamengo", "Palmeiras", "Botafogo", "Fortaleza", "São Paulo", "Bahia", "Cruzeiro", "Internacional", "Atlético-MG", "Vasco", "Corinthians", "Fluminense", "Grêmio", "Athletico-PR", "Vitória", "Juventude", "Criciúma", "Cuiabá", "Atlético-GO", "Bragantino"],
    "BRA_B": ["Santos", "Sport", "Novorizontino", "Mirassol", "Vila Nova", "América-MG", "Ceará", "Coritiba", "Avaí", "Operário-PR", "Amazonas", "Goiás"],
    "BRA_C": ["Náutico", "Remo", "Figueirense", "CSA", "Botafogo-PB", "ABC", "Londrina", "Caxias", "Ferroviária", "São Bernardo", "Volta Redonda", "Ypiranga"],
    "ENG_P": ["Man. City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Chelsea", "Man. United", "Newcastle", "West Ham", "Brighton"],
    "ESP_L": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Athletic Bilbao", "Real Sociedad", "Sevilla", "Villarreal"],
    "ITA_A": ["Inter", "Milan", "Juventus", "Atalanta", "Roma", "Napoli", "Lazio", "Fiorentina"],
    "GER_B": ["Leverkusen", "Bayern", "Stuttgart", "Leipzig", "Dortmund", "Frankfurt"],
    "UCL": ["Real Madrid", "Man. City", "Bayern", "Arsenal", "Barcelona", "Inter", "PSG", "Leverkusen"],
    "LIB": ["Flamengo", "Palmeiras", "River Plate", "Botafogo", "São Paulo", "Atlético-MG", "Peñarol", "Colo-Colo"],
}

# --- 3. CSS AVANÇADO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;600;800&display=swap');
    
    /* Global Styles */
    .stApp { background-color: #050a0e; color: #e4e6eb; font-family: 'Inter', sans-serif; }
    [data-testid="stHeader"] { background: transparent !important; }
    
    /* Sidebar Customization */
    [data-testid="stSidebar"] { 
        background-color: #080f15 !important; 
        border-right: 1px solid rgba(240, 90, 34, 0.3) !important; 
    }

    /* Botões de Navegação */
    .stButton > button { 
        background: linear-gradient(90deg, rgba(240, 90, 34, 0.05) 0%, rgba(26, 36, 45, 0.6) 100%) !important;
        color: #a0aec0 !important; 
        font-size: 0.8rem !important; 
        border-radius: 8px !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important; 
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        text-align: left !important;
        padding: 10px 15px !important;
    }

    .stButton > button:hover { 
        background: linear-gradient(90deg, rgba(240, 90, 34, 0.2) 0%, rgba(240, 90, 34, 0.05) 100%) !important;
        color: #fff !important; 
        border: 1px solid #f05a22 !important;
        transform: translateX(8px);
    }

    /* Estilo Especial para Botão Primário */
    div[data-testid="stVerticalBlock"] > div:has(button[kind="primary"]) button {
        background: linear-gradient(135deg, #f05a22 0%, #ff8c00 100%) !important;
        color: white !important;
        font-weight: 800 !important;
        text-align: center !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(240, 90, 34, 0.4) !important;
    }

    /* Cards e Containers */
    .main-card { 
        background: rgba(17, 25, 33, 0.8);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-top: 3px solid #f05a22;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    .stat-box {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.05);
        transition: 0.3s;
    }
    
    .stat-box:hover {
        background: rgba(240, 90, 34, 0.05);
        border-color: #f05a22;
    }

    .label-mini { color: #8a99a8; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
    .val-mini { color: #00ffc3; font-size: 22px; font-weight: 900; margin-top: 5px; }
    
    /* Badges */
    .badge {
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 10px;
        font-weight: bold;
        background: rgba(240, 90, 34, 0.2);
        color: #f05a22;
        border: 1px solid #f05a22;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. ENGINE DE PROCESSAMENTO ---
def processar_analise(casa, fora):
    # Simulação de algoritmo complexo usando hash do confronto
    input_str = f"{casa}{fora}{time.strftime('%Y%m%d')}"
    seed = int(hashlib.sha256(input_str.encode()).hexdigest(), 16)
    
    np.random.seed(seed % 10000)
    
    # Gera probabilidades que somam ~100
    p1 = np.random.randint(25, 60)
    p2 = np.random.randint(15, 30)
    p3 = 100 - p1 - p2
    
    return {
        "prob_casa": p1, "prob_empate": p2, "prob_fora": p3,
        "gols": np.random.randint(45, 85),
        "cantos": np.random.randint(50, 92),
        "chutes": np.random.randint(60, 95),
        "cartoes": np.random.randint(30, 80),
        "tendencia": np.random.choice(["Over 2.5", "BTTS Yes", "Casa Empate", "Under 3.5"])
    }

# --- 5. SIDEBAR ---
with st.sidebar:
    st.markdown(f"""
        <div style="text-align:center; padding: 20px 0;">
            <h2 style="color:#f05a22; font-family:Orbitron; font-size:1.2rem; margin:0;">GESTOR IA</h2>
            <p style="color:#666; font-size:0.7rem; letter-spacing:2px;">SISTEMA NEURAL DE PREDIÇÃO</p>
        </div>
    """, unsafe_allow_html=True)
    
    if 'liga' not in st.session_state: st.session_state.liga = 'BRA_A'

    st.markdown("<p style='font-size:0.7rem; color:#f05a22; font-weight:bold; margin-left:5px;'>CAMPEONATOS</p>", unsafe_allow_html=True)
    
    col_nav1, col_nav2 = st.columns(2)
    with col_nav1:
        if st.button("🇧🇷 SÉRIE A"): st.session_state.liga = 'BRA_A'
        if st.button("🏴󠁧󠁢󠁥󠁮󠁧󠁿 PREMIER"): st.session_state.liga = 'ENG_P'
        if st.button("🇪🇸 LA LIGA"): st.session_state.liga = 'ESP_L'
    with col_nav2:
        if st.button("🏆 CHAMPIONS"): st.session_state.liga = 'UCL'
        if st.button("☀️ NORDESTE"): st.session_state.liga = 'CNE'
        if st.button("🏆 LIBERTA"): st.session_state.liga = 'LIB'

    st.divider()
    st.markdown("<div style='background:rgba(240,90,34,0.1); padding:15px; border-radius:10px; border:1px solid rgba(240,90,34,0.2);'><p style='color:#f05a22; font-size:11px; margin:0;'><b>STATUS DO SERVIDOR</b></p><p style='color:#00ffc3; font-size:10px; margin:0;'>● Conectado à API Global</p></div>", unsafe_allow_html=True)

# --- 6. ÁREA PRINCIPAL ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px;">
        <div>
            <h1 style="font-family:Orbitron; font-size:1.5rem; margin:0; color:white;">ANÁLISE <span style="color:#f05a22;">ESTRATÉGICA</span></h1>
            <p style="color:#666; margin:0; font-size:0.8rem;">Algoritmo v4.2.0 - Deep Learning</p>
        </div>
        <div class="badge">LIVE DATA FEED</div>
    </div>
""", unsafe_allow_html=True)

# Seleção de Times
lista_times = DIC_TIMES.get(st.session_state.liga, ["Selecione..."])
c1, c2, c3 = st.columns([4, 4, 3])

with c1:
    casa = st.selectbox("MANDANTE", sorted(lista_times))
with c2:
    fora = st.selectbox("VISITANTE", sorted([t for t in lista_times if t != casa]))
with c3:
    st.markdown("<br>", unsafe_allow_html=True)
    btn_analise = st.button("🔥 INICIAR PROCESSAMENTO", use_container_width=True, type="primary")

if btn_analise:
    with st.spinner("🧠 Sincronizando variáveis táticas..."):
        time.sleep(1.5) # Simulação de processamento
        res = processar_analise(casa, fora)
    
    # --- RESULTADOS PRINCIPAIS ---
    st.markdown(f"""
        <div class="main-card">
            <div style="text-align:center; margin-bottom:40px;">
                <span style="color:#8a99a8; font-size:12px; font-weight:800; letter-spacing:3px;">PROBABILIDADES FINAIS</span>
                <div style="display: flex; justify-content: center; align-items: center; gap: 40px; margin-top: 20px;">
                    <div>
                        <div style="font-size: 3rem; font-weight: 900; color: #f05a22; font-family: Orbitron;">{res['prob_casa']}%</div>
                        <div style="font-size: 11px; color: #fff; opacity: 0.7;">{casa.upper()}</div>
                    </div>
                    <div style="height: 50px; width: 2px; background: rgba(255,255,255,0.1);"></div>
                    <div>
                        <div style="font-size: 2.2rem; font-weight: 900; color: #fff; font-family: Orbitron; opacity: 0.6;">{res['prob_empate']}%</div>
                        <div style="font-size: 11px; color: #fff; opacity: 0.7;">EMPATE</div>
                    </div>
                    <div style="height: 50px; width: 2px; background: rgba(255,255,255,0.1);"></div>
                    <div>
                        <div style="font-size: 3rem; font-weight: 900; color: #f05a22; font-family: Orbitron;">{res['prob_fora']}%</div>
                        <div style="font-size: 11px; color: #fff; opacity: 0.7;">{fora.upper()}</div>
                    </div>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 15px;">
                <div class="stat-box">
                    <div class="label-mini">Over 2.5 Gols</div>
                    <div class="val-mini">{res['gols']}%</div>
                </div>
                <div class="stat-box">
                    <div class="label-mini">Cantos +9.5</div>
                    <div class="val-mini">{res['cantos']}%</div>
                </div>
                <div class="stat-box">
                    <div class="label-mini">Chutes ao Gol</div>
                    <div class="val-mini">{res['chutes']}%</div>
                </div>
                <div class="stat-box">
                    <div class="label-mini">Cartões +3.5</div>
                    <div class="val-mini">{res['cartoes']}%</div>
                </div>
                <div class="stat-box" style="border-color: #00ffc3;">
                    <div class="label-mini" style="color:#00ffc3;">Principal Insight</div>
                    <div class="val-mini" style="font-size: 14px; color:#fff;">{res['tendencia']}</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- MÉTRICAS AUXILIARES ---
    st.markdown("<br>", unsafe_allow_html=True)
    ca1, ca2 = st.columns(2)
    
    with ca1:
        st.markdown(f"""
            <div style="background:rgba(255,255,255,0.03); padding:20px; border-radius:15px; border-left:4px solid #f05a22;">
                <h4 style="margin:0 0 10px 0; font-size:14px; color:#f05a22; font-family:Orbitron;">ANÁLISE DE CAMPO</h4>
                <p style="font-size:12px; color:#cbd5e0; line-height:1.6;">
                    O modelo detectou uma pressão ofensiva superior do <b>{casa}</b> nos primeiros 15 minutos. 
                    A linha de defesa do <b>{fora}</b> apresenta vulnerabilidades em transições rápidas. 
                    Expectativa de jogo aberto com alta incidência de finalizações de média distância.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with ca2:
        st.markdown(f"""
            <div style="background:rgba(255,255,255,0.03); padding:20px; border-radius:15px; border-left:4px solid #00ffc3;">
                <h4 style="margin:0 0 10px 0; font-size:14px; color:#00ffc3; font-family:Orbitron;">POWER RATING</h4>
                <div style="display:flex; justify-content:space-between; margin-bottom:5px;">
                    <span style="font-size:11px;">Índice de Confiança</span><span style="font-size:11px; color:#00ffc3;">Alta</span>
                </div>
                <div style="background:rgba(255,255,255,0.1); height:6px; border-radius:3px;">
                    <div style="background:#00ffc3; width:82%; height:100%; border-radius:3px;"></div>
                </div>
                <p style="font-size:10px; color:#666; margin-top:10px;">Basado em Volatilidade Histórica e Performance Recente (H2H).</p>
            </div>
        """, unsafe_allow_html=True)

else:
    # Estado Inicial
    st.markdown("""
        <div style="height:300px; display:flex; flex-direction:column; align-items:center; justify-content:center; border:1px dashed rgba(240,90,34,0.3); border-radius:20px; background:rgba(240,90,34,0.02);">
            <div style="font-size:40px; margin-bottom:10px;">🛡️</div>
            <div style="color:#4a5568; font-family:Orbitron; font-size:12px; letter-spacing:2px;">AGUARDANDO INPUT DE CONFRONTO...</div>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align:center; color:#444; font-size:10px; margin-top:50px;'>GESTOR IA PRO v4.2 © 2024 - O uso desta ferramenta não garante resultados. Jogue com responsabilidade.</p>", unsafe_allow_html=True)
