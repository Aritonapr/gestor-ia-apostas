import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def capturar_jogos():
    print(f"Iniciando busca profunda: {datetime.now()}")
    jogos_reais = []
    
    try:
        # Mudando para a versão mobile ou simplificada que é mais fácil de ler
        url = "https://www.ogol.com.br/jogos_vivos.php"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # O OGol organiza jogos em tabelas com a classe 'zz_zz_zz' ou dentro de 'box_jogos'
        tabela = soup.find('div', id='page_main')
        linhas = tabela.find_all('tr') if tabela else []

        for linha in linhas:
            try:
                # Procura o placar (ex: 1-0 ou 2-2)
                res = linha.find('td', class_='result')
                if res and '-' in res.text:
                    times = linha.find_all('td', class_='parent')
                    minuto = linha.find('td', class_='minute')
                    
                    if len(times) >= 2:
                        home = times[0].get_text(strip=True)
                        away = times[1].get_text(strip=True)
                        placar = res.get_text(strip=True).split('-')
                        min_text = minuto.get_text(strip=True).replace("'", "") if minuto else "0"

                        jogos_reais.append({
                            "DATA": datetime.now().strftime('%Y-%m-%d'),
                            "HOME": home,
                            "AWAY": away,
                            "PLACAR_HOME": placar[0],
                            "PLACAR_AWAY": placar[1],
                            "MINUTO": min_text,
                            "AP1": "65" # Valor de teste para o gráfico subir
                        })
            except:
                continue

    except Exception as e:
        print(f"Erro: {e}")

    # Força a criação do arquivo mesmo se a lista for pequena
    df = pd.DataFrame(jogos_reais if jogos_reais else [], 
                      columns=["DATA", "HOME", "AWAY", "PLACAR_HOME", "PLACAR_AWAY", "MINUTO", "AP1"])
    
    df.to_csv('base_jogos_jarvis.csv', index=False)
    print(f"Finalizado! {len(jogos_reais)} jogos salvos no CSV.")

if __name__ == "__main__":
    capturar_jogos()
