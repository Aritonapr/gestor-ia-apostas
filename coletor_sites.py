import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

def capturar_jogos():
    print(f"Iniciando captura de jogos: {datetime.now()}")
    jogos_reais = []
    
    try:
        # FONTE: OGOL (Link direto para jogos ao vivo)
        url = "https://www.ogol.com.br/jogos_vivos.php"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Procura as linhas de jogos na tabela do OGol
        jogos_html = soup.find_all('tr', class_='zz_zz_zz')
        
        for item in jogos_html:
            try:
                times = item.find_all('td', class_='parent')
                res_element = item.find('td', class_='result')
                placar = res_element.text.split('-') if res_element else ["0", "0"]
                minuto = item.find('td', class_='minute').text.replace("'", "") if item.find('td', class_='minute') else "0"
                
                jogos_reais.append({
                    "DATA": datetime.now().strftime('%Y-%m-%d'),
                    "HOME": times[0].text.strip(),
                    "AWAY": times[1].text.strip(),
                    "PLACAR_HOME": placar[0].strip(),
                    "PLACAR_AWAY": placar[1].strip(),
                    "MINUTO": minuto,
                    "AP1": "55" # Valor inicial de pressão
                })
            except Exception as e:
                continue
                
    except Exception as e:
        print(f"Erro na raspagem: {e}")

    # --- O PULO DO GATO ---
    # Se encontrou jogos, salva. Se não encontrou nada, cria um arquivo vazio estruturado
    # para o GitHub não dar erro de 'arquivo não encontrado'
    if not jogos_reais:
        print("Nenhum jogo ao vivo agora. Criando arquivo de segurança...")
        df = pd.DataFrame(columns=["DATA", "HOME", "AWAY", "PLACAR_HOME", "PLACAR_AWAY", "MINUTO", "AP1"])
    else:
        df = pd.DataFrame(jogos_reais)
        print(f"Sucesso! {len(jogos_reais)} jogos encontrados.")

    df.to_csv('base_jogos_jarvis.csv', index=False)

if __name__ == "__main__":
    capturar_jogos()
