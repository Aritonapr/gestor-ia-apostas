import pandas as pd
import requests
from datetime import datetime
import os
import random

# ==============================================================================
# PROTOCOLO JARVIS - COLETOR DE DADOS GRATUITO (SEM API)
# VERSÃO: 1.0 - 2026
# FUNÇÃO: Gerar database_diario.csv sem custo de API
# ==============================================================================

def coletar_dados_gratuitos():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando coleta de dados...")

    # Lista de times de elite para garantir que o sistema sempre tenha dados
    times_casa = ["Real Madrid", "Man City", "Bayern Munich", "Arsenal", "Barcelona", "Flamengo", "Palmeiras", "Liverpool"]
    times_fora = ["Chelsea", "Juventus", "Dortmund", "PSG", "Inter Milan", "São Paulo", "Corinthians", "Benfica"]
    ligas = ["UEFA Champions League", "Premier League", "Brasileirão Série A", "La Liga", "Bundesliga"]

    dados_jogos = []

    # Simulando a raspagem de 20 jogos (Este bloco será expandido conforme o site alvo)
    for i in range(20):
        casa = random.choice(times_casa)
        fora = random.choice(times_fora)
        while fora == casa:
            fora = random.choice(times_fora)
            
        liga = random.choice(ligas)
        confianca = random.randint(65, 98)
        
        # Estrutura de colunas exata que o seu app.py espera
        jogo = {
            "CASA": casa,
            "FORA": fora,
            "LIGA": liga,
            "CONFIANCA": f"{confianca}%",
            "CONF_NUM": confianca,
            "VENCEDOR": "FAVORITO" if confianca > 80 else "PROBABILISTICO",
            "GOLS": "OVER 1.5" if confianca > 75 else "OVER 0.5",
            "CANTOS": f"{random.randint(8, 11)}.5+",
            "CARTÕES": f"{random.randint(3, 5)}.5+",
            "CHUTES": f"{random.randint(7, 14)}+",
            "DEFESAS": f"{random.randint(4, 9)}+",
            "DATA": datetime.now().strftime("%d/%m/%Y")
        }
        dados_jogos.append(jogo)

    # Criando o DataFrame (tabela)
    df = pd.DataFrame(dados_jogos)

    # Garantindo que a pasta 'data' existe
    if not os.path.exists('data'):
        os.makedirs('data')

    # Salvando o arquivo que o Jarvis (app.py) lê
    path_csv = "data/database_diario.csv"
    df.to_csv(path_csv, index=False)
    
    print(f"✅ Sucesso! {len(df)} jogos salvos em {path_csv}")

if __name__ == "__main__":
    coletar_dados_gratuitos()
