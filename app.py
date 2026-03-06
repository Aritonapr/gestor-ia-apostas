import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson
import requests

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="GESTOR IA - BRASILEIRÃO & ELITE", layout="wide", page_icon="🇧🇷")

# --- ESTILO VISUAL ---
st.markdown("""
    <style>
    .main { background-color: #0b1218; color: #e4e6eb; }
    div[data-testid="stSidebar"] { background-color: #1a242d; }
    .stButton>button { background: linear-gradient(90deg, #f05a22 0%, #ff8235 100%); color: white; border: none; padding: 12px 30px; border-radius: 25px; font-weight: bold; width: 100%; transition: 0.3s; }
    .card-jogo { background-color: #1a242d; padding: 25px; border-radius: 15px; border-top: 4px solid #f05a22; margin-bottom: 20px; box-shadow: 0 8px 16px rgba(0,0,0,0.4); }
    .metric-value { color: #f05a22; font-size: 24px; font-weight: bold; }
    .success-text { color: #28a745; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNÇÃO TELEGRAM ---
def enviar_telegram(mensagem, token, chat_id):
    if token and chat_id:
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={mensagem}"
        requests.get(url)

# --- ENGINE DE DADOS (BRASILEIRÃO + EUROPA) ---
@st.cache_data(ttl=3600)
def get_data(league_code):
    # Ligas Europeias
    if league_code != 'BRA':
        url = f"https://www.football-data.co.uk/mmz4281/2425/{league_code}.csv"
    else:
        # Fonte para Brasileirão Série A (Repositório de dados atualizados)
        url = "https://raw.githubusercontent.com/adaoduque/brasileirao-dataset/master/data/brasileirao_serie_a.csv"
    
    try:
        df = pd.read_csv(url)
        # Padronização para o Brasileirão (Ajustando nomes de colunas se necessário)
        if league_code == 'BRA':
            df = df.rename(columns={'home_team': 'HomeTeam', 'away_team': 'AwayTeam', 'home_score': 'FTHG', 'away_score': 'FTAG', 'result': 'FTR'})
        return df
    except:
        return pd.DataFrame()

def calcular_probabilidades(home, away, df):
    h_matches = df[df['HomeTeam'] == home].tail(10)
    a_matches = df[df['AwayTeam'] == away].tail(10)
    if len(h_matches) == 0 or len(a_matches) == 0: return None
    
    xg_h = h_matches['FTHG'].mean()
    xg_a = a_matches['FTAG'].mean()
    
    prob_h_list = poisson.pmf(np.arange(0, 5), xg_h)
    prob_a_list = poisson.pmf(np.arange(0, 5), xg_a)
    matrix = np.outer(prob_h_list, prob_a_list)
    
    win_h = np.sum(np.triu(matrix, 1)) * 100
    draw = np.trace(matrix) * 100
    win_a = np.sum(np.tril(matrix, -1)) * 100
    over25 = (1 - (matrix[0,0] + matrix[0,1] + matrix[0,2] + matrix[1,0] + matrix[1,1] + matrix[2,0])) * 100
    
    return {
        'win_h': win_h, 'draw': draw, 'win_a': win_a, 'over25': over25,
        'odd_justa_h': 100/win_h if win_h > 0 else 0, 'xg_h': xg_h, 'xg_a': xg_a
    }

# --- SIDEBAR: CONFIGURAÇÃO TELEGRAM ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Betano_logo.svg/1200px-Betano_logo.svg.png", width=180)
st.sidebar.header("🤖 BOT TELEGRAM")
tg_token = st.sidebar.text_input("Bot Token", type="password")
tg_id = st.sidebar.text_input("Seu Chat ID")

st.sidebar.markdown("---")
liga_nome = st.sidebar.selectbox("🏆 SELECIONE A LIGA", 
    ['Brasileirão Série A', 'Premier League', 'La Liga', 'Serie A', 'Bundesliga'])

ligas_map = {
    'Brasileirão Série A': 'BRA', 'Premier League':'E0', 'La Liga':'SP1', 
    'Serie A':'I1', 'Bundesliga':'D1'
}

df = get_data(ligas_map[liga_nome])

if not df.empty:
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 ANALISADOR", "🔍 SCANNER", "📈 HISTÓRICO/BACKTEST", "📋 RELATÓRIO"])

    with tab1:
        teams = sorted(df['HomeTeam'].unique())
        c1, c2 = st.columns(2)
        t_home = c1.selectbox("Casa", teams)
        t_away = c2.selectbox("Fora", teams)
        
        if st.button("GERAR ANÁLISE"):
            res = calcular_probabilidades(t_home, t_away, df)
            if res:
                st.markdown(f"""
                <div class="card-jogo">
                    <h3 style='text-align:center;'>{t_home} {res['xg_h']:.0f} x {res['xg_a']:.0f} {t_away}</h3>
                    <div style='display:flex; justify-content:space-around; text-align:center;'>
                        <div><p>Casa</p><p class='metric-value'>{res['win_h']:.1f}%</p></div>
                        <div><p>Empate</p><p class='metric-value'>{res['draw']:.1f}%</p></div>
                        <div><p>Fora</p><p class='metric-value'>{res['win_a']:.1f}%</p></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Alerta Telegram Manual
                if st.button("Enviar esta análise para o Telegram"):
                    msg = f"⚽ ANÁLISE IA: {t_home} vs {t_away}\n🏠 Casa: {res['win_h']:.1f}%\n📊 Over 2.5: {res['over25']:.1f}%\n💰 Odd Justa: {res['odd_justa_h']:.2f}"
                    enviar_telegram(msg, tg_token, tg_id)
                    st.toast("Enviado para o Telegram!")

    with tab2:
        st.header("🔍 Scanner de Valor (EV+)")
        if st.button("VARRE LIGA INTEIRA"):
            oportunidades = []
            for h in teams[:10]:
                for a in teams[10:20]:
                    if h != a:
                        r = calcular_probabilidades(h, a, df)
                        if r and r['win_h'] > 70:
                            oportunidades.append(f"⚠️ VALOR: {h} para vencer ({r['win_h']:.1f}%)")
                            st.write(f"✅ Encontrado: {h} vs {a} - Prob: {r['win_h']:.1f}%")
            
            if oportunidades and tg_token:
                enviar_telegram("\n".join(oportunidades), tg_token, tg_id)

    with tab3:
        st.header("📈 Backtest: A IA é confiável?")
        st.write("Analisando os últimos 20 jogos e comparando com o que a IA previu:")
        ultimos_jogos = df.tail(20)
        acertos = 0
        
        for idx, row in ultimos_jogos.iterrows():
            r = calcular_probabilidades(row['HomeTeam'], row['AwayTeam'], df.head(idx))
            if r:
                predicao = "H" if r['win_h'] > r['win_a'] and r['win_h'] > r['draw'] else "A"
                if predicao == row['FTR']:
                    acertos += 1
                    status = "✅ ACERTO"
                else:
                    status = "❌ ERRO"
                st.write(f"{row['HomeTeam']} vs {row['AwayTeam']} | Previsão IA: {predicao} | Real: {row['FTR']} | {status}")
        
        st.metric("Taxa de Acerto (Últimos 20 jogos)", f"{(acertos/20)*100}%")

    with tab4:
        st.header("📋 Relatório")
        st.write("Dados atualizados com sucesso para:", liga_nome)
        st.dataframe(df.tail(5))

else:
    st.error("Erro ao carregar dados. Verifique a conexão.")
