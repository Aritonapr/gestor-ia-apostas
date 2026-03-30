import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO JARVIS v62.8 - CALIBRAGEM 29/03/2026]
# ==============================================================================

def calcular_confianca_jarvis(time_casa, df_hist):
    conf = 72.0
    if df_hist is not None:
        try:
            # Pega as 4 primeiras letras do time para cruzar o histórico
            termo = str(time_casa)[:4]
            filtro = df_hist[df_hist['Casa'].str.contains(termo, case=False, na=False)]
            if not filtro.empty:
                taxa = (len(filtro[filtro['Resultado'] == 'H']) / len(filtro)) * 100
                conf = round(taxa + 6, 1)
        except: pass
    return f"{min(max(conf, 60.0), 98.4)}%"

def sync():
    now_full = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(f"🤖 JARVIS v62.8 | DATA DE OPERAÇÃO: {now_full}")

    path_hist = "data/historico_5_temporadas.csv"
    df_hist = pd.read_csv(path_hist) if os.path.exists(path_hist) else None

    # URL ESTÁVEL DE 2026
    url = "https://www.ogol.com.br/jogos_dia.php"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    try:
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')

        lista_jogos = []

        # O OGOL organiza os jogos em linhas de tabelas de classe 'row'
        rows = soup.find_all('tr')

        current_league = "FUTEBOL PROFISSIONAL"

        for row in rows:
            # Pega a liga se a linha for um cabeçalho
            league_header = row.find('th', class_='league')
            if league_header:
                current_league = league_header.get_text(strip=True)

            # Pega os jogos
            cols = row.find_all('td')
            if len(cols) >= 4:
                try:
                    time_casa = cols[1].get_text(strip=True)
                    time_fora = cols[3].get_text(strip=True)
                    status = cols[0].get_text(strip=True) # Ex: 21:30, AO VIVO, Encerrado

                    if time_casa and time_fora:
                        conf = calcular_confianca_jarvis(time_casa, df_hist)
                        lista_jogos.append({
                            "STATUS": status.upper(),
                            "LIGA": current_league.upper(),
                            "CASA": time_casa,
                            "FORA": time_fora,
                            "GOLS": "OVER 1.5",
                            "CONF": conf,
                            "CANTOS": "9.5+",
                            "CHUTES": "10+",
                            "DEFESAS": "6+",
                            "TMETA": "14+",
                            "SYNC": now_full
                        })
                except:
                    continue

        if lista_jogos:
            df = pd.DataFrame(lista_jogos).drop_duplicates(subset=['CASA', 'FORA'])
            if not os.path.exists('data'): os.makedirs('data')
            df.to_csv("data/database_diario.csv", index=False)
            print(f"✅ SUCESSO! {len(df)} jogos de 29/03/2026 capturados!")
        else:
            print("⚠️ AVISO: Nenhum jogo encontrado. Limpando cache...")
            df_vazio = pd.DataFrame(columns=["STATUS","LIGA","CASA","FORA","GOLS","CONF","CANTOS","CHUTES","DEFESAS","TMETA","SYNC"])
            df_vazio.to_csv("data/database_diario.csv", index=False)

    except Exception as e:
        print(f"❌ ERRO CRÍTICO NO MOTOR: {e}")

if __name__ == "__main__":
    sync()
