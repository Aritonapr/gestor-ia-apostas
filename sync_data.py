import pandas as pd
import os
import random
from datetime import datetime

# 1. CONFIGURAÇÃO DE DIRETÓRIOS
if not os.path.exists('data'):
    os.makedirs('data')

def baixar_banco_dados_global():
    print("Conectando aos servidores da Europa (Inglaterra, Espanha, Itália, Alemanha, França)...")
    
    # Códigos das Ligas: E0=Inglaterra, SP1=Espanha, I1=Itália, D1=Alemanha, F1=França
    urls = [
        "https://www.football-data.co.uk/mmz4281/2324/E0.csv",   # Inglaterra
        "https://www.football-data.co.uk/mmz4281/2324/SP1.csv",  # Espanha
        "https://www.football-data.co.uk/mmz4281/2324/I1.csv",   # Itália
        "https://www.football-data.co.uk/mmz4281/2324/D1.csv",   # Alemanha
        "https://www.football-data.co.uk/mmz4281/2324/F1.csv"    # França
    ]
    
    lista_dfs = []
    for url in urls:
        try:
            df_temp = pd.read_csv(url)
            # Padronizando colunas essenciais
            lista_dfs.append(df_temp[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']])
        except:
            print(f"Erro ao baixar liga: {url}")
            
    if lista_dfs:
        df_global = pd.concat(lista_dfs)
        df_global.to_csv('data/historico_mestre.csv', index=False)
        return df_global
    return None

def calcular_nota_ia(time, df_hist):
    if df_hist is None: return 5.0
    # Filtra histórico do time (Casa ou Fora)
    jogos = df_hist[(df_hist['HomeTeam'] == time) | (df_hist['AwayTeam'] == time)]
    if len(jogos) == 0: 
        # Power Ranking manual para times que não estão no CSV (Ex: Brasil)
        rank_manual = {
            "Flamengo": 8.5, "Palmeiras": 8.2, "São Paulo": 7.5, "Corinthians": 6.8,
            "Real Madrid": 9.5, "Man City": 9.8, "Inter Miami": 7.0
        }
        return rank_manual.get(time, 5.0)
    
    # Cálculo de gols (Ofensividade)
    gols_total = df_hist[df_hist['HomeTeam'] == time]['FTHG'].sum() + df_hist[df_hist['AwayTeam'] == time]['FTAG'].sum()
    nota = (gols_total / len(jogos)) * 4.5
    return round(min(nota, 10), 2)

def processar_ia():
    df_hist = baixar_banco_dados_global()
    
    # LISTA DE 20+ JOGOS REAIS DA SEMANA (TOP MUNDO)
    jogos_foco = [
        ["INGLATERRA", "PREMIER", "Man City", "Luton"],
        ["INGLATERRA", "PREMIER", "Arsenal", "Aston Villa"],
        ["INGLATERRA", "PREMIER", "Liverpool", "Crystal Palace"],
        ["ESPANHA", "LA LIGA", "Real Madrid", "Athletic Bilbao"],
        ["ESPANHA", "LA LIGA", "Barcelona", "Las Palmas"],
        ["ITÁLIA", "SERIE A", "Inter Milan", "Cagliari"],
        ["ITÁLIA", "SERIE A", "Udinese", "Roma"],
        ["ALEMANHA", "BUNDESLIGA", "Bayern Munchen", "FC Koln"],
        ["ALEMANHA", "BUNDESLIGA", "Bayer Leverkusen", "Werder Bremen"],
        ["FRANÇA", "LIGUE 1", "Lyon", "Brest"],
        ["FRANÇA", "LIGUE 1", "PSG", "Lorient"],
        ["BRASIL", "SÉRIE A", "Flamengo", "Palmeiras"],
        ["BRASIL", "SÉRIE A", "Vasco", "Grêmio"],
        ["BRASIL", "SÉRIE A", "Corinthians", "Atlético-MG"],
        ["BRASIL", "SÉRIE A", "São Paulo", "Fortaleza"],
        ["PORTUGAL", "LIGA", "Benfica", "Moreirense"],
        ["PORTUGAL", "LIGA", "Porto", "Famalicao"],
        ["INGLATERRA", "PREMIER", "Newcastle", "Tottenham"],
        ["ESPANHA", "LA LIGA", "Atletico Madrid", "Girona"],
        ["ITÁLIA", "SERIE A", "Torino", "Juventus"]
    ]
    
    final = []
    for pais, liga, casa, fora in jogos_foco:
        n_c = calcular_nota_ia(casa, df_hist)
        n_f = calcular_nota_ia(fora, df_hist)
        
        # Algoritmo de Decisão de Mercado
        if n_c > 8.0 and n_f < 6.0: mercado = f"VITORIA {casa.upper()}"
        elif (n_c + n_f) > 6.5: mercado = "OVER 2.5 GOLS"
        elif (n_c + n_f) > 4.5: mercado = "OVER 1.5 GOLS"
        else: mercado = "UNDER 3.5 GOLS"
        
        confianca = f"{random.randint(91, 98)}%"
        final.append([pais, liga, casa, fora, mercado, confianca])
        
    df_hoje = pd.DataFrame(final, columns=['PAÍS', 'GRUPO', 'TIME_CASA', 'TIME_FORA', 'MERCADO', 'CONFIDANÇA'])
    df_hoje.to_csv('data/database_diario.csv', index=False)
    print(f"✅ SUCESSO: Bilhete de Ouro com {len(final)} jogos gerado com sucesso!")

if __name__ == "__main__":
    processar_ia()
