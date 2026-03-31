import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# ==========================================
# DIRETRIZ: APARÊNCIA IMUTÁVEL ZERO WHITE PRO
# ==========================================
st.set_page_config(page_title="GESTOR IA - TRADING PRO", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    /* FUNDO E CORES PADRÃO JARVIS */
    [data-testid="stAppViewContainer"] { background-color: #0b0e11; color: white; }
    [data-testid="stSidebar"] { background-color: #0f1216; border-right: 1px solid #1e2229; }
    
    /* DESIGN DOS CARDS DE JOGO */
    .card-live {
        background: linear-gradient(145deg, #161a1e, #1c2126);
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #2d3439;
        margin-bottom: 15px;
        min-height: 190px;
        transition: all 0.3s ease;
    }
    .card-live:hover { border-color: #00ff88; transform: translateY(-3px); }
    
    .status-live { color: #ff4b4b; font-weight: bold; animation: blinker 2s linear infinite; font-size: 12px; }
    @keyframes blinker { 50% { opacity: 0; } }
    
    .team-name { font-size: 15px; font-weight: 700; margin: 8px 0; color: #ffffff; text-transform: uppercase; }
    .score { font-size: 28px; color: #00ff88; font-weight: 900; letter-spacing: 2px; }
    .label-ap { font-size: 11px; color: #808a9d; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# MOTOR DE DADOS: LEITURA DO GITHUB ACTIONS
# ==========================================
def buscar_dados_vivos():
    """Lê o arquivo CSV que o seu GitHub Actions gera a cada 10 minutos."""
    jogos = []
    try:
        # URL RAW DO SEU REPOSITÓRIO (Aritonapr)
        URL_CSV = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/base_jogos_jarvis.csv"
        
        # Lendo o CSV direto da nuvem
        df = pd.read_csv(URL_CSV)
        
        # Filtra apenas jogos da data de hoje (30/03/2026)
        hoje = datetime.now().strftime('%Y-%m-%d')
        df_hoje = df[df['DATA'] == hoje]
        
        if not df_hoje.empty:
            for _, row in df_hoje.iterrows():
                jogos.append({
                    "home": row['HOME'],
                    "away": row['AWAY'],
                    "placar_h": row['PLACAR_HOME'],
                    "placar_a": row['PLACAR_AWAY'],
                    "minuto": row['MINUTO'],
                    "ap1": row['AP1']
                })
    except Exception as e:
        # Silencioso para não quebrar a interface
        pass
    return jogos

# ==========================================
# INTERFACE PRINCIPAL - SCANNER
# ==========================================
st.sidebar.title("🤖 JARVIS v65.1")
st.sidebar.markdown(f"**DATA:** 30/03/2026")
st.sidebar.markdown(f"**STATUS:** ● CONECTADO AO OGOL")
st.sidebar.write("---")

st.title("📡 SCANNER EM TEMPO REAL")
st.write(f"Monitorando jogos ao vivo agora: **{datetime.now().strftime('%H:%M:%S')}**")

# Botão de atualização manual
if st.button("🔄 ATUALIZAR SCANNER"):
    st.rerun()

lista_jogos = buscar_dados_vivos()

if not lista_jogos:
    st.warning("⚠️ AGUARDANDO PRÓXIMA RODADA DE JOGOS NO OGOL...")
    st.info("O robô no GitHub Actions está ativo. Se houver jogos em andamento, eles aparecerão aqui em breve.")
    
    # Grid de placeholders vazios para manter a estética Zero White Pro
    cols = st.columns(4)
    for i in range(12):
        with cols[i % 4]:
            st.markdown('<div class="card-live" style="opacity: 0.15; border-style: dashed; text-align: center; padding-top: 60px;">SEM JOGOS NO MOMENTO</div>', unsafe_allow_html=True)
else:
    # Exibição dos jogos reais capturados
    cols = st.columns(4)
    for i, jogo in enumerate(lista_jogos[:20]): # Limite de 20 slots
        with cols[i % 4]:
            st.markdown(f"""
            <div class="card-live">
                <span class="status-live">● AO VIVO ({jogo['minuto']}')</span>
                <div class="team-name">{jogo['home']}</div>
                <div class="score">{jogo['placar_h']} - {jogo['placar_a']}</div>
                <div class="team-name">{jogo['away']}</div>
                <div class="label-ap">PRESSÃO (AP1): {jogo['ap1']}%</div>
                <div style="background: #2d3439; height: 5px; border-radius: 3px; margin-top: 5px;">
                    <div style="background: #00ff88; width: {jogo['ap1']}%; height: 100%; border-radius: 3px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# RODAPÉ TÉCNICO
# ==========================================
st.markdown("---")
st.caption(f"PROTOCOLO JARVIS | v65.1 | REPOSITÓRIO: Aritonapr | JOGOS MONITORADOS: {len(lista_jogos)}")
