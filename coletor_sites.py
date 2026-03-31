import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def capturar_jogos():
    print(f"Iniciando busca no BeSoccer: {datetime.now()}")
    jogos_reais = []
    
    try:
        # BeSoccer é excelente para raspagem rápida
        url = "https://pt.besoccer.com/livescore"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Procura os blocos de jogos
        partidas = soup.find_all('a', class_='match-link')
        
        for p in partidas:
            try:
                # Extração de nomes e placar
                home = p.find('div', class_='team-name').text.strip()
                away = p.find_all('div', class_='team-name')[1].text.strip()
                placar = p.find('div', class_='marker').text.strip().split('-')
                minuto = p.find('div', class_='status-match').text.strip().replace("'", "")
                
                # Se houver um número no minuto, é porque está rolando
                if minuto.isdigit() or minuto == "45+" or minuto == "90+":
                    jogos_reais.append({
                        "DATA": datetime.now().strftime('%Y-%m-%d'),
                        "HOME": home,
                        "AWAY": away,
                        "PLACAR_HOME": placar[0].strip(),
                        "PLACAR_AWAY": placar[1].strip(),
                        "MINUTO": minuto,
                        "AP1": "70" # Pressão base para o Jarvis
                    })
            except:
                continue

    except Exception as e:
        print(f"Erro na captura: {e}")

    # Salva o arquivo. Se não achar nada, cria 2 jogos fictícios de SINAL apenas para você ver que o código rodou.
    if not jogos_reais:
        print("Nenhum ao vivo no BeSoccer. Criando jogos de sinalização...")
        jogos_reais = [
            {"DATA": "2026-03-30", "HOME": "SINALIZADOR", "AWAY": "JARVIS", "PLACAR_HOME": "1", "PLACAR_AWAY": "0", "MINUTO": "1", "AP1": "50"}
        ]

    df = pd.DataFrame(jogos_reais)
    df.to_csv('base_jogos_jarvis.csv', index=False)
    print(f"Finalizado! {len(jogos_reais)} jogos processados.")

if __name__ == "__main__":
    capturar_jogos()
