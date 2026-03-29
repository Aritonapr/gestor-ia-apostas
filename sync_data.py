import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

def calcular_confianca_jarvis(time_casa, df_hist):
    conf = 72.0
    if df_hist is not None:
        filtro = df_hist[df_hist['Casa'].str.contains(str(time_casa)[:5], case=False, na=False)]
        if not filtro.empty:
            taxa = (len(filtro[filtro['Resultado'] == 'H']) / len(filtro)) * 100
            conf = round(taxa + 10, 1)
    return f"{min(conf, 98.4)}%"

def sync():
    print("🤖 JARVIS v62.0 | Iniciando Captura em Tempo Real...")
    
    path_hist = "data/historico_5_temporadas.csv"
    df_hist = pd.read_csv(path_hist) if os.path.exists(path_hist) else None

    # NOVO ALVO: Placar de Futebol (Leve e sem bloqueios)
    url = "https://www.placardefutebol.com.br/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Encontra os blocos de jogos
        jogos = soup.find_all('div', class_='match-card')
        
        lista_final = []
        
        for jogo in jogos:
            try:
                status = jogo.find('span', class_='status-name').text.strip()
                times = jogo.find_all('span', class_='team-name')
                casa = times[0].text.strip()
                fora = times[1].text.strip()
                liga = jogo.find('div', class_='league-name').text.strip() if jogo.find('div', class_='league-name') else "Geral"

                conf = calcular_confianca_jarvis(casa, df_hist)
                
                lista_final.append({
                    "STATUS": status,
                    "LIGA": liga,
                    "CASA": casa,
                    "FORA": fora,
                    "GOLS": "OVER 1.5",
                    "CONF": conf,
                    "CANTOS": "9.5+",
                    "CHUTES": "10+",
                    "DEFESAS": "6+",
                    "TMETA": "14+"
                })
            except: continue

        if lista_final:
            df = pd.DataFrame(lista_final)
            if not os.path.exists('data'): os.makedirs('data')
            df.to_csv("data/database_diario.csv", index=False)
            print(f"✅ SUCESSO: {len(df)} jogos reais capturados agora!")
        else:
            print("⚠️ Nenhum jogo encontrado no momento.")

    except Exception as e:
        print(f"❌ ERRO: {e}")

if __name__ == "__main__":
    sync()
