import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def capturar_jogos():
    print(f"Iniciando captura de jogos: {datetime.now()}")
    jogos_reais = []
    
    try:
        # FONTE: OGOL (Uma das mais estáveis para scraping)
        url = "https://www.ogol.com.br/jogos_vivos.php"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Procura a tabela de jogos ao vivo
        jogos_html = soup.find_all('tr', class_='zz_zz_zz') # Classe comum no OGol para linhas de jogos
        
        for item in jogos_html:
            try:
                times = item.find_all('td', class_='parent')
                placar = item.find('td', class_='result').text.split('-')
                minuto = item.find('td', class_='minute').text.replace("'", "")
                
                jogos_reais.append({
                    "DATA": datetime.now().strftime('%Y-%m-%d'),
                    "HOME": times[0].text.strip(),
                    "AWAY": times[1].text.strip(),
                    "PLACAR_HOME": placar[0].strip(),
                    "PLACAR_AWAY": placar[1].strip(),
                    "MINUTO": minuto,
                    "AP1": "50" # Valor base para o Jarvis calcular depois
                })
            except:
                continue
                
    except Exception as e:
        print(f"Erro na captura: {e}")

    # Salva ou atualiza o arquivo que o Jarvis lê
    if jogos_reais:
        df = pd.DataFrame(jogos_reais)
        df.to_csv('base_jogos_jarvis.csv', index=False)
        print(f"Sucesso! {len(jogos_reais)} jogos sincronizados.")
    else:
        print("Nenhum jogo ao vivo encontrado no momento.")

if __name__ == "__main__":
    capturar_jogos()
