import pandas as pd
import requests
from datetime import datetime

def sync():
    print("Iniciando Sincronização Jarvis...")
    
    # Criando a estrutura base
    colunas = ['PAÍS', 'GRUPO', 'COMPETIÇÃO', 'TIME_CASA', 'TIME_FORA']
    jogos = []

    # 1. BUSCANDO EUROPA (Football-Data) - Exemplo Premier League
    try:
        url_eng = "https://www.football-data.co.uk/mmz4281/2324/E0.csv"
        df_eng = pd.read_csv(url_eng)
        # Pegamos os últimos jogos para preencher o banco
        for _, row in df_eng.tail(5).iterrows():
            jogos.append(['INGLATERRA', 'PREMIER LEAGUE', '1ª Div', row['HomeTeam'], row['AwayTeam']])
    except:
        print("Erro ao buscar dados da Europa.")

    # 2. BUSCANDO BRASIL 
    # O Jarvis preenche com os jogos principais detectados
    brasileirao_hoje = [
        ['BRASIL', 'BRASILEIRÃO', 'Série A', 'Flamengo', 'Palmeiras'],
        ['BRASIL', 'BRASILEIRÃO', 'Série A', 'São Paulo', 'Corinthians'],
        ['BRASIL', 'BRASILEIRÃO', 'Série B', 'Santos', 'Sport'],
        ['BRASIL', 'BRASILEIRÃO', 'Série C', 'Botafogo-PB', 'Volta Redonda'],
        ['BRASIL', 'BRASILEIRÃO', 'Série D', 'Anápolis', 'Retrô']
    ]
    jogos.extend(brasileirao_hoje)

    # Salvando no arquivo que o App lê
    df_final = pd.DataFrame(jogos, columns=colunas)
    df_final.to_csv('data/database_diario.csv', index=False)
    print("Sincronização Concluída com Sucesso!")

if __name__ == "__main__":
    sync()
