import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import poisson
import requests

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="GESTOR IA - BRASILEIRÃO & ELITE", layout="wide", page_icon="🇧🇷")

# --- ESTILO VISUAL BETANO DARK ---
st.markdown("""
    <style>
    .main { background-color: #0b1218; color: #e4e6eb; }
    div[data-testid="stSidebar"] { background-color: #1a242d; }
    .stButton>button { background: linear-gradient(90deg, #f05a22 0%, #ff8235 100%); color: white; border: none; padding: 12px 30px; border-radius: 25px; font-weight: bold; width: 100%; }
    .card-jogo { background-color: #1a242d; padding: 20px; border-radius: 15px; border-top: 4px solid #f05a22; margin-bottom: 20px; }
    .metric-value { color: #f05a22; font-size: 24px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNÇÃO TELEGRAM ---
def enviar_telegram(mensagem, token, chat_id):
    if token and chat_id:
        try:
            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={mensagem}"
            requests.get(url)
        except:
            pass

# --- ENGINE DE DADOS ---
@st.cache_data(ttl=3600)
def get_data(league_code):
    if league_code == 'BRA':
        # Fonte alternativa e mais estável para o Brasileirão
        url = "https://raw.githubusercontent.com/automacaobrasil/dataset-brasileirao/main/brasileirao_serie_a.csv"
    else:
        url = f"https://www.football-data.co.uk/mmz4281/2425/{league_code}.csv"
    
    try:
        df = pd.read_csv(url)
        # Padronização de Colunas (Brasil vs Europa)
        if league_code == 'BRA':
            # Se for Brasil, traduzimos os nomes das colunas
            mapping = {
                'mandante': 'HomeTeam', 'visitante': 'AwayTeam', 
                'mandante_placar': 'FTHG', 'visitante_placar': 'FTAG',
                'vencedor': 'FTR'
            }
            df = df.rename(columns=mapping)
        
        # Garante que as colunas de gols sejam números
        df['FTHG'] = pd.to_numeric(df['FTHG'], errors='coerce')
        df['FTAG'] = pd.to_numeric(df['FTAG'], errors='coerce')
        return df.dropna(subset=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()

def calcular_probabilidades(home, away, df):
    # Filtra os últimos 10 jogos de cada time
    h_matches = df[df['HomeTeam'] == home].tail(10)
    a_matches = df[df['AwayTeam'] == away].tail(10)
    
    if len(h_matches) == 0 or len(a_matches) == 0:
        return None
    
    xg_h = h_matches['FTHG'].mean()
    xg_a = a_matches['FTAG'].mean()
    
    # Poisson
    prob_h_list = poisson.pmf(np.arange(0, 6), xg_h)
    prob_a_list = poisson.pmf(np.arange(0, 6), xg_a)
    matrix = np.outer(prob_h_list, prob_a_list)
    
    win_h = np.sum(np.triu(matrix, 1)) * 100
    draw = np.trace(matrix) * 100
    win_a = np.sum(np.tril(matrix, -1)) * 100
    over25 = (1 - (matrix[0,0] + matrix[0,1] + matrix[0,2] + matrix[1,0] + matrix[1,1] + matrix[2,0])) * 100
    
    return {
        'win_h': win_h, 'draw': draw, 'win_a': win_a, 'over25': over25,
        'odd_justa_h': 100/win_h if win_h > 0 else 0, 'xg_h': xg_h, 'xg_a': xg_a
    }

# --- SIDEBAR ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Betano_logo.svg/1200px-Betano_logo.svg.png", width=180)
st.sidebar.header("🤖 BOT TELEGRAM")
tg_token = st.sidebar.text_input("Bot Token", type="password", help="Pegue no @BotFather")
tg_id = st.sidebar.text_input("Seu Chat ID", help="Pegue no @userinfobot")

st.sidebar.markdown("---")
liga_nome = st.sidebar.selectbox("🏆 SELECIONE A LIGA", 
    ['Brasileirão Série A', 'Premier League', 'La Liga', 'Serie A', 'Bundesliga'])

ligas_map = {
    'Brasileirão Série A': 'BRA', 'Premier League':'E0', 
    'La Liga':'SP1', 'Serie A':'I1', 'Bundesliga':'D1'
}

# --- CARREGAMENTO ---
df = get_data(ligas_map[liga_nome])

if not df.empty:
    tab1, tab2, tab3 = st.tabs(["🎯 ANALISADOR", "🔍 SCANNER DE VALOR", "📈 BACKTEST"])

    with tab1:
        teams = sorted(df['HomeTeam'].unique())
        c1, c2 = st.columns(2)
        t_home = c1.selectbox("Time da Casa", teams)
        t_away = c2.selectbox("Time de Fora", teams)
        
        if st.button("GERAR ANÁLISE"):
            res = calcular_probabilidades(t_home, t_away, df)
            if res:
                st.markdown(f"""
                <div class="card-jogo">
                    <h3 style='text-align:center;'>{t_home} vs {t_away}</h3>
                    <div style='display:flex; justify-content:space-around; text-align:center;'>
                        <div><p>Casa</p><p class='metric-value'>{res['win_h']:.1f}%</p></div>
                        <div><p>Empate</p><p class='metric-value'>{res['draw']:.1f}%</p></div>
                        <div><p>Fora</p><p class='metric-value'>{res['win_a']:.1f}%</p></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.write(f"📊 **Probabilidade Over 2.5 Gols:** {res['over25']:.1f}%")
                st.write(f"💰 **Odd Justa (Casa):** {res['odd_justa_h']:.2f}")

                if tg_token and tg_id:
                    if st.button("Enviar para o Telegram"):
                        msg = f"⚽ IA: {t_home} vs {t_away}\n🏠 Vit: {res['win_h']:.1f}%\n📊 Over 2.5: {res['over25']:.1f}%"
                        enviar_telegram(msg, tg_token, tg_id)
                        st.success("Mensagem enviada!")

    with tab2:
        st.header("🔎 Scanner de Valor (Top 10)")
        if st.button("VARRE LIGA INTEIRA"):
            with st.spinner("Analisando combinações..."):
                encontrados = []
                for h in teams[:10]: # Limite para não travar
                    for a in teams:
                        if h != a:
                            r = calcular_probabilidades(h, a, df)
                            if r and r['win_h'] > 70:
                                encontrados.append([h, a, f"{r['win_h']:.1f}%", f"{r['odd_justa_h']:.2f}"])
                
                if encontrados:
                    scan_df = pd.DataFrame(encontrados, columns=['Casa', 'Fora', 'Prob. Casa', 'Odd Justa'])
                    st.table(scan_df)
                else:
                    st.write("Nenhuma oportunidade óbvia encontrada agora.")

    with tab3:
        st.header("📈 Backtest (Últimos 10 Jogos)")
        ultimos = df.tail(10)
        acertos = 0
        for _, row in ultimos.iterrows():
            r = calcular_probabilidades(row['HomeTeam'], row['AwayTeam'], df.head(_))
            if r:
                # Simplificação: se Prob Casa > 50% e Casa ganhou, é acerto.
                previsao = "H" if r['win_h'] > 50 else ("A" if r['win_a'] > 50 else "D")
                real = row['FTR']
                if previsao == real or (previsao == "H" and row['FTHG'] > row['FTAG']):
                    acertos += 1
        st.metric("Taxa de Assertividade IA", f"{(acertos/10)*100}%")

else:
    st.warning("Selecione uma liga para começar.")
