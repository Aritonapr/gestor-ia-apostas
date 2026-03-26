import pandas as pd
import os

# Garante que a pasta 'data' existe
if not os.path.exists('data'):
    os.makedirs('data')

def buscar_jogos_reais():
    print("Iniciando busca de jogos do dia...")
    
    # Criando a lista de jogos (Este robô pode ser expandido para ler APIs)
    jogos = [
        ["BRASIL", "SÉRIE A", "Flamengo", "Palmeiras"],
        ["BRASIL", "SÉRIE A", "São Paulo", "Corinthians"],
        ["INGLATERRA", "PREMIER", "Man City", "Arsenal"],
        ["INGLATERRA", "PREMIER", "Liverpool", "Chelsea"],
        ["ESPANHA", "LA LIGA", "Real Madrid", "Barcelona"],
        ["ITÁLIA", "SERIE A", "Inter Milan", "Juventus"],
        ["BRASIL", "SERIE B", "Santos", "Sport"],
        ["BRASIL", "SÉRIE A", "Vasco", "Botafogo"],
        ["BRASIL", "SÉRIE A", "Grêmio", "Internacional"],
        ["ALEMANHA", "BUNDESLIGA", "Bayern", "Dortmund"],
        ["FRANÇA", "LIGUE 1", "PSG", "Monaco"],
        ["BRASIL", "SÉRIE A", "Bahia", "Fortaleza"],
        ["BRASIL", "SÉRIE A", "Athletico-PR", "Cruzeiro"],
        ["BRASIL", "SÉRIE A", "Fluminense", "Atlético-MG"],
        ["PORTUGAL", "LIGA", "Benfica", "Porto"],
        ["HOLANDA", "EREDIVISIE", "Ajax", "PSV"],
        ["ARGENTINA", "LIGA", "River Plate", "Boca Juniors"],
        ["EUA", "MLS", "Inter Miami", "LA Galaxy"],
        ["EUROPA", "CHAMPIONS", "Real Madrid", "Man City"],
        ["EUROPA", "CHAMPIONS", "Arsenal", "Bayern"]
    ]
    
    df = pd.DataFrame(jogos, columns=['PAÍS', 'GRUPO', 'TIME_CASA', 'TIME_FORA'])
    
    # Salva o arquivo que o seu bot lê
    df.to_csv('data/database_diario.csv', index=False)
    print("Sucesso: 20 jogos salvos em data/database_diario.csv")

if __name__ == "__main__":
    buscar_jogos_reais()
