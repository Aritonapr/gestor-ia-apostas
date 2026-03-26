import pandas as pd
import os
import random
from datetime import datetime

# CONFIGURAÇÃO DE DIRETÓRIO
if not os.path.exists('data'):
    os.makedirs('data')

# 1. BASE DE DADOS DE TENDÊNCIAS POR LIGA (HISTÓRICO SIMULADO)
# Isso substitui a leitura de 5 temporadas enquanto você não tem o CSV grande.
stats_ligas = {
    "PREMIER": {"media_gols": 2.85, "home_win": 45, "corners_avg": 10.5},
    "SÉRIE A": {"media_gols": 2.40, "home_win": 48, "corners_avg": 8.5},
    "LA LIGA": {"media_gols": 2.55, "home_win": 42, "corners_avg": 9.0},
    "CHAMPIONS": {"media_gols": 3.10, "home_win": 40, "corners_avg": 11.0},
    "BUNDESLIGA": {"media_gols": 3.20, "home_win": 43, "corners_avg": 10.0},
}

# 2. POWER RANKING ATUALIZADO
power_ranking = {
    "Man City": {"forca": 9.8, "over_tendency": 0.9},
    "Arsenal": {"forca": 9.2, "over_tendency": 0.8},
    "Liverpool": {"forca": 9.5, "over_tendency": 0.85},
    "Real Madrid": {"forca": 9.6, "over_tendency": 0.8},
    "Bayern Munchen": {"forca": 9.4, "over_tendency": 0.95},
    "Flamengo": {"forca": 8.8, "over_tendency": 0.75},
    "Palmeiras": {"forca": 8.5, "over_tendency": 0.6},
    "Luton": {"forca": 4.0, "over_tendency": 0.8},
    "Vasco": {"forca": 5.5, "over_tendency": 0.4},
}

def calcular_palpite_ia(casa, fora, liga):
    # Pega os dados ou usa um padrão
    c = power_ranking.get(casa, {"forca": 5.0, "over_tendency": 0.5})
    f = power_ranking.get(fora, {"forca": 5.0, "over_tendency": 0.5})
    l = stats_ligas.get(liga, {"media_gols": 2.5, "corners_avg": 9.0})
    
    # Lógica de Veredito
    score_casa = c['forca'] + 1.5 # +1.5 pelo fator casa
    score_fora = f['forca']
    
    # 1. Decisão de Vencedor
    if score_casa > score_fora + 2.5:
        return f"VITORIA {casa.upper()}", random.randint(88, 96)
    
    # 2. Decisão de Gols (Baseado na média da liga + tendência dos times)
    tendencia_gols = (c['over_tendency'] + f['over_tendency'] + (l['media_gols']/4)) / 3
    if tendencia_gols > 0.75:
        return "OVER 2.5 GOLS", random.randint(90, 98)
    
    # 3. Decisão de Cantos
    if l['corners_avg'] > 10.0:
        return f"OVER {l['corners_avg'] - 1} CANTOS", random.randint(87, 94)
    
    return "OVER 1.5 GOLS", random.randint(92, 99)

def executar_jarvis():
    print("Processando inteligência de mercado...")
    # Jogos que o robô vai analisar hoje
    confrontos = [
        ["INGLATERRA", "PREMIER", "Man City", "Luton"],
        ["EUROPA", "CHAMPIONS", "Real Madrid", "Man City"],
        ["EUROPA", "CHAMPIONS", "Arsenal", "Bayern Munchen"],
        ["BRASIL", "SÉRIE A", "Flamengo", "Palmeiras"],
        ["BRASIL", "SÉRIE A", "Vasco", "Corinthians"],
        ["ESPANHA", "LA LIGA", "Barcelona", "PSG"],
        ["ALEMANHA", "BUNDESLIGA", "Bayern Munchen", "Dortmund"],
    ]
    
    data_final = []
    for pais, liga, casa, fora in confrontos:
        mercado, confia = calcular_palpite_ia(casa, fora, liga)
        data_final.append([pais, liga, casa, fora, mercado, confia])
        
    df = pd.DataFrame(data_final, columns=['PAÍS', 'GRUPO', 'TIME_CASA', 'TIME_FORA', 'MERCADO', 'CONFIDANÇA'])
    df.to_csv('data/database_diario.csv', index=False)
    print("✅ Bilhete atualizado com lógica de Ligas e Fator Casa.")

if __name__ == "__main__":
    executar_jarvis()
