import pandas as pd
import os
import random

# CONFIGURAÇÃO DO DIRETÓRIO
if not os.path.exists('data'):
    os.makedirs('data')

def buscar_jogos_ia():
    print("Iniciando coleta de jogos via IA...")
    
    # Este é um simulador de coleta. Em um cenário avançado, 
    # aqui conectaríamos com APIs de futebol (API-Football, etc).
    jogos = [
        ["BRASIL", "SERIE A", "Flamengo", "Palmeiras"],
        ["BRASIL", "SERIE A", "São Paulo", "Corinthians"],
        ["INGLATERRA", "PREMIER", "Man City", "Arsenal"],
        ["INGLATERRA", "PREMIER", "Liverpool", "Chelsea"],
        ["ESPANHA", "LA LIGA", "Real Madrid", "Barcelona"],
        ["ITÁLIA", "SERIE A", "Inter Milan", "Juventus"],
        ["BRASIL", "SERIE B", "Santos", "Sport"],
        ["BRASIL", "SERIE A", "Vasco", "Botafogo"],
        ["BRASIL", "SERIE A", "Grêmio", "Internacional"],
        ["INGLATERRA", "PREMIER", "Tottenham", "Aston Villa"],
        ["ALEMANHA", "BUNDESLIGA", "Bayern", "Dortmund"],
        ["FRANÇA", "LIGUE 1", "PSG", "Monaco"],
        ["BRASIL", "SERIE A", "Bahia", "Fortaleza"],
        ["BRASIL", "SERIE A", "Athletico-PR", "Cruzeiro"],
        ["BRASIL", "SERIE A", "Fluminense", "Atlético-MG"],
        ["BRASIL", "COPA", "Cuiabá", "Coritiba"],
        ["PORTUGAL", "LIGA", "Benfica", "Porto"],
        ["HOLANDA", "EREDIVISIE", "Ajax", "PSV"],
        ["ARGENTINA", "LIGA", "River Plate", "Boca Juniors"],
        ["EUA", "MLS", "Inter Miami", "LA Galaxy"]
    ]
    
    df = pd.DataFrame(jogos, columns=['PAÍS', 'GRUPO', 'TIME_CASA', 'TIME_FORA'])
    
    # Salva no arquivo que o app.py lê
    df.to_csv('data/database_diario.csv', index=False)
    print("Sucesso! 20 jogos carregados em data/database_diario.csv")

if __name__ == "__main__":
    buscar_jogos_ia()
